# Rapport d'audit — DOS-PHYS-0001 « Équilibre acido-basique »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-13
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_valide`** (0 critique, 0 majeure, 7 mineures ; aucun marqueur restant) — relecture enseignante requise pour `valide_enseignant`.

## Documents lus pendant l'audit
- SRLF/SFMU 2019 [S11], texte intégral (PMC6695455) : R1.1–R3.14 avec leurs grades, valeurs du trou anionique (12 ± 4 sans K+, 16 ± 4 avec K+), formule du TA corrigé, résumé de BICAR-ICU.
- Consensus ADA/EASD/JBDS/AACE/DTS 2024 [S19], version Diabetologia en texte intégral (PMC11343900) : critères D-K-A, sévérité, bolus d'insuline, bicarbonate.
- Résumé PubMed de BICAR-ICU [S17] (PMID 29910040).

## Contrôles des points prioritaires
- Henderson-Hasselbalch : pK' 6,1 ; 0,03 mmol/L/mmHg (0,23 en kPa) ; forme d'Henderson 24 × PaCO2/HCO3- ; table pH ↔ [H+] : **conformes**.
- Gaz du sang normaux (pH 7,35–7,45 ; PaCO2 35–45 mmHg ; HCO3- 22–26 ; EB ± 2) : **conformes**.
- TA sans K+ (12 ± 4) et avec K+ (16 ± 4), correction + 0,25 × (40 − albumine), delta ratio (< 1 / 1–2 / > 2), trou osmolaire : **conformes** ([S11] texte intégral).
- Winter 1,5 × HCO3- + 8 ± 2 (et version kPa), alcalose métabolique + 0,7, respiratoires 0,1/0,35 et 0,2/0,4 avec limites : **conformes** (Adrogué-Madias).
- Recommandations SRLF/SFMU citées (bicarbonate, épuration, ventilation, lactate, cétonémie) : **conformes** aux grades du texte intégral.
- Cohérence interne des gaz du sang recalculée pour tous les exemples : une incohérence (QCM 4).

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 8.5 | « l'hypercapnie s'accompagne obligatoirement d'une hypoxémie » (faux pour une hypercapnie modeste) | Mineure | Toute hausse de PaCO2 abaisse la PAO2 ; hypoxémie dès que l'hypercapnie est notable | Équation des gaz alvéolaires (§ 9.9) |
| 10.1 | Critères de l'acidocétose incomplets (pas de critère A ; seuil glycémique imprécis) | Mineure | Critères D-K-A 2024 complets (≥ 11,1 mmol/L ou diabète connu ; β-OHB ≥ 3,0 ou cétonurie ≥ 2+ ; pH < 7,30 et/ou HCO3- < 18), alignés sur DOS-DIAB-0002 | [S19] texte intégral |
| 14.2 | SSC 2021 : « recommande de ne pas » alors qu'il s'agit d'une suggestion (faible) | Mineure | « suggère (recommandation faible) » | [S18] |
| 14.2 | Marqueur `[POSOLOGIE À VÉRIFIER]` sans dose proposée | Mineure | Marqueur levé : dossier sans posologie ; modalités BICAR-ICU (4,2 %, pH cible ≥ 7,30) et seuil pH < 7,0 de l'acidocétose avec renvoi à DOS-DIAB-0002 | [S11], [S17], [S19] |
| 17 (Q7) | Bolus d'insuline : précision manquante | Mineure | Bolus seulement si accès veineux retardé (consensus 2024) ; pas de bolus (SRLF R3.2) | [S11], [S19] |
| 20 (QCM 4) | Gaz du sang incohérents : pH 7,25 avec PaCO2 32 et HCO3- 12 (Henderson : 7,19) | Mineure | pH 7,20 ; contrôle de cohérence ajouté (aussi dans le lot, QCM-PHYS-1304) | Henderson |
| 21 | Seuil du bicarbonate dans l'acidocétose `[À VÉRIFIER]` | Mineure | « à envisager seulement si pH < 7,0 » | [S19] texte intégral |

## Lot (QCM, cas)
- 13 QCM (QCM-PHYS-1301 à 1313) relus ; 1 corrigé (1304) ; 13/13 `audite_valide`.
- CAS-PHYS-1301 (BPCO + alcalose métabolique) : gaz cohérents ; nuance ajoutée (compensation rénale partielle après 4 jours ; argument décisif = hypochlorémie + hypokaliémie) ; marqueur KCl remplacé par un renvoi (DOS-NEPH-0002). `audite_valide`.
- CAS-PHYS-1302 (méthanol) : Winter, TA, trou osmolaire recalculés, exacts ; seuil d'épuration (TA > 20) conforme à R3.12 ; marqueur remplacé par un renvoi (RCP, centre antipoison, DOS-URGE-0001). `audite_valide`.

## Reste à faire
- Aucun point bloquant. Relecture enseignante (statut `valide_enseignant`).
- Facultatif : référence algérienne (protocoles de réanimation) si un texte national est publié.
