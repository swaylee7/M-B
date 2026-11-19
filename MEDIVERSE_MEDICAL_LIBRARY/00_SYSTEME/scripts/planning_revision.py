#!/usr/bin/env python3
"""Génère un planning de révision du résidanat (24 semaines) à partir des 314 items du programme.

Principe : chaque semaine mêle médecine, chirurgie et sciences fondamentales (proportionnellement à leur poids),
avec répétition espacée (relecture à S+1 et S+4). Les liens vers les dossiers/QCM disponibles sont ajoutés.
Sortie : 16_RESIDANAT_ALGERIE/08_PLANNING_REVISION/PLANNING_24_SEMAINES.md (+ .json)
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from commun import RACINE, charger_json, ecrire_json, maintenant  # noqa: E402

SEMAINES = 24
REVISION_FINALE = 2   # 2 dernières semaines : révision générale et examens blancs


def main() -> int:
    items = charger_json(RACINE / "16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json")["items"]
    utiles = SEMAINES - REVISION_FINALE
    parts = {p: [i for i in items if i["partie"] == p] for p in ("MED", "CHI", "SF")}
    plan = [[] for _ in range(utiles)]
    for p, lst in parts.items():
        for k, it in enumerate(lst):           # répartition régulière, ordre du programme conservé
            plan[k * utiles // len(lst)].append(it)
    lignes = ["# Planning de révision du résidanat — 24 semaines", "",
              f"_Généré le {maintenant()} à partir du programme (DOC-00001). Proposition pédagogique Mediverse, à adapter à la date du concours._", "",
              "**Méthode** : 5 jours d'apprentissage par semaine (≈ 3 items/jour), 1 jour de QCM et cas cliniques, 1 jour de repos ou de rattrapage.",
              "Relire les items de la semaine S−1 (rappel à J+7) et ceux de la semaine S−4 (rappel à J+30) — répétition espacée.",
              "Les deux dernières semaines sont réservées aux examens blancs et à la révision des fiches et des pièges classiques.", ""]
    sortie = []
    for s, lot in enumerate(plan, 1):
        lignes += [f"## Semaine {s} — {len(lot)} items", ""]
        if s > 1:
            lignes.append(f"_Rappels : semaine {s - 1} (J+7)" + (f", semaine {s - 4} (J+30)" if s > 4 else "") + "_")
            lignes.append("")
        lignes += ["| Item | Intitulé | Dossier | QCM |", "|---|---|---|---|"]
        for it in lot:
            dos = ", ".join(d["id"] for d in it.get("dossiers", [])) or "—"
            lignes.append(f"| {it['id']} | {it['intitule'][:100]} | {dos} | {it.get('qcm', 0)} |")
        lignes.append("")
        sortie.append({"semaine": s, "items": [it["id"] for it in lot]})
    lignes += [f"## Semaines {utiles + 1}–{SEMAINES} — révision générale", "",
               "- Examen blanc chronométré (format de la session en cours : vérifier les modalités officielles de l'année).",
               "- Relecture des fiches, des tableaux de synthèse et des pièges classiques de chaque item.",
               "- Retour ciblé sur les items dont le score aux QCM est inférieur à 70 %.", ""]
    dest = RACINE / "16_RESIDANAT_ALGERIE/08_PLANNING_REVISION"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "PLANNING_24_SEMAINES.md").write_text("\n".join(lignes), encoding="utf-8")
    ecrire_json(dest / "planning_24_semaines.json", {"genere_le": maintenant(), "semaines": sortie}, agent="RES-06", sauvegarde=False)
    print(f"Planning : {len(items)} items sur {utiles} semaines + {REVISION_FINALE} de révision")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
