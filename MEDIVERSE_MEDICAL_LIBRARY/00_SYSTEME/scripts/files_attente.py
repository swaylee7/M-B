#!/usr/bin/env python3
"""Régénère les files d'attente de travail (reprise après interruption, §15/§17) à partir de l'état réel.

Files produites dans 00_SYSTEME/files_attente/ :
  * dossiers_residanat.json  — un dossier par item du programme (à faire / à auditer / corrections / validé), poste DOS-xx assigné
  * qcm_residanat.json       — items avec moins de 10 QCM
  * audits.json              — dossiers au statut brouillon_a_auditer ou audite_corrections_requises
  * acquisitions.json        — acquisitions échouées à relancer (journal)
L'ordre de priorité des items suit le plan de travail (§17) : clinique fréquente d'abord, puis fondamentales.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, SYSTEME, charger_json, ecrire_json, maintenant  # noqa: E402

POSTES_DOS = {"CARD": "DOS-01", "PNEU": "DOS-02", "INFE": "DOS-02", "ENDO": "DOS-03", "DIAB": "DOS-03", "NEPH": "DOS-03",
              "GAST": "DOS-04", "HEPA": "DOS-04", "CDIG": "DOS-04", "CGEN": "DOS-04", "PEDI": "DOS-05", "NEON": "DOS-05",
              "NEUR": "DOS-06", "MINT_REA": "DOS-06", "URGE": "DOS-06", "GYNE": "DOS-07", "OBST": "DOS-07",
              "HEMA": "DOS-08", "ONCO": "DOS-08", "RHUM": "DOS-09", "MINT": "DOS-09", "DERM": "DOS-09", "MPR": "DOS-09",
              "PSYC": "DOS-10", "MLEG": "DOS-10", "MTRA": "DOS-10", "UROL": "DOS-11", "ORTH": "DOS-11", "TRAU": "DOS-11",
              "ORL": "DOS-12", "OPHT": "DOS-12", "NCHI": "DOS-12", "CPLA": "DOS-11", "CCVA": "DOS-01", "CPED": "DOS-05",
              "SPUB": "DOS-15", "EPID": "DOS-15", "GERI": "DOS-15", "PHAR": "DOS-14", "MICR": "DOS-14", "PARA": "DOS-14",
              "IMMU": "DOS-14", "ANAP": "DOS-14", "IMPA": "DOS-14"}
PRIO_PARTIE = {"MED": 1, "CHI": 2, "SF": 3}
AUDITES = {"audite_valide", "valide_enseignant"}


def main() -> int:
    prog = charger_json(RACINE / "16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json")["items"]
    fa = SYSTEME / "files_attente"
    fa.mkdir(exist_ok=True)
    doss, qcm = [], []
    for i in sorted(prog, key=lambda x: (PRIO_PARTIE[x["partie"]], x["numero"])):
        ds = i.get("dossiers", [])
        if not ds:
            etat = "a_faire"
        elif any(d["statut"] in AUDITES for d in ds):
            etat = "valide"
        elif any(d["statut"] == "audite_corrections_requises" for d in ds):
            etat = "corrections"
        else:
            etat = "a_auditer"
        sp = i["specialites"][0]
        doss.append({"item": i["id"], "intitule": i["intitule"], "specialite": sp, "poste": POSTES_DOS.get(sp, "DOS-13"),
                     "etat": etat, "dossiers": [d["id"] for d in ds]})
        if i.get("qcm", 0) < 10:
            qcm.append({"item": i["id"], "intitule": i["intitule"], "specialite": sp, "qcm_existants": i.get("qcm", 0), "objectif": 10,
                        "poste": {"SF": "RES-02", "MED": "RES-03", "CHI": "RES-04"}[i["partie"]]})
    inv = charger_json(SYSTEME / "journaux/inventaire_dossiers.json", {"dossiers": []})
    audits = [{"dossier": d["id"], "chemin": d["chemin"], "statut": d["statut"], "mots": d["mots"],
               "marqueurs_posologie": d.get("posologie_a_verifier", 0), "poste": "AUD-01/AUD-02"}
              for d in inv["dossiers"] if d["statut"] in ("brouillon_a_auditer", "audite_corrections_requises")]
    echecs = []
    j = SYSTEME / "journaux/operations.jsonl"
    if j.exists():
        for l in j.read_text(encoding="utf-8").splitlines():
            try:
                e = json.loads(l)
            except Exception:
                continue
            if e.get("action") == "echec_acquisition":
                echecs.append({"cible": e["cible"], "url": (e.get("details") or {}).get("url"), "erreur": (e.get("details") or {}).get("erreur"),
                               "date": e["date"], "agent": e["agent"]})
    for nom, contenu in [("dossiers_residanat", doss), ("qcm_residanat", qcm), ("audits", audits), ("acquisitions", echecs)]:
        ecrire_json(fa / f"{nom}.json", {"genere_le": maintenant(), "total": len(contenu), "taches": contenu},
                    agent="orchestrateur", sauvegarde=False)
    a_faire = sum(1 for d in doss if d["etat"] == "a_faire")
    print(f"Files : dossiers à faire {a_faire}/{len(doss)} | items <10 QCM {len(qcm)} | audits {len(audits)} | acquisitions à relancer {len(echecs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
