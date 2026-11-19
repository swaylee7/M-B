# Journal — RES-04

Mission : Banque QCM — chirurgie

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19 — démarrage : lecture CONVENTIONS, schéma QCM, programme (60 items RES-CHI sans QCM), catalogues REC/OUV. Outil DSL → JSON + validateur (scratchpad). Références hors catalogue vérifiées via Europe PMC (PMID notés dans les sources).
- 2026-11-19 — lot a : 36 QCM (CHI-001 → 014, hors 010/012), validation 0 erreur. Ids QCM-<CODE>-4001 → 4036.
- 2026-11-19 — lot a (RES-04-a.json) terminé : 90 QCM, 30 items (CHI-001 → 032 hors 010/012), 3 QCM/item, 0 erreur ; QCS 16 (18 %). Ids 4001 → 4090.
- 2026-11-19 — lot b (RES-04-b.json) terminé : 90 QCM, 30 items (CHI-033 → 067 hors 056/057/058/062/066), ids 4091 → 4180.
- 2026-11-19 — contrôle qualité : propositions mélangées de façon déterministe (sauf 13 QCS à ordre signifiant : grades/classifications) ; nombre de bonnes réponses varié (QCM : 2 → 31, 3 → 63, 4 → 54, 5 → 4) ; 63 propositions réécrites (vrai ↔ faux). QCS 28 (16 %). Validation python3 : 180 QCM, 5 propositions, réponses ⊂ propositions, ids uniques sur tous les lots, items existants, préfixes Vrai/Faux cohérents → 0 erreur.
- 2026-11-19 — sources : catalogue REC/OUV + articles vérifiés via Europe PMC (PMID indiqués). Références incomplètes marquées À VÉRIFIER : ESCMID abcès cérébral 2024 (volume/pages), manuel OMS du sperme 2021 (hors catalogue).
- Points à auditer : (1) QCM-UROL-4081 sus-pubien vs urétral dans la prostatite aiguë (recommandations évolutives) ; (2) œsophage/estomac rédigés d'après ESMO 2022 — vérifier la position ESMO 2026 (REC-0371, FLOT vs CROSS) ; (3) classifications sans source primaire vérifiée (Garden, Pauwels, Cauchoix-Duparc, Ladd, Sher, Kirkendall non utilisée) citées via traités ; (4) chiffres à recontrôler : Parkland, Baux révisé (+17), seuil PIC 22 mmHg, baisse de 20-25 % de la PAM (HTA maligne), objectifs glycémiques ADA, durées HAS de l'OMA, échographie de hanche à 1 mois (HAS 2013) ; (5) prévalences indicatives (atrésie type III ≈ 85 %, résécabilité pancréas 15-20 %).
