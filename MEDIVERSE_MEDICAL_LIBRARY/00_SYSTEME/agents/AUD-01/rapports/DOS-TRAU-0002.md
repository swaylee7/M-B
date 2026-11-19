# Rapport d'audit — DOS-TRAU-0002 « Fracture de l'extrémité inférieure du radius »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-11.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**.
- **Bilan** : 7 corrections (critiques 0, majeures 0, mineures 7). Marqueurs de posologie : 3 au départ, 2 restants (antibioprophylaxie de la fracture ouverte, anesthésiques locaux).
- **Vérifications** :
  - Europe PMC : Kamal et Shapiro 2022 ; Lichtman 2010 (AAOS 2009) ; Ekrol 2014 ; CROSSFIRE ; WRIST ; Lafontaine 1989 (Injury, Acta Orthop Belg) ;
  - Frykman 1967 (PMID 4175195) et Castaing 1964 (PMID 14198868) retrouvés dans PubMed ;
  - recherches web : recommandations AAOS 2020 (vitamine C, repère de 65 ans).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| Sources S10, S11 | Frykman et Castaing à `verifiee: false`. | mineure | Passées à `true` (PMID) ; pagination de Frykman corrigée (Suppl 108:3+). | Europe PMC |
| § 9.5 | Seuils de réduction acceptable « à vérifier ». | mineure | Attribués à l'AAOS 2009 (fixation suggérée au-delà de 3 mm de raccourcissement, 10° de bascule dorsale ou 2 mm de marche ; force modérée). | [S14] |
| § 13.2.5 | Seuil d'âge de l'AAOS 2020 incertain. | mineure | Sept recommandations ; repère de 65 ans ; pas de bénéfice démontré de la chirurgie à long terme ; libellé exact [À VÉRIFIER]. | [S1, S2] |
| § 13.2.5–13.2.6, rééducation | Position de l'AAOS « à vérifier ». | mineure | Pas de différence entre exercices à domicile et rééducation supervisée. | [S2] |
| § 21, vitamine C | Formulation de l'AAOS 2009 approximative (« ~50 jours ») ; preuves contraires non citées. | mineure | Formulation exacte de l'AAOS 2009 : « suggère » une vitamine C adjuvante pour prévenir les douleurs disproportionnées (force modérée). Essai d'Ekrol 2014 (336 patients, 500 mg/j pendant 50 jours) : aucun bénéfice. Position de l'AAOS 2020 [À VÉRIFIER]. | [S14, S15] |
| § 13.2.1, analgésie (AUD-02) | Aucune dose. | mineure | Paracétamol 1 g toutes les 6 h (4 g/j au maximum ; 3 g/j si facteur de risque) ; ibuprofène 400 mg × 3/j. Marqueur levé. | RCP |
| § 21 | Lignes « Chirurgie du sujet âgé » et « Critères de réduction » imprécises. | mineure | Repère de 65 ans ; AAOS 2009. | [S1, S14] |

## Points vérifiés sans modification

- Paramètres radiologiques normaux ; signe de Laugier.
- Frykman I à VIII (types pairs : styloïde ulnaire).
- AO/OTA 2R3 : B1 sagittale, B2 marge dorsale, B3 marge palmaire ; C1 à C3.
- Lafontaine : bascule dorsale > 20°, comminution dorsale, trait radio-carpien, fracture de l'ulna, âge > 60 ans. Les résumés de 1989 ne donnent pas le seuil de 3 facteurs, qui reste [À VÉRIFIER].
- Essais :
  - DRAFFT ;
  - CROSSFIRE : 166 randomisés, âge moyen 71 ans, 90 % de femmes, complications 14 % contre 8 % (différence non significative) ;
  - WRIST : 304 patients, cals vicieux 59,1 % sous plâtre contre 8 à 17 %.

## QCM et cas associés

- QCM-TRAU-1113 à 1124 : exacts → `audite_valide`. QCM-TRAU-1120 : explication sur la vitamine C sourcée (AAOS 2009, Ekrol 2014).
- CAS-TRAU-1103 et CAS-TRAU-1104 : marqueurs levés (analgésie) → `audite_valide`.

## Reste à faire

1. Texte intégral de l'AAOS 2020 (drfcpg.pdf) : libellés et forces des 7 recommandations, vitamine C.
2. Seuil de 3 facteurs de Lafontaine (texte original) ; classifications d'Older et de Fernandez.
3. Antibioprophylaxie de la fracture ouverte (protocole local ; divergence céfazoline / amoxicilline-acide clavulanique selon les pays).
4. Durées d'immobilisation (adulte, fracture en motte de beurre de l'enfant).
5. Relecture humaine qualifiée.
