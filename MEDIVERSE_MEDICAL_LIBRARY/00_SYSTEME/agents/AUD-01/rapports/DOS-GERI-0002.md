# Rapport d'audit — DOS-GERI-0002 « Troubles confusionnels du sujet âgé : syndrome confusionnel aigu (delirium) »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA), AUD-02 (posologies, IA) et AUD-04 (références, IA), indépendants du rédacteur DOS-15.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Aucune erreur critique ou majeure, mais **2 posologies restent marquées** :
  - halopéridol (§ 12.5 et cas du § 16) ;
  - benzodiazépine du delirium tremens (§ 9).
- **Bilan** : 19 corrections (critiques 0, majeures 0, mineures 19). AUD-01 : 11 ; AUD-02 : 3 ; AUD-04 : 5.

## Sources relues pendant l'audit

- **NICE CG103**, recommandations et contexte (nice.org.uk) :
  - 4 facteurs de risque (1.2.1) ; intervention multicomposante dans les 24 h (1.4.2-1.4.13) ;
  - 4AT par défaut, CAM-ICU ou ICDSC en réanimation (1.6.1, 2023) ;
  - désescalade puis halopéridol à court terme, habituellement ≤ 1 semaine, à la dose la plus faible, avec avis de la MHRA (1.7.3-1.7.4) ;
  - prévalence 20-30 % en médecine, 10-50 % en chirurgie, < 20 % en long séjour (contexte) ;
  - CG103 ne traite pas des benzodiazépines.
- **HAS 2009**, « Confusion aiguë chez la personne âgée », PDF des recommandations :
  - bilan initial systématique ;
  - TDM en 1re intention (signe de localisation, suspicion d'hémorragie méningée, traumatisme crânien même mineur) ou en 2e intention ;
  - traitement de 24 à 48 h au maximum, en monothérapie, à 1/4-1/2 de la dose adulte ;
  - benzodiazépine orale courte (alprazolam, lorazépam, oxazépam) si l'anxiété prédomine, neuroleptique si troubles productifs ; éviter la forme injectable ;
  - CAM décrite, mais traduction française non validée ;
  - confusion postopératoire hors champ.
- **NICE CG100** (sevrage alcoolique) : lorazépam oral en 1re intention dans le delirium tremens (1.1.4.1) ; thiamine parentérale ≥ 5 jours si Gayet-Wernicke suspecté (1.2.1.4).
- **EFNS 2010** (Galvin, PMID 20642790), résumé : thiamine 200 mg × 3/j, de préférence IV, avant tout glucide (niveau C).
- **Beers 2023**, texte intégral (PMC) :
  - médicaments à éviter dans le delirium : anticholinergiques, antipsychotiques, benzodiazépines, corticoïdes, anti-H2, Z-drugs, opioïdes (ajoutés en 2023) ;
  - benzodiazépines possiblement appropriées dans les sevrages en alcool ou en benzodiazépines.
- **PubMed** : CAM 1990, Tieges 2021 (sensibilité et spécificité 0,88), Bellelli 2014, HELP 1999 (9,9 % vs 15,0 %, OR 0,60), Inouye 1996, Inouye 2014, Ely 2001, Wilson 2020, PADIS 2018.
- **CIM-11** : code 6D70 confirmé par une source secondaire (CISMeF ; icd.who.int inaccessible).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 1.2 | Code CIM-11 « à vérifier ». | mineure | 6D70 et sous-codes (6D70.0, .1, .2). | CISMeF |
| § 3 | Chiffres de prévalence « à confronter au texte NICE ». | mineure | Confirmés (contexte de CG103) ; marqueur retiré. | [S1] |
| § 8.3, scanner | Indications incomplètes par rapport à la HAS. | mineure | Hémorragie méningée suspectée ; 1re et 2e intention ; antiagrégants. | [S6] |
| § 12.5, NICE | Désescalade et avis de la MHRA absents. | mineure | Formulation 1.7.4 complétée ; absence de dose absolue signalée. | [S1] |
| § 12.5, HAS | « Molécules et posologies exactes à vérifier » ; « durée brève ». | mineure | 24-48 h au maximum, monothérapie, évaluation de la 1re dose, 1/4-1/2 de la dose adulte, molécules, voie orale, réintroduction en cas de sevrage. | [S6] |
| § 12.5, benzodiazépines | Exclusivité « réservée au sevrage » attribuée au NICE (S1), qui ne traite pas ce point. | mineure | Attribution à Beers 2023 et à NICE CG100 ; nuance de la HAS (anxiété prédominante). | [S10, S17, S6] |
| § 12.6 | Libellés Beers « à confronter ». | mineure | Liste exacte des médicaments à éviter dans le delirium (opioïdes ajoutés en 2023). | [S10] |
| § 14 | Chiffres HELP « à confronter ». | mineure | Confirmés ; OR apparié 0,60 ajouté. | [S8] |
| § 15.1 et 15.2 | Algorithme : durée de traitement et place des benzodiazépines. | mineure | 24-48 h selon la HAS ; benzodiazépine en cas de sevrage ou d'anxiété prédominante ; thiamine avant tout glucide. | [S6] |
| § 20, divergences | Outil HAS (« à vérifier ») ; psychotropes ; prévention médicamenteuse. | mineure | Position de la HAS sur la CAM ; positions NICE, Beers et HAS datées ; position NICE sur la prévention. SIGN laissé à vérifier. | [S1, S6, S10] |
| Bandeau | Statut « brouillon » ; « aucune posologie validée ». | mineure | Statut d'audit ; état des posologies. | — |
| § 9, Gayet-Wernicke et delirium tremens (AUD-02) | `[POSOLOGIE À VÉRIFIER]` sur la thiamine. | — (levé) | Thiamine **200 mg × 3/j IV avant tout glucide** (EFNS 2010), voie parentérale ≥ 5 jours puis relais oral (NICE CG100). | [S18, S17] |
| § 9, delirium tremens (AUD-02) | Benzodiazépine sans molécule ni source. | mineure | Lorazépam oral en 1re intention ; parentéral ou halopéridol en recours (NICE CG100). **Dose : marqueur maintenu** (dose titrée selon les symptômes, sans dose standard dans les sources consultées). | [S17] |
| § 16, cas (AUD-02) | Antipsychotique « à très faible dose » sans repère. | mineure | Règle HAS (1/4-1/2 de la dose adulte, voie orale, 24-48 h) et règle NICE (dose la plus faible). **Dose absolue : marqueur maintenu**. | [S6, S1] |
| S1, S6 (AUD-04) | Remarques « non relu intégralement ». | mineure | Remarques réécrites d'après les textes relus. | — |
| S5, S7, S9, S13, S14, S16 (AUD-04) | Non vérifiées. | mineure | PMID : 24590568, 23992774, 8596223, 11730446, 33184265, 30113379 ; DOI. | PubMed |
| S8 (AUD-04) | Chiffres HELP non vérifiés. | mineure | PMID 10053175 ; résumé relu. | PubMed |
| S17 (AUD-04) | Source manquante (sevrage alcoolique). | mineure | NICE CG100 ajouté. | nice.org.uk |
| S18 (AUD-04) | Source manquante (thiamine). | mineure | EFNS 2010 ajouté. | PMID 20642790 |

## Points vérifiés sans modification

- Critères DSM-5-TR (reformulés) ; formes hyper-, hypo-active et mixte.
- 4AT : items, cotation (0/4 ; 0/1/2 ; 0/1/2 ; 0/4) et seuils (≥ 4 ; 1-3 ; 0).
- CAM : critères 1 + 2 + (3 ou 4) ; sensibilité 94-100 % ; spécificité 90-95 %.
- Facteurs précipitants d'Inouye 1996.
- Prévention multicomposante NICE (10 domaines, dont le bouchon de cérumen).
- Delirium tremens 48-72 h après l'arrêt.
- Loi 18-11 : art. 21, 23 al. 2 (mineurs et incapables), 87, 198, 343 conformes.
- Cas de Mme B. : 4AT = 11 ; oxybutynine + donépézil (association incohérente).
- QCM 1 à 10 du dossier : exacts.

## QCM et cas associés

- **QCM-GERI-1514 à 1526** → `audite_valide`.
  - 4AT recalculés : 2 et 12.
  - CAM positive par le critère 4.
  - Explication du QCM-GERI-1521 alignée sur la HAS.
- **CAS-GERI-1503** (confusion hypoactive postopératoire, 4AT = 11) → `audite_valide`.
- **CAS-GERI-1504** (delirium tremens) → `audite_corrections_requises`.
  - Thiamine levée (EFNS 2010, NICE CG100) ; lorazépam précisé.
  - **Dose de la benzodiazépine : marqueur maintenu.**

## Reste à faire

1. **Posologies** à confronter au RCP algérien ou européen et au protocole local :
   - halopéridol chez le sujet âgé confus (RCP harmonisé européen) ;
   - benzodiazépine du sevrage alcoolique, par exemple selon un protocole guidé par un score (SFA 2015, CIWA-Ar).
2. SIGN 157 (hôte inaccessible) ; formulation exacte de PADIS 2018 sur la prévention médicamenteuse ; libellés des critères STOPP/START v3 sur le delirium.
3. Cadre légal algérien de la contention physique en milieu somatique ; données épidémiologiques algériennes.
4. Relecture par un enseignant de gériatrie.
