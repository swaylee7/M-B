# Rapport d'audit — DOS-INFE-0006 « États septicémiques (sepsis) : diagnostic, pronostic, traitement »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-02, lot 2)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1) ; QCM-INFE-0240 à 0252 ; CAS-INFE-0207 et 0208 (`DOS-02-lot2.json`)
- **Verdict** : `audite_corrections_requises` — 0 erreur critique ; 1 erreur majeure corrigée (CAS-INFE-0208) ; 13 corrections mineures ; **marqueurs `[POSOLOGIE À VÉRIFIER]` restants : 1 dans le dossier (noradrénaline : dose et unité base/tartrate, maintenu par cohérence avec DOS-MINT_REA-0001) + 1 dans CAS-INFE-0208 (dose maximale et durée de l'antistaphylococcique)** ; texte de la SSC 2026 non lu
- **Sauvegarde** : `00_SYSTEME/sauvegardes/20261119/07_MEDECINE_INTERNE/28_INFE_INFECTIOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-INFE-0006__ETATS_SEPTICEMIQUES_SEPSIS.avant_audit.md`

## Vérifications sur les textes
- **SSC 2021 — texte intégral lu** (libre accès, Europe PMC PMC8486643) : qSOFA déconseillé comme outil unique (forte, certitude modérée) ; lactate suggéré ; **≥ 30 mL/kg de cristalloïdes dans les 3 premières heures** (suggestion, certitude faible) ; antibiotiques **immédiatement, idéalement dans l'heure** si choc possible ou sepsis probable, **dans les 3 h** si sepsis possible sans choc, report si faible probabilité ; PCT non pour débuter, oui pour arrêter ; bithérapie anti-BGN si risque de BMR ; perfusion prolongée des bêta-lactamines ; contrôle de la source ; désescalade quotidienne ; cristalloïdes balancés, albumine, pas d'amidons ni de gélatines ; **PAM 65 mmHg** ; **noradrénaline en première intention**, vasopressine (en pratique à 0,25–0,5 µg/kg/min de noradrénaline), dobutamine ou adrénaline si dysfonction cardiaque, voie périphérique ; **hydrocortisone 200 mg/j (50 mg/6 h ou continu) à partir de 0,25 µg/kg/min de noradrénaline ou d'adrénaline au moins 4 h après le début** ; bicarbonate si pH ≤ 7,2 avec IRA ; insuline ≥ 180 mg/dL, cible 144–180 ; pas de vitamine C. **Conformes au dossier.**
- **Livre AWaRe 2022, chapitre 24** : tableau 24.1 (SOFA) et tableau 24.7 (options probabilistes, doses) — **conformes** ; méropénem 2 g/8 h dans le tableau du sepsis (1 g/8 h dans le chapitre des infections intra-abdominales hors sepsis).
- **Sepsis-3** (résumé PubMed, PMID 26903338) : mortalité > 10 % (sepsis) et > 40 % (choc septique). Seymour 2016 (PMID 26903335) vérifié.
- **SSC 2026 adulte** (PMID 41870560) et **SSC enfant 2026** (PMID 41869844 / 41870559) : existence et métadonnées vérifiées ; textes non accessibles (Springer bloqué) — positions 2026 laissées `[À VÉRIFIER]`, en cohérence avec DOS-MINT_REA-0001.
- QCM-INFE-0240 à 0252 : réponses exactes. CAS-INFE-0207 : exact (ΔSOFA ≥ 2 sur 5 organes, choc septique).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| CAS-INFE-0208 (lot) | Diagnostic de « sepsis (SOFA augmenté : plaquettes) » alors qu'avec 112 000 plaquettes, PAM 76, Glasgow 15 et créatinine 105 µmol/L, **ΔSOFA = 1** : critères de Sepsis-3 non réunis | **Majeure** | Plaquettes portées à 92 000/mm³ (ΔSOFA = 2) ; diagnostic reformulé (qSOFA 1) | S1, S4 (tableau 24.1) |
| CAS-INFE-0208 (lot) | Cloxacilline / céfazoline « à forte dose » sous `[POSOLOGIE ET DURÉE À VÉRIFIER]` | Mineure | Doses AWaRe ajoutées (cloxacilline ≥ 2 g/6 h IV, céfazoline 2 g/8 h IV, vancomycine 15–20 mg/kg/12 h) ; marqueur restreint à la dose maximale et à la durée | S4 |
| § 17 et CAS-INFE-0207 | Méropénem / C3G + métronidazole + amikacine sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | Méropénem 2 g/8 h ou C3G + métronidazole 500 mg/8 h + amikacine 15 mg/kg/24 h ; adaptation rénale après la première dose | S4 (tableau 24.7) |
| § 7.2 | Bornes du SOFA `[À VÉRIFIER]` | Mineure (levée) | Conformes au tableau 24.1 ; équivalences en µmol/L | S4 |
| § 9.1 | Formulation des hémocultures `[À VÉRIFIER]` | Mineure | Bonne pratique SSC 2016 rappelée en 2021 (« sans retard substantiel ») | S2 |
| § 12.2 | Mortalité `[À VÉRIFIER — chiffres exacts]` | Mineure (levée) | > 10 % et > 40 % (Sepsis-3) | S1 |
| § 7.3 | Force de la recommandation sur le qSOFA absente | Mineure | Forte, certitude modérée | S2 |
| § 21 et QCM-INFE-0242 (dossier et lot) | SSC 2026 : position sur le qSOFA dite « renforcée » alors qu'elle était déjà forte en 2021 | Mineure | « Maintenue » (forte, NEWS/MEWS/SIRS préférés), comme DOS-MINT_REA-0001 | DOS-MINT_REA-0001, S2 |
| § 13.2 b | Méropénem 2 g/8 h sans précision (point 4 du rédacteur) | Mineure | Dose du tableau du sepsis ; 1 g/8 h hors sepsis ; réservé aux contextes de BLSE fréquentes | S4 |
| § 10.2, § 21, YAML | SSC enfant 2026 seulement « signalée » ; S7 (2020) non signalée comme remplacée | Mineure | S10 ajoutée (métadonnées vérifiées) ; S7 « remplacée » | PubMed |
| § 13.2 b, § 13.4 | Protocole national non qualifié | Mineure | « Aucun protocole national algérien retrouvé » | Recherche (audit) |
| YAML, § 22 | S2 dite « non relue » ; S9 non vérifiée | Mineure | S2 lue (texte intégral) ; S9 vérifiée | Europe PMC, PubMed |
| QCM-INFE-0252 (lot) | Explication D sous `[À VÉRIFIER — durée]` | Mineure | Reformulée sans durée chiffrée (arrêt dès l'antibiogramme) | S4 |
| En-tête | Statut, version, bloc `audit` | Mineure | v1.1 | Protocole |

## Reste à faire
1. **Noradrénaline** : dose initiale et unité (base ou tartrate) selon le protocole local et le RCP algérien — marqueur conservé (dossier et DOS-MINT_REA-0001).
2. **CAS-INFE-0208** : dose maximale et durée de l'antistaphylococcique dans une bactériémie à *S. aureus* compliquée de thrombose du sinus caverneux ; place de l'anticoagulation (`[À VÉRIFIER]`) — cas en `audite_corrections_requises`.
3. **SSC 2026 adulte et enfant** : lire le texte intégral (dépistage, remplissage, corticoïdes, délais, bithérapie) et lever les `[À VÉRIFIER]` du § 21.
4. NICE NG51 (seuils NEWS2), définitions du SRIS (1991) : non relus.
5. Données algériennes (épidémiologie du sepsis, résistance : BLSE, carbapénémases, SARM) : **non retrouvées**.
