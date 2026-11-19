# Rapport d'audit — DOS-OBST-0002 « Hémorragie de la délivrance : diagnostic et traitement »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-07)
- **Objets audités** : dossier v1.0 ; QCM-OBST-0713 à 0724 et CAS-OBST-0703, CAS-OBST-0704 (lots `DOS-07.json`)
- **Verdict** : `audite_corrections_requises` (v1.1) — aucune erreur critique ; 3 corrections majeures ; 19 mineures ; 2 marqueurs de posologie restent (schéma français d'entretien de l'ocytocine, sulprostone).
- **Documents acquis consultés (texte intégral)** : OMS 2025, *Consolidated guidelines for the prevention, diagnosis and treatment of postpartum haemorrhage* (DOC-00035) ; FIGO 2022, *Recommendations on the management of PPH* (DOC-00096). Recherches web : E-MOTIVE, CNGOF 2014 (texte non accessible : cngof.fr et sfar.org non joignables).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §1.1, algorithme, §18, §21 | Définition 2025 approximative (« ≈ 300 mL avec signes vitaux anormaux », À VÉRIFIER) | **majeure** | Recommandation 22 citée exactement : perte **mesurée** ≥ 300 mL + un signe hémodynamique anormal (pouls > 100/min, index de choc > 1, PAS < 100 ou PAD < 60 mmHg) **ou** ≥ 500 mL, le premier atteint, dans les 24 h, vigilance les 2 premières heures | OMS 2025, rec. 22 [S7] |
| §13.3.1 prévention | Positions antérieures (OMS 2012/2018) présentées comme actuelles : carbétocine réservée aux contextes sans chaîne du froid ; misoprostol 600 µg seulement | **majeure** (actualité) | OMS 2025 : un seul utérotonique ; ocytocine 10 UI IM/IV (choix préférentiel ; IV lente préférée si voie veineuse), carbétocine 100 µg pour toutes les naissances (thermostable si chaîne du froid incertaine), misoprostol 400 ou 600 µg per os ; ergométrine, ocytocine-ergométrine et prostaglandines injectables non recommandées en prévention | OMS 2025, rec. 7-11 |
| YAML / §22 | S7 « texte intégral non consulté » ; S11-S14 non vérifiées ; FIGO 2022 absente | **majeure** (traçabilité) | S7 = document acquis DOC-00035 ; S11, S12, S14 confirmées par la bibliographie de FIGO 2022 ; S13 citée par OMS 2025 ; S15 (FIGO 2022, DOC-00096) ajoutée | DOC-00035, DOC-00096 |
| §13.2.5 | TXA prophylactique « [À VÉRIFIER — positions 2025] » | mineure | Non recommandé après voie basse ni césarienne | OMS 2025, rec. 14-15 |
| §13.2.5 | TXA : recommandation 2017 seule | mineure | Reprise en 2025 (rec. 27) : 1 g IV en 10 min dans les 3 h, 2e dose si saignement à 30 min ou reprise dans les 24 h — **posologie confirmée** | OMS 2025 |
| §13.2.4 ocytocine | Marqueur global sur le traitement | mineure (posologie) | Schéma OMS 2025 ajouté (10 UI IV en 1-2 min ou 5-10 min ; entretien 10-20 UI sur 4 h) ; schéma CNGOF (entretien, cumul 40 UI) **marqueur maintenu** | OMS 2025, rec. 24 |
| §13.2.4 carbétocine | « pas de recommandation de traitement » [S13 — À VÉRIFIER] | mineure | Prévention seulement ; l'ocytocine IV est l'utérotonique de traitement | OMS 2025, rec. 7.2, 11, 24 |
| §13.2.4 misoprostol | Prévention 600 µg | mineure | 400 ou 600 µg per os (OMS 2025) | OMS 2025, rec. 7.3 |
| §13.2.4 ergométrine | Marqueur sur 0,2 mg | mineure (posologie) | 0,2 mg (200 µg) IM ou IV lente ; **marqueur levé** | FIGO 2022 [S15] |
| §13.2.4 | « Recommandation OMS 2012 » | mineure | Reprise en 2025 (rec. 25) | OMS 2025 |
| §7.2, §12.3 | Index de choc « ≥ 0,9-1 » [À VÉRIFIER] | mineure | > 0,9 (alerte FIGO 2022) ; > 1 (critère OMS 2025) | DOC-00096, DOC-00035 |
| §5, §9 | Fibrinogène < 2 g/L [À VÉRIFIER] | mineure | < 2 g/L = indication de substitution | FIGO 2022 |
| §13.2.6 | Remplissage : objectifs [À VÉRIFIER] | mineure | Cristalloïdes isotoniques préférés aux colloïdes ; cible de réanimation hypotensive PAS 80-90 / PAM 50-60 mmHg (FIGO) | OMS 2025 rec. 28 ; FIGO 2022 |
| §13.2.6 | Ratio PFC/CGR et cible de fibrinogène [À VÉRIFIER] | mineure | 1:2 à 1:1 (ACOG 1:1:1) ; fibrinogène ≥ 1,5-2 g/L | FIGO 2022 |
| §13.2.6 | NASG [À VÉRIFIER] | mineure | Mesure temporaire recommandée | OMS 2025, rec. 35 |
| §13.2.7 | Restriction du ballonnet [À VÉRIFIER] ; tamponnement par mèches non traité | mineure | Conditions de la rec. 36 détaillées ; mèches non recommandées (rec. 37) | OMS 2025 |
| §14.2 | Fer [À VÉRIFIER] | mineure | Fer oral 6-12 semaines (rec. 42) ; fer IV si fer oral impossible ou anémie sévère (rec. 43) | OMS 2025 |
| §13.3.1 | Après césarienne | mineure | Ocytocine 10 UI ou carbétocine 100 µg ; pas de TXA prophylactique ; 5 UI (France) laissé à vérifier | OMS 2025 |
| §13.2.3 | E-MOTIVE : « près de 100 000 accouchements, 78 hôpitaux » | mineure | 80 hôpitaux randomisés (Kenya, Nigeria, Afrique du Sud, Tanzanie), 210 132 accouchements par voie basse | Recherche web (NEJM 2023, communiqué OMS) |
| §1.1 | Définition ACOG [S12 — À VÉRIFIER] | mineure | Marqueur levé (S12 vérifiée) | DOC-00096 |
| §21 | 2e ligne RCOG/ACOG [À VÉRIFIER] | mineure | Carboprost 0,25 mg IM, misoprostol, ergométrine (synthèse FIGO) | FIGO 2022 |
| §20 corrigé QCM 4 | Misoprostol 600 µg seulement | mineure | 400 ou 600 µg (OMS 2025) | OMS 2025 |

**Erreurs critiques (dose)** : aucune. TXA, misoprostol 800 µg SL, ergométrine, ocytocine prophylactique, contre-indications (ergométrine/HTA, sulprostone/coronaropathie, jamais IM) exacts.

## QCM et cas
QCM-OBST-0713 à 0724 : réponses exactes ; explications de 0713, 0716, 0717, 0719 mises à jour (OMS 2025) → `audite_valide`. CAS-OBST-0703 (atonie) : explication complétée (critères OMS 2025) ; CAS-OBST-0704 (placenta accreta) : TXA restreint à l'hémorragie (pas de TXA prophylactique) → `audite_valide`.

## Références
15 sources, toutes vérifiées (S7 et S15 en texte intégral acquis).

## Reste à faire
1. **Posologies (marqueurs maintenus)** : schéma français d'entretien de l'ocytocine (débit, durée, dose cumulée de 40 UI) et sulprostone (500 µg/h, relais, maximum 1 500 µg/24 h) → texte intégral CNGOF 2014 et RCP Nalador.
2. CNGOF 2014 : cible d'Hb (> 8 g/dL ?), seuil plaquettaire, délai de la thromboprophylaxie, place du TXA (formulation), 5 UI après césarienne.
3. Consulter les protocoles nationaux algériens 2025 [S10] et la disponibilité du sulprostone, de la carbétocine thermostable et de la radiologie interventionnelle en Algérie.
4. Motif de la restriction OMS du ballonnet (essais en contexte de faibles ressources).
