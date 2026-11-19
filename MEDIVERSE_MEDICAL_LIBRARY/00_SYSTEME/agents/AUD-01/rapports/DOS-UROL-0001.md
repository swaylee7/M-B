# Rapport d'audit — DOS-UROL-0001 « Lithiase urinaire : diagnostic et traitement (incluant la colique néphrétique compliquée) »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-11.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**.
- **Bilan** : 11 corrections (critiques 0, majeures 0, mineures 11). Marqueurs de posologie : 9 au départ, 3 restants.
- **Vérifications** :
  - résumés Europe PMC : EAU 2025 (PMID 40268592), Pathan 2016, SUSPEND, STONE ;
  - recherche web : formulation du TME par l'EAU et révision de la section 3.4.3 dans l'édition 2026.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2.1, AINS (AUD-02) | Kétoprofène IV sans dose maximale. | mineure | 100 mg IV en 20 min, jusqu'à 3 fois par 24 h (300 mg/j au maximum), voie IV limitée à 48 h. Marqueur levé. | RCP ; [S9] |
| § 13.2.1, morphine (AUD-02) | Aucune précaution rénale. | mineure | Accumulation des métabolites en insuffisance rénale ; dose de l'essai de Pathan distinguée de la titration. Marqueur restreint aux modalités de titration. | [S14] |
| § 13.2.2 et § 21, TME | Position de l'EAU imprécise et non datée. | mineure | EAU 2025 : TME « à envisager » chez des patients sélectionnés ; éditions antérieures : option fortement recommandée pour l'uretère distal > 5 mm ; révision 2026 signalée [À VÉRIFIER]. | [S1, S2, S3] |
| § 13.2.2 (AUD-02) | Tamsulosine signalée par un marqueur. | mineure | 0,4 mg une fois par jour pendant 4 semaines au plus. Marqueur levé. | RCP ; [S12] |
| § 13.2.6, thiazidique (AUD-02) | Aucune dose. | mineure | Hydrochlorothiazide 25 mg/j, jusqu'à 50 mg/j ; surveillance de la kaliémie. Marqueur levé. | RCP |
| § 13.2.6, acide urique | Cibles de pH « à vérifier ». | mineure | 6,2–6,8 en prévention, 7,0–7,2 pour la dissolution. | EAU [S1] |
| § 13.3.1 (AUD-02) | AINS per os sans dose. | mineure | Ibuprofène 400 mg × 3/j ou diclofénac 50 mg × 2–3/j (150 mg/j au maximum), quelques jours. Marqueur levé. | RCP |
| § 17, question 2 (AUD-02) | Marqueur sur l'AINS. | mineure | Renvoi aux doses du § 13.2.1. Marqueur levé. | RCP ; [S9, S14] |
| § 17, question 4 | Marqueur faisant doublon avec le § 13.2.4. | mineure | Renvoi au § 13.2.4. | — |
| § 12.1 | « Grande majorité » des calculs ≤ 5 mm éliminés : formulation trop forte. | mineure | Environ 68 % (≤ 5 mm) et 47 % (5–10 mm) selon la méta-analyse AUA/EAU ; [À VÉRIFIER] sur la source primaire. | Méta-analyse AUA/EAU 2007 (non relue) |
| § 10.3, grossesse | Seuil de 24 SA seul mentionné. | mineure | Mise en garde de la FDA dès 20 SA ajoutée. | FDA 2020 |

## Points vérifiés sans modification

- Définitions de la colique néphrétique simple, compliquée et sur terrain à risque.
- Physiopathologie (prostaglandines, obstruction infectée).
- Imagerie : l'EAU 2025 place l'échographie en première ligne et le scanner faible dose comme référence (résumé lu) ; essai de Smith-Bindman.
- Essai de Pathan : 3 bras en double aveugle, AINS au moins aussi efficaces que la morphine avec moins d'effets indésirables.
- SUSPEND et STONE négatifs.
- Drainage par JJ ou néphrostomie d'efficacité équivalente (Pearle 1998) ; « drainer d'abord ».
- Indications de LEC, URS et NLPC ; dissolution de l'acide urique.
- Bilan métabolique de première intention ; séries algériennes (chiffres conformes aux résumés cités).

## QCM et cas associés

- QCM-UROL-1101 à 1112 : réponses exactes → `audite_valide` ; explication de 1112 complétée (cibles de pH). QCM-UROL-1106 D est conforme au résumé de l'EAU 2025.
- CAS-UROL-1101 → `audite_corrections_requises` :
  - morphine à doses réduites en insuffisance rénale ;
  - bicarbonate plutôt que citrate de potassium tant que persistent l'hyperkaliémie et l'insuffisance rénale ;
  - marqueurs maintenus (hyperkaliémie, titration).
- CAS-UROL-1102 → `audite_corrections_requises` : doses des antalgiques ajoutées ; marqueur des thiols maintenu.

## Reste à faire

1. Lire l'édition EAU 2026 en ligne [S2] : section 3.4.3 (TME), taux d'expulsion spontanée, délai avant intervention, tableau des traitements préventifs (dose des citrates alcalins).
2. Fiche HAS/SPILF en vigueur sur la pyélonéphrite : doses de C3G et d'amikacine, durée de traitement de la forme obstructive (marqueur maintenu).
3. Protocole local de titration morphinique (marqueur maintenu).
4. Relecture humaine qualifiée (urologie).
