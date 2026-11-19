# Rapport d'audit — DOS-GYNE-0003 « Tumeurs du sein »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-07)
- **Objets audités** : dossier v1.0 ; QCM-GYNE-0725 à 0736 et CAS-GYNE-0705, CAS-GYNE-0706 (lots `DOS-07.json`)
- **Verdict** : `audite_corrections_requises` (v1.1) — aucune erreur critique ni majeure de contenu ; 1 correction majeure de traçabilité ; 7 mineures. Toutes les références sont désormais vérifiées, mais le texte intégral d'ESMO 2024 (référence principale de la stratégie) n'a pas pu être consulté : les modalités thérapeutiques marquées [À VÉRIFIER] restent à confirmer.
- **Recherches web** : KEYNOTE-522, OlympiA, DESTINY-Breast04, ESMO 2021 (cancer métastatique), ASCO/CAP 2023 (HER2), Elston-Ellis 1991, AJCC 8e édition.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| YAML / §22 | S9 à S15 non vérifiées | **majeure** (traçabilité) | S9 (AJCC 8), S10 (PMID 1757079), S11 (JCO 2023;41(22):3867-3872), S12 (KEYNOTE-522, PMID 32101663 ; EFS NEJM 2022), S13 (OlympiA, DOI), S14 (DESTINY-Breast04, DOI), S15 (ESMO 2021, DOI) vérifiées | Recherche web |
| §7.4, §21 | Seuil RE ≥ 1 % / « RE faible » attribué à S11 (guide HER2) | mineure | Attribué à la recommandation ASCO/CAP 2020 sur les récepteurs hormonaux (référence à ajouter) | — |
| §7.4, §21 | « HER2-low » présenté sans nuance | mineure | L'ASCO/CAP 2023 n'en fait pas une catégorie diagnostique mais impose de distinguer IHC 0 et 1+ | S11 |
| §9.2 | Seuils BI-RADS [À VÉRIFIER] | mineure | Seuils de l'atlas ACR 2013 confirmés (3 ≤ 2 % ; 4A > 2-10 % ; 4B > 10-50 % ; 4C > 50-< 95 % ; 5 ≥ 95 %) ; surveillance BI-RADS 3 à 6, 12 et 24 mois | ACR [S4] |
| §13.3 triple négatif | Schéma KEYNOTE-522 [À VÉRIFIER] | mineure | Stades II-III ; paclitaxel-carboplatine puis anthracycline-cyclophosphamide + pembrolizumab, poursuivi en adjuvant ; olaparib (OlympiA) si mutation constitutionnelle BRCA | S12, S13 |
| §7.5 | Stade pronostique AJCC [À VÉRIFIER] | mineure | Précisé (grade, RE, RP, HER2 ± signature ; stade anatomique si biomarqueurs indisponibles) | S9 |
| §13.2.4 | Marqueur générique [POSOLOGIE À VÉRIFIER] sans dose énoncée | mineure | Reformulé (posologies volontairement non détaillées ; renvoi aux protocoles et RCP) | — |
| §7.3, §13.2.4, §13.3, §17 | Marqueurs [S9/S10/S15 — À VÉRIFIER] | mineure | Levés (références vérifiées) | — |

**Erreurs critiques** : aucune. Classification OMS 2019 (NST, lobulaire, « pattern médullaire »), grade de Nottingham (3-5 / 6-7 / 8-9), BI-RADS 5e édition, densité a-d, TNM AJCC 8 (T1mi-T4d, N1-N3), sous-types de substitution, triple évaluation, indications néo-adjuvantes HER2+/triple négatif (≥ T2 ou N+), T-DM1 si résidu, trastuzumab 1 an, cancer inflammatoire (pas de ganglion sentinelle) : exacts.

## QCM et cas
QCM-GYNE-0725 à 0736 : réponses exactes et explications cohérentes → `audite_valide`. CAS-GYNE-0705 (HER2+ cT2N1) et CAS-GYNE-0706 (tumeur phyllode borderline) : exacts → `audite_valide`.

## Références
15 sources, toutes vérifiées (existence et pagination) ; ESMO 2024 [S1] vérifiée comme référence mais non lue en texte intégral.

## Reste à faire
1. Lire ESMO 2024 (Loibl et al., Ann Oncol 2024;35:159-182) et confirmer : indications du bilan d'extension, désescalade axillaire (1-2 ganglions sentinelles ; après néo-adjuvant), hypofractionnement (40 Gy/15 fr ; 26 Gy/5 fr), inhibiteurs de CDK4/6 adjuvants (abémaciclib, ribociclib), rythme de surveillance, chirurgie prophylactique BRCA, grossesse.
2. Ajouter la référence ASCO/CAP 2020 sur les récepteurs hormonaux (RE faibles 1-10 %).
3. Dépistage : ECIBC et USPSTF (âge de début), données algériennes de stade au diagnostic (registres).
4. Ordres de grandeur (RH+ ≈ 70 %, HER2+ 15-20 %, sein de l'homme ≈ 1 %, GLOBOCAN mondial 2022) : citer une source.
