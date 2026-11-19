# Journal — RES-06

Mission : Fiches mémo, tableaux de révision et pièges classiques

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19 — démarrage de la mission RES-06 lot 1 : 20 fiches de révision dérivées des dossiers v1.1 audités + compilation des pièges classiques. Lecture de `00_SYSTEME/CONVENTIONS.md`.
- 2026-11-19 — FIC-CARD-0001 (insuffisance cardiaque) créée depuis DOS-CARD-0001 v1.1.
- 2026-11-19 — FIC-CARD-0002 (HTA), FIC-CARD-0003 (SCA ST+), FIC-CARD-0004 (SCA ST−), FIC-CARD-0005 (endocardites) créées.
- 2026-11-19 — FIC-PNEU-0001 (tuberculose), FIC-PNEU-0002 (pneumonies), FIC-PNEU-0003 (asthme) créées.
- 2026-11-19 — FIC-INFE-0001 (méningites purulentes), FIC-INFE-0002 (brucellose) créées.
- 2026-11-19 — FIC-GAST-0001 (hémorragies digestives), FIC-HEPA-0001 (hépatites A-B-C), FIC-HEPA-0002 (cirrhoses) créées.
- 2026-11-19 — FIC-CDIG-0001 (kyste hydatique du foie), FIC-CDIG-0002 (pancréatite aiguë) créées.
- 2026-11-19 — FIC-DIAB-0001 (diabète sucré), FIC-DIAB-0002 (complications aiguës du diabète) créées.
- 2026-11-19 — FIC-ENDO-0001 (hyperthyroïdies) créée.
- 2026-11-19 — FIC-NEPH-0001 (IRA), FIC-NEPH-0002 (dyskaliémies) créées. **Lot 1 complet : 20 fiches** (1 370 à 1 700 mots de corps chacune ; 9 sections ; sources YAML copiées à l'identique du dossier par script, champ `remarque` omis ; 4 à 6 sources par fiche).
- 2026-11-19 — Contrôles automatiques : YAML valide, 9 sections, 9–10 pièges et 10 lignes « 5 minutes » par fiche ; tous les nombres des fiches retrouvés dans le dossier source ; marqueurs `[POSOLOGIE À VÉRIFIER …]` repris à l'identique pour les posologies citées. `valider.py` : 0 erreur, aucun avertissement sur les fiches. Mnémotechniques non originaux (CHAMPIT, BASIC, AEIOU) signalés comme tels.
- 2026-11-19 — Compilation `16_RESIDANAT_ALGERIE/07_PIEGES_CLASSIQUES/PIEGES_CLASSIQUES_LOT1.md` : 199 pièges, 7 modules du programme (maladies infectieuses, gastroentérologie, pneumologie, cardiologie, endocrinologie, néphrologie, chirurgie), renvoi item + fiche + numéro de piège. Opérations inscrites dans `00_SYSTEME/journaux/operations.jsonl`.
- 2026-11-19 — Incohérences repérées dans les dossiers (signalées, **non corrigées**) :
  1. DOS-CARD-0005 vs DOS-INFE-0002 — EI à *Brucella* : rifampicine 300–600 mg/j + doxycycline + cotrimoxazole ≥ 3–6 mois (CARD-0005, d'après ESC 2015) contre doxycycline + rifampicine (600–900 mg/j) + aminoside ± cotrimoxazole (INFE-0002).
  2. DOS-CARD-0005 — abandon de la clindamycine affirmé sans réserve en points clés/pièges, mais marqué `[À VÉRIFIER]` pour l'ESC 2023 en §15.1 et §21.
  3. DOS-ENDO-0001 — fréquence de l'agranulocytose : 0,1–1 % (texte) vs ≈ 0,6 % MMI et 1–1,5 % PTU (tableau ETA cité).
  4. DOS-DIAB-0002 — glycémie cible sous perfusion d'insuline après 250 mg/dL : « autour de 200 mg/dL » (§13.2) vs « ≈ 150–200 mg/dL » (§21) ; piège n° 1 formulé avec l'ancien seuil 2,50 g/L.
  5. DOS-HEPA-0001 — point clé 7 attribue à l'OMS 2024 le critère « ADN ≥ 2 000 + ALAT > LSN **et/ou fibrose** », alors que §13.3.2 sépare fibrose (critère 1) et ADN + ALAT (critère 2).
  6. DOS-PNEU-0001 — calendrier des microscopies de contrôle M2/M5/M6 (OMS) vs M2/M4/M6 (supports nationaux) : divergence signalée par le dossier lui-même, à trancher sur l'Instruction n°07/2024.
  7. DOS-HEPA-0001 — date du vaccin VHB en Algérie (2000 vs 2003), déjà signalée dans le dossier.
