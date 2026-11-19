# Rapport d'audit — DOS-ORL-0003 « Cancer du cavum (carcinome du nasopharynx) : diagnostic, traitement »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-12.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**.
  - Aucun marqueur posologique restant (2 levés dans le dossier, 2 dans les cas).
  - Les textes intégraux de l'ESMO-EURACAN 2021 et de la CSCO-ASCO 2021 n'ont pas été consultés : dose cumulée ≥ 200 mg/m², 70 Gy en 33-35 fractions, rythme de surveillance.
  - NCCN non consulté.
  - Données algériennes nationales manquantes.
- **Bilan** : 11 corrections (critiques 0, majeures 0, mineures 11). AUD-01 : 6 ; AUD-02 : 5.
- **Vérifications** :
  - **Pan et al., JAMA Oncol 2024** (PMC11581663), lu en texte intégral, en particulier le tableau 2 (TNM-8 et TNM-9) ;
  - résumés PubMed des essais : Intergroup 0099, Sun 2016 (TPF), Zhang 2019 (GP en induction), Zhang 2016 (GP en métastatique), KCSG-HN10-02 (cisplatine hebdomadaire) ;
  - Feng 2009 (PMC2768108), Laouamri 2001 (résumé), registre de Sétif (Hamdi Cherif 2014, PMC4164767, texte intégral).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 7.3, TNM-9 | Référence secondaire hors liste des sources (Lee & Bae 2026, existante : PMID 41669725). | mineure | Remplacée par le tableau 2 de S4. Précisions ajoutées : T inchangées sur le fond, infiltration osseuse « non équivoque » pour T3 ; pour T4, nerfs crâniens (atteinte non équivoque), orbite y compris la fissure orbitaire inférieure, face antérolatérale du ptérygoïdien latéral. | [S4] |
| S4 | Référence incomplète. | mineure | JAMA Oncol. 2024;10(12):1627-1635 (+ erratum). | PMID 39388190 |
| S5 (AJCC 8e éd.) | `verifiee: false`. | mineure | Ouvrage non consulté, mais définitions T/N/M et groupes de stades de la TNM-8 contrôlés dans le tableau 2 de S4 : passé à `verifiee: true` avec cette mention. | [S4] |
| § 3.2, Algérie | Épidémiologie entièrement `[À VÉRIFIER]`. | mineure | Registre de Sétif : ASR 5,0/100 000 chez l'homme (5 % des cancers masculins) et 2,1 chez la femme en 2006-2010 ; baisse chez l'homme de −3,4 %/an entre 1996 et 2010. Données régionales : `[À VÉRIFIER]` maintenu pour le niveau national. | [S15] |
| § 3.2, étude de Sétif | Effectif absent. | mineure | 72 cas et 72 témoins (résumé). | [S13] |
| § 13.2.2, chimiothérapie concomitante (AUD-02) | Marqueur posologique. | mineure | Levé. Cisplatine 100 mg/m² J1, J22, J43 (Intergroup 0099, bras de RCC des essais d'induction). Cisplatine 40 mg/m² par semaine, 7 administrations (KCSG-HN10-02, phase II randomisée). Dose cumulée ≥ 200 mg/m² rattachée à S1 et S3 (textes non relus). | [S8], [S6], [S7], [S16] |
| § 13.2.2, induction (AUD-02) | Marqueur posologique. | mineure | Levé, avec le nom des protocoles conservé. **GP** : gemcitabine 1 000 mg/m² J1 et J8 + cisplatine 80 mg/m² J1, toutes les 3 semaines × 3. **TPF** : docétaxel 60 + cisplatine 60 + 5-FU 600 mg/m²/j en perfusion continue J1-J5, toutes les 3 semaines × 3. Doses des essais, à adapter selon le RCP et le centre. | [S6], [S7] |
| § 13.2.2, adjuvant | Schéma non chiffré. | mineure | Cisplatine 80 mg/m² J1 + 5-FU 1 000 mg/m²/j J1-J4, toutes les 4 semaines × 3 (Intergroup 0099). | [S8] |
| § 13.2.2, métastatique | Schéma GP non chiffré. | mineure | Gemcitabine 1 000 mg/m² J1 et J8 + cisplatine 80 mg/m², toutes les 3 semaines, 6 cycles au plus. | [S9] |
| § 17, cas (AUD-02) | Marqueur posologique. | mineure | Levé (cisplatine 100 mg/m² toutes les 3 semaines ; dose cumulée ≥ 200 mg/m²). | [S1], [S3], [S6] |
| § 13.4, Algérie | Affirmations non sourcées (prise en charge, IMRT, anti-PD-1). | mineure | Reformulées ; `[À VÉRIFIER]` maintenus. | [S15] |

## Points vérifiés sans modification

- **TNM-8** (contrôlée via S4) :
  - T1-T4, N1-N3 ;
  - stades : I = T1N0 ; II = T1N1 ou T2N0-1 ; III = T1-2N2 ou T3N0-2 ; IVA = T4 ou N3 ; IVB = M1.
- **TNM-9** (S4) :
  - 4 914 patients ;
  - extension extraganglionnaire radiologique avancée = N3 ;
  - stades IA = T1-2N0, IB = T1-2N1, II = T3 ou N2, III = T4 ou N3 ;
  - IVA = M1a (≤ 3 lésions), IVB = M1b (> 3 lésions) ;
  - application en janvier 2025.
- **Cas cliniques** : CAS-ORL-1205 (T4N2M0 : IVA en TNM-8, III en TNM-9) et CAS-ORL-1206 (T2N3M0 : IVA, puis III) exacts.
- **Feng 2009** :
  - 636 cas et 615 témoins ;
  - tabac associé aux formes différenciées seulement ;
  - cannabis et kanoun pendant l'enfance associés au risque ;
  - ni l'alcool ni la chicha ne sont associés.
- **Laouamri 2001** : beurre rance (risque × 4 à 7), conserves marinées (× 4 à 12).
- **Chan 2017** : 20 174 hommes de 40 à 62 ans.

## QCM et cas associés

- **QCM-ORL-1225 à 1236** : exacts ; QCM-ORL-1228 (T2N2 = stade III) et QCM-ORL-1229 vérifiées sur le tableau de Pan 2024 → 12 `audite_valide`.
- **CAS-ORL-1205 et CAS-ORL-1206** : marqueurs levés (doses de l'essai GP et cisplatine 100 mg/m² toutes les 3 semaines) → `audite_valide`.

## Reste à faire

1. Texte intégral de l'ESMO-EURACAN 2021 et de la CSCO-ASCO 2021 : dose cumulée, dose et fractionnement de l'IMRT, stade II, rythme de surveillance.
2. NCCN (version en vigueur) ; place des anti-PD-1 après JUPITER-02.
3. GLOBOCAN 2022 : chiffres pour l'Algérie ; registres nationaux ; proportion des formes juvéniles.
4. Accès à l'IMRT et aux anti-PD-1 en Algérie (Plan cancer, nomenclature).
5. Relecture enseignant (oncologue radiothérapeute).
