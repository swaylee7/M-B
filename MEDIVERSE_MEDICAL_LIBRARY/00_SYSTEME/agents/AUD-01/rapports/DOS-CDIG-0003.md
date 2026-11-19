# Rapport d'audit — DOS-CDIG-0003 « Cancer du côlon »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01, AUD-02, AUD-04 (IA), indépendants du rédacteur DOS-04.
- **Objets audités** :
  - dossier v1.0 ;
  - QCM-CDIG-0451…0462 ;
  - CAS-CDIG-0451 et 0452 (lots DOS-04-lot2).
- **Verdict** : `audite_corrections_requises` (v1.1).
  - Aucune erreur critique.
  - Une erreur majeure corrigée (critères d'Amsterdam II mal appliqués dans le cas commenté).
  - 10 corrections au total.
  - Les 2 marqueurs de posologie sont levés.
  - Restent à lire : le texte intégral de l'ESMO 2020 (cancer localisé : facteurs de risque du stade II, rythme de surveillance) et de l'ESMO 2026 (cancer métastatique), ainsi que le Plan cancer algérien (S24) et S25.
- **Moyens de vérification** :
  - texte intégral de la BSG/ACPGBI/UKCGG 2020 (PMC7034349) ;
  - résumés PubMed de l'ESGE 2020, de X-ACT et d'ACT ;
  - recherche web : RCP Xeloda ; recommandation de l'EMA sur le déficit en DPD (2020) ; synthèses de l'ESMO 2026 ; métadonnées du TNM 8 (UICC).
- **Contrôles sans erreur** :
  - posologies FOLFOX et CAPOX relevées dans SCOT ;
  - chiffres d'IDEA (HR 1,07 ; 0,95 ; 1,16 ; 83,1/83,3 % ; 64,4/62,7 %) et de SCOT (76,7/77,1 %).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 17, question 2 | Le corrigé affirmait que les critères d'Amsterdam II n'étaient pas remplis (« exigent au moins 3 apparentés »). Or la patiente (44 ans), son père (48 ans) et sa tante paternelle (endomètre, 51 ans) forment 3 apparentés, le père étant apparenté au 1ᵉʳ degré des deux autres, sur 2 générations, avec un cancer avant 50 ans | **majeure** | Critères d'Amsterdam II **remplis**, sous réserve de la confirmation histologique et de l'exclusion d'une PAF. Bethesda également | Vasen 1999 [S10] |
| § 13.2.2 | Fluoropyrimidine seule sous marqueur | mineure (AUD-02) | Capécitabine 1 250 mg/m² × 2/j de J1 à J14 toutes les 3 semaines, 8 cycles (6 mois). LV5FU2 : nom du protocole conservé, doses selon le protocole de l'établissement | X-ACT + RCP Xeloda [S26] |
| § 13.2.2 | Adaptations (DPD) sous marqueur | mineure (AUD-02) | Déficit complet : contre-indication ; déficit partiel : dose initiale réduite. Autres adaptations selon le RCP | EMA 2020 [S27] |
| § 9.3, § 13.2.2, § 13.2.2 bis, § 17 | Dépistage du déficit en DPD « source à citer » (4 occurrences) | mineure | Sourcé | [S27] |
| § 6.3, § 17 Q6 | Âges de surveillance du Lynch « À VÉRIFIER » | mineure | Confirmés : coloscopie tous les 2 ans dès 25 ans (*MLH1*/*MSH2*) et dès 35 ans (*MSH6*/*PMS2*), jusqu'à 75 ans ; aspirine quotidienne (BSG, forte) | [S12] (texte intégral) |
| § 13.3.2 | Formulation de l'ESGE à vérifier | mineure | Prothèse en pont : à discuter en décision partagée (forte) ; délai d'environ 2 semaines ; colostomie de décharge comme alternative | [S15] |
| Bandeau, § 13.2.3, § 21 | ESMO 2026 non relue | mineure (actualité) | Première ligne guidée d'abord par MMR/MSI ; encorafénib + cétuximab + mFOLFOX6 en 1ʳᵉ ligne si BRAF V600E (synthèses publiées). Le reste `[À VÉRIFIER]` | [S3] |
| § 21 | Divergences sur la surveillance du Lynch | mineure | Ligne ajoutée | [S12, S13] |
| YAML, § 22 | Traçabilité | mineure (AUD-04) | S5 (TNM 8) vérifiée (UICC, ISBN). Ajout de S26 et S27. S3, S12 et S15 précisées | — |
| QCM-CDIG-0461 | Référence ESMO 2023 sans mention de la version 2026 | mineure | Explication actualisée ; source ajoutée | [S3] |

## TNM 8 et scores contrôlés

- **T** (Tis à T4b), **N** (N1a/b/c, N2a/b) et **M** (M1a/b/c) : exacts.
- **Stades** 0 à IVC : exacts, dont IIIA, IIIB et IIIC.
- **Calculs** :
  - QCM-CDIG-0451 : pT3 N2a = IIIB ;
  - cas du dossier : pT3 N1b = IIIB ;
  - CAS-CDIG-0451 : pT4a N2a = IIIC ;
  - CAS-CDIG-0452 : pT4a N0 = IIB.
- **Amsterdam II** et **Bethesda révisés** : énoncés exacts (seule l'application au cas était erronée).

## QCM et cas

- QCM-CDIG-0451…0462 : réponses exactes → `audite_valide`.
- CAS-CDIG-0451 et 0452 : exacts → `audite_valide`.

## Reste à faire

1. Lire le texte intégral de l'**ESMO 2020** (cancer localisé) :
   - liste des facteurs de risque du stade II ;
   - fluoropyrimidine au stade II MSS sans facteur de risque ;
   - délai de l'adjuvant ;
   - rythmes de surveillance.
2. Lire le texte intégral de l'**ESMO 2026** (cancer métastatique) :
   - immunothérapie des tumeurs MSI-H ;
   - réintroduction des anti-EGFR ;
   - transplantation hépatique.
3. Plan national cancer 2015–2019 (S24) ; résumé ASCO 2018 (S25), non retrouvé ; données des registres algériens.
4. Sources des points encore marqués `[À VÉRIFIER]` : proportion de MSI, *S. gallolyticus*, oxaliplatine après 70 ans, surveillance après polypectomie (ESGE), recommandations françaises de dépistage (INCa).
5. Relecture par un enseignant.
