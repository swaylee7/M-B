#!/usr/bin/env python3
"""Génère / met à jour le registre des 100 postes d'agents (§15) et leurs répertoires de travail.

MODE D'EXÉCUTION RÉEL (transparence, §15 dernier alinéa) :
  Il n'existe pas 100 processus permanents. Chaque « agent » est un POSTE (mission + périmètre + objectifs +
  journal + état de reprise). Les postes sont exécutés par lots par des sessions Claude Code : une session
  orchestratrice et jusqu'à ~10 sous-agents simultanés. Un même sous-agent peut tenir plusieurs postes
  successivement. L'état de chaque poste (`etat.json`) permet la reprise après interruption.

Idempotent : n'écrase jamais un journal ni un état existant.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import SYSTEME, ecrire_json, maintenant  # noqa: E402

GROUPES_SPE = [
    ("Sciences fondamentales I", "ANAT,HIST,EMBR"), ("Sciences fondamentales II", "PHYS,BIOP"),
    ("Biochimie-génétique", "BIOC,GENE,BIOM"), ("Pharmacologie", "PHAR"),
    ("Microbiologie-parasitologie-immunologie", "MICR,PARA,IMMU"), ("Pathologie", "ANAP,IMPA"),
    ("Médecine interne-gériatrie", "MINT,GERI,MFAM"), ("Cardiologie", "CARD"), ("Pneumologie", "PNEU"),
    ("Gastro-hépatologie", "GAST,HEPA"), ("Néphrologie", "NEPH"), ("Neurologie", "NEUR"),
    ("Psychiatrie", "PSYC"), ("Dermatologie", "DERM"), ("Rhumatologie-MPR", "RHUM,MPR"),
    ("Endocrinologie-diabétologie", "ENDO,DIAB"), ("Hématologie-oncologie", "HEMA,ONCO"),
    ("Infectiologie", "INFE"), ("Pédiatrie-néonatologie", "PEDI,NEON"), ("Gynéco-obstétrique", "GYNE,OBST"),
    ("Chirurgie générale et digestive", "CGEN,CDIG"), ("Urologie", "UROL"), ("Orthopédie-traumatologie", "ORTH,TRAU"),
    ("Neurochirurgie", "NCHI"), ("ORL-ophtalmologie", "ORL,OPHT"), ("Urgences-réanimation", "ANES,URGE,MINT_REA"),
    ("Imagerie", "RADI,IMAG,MNUC"), ("Médecine légale-travail", "MLEG,MTRA"), ("Santé publique-épidémiologie", "SPUB,EPID"),
    ("Chirurgies spécialisées", "CCVA,CTHO,CPED,CPLA,DENT"),
]


def postes() -> list[dict]:
    p = []
    # 30 — recherche et acquisition documentaire
    acq_speciaux = [
        ("ACQ-01", "Algérie — textes officiels (MESRS, MSPRH, JORADP), programmes du résidanat et du DEMS", "ALL"),
        ("ACQ-02", "Algérie — polycopiés et cours publiés par les facultés de médecine (accès public)", "ALL"),
        ("ACQ-03", "Algérie — guides et programmes nationaux de santé (tuberculose, PEV, paludisme, MTH, santé maternelle)", "ALL"),
        ("ACQ-04", "OMS — guides et manuels sous licence ouverte (IRIS)", "ALL"),
        ("ACQ-05", "NCBI Bookshelf / PubMed Central — ouvrages et revues en accès ouvert (licences vérifiées)", "ALL"),
        ("ACQ-06", "France — HAS, ANSM, Santé publique France (stockage local si non redistribuable)", "ALL"),
        ("ACQ-07", "France — référentiels des collèges des enseignants (catalogage ; stockage local uniquement si autorisé)", "ALL"),
        ("ACQ-08", "Sociétés savantes internationales (ESC, ERS, KDIGO, GINA, GOLD…) — catalogage et acquisition si licence", "ALL"),
    ]
    for i, (aid, mission, sp) in enumerate(acq_speciaux):
        p.append({"id": aid, "groupe": "recherche_acquisition", "mission": mission, "specialites": sp})
    for k, (nom, sp) in enumerate(GROUPES_SPE[:22], start=9):
        p.append({"id": f"ACQ-{k:02d}", "groupe": "recherche_acquisition",
                  "mission": f"Veille et acquisition de ressources libres — {nom}", "specialites": sp})
    # 20 — analyse et structuration des ouvrages
    for k, (nom, sp) in enumerate(GROUPES_SPE[:20], start=1):
        p.append({"id": f"ANA-{k:02d}", "groupe": "analyse_structuration",
                  "mission": f"Catalogue vérifié des ouvrages de référence et structuration des contenus — {nom}", "specialites": sp})
    # 15 — dossiers pédagogiques
    dos = [("Cardiologie-angiologie", "CARD"), ("Pneumologie-infectiologie", "PNEU,INFE"),
           ("Endocrinologie-diabétologie-néphrologie", "ENDO,DIAB,NEPH"), ("Gastro-hépatologie-chirurgie digestive", "GAST,HEPA,CDIG,CGEN"),
           ("Pédiatrie-néonatologie", "PEDI,NEON"), ("Neurologie-réanimation-urgences", "NEUR,MINT_REA,URGE"),
           ("Gynécologie-obstétrique", "GYNE,OBST"), ("Hématologie-oncologie", "HEMA,ONCO"),
           ("Rhumatologie-médecine interne-dermatologie", "RHUM,MINT,DERM"), ("Psychiatrie-médecine légale-travail", "PSYC,MLEG,MTRA"),
           ("Urologie-orthopédie-traumatologie", "UROL,ORTH,TRAU"), ("ORL-ophtalmologie-neurochirurgie", "ORL,OPHT,NCHI"),
           ("Sciences fondamentales", "ANAT,HIST,EMBR,PHYS,BIOP,BIOC,GENE"), ("Microbiologie-immunologie-pathologie-pharmacologie", "MICR,PARA,IMMU,ANAP,PHAR"),
           ("Santé publique-épidémiologie-gériatrie", "SPUB,EPID,GERI")]
    for k, (nom, sp) in enumerate(dos, start=1):
        p.append({"id": f"DOS-{k:02d}", "groupe": "dossiers_pedagogiques",
                  "mission": f"Dossiers pédagogiques originaux approfondis — {nom}", "specialites": sp})
    # 10 — recommandations et protocoles
    rec = [("Algérie (MSPRH, INSP, programmes nationaux)", "ALL"), ("HAS et sociétés savantes françaises", "ALL"),
           ("OMS", "ALL"), ("Cardiologie-vasculaire (ESC, ESH, AHA/ACC)", "CARD"), ("Pneumologie (GINA, GOLD, ERS/ATS)", "PNEU"),
           ("Infectiologie et antibiothérapie (SPILF, IDSA, OMS)", "INFE"), ("Néphro-endocrino-diabéto (KDIGO, ADA, EASD, ETA)", "NEPH,ENDO,DIAB"),
           ("Gastro-hépatologie (EASL, AASLD, ESGE)", "GAST,HEPA"), ("Oncologie (ESMO, NCCN-accès libre)", "ONCO"),
           ("Protocoles d'urgence et de réanimation", "URGE,MINT_REA,ANES")]
    for k, (nom, sp) in enumerate(rec, start=1):
        p.append({"id": f"REC-{k:02d}", "groupe": "recommandations_protocoles",
                  "mission": f"Catalogue daté des recommandations et protocoles — {nom}", "specialites": sp})
    # 10 — résidanat et DEMS
    res = [("RES-01", "Programme du résidanat : import, items, rattachements, couverture"),
           ("RES-02", "Banque QCM — sciences fondamentales"), ("RES-03", "Banque QCM — médecine"),
           ("RES-04", "Banque QCM — chirurgie"), ("RES-05", "Cas cliniques progressifs résidanat"),
           ("RES-06", "Fiches mémo, tableaux de révision et pièges classiques"),
           ("RES-07", "Annales : recherche de sujets authentiques sourcés (jamais inventés)"),
           ("DEMS-01", "DEMS : programmes officiels et objectifs par spécialité médicale"),
           ("DEMS-02", "DEMS : programmes officiels et objectifs par spécialité chirurgicale"),
           ("DEMS-03", "DEMS : parcours progressifs, urgences et conduites à tenir")]
    for aid, mission in res:
        p.append({"id": aid, "groupe": "residanat_dems", "mission": mission, "specialites": "ALL"})
    # 5 — traduction
    for aid, mission in [("TRA-01", "Glossaire médical FR–EN–AR (termes cliniques)"),
                         ("TRA-02", "Glossaire FR–EN–AR (sciences fondamentales, pharmacologie)"),
                         ("TRA-03", "Traduction FR de documents sous licence autorisant l'adaptation (ex. CC BY, CC BY-NC-SA OMS)"),
                         ("TRA-04", "Fiches bilingues de termes et abréviations"),
                         ("TRA-05", "Contrôle qualité des traductions")]:
        p.append({"id": aid, "groupe": "traduction", "mission": mission, "specialites": "ALL"})
    # 5 — OCR et PDF
    for aid, mission in [("OCR-01", "Détection des PDF scannés (sans texte) dans le registre"),
                         ("OCR-02", "OCR des documents autorisés (nécessite tesseract/ocrmypdf)"),
                         ("OCR-03", "Correction post-OCR et contrôle qualité du texte"),
                         ("OCR-04", "Exports ODT/PDF/ODS et tables des matières"),
                         ("OCR-05", "Intégrité des fichiers : pages, empreintes, doublons")]:
        p.append({"id": aid, "groupe": "ocr_pdf", "mission": mission, "specialites": "ALL"})
    # 5 — audit
    for aid, mission in [("AUD-01", "Audit scientifique des dossiers (exactitude, cohérence, actualité)"),
                         ("AUD-02", "Audit des posologies et contre-indications"),
                         ("AUD-03", "Audit des QCM et cas cliniques"),
                         ("AUD-04", "Audit des références (existence, date, statut actuel/remplacé)"),
                         ("AUD-05", "Audit des lacunes de couverture et relance des recherches")]:
        p.append({"id": aid, "groupe": "audit_qualite", "mission": mission, "specialites": "ALL"})
    assert len(p) == 100, len(p)
    return p


def main() -> int:
    base = SYSTEME / "agents"
    reg = []
    for a in postes():
        d = base / a["id"]
        d.mkdir(parents=True, exist_ok=True)
        a["repertoire"] = f"00_SYSTEME/agents/{a['id']}"
        a["journal"] = f"{a['repertoire']}/journal.md"
        a["etat"] = f"{a['repertoire']}/etat.json"
        j = d / "journal.md"
        if not j.exists():
            j.write_text(f"# Journal — {a['id']}\n\nMission : {a['mission']}\n\n"
                         f"- {maintenant()} — poste créé (aucune exécution encore).\n", encoding="utf-8")
        e = d / "etat.json"
        if not e.exists():
            e.write_text(json.dumps({"id": a["id"], "statut": "en_attente", "derniere_execution": None,
                                     "taches_terminees": [], "taches_suivantes": [], "objectifs": {}, "compteurs": {}},
                                    ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        reg.append(a)
    ecrire_json(base / "registre_agents.json", {
        "version": 1, "date": maintenant(), "total": len(reg),
        "mode_execution": ("Postes exécutés par lots par des sessions Claude Code (1 orchestrateur + ~10 sous-agents "
                           "simultanés au maximum). Pas de processus permanents. Reprise via etat.json + files d'attente."),
        "postes": reg}, agent="orchestrateur")
    print(f"{len(reg)} postes d'agents enregistrés.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
