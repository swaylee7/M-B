# Rapport d'audit — DOS-TRAU-0001 « Fractures du col du fémur : classification, diagnostic, traitement »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-11.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**.
- **Bilan** : 15 corrections (critiques 0, majeures 1, mineures 14). Marqueurs de posologie : 6 au départ, 1 restant (anesthésiques locaux des blocs).
- **Vérifications** :
  - résumés Europe PMC : HIP ATTACK, HEALTH, FAITH, Bartoníček 2001, Nandi 2021, Moon et Mehlman 2006 ;
  - Garden 1961 recherchée dans Europe PMC sans résultat ;
  - recherches web : mise à jour 2023 de NICE CG124 ; NICE NG89 (fractures de fragilité).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 7.6, § 13.2.4, algorithmes, § 18, § 21 | Critère NICE de la PTH présenté dans sa version antérieure (« offer » ; absence de trouble cognitif) comme actuel. | majeure | NICE 2023 : PTH à **envisager** (« consider ») chez le patient autonome à l'extérieur avec au plus une canne ; version antérieure datée ; autres conditions [À VÉRIFIER]. | [S1], recherche web |
| § 7.2, Garden | Limites incomplètes. | mineure | Lecture sur le seul cliché de face, bascule postérieure ignorée, reproductibilité médiocre. | — |
| § 7.3, Pauwels | Seuils non sourcés ; aucune limite. | mineure | Seuils originaux (I ≤ 30°, II 30–50°, III ≥ 50°) ; limites (mesure, reproductibilité, valeur pronostique) ; valeur biomécanique conservée. | [S17, S18] |
| § 7.5, Delbet | Taux d'ostéonécrose « à vérifier ». | mineure | 38 %, 28 %, 18 % et 5 % (méta-analyse de 360 cas). | [S19] |
| § 13.2.1 (AUD-02) | Paracétamol sans dose. | mineure | 1 g toutes les 6 h ; adaptation au poids et au terrain. Marqueur levé. | RCP ; [S1] |
| § 13.2.2 | Délai : confusion fréquente entre 36 h et la recommandation NICE. | mineure | Les 36 h sont un indicateur d'audit britannique ; NICE recommande le jour de l'admission ou le lendemain [À VÉRIFIER]. | [S1] |
| § 13.2.2, HIP ATTACK | Un seul critère composite était décrit. | mineure | Deux critères principaux (mortalité 9 % contre 10 % ; complications majeures 22 % contre 22 %) ; délai médian de 6 h contre 24 h. | [S6] (résumé lu) |
| § 13.2.3, acide tranexamique (AUD-02) | Aucune dose. | mineure | 1 g IV à l'induction (exemple) ; schéma du RCP ; adaptation rénale ; contre-indications. Marqueur levé. | RCP ; [S2] |
| § 13.2.4, clou | Clou présenté comme le standard des fractures trochantériennes instables. | mineure | Fractures sous-trochantériennes et à trait oblique inversé ; NICE préfère la vis-plaque pour A1–A2. | [S1, S2] |
| § 13.2.4, tige cimentée | « Type unique de tige » attribué à NICE 2023. | mineure | Présenté comme une proposition du projet de 2022, [À VÉRIFIER]. | Recherche web |
| § 13.2.4, FAITH | Sous-groupes « à vérifier ». | mineure | Confirmés (fumeurs, fractures déplacées ou basicervicales) ; ostéonécrose 9 % contre 5 % avec la vis-plaque. | [S5] (résumé lu) |
| § 13.2.6, thromboprophylaxie (AUD-02) | Adaptation rénale et durée non précisées. | mineure | Énoxaparine 4 000 UI/j (2 000 UI/j si ClCr 15–30 mL/min) ; fondaparinux 2,5 mg/j (1,5 mg si ClCr 20–50 mL/min ; contre-indiqué si < 20 mL/min) ; **1 mois** (NICE NG89) ; délais pré- et postopératoires. Marqueur levé. | RCP ; [S16] |
| § 13.2.7 (AUD-02) | Bisphosphonate sans dose. | mineure | Acide zolédronique 5 mg/an, au moins 2 semaines après la chirurgie, contre-indiqué si ClCr < 35 mL/min ; alendronate 70 mg/semaine. Marqueur levé. | RCP ; [S10] |
| § 17, question 3 (AUD-02) | HBPM sans dose. | mineure | Dose et adaptation à la clairance. Marqueur levé. | RCP |
| Sources | Sources manquantes. | mineure | Ajout de S16 (NICE NG89), S17 (Bartoníček), S18 (Nandi) et S19 (Moon et Mehlman). | — |

## Points vérifiés sans modification

- Garden I à IV (travées), simplification non déplacée / déplacée.
- AO/OTA 2018 : 31A, 31B (B1 sous-capitale, B2 transcervicale, B3 basicervicale), 31C (tête).
- Delbet I à IV.
- NICE : chirurgie le jour de l'admission ou le lendemain ; IRM puis scanner si IRM indisponible sous 24 h ; pas d'AINS ; appui complet immédiat ; filière orthogériatrique.
- AAOS 2021 : pas de traction ; blocs ; acide tranexamique ; seuil transfusionnel de 8 g/dL ; rachianesthésie et anesthésie générale équivalentes ; uni- et bipolaire équivalentes ; tige cimentée.
- HEALTH : réinterventions 7,9 % contre 8,3 % ; luxations 4,7 % contre 2,4 %.

## QCM et cas associés

- QCM-TRAU-1101 à 1112 : exacts → `audite_valide`. Explications complétées :
  - 1105 : NICE 2023 ;
  - 1106 : FAITH ;
  - 1110 : posologies, NICE NG89.
- CAS-TRAU-1101 et CAS-TRAU-1102 : thromboprophylaxie précisée → `audite_valide`.

## Reste à faire

1. Texte en vigueur de NICE CG124 (2023) : conditions complètes de la PTH ; libellé final sur la tige cimentée.
2. Force de la recommandation AAOS 2021 sur le délai de 24 à 48 h ; critères secondaires de HIP ATTACK ; indicateur des 36 h.
3. Durée exacte de la SFAR 2011 ; place de l'aspirine (ESA 2018).
4. Garden 1961 (JBJS Br) et Pauwels 1935 (ouvrage) toujours à `verifiee: false`.
5. Anesthésiques locaux des blocs (protocole local, marqueur maintenu).
6. Relecture humaine qualifiée (chirurgie orthopédique et traumatologique).
