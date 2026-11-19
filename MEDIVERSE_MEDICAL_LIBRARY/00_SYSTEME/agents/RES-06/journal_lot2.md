# Journal — RES-06 (lot 2)

Mission : fiches de révision (mémo, tableaux, pièges classiques) dérivées des dossiers v1.1 audités — lot 2 :
pédiatrie, néonatologie, neurologie, réanimation, urgences, obstétrique, gynécologie, hématologie (20 fiches)
+ compilation `16_RESIDANAT_ALGERIE/07_PIEGES_CLASSIQUES/PIEGES_CLASSIQUES_LOT2.md`.
Le lot 1 (cardio, pneumo-infectio, gastro, endocrino-néphro) est traité par un autre agent RES-06 : ses fichiers
(`journal.md`, `etat.json`, fiches CARD/PNEU/…) ne sont pas modifiés.

- 2026-11-19 — démarrage du lot 2. Lecture de `00_SYSTEME/CONVENTIONS.md` et de FIC-PNEU-0002 (lot 1) pour harmoniser le format.
- 2026-11-19 — FIC-PEDI-0001 (déshydratations), FIC-PEDI-0002 (vaccinations/PEV), FIC-PEDI-0003 (malnutrition) créées depuis DOS-PEDI-0001…0003 v1.1 (sources YAML copiées à l'identique du dossier par script).
- 2026-11-19 — FIC-NEON-0001 (ictère néonatal), FIC-NEON-0002 (infections néonatales) créées depuis DOS-NEON-0001…0002 v1.1.
- 2026-11-19 — FIC-NEUR-0001 (AVC) créée depuis DOS-NEUR-0001 v1.1.
- 2026-11-19 — FIC-MINT_REA-0001 (états de choc) créée depuis DOS-MINT_REA-0001 v1.1.
- 2026-11-19 — FIC-MINT_REA-0002 (comas) créée depuis DOS-MINT_REA-0002 v1.1.
- 2026-11-19 — FIC-URGE-0001 (intoxications aiguës) créée depuis DOS-URGE-0001 v1.1.
- 2026-11-19 — FIC-URGE-0002 (morsures et envenimations) créée depuis DOS-URGE-0002 v1.1.
- 2026-11-19 — FIC-OBST-0001 (pré-éclampsie) créée depuis DOS-OBST-0001 v1.1.
- 2026-11-19 — FIC-OBST-0002 (hémorragie de la délivrance) créée depuis DOS-OBST-0002 v1.1.
- 2026-11-19 — FIC-GYNE-0001 (GEU) créée depuis DOS-GYNE-0001 v1.1.
- 2026-11-19 — FIC-GYNE-0002 (cancer du col) créée depuis DOS-GYNE-0002 v1.1 (dossier audite_valide).
- 2026-11-19 — FIC-GYNE-0003 (tumeurs du sein) créée depuis DOS-GYNE-0003 v1.1.
- 2026-11-19 — FIC-HEMA-0001 (anémies de l'adulte) créée depuis DOS-HEMA-0001 v1.1.
- 2026-11-19 — FIC-HEMA-0002 (PTI) créée depuis DOS-HEMA-0002 v1.1.
- 2026-11-19 — FIC-HEMA-0003 (hémophilie) créée depuis DOS-HEMA-0003 v1.1 (dossier audite_valide).
- 2026-11-19 — FIC-HEMA-0004 (myélome) créée depuis DOS-HEMA-0004 v1.1 (dossier audite_valide).
- 2026-11-19 — FIC-HEMA-0005 (lymphome de Hodgkin) créée depuis DOS-HEMA-0005 v1.1 (dossier audite_valide). Les 20 fiches du lot 2 sont rédigées.
- 2026-11-19 — Contrôles qualité : (1) en-têtes YAML valides (20/20), sections 1 à 9 présentes, statut et items identiques au dossier source ; (2) 1 367 à 1 658 mots « réels » par fiche (hors balises Markdown) ; (3) vérification automatique que chaque dose chiffrée de la fiche figure dans le dossier source (écarts résiduels = simples différences de typographie « 2 à 4 g » / « 2–4 g », contrôlés un par un) ; (4) marqueurs `[POSOLOGIE À VÉRIFIER …]` / `[À VÉRIFIER]` conservés ; (5) les références [Sx] citées dans le corps mais absentes de l'en-tête sont listées en fin de section 9 (texte repris du dossier).
- 2026-11-19 — Compilation `16_RESIDANAT_ALGERIE/07_PIEGES_CLASSIQUES/PIEGES_CLASSIQUES_LOT2.md` : 200 pièges (10 par fiche), groupés par module du programme (Neurologie 10, Pédiatrie 50, Réanimation 40, Hématologie clinique 50, Chirurgie/gynéco-obstétrique 50), avec renvoi à l'item et à la fiche (numéro du piège).
- 2026-11-19 — Incohérences repérées dans les dossiers sources (signalées, **dossiers non modifiés**) :
  1. DOS-PEDI-0001 §13.3 (plan B) — sonde nasogastrique « même volume (20 mL/kg/h pendant 4 heures environ) » = 80 mL/kg, alors que le volume du plan B est de 75 mL/kg (écart mineur, à expliciter).
  2. DOS-PEDI-0002 §13.4/§21 — VPO à la naissance absent des arrêtés de 2018 et 2026 mais mentionné par le guide pratique 2023 (S5) : discordance déjà signalée par le dossier, toujours non tranchée.
  3. DOS-PEDI-0003 §13.2/§13.3/§14 — seuils d'alerte de surcharge non harmonisés : choc « FR +5/min et FC +15/min » ; transfusion « FR +5 ou FC +25/min » ; transition « FR ≥ +5 et FC ≥ +25 » (contextes OMS distincts, à expliciter) ; suivi ambulatoire « chaque semaine ou toutes les deux semaines » (§13.3) vs « suivi hebdomadaire » (§16).
  4. DOS-PEDI-0003, DOS-NEON-0001, DOS-NEON-0002 — avertissement d'en-tête « toutes les sources internationales sont verifiee: false » devenu inexact après l'audit v1.1 (plusieurs sources vérifiées) ; NEON-0002 : titre de tableau « posologies … toutes à vérifier » également dépassé.
  5. DOS-NEON-0002 — la source S1 (RBP SFN/SFP 2017, label HAS) est citée « HAS 2017 » dans le texte : libellé à harmoniser.
  6. DOS-MINT_REA-0001 vs DOS-PEDI-0002 — adrénaline IM de l'anaphylaxie chez l'enfant : maximum 0,3 mg (MINT_REA-0001 §13.2c, §16.2) vs 0,5 mg (PEDI-0002 §12.3) ; renouvellement « après 5 min » vs « toutes les 5 à 15 min ».
  7. DOS-OBST-0002 §13.2.4 — posologie de la méthylergométrine (0,2 mg IM) attribuée à [S15] dans la cellule, alors que la colonne « Source » indique [S2].
  8. DOS-HEMA-0003 — S7 (PNDS hémophilie A acquise) marquée verifiee: true avec « [date de publication à préciser] » ; S2 datée « 2019, mise en ligne juin 2023 » mais citée « PNDS 2023 » dans le texte.
- 2026-11-19 — Fin du lot 2 : 20 fiches + 1 compilation de pièges. Statut des fiches : `brouillon_a_auditer` (audit AUD à prévoir). Aucun fichier du lot 1 modifié (journal.md, etat.json, fiches CARD/PNEU/…, PIEGES_CLASSIQUES_LOT1.md).
