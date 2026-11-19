# Journal — RES-03

Mission : Banque QCM — médecine

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19 — démarrage : lecture CONVENTIONS, schéma QCM, programme (75 items RES-MED attribués), catalogues recommandations (340) et ouvrages. Outil d'assemblage (définitions compactes → JSON) + validateur dans le scratchpad de session. Plage d'ids : QCM-<CODE>-3001…3225 (3001 + 3×rang de l'item + n).
- 2026-11-19 — lots 1-3 assemblés dans RES-03-a.json : 72 QCM (MED-001 → MED-031, 24 items × 3), validation 0 erreur. Suite : MED-032 → 052.
- 2026-11-19 — lot 4 : MED-032 → 039 (24 QCM) ; RES-03-a.json = 96 QCM, 0 erreur. Note : banque_qcm.json fusionne déjà les lots (indexer) — validateur adapté pour exclure les entrées RES-03 de la banque.
- 2026-11-19 — lot a TERMINÉ : RES-03-a.json = 126 QCM (42 items MED-001 → 052 × 3). Lot b démarré : MED-054, 055, 058, 061 (12 QCM). Total 138, 0 erreur.
- 2026-11-19 — lots 7-8 : MED-062 → 082 (48 QCM) ; RES-03-b.json en cours. Total 186 QCM, 0 erreur. Reste : ENDO (083→097) et RHUM (098).
- 2026-11-19 — lots 9-10 : ENDO (083 → 097) et RHUM (098). **Mission terminée : 225 QCM, 75 items × 3** — RES-03-a.json (126, MED-001→052), RES-03-b.json (99, MED-054→098). Validation : 0 erreur (5 propositions A–E, réponses ⊂ propositions, QCS = 1 réponse, ids uniques sur tous les lots, plage 3001–3225, items existants, spécialité = 1er code, origine originale_mediverse, annale nulle).
  - Formats : 188 QCM / 37 QCS (16 %) ; difficulté 1/2/3 = 44/138/43 ; nb de réponses justes 1/2/3/4/5 = 37/7/89/84/8.
  - Sources : recommandations du catalogue (REC-xxxx, citées par organisme, titre, année) et ouvrages du catalogue (OUV-xxxx). Aucune posologie non standard ; seules doses chiffrées : benzathine-pénicilline 2,4 MUI (syphilis précoce, CDC 2021/OMS 2024) et vitamine D 400 UI/j (Munns 2016).
  - Points à auditer : contenus 2025-2026 non lus en détail (SSC 2026, ESC/EACTS valvulopathies 2025 — seuils marqués [À VÉRIFIER], ESC myocardite-péricardite 2025, McDonald 2024 [À VÉRIFIER], ECCO RCH 2026, ESC FA 2024 CHA2DS2-VA, OMS TB module 4 2026 pour la durée du mal de Pott chez l'adulte, AHA/ACC EP 2026) ; position ESPGHAN 2017 sur le lait de vache < 12 mois (non cataloguée, [À VÉRIFIER]) ; faits algériens non chiffrés à sourcer (certification OMS « exempt de paludisme » 2019, rage canine endémique, hémoglobinopathies/G6PD) ; durée Maastricht VI « 10 jours » pour la quadrithérapie bismuthée galénique combinée ; seuil français de l'IRC (PaO2 < 70 mmHg).
