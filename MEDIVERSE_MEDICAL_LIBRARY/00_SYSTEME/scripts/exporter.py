#!/usr/bin/env python3
"""Exports de la bibliothèque (§13) : ODT + PDF des dossiers/fiches, livrets QCM et cas cliniques par spécialité,
tableaux ODS des catalogues. Ne régénère que ce qui a changé (manifeste d'empreintes).

Usage : python3 00_SYSTEME/scripts/exporter.py [--force] [--sans-pdf]
Prérequis : pandoc, LibreOffice (soffice), openpyxl. Lancer indexer.py avant.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, charger_json, dossier_specialite, ecrire_json, journaliser, lister, maintenant, specialite_par_code  # noqa: E402

MANIFESTE = RACINE / "00_SYSTEME/journaux/manifeste_exports.json"
RE_FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
ENTETE_GENERE = "<!-- Fichier GÉNÉRÉ par 00_SYSTEME/scripts/exporter.py à partir des données JSON : ne pas éditer à la main. -->\n\n"


def h(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def soffice(fichiers: list[Path], fmt: str) -> None:
    par_dossier = defaultdict(list)
    for f in fichiers:
        par_dossier[f.parent].append(f)
    for d, fs in par_dossier.items():
        for i in range(0, len(fs), 20):
            subprocess.run(["soffice", "--headless", "--convert-to", fmt, "--outdir", str(d), *map(str, fs[i:i + 20])],
                           capture_output=True, text=True, timeout=900)


CSS = RACINE / "00_SYSTEME/modeles/style_pdf.css"
JS_PDF = RACINE / "00_SYSTEME/scripts/html_vers_pdf.js"


def pdf_chromium(odts: list[Path]) -> None:
    """PDF via HTML pandoc + Chromium (tableaux bordés, pagination). Repli LibreOffice si Chromium échoue."""
    htmls = []
    for odt in odts:
        src = odt.with_suffix(".md")
        html = odt.with_suffix(".html")
        try:
            corps, meta = preparer(src)
            with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as t:
                t.write(corps); tmp = t.name
            subprocess.run(["pandoc", tmp, "-f", "markdown+pipe_tables+grid_tables-yaml_metadata_block", "-s", "--embed-resources", "--toc", "--toc-depth=2",
                            "-c", str(CSS), "-o", str(html), "-M", "lang=fr", *meta], check=True, capture_output=True, text=True)
            Path(tmp).unlink()
            htmls.append(html)
        except subprocess.CalledProcessError:
            pass
    if htmls:
        r = subprocess.run(["node", str(JS_PDF), *map(str, htmls)], capture_output=True, text=True, timeout=3600)
        if r.returncode != 0 or "ECHEC" in r.stderr:
            print(r.stderr[:500], file=sys.stderr)
    manquants = [o for o in odts if not o.with_suffix(".pdf").exists() or o.with_suffix(".pdf").stat().st_mtime < o.stat().st_mtime]
    if manquants:
        soffice(manquants, "pdf")
    for h_ in htmls:
        h_.unlink(missing_ok=True)


def preparer(md: Path) -> tuple[str, list[str]]:
    """Retourne (corps Markdown sans en-tête YAML, avec bandeau de métadonnées ; arguments -M pour pandoc)."""
    import yaml
    texte = md.read_text(encoding="utf-8")
    m = RE_FM.match(texte)
    fm, corps = {}, texte
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            fm = {}
        corps = texte[m.end():]
    if not fm:  # livrets générés : titre = premier H1
        h1 = re.search(r"^#\s+(.+)$", corps, re.M)
        titre = h1.group(1).strip() if h1 else md.stem
        corps = corps.replace(h1.group(0), "", 1) if h1 else corps
        return corps, ["-M", f"title={titre}", "-M", "subtitle=Bibliothèque médicale Mediverse"]
    titre = str(fm.get("titre") or md.stem)
    corps = re.sub(r"^\s*#\s+" + re.escape(titre) + r"\s*\n", "", corps, count=1)
    items = ", ".join(fm.get("items_residanat") or []) or "—"
    corps = (f"| Identifiant | Statut | Version | Items du résidanat | Révision |\n|---|---|---|---|---|\n"
             f"| {fm.get('id', '')} | {fm.get('statut', '')} | {fm.get('version', '')} | {items} | {fm.get('date_revision', '')} |\n\n") + corps
    return corps, ["-M", f"title={titre}", "-M", "subtitle=Bibliothèque médicale Mediverse — dossier pédagogique original",
                   "-M", f"author={fm.get('auteur', 'Mediverse')}", "-M", f"date={fm.get('date_revision', '')}"]


def md_vers_odt(md: Path, odt: Path) -> None:
    import yaml
    texte = md.read_text(encoding="utf-8")
    m = RE_FM.match(texte)
    fm, corps = {}, texte
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except Exception:
            fm = {}
        corps = texte[m.end():]
    titre = str(fm.get("titre") or md.stem)
    # le titre est porté par les métadonnées : retirer un éventuel H1 identique en tête
    corps = re.sub(r"^\s*#\s+" + re.escape(titre) + r"\s*\n", "", corps, count=1)
    if fm:
        items = ", ".join(fm.get("items_residanat") or []) or "—"
        corps = (f"| Identifiant | Statut | Version | Items du résidanat | Révision |\n|---|---|---|---|---|\n"
                 f"| {fm.get('id', '')} | {fm.get('statut', '')} | {fm.get('version', '')} | {items} | {fm.get('date_revision', '')} |\n\n") + corps
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as t:
        t.write(corps)
        tmp = t.name
    sous_titre = "Bibliothèque médicale Mediverse — dossier pédagogique original"
    subprocess.run(["pandoc", tmp, "-f", "markdown+pipe_tables+grid_tables-yaml_metadata_block", "-o", str(odt), "--toc", "--toc-depth=2",
                    "-M", f"title={titre}", "-M", f"subtitle={sous_titre}",
                    "-M", f"author={fm.get('auteur', 'Mediverse')}", "-M", f"date={fm.get('date_revision', '')}"],
                   check=True, capture_output=True, text=True)
    Path(tmp).unlink()


def livret_qcm(code: str, nom: str, qs: list[dict]) -> str:
    qs = sorted(qs, key=lambda q: q["id"])
    l = [ENTETE_GENERE, f"# QCM d'entraînement — {nom}", "",
         f"_{len(qs)} questions originales Mediverse (non issues d'annales). Statut : à auditer._", "", "## Questions", ""]
    for n, q in enumerate(qs, 1):
        l += [f"### {n}. {q.get('theme', '')} `{q['id']}`", "", q.get("enonce", ""), ""]
        for k, v in (q.get("propositions") or {}).items():
            l.append(f"- **{k}.** {v}")
        l.append("")
    l += ["## Corrigé commenté", ""]
    for n, q in enumerate(qs, 1):
        l += [f"### {n}. `{q['id']}` — réponse(s) : **{', '.join(q.get('reponses_correctes') or [])}**", "",
              q.get("explication_generale", ""), ""]
        for k, v in (q.get("explications_par_proposition") or {}).items():
            l.append(f"- **{k}** : {v}")
        if q.get("piege_classique"):
            l += ["", f"> Piège classique : {q['piege_classique']}"]
        src = "; ".join(s.get("reference", "") for s in q.get("sources") or [] if isinstance(s, dict))
        if src:
            l += ["", f"_Sources : {src}_"]
        l.append("")
    return "\n".join(l)


RUBRIQUES = [("identite", "Identité (scénario fictif)"), ("motif_consultation", "Motif de consultation"), ("antecedents", "Antécédents"),
             ("symptomes", "Symptômes"), ("examen_clinique", "Examen clinique"), ("biologie", "Résultats biologiques"),
             ("imagerie", "Imagerie"), ("hypotheses_diagnostiques", "Hypothèses diagnostiques"),
             ("diagnostics_differentiels", "Diagnostics différentiels"), ("examens_a_demander", "Examens à demander"),
             ("diagnostic_final", "Diagnostic final"), ("traitement", "Traitement"), ("surveillance", "Surveillance"),
             ("evolution", "Évolution"), ("explication_pedagogique", "Explication pédagogique")]


def livret_cas(nom: str, cas: list[dict]) -> str:
    l = [ENTETE_GENERE, f"# Cas cliniques — {nom}", "", f"_{len(cas)} cas originaux (scénarios fictifs). Statut : à auditer._", ""]
    for c in sorted(cas, key=lambda x: x["id"]):
        l += [f"## {c.get('titre', '')} `{c['id']}`", "", f"**Niveau** : {c.get('niveau', '')} — **Items** : {', '.join(c.get('items_residanat') or []) or '—'}", ""]
        for k, lib in RUBRIQUES:
            v = c.get(k)
            if not v:
                continue
            l += [f"### {lib}", ""]
            l += ([f"- {x}" for x in v] if isinstance(v, list) else [str(v)])
            l.append("")
        if c.get("questions"):
            l += ["### Questions", ""]
            for qq in c["questions"]:
                if isinstance(qq, dict):
                    l += [f"- **Q.** {qq.get('question', '')}", f"  - **R.** {qq.get('reponse', '')}"]
            l.append("")
        src = "; ".join(s.get("reference", "") for s in c.get("sources") or [] if isinstance(s, dict))
        if src:
            l += [f"_Sources : {src}_", ""]
    return "\n".join(l)


def vers_ods(lignes: list[dict], colonnes: list[str], cible: Path, feuille: str) -> Path:
    from openpyxl import Workbook
    from openpyxl.styles import Font
    wb = Workbook(); ws = wb.active; ws.title = feuille[:31]
    ws.append(colonnes)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in lignes:
        ws.append([(json.dumps(r.get(k), ensure_ascii=False) if isinstance(r.get(k), (list, dict)) else r.get(k)) for k in colonnes])
    ws.freeze_panes = "A2"
    xlsx = cible.with_suffix(".xlsx")
    wb.save(xlsx)
    return xlsx


def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--force", action="store_true"); ap.add_argument("--sans-pdf", action="store_true")
    a = ap.parse_args()
    man = charger_json(MANIFESTE, {})
    a_pdf, n_odt = [], 0
    spe = specialite_par_code()

    # 1) livrets générés (QCM, cas) -> Markdown dans chaque spécialité
    qcm = charger_json(RACINE / "21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/banque_qcm.json", {}).get("qcm", [])
    cas = charger_json(RACINE / "20_CAS_CLINIQUES/banque_cas_cliniques.json", {}).get("cas", [])
    generes = []
    for code, sp in spe.items():
        qs = [q for q in qcm if q.get("specialite") == code]
        if qs:
            p = dossier_specialite(sp) / "06_QCM" / f"LIVRET_QCM_{code}.md"
            p.write_text(livret_qcm(code, sp["nom"], qs), encoding="utf-8"); generes.append(p)
        cs = [c for c in cas if c.get("specialite") == code]
        if cs:
            p = dossier_specialite(sp) / "05_CAS_CLINIQUES" / f"LIVRET_CAS_{code}.md"
            p.write_text(livret_cas(sp["nom"], cs), encoding="utf-8"); generes.append(p)

    # 2) Markdown -> ODT (+ PDF)
    sources = lister("**/02_DOSSIERS_PEDAGOGIQUES/*.md") + lister("**/03_FICHES_REVISION/*.md") + generes
    for md in sources:
        cle = str(md.relative_to(RACINE))
        emp = h(md.read_text(encoding="utf-8"))
        odt, pdf = md.with_suffix(".odt"), md.with_suffix(".pdf")
        if not a.force and man.get(cle) == emp and odt.exists() and (a.sans_pdf or pdf.exists()):
            continue
        try:
            if md in generes:
                subprocess.run(["pandoc", str(md), "-o", str(odt), "--toc", "--toc-depth=1"], check=True, capture_output=True)
            else:
                md_vers_odt(md, odt)
            n_odt += 1
            a_pdf.append(odt)
            man[cle] = emp
        except subprocess.CalledProcessError as e:
            journaliser("exporteur", "echec_export_odt", cle, {"erreur": (e.stderr or b"")[:300].decode("utf-8", "ignore") if isinstance(e.stderr, bytes) else str(e.stderr)[:300]})
            print(f"ECHEC ODT {cle}", file=sys.stderr)
    if a_pdf and not a.sans_pdf:
        pdf_chromium(a_pdf)

    # 3) tableaux ODS
    tab = []
    def t(chemin_json, cle, colonnes, feuille):
        d = charger_json(RACINE / chemin_json, None)
        if d and d.get(cle):
            tab.append(vers_ods(d[cle], colonnes, (RACINE / chemin_json).with_suffix(".ods"), feuille))
    t("24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/catalogue_ouvrages.json", "ouvrages",
      ["id", "titre", "auteurs_editeurs", "edition", "annee", "editeur_commercial", "isbn", "langue", "specialites", "origine_priorite",
       "traduction_francaise", "statut_acquisition", "voies_acces_legales", "verification", "notes"], "Ouvrages")
    t("18_RECOMMANDATIONS/00_CATALOGUE/catalogue_recommandations.json", "recommandations",
      ["id", "titre", "organisme", "zone", "date_publication", "date_mise_a_jour", "statut", "remplacee_par", "domaine", "items_residanat",
       "population", "systeme_gradation", "points_cles", "reference_bibliographique", "doi", "url", "acces", "licence", "document_acquis", "verification"], "Recommandations")
    t("21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/banque_qcm.json", "qcm",
      ["id", "format", "specialite", "items_residanat", "theme", "difficulte", "niveau", "enonce", "propositions", "reponses_correctes",
       "explication_generale", "explications_par_proposition", "piege_classique", "origine", "annale", "sources", "statut", "auteur", "date_creation"], "QCM")
    t("20_CAS_CLINIQUES/banque_cas_cliniques.json", "cas",
      ["id", "titre", "niveau", "specialite", "items_residanat", *[k for k, _ in RUBRIQUES], "sources", "statut"], "Cas cliniques")
    t("22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/referentiel_pathologies.json", "pathologies",
      ["id", "nom_fr", "nom_en", "synonymes", "cim10", "specialite", "sous_specialite", "categories", "maladie_rare", "priorite",
       "items_residanat", "symptomes", "signes_cliniques", "examens_cles", "traitements_cles", "pathologies_liees", "dossier", "statut"], "Pathologies")
    t("23_GLOSSAIRES/FR_EN_AR/glossaire_fr_en_ar.json", "termes",
      ["id", "fr", "en", "ar", "ar_variantes", "definition_fr", "categorie", "specialites", "statut_ar"], "Glossaire")
    t("16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json", "items",
      ["id", "partie", "module_programme", "numero", "intitule", "specialites", "dossiers", "qcm", "cas_cliniques"], "Programme résidanat")
    t("00_SYSTEME/registre_acquisitions.json", "documents",
      ["id", "titre", "emetteur", "date_publication", "type", "langue", "specialites", "url_source", "date_acquisition", "licence",
       "redistribution", "emplacement", "sha256", "taille_octets", "pages", "texte_extractible", "ocr_requis", "notes"], "Registre")
    tb = charger_json(RACINE / "25_INDEX_GENERAL/tableau_de_bord.json", None)
    if tb:
        tab.append(vers_ods(tb["specialites"], list(tb["specialites"][0].keys()), RACINE / "25_INDEX_GENERAL/tableau_de_bord.ods", "Couverture"))
    if tab:
        soffice(tab, "ods")
        for x in tab:
            x.unlink(missing_ok=True)

    ecrire_json(MANIFESTE, man, agent="exporteur", sauvegarde=False)
    journaliser("exporteur", "exports", "bibliotheque", {"odt": n_odt, "pdf": 0 if a.sans_pdf else len(a_pdf), "ods": len(tab)})
    print(f"Exports : {n_odt} ODT, {0 if a.sans_pdf else len(a_pdf)} PDF, {len(tab)} ODS ({maintenant()})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
