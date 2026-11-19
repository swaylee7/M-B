# Rapport d'audit — DOS-CARD-0007 « Les troubles du rythme cardiaque »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (scientifique, IA) et AUD-02 (posologies, IA). Ils sont indépendants du rédacteur DOS-01.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Il reste un marqueur posologique (glucagon et aminophylline dans les bradycardies, doses non confirmées).
- **Bilan** : 9 corrections (critiques 0, majeures 0, mineures 9). Marqueurs posologiques : 1 levé sur 2 (TV).
- **Vérifications** : PubMed (ACC/AHA 2023 FA, INVICTUS, PROCAMIO ; résumés d'INVICTUS et de PROCAMIO lus) ; recherches web sur les classes ESC 2024 de la cardioversion pharmacologique et ESC 2022 du traitement IV de la TV (sources secondaires concordantes).
- **Cohérence avec le lot 1** : CHA2DS2-VA (ESC 2024), doses d'AOD et critères de réduction identiques à DOS-CARD-0001 et DOS-PHAR-0002.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2.2 (TV monomorphe bien tolérée) | `[POSOLOGIE À VÉRIFIER]` ; amiodarone « 300 mg en 10–60 min puis perfusion » imprécise ; classes absentes. | mineure | Marqueur levé : cardioversion électrique en première intention (I) ; procaïnamide IV si cardiopathie structurelle (IIa ; schéma PROCAMIO 10 mg/kg en 20 min ; disponibilité locale à vérifier) ; amiodarone IV en l'absence de diagnostic établi (IIb) : 300 mg en 10–20 min puis 900 mg/24 h. | ESC 2022 [S3] ; PROCAMIO [S11] ; ERC 2021 [S7] |
| § 13.2.2 (cardioversion pharmacologique) | Tableau attribué à l'ESC 2020, sans les classes ESC 2024. | mineure | Ajout : flécaïnide ou propafénone IV (I, hors HVG sévère, ICFEr, coronaropathie) ; vernakalant IV (I, hors SCA récent, ICFEr, RA serré) ; amiodarone IV (I si HVG sévère, ICFEr ou coronaropathie, conversion plus lente) ; pilule de poche (IIa). | ESC 2024 [S1] |
| § 13.3.2 (contrôle de la fréquence) | Absence de l'option aiguë en cas d'instabilité ou de FEVG très altérée. | mineure | Amiodarone IV, digoxine, esmolol ou landiolol à envisager (IIa). | ESC 2024 [S1] |
| § 13.2.4 (énergie de la cardioversion) | Marqueur `[À VÉRIFIER]`. | mineure | Levé : premier choc à énergie maximale pour la FA, 70–120 J pour le flutter et les TSV (ERC 2021) ; respecter les indications du fabricant. | [S7] |
| § 21 (score, ACC/AHA 2023) | Seuil de risque annuel `[À VÉRIFIER]`. | mineure | Anticoagulation recommandée si risque annuel ≥ 2 % (CHA2DS2-VASc ≥ 2 chez l'homme, ≥ 3 chez la femme), raisonnable entre 1 et 2 %. | [S9] |
| § 21 (classification ACC/AHA 2023) | Stades `[À VÉRIFIER]`. | mineure | Stades 1 à 4 détaillés (3A–3D). | [S9] |
| § 21 (fermeture de l'auricule) | Position ACC/AHA `[À VÉRIFIER]`. | mineure | Classe 2a en cas de contre-indication non réversible à l'anticoagulation. | [S9] |
| Sources | S9 (ACC/AHA 2023) et S10 (INVICTUS) non vérifiées. | mineure | Vérifiées (DOI, PMID) ; S11 (PROCAMIO) ajoutée. | PubMed |
| En-tête, bandeau, note finale | Statut et note obsolètes. | mineure | Mis à jour. | — |

## Posologies et scores confrontés et conformes (sans modification)

- **Contrôle de la fréquence** (ESC 2020/2024) : métoprolol 2,5–5 mg IV puis 25–100 mg × 2/j ; bisoprolol 1,25–20 mg/j ; esmolol 500 µg/kg puis 50–300 µg/kg/min ; diltiazem 0,25 mg/kg puis 5–15 mg/h, 60 mg × 3/j jusqu'à 360 mg/j ; vérapamil 2,5–10 mg IV, 40 mg × 2/j jusqu'à 480 mg/j ; digoxine 0,5 mg IV (0,75–1,5 mg/24 h), 0,0625–0,25 mg/j ; amiodarone 300 mg IV en 30–60 min puis 900–1 200 mg/24 h, 200 mg/j.
- **Cardioversion** : flécaïnide 2 mg/kg IV ou 200–300 mg per os ; propafénone 1,5–2 mg/kg IV ou 450–600 mg ; vernakalant 3 puis 2 mg/kg et contre-indications ; amiodarone 5–7 mg/kg en 1–2 h puis 50 mg/h (≤ 1,2 g/24 h). Seuil de 24 h, 3 semaines d'anticoagulation ou ETO, 4 semaines après.
- **TSV** : adénosine 6 puis 12 mg (6–18 mg), vérapamil 0,075–0,15 mg/kg, diltiazem 0,25 mg/kg, métoprolol 2,5–15 mg. **Arrêt cardiaque** : amiodarone 300 puis 150 mg, adrénaline 1 mg, lidocaïne 100 mg. **Torsades** : magnésium 2 g. **Bradycardie** : atropine 0,5 mg jusqu'à 3 mg, isoprénaline 5 µg/min, adrénaline 2–10 µg/min.
- **AOD dans la FA** : apixaban (2 critères sur 3, ou clairance 15–29), rivaroxaban 15 mg (15–49 mL/min), dabigatran (110 mg ; contre-indiqué < 30), édoxaban 30 mg : conformes aux RCP et à DOS-PHAR-0002.
- **Scores et seuils** : CHA2DS2-VA (≥ 2 : I ; 1 : IIa ; hors valve mécanique et RM modéré à serré), HAS-BLED, classification de la FA, QTc ≥ 480 ms, Brugada de type 1, stimulation (ESC 2021), DAI (ESC 2022), syncope (ESC 2018), FA pré-excitée (ESC 2019 : ibutilide ou procaïnamide IIa, amiodarone III).

## QCM et cas associés

- **QCM-CARD-0113 à 0124** : réponses exactes ; les 8 QCM intégrés concordent avec le lot. 12/12 `audite_valide`.
- **CAS-CARD-0103** (FA sur RM rhumatismal) et **CAS-CARD-0104** (BAV complet) : conformes. 2/2 `audite_valide`.

## Reste à faire

1. **Bloquant** : doses du glucagon (intoxication par bêtabloquant ou inhibiteur calcique) et de l'aminophylline (marqueur maintenu ; ERC 2021 ou protocoles de toxicologie à consulter).
2. Classes ESC 2024 et ESC 2022 recoupées par des sources secondaires : à confirmer sur les textes intégraux ; définition de la bradycardie (FC < 50/min) selon l'ESC 2021 `[À VÉRIFIER]` ; contenu de l'ERC 2025 sur les arythmies péri-arrêt.
3. Disponibilité en Algérie du vernakalant, de l'ibutilide, de la procaïnamide, de l'isoprénaline ; accès à l'ablation et aux DAI ; données épidémiologiques sur la FA.
4. Relecture par un enseignant.
