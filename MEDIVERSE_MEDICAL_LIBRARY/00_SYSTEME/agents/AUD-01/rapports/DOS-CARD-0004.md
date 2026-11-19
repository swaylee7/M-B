# Rapport d'audit — DOS-CARD-0004 « Syndromes coronariens aigus sans sus-décalage de ST »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (scientifique, IA) et AUD-02 (posologies, IA). Ils sont indépendants du rédacteur DOS-01.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Un seul blocage subsiste : le marqueur `[POSOLOGIE À VÉRIFIER]` sur le schéma d'HNF en attente de coronarographie. Les références S1 à S6 sont toutes vérifiées (S4 l'a été pendant l'audit).
- **Bilan** : 8 corrections (critiques 0, majeures 0, mineures 8).
- **Recherche web utilisée** : 1 (référence ESC 2020 SCA ST−).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 9.2 (algorithme hs-cTn 0 h/1 h) | Un seul exemple de seuils (Elecsys), assorti d'un marqueur, avec un risque de généralisation abusive. | mineure | Les seuils Elecsys ont été confirmés. Ajout d'un tableau à deux dosages (hs-cTnT Elecsys : 5 / 12 et Δ 3 / 52 / Δ 5 ng/L ; hs-cTnI Architect : 4 / 5 et Δ 2 / 64 / Δ 6 ng/L) et d'un avertissement explicite : **ne jamais transposer les seuils d'un dosage à un autre**. | ESC 2020/2023 [S1, S4] |
| Cas clinique, question 1 | « [seuil à vérifier selon le dosage local] ». | mineure | Précisé : seuil propre au dosage Elecsys. | [S1] |
| Cas clinique, question 3 (patiente sous apixaban) | La conduite proposée était incomplète, voire ambiguë, sur l'anticoagulation parentérale pendant l'angioplastie. | mineure | Ajouté : anticoagulation parentérale complémentaire pendant l'angioplastie quel que soit le délai depuis la dernière prise d'AOD (ESC 2020) ; pas de chevauchement en dehors de la salle ; voie radiale. | [S4] |
| § 21 (catégories de risque ESC 2020) | Erreur factuelle : la catégorie « intermédiaire » appartenait à l'ESC 2015, pas à l'ESC 2020. | mineure | ESC 2020 : très haut, haut et faible risque ; la catégorie intermédiaire (< 72 h) a été supprimée en 2020. | [S4] |
| Référence S4 (ESC 2020) | Référence non vérifiée, sans DOI. | mineure | Vérifiée : Eur Heart J 2021;42(14):1289-1367, doi 10.1093/eurheartj/ehaa575, `verifiee: true`. | Recherche web |
| § 13.2.3 (fondaparinux) | Seuil rénal marqué `[À VÉRIFIER — RCP]`. | mineure | Contre-indiqué si clairance < 20 mL/min (RCP). Marqueur levé. | RCP Arixtra |
| § 13.2.4 (arrêt des P2Y12 avant pontage) | Délais marqués `[À VÉRIFIER]`. | mineure | Ticagrélor ≥ 3 j, clopidogrel ≥ 5 j, prasugrel ≥ 7 j (ESC 2023, IIa) ; aspirine poursuivie ; pas de retard en urgence. | [S1] |
| § 13.3.2 (traitement antithrombotique prolongé) | `[POSOLOGIES À VÉRIFIER]` sur le ticagrélor 60 mg et le rivaroxaban 2,5 mg. | mineure | Conformes aux RCP (PEGASUS, COMPASS), classe IIa. Ajout des autres options (clopidogrel, prasugrel). | [S1] ; RCP |

## Points vérifiés sans modification

- Stratification ESC 2023 : critères de très haut risque (< 2 h) et de haut risque (NSTEMI, ST-T dynamiques, sus-décalage transitoire, GRACE > 140 : < 24 h, IIa). Le passage de la classe I (2020) à IIa (2023) est exact.
- Prétraitement (classe III si coronarographie < 24 h ; IIb sinon). Anti-GP IIb/IIIa en sauvetage. Prasugrel préféré (IIa).
- Posologies : aspirine, P2Y12, énoxaparine 1 mg/kg/12 h (une fois par 24 h si clairance < 30 mL/min), fondaparinux 2,5 mg/j avec bolus d'HNF en salle, bivalirudine, HNF pendant l'angioplastie : conformes.
- Patient en FA (ESC 2023) : triple thérapie ≤ 1 semaine, puis AOD + clopidogrel jusqu'à 12 mois, puis AOD seul ; prasugrel et ticagrélor exclus. Conforme.
- QCM-CARD-0037 à 0048 : réponses exactes. CAS-CARD-0007 : conforme. CAS-CARD-0008 : ECG rendu cohérent avec les seuils de sus-décalage (2 mm en V2–V4).

## Reste à faire

1. **Bloquant** — HNF en attente de coronarographie (§ 13.2.3) : bolus et débit de perfusion (60–70 UI/kg puis 12–15 UI/kg/h, TCA 1,5–2,5 fois le témoin, ou 70–100 UI/kg puis TCA 60–80 s). Le libellé du tableau ESC 2023 n'a pas pu être confirmé. Marqueur maintenu.
2. Positions ACC/AHA 2025 marquées `[À VÉRIFIER]` au § 21 (formulations et hiérarchie des P2Y12).
3. Arrêt de la metformine autour de l'injection de produit de contraste ; seuils transfusionnels.
4. Données algériennes : disponibilité de la troponine ultrasensible, accès à la coronarographie dans les 24 h, molécules disponibles.
5. Faire relire le dossier par un enseignant.
