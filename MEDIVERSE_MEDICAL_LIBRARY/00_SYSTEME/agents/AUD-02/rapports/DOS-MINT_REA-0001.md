# Rapport d'audit — DOS-MINT_REA-0001 « États de choc »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, auditeur indépendant du rédacteur (DOS-06)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1), QCM-MINT_REA-0001 à 0012, CAS-MINT_REA-0001 et 0002
- **Verdict** : `audite_corrections_requises` (aucune erreur critique ; 1 erreur majeure corrigée ; 3 marqueurs de posologie conservés)

## Vérifications effectuées
- **Adrénaline** IM 0,01 mg/kg de la solution à 1 mg/mL, max 0,5 mg adulte (0,3 mg enfant), cuisse, répétable à 5 min — **exacte** (WAO 2020, EAACI 2021). Bolus IV de 1 mg réservé à l'arrêt cardiaque — **exact**.
- **Sepsis-3** (SOFA ≥ 2 ; choc septique = vasopresseur pour PAM ≥ 65 + lactate > 2 mmol/L) ; **qSOFA** (FR ≥ 22, conscience, PAS ≤ 100) — **exacts**.
- **SSC** : 30 mL/kg en 3 h, noradrénaline en première intention, vasopressine 0,03 U/min, adrénaline en 3e ligne, hydrocortisone 200 mg/j, Hb < 7 g/dL, bicarbonate si pH ≤ 7,20 avec IRA, HEA proscrits — **exacts**. Statut SSC 2026 confirmé (Crit Care Med 2026;54(4):725-812 et Intensive Care Med 2026;52(5):863-936 ; catalogue REC-0266) : 30 mL/kg maintenu (certitude faible, poids ajusté si IMC > 30), certitude des corticoïdes abaissée à « faible », NEWS/MEWS/SIRS préférés au qSOFA (recommandation forte).
- **Choc hémorragique** : PAS 80–90 (PAM ≥ 80 si TC grave), acide tranexamique 1 g/10 min puis 1 g/8 h (< 3 h), fibrinogène si < 1,5 g/L (3–4 g), ratio plasma/CGR ≥ 1:2, Hb 7–9 g/dL — **exacts** (guide européen 2023).
- **SCAI A–E**, DanGer Shock (45,8 % contre 58,5 %, HR 0,74), classes ATLS, Ring et Messmer, tests de précharge-dépendance (LJP ≥ 10 %, VPP > 12–13 %, occlusion télé-expiratoire ≥ 5 %) — **exacts**.
- QCM (12) et cas (2) : réponses exactes.

## Corrections apportées

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 21 | Affirmation non étayée : « SSC 2026 : noradrénaline **ou** adrénaline en première intention ; noradrénaline préférée en cas de tachyarythmie » (formulation proche de la SSC pédiatrique, pas de la SSC adulte) | **Majeure** | Ligne réécrite : la SSC 2026 garde la noradrénaline en première intention (suggestion de force abaissée) et suggère, en cas de dysfonction cardiaque, dobutamine ajoutée ou adrénaline seule (certitude très faible) | S1 (résumés SCCM/ESICM, synthèses secondaires) |
| § 13.2-d, § 17, § 20.2, § 21 | Critère de l'hydrocortisone mal restitué (« ≥ 0,25 µg/kg/min **depuis** 4 h ») | Mineure | « dose ≥ 0,25 µg/kg/min au moins 4 h après le début du vasopresseur » (formulation SSC 2021) ; idem dans QCM-MINT_REA-0006 et CAS-MINT_REA-0001 (JSON) | S2 |
| § 13.2-c | Dobutamine 2,5–20 µg/kg/min sous [POSOLOGIE À VÉRIFIER] | Mineure (levée) | 2 à 20 µg/kg/min, perfusion continue sans bolus — marqueur levé | ESC 2021 IC [S10] (tableau des inotropes) |
| § 13.2-c | Noradrénaline : risque d'erreur base/tartrate non signalé | Mineure | Avertissement ajouté (facteur ≈ 2) ; marqueur maintenu | Pharmacologie (RCP) |
| § 13.2-b, § 21 | SSC 2026 « formulation similaire » sur le remplissage | Mineure | Précisé : suggestion maintenue, certitude faible, poids ajusté/idéal si IMC > 30 | S1 |
| § 8.3, § 21 | qSOFA : force de la recommandation SSC 2026 non précisée | Mineure | « recommandation forte, certitude modérée » | S1 |
| § 20.2 (QCM 6-C) | Suggestion attribuée à la seule SSC 2026 | Mineure | « SSC 2021, maintenue en 2026 » (dossier et JSON) | S1, S2 |
| YAML S1, § 22 | Référence SSC 2026 incomplète | Mineure | Auteurs, volume, pages, co-publication ICM | Catalogue REC-0266 ; recherche |
| En-tête | Statut, version, bloc `audit` | — | v1.1 | Protocole |

## Reste à faire
1. Marqueurs de posologie conservés : noradrénaline (dose initiale et unité base/tartrate selon le protocole local) ; adrénaline IV titrée dans l'anaphylaxie réfractaire ; glucagon chez le patient sous bêtabloquant (également dans CAS-MINT_REA-0002, statut `audite_corrections_requises`).
2. Lire le texte intégral de la SSC 2026 (libellés exacts, dont adrénaline et vasopressine) ; envisager de citer la SSC pédiatrique 2026, parue, qui remplace la version 2020 (REC-0267).
3. Sources non vérifiées : S13 (Resuscitation Council UK 2021), S14 (SFMU 2016), S15 (essais) ; remplissage de l'anaphylaxie (volumes) [À VÉRIFIER].
4. Données algériennes (épidémiologie, disponibilité des auto-injecteurs et de la vasopressine) [À VÉRIFIER].
