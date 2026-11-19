#!/usr/bin/env python3
"""Tableau de bord global (§17) + statut par spécialité (README de chaque spécialité).

Couverture d'une spécialité (deux mesures, jamais confondues) :
  * brute   = items du résidanat rattachés à la spécialité ayant au moins un dossier pédagogique (quel que soit son statut) ;
  * auditée = items ayant au moins un dossier au statut `audite_valide` ou `valide_enseignant`.
Une spécialité n'est jamais déclarée « terminée » : seule la couverture auditée compte (§17, §18).

Usage : python3 00_SYSTEME/scripts/tableau_de_bord.py   (lancer indexer.py avant)
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, charger_json, dossier_specialite, ecrire_json, journaliser, maintenant, specialites  # noqa: E402

AUDITES = {"audite_valide", "valide_enseignant"}


def pct(a: int, b: int) -> str:
    return f"{(100 * a / b):.0f} %" if b else "—"


def main() -> int:
    c = lambda p: charger_json(RACINE / p, {})  # noqa: E731
    ouv = c("24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/catalogue_ouvrages.json").get("ouvrages", [])
    rec = c("18_RECOMMANDATIONS/00_CATALOGUE/catalogue_recommandations.json").get("recommandations", [])
    qcm = c("21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/banque_qcm.json").get("qcm", [])
    cas = c("20_CAS_CLINIQUES/banque_cas_cliniques.json").get("cas", [])
    pat = c("22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/referentiel_pathologies.json").get("pathologies", [])
    glo = c("23_GLOSSAIRES/FR_EN_AR/glossaire_fr_en_ar.json").get("termes", [])
    reg = c("00_SYSTEME/registre_acquisitions.json").get("documents", [])
    inv = c("00_SYSTEME/journaux/inventaire_dossiers.json")
    dossiers, fiches = inv.get("dossiers", []), inv.get("fiches", [])
    prog = c("16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json").get("items", [])
    trad = list(RACINE.glob("**/TRADUCTIONS/**/*.md"))
    echecs = []
    jpath = RACINE / "00_SYSTEME/journaux/operations.jsonl"
    if jpath.exists():
        for l in jpath.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(l)
            except Exception:
                continue
            if e.get("action") == "echec_acquisition":
                echecs.append(e)

    acquis = [o for o in ouv if str(o.get("statut_acquisition", "")).startswith(("acquis", "fourni"))]
    g = {
        "date": maintenant(),
        "livres_identifies": len(ouv),
        "livres_verifies": sum(1 for o in ouv if (o.get("verification") or {}).get("statut") == "verifie"),
        "livres_acquis": len(acquis),
        "documents_pdf_complets": sum(1 for d in reg if d.get("verification") == "integrite_pdf_ok"),
        "documents_pdf_redistribuables": sum(1 for d in reg if d.get("redistribution") == "redistribuable"),
        "documents_pdf_locaux": sum(1 for d in reg if d.get("redistribution") == "local_uniquement"),
        "documents_scannes_sans_texte": sum(1 for d in reg if d.get("ocr_requis")),
        "documents_ocrises": sum(1 for d in reg if d.get("ocr_effectue")),
        "traductions": len(trad),
        "recommandations": len(rec),
        "recommandations_actuelles": sum(1 for r in rec if r.get("statut") in ("actuelle", "partiellement_mise_a_jour")),
        "recommandations_remplacees": sum(1 for r in rec if r.get("statut") in ("remplacee", "archive_historique")),
        "pathologies_referencees": len(pat),
        "pathologies_avec_dossier": sum(1 for p in pat if p.get("dossier")),
        "dossiers_pedagogiques": len(dossiers),
        "dossiers_audites": sum(1 for d in dossiers if d.get("statut") in AUDITES),
        "dossiers_audit_effectue": sum(1 for d in dossiers if d.get("statut") in AUDITES | {"audite_corrections_requises"}),
        "mots_dossiers": sum(d.get("mots", 0) for d in dossiers),
        "fiches_revision": len(fiches),
        "cas_cliniques": len(cas),
        "qcm": len(qcm),
        "termes_glossaire": len(glo),
        "items_residanat": len(prog),
        "items_residanat_couverts_brut": sum(1 for i in prog if i.get("dossiers")),
        "items_residanat_couverts_audites": sum(1 for i in prog if any(d["statut"] in AUDITES for d in i.get("dossiers", []))),
        "acquisitions_echouees": len(echecs),
    }
    g["ressources_manquantes"] = {
        "ouvrages_non_acquis": len(ouv) - len(acquis),
        "items_residanat_sans_dossier": len(prog) - g["items_residanat_couverts_brut"],
        "items_residanat_sans_qcm": sum(1 for i in prog if not i.get("qcm")),
        "acquisitions_echouees": len(echecs),
    }

    par = defaultdict(lambda: Counter())
    for i in prog:
        for s in i["specialites"]:
            par[s]["items"] += 1
            par[s]["items_couverts"] += 1 if i.get("dossiers") else 0
            par[s]["items_audites"] += 1 if any(d["statut"] in AUDITES for d in i.get("dossiers", [])) else 0
    for d in dossiers:
        par[d.get("specialite")]["dossiers"] += 1
        par[d.get("specialite")]["dossiers_audites"] += 1 if d.get("statut") in AUDITES else 0
    for q in qcm: par[q.get("specialite")]["qcm"] += 1
    for x in cas: par[x.get("specialite")]["cas"] += 1
    for p in pat: par[p.get("specialite")]["pathologies"] += 1
    for o in ouv:
        for s in o.get("specialites") or []: par[s]["ouvrages"] += 1
    for r in rec:
        for s in r.get("domaine") or []: par[s]["recommandations"] += 1

    lignes, tableau = [], []
    for sp in specialites():
        k = par[sp["code"]]
        ligne = {"n": sp["n"], "code": sp["code"], "specialite": sp["nom"], "items_residanat": k["items"],
                 "couverture_brute": pct(k["items_couverts"], k["items"]), "couverture_auditee": pct(k["items_audites"], k["items"]),
                 "dossiers": k["dossiers"], "dossiers_audites": k["dossiers_audites"], "qcm": k["qcm"], "cas": k["cas"],
                 "pathologies": k["pathologies"], "ouvrages": k["ouvrages"], "recommandations": k["recommandations"]}
        tableau.append(ligne)
        lignes.append(f"| {sp['n']} | {sp['nom']} | {k['items']} | {ligne['couverture_brute']} | {ligne['couverture_auditee']} | "
                      f"{k['dossiers']} ({k['dossiers_audites']}) | {k['qcm']} | {k['cas']} | {k['pathologies']} | {k['ouvrages']} | {k['recommandations']} |")
        # README de spécialité (régénéré : ne pas éditer à la main)
        base = dossier_specialite(sp)
        ds = [d for d in dossiers if d.get("specialite") == sp["code"]]
        its = [i for i in prog if sp["code"] in i["specialites"]]
        txt = [f"# {sp['n']:02d} — {sp['nom']} (`{sp['code']}`)", "",
               "> Fichier généré par `00_SYSTEME/scripts/tableau_de_bord.py` — ne pas éditer à la main.", "",
               f"**Sous-spécialités** : {', '.join(sp.get('sous', []))}", "",
               "## État", "",
               f"- Items du résidanat rattachés : **{k['items']}** — couverture brute {ligne['couverture_brute']}, auditée {ligne['couverture_auditee']}",
               f"- Dossiers pédagogiques : {k['dossiers']} (audités : {k['dossiers_audites']})",
               f"- QCM : {k['qcm']} — cas cliniques : {k['cas']} — pathologies référencées : {k['pathologies']}",
               f"- Ouvrages catalogués : {k['ouvrages']} — recommandations : {k['recommandations']}",
               "- **Statut : en construction** (aucune spécialité n'est déclarée terminée sans audit complet).", ""]
        if ds:
            txt += ["## Dossiers pédagogiques", "", "| ID | Titre | Statut | Mots |", "|---|---|---|---|"]
            txt += [f"| {d['id']} | [{d['titre']}]({Path(d['chemin']).relative_to(base.relative_to(RACINE)).as_posix()}) | {d['statut']} | {d['mots']} |" for d in ds]
            txt.append("")
        if its:
            txt += ["## Items du programme du résidanat", "", "| Item | Intitulé | Dossier | QCM | Cas |", "|---|---|---|---|---|"]
            txt += [f"| {i['id']} | {i['intitule'][:110]} | {', '.join(d['id'] for d in i.get('dossiers', [])) or '—'} | {i.get('qcm', 0)} | {i.get('cas_cliniques', 0)} |" for i in its]
            txt.append("")
        (base / "README.md").write_text("\n".join(txt), encoding="utf-8")

    md = ["# Tableau de bord — Bibliothèque médicale Mediverse", "",
          f"_Généré le {g['date']} par `00_SYSTEME/scripts/tableau_de_bord.py`. Chiffres calculés à partir des fichiers réellement présents._", "",
          "## Indicateurs globaux", "", "| Indicateur | Valeur |", "|---|---|",
          f"| Livres identifiés (catalogue) | {g['livres_identifies']} (édition vérifiée : {g['livres_verifies']}) |",
          f"| Livres acquis | {g['livres_acquis']} |",
          f"| Documents PDF complets (intégrité vérifiée) | {g['documents_pdf_complets']} (versionnés : {g['documents_pdf_redistribuables']}, locaux : {g['documents_pdf_locaux']}) |",
          f"| Documents scannés (sans texte) | {g['documents_scannes_sans_texte']} |",
          f"| Documents OCRisés | {g['documents_ocrises']} |",
          f"| Traductions | {g['traductions']} |",
          f"| Recommandations cataloguées | {g['recommandations']} (actuelles : {g['recommandations_actuelles']}, remplacées : {g['recommandations_remplacees']}) |",
          f"| Pathologies référencées | {g['pathologies_referencees']} (avec dossier : {g['pathologies_avec_dossier']}) |",
          f"| Dossiers pédagogiques | {g['dossiers_pedagogiques']} (audit effectué : {g['dossiers_audit_effectue']} ; validés : {g['dossiers_audites']}) — {g['mots_dossiers']:,} mots |".replace(",", " "),
          f"| Fiches de révision | {g['fiches_revision']} |",
          f"| Cas cliniques | {g['cas_cliniques']} |",
          f"| QCM | {g['qcm']} |",
          f"| Termes du glossaire FR–EN–AR | {g['termes_glossaire']} |",
          f"| Items du résidanat couverts | {g['items_residanat_couverts_brut']} / {g['items_residanat']} (brut) — {g['items_residanat_couverts_audites']} audités |",
          f"| Ressources manquantes | ouvrages non acquis : {g['ressources_manquantes']['ouvrages_non_acquis']} ; items sans dossier : {g['ressources_manquantes']['items_residanat_sans_dossier']} ; items sans QCM : {g['ressources_manquantes']['items_residanat_sans_qcm']} ; acquisitions échouées : {g['acquisitions_echouees']} |",
          "", "## Couverture par spécialité", "",
          "Couverture = part des items du résidanat rattachés à la spécialité disposant d'un dossier (brute) / d'un dossier audité (auditée).", "",
          "| # | Spécialité | Items rés. | Couv. brute | Couv. auditée | Dossiers (audités) | QCM | Cas | Pathologies | Ouvrages | Recos |",
          "|---|---|---|---|---|---|---|---|---|---|---|", *lignes, ""]
    (RACINE / "25_INDEX_GENERAL/TABLEAU_DE_BORD.md").write_text("\n".join(md), encoding="utf-8")
    ecrire_json(RACINE / "25_INDEX_GENERAL/tableau_de_bord.json", {"global": g, "specialites": tableau}, agent="tableau_de_bord", sauvegarde=False)
    journaliser("tableau_de_bord", "generation", "25_INDEX_GENERAL/TABLEAU_DE_BORD.md")
    print(json.dumps({k: v for k, v in g.items() if k != "ressources_manquantes"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
