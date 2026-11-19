# Rapport d'audit — DOS-INFE-0003 « Fièvres typhoïde et paratyphoïdes : signes, diagnostic, traitement »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-02, lot 2)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1) ; QCM-INFE-0201 à 0213 ; CAS-INFE-0201 et 0202 (`DOS-02-lot2.json`)
- **Verdict** : `audite_valide` — 0 erreur critique ; 1 erreur majeure corrigée (actualité) ; 18 corrections mineures ; **0 marqueur `[POSOLOGIE À VÉRIFIER]` restant** (4 levés : méropénem XDR dans le dossier et dans l'algorithme, dexaméthasone, portage chronique ; + CAS-INFE-0202)
- **Sauvegarde** : `00_SYSTEME/sauvegardes/20261119/07_MEDECINE_INTERNE/28_INFE_INFECTIOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-INFE-0003__FIEVRES_TYPHOIDE_ET_PARATYPHOIDES.avant_audit.md`

## Vérifications sur les textes
- **Livre AWaRe de l'OMS 2022 (DOC-00039), chapitre 15 et tableau 24.7** (pdftotext) : ciprofloxacine 500 mg/12 h (enfant 15 mg/kg/dose/12 h, tranches de poids) si faible risque de résistance aux FQ ; sinon azithromycine 1 g J1 puis 500 mg/j (enfant 20 mg/kg/j) pour les formes légères, ceftriaxone 2 g/j (enfant 80 mg/kg/j) pour les formes sévères ; 7 jours (légère) / 10 jours (sévère, apyrexie ≥ 48 h) ; Widal non fiable ; hémocultures positives chez 5–7 patients sur 10 ; monothérapie recommandée ; XDR au Pakistan depuis 2016 ; méropénem 1 g/8 h (enfant 20 mg/kg/8 h) dans les infections intra-abdominales compliquées, 2 g/8 h dans le tableau du sepsis. **Conformes.**
- **Note de synthèse OMS sur les vaccins antityphoïdiques, 14 août 2026** (WER 2026;101(32):166-180 ; téléchargée depuis IRIS, lue) : **remplace la note de 2018** citée comme actuelle par le dossier.
- **Document technique OMS 2003 (WHO/V&B/03.07)** (IRIS, lu) : incubation, rechutes, portage, dexaméthasone, éviction des manipulateurs d'aliments.
- **PubMed (API eutils)** : Parry 2002 (PMID 12456854), Hoffman 1984 (PMID 6361558, résumé lu : 3 mg/kg, létalité 10 % vs 55,6 %), Klemm 2018 (PMID 29463654), Shakya 2019 (PMID 31800986) confirmés.
- QCM-INFE-0201 à 0213 : réponses exactes ; CAS-INFE-0201/0202 : exacts après les précisions ci-dessous.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 15.3 (et § 2, 18, 19, 21) | Note OMS de **2018** présentée comme la position actuelle (« TCV dès 6 mois en dose unique ») alors qu'elle est **remplacée par la note d'août 2026** : 1re dose entre **9 et 24 mois** là où l'incidence est élevée, dès 2 ans si incidence moyenne, rappel vers 5 ans si incidence très élevée ; âges et rappels du Vi-PS et du Ty21a laissés `[À VÉRIFIER]` | **Majeure** (actualité) | Tableau et texte refaits selon la note 2026 (TCV, Vi-PS dès 2 ans avec revaccination tous les 3 ans, Ty21a dès 6 ans en 3 doses un jour sur deux, groupes particuliers, voyageurs, manipulateurs d'aliments, épidémies) ; S2 signalée « remplacée » | S11 |
| QCM-INFE-0211 (lot) | Propositions A et B fondées sur la note 2018 (« dès 6 mois ») | Mineure | Réécrites selon la note 2026 (réponses inchangées : A, B, E) | S11 |
| CAS-INFE-0202 (lot), question 4 | « Dose unique dès 6 mois selon l'OMS » | Mineure | Vaccination du voyageur selon la note 2026 (tout vaccin homologué) | S11 |
| § 13.2 c, § 13.3 | Méropénem (XDR) sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | Pas de dose OMS propre à la forme XDR : doses usuelles AWaRe (1 g/8 h ; enfant 20 mg/kg/8 h ; 2 g/8 h en sepsis) ; résistance aux carbapénèmes signalée en Asie du Sud | S1, S11 |
| CAS-INFE-0202 (lot) | Méropénem ± azithromycine sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | 20 mg/kg/8 h IV ± azithromycine 20 mg/kg/j | S1 |
| § 13.2 e | Dexaméthasone sous `[POSOLOGIE À VÉRIFIER]` et indications non précisées | Mineure (levée) | 3 mg/kg IV en 30 min puis 1 mg/kg/6 h, 8 doses, si délire, obnubilation, stupeur, coma ou choc, après PL ; données anciennes signalées | S12, S9 |
| § 13.4 | Portage chronique sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | Ciprofloxacine 750 mg × 2/j, 28 jours ; alternatives ; cholécystectomie si lithiase | S12 |
| § 8.1 | Incubation `[À VÉRIFIER : extrêmes]` | Mineure | 8–14 jours (3 à > 60 jours) | S12 |
| § 12.1 | Fréquence des rechutes et du portage non chiffrée | Mineure | Rechutes 5–20 % ; portage 1–5 % | S12 |
| § 14 | Coprocultures de contrôle `[À VÉRIFIER]` | Mineure | 3 coprocultures négatives à ≥ 1 mois d'intervalle avant reprise des manipulateurs d'aliments (OMS 2003) ; réglementation algérienne non retrouvée | S12 |
| § 3.1 | Épidémiologie limitée aux données 2017 ; résistances récentes absentes | Mineure | GBD 2023 (6,2 millions de cas, 72 000 décès) ; résistances à l'azithromycine, aux C3G et aux carbapénèmes en Asie du Sud | S11 |
| § 17 et CAS-INFE-0201 | Patient « prostré, répondant lentement » classé en forme non compliquée alors que l'algorithme range l'encéphalopathie parmi les formes graves | Mineure | Précisé : éveillé, orienté, Glasgow 15 ; commentaire sur les signes qui feraient basculer en forme grave | S1, S12 |
| § 20 (QCM 7-E) et QCM-INFE-0207 | « Posologie à confronter au protocole local » | Mineure | Dose usuelle du méropénem indiquée | S1 |
| § 21 | Ligne « dexaméthasone » sans position de l'OMS | Mineure | Schéma OMS 2003 ajouté | S12 |
| § 3.2, § 13.5 | Arrêté de déclaration, données de résistance et protocole national non qualifiés | Mineure | Mentions explicites « non retrouvés » | Recherche (audit) |
| YAML, § 22 | S8 et S9 non vérifiées ; S2 non signalée comme remplacée | Mineure | S8, S9 vérifiées (PubMed) ; S2 « remplacée » ; S11 et S12 ajoutées | PubMed, IRIS |
| § 2 | Historique arrêté en 2018 | Mineure | Note OMS 2026 ajoutée | S11 |
| § 18 (point 10), § 19 | Messages fondés sur la note 2018 | Mineure | Actualisés (note 2026) ; piège « citer la note 2018 » ajouté | S11 |
| § 21 (en-tête) | « Note de synthèse 2018 » | Mineure | « Note de synthèse 2026 » | S11 |

## Reste à faire (sans incidence sur le verdict)
1. E.Pilly en vigueur (S10, non vérifiée) : positions françaises (durées, azithromycine, association C3G + azithromycine, Vi-PS chez le voyageur) — `[À VÉRIFIER]` conservés au § 21.
2. Données algériennes : incidence (INSP), résistance de *S.* Typhi (réseau national), arrêté fixant les modalités de déclaration, règles d'éviction des porteurs : **non retrouvés**.
3. Femme enceinte (choix C3G/azithromycine, RCP) et quelques détails cliniques (survie, Widal, hémophagocytose) : `[À VÉRIFIER]` non posologiques conservés.
