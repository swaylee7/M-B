# Rapport d'audit — DOS-INFE-0005 « Infection à VIH »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-02, lot 2)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1) ; QCM-INFE-0227 à 0239 ; CAS-INFE-0205 et 0206 (`DOS-02-lot2.json`)
- **Verdict** : `audite_corrections_requises` — 0 erreur critique ; 1 erreur majeure corrigée ; 18 corrections mineures ; **marqueurs `[POSOLOGIE À VÉRIFIER]` restants : 3 dans le dossier (toxoplasmose cérébrale, candidose oro-œsophagienne, fluconazole du cas du § 17) + 1 dans CAS-INFE-0205 (lot)** ; 9 levés (dossier et lot)
- **Sauvegarde** : `00_SYSTEME/sauvegardes/20261119/07_MEDECINE_INTERNE/28_INFE_INFECTIOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-INFE-0005__INFECTION_A_VIH.avant_audit.md`

## Vérifications sur les textes
- **OMS 2021, lignes directrices consolidées (DOC-00029)** — annexe 1 : TDF 300 mg, 3TC 300 mg, DTG 50 mg ; **TLD 1 cp/j dès 30 kg** ; **DTG 50 mg × 2/j avec la rifampicine et 2 semaines après la dernière dose** ; RAL 800 mg × 2/j sous rifampicine ; EFV 400/600 mg ; DRV/r 800/100 mg/j ; NVP 200 mg/j puis × 2/j ; interactions du DTG (cations polyvalents, inducteurs, metformine). Cotrimoxazole : stade 3–4 et/ou CD4 ≤ 350, tuberculose active, nourrissons exposés dès 4–6 semaines ; dose adulte = 1 cp à 800/160 mg/j (tableau A1.6) ; névirapine néonatale 1,5 mL de la solution à 10 mg/mL de 0 à 6 semaines (tableau A1.7). Glossaire : suppression < 50 copies/mL, échec > 1 000 copies/mL après ≥ 6 mois ; virémie de bas niveau 50–1 000. PrEP 2+1+1 (HSH cisgenres), 7 jours d'amorce pour les autres populations ; PPE ≤ 72 h, 28 jours, AZT + 3TC chez l'enfant ≤ 10 ans. Cryptococcose (compilation de 2021 : consolidation 400–800 mg/j). **Conformes**, sauf la consolidation (voir ci-dessous).
- **OMS 2025, mise à jour clinique (DOC-00057)** : DTG + 3TC et CAB + RPV sans hépatite B active ; RPV incompatible avec la rifampicine ; prophylaxie du nourrisson (NVP 6 semaines ; trithérapie si haut risque ; définitions du haut risque) ; allaitement ; **3HP « suggéré comme schéma préféré » (recommandation conditionnelle, certitude faible)**.
- Lus pendant l'audit (IRIS) : **OMS 2022 cryptococcose** (consolidation **800 mg/j** ; préemptif 800–1 200 mg/j 2 semaines ; ponctions évacuatrices), **OMS 2022 cabotégravir en PrEP**, **OMS 2025 lénacapavir**.
- **RCP Vocabria/Rekambys (EMA)** : schéma bimestriel confirmé par extraits (site de l'EMA inaccessible). **Pneumocystose** : posologies NIH confirmées par deux extraits secondaires concordants (clinicalinfo.hiv.gov inaccessible).
- PubMed : PARTNER (PMID 31056293) confirmé.
- QCM-INFE-0227 à 0239 : réponses exactes. CAS-INFE-0205 et 0206 : exacts.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 12.3 (cryptococcose), § 20 (QCM 10) et QCM-INFE-0236 | Consolidation « fluconazole 400–800 mg/j » : borne basse de la compilation de 2021, **remplacée** par 800 mg/j dans les lignes directrices spécifiques de 2022 | **Majeure** (actualité d'une posologie) | 800 mg/j pendant 8 semaines ; entretien 200 mg/j jusqu'à CD4 > 200 et charge virale supprimée ; divergence 2021/2022 datée | S3 (OMS 2022) |
| § 12.3 (antigénémie isolée) | Traitement préemptif sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | 800–1 200 mg/j pendant 2 semaines puis consolidation et entretien | S3 |
| § 12.3 (pneumocystose) | Traitement sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | TMP 15–20 + SMX 75–100 mg/kg/j, 21 jours ; prednisone si PaO₂ < 70 mmHg (schéma dégressif) | S14 (par extraits) |
| § 13.2 (CAB + RPV) | Posologie absente (marqueur) | Mineure (levée) | 600/900 mg IM à M1 et M2 puis tous les 2 mois (phase orale facultative) ; RPV et rifampicine incompatibles | S13, S2 |
| § 13.4 | Cotrimoxazole prophylactique sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | 800/160 mg 1×/j (adulte, ≥ 25 kg) ; tranches de poids chez l'enfant | S1 (tableau A1.6) |
| § 15.2 | PrEP par cabotégravir sous marqueur | Mineure (levée) | 600 mg IM, 2 injections à 4 semaines puis toutes les 8 semaines | S12 |
| § 15.2 | PrEP par lénacapavir sous marqueur | Mineure (levée) | 927 mg SC toutes les 26 semaines + 600 mg per os à J1 et J2 | S11 |
| CAS-INFE-0206 (lot) | Dose néonatale de névirapine sous marqueur | Mineure (levée) | 15 mg (1,5 mL à 10 mg/mL) 1×/j de 0 à 6 semaines | S1 (tableau A1.7) |
| § 17 et CAS-INFE-0205 | Cotrimoxazole sous marqueur | Mineure (levée) | 800/160 mg/j | S1 |
| § 12.3 | Ponctions évacuatrices `[À VÉRIFIER]` | Mineure | Objectif < 20 cmH₂O ou moitié de la pression initiale, répétées chaque jour si symptômes | S3 |
| § 13.2 (DTG) | Interactions `[À VÉRIFIER]` | Mineure | Cations polyvalents (2 h avant / 6 h après), inducteurs, metformine | S1 |
| § 13.4, § 21 | « 3HP préféré » sans nuance | Mineure | « Suggéré comme schéma préféré » (conditionnelle, 2025) | S2 |
| § 6, § 15.1 | « Indétectable = intransmissible » `[À VÉRIFIER — référence]` | Mineure | PARTNER vérifiée et contextualisée | S9 |
| § 12.3 (toxoplasmose) | Marqueur sans explication | Mineure | Marqueur **maintenu** et motivé (sources consultées discordantes) | — |
| § 3.2, § 13.5 | Protocoles nationaux non qualifiés | Mineure | Guide national de TAR/PTME **non retrouvé** ; estimations ONUSIDA/OMS non retrouvées | Recherche (audit) |
| § 15.4 | Position algérienne sur l'allaitement absente | Mineure | « Non retrouvée » `[À VÉRIFIER]` | — |
| YAML, § 22 | S3 non lue ; S9 non vérifiée ; sources des posologies absentes | Mineure | S3 lue, S9 vérifiée ; S11–S14 ajoutées | IRIS, PubMed |
| En-tête | Statut, version, bloc `audit` | Mineure | v1.1 | Protocole |

## Reste à faire
1. **Toxoplasmose cérébrale** : posologies (pyriméthamine — dose de charge et dose selon le poids —, sulfadiazine, acide folinique, cotrimoxazole) à lire dans les recommandations NIH ou EACS en vigueur (sites inaccessibles pendant la session) — marqueur conservé.
2. **Candidose oro-œsophagienne** : dose et durée du fluconazole (IDSA 2016 ou NIH) — marqueur conservé (dossier et CAS-INFE-0205).
3. IRIS (corticoïdes), CMV, leishmaniose viscérale, VIH-2, stades OMS complets, délais des marqueurs virologiques : `[À VÉRIFIER]` non posologiques conservés.
4. Données algériennes : estimations ONUSIDA, chiffres officiels du ministère (S8, presse), protocole national de TAR et de PTME, position sur l'allaitement — **non retrouvés**.
5. Confronter le schéma de CAB + RPV au RCP enregistré en Algérie (le cas échéant).
