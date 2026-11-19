# Rapport d'audit — DOS-HEPA-0002 « Cirrhoses »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (scientifique), AUD-02 (posologies), AUD-04 (références) — IA
- **Objets audités** : dossier v1.0 (DOS-04) ; QCM-HEPA-0413…0424 ; CAS-HEPA-0403, CAS-HEPA-0404 (lots DOS-04).
- **Verdict** : `audite_corrections_requises` (v1.1). Aucune erreur critique. Trois erreurs majeures corrigées. Plus aucun marqueur `[POSOLOGIE À VÉRIFIER]`. Toutes les références sont vérifiées.
- **Points ouverts** (voir « Reste à faire ») : dose maximale de paracétamol, seuil de MELD pour l'orientation vers la greffe, traitements de l'hépatite auto-immune, de l'hémochromatose et de la maladie de Wilson non sourcés, positions AASLD et FDA non relues.
- **Moyens de vérification** :
  - texte intégral de Baveno VII (PMC11090185) ;
  - PDF OMS 2024 sur le VHB (tableau 17.1) ;
  - PubMed ;
  - une recherche web sur la posologie du carvédilol ;
  - méthodes de PREDESCI, relevées dans une revue systématique (Hepatol Commun 2024, PMC10830085).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §13.2.2 | Carvédilol : posologie attribuée à Baveno VII, qui n'en donne pas ; objectif « dose maximale tolérée » ambigu (risque d'escalade sans borne) | majeure (posologie) | 6,25 mg/j, puis 12,5 mg/j (dose cible usuelle). Titration jusqu'à 25 mg/j au maximum dans PREDESCI, avec PAS > 90 mmHg et FC > 55/min. Propranolol selon le schéma de PREDESCI (40 → 160 mg × 2/j). Nadolol ajouté | PREDESCI [S14] ; Baveno VII 5.14–5.15 |
| Lot cas | CAS-HEPA-0404 incohérent avec l'algorithme du dossier : IRA « stade 1B » alors que la créatinine (132 µmol/L) correspond au stade 1A, traitée par albumine 1 g/kg ; restriction hydrique pour une hyponatrémie « liée aux diurétiques » | majeure | Créatinine portée à 142 µmol/L (× 1,67, stade 1B, albumine justifiée). Hyponatrémie : arrêt des diurétiques et expansion par albumine ; restriction hydrique seulement si l'hyponatrémie reste hypervolémique | EASL 2018 [S1] (critères ICA) |
| YAML / §22 | Neuf références `verifiee: false` (S10–S18) sans DOI | majeure (traçabilité) | Toutes confirmées (DOI, PMID). Ajout de S19 (EASL CBP 2017, posologie de l'AUDC) et de S20 (OMS VHB 2024, adaptation rénale) | PubMed 4541913, 11172350, 33942342, 35724930, 30910320, 29861076, 10432325, 33657294, 30144956, 28427765 |
| §1.2 | Définition de la recompensation incomplète | mineure | Trois conditions, dont l'absence de décompensation pendant au moins 12 mois. Les BBNS ne sont pas arrêtés tant que l'HTPCS persiste | Baveno VII 7.23–7.24 |
| §7.3 | Règle des 25 kPa : précision sur l'IMC absente ; mention « à vérifier » | mineure | Vérifié. Précision « NASH non obèse (IMC < 30) ». Une mesure ≥ 10 kPa doit être répétée à jeun ou complétée par un FIB-4 ≥ 2,67 | Baveno VII 2.4, 2.11, 2.15–2.16 |
| §9.4 | Indications de l'endoscopie de dépistage | mineure | Patient ne pouvant recevoir de BBNS : endoscopie si élastométrie ≥ 20 kPa ou plaquettes ≤ 150 G/L. Patient ascitique non traité : endoscopie indiquée | Baveno VII 2.19, 7.3 |
| §13.2.1 | AUDC 13–15 mg/kg/j sous marqueur | mineure | Marqueur levé | EASL CBP 2017 [S19] |
| §13.2.2 | Indications et précautions des BBNS | mineure | Chez l'ascitique : BBNS ou carvédilol préférés à la ligature pour les varices à haut risque ; réduction ou arrêt si PAS < 90 mmHg, PAM < 65 mmHg ou SHR-IRA, puis reprise | Baveno VII 7.6–7.8 |
| §13.2.3 | Diurétiques sous marqueur | mineure | Levé : schéma par paliers de l'EASL 2018 (spironolactone 100 → 400 mg, furosémide 40 → 160 mg) | EASL 2018 [S1] |
| §13.2.3 | Albumine après paracentèse | mineure | Ajout de la fourchette AASLD 2021 (6–8 g par litre) à côté de l'EASL 2018 (8 g par litre au-delà de 5 L) | [S1, S12] |
| §13.2.4 | Norfloxacine sous marqueur | mineure | Dose de 400 mg/j sourcée (EASL 2018). Seule la disponibilité en Algérie reste `[À VÉRIFIER]` | [S1] |
| §13.2.5 | Terlipressine sous marqueur | mineure | Levé : schéma EASL 2018 (1 mg toutes les 4–6 h ou 2 mg/24 h, jusqu'à 12 mg/24 h, avec albumine 20–40 g/j). Recherche d'une surcharge et d'une hypoxémie avant traitement (CONFIRM) | [S1, S17] |
| §13.2.7 | Encéphalopathie sous marqueur | mineure | Levé : lactulose titré pour 2–3 selles par jour, rifaximine 550 mg × 2/j | EASL 2022 [S13] ; RCP |
| §13.2.9 | Apports nutritionnels « non revérifiés » | mineure | Confirmés : au moins 35 kcal/kg/j et 1,2–1,5 g/kg/j de protéines | EASL 2019 [S18] |
| §13.2.11 | Critères de futilité du TIPS | mineure | Child ≥ 14, ou MELD > 30 avec lactates > 12 mmol/L. TIPS envisagé dès 3 grandes paracentèses ou plus par an | Baveno VII 6.31, 7.4 |
| §17 Q1 | IRA « stade 1B/2 » | mineure | Stade 1B (créatinine × 1,5 et > 133 µmol/L) | Critères ICA [S1] |
| §17 Q2 | Entécavir sous marqueur | mineure | 1 mg/j à jeun, réduit à 0,5 mg/j (ou 1 mg toutes les 48 h) si la clairance est de 30–49 mL/min ; TAF en alternative | OMS 2024, tableau 17.1 [S20] |
| Bandeau | Statut | mineure | Mis à jour | — |
| Lot cas | CAS-HEPA-0403 : FIB-4 « ≈ 4,3 » | mineure | Recalculé : ≈ 4,2 | — |
| Lot QCM | QCM-HEPA-0418 | mineure | Ajout de la fourchette AASLD (6–8 g par litre) | [S12] |
| Lot cas | Statuts | mineure | CAS-HEPA-0403 et 0404 passés en `audite_valide` | — |

Total : 21 corrections (3 majeures), aucune critique.

**Posologies contrôlées et exactes** (EASL 2018 sauf mention) :
- sodium : 80–120 mmol/j ;
- spironolactone 100 → 400 mg et furosémide 40 → 160 mg ;
- objectif de perte de poids ≤ 0,5 ou ≤ 1 kg/j ;
- albumine : 8 g par litre (paracentèse > 5 L), 1,5 g/kg puis 1 g/kg (ILA), 1 g/kg/j pendant 2 jours (IRA) ;
- terlipressine ;
- norfloxacine 400 mg/j ;
- rifaximine 550 mg × 2/j ;
- correction de la natrémie ≤ 8 mmol/L par 24 h.

**Classifications et scores contrôlés** :
- Child-Pugh : barème exact ; calculs justes dans le QCM 1 (B8), le QCM-HEPA-0413 (C12), le cas (C13) et CAS-GAST-0401 (C12) ;
- MELD et MELD-Na ;
- West Haven ;
- critères ICA et SHR-IRA ;
- grades de l'ACLF selon l'EASL-CLIF ;
- « règle des 5 » de Baveno VII.

## QCM et cas

- QCM-HEPA-0413…0424 : exacts ; `audite_valide`.
- CAS-HEPA-0403 et 0404 : corrigés ; `audite_valide`.

## Références (AUD-04)

- **Avant** : 9/18 vérifiées.
- **Après** : 20/20.

## Reste à faire

1. Paracétamol chez le cirrhotique : fixer la dose maximale à partir d'une source (RCP ou recommandation).
2. MELD ≥ 15 comme seuil d'orientation vers la greffe : citer la recommandation (EASL ou AASLD, transplantation).
3. Traitements de l'hépatite auto-immune, de l'hémochromatose et de la maladie de Wilson : citer les recommandations EASL correspondantes.
4. Albumine au long cours : relire la position AASLD 2021. Terlipressine : relire les précautions de la FDA.
5. Données épidémiologiques mondiales et algériennes (MASLD, alcool, transplantation hépatique).
6. Grossesse et cirrhose : sourcer.
7. Confirmer le schéma « 6,25 → 12,5 mg/j » du carvédilol dans une recommandation (Baveno VI ou AASLD 2024), au-delà de PREDESCI.
