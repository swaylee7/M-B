# Rapport d'audit — DOS-IMMU-0002 « États d'hypersensibilité I à IV, choc anaphylactique »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-13
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_valide`** (0 critique, 0 majeure, 11 mineures ; marqueurs de posologie levés : 2/2) — relecture enseignante requise pour `valide_enseignant`.

## Documents lus pendant l'audit
- **WAO 2020** [S7] en texte intégral (PMC7607509 ; document acquis DOC-00086) :
  - posologie de l'adrénaline (texte et **tableau 6**) ;
  - remplissage (bolus de 20 mL/kg) ;
  - position, glucagon, corticoïdes ;
  - réaction biphasique (environ la moitié dans les 6 à 12 h) ;
  - tryptase (élevée de 15 min à 3 h, pic à 1-2 h, 36-40 % < 11,4 µg/L, basale ≥ 24 h) ;
  - épidémiologie (50-112/100 000 personnes-années ; 0,3-5,1 % ; 26,5-54 % de récidives) ;
  - disponibilité des auto-injecteurs (32 % des pays).
- Résumés PubMed :
  - EAACI 2021 [S8] : adrénaline IM précoce en première ligne, prélèvement de la tryptase ;
  - EAACI 2023 [S5] : « neuf types » ;
  - ESCD 2026 [S18] ;
  - Fennouh 2026 [S19] : 4,69 % ; chiens 16,9 % ; Sud 10,51 %.
- Inaccessibles : texte de l'EAACI 2021 (Wiley et dépôt universitaire bloqués), SFMU 2016 et son erratum (afpa.org et link.springer.com bloqués).

## Posologie de l'adrénaline IM (priorité AUD-02)
- Dossier conforme à la WAO 2020 :
  - **0,01 mg/kg** de la solution à 1 mg/mL, **maximum 0,5 mg** par injection (adolescent et adulte) ;
  - répétée **toutes les 5 à 15 min** si les symptômes persistent (donc dès 5 min) ;
  - barème du tableau 6 : < 10 kg 0,01 mg/kg ; 1-5 ans 0,15 mg ; 6-12 ans 0,3 mg ; adolescent et adulte 0,5 mg.
- **Cohérence** : barème identique dans DOS-MINT_REA-0001 (tableau des vasopresseurs) et DOS-PEDI-0002. Aucune divergence créée : le dossier présente le barème de la WAO sans commentaire sur un plafond pédiatrique, que l'agent d'harmonisation traite.
- Marqueur `[POSOLOGIE À VÉRIFIER]` **levé** : posologie standard, source nommée et relue.
- Remplissage : bolus de 20 mL/kg de cristalloïdes en cas d'instabilité cardiovasculaire (WAO 2020) ; marqueur levé.
- **Point transversal signalé** : DOS-MINT_REA-0001 indique « 500-1 000 mL chez l'adulte, 10-20 mL/kg chez l'enfant [S13 — À VÉRIFIER] ». La WAO 2020 donne un bolus de 20 mL/kg. À harmoniser par l'agent de cohérence, sans modification ici.

## Tableau des corrections

11 corrections en 9 lignes (la nomenclature EAACI est corrigée aux §§ 2 et 21, le délai du type II aux §§ 5.1 et 16.2).

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 14.1 (2) | Marqueur de posologie sur l'adrénaline IM ; intervalle de répétition | Mineure | Dose vérifiée ; répétition « toutes les 5 à 15 min (dès 5 min) » ; voie IV réservée ; EAACI 2021 citée pour la première ligne ; marqueur levé | [S7] tableau 6, [S8] |
| 14.1 (4) | Marqueur sur le remplissage | Mineure | Bolus de 20 mL/kg ; O2 à haut débit ; voie veineuse de gros calibre ; marqueur levé | [S7] |
| 14.1 (9) | Auto-injecteurs en Algérie `[À VÉRIFIER]` | Mineure | Données WAO (32 % des pays ; seringues pré-remplies ou ampoules à défaut) ; non-vérification en Algérie déclarée | [S7] |
| 14.1 | Erratum de la SFMU 2016 non caractérisé | Mineure | Référence de l'erratum ; texte non relu ; doses présentées = WAO | [S12] |
| 2, 21 | EAACI 2023 : « sept types » | Mineure | « neuf types » (I-III, IVa-c, V, VI, VII) | [S5] résumé |
| 5.1, 16.2 | Délai du type II « heures à jours », contredit par l'accident ABO (minutes) | Mineure | « minutes (accident ABO) à jours » | [S1, S3] ; DOS-HEMA-0006 |
| 8.1 | Proportion de tryptases normales non chiffrée | Mineure | 36-40 % < 11,4 µg/L ; élévation de 15 min à 3 h ou plus | [S7] |
| 21 | Tranches de la SFMU `[À VÉRIFIER]` | Mineure | Ligne reformulée : barème WAO, cohérence avec MINT_REA/PEDI, SFMU non relue | [S7] |
| 21 | Patch-tests ESCD 2026 `[À VÉRIFIER]` | Mineure | Résumé seul relu ; principes de 2015 maintenus | [S17], [S18] |

## Lot (QCM, cas)
- 13 QCM (QCM-IMMU-1314 à 1326) relus sans erreur ; posologie des QCM conforme à la WAO 2020 ; 13/13 `audite_valide`.
- CAS-IMMU-1303 (kyste hydatique) : tryptase (seuil 9,2 µg/L) exacte ; adrénaline IV titrée justifiée en contexte peropératoire ; marqueur remplacé par un renvoi (albendazole + praziquantel si déversement : DOS-CDIG-0001, OMS 2025) ; `audite_valide`.
- CAS-IMMU-1304 (henné noir) : exact ; marqueur sans dose retiré ; `audite_valide`.

## Reste à faire
- Relire le texte intégral de l'EAACI 2021, de la SFMU 2016 et de son erratum dès que les hôtes sont accessibles.
- Vérifier la disponibilité des auto-injecteurs d'adrénaline en Algérie (nomenclature nationale).
- Harmoniser le volume de remplissage avec DOS-MINT_REA-0001 (voir ci-dessus).
- Relecture enseignante.
