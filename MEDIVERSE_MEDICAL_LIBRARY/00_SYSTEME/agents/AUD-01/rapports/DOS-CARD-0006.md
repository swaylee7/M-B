# Rapport d'audit — DOS-CARD-0006 « Embolie pulmonaire et thromboses veineuses »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (scientifique, IA) et AUD-02 (posologies, IA). Ils sont indépendants du rédacteur DOS-01.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Il reste un marqueur posologique (doses initiales d'AVK dans la pratique française et algérienne, maintenu par cohérence avec DOS-PHAR-0002). La source S20 (RCP européen harmonisé de l'énoxaparine) n'est pas relue en texte intégral.
- **Bilan** : 14 corrections (critiques 0, majeures 1, mineures 13). Marqueurs posologiques : 3 levés sur 4.
- **Vérifications** : PubMed (eutils) pour YEARS, PROPER, ESVS 2021, recommandations françaises 2019, cardio-oncologie ESC 2022, ADJUST-PE, Artemis, PEITHO et PRAGUE-26 (résumés lus pour YEARS, PROPER, PEITHO et PRAGUE-26) ; une recherche web (posologie de la ténectéplase dans PEITHO).
- **Cohérence avec les dossiers audités** : HNF, HBPM, fondaparinux, AOD, AVK et antidotes alignés sur DOS-PHAR-0002 ; ténectéplase alignée sur DOS-CARD-0003.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.3.1 (énoxaparine, clairance < 30 mL/min) | « Contre-indiquée à dose curative selon le RCP français ; certains RCP prévoient 1 mg/kg/24 h » : obsolète, et contradictoire avec DOS-PHAR-0002 et DOS-CARD-0004 (audités). | **majeure** | Clairance 15–30 mL/min : 100 UI/kg (1 mg/kg) une fois par 24 h (RCP européen harmonisé) ; < 15 mL/min : non recommandée ; l'HNF reste souvent préférée. | RCP [S20] ; DOS-PHAR-0002 |
| § 13.3.1 (HNF) | `[POSOLOGIE À VÉRIFIER]` ; cible de TCA « 1,5 à 2,5 fois » imprécise. | mineure | Marqueur levé : bolus 80 UI/kg puis 18 UI/kg/h (nomogramme de Raschke), premier TCA à 6 h, zone 1,5–2,3 fois le témoin à calibrer localement, ou anti-Xa 0,3–0,7 UI/mL. | Raschke 1993 [S14] ; ACCP 2012 [S15] |
| § 13.3.4 (ténectéplase) | `[POSOLOGIE À VÉRIFIER]` ; aucune dose ni résultat d'essai. | mineure | Marqueur levé : usage hors AMM ; dans PEITHO, bolus IV unique de 30 à 50 mg selon le poids (comme dans le STEMI) ; résultats ajoutés (moins de décompensations, pas de baisse de la mortalité, plus d'hémorragies et d'AVC). | PEITHO [S17] ; DOS-CARD-0003 |
| § 13.3.8 (antagonisation des AVK) | `[POSOLOGIE À VÉRIFIER]` sur le CCP. | mineure | Marqueur levé : CCP ≈ 25 UI/kg (ou selon l'INR) + vitamine K 10 mg ; objectif INR < 1,5 ; INR à 30 min. | HAS 2008 [S16] ; DOS-PHAR-0002 |
| § 13.3.8 (protamine) | Délai et neutralisation partielle des HBPM non précisés. | mineure | HNF des 2–3 h précédentes, IV lente, ≤ 50 mg par injection ; HBPM : ≤ 60 % de neutralisation, 1 mg pour 100 UI anti-Xa si < 8 h. | ACCP 2012 [S15] |
| § 13.3.8 (anti-Xa directs) | Andexanet présenté sans l'actualité 2025. | mineure | AMM européenne limitée à l'apixaban et au rivaroxaban, excès thrombotique dans ANNEXA-I, retrait du marché américain en décembre 2025 ; CCP 50 UI/kg à défaut. | AABB/FDA [S19] ; DOS-PHAR-0002 |
| § 13.3.3 (initiation des AVK) | Aucune dose de référence. | mineure | Ajout : ACCP 2012 (warfarine 10 mg/j pendant 2 jours chez l'ambulatoire en bonne santé) ; marqueur **maintenu** pour la pratique française et algérienne. | ACCP 2012 (Holbrook), source vérifiée de DOS-PHAR-0002 |
| § 13.3.7 (EP à haut risque pendant la grossesse) | Thrombolyse ou embolectomie présentées en classe I. | mineure | Classe IIa (ESC 2019). | [S1] |
| § 7.1 (sPESI 0 avec atteinte VD ou troponine) | Classement « intermédiaire-faible » systématique. | mineure | Note du tableau ESC 2019 : catégorie intermédiaire (intermédiaire-faible si un seul critère). | [S1] |
| § 13.3.6 et § 21 (cancer) | ESC 2022 : HBPM présentées comme « alternative » aux AOD. | mineure | Les deux options sont de classe I (HBPM si plaquettes > 50 G/L). | [S6] |
| § 12.3 (HTP-TEC) | Fréquence marquée `[À VÉRIFIER]`. | mineure | Incidence cumulée de 0,1 à 9,1 % à 2 ans selon les séries citées par l'ESC 2019. | [S1] |
| § 13.3.5 et § 21 (traitement par cathéter) | PRAGUE-26 « présenté en 2026 », sans résultat. | mineure | Résultats publiés (NEJM, août 2026) : critère composite à 7 jours 0,7 % contre 6,8 %, hémorragies majeures 1,4 % contre 2,2 % ; non encore intégrés dans une recommandation européenne. | PRAGUE-26 [S18] |
| Sources | S10 (YEARS), S11 (PROPER) et S13 (recommandations françaises 2019) non vérifiées ; DOI de S3, S8, S9 et pagination de S6 manquants. | mineure | Toutes vérifiées sur PubMed (DOI et PMID ajoutés ; résultats de YEARS et PROPER en remarque). Sources S14 à S20 ajoutées. | PubMed |
| En-tête, bandeau, note finale | Statut et note de bas de page obsolètes. | mineure | Mis à jour (marqueurs levés et restants). | — |

## Posologies et scores confrontés et conformes (sans modification)

- **Scores** : Wells TVP (seuil 2), Wells EP (3 niveaux 0–1 / 2–6 / ≥ 7 ; 2 niveaux ≤ 4 / > 4), Genève révisé original et simplifié (seuils exacts), PERC (8 critères), YEARS (1 000 / 500 ng/mL), D-dimères ajustés à l'âge (âge × 10 après 50 ans, ADJUST-PE, IIa), PESI (classes I–V) et sPESI, classes de risque ESC 2019, critères de Hestia, catégories AHA/ACC 2026 (A–E).
- **Thrombolyse** : altéplase 100 mg en 2 h ou 0,6 mg/kg en 15 min (≤ 50 mg) ; streptokinase ; urokinase ; contre-indications absolues et relatives ; bénéfice maximal < 48 h.
- **HBPM et fondaparinux curatifs**, AOD (phases initiales, entretien, doses réduites après 6 mois en IIa, critères de l'édoxaban 30 mg, dabigatran 110 mg), prophylaxie (énoxaparine 4 000 UI, fondaparinux 2,5 mg, HNF 5 000 UI × 2–3/j) : conformes à l'ESC 2019 et à DOS-PHAR-0002.
- Soutien hémodynamique (remplissage ≤ 500 mL, noradrénaline 0,2–1 µg/kg/min, dobutamine 2–20 µg/kg/min), durées d'anticoagulation (classes ESC 2019), grossesse (HBPM, 24 h avant une péridurale, ≥ 6 semaines post-partum et ≥ 3 mois au total), TVS (fondaparinux 2,5 mg × 45 j, 3 cm de la jonction).

## QCM et cas associés

- **QCM-CARD-0101 à 0112** : réponses exactes ; les 8 QCM intégrés concordent avec le lot (énoncés, propositions, réponses, explications). 12/12 `audite_valide`.
- **CAS-CARD-0101** : conforme ; point secondaire maintenu (contraception progestative) `[À VÉRIFIER]`. **CAS-CARD-0102** : posologie de l'HNF précisée (80 UI/kg puis 18 UI/kg/h) ; conforme. 2/2 `audite_valide`.

## Reste à faire

1. **Bloquant** : doses initiales d'AVK dans la pratique française et algérienne (marqueur maintenu, comme dans DOS-PHAR-0002).
2. Relire le RCP européen harmonisé de l'énoxaparine en vigueur et l'AMM algérienne (source S20, `verifiee: false`).
3. Définitions des sous-catégories D1–D2 et E1–E2 de l'AHA/ACC 2026 ; parution de la nouvelle recommandation ESC sur l'EP.
4. Position exacte de l'ESVS 2021 sur la TVP distale et sur le seuil ajusté à l'âge dans la TVP ; formulation des recommandations françaises 2019 sur les D-dimères ; chapitre MTEV de l'ESC 2025 grossesse.
5. Données algériennes (épidémiologie de la MTEV, disponibilité des AOD, des thrombolytiques, de l'idarucizumab et des CCP, accès à la scintigraphie).
6. Relecture par un enseignant (statut `valide_enseignant`).
