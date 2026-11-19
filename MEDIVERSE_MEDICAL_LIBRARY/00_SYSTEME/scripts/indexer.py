#!/usr/bin/env python3
"""Indexeur central de la bibliothèque Mediverse.

1. Fusionne les lots écrits par les agents (`lots/*.json`) en catalogues consolidés, en contrôlant l'unicité des id.
2. Recense les dossiers pédagogiques (en-tête YAML) et calcule des indicateurs qualité (mots, sources, marqueurs).
3. Relie les items du résidanat aux dossiers, QCM et cas cliniques.
4. Construit l'index de recherche : 25_INDEX_GENERAL/index_general.json + index_bibliotheque.sqlite (FTS5).

Usage : python3 00_SYSTEME/scripts/indexer.py
"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, charger_json, ecrire_json, journaliser, lister, maintenant, specialite_par_code  # noqa: E402

CATALOGUES = {
    # type: (dossier des lots, clé de liste, fichier consolidé)
    "ouvrages": ("24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/lots", "ouvrages", "24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/catalogue_ouvrages.json"),
    "recommandations": ("18_RECOMMANDATIONS/00_CATALOGUE/lots", "recommandations", "18_RECOMMANDATIONS/00_CATALOGUE/catalogue_recommandations.json"),
    "qcm": ("21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots", "qcm", "21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/banque_qcm.json"),
    "cas": ("20_CAS_CLINIQUES/lots", "cas", "20_CAS_CLINIQUES/banque_cas_cliniques.json"),
    "pathologies": ("22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots", "pathologies", "22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/referentiel_pathologies.json"),
    "glossaire": ("23_GLOSSAIRES/FR_EN_AR/lots", "termes", "23_GLOSSAIRES/FR_EN_AR/glossaire_fr_en_ar.json"),
}
RE_FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
MARQUEURS = {"a_verifier": r"\[À VÉRIFIER", "posologie_a_verifier": r"\[POSOLOGIE À VÉRIFIER"}


def fusionner(type_: str) -> tuple[list[dict], list[str]]:
    dossier, cle, _ = CATALOGUES[type_]
    elements, vus, anomalies = [], {}, []
    for f in sorted((RACINE / dossier).glob("*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:  # lot illisible : signalé, jamais ignoré silencieusement
            anomalies.append(f"{f.name}: JSON invalide ({e})")
            continue
        for el in d.get(cle, []):
            el = dict(el)
            el["_lot"] = f.name
            i = el.get("id")
            if not i:
                anomalies.append(f"{f.name}: élément sans id"); continue
            if i in vus:
                anomalies.append(f"{f.name}: id en double {i} (déjà dans {vus[i]}) — élément conservé avec suffixe")
                el["id"] = f"{i}-DUP-{f.stem}"
            vus[el["id"]] = f.name
            elements.append(el)
    return elements, anomalies


def lire_dossier(md: Path) -> dict | None:
    texte = md.read_text(encoding="utf-8")
    m = RE_FM.match(texte)
    if not m:
        return None
    import yaml
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception as e:
        fm = {"_erreur_yaml": str(e)}
    corps = texte[m.end():]
    sources = fm.get("sources") or []
    cites = set(re.findall(r"\bS(\d+)\b", " ".join(re.findall(r"\[S[\d,\sS–-]+\]", corps))))
    return {
        "id": fm.get("id", md.stem.split("__")[0]),
        "titre": fm.get("titre", md.stem),
        "specialite": fm.get("specialite"),
        "items_residanat": fm.get("items_residanat") or [],
        "statut": fm.get("statut", "inconnu"),
        "version": str(fm.get("version", "")),
        "date_revision": str(fm.get("date_revision", "")),
        "chemin": str(md.relative_to(RACINE)),
        "mots": len(corps.split()),
        "nb_sources": len(sources),
        "nb_sources_verifiees": sum(1 for s in sources if isinstance(s, dict) and s.get("verifiee") is True),
        "nb_citations_distinctes": len(cites),
        **{k: len(re.findall(v, corps)) for k, v in MARQUEURS.items()},
        "erreur_yaml": fm.get("_erreur_yaml"),
        "_texte": corps,
    }


def main() -> int:
    rapport = {"date": maintenant(), "anomalies": {}}
    donnees = {}
    for t, (_, cle, sortie) in CATALOGUES.items():
        el, an = fusionner(t)
        donnees[t] = el
        rapport["anomalies"][t] = an
        if el or (RACINE / sortie).exists():
            ecrire_json(RACINE / sortie, {"genere_le": maintenant(), "total": len(el), cle: el}, agent="indexeur")

    dossiers = []
    for md in lister("**/02_DOSSIERS_PEDAGOGIQUES/*.md"):
        d = lire_dossier(md)
        if d:
            dossiers.append(d)
    fiches = [d for md in lister("**/03_FICHES_REVISION/*.md") if (d := lire_dossier(md))]

    # liens items du résidanat
    prog_path = RACINE / "16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json"
    prog = charger_json(prog_path)
    if prog:
        par_item = {i["id"]: i for i in prog["items"]}
        for i in par_item.values():
            i["dossiers"], i["qcm"], i["cas_cliniques"], i["fiches"] = [], 0, 0, []
        for d in dossiers:
            for it in d["items_residanat"]:
                if it in par_item:
                    par_item[it]["dossiers"].append({"id": d["id"], "statut": d["statut"], "chemin": d["chemin"]})
        for f in fiches:
            for it in f["items_residanat"]:
                if it in par_item:
                    par_item[it]["fiches"].append(f["id"])
        for q in donnees["qcm"]:
            for it in q.get("items_residanat") or []:
                if it in par_item:
                    par_item[it]["qcm"] += 1
        for c in donnees["cas"]:
            for it in c.get("items_residanat") or []:
                if it in par_item:
                    par_item[it]["cas_cliniques"] += 1
        prog["indexe_le"] = maintenant()
        ecrire_json(prog_path, prog, agent="indexeur")
        # liens pathologies -> dossiers (via les items du résidanat partagés)
        for p in donnees["pathologies"]:
            ds = sorted({d["id"] for it in (p.get("items_residanat") or []) if it in par_item
                         for d in par_item[it]["dossiers"]})
            p["dossier"] = ds or None
        _, cle_p, sortie_p = CATALOGUES["pathologies"]
        if donnees["pathologies"]:
            ecrire_json(RACINE / sortie_p, {"genere_le": maintenant(), "total": len(donnees["pathologies"]),
                                            cle_p: donnees["pathologies"]}, agent="indexeur", sauvegarde=False)

    # index général (métadonnées) + SQLite FTS5 (texte intégral)
    spe = specialite_par_code()
    entrees = []
    def ajout(type_, id_, titre, specialite, chemin, texte):
        entrees.append({"type": type_, "id": id_, "titre": titre, "specialite": specialite,
                        "specialite_nom": spe.get(specialite or "", {}).get("nom", ""), "chemin": chemin, "_texte": texte})
    for d in dossiers:
        ajout("dossier", d["id"], d["titre"], d["specialite"], d["chemin"], d["_texte"])
    for f in fiches:
        ajout("fiche", f["id"], f["titre"], f["specialite"], f["chemin"], f["_texte"])
    for q in donnees["qcm"]:
        txt = " ".join([q.get("enonce", ""), *(q.get("propositions") or {}).values(), q.get("explication_generale", "")])
        ajout("qcm", q["id"], (q.get("theme") or q.get("enonce", ""))[:120], q.get("specialite"), CATALOGUES["qcm"][2], txt)
    for c in donnees["cas"]:
        txt = " ".join(str(v) for k, v in c.items() if isinstance(v, str))
        ajout("cas_clinique", c["id"], c.get("titre", ""), c.get("specialite"), CATALOGUES["cas"][2], txt)
    for r in donnees["recommandations"]:
        dom = r.get("domaine") or []
        txt = " ".join([r.get("titre", ""), r.get("organisme", ""), " ".join(r.get("points_cles") or [])])
        ajout("recommandation", r["id"], f"{r.get('organisme', '')} — {r.get('titre', '')}", dom[0] if dom else None,
              CATALOGUES["recommandations"][2], txt)
    for o in donnees["ouvrages"]:
        sp = o.get("specialites") or []
        ajout("ouvrage", o["id"], f"{o.get('titre', '')} ({o.get('edition', '')}, {o.get('annee', '')})", sp[0] if sp else None,
              CATALOGUES["ouvrages"][2], " ".join([o.get("titre", ""), " ".join(o.get("auteurs_editeurs") or [])]))
    for p in donnees["pathologies"]:
        txt = " ".join([p.get("nom_fr", ""), p.get("nom_en", ""), " ".join(p.get("synonymes") or []),
                        " ".join(p.get("symptomes") or []), " ".join(p.get("signes_cliniques") or [])])
        ajout("pathologie", p["id"], p.get("nom_fr", ""), p.get("specialite"), CATALOGUES["pathologies"][2], txt)
    for g in donnees["glossaire"]:
        # "ar" peut valoir null (équivalent arabe à établir) : on le remplace par "" pour l'index
        ar = g.get("ar") or ""
        ajout("terme", g["id"], f"{g.get('fr') or ''} / {g.get('en') or ''} / {ar}", (g.get("specialites") or [None])[0],
              CATALOGUES["glossaire"][2], " ".join([g.get("fr") or "", g.get("en") or "", ar, " ".join(g.get("ar_variantes") or []),
                                                   g.get("developpement_fr") or "", g.get("developpement_en") or "", g.get("definition_fr") or ""]))
    reg = charger_json(RACINE / "00_SYSTEME/registre_acquisitions.json", {"documents": []})
    for doc in reg["documents"]:
        if doc.get("redistribution") == "redistribuable":
            ajout("document_acquis", doc["id"], doc["titre"], (doc.get("specialites") or [None])[0], doc["emplacement"],
                  doc["titre"] + " " + doc.get("emetteur", ""))

    idx_dir = RACINE / "25_INDEX_GENERAL"
    idx_dir.mkdir(exist_ok=True)
    ecrire_json(idx_dir / "index_general.json", {"genere_le": maintenant(), "total": len(entrees),
                                                  "entrees": [{k: v for k, v in e.items() if k != "_texte"} for e in entrees]},
                agent="indexeur", sauvegarde=False)
    base = idx_dir / "index_bibliotheque.sqlite"
    if base.exists():
        base.unlink()
    con = sqlite3.connect(base)
    con.execute("CREATE VIRTUAL TABLE recherche USING fts5(type, id, titre, specialite, specialite_nom, chemin, texte, "
                "tokenize='unicode61 remove_diacritics 2')")
    con.executemany("INSERT INTO recherche VALUES (?,?,?,?,?,?,?)",
                    [(e["type"], e["id"], e["titre"], e["specialite"] or "", e["specialite_nom"], e["chemin"], e["_texte"]) for e in entrees])
    con.commit(); con.close()

    ecrire_json(RACINE / "00_SYSTEME/journaux/inventaire_dossiers.json",
                {"genere_le": maintenant(), "dossiers": [{k: v for k, v in d.items() if k != "_texte"} for d in dossiers],
                 "fiches": [{k: v for k, v in f.items() if k != "_texte"} for f in fiches]}, agent="indexeur", sauvegarde=False)
    ecrire_json(RACINE / "00_SYSTEME/journaux/rapport_indexation.json", rapport, agent="indexeur", sauvegarde=False)
    journaliser("indexeur", "indexation", "25_INDEX_GENERAL", {"entrees": len(entrees), "dossiers": len(dossiers)})
    n_an = sum(len(v) for v in rapport["anomalies"].values())
    print(f"Index : {len(entrees)} entrées | dossiers {len(dossiers)} | fiches {len(fiches)} | QCM {len(donnees['qcm'])} | "
          f"cas {len(donnees['cas'])} | recos {len(donnees['recommandations'])} | ouvrages {len(donnees['ouvrages'])} | "
          f"pathologies {len(donnees['pathologies'])} | termes {len(donnees['glossaire'])} | anomalies {n_an}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
