# Rapport d'audit — DOS-ORL-0001 « Otite moyenne aiguë : définition, diagnostic, évolution, traitement »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-12.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_valide**.
  - Aucune erreur critique ni majeure.
  - Aucun marqueur `[POSOLOGIE À VÉRIFIER]` restant (2 levés).
  - Restent des `[À VÉRIFIER]` non bloquants : données algériennes récentes, nomenclature, protocole local de la mastoïdite, recommandations sur l'OSM.
- **Bilan** : 6 corrections (critiques 0, majeures 0, mineures 6). AUD-01 : 4 ; AUD-02 : 2.
- **Vérifications** :
  - fiches HAS–SPILF–GPIP relues en texte intégral sur has-sante.fr : OMA purulente de l'enfant (mise à jour du 14 mai 2025) et de l'adulte (mise à jour du 13 mai 2025) ;
  - synthèse HAS des durées (DOC-00079, acquis localement) ;
  - arrêté du 3 juillet 2018 (DOC-00070), relu : « anti-pneumococcique 13 » à 2, 4 et 12 mois ;
  - résumés Europe PMC des deux revues Cochrane 2023 (S7, S8) ;
  - texte intégral de Ramdani-Bouguessa 2015 (PMC4475694).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 3, Algérie | Résistance du pneumocoque présentée comme non documentée. | mineure | Données algériennes ajoutées (2005-2012, 270 souches pédiatriques) : pénicilline I 20,6 % et R 27,5 % ; amoxicilline I 2,6 % et R 0,4 %. Pour les 47 souches d'otites : pénicilline I 25,5 % et R 10,6 %, amoxicilline 0 %. Période antérieure à la généralisation du VPC : `[À VÉRIFIER]` maintenu pour les données récentes. | [S12] |
| § 21, contexte algérien | Même lacune. | mineure | Phrase mise à jour (amoxicilline restée active, y compris sur les souches d'otites). | [S12] |
| § 13.2.2, cotrimoxazole de l'adulte (AUD-02) | Marqueur posologique. Le libellé de la fiche HAS (« 800 mg par jour + 160 mg par jour, 2 fois par jour ») est ambigu. | mineure | Marqueur levé : 800/160 mg deux fois par jour (1 600/320 mg/j), 5 jours. L'ambiguïté du libellé est signalée. | Fiche HAS adulte [S2] |
| § 13.3.3, échec (AUD-02) | Marqueur posologique sur l'amoxicilline–acide clavulanique et le cefpodoxime après échec. | mineure | Marqueur levé : posologies de la fiche HAS pour ces molécules (amoxicilline 80 mg/kg/j, max 3 g/j ; cefpodoxime 8 mg/kg/j, max 400 mg/j ; en 2 prises). Le texte SPILF 2011 n'a pas été relu, ce qui est signalé. | [S1] |
| Références, S11 | Valence du VPC non sourcée. | mineure | Précision : l'arrêté de 2018 relu mentionne l'« anti-pneumococcique 13 ». | DOC-00070 |
| Références | Source algérienne absente. | mineure | S12 ajoutée (vérifiée, texte intégral). | PMID 26106481 |

## Points vérifiés sans modification

Fiches HAS 2025, vérifiées mot à mot :

- **Enfant** :
  - amoxicilline 80 mg/kg/j en 2 prises (max 3 g/j) ;
  - amoxicilline–acide clavulanique 80 mg/kg/j (dose d'amoxicilline) si otite-conjonctivite ;
  - cefpodoxime 8 mg/kg/j (max 400 mg/j) ;
  - sulfaméthoxazole-triméthoprime 30/6 mg/kg/j (max 800/160 mg/j, libellé exact de la fiche).
- **Durées** :
  - < 3 mois : avis spécialisé ;
  - 3 mois-2 ans : 10 jours ;
  - > 2 ans, symptômes modérés : abstention et réévaluation à 48-72 h ;
  - > 2 ans, symptômes importants : 5 jours, ou 10 jours si otorrhée ou otite récidivante (récidive plus de 4 jours après l'arrêt).
- **Symptomatique** :
  - paracétamol 60 mg/kg/j en 4 prises (max 80 mg/kg/j), 72 h au plus ;
  - ibuprofène en 2e intention dès 3 mois : 20-30 mg/kg/j (max 30), 24 h au plus entre 3 et 6 mois, 72 h au plus au-delà ;
  - AINS non recommandés en cas de varicelle ou d'infection ORL sévère ou compliquée.
- **Adulte** :
  - amoxicilline 3 g/j en 3 prises, 5 jours ;
  - céfuroxime axétil 500 mg/j ou cefpodoxime 400 mg/j ;
  - pristinamycine 2 g/j ;
  - échec à 72 h : avis spécialisé ;
  - pas d'antibiotique si les tympans n'ont pas été vus.

AAP 2013 :

- critères diagnostiques ;
- définition de la forme sévère (otalgie modérée à sévère, ≥ 48 h, ou T ≥ 39 °C) ;
- tableau d'observation selon l'âge ;
- durées 10 j, 7 j et 5-7 j ;
- critères de récidive (3 épisodes/6 mois ou 4/12 mois) ;
- pas d'antibioprophylaxie.

Revues Cochrane 2023 : conclusions conformes aux résumés.

## QCM et cas associés

- **QCM-ORL-1201 à 1212** : exacts ; posologies conformes aux fiches 2025 → 12 `audite_valide`.
- **CAS-ORL-1201** : 880 mg/j en 2 prises pour 11 kg, 10 jours ; VPC13 à 2-4-12 mois → `audite_valide`.
- **CAS-ORL-1202** (mastoïdite) : tableau exact ; sous-dosage de 25 mg/kg/j en une prise bien identifié. La posologie de la C3G injectable n'est pas vérifiée (marqueur maintenu) → `audite_corrections_requises`.

## Reste à faire

1. Données de résistance du pneumocoque postérieures à la généralisation du VPC (réseau algérien de surveillance).
2. Recommandations SPILF-GPIP sur la mastoïdite (choix et doses de la C3G).
3. Nomenclature algérienne (cefpodoxime en suspension, pristinamycine).
4. Relecture enseignant.
