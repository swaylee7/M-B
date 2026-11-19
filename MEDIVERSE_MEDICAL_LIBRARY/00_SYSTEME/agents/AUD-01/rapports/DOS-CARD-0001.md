# Rapport d'audit — DOS-CARD-0001 « Insuffisance cardiaque aiguë et chronique »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies et contre-indications, IA). Ils sont indépendants du rédacteur DOS-01.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Il reste 1 marqueur posologique, et le contenu ESC 2026 n'a pas été lu en texte intégral.
- **Bilan** : 11 corrections (critiques 0, majeures 1, mineures 10).
- **Recherches web utilisées** : 3. Deux ont porté sur le contenu ESC 2026, une sur STRONG-HF. WebFetch était bloqué (escardio.org et tctmd.com hors du réseau autorisé).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2.3, tableau des contre-indications (ivabradine) | La contre-indication était donnée à « FC < 60/min avant traitement ». C'est faux : le RCP fixe le seuil à une FC de repos < 70/min. Le texte contredisait aussi l'indication du § 13.3.1 (FC ≥ 70/min). | **majeure** | Seuil corrigé à FC de repos < 70/min. Ajout des contre-indications IC aiguë ou instable, association vérapamil/diltiazem et inhibiteurs puissants du CYP3A4. | RCP de l'ivabradine ; ESC 2021 [S1] |
| Encadré « actualité » (ESC 2026) | Le contenu venait de la presse et n'était pas recoupé. Les seuils de la recommandation sur les agonistes du GLP-1 manquaient. | mineure | Contenu recoupé par recherche web : deux phénotypes (< 50 % et ≥ 50 %), stades A–D, « IC décompensée », traitement fondamental, ARM en classe I quelle que soit la FEVG, GLP-1 en classe IIa (IMC ≥ 30 kg/m² ; FEVG ≥ 45 % ou ≥ 50 % selon les sources), nouvelle gradation B1/B2. La mention « texte intégral à consulter » est maintenue. | [S3] ; communiqué ESC, TCTMD, HCPLive, AJMC, Cardiovascular Business, Epocrates (sources secondaires) |
| § 12.2 (fibrillation atriale) | Le score cité était CHA2DS2-VASc, alors que l'ESC 2024 utilise le CHA2DS2-VA. | mineure | Remplacé par CHA2DS2-VA, avec ses seuils (≥ 2 : anticoagulation recommandée ; 1 : à envisager). Ajout de la source S10. | ESC 2024 FA [S10] |
| § 13.3.3 (ICFEp, évolution 2026) | La classe, l'IMC et la FEVG de la recommandation GLP-1 étaient marqués « À VÉRIFIER ». | mineure | Précisés d'après les sources concordantes. Le marqueur porte désormais sur la molécule d'ARM. | [S3] |
| § 21 (divergences, lignes ARM et GLP-1) | Formulations imprécises. | mineure | Mises en cohérence avec le recoupement. | [S3] |
| § 13.3.1 (fer IV) | La classe était mal décrite (« élargi en 2023 »). | mineure | ESC 2021 : classe IIa (FEVG < 45 %). ESC 2023 : classe I (symptômes et qualité de vie, ICFEr/ICFEmr) et classe IIa (hospitalisations). | [S1, S2] |
| Références S3, S9 | S9 (STRONG-HF) était incomplète et non vérifiée. | mineure | S9 complétée (Lancet 2022;400(10367):1938-1952, doi 10.1016/S0140-6736(22)02076-1, PMID 36356631) et passée à `verifiee: true`. Remarque S3 mise à jour. | Recherche web |
| § 13.2.2 (sacubitril/valsartan) | `[POSOLOGIE À VÉRIFIER]` sur la dose de 24/26 mg. | mineure | Marqueur levé. Critères du RCP précisés : PAS 100–110 mmHg, patient naïf ou sous faible dose d'IEC/ARA II, DFGe < 60 ou < 30, insuffisance hépatique modérée, âge ≥ 75 ans ; pas d'initiation si PAS < 100 mmHg. | RCP Entresto (EMA) |
| § 13.2.5 (inotropes) | `[POSOLOGIES À VÉRIFIER]`. | mineure | Marqueur levé : doses conformes au tableau ESC 2021. Ajout des bolus facultatifs (lévosimendan 12 µg/kg ; milrinone 25–75 µg/kg). | ESC 2021 [S1] |
| § 13.3.1 (seuils de tolérance de la titration) | Marqueur « à confronter au document ESC/HFA ». | mineure | Marqueur levé : créatinine + 50 % ou 266 µmol/L et K+ ≤ 5,5 mmol/L acceptables ; arrêt si K+ > 6,0 mmol/L ou créatinine > 310 µmol/L ou doublée. | Guide pratique ESC [S1] |
| § 13.3.1 (fer IV, posologie) | `[POSOLOGIE À VÉRIFIER — RCP]`. | mineure | Marqueur levé : tableau de dose cumulée du carboxymaltose ferrique (Hb, poids), maximum 1 000 mg par semaine, surveillance de la phosphatémie ; dérisomaltose jusqu'à 20 mg/kg par perfusion. | RCP Ferinject, Monofer |

## Points vérifiés sans modification

- Tableau des doses initiales et cibles (IEC, ARNI, BB, ARM, iSGLT2, ARA II, ivabradine, vériciguat, digoxine, hydralazine/dinitrate) : conforme à l'ESC 2021. Tableau des diurétiques : conforme.
- IC aiguë : furosémide IV 20–40 mg ou 1 à 2 fois la dose orale ; natriurèse < 50–70 mmol/L à 2 h ; diurèse < 100–150 mL/h ; maximum 400–600 mg/j. Trinitrine 10–20 puis jusqu'à 200 µg/min. Noradrénaline 0,2–1 µg/kg/min (tableau ESC 2021). Tout est conforme.
- Peptides natriurétiques (35/125 ; 100/300/120), carence martiale, critères échographiques de l'ICFEp, H2FPEF, DAI et CRT, CHAMPIT : conformes.
- Chiffres STEPS (31,6 % ; 36,2 %) recoupés par recherche web sur le résumé de Moussouni 2022.

## QCM et cas associés

- **QCM-CARD-0001 à 0012** : les réponses sont exactes. QCM-0012 (ESC 2026) : explications précisées. Il est laissé en `audite_corrections_requises` en attendant le texte intégral ESC 2026.
- **CAS-CARD-0001** : CHA2DS2-VASc remplacé par CHA2DS2-VA (score 5). Marqueur levé sur la dose de l'AOD (apixaban 5 mg × 2/j, aucun critère de réduction). Mention ESC 2026 reformulée.
- **CAS-CARD-0002** : marqueur levé (AVK et non AOD dans le rétrécissement mitral modéré à serré : ESC/EACTS, essai INVICTUS).

## Reste à faire

1. **Bromocriptine** (cardiomyopathie du péripartum, § 10.3) : le marqueur `[POSOLOGIE À VÉRIFIER]` est maintenu. Le schéma n'a pas été confirmé par recherche web, et la recommandation ESC Grossesse la plus récente est à consulter.
2. **ESC 2026 [S3]** : lire le texte intégral pour la liste des auteurs, le volume et les pages, les classes et niveaux exacts, la molécule d'ARM, le seuil de FEVG de la recommandation GLP-1, le statut de l'IC à FEVG améliorée, la place de l'acétazolamide (§ 16.3) et la taxonomie du traitement.
3. Vérifier la référence S10 (ESC 2024 FA, DOI présumé 10.1093/eurheartj/ehae176).
4. Données algériennes encore marquées `[À VÉRIFIER]` : incidence de l'IC, part des valvulopathies rhumatismales, disponibilité et remboursement des molécules, accès aux dispositifs et à la greffe.
5. Ajouter les sources du seuil de baisse du NT-proBNP > 30 %, des stades SCAI, de MAGGIC et du Seattle HF Model.
6. Faire relire le dossier par un enseignant (statut `valide_enseignant`).
