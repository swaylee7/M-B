#!/usr/bin/env python3
"""Construit (de façon idempotente) l'arborescence complète de la bibliothèque.

Usage : python3 MEDIVERSE_MEDICAL_LIBRARY/00_SYSTEME/scripts/construire_architecture.py
Ne supprime jamais rien : ajoute seulement les dossiers manquants.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, CONFIG, charger_yaml, dossier_specialite, journaliser, slug  # noqa: E402

SECTIONS_TRANSVERSES = {
    "16_RESIDANAT_ALGERIE": ["00_TEXTES_OFFICIELS", "01_PROGRAMME_ITEMS", "02_COURS_PAR_ITEM",
                             "03_ANNALES_SOURCEES", "04_QCM_ENTRAINEMENT", "05_CAS_CLINIQUES",
                             "06_FICHES_MEMO", "07_PIEGES_CLASSIQUES", "08_PLANNING_REVISION"],
    "17_DEMS": ["00_TEXTES_OFFICIELS", "01_PARCOURS_PAR_SPECIALITE", "02_OBJECTIFS_PEDAGOGIQUES",
                "03_EVALUATIONS", "04_URGENCES_ET_CAT"],
    "18_RECOMMANDATIONS": ["00_CATALOGUE", "01_ALGERIE", "02_FRANCE_HAS", "03_SOCIETES_SAVANTES",
                           "04_OMS", "05_EUROPE", "06_AMERIQUE_DU_NORD", "07_ARCHIVES_REMPLACEES"],
    "19_PROTOCOLES": ["01_URGENCES", "02_REANIMATION", "03_ANTIBIOTHERAPIE", "04_PEDIATRIE",
                      "05_OBSTETRIQUE", "06_THERAPEUTIQUE_GENERALE"],
    "20_CAS_CLINIQUES": ["NIVEAU_1_ETUDIANT", "NIVEAU_2_GENERALISTE", "NIVEAU_3_RESIDENT",
                         "NIVEAU_4_SPECIALISTE", "PREPARATION_RESIDANAT", "PREPARATION_DEMS"],
    "21_QCM_ANNALES": ["01_BANQUE_QCM_ORIGINALE", "02_ANNALES_SOURCEES", "03_EXPORTS"],
    "22_ENCYCLOPEDIE_PATHOLOGIES": ["00_REFERENTIEL", "01_FICHES", "02_GRAPHE_LIENS"],
    "23_GLOSSAIRES": ["FR_EN_AR"],
    "24_BIBLIOGRAPHIE": ["00_CATALOGUE_OUVRAGES", "01_REFERENCES_CITEES"],
    "25_INDEX_GENERAL": [],
    "00_SYSTEME": [],
}


def main() -> int:
    cfg = charger_yaml(CONFIG / "specialites.yaml")
    crees = 0
    for d in cfg["dossiers_racine"]:
        p = RACINE / d
        if not p.exists():
            p.mkdir(parents=True); crees += 1
        for sd in SECTIONS_TRANSVERSES.get(d, []):
            q = p / sd
            if not q.exists():
                q.mkdir(parents=True); crees += 1
            (q / ".gitkeep").touch()
    for sp in cfg["specialites"]:
        base = dossier_specialite(sp)
        for sd in cfg["sous_dossiers_standard"]:
            q = base / sd
            if not q.exists():
                q.mkdir(parents=True); crees += 1
            (q / ".gitkeep").touch()
        for i, sous in enumerate(sp.get("sous", []), 1):
            q = base / "SOUS_SPECIALITES" / f"{i:02d}_{slug(sous)}"
            if not q.exists():
                q.mkdir(parents=True); crees += 1
            (q / ".gitkeep").touch()
    journaliser("architecte", "construire_architecture", str(RACINE.name), {"dossiers_crees": crees})
    print(f"Architecture OK — {crees} dossier(s) créé(s), {len(cfg['specialites'])} spécialités.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
