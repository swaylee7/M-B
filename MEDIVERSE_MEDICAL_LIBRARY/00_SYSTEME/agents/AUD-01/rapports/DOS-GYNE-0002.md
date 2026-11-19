# Rapport d'audit — DOS-GYNE-0002 « Cancer du col de l'utérus »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-07)
- **Objets audités** : dossier v1.0 ; QCM-GYNE-0713 à 0724 et CAS-GYNE-0703, CAS-GYNE-0704 (lots `DOS-07.json`)
- **Verdict** : `audite_valide` (v1.1) — aucune erreur critique ni majeure restante ; aucun marqueur de posologie ; références majeures vérifiées (dont ESGO 2023 en texte intégral). Relecture enseignante (`valide_enseignant`) non faite.
- **Documents acquis consultés (texte intégral)** : ESGO/ESTRO/ESP 2023 (DOC-00094) ; OMS 2021, dépistage et traitement des lésions précancéreuses (DOC-00044) ; arrêté algérien du 28/04/2026, JORADP n° 36 (DOC-00071). Recherches web : révision FIGO 2025, KEYNOTE-A18, INTERLACE, SHAPE, position OMS 2022 sur les vaccins HPV.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §15.1, §15.3, cas §17, §18, §21, QCM-GYNE-0722 | Vaccination HPV en Algérie présentée comme « à vérifier » | **majeure** (actualité nationale) | Arrêté du 28 avril 2026 (JORADP n° 36 du 17/05/2026) : vaccination « anti human papilloma-virus » inscrite au calendrier obligatoire à **11-13 ans** ; le texte ne précise ni le sexe, ni le nombre de doses, ni le vaccin (laissé [À VÉRIFIER], sans extrapolation) | DOC-00071 [S15] |
| §13.2.2 | Ganglion sentinelle « complété ou remplacé par une lymphadénectomie selon les situations » (imprécis) | **majeure** | ESGO 2023 : premier temps chirurgical, vert d'indocyanine préféré, examen extemporané ; si négatif, lymphadénectomie pelvienne systématique (T1b1-T2a1) ; sentinelle seule pour T1a1 avec emboles et T1a2 ; atteinte peropératoire → abandon de l'hystérectomie radicale et radiochimiothérapie | DOC-00094 [S9] |
| YAML / §22 | S9-S13 non vérifiées ; pas de source pour le texte algérien ni pour le schéma vaccinal OMS | **majeure** (traçabilité) | S9 (DOC-00094, DOI), S10 (citée par S9), S11 (Lancet 2024;404:1321-1332, DOI), S12 (NEJM 2024;390:819-829, DOI), S13 (Lancet 2024;404:1525-1535) vérifiées ; S15 (arrêté 2026) et S16 (OMS 2022) ajoutées | Recherche web, documents acquis |
| §15.1 | Schéma OMS 2022 [À VÉRIFIER] | mineure | 1 ou 2 doses de 9 à 20 ans ; 2 doses après 21 ans ; ≥ 2 (si possible 3) chez l'immunodéprimé | OMS, WER 2022;97(50) [S16] |
| §1, §18, QCM-GYNE-0713 | Seuil d'élimination « ≤ 4 » | mineure | « < 4 » pour 100 000 femmes-années | Stratégie OMS 2020 [S3] |
| §7.3 | Révision FIGO 2025 non mentionnée | mineure | Aucune révision FIGO 2025 identifiée ; FIGO 2018 reste la référence (avec le TNM selon l'ESGO) ; rectificatif évoqué en 2024 non consulté [À VÉRIFIER] | Recherche web |
| §9.2 | IRM « à partir du stade IB1 » ; cystoscopie « si suspicion » ; TEP ≥ IB3 | mineure | IRM obligatoire au bilan initial (facultative pour T1a à marges saines après conisation) ; cystoscopie/rectoscopie non recommandées en routine ; TEP pour T1b3+ (sauf T2a1) et avant toute radiochimiothérapie curative ; curage lombo-aortique de stadification envisageable | ESGO 2023 |
| §13.2.2 | Voie mini-invasive | mineure | Admise seulement pour tumeurs < 2 cm à marges saines après conisation, en centre expert | ESGO 2023 |
| §13.2.2 | SHAPE et Querleu-Morrow [À VÉRIFIER] | mineure | SHAPE : récidive pelvienne à 3 ans 2,52 % vs 2,17 %, moins de troubles urinaires ; Querleu-Morrow modifiée 2017 | S12 ; ESGO 2023 |
| §13.2.3 | Radiothérapie « 45-50 Gy » [À VÉRIFIER] | mineure | 45 Gy/25 fr ou 46 Gy/23 fr ; boost ganglionnaire ≈ 60 Gy EQD2 ; pas de boost externe tumoral | ESGO 2023 |
| §13.2.3 | Cisplatine 40 mg/m² [POSOLOGIE À VÉRIFIER] | mineure (posologie) | Dose confirmée ; **marqueur levé** ; carboplatine AUC 2 si contre-indication | ESGO 2023 |
| §13.2.3, cas | Durée totale « ≤ 7-8 semaines » | mineure | Ne pas dépasser **7 semaines** | ESGO 2023 |
| §13.2.4 | INTERLACE, KEYNOTE-A18, traitement métastatique [À VÉRIFIER] | mineure | Résultats chiffrés (INTERLACE : SG 80 % vs 72 % à 5 ans ; KEYNOTE-A18 : SG 82,6 % vs 74,8 % à 36 mois) ; métastatique : platine-paclitaxel ± bévacizumab, + pembrolizumab si CPS ≥ 1, cémiplimab en 2e ligne | S11, S13, ESGO 2023 |
| §13.3 | IA1 avec emboles / IA2 | mineure | Conisation ou hystérectomie simple sans paramétrectomie ; sentinelle à envisager (IA1 LVSI+, IA2 LVSI−), obligatoire (IA2 LVSI+) | ESGO 2023 |
| §14.2, cas | Surveillance (rythme fixe, frottis « difficiles ») [À VÉRIFIER] | mineure | Surveillance individualisée ; imagerie de réponse pas avant 3 mois ; cytologie non recommandée après irradiation | ESGO 2023 |
| §15.2, §21 | Âges et intervalles OMS [À VÉRIFIER] | mineure | 30 ans / 5-10 ans ; VIH 25 ans / 3-5 ans confirmés (rec. 5, 8, 25, 28) | DOC-00044 |
| §15.2, QCM-GYNE-0716 | « Le triage réduit **de moitié** les traitements » | mineure (inexactitude) | « réduit les traitements inutiles » | DOC-00044 |
| §15.2 algorithme | Triage négatif → HPV « à 12 mois » | mineure | 24 mois (population générale), 12 mois (femmes vivant avec le VIH) | OMS 2021, rec. 11 et 31 |
| §7.1-7.2 | S10 [À VÉRIFIER] | mineure | Marqueurs levés (édition 2020 citée par l'ESGO) | DOC-00094 |
| §20 | QCM 1 et corrigés (≤ 4 ; « de moitié ») | mineure | Corrigés | — |

**Erreurs critiques** : aucune. Stadification FIGO 2018 (IA1 < 3 mm, IA2 3-5 mm, IB1 < 2 cm, IB2 2-4 cm, IB3 ≥ 4 cm, IIA1/IIA2, IIB, IIIA, IIIB, IIIC1/IIIC2 r/p, IVA/IVB), LACC, cibles 90-70-90 : exacts.

## QCM et cas
QCM-GYNE-0713 à 0724 : réponses exactes ; 0713, 0716, 0720, 0722 mis à jour → `audite_valide`. CAS-GYNE-0703 (IIIC1r) : radiothérapie, durée totale et surveillance corrigées, sources ajoutées ; CAS-GYNE-0704 (IA1) exact → `audite_valide`.

## Références
16 sources ; 15 vérifiées. Non vérifiée : S14 (Bethesda 2015, référence mineure).

## Reste à faire (non bloquant)
1. Modalités d'application de l'arrêté du 28/04/2026 (sexe, nombre de doses, vaccin) : instructions techniques du ministère de la Santé.
2. Contenu exact du corrigendum FIGO 2019 et du rectificatif mentionné en 2024.
3. Chiffres mondiaux GLOBOCAN 2022, atlas du registre de Sétif 1986-2016, survies par stade (rapport FIGO 2021), terminologie LAST (p16), recommandations HAS 2019.
4. Vérifier S14 (Bethesda) et la pagination de la publication KEYNOTE-A18 sur la survie sans progression (Lancet 2024;403:1341-1350).
