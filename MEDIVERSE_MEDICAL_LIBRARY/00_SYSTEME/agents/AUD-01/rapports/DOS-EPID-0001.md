# Rapport d'audit — DOS-EPID-0001 « Mesure de l'état de santé de la population : indicateurs de santé et mesures d'impact »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-04 (références, IA), indépendants du rédacteur DOS-15. Pas de posologie dans ce dossier (AUD-02 sans objet).
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**.
  - Aucune erreur critique ni majeure.
  - Reste : chiffres algériens (ONS 2023, STEPS 2016-2017) non confrontés aux publications primaires.
- **Bilan** : 12 corrections (critiques 0, majeures 0, mineures 12). AUD-01 : 4 ; AUD-04 : 8.

## Méthode

- Lecture intégrale du dossier, du lot QCM (13 QCM EPID de l'item RES-MED-128) et des cas CAS-EPID-1501 et 1502.
- **Tous les exemples chiffrés recalculés par script Python** : exemples 1 à 12, situation commentée, QCM 1 à 10 du dossier. Aucun écart.
  - Densité d'incidence : 2/23,5 = 85,1 ‰ PA.
  - Standardisation : taux standardisés 8,25 ‰ et 7,05 ‰ ; ICM 0,855 ; RSM 0,858.
  - RR = 6, avec IC 95 % (méthode logarithmique) de 4,03 à 8,92.
  - FAP : 50 % par les trois formules ; 33 % dans la situation commentée.
  - NNT 20 ; efficacité vaccinale 90 % ; fraction prévenue dans la population 72 %.
  - Tableau de bord de mortalité (exemple 5) et QCM 3 : dénominateurs vérifiés (naissances vivantes, naissances totales).
- **Définitions vérifiées** :
  - prévalence, incidence cumulée, densité d'incidence, relation P/(1 − P) = DI × D ;
  - létalité et mortalité spécifique ;
  - mortalité infantile et ses composantes, mortinatalité (seuils CIM-10 : 22 semaines ou 500 g ; OMS : 28 semaines ou 1 000 g), mortalité périnatale ;
  - décès maternel (42 jours, causes ni accidentelles ni fortuites) ; RMM et taux de mortalité maternelle ;
  - standardisation directe et indirecte ; espérance de vie ; DALY = YLL + YLD (pondération par l'âge et actualisation abandonnées depuis GBD 2010) ; QALY et ICER ;
  - RA, FEE, RAP, FAP (Levin, Miettinen), RRR, RAR, NNT, NNH, fraction prévenue.
- **Textes algériens relus** (pdftotext) : loi 18-11 (DOC-00074) aux art. 2, 11, 36, 38-39, 45-48, 204, 290, 293-294, 319-323, 338 ; décret 22-178 (art. 5-9) ; décret 22-250 (annexe). Tous conformes.
  - Ces articles ne sont pas modifiés par l'ordonnance 20-02, lue par l'audit (DOC-00116).
- **Sources primaires des chiffres algériens** : tentatives infructueuses.
  - ONS : ons.dz et le miroir ambassade-algerie.ch sont refusés par le proxy.
  - STEPS 2016-2017 : la page OMS de la fiche « 2016-2017 STEPS Fact Sheet Algeria » est trouvée sur who.int, mais son PDF (cdn.who.int) est inaccessible, de même qu'afro.who.int.
  - Une recherche web confirme la cohérence interne des chiffres de presse de l'ONS : 17 797 décès infantiles pour environ 895 000 naissances, soit 19,9 ‰.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 7.4, texte et tableau ONS | Chiffres de presse présentés comme « valeur publiée ». | mineure | En-tête « valeur relayée par la presse (source secondaire) » ; mention explicite « ce ne sont pas des chiffres officiels vérifiés » ; marqueur `[À VÉRIFIER — source primaire non consultée]`. | [S4] |
| § 7.4, STEPS | Diabète, hyperglycémie modérée et tabac attribués au fascicule, alors qu'ils proviennent d'un communiqué de l'OMS Afrique. | mineure | Origine secondaire signalée, avec marqueur. | [S5] |
| § 7.4, HTA | IC de la pré-HTA absent ; effectif « 6 989 » non vérifiable dans le résumé. | mineure | IC 35,2-37,5 ajouté ; mise en garde sur les définitions de l'analyse secondaire. | [S6] (PMID 35982441) |
| Bandeau de statut | « Brouillon à auditer ». | mineure | Statut d'audit et réserves. | — |
| S4 (AUD-04) | Remarque incomplète sur l'accès à la source. | mineure | Hôtes inaccessibles précisés ; marqueur ajouté. | — |
| S5 (AUD-04) | Pas d'URL. | mineure | URL de la page OMS de la fiche STEPS ; remarque réécrite. | who.int |
| S6 (AUD-04) | Auteurs, volume et numéro « à vérifier ». | mineure | Référence complète : Moussouni, Sidi-Yakhlef, Hamdaoui, Aouar, Belkhatir ; 2022;22(1):1571. | PubMed |
| S8 (AUD-04) | Chiffres GBD non sourcés dans la remarque. | mineure | Résumé relu : DALY de 2,63 à 2,88 milliards ; COVID-19 1re cause en 2021 ; HALE de 61,3 à 62,2 ans, baisse de 2,2 % entre 2019 et 2021. | PMID 38642570 |
| S10 (AUD-04) | Gordis 6e éd. « à vérifier ». | mineure | Confirmée (WorldCat OCLC 1079273274). | WorldCat |
| S13 (AUD-04) | Laupacis 1988 non vérifié. | mineure | PMID 3374545 et DOI. | PubMed |
| S14 (AUD-04) | Levin 1953 non vérifié. | mineure | PMID 13124110. | PubMed |
| S15 (AUD-04) | Murray 1994 non vérifié. | mineure | PMID 8062401. | PubMed |

## Points vérifiés sans modification

- Les 12 exemples et les 10 QCM du dossier (réponses et corrigés exacts).
- Les cibles ODD 3.1 et 3.2 :
  - RMM inférieur à 70 pour 100 000 naissances vivantes ;
  - mortalité néonatale ≤ 12 ‰ ;
  - mortalité des moins de 5 ans ≤ 25 ‰.
- L'observatoire national de la santé (art. 11) et les comptes nationaux de la santé (art. 338).
- L'obligation des structures privées d'intégrer le système national d'information sanitaire (art. 321).
- Les infections du site opératoire, les PAVM et les BMR figurent dans la catégorie 1 du décret 22-250.

## QCM et cas associés

- **QCM-EPID-1501 à 1513** : calculs exacts → `audite_valide`.
  - QCM-EPID-1512 : explication A complétée (chiffre ONS de source secondaire, marqueur ajouté).
- **CAS-EPID-1501** (tableau de bord) : indicateurs recalculés et exacts → `audite_valide`.
  - TBN 20 ‰ ; TMI 17 ‰ ; mortinatalité 14,8 ‰ ; mortalité périnatale 22,2 ‰ ; RMM 56,25 pour 100 000.
- **CAS-EPID-1502** (rougeole scolaire) → `audite_valide`.
  - Calculs exacts : efficacité vaccinale 95 % ; fraction prévenue 76 % ; méthode de dépistage concordante.
  - Ajout : vitamine A pour tout enfant malade, selon l'OMS.

## Reste à faire

1. Confronter les chiffres ONS 2023 à la publication n° 1030 (taux de natalité 19,32 ou 19,63 ‰ ; mortalité infantile ; espérance de vie). Il faut ouvrir l'accès à ons.dz.
2. Confronter les chiffres STEPS (diabète, hyperglycémie modérée, tabac) à la fiche OMS : PDF sur cdn.who.int.
3. Vérifier S11 (Porta), S12 (liste OMS des 100 indicateurs), S16 (CIM) et S17 (A/RES/70/1).
4. Seuil réglementaire algérien de la mortinaissance.
5. Relecture par un enseignant.
