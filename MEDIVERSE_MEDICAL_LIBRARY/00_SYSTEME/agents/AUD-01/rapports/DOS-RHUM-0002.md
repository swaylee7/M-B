# Rapport d'audit — DOS-RHUM-0002 « Pelvispondylite rhumatismale (spondyloarthrite axiale) : diagnostic et traitement »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-09.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**.
  - Aucun marqueur posologique restant.
  - Restent : instruction algérienne ITL 2024 non relue ; RCP (S13) non consultés ; chiffres PROSPA non lus (pas de résumé disponible).
- **Bilan** : 12 corrections (critiques 0, majeures 1, mineures 11). AUD-01 : 8 ; AUD-02 : 4.
- **Vérifications** :
  - catalogue REC-0460 ;
  - résumés Europe PMC : Ziade 2017 (HLA-B27), ACR/SAA/SPARTAN 2019 (page PMC), Götestam Skorpen 2016 ;
  - OMS 2024 (DOC-00027) et S3 allemande 2026, partie 2 (texte intégral).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2.7, point 1 | Traitement de l'ITL sans schéma ni délai. | majeure | Schémas de l'OMS 2024, interactions, délai de 4 semaines (S3 2026) ; instruction algérienne « à confirmer ». | [S15, S16] |
| § 3 et § 9.1 | Le HLA-B27 était présenté comme « de valeur moindre » au Maghreb. La revue source conclut que son dosage reste utile, du fait d'odds ratios élevés (21,6 à 105,6). | mineure | Nuance : sensibilité moindre, mais forte valeur d'orientation d'un HLA-B27 positif. | Ziade 2017 [S7] |
| § 10, forme de la femme | « Certains anti-TNF utilisables [À VÉRIFIER] ». | mineure | Anti-TNF raisonnablement sûrs aux 1er et 2e trimestres (EULAR 2016). | [S17] |
| § 13.2.2 | Critère d'échec des AINS marqué « À VÉRIFIER ». | mineure | ≥ 2 AINS sur 4 semaines au total (algorithme ASAS-EULAR). | [S1] |
| § 13.2.6, ligne JAK | Mention « RCP À VÉRIFIER » sans les restrictions de l'EMA. | mineure | Restrictions EMA 2023 ajoutées. | [S14] |
| § 21, décroissance | Position de l'ACR 2019 « à vérifier ». | mineure | Décroissance et arrêt des biothérapies déconseillés chez le patient stable (résumé relu). | [S6] |
| § 21, ITL | Pas de référence internationale sur le traitement. | mineure | OMS 2024 et S3 2026 ajoutées. | [S15, S16] |
| § 13.2.2, AINS (AUD-02) | Marqueur posologique. | — | Levé : dose maximale du RCP (exemples : naproxène 500 mg × 2/j, diclofénac ≤ 150 mg/j, célécoxib 200–400 mg/j, étoricoxib 60–90 mg/j). | RCP [S13] |
| § 13.2.5, sulfasalazine (AUD-02) | Marqueur posologique. | — | Levé : jusqu'à 2 g/j (3 g/j au maximum). | [S13] |
| § 13.2.6, biothérapies (AUD-02) | Marqueur posologique. | — | Levé : tableau des doses d'AMM dans la SpA axiale (anti-TNF, infliximab 5 mg/kg, sécukinumab 150 mg, ixékizumab, bimékizumab ; tofacitinib, upadacitinib). | [S13] |
| § 17, cas (AUD-02) | Marqueur posologique sur les AINS. | — | Levé (renvoi au § 13.2.2). | [S13] |

## Points vérifiés sans modification

- Critères de New York modifiés : grade ≥ 2 bilatéral ou grade 3–4 unilatéral, + 1 critère clinique.
- Critères ASAS 2009 de lombalgie inflammatoire (≥ 4/5) et de SpA axiale (lombalgie ≥ 3 mois, début < 45 ans ; imagerie + 1 signe, ou HLA-B27 + 2 signes ; liste des signes).
- Seuils de l'ASDAS (< 1,3 ; < 2,1 ; ≤ 3,5 ; > 3,5) ; BASDAI ≥ 4.
- Indication des b/tsDMARD selon l'ASAS-EULAR 2022 (ASDAS ≥ 2,1, échec de 2 AINS, CRP, IRM ou radiographie positive).
- Choix selon l'atteinte extra-squelettique : anticorps monoclonal anti-TNF si uvéite ou MICI ; anti-IL-17 si psoriasis ; inefficacité des anti-IL-23 sur l'atteinte axiale.
- Diagnostics différentiels infectieux algériens (brucellose, tuberculose).

## QCM et cas associés

- **QCM-RHUM-0915 à 0927** : exacts (QCM-RHUM-0927 : explication complétée) → `audite_valide`.
- **CAS-RHUM-0903** : marqueur AINS levé → `audite_valide`.
- **CAS-RHUM-0904** (sacro-iliite brucellienne) : la référence d'**Ioannina** (consensus de 2007 sur le traitement de la brucellose) y est citée à juste titre.
  - Ce cas traite le principal diagnostic différentiel infectieux de la SpA axiale en Algérie ; le texte n'est cité ni dans le dossier ni dans les autres cas.
  - Référence complétée et vérifiée : PMID 18162038, catalogue REC-0289, document DOC-00080 relu.
  - Posologies levées : doxycycline 100 mg × 2/j au moins 6 semaines, avec streptomycine 15 mg/kg/j pendant 2–3 semaines, gentamicine 5 mg/kg/j pendant 7 jours ou rifampicine 600–900 mg/j ; ≥ 3 mois pour une spondylodiscite.
  - Statut : `audite_valide`.

## Reste à faire

1. Instruction ITL 2024 : schémas et délai ; S10 à vérifier.
2. RCP en vigueur pour les doses levées (S13).
3. Lire PROSPA 2026 (S8) et rechercher des données algériennes.
4. Texte intégral de l'ASAS-EULAR 2022 : critère de réponse à 12 semaines (« à confirmer »), numéros des recommandations.
5. EULAR 2023 (rhumatisme psoriasique) sur l'atteinte axiale.
6. Accès à l'IRM et nomenclature des biothérapies en Algérie.
7. Relecture enseignant.
