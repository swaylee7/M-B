#!/usr/bin/env python3
"""Importe le programme du concours de résidanat (médecine) depuis le PDF officiel acquis
et produit 16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json.

Identifiants stables : RES-SF-001..073 (sciences fondamentales), RES-MED-001..174, RES-CHI-001..067.
Le rattachement aux spécialités est une décision éditoriale de la bibliothèque (champ "specialites"),
distincte du texte du programme (champs "module_programme" et "intitule", repris tels quels).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, charger_json, ecrire_json  # noqa: E402

PDF = RACINE / "16_RESIDANAT_ALGERIE/00_TEXTES_OFFICIELS/Programme_concours_residanat_medecine_a_compter_de_2024-2025__FMED_Tlemcen.pdf"
SORTIE = RACINE / "16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json"

SF = {1: "EMBR", 2: "ANAT,HIST,PHYS,BIOP", 3: "BIOP,OPHT", 4: "ANAT,HIST,PHYS,BIOP", 5: "ANAT,HIST,BIOP",
      6: "PHYS", 7: "PHYS,BIOP", 8: "PHYS", 9: "ANAT,PHYS", 10: "HIST,PHYS", 11: "ANAT,HIST,PHYS",
      12: "ANAT,HIST,PHYS", 13: "ANAT,HIST,PHYS", 14: "PHYS,BIOC", 15: "BIOC,PHYS", 16: "PHYS",
      17: "HIST,PHYS", 18: "PHYS", 19: "PHYS", 20: "BIOC,PHYS", 21: "GENE", 22: "GENE", 23: "GENE",
      24: "GENE", 25: "GENE", 26: "BIOC", 27: "BIOC", 28: "BIOC", 29: "BIOC", 30: "BIOC", 31: "MICR,PARA",
      32: "MICR,BIOM", 33: "HEMA,PHYS", 34: "IMMU", 35: "IMMU", 36: "IMMU", 37: "IMMU", 38: "IMMU,IMPA",
      39: "ANAP", 40: "ANAP", 41: "ANAP", 42: "ANAP", 43: "HIST,PHYS", 44: "PHYS", 45: "PHYS", 46: "PHYS",
      47: "PHYS", 48: "PHAR", 49: "PHYS,BIOP", 50: "PHYS,BIOP", 51: "BIOP", 52: "HIST,PHYS",
      53: "ANAT,HIST,PHYS", 54: "PHYS", 55: "BIOC", 56: "ANAP", 57: "ANAP", 58: "ANAP", 59: "ANAP",
      60: "ANAP", 61: "BIOP,RADI", 62: "IMAG", 63: "IMAG", 64: "IMAG", 65: "RADI", 66: "RADI", 67: "BIOP",
      68: "BIOP,MNUC", 69: "ANAT", 70: "PHYS,BIOP", 71: "BIOP", 72: "BIOP", 73: "MICR"}

MODULES_MED = {"MALADIES INFECTIEUSES": "INFE", "DERMATOLOGIE": "DERM", "GASTROENTEROLOGIE": "GAST",
               "NEUROLOGIE": "NEUR", "PNEUMOLOGIE": "PNEU", "CARDIOLOGIE": "CARD", "PEDIATRIE": "PEDI",
               "ENDOCRINOLOGIE": "ENDO", "RHUMATOLOGIE - READAPTATION PHYSIQUE": "RHUM", "REANIMATION": "MINT_REA",
               "HEMATOLOGIE CLINIQUE": "HEMA", "NEPHROLOGIE": "NEPH", "EPIDEMIOLOGIE ET MEDECINE PREVENTIVE": "EPID",
               "MEDECINE LEGALE": "MLEG", "MEDECINE DU TRAVAIL": "MTRA", "PSYCHIATRIE": "PSYC",
               "MALADIES SYSTEMIQUES": "MINT", "PERSONNES AGEES": "GERI", "THERAPEUTIQUE": "PHAR"}
SURCHARGE_MED = {19: "HEPA,INFE", 20: "HEPA", 21: "GAST,PARA,INFE", 22: "HEPA,GAST", 23: "HEPA",
                 42: "PNEU,INFE", 46: "PNEU,ONCO", 69: "NEON,PEDI", 75: "NEON", 76: "NEON,PEDI", 81: "NEON,INFE",
                 86: "ENDO,ONCO", 91: "DIAB,ENDO", 92: "DIAB,URGE", 98: "RHUM,INFE", 104: "MPR,ORTH", 105: "MPR,NEUR",
                 108: "MINT_REA,URGE", 109: "URGE,MINT_REA", 110: "URGE", 111: "URGE",
                 115: "HEMA,ONCO", 116: "HEMA,ONCO", 117: "HEMA,ONCO", 134: "SPUB,EPID", 135: "SPUB",
                 136: "SPUB", 137: "SPUB", 154: "MINT,RHUM", 171: "HEMA,ANES", 172: "NEPH", 174: "GYNE,PHAR"}
CHI = {**{i: "CDIG,ONCO" for i in range(1, 7)}, 7: "CDIG", 8: "CDIG", 9: "CDIG", 10: "CDIG,GAST", 11: "CGEN",
       12: "CDIG,PARA", 13: "CGEN,ENDO", 14: "CGEN", 15: "CGEN", 16: "CGEN,CDIG", 17: "CPLA,MINT_REA",
       18: "CCVA", 19: "CPED", 20: "CPED", 21: "ORTH,CPED", 22: "CPED", 23: "UROL", 24: "UROL,ONCO",
       25: "UROL", 26: "UROL,ONCO", 27: "UROL,ONCO", 28: "UROL,CPED", 29: "UROL", 30: "UROL", 31: "UROL",
       32: "UROL", 33: "TRAU", 34: "TRAU", 35: "TRAU", 36: "TRAU", 37: "ORTH,RHUM", 38: "ORTH,INFE",
       39: "ORTH,ONCO", 40: "OPHT", 41: "OPHT", 42: "OPHT,DIAB", 43: "OPHT,CARD", 44: "ORL", 45: "ORL",
       46: "ORL,URGE", 47: "ORL,NEUR", 48: "ORL,PEDI", 49: "ORL,ONCO", 50: "ORL,ONCO", 51: "NCHI,URGE",
       52: "NCHI,NEUR", 53: "NCHI,TRAU", 54: "NCHI,INFE", 55: "NCHI,NEUR", 56: "OBST", 57: "GYNE",
       58: "GYNE,ONCO", 59: "GYNE,ONCO", 60: "GYNE", 61: "GYNE,ONCO", 62: "GYNE,ONCO", 63: "OBST",
       64: "OBST", 65: "GYNE", 66: "OBST", 67: "OBST,DIAB"}


def texte_pdf() -> list[str]:
    r = subprocess.run(["pdftotext", "-layout", str(PDF), "-"], capture_output=True, text=True, check=True)
    return r.stdout.splitlines()


def main() -> int:
    lignes = texte_pdf()
    items, partie, module, courant = [], None, None, None
    re_item = re.compile(r"^\s*Item\s*(\d+)\.?\s+(.*)$")
    for brut in lignes:
        l = brut.rstrip()
        s = l.strip()
        if not s:
            continue
        if s.startswith("Programme de sciences fondamentales"):
            partie, module = "SF", "SCIENCES FONDAMENTALES"; continue
        if s.startswith("Programme de médecine"):
            partie = "MED"; continue
        if s.startswith("Programme de chirurgie"):
            partie, module = "CHI", "CHIRURGIE"; continue
        if partie == "MED" and s in MODULES_MED:
            module = s; continue
        m = re_item.match(l)
        if m and partie:
            courant = {"partie": partie, "module_programme": module, "numero": int(m.group(1)),
                       "intitule": m.group(2).strip()}
            items.append(courant); continue
        if courant and partie and l.startswith(" ") and not s.isupper():
            courant["intitule"] += " " + s
    for it in items:
        it["intitule"] = re.sub(r"\s+", " ", it["intitule"]).replace("Ciagnostic", "Diagnostic")
        n = it["numero"]
        if it["partie"] == "SF":
            sp = SF[n]
        elif it["partie"] == "MED":
            sp = SURCHARGE_MED.get(n, MODULES_MED[it["module_programme"]])
        else:
            sp = CHI[n]
        it["id"] = f"RES-{ {'SF': 'SF', 'MED': 'MED', 'CHI': 'CHI'}[it['partie']] }-{n:03d}".replace(" ", "")
        it["specialites"] = sp.split(",")
        it["dossiers"] = []          # rempli par l'indexeur (dossiers pédagogiques couvrant l'item)
        it["qcm"] = 0; it["cas_cliniques"] = 0
    attendus = {"SF": 73, "MED": 174, "CHI": 67}
    for p, n in attendus.items():
        nums = sorted(i["numero"] for i in items if i["partie"] == p)
        if nums != list(range(1, n + 1)):
            print(f"ERREUR import {p}: {len(nums)} items, attendus {n}", file=sys.stderr)
            return 1
    ancien = charger_json(SORTIE, None)
    if ancien:  # préserver les liens déjà établis
        prev = {i["id"]: i for i in ancien["items"]}
        for it in items:
            if it["id"] in prev:
                for k in ("dossiers", "qcm", "cas_cliniques"):
                    it[k] = prev[it["id"]].get(k, it[k])
    ecrire_json(SORTIE, {
        "source": "DOC-00001 — Programme de concours de résidanat à compter de 2024-2025 (FMED Tlemcen)",
        "remarque": "Intitulés repris du document source ; rattachement aux spécialités = choix éditorial Mediverse.",
        "total": len(items), "items": items}, agent="RES-01")
    print(f"{len(items)} items importés -> {SORTIE.relative_to(RACINE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
