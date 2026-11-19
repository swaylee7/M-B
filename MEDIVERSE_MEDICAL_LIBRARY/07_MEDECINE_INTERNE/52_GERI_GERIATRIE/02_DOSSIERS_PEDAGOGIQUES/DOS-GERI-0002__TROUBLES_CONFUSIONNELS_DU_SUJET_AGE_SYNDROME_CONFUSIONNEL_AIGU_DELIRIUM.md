---
id: DOS-GERI-0002
titre: "Troubles confusionnels du sujet âgé : syndrome confusionnel aigu (delirium)"
specialite: GERI
sous_specialite: "Syndromes gériatriques — confusion aiguë"
items_residanat: [RES-MED-165]
niveaux: [etudiant, generaliste, resident, residanat, dems]
langue: fr
version: "1.2"
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent DOS-15 (IA) — dossier pédagogique original"
statut: audite_corrections_requises
audit:
  - date: 2026-11-19
    auditeur: "AUD-01 (IA)"
    verdict: audite_corrections_requises
    corrections: 11
    rapport: 00_SYSTEME/agents/AUD-01/rapports/DOS-GERI-0002.md
    remarque: "Textes relus : NICE CG103 (recommandations et contexte en ligne), HAS 2009 confusion aiguë (PDF), Beers 2023 (PMC), NICE CG100 (sevrage alcoolique). 4AT, CAM, critères NICE et HELP confirmés. Aucune erreur critique ou majeure."
  - date: 2026-11-19
    auditeur: "AUD-02 (IA)"
    verdict: audite_corrections_requises
    corrections: 3
    rapport: 00_SYSTEME/agents/AUD-01/rapports/DOS-GERI-0002.md
    remarque: "Thiamine levée (200 mg × 3/j IV avant tout glucide, EFNS 2010 ; voie parentérale au moins 5 jours si Gayet-Wernicke suspecté, NICE CG100). Restent 2 marqueurs : dose de l'halopéridol (NICE et HAS ne donnent pas de dose absolue ; RCP non consultable) et dose de la benzodiazépine du sevrage (lorazépam oral en 1re intention selon NICE CG100, dose non fixée)."
  - date: 2026-11-19
    auditeur: "AUD-04 (IA)"
    verdict: audite_corrections_requises
    corrections: 5
    rapport: 00_SYSTEME/agents/AUD-01/rapports/DOS-GERI-0002.md
    remarque: "S3-S5, S7-S9, S13, S14, S16 vérifiées par PubMed ; S17 (NICE CG100) et S18 (EFNS 2010) ajoutées. Non revérifiées : DSM-5-TR (S2), SIGN 157 (S12, hôte inaccessible) ; formulation exacte de PADIS sur la prévention médicamenteuse non relue."
  - date: 2026-11-19
    auditeur: "AUD-05 (IA)"
    verdict: audite_corrections_requises
    corrections: 1
    rapport: 00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md
    remarque: "Audit de cohérence (lot 6) : code CIM-11 du delirium (6D70, sous-codes 6D70.0 à 6D70.2) harmonisé — vérifié sur des sources secondaires concordantes (CISMeF, recherche du 2026-11-19), navigateur OMS non consulté ; marqueur contradictoire du § 21 levé. Restent ouverts les points des audits précédents."
sources:
  - id: S1
    reference: "National Institute for Health and Care Excellence. Delirium: prevention, diagnosis and management in hospital and long-term care. Clinical guideline CG103. Londres : NICE ; 2010, mise à jour janvier 2023."
    organisme: NICE
    annee: 2023
    type: recommandation
    doi: ""
    url: "https://www.nice.org.uk/guidance/cg103"
    verifiee: true
    remarque: "Recommandations et contexte relus en ligne par l'audit (nice.org.uk) : 4AT par défaut, CAM-ICU ou ICDSC en réanimation et salle de réveil (1.6.1, 2023) ; 4 facteurs de risque (1.2.1) ; intervention multicomposante dans les 24 h (1.4.2) ; halopéridol à court terme (habituellement ≤ 1 semaine), dose la plus faible, titration prudente, en tenant compte de l'avis de la MHRA sur les risques cardiaques et neurologiques (1.7.4, 2010) ; prévalence 20-30 % en médecine, 10-50 % en chirurgie, < 20 % en long séjour (contexte). CG103 ne traite pas des benzodiazépines."
  - id: S2
    reference: "American Psychiatric Association. Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR). Washington, DC: APA; 2022."
    organisme: APA
    annee: 2022
    type: ouvrage
    doi: ""
    url: ""
    verifiee: false
    remarque: "Critères du delirium reformulés, non recopiés ; référence non revérifiée pendant la session."
  - id: S3
    reference: "Inouye SK, van Dyck CH, Alessi CA, Balkin S, Siegal AP, Horwitz RI. Clarifying confusion: the confusion assessment method. A new method for detection of delirium. Ann Intern Med. 1990;113(12):941-948."
    organisme: "Annals of Internal Medicine"
    annee: 1990
    type: article
    doi: "10.7326/0003-4819-113-12-941"
    url: "https://pubmed.ncbi.nlm.nih.gov/2240918/"
    verifiee: true
    remarque: "Algorithme (critères 1 + 2 + 3 ou 4), sensibilité 94-100 %, spécificité 90-95 %, kappa 0,81-1,0 confirmés par recherche web."
  - id: S4
    reference: "Tieges Z, Maclullich AMJ, Anand A, et al. Diagnostic accuracy of the 4AT for delirium detection in older adults: systematic review and meta-analysis. Age Ageing. 2021;50(3):733-743."
    organisme: "Age and Ageing"
    annee: 2021
    type: article
    doi: "10.1093/ageing/afaa224"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC8099016"
    verifiee: true
    remarque: "17 études, 3 702 observations ; sensibilité et spécificité poolées 0,88 / 0,88."
  - id: S5
    reference: "Bellelli G, Morandi A, Davis DHJ, et al. Validation of the 4AT, a new instrument for rapid delirium screening: a study in 234 hospitalised older people. Age Ageing. 2014;43(4):496-502."
    organisme: "Age and Ageing"
    annee: 2014
    type: article
    doi: "10.1093/ageing/afu021"
    url: ""
    verifiee: true
    remarque: "PMID 24590568."
  - id: S6
    reference: "Haute Autorité de santé. Confusion aiguë chez la personne âgée : prise en charge initiale de l'agitation. Recommandations de bonne pratique. Mai 2009."
    organisme: HAS
    annee: 2009
    type: recommandation
    doi: ""
    url: "https://www.has-sante.fr/jcms/c_819557/"
    verifiee: true
    remarque: "Texte des recommandations relu par l'audit (PDF has-sante.fr) : urgence médicale ; bilan initial systématique ; TDM non systématique, en 1re intention si signe de localisation, suspicion d'hémorragie méningée ou traumatisme crânien même mineur, en 2e intention si bilan négatif ; traitement médicamenteux de 24 à 48 h au maximum, en monothérapie, à 1/4-1/2 de la dose adulte ; benzodiazépine orale d'action courte (alprazolam, lorazépam, oxazépam) si anxiété prédominante, neuroleptique si troubles productifs ; CAM décrite, mais version française non validée ; confusion postopératoire hors champ."
  - id: S7
    reference: "Inouye SK, Westendorp RGJ, Saczynski JS. Delirium in elderly people. Lancet. 2014;383(9920):911-922."
    organisme: Lancet
    annee: 2014
    type: article
    doi: "10.1016/S0140-6736(13)60688-1"
    url: ""
    verifiee: true
    remarque: "PMID 23992774."
  - id: S8
    reference: "Inouye SK, Bogardus ST Jr, Charpentier PA, et al. A multicomponent intervention to prevent delirium in hospitalized older patients. N Engl J Med. 1999;340(9):669-676."
    organisme: NEJM
    annee: 1999
    type: article
    doi: "10.1056/NEJM199903043400901"
    url: ""
    verifiee: true
    remarque: "Essai HELP ; PMID 10053175 ; résumé relu : confusion chez 9,9 % (intervention) contre 15,0 % (soins usuels), OR apparié 0,60."
  - id: S9
    reference: "Inouye SK, Charpentier PA. Precipitating factors for delirium in hospitalized elderly persons: predictive model and interrelationship with baseline vulnerability. JAMA. 1996;275(11):852-857."
    organisme: JAMA
    annee: 1996
    type: article
    doi: ""
    url: ""
    verifiee: true
    remarque: "PMID 8596223."
  - id: S10
    reference: "2023 American Geriatrics Society Beers Criteria® Update Expert Panel. American Geriatrics Society 2023 updated AGS Beers Criteria® for potentially inappropriate medication use in older adults. J Am Geriatr Soc. 2023;71(7):2052-2081."
    organisme: "American Geriatrics Society"
    annee: 2023
    type: recommandation
    doi: "10.1111/jgs.18372"
    url: "https://pubmed.ncbi.nlm.nih.gov/37139824/"
    verifiee: true
  - id: S11
    reference: "O'Mahony D, Cherubini A, Guiteras AR, et al. STOPP/START criteria for potentially inappropriate prescribing in older people: version 3. Eur Geriatr Med. 2023;14(4):625-632."
    organisme: "European Geriatric Medicine Society"
    annee: 2023
    type: recommandation
    doi: "10.1007/s41999-023-00777-y"
    url: "https://pubmed.ncbi.nlm.nih.gov/37256475/"
    verifiee: true
  - id: S12
    reference: "Scottish Intercollegiate Guidelines Network. Risk reduction and management of delirium (SIGN 157). Edinburgh: SIGN; 2019."
    organisme: SIGN
    annee: 2019
    type: recommandation
    doi: ""
    url: ""
    verifiee: false
  - id: S13
    reference: "Ely EW, Inouye SK, Bernard GR, et al. Delirium in mechanically ventilated patients: validity and reliability of the confusion assessment method for the intensive care unit (CAM-ICU). JAMA. 2001;286(21):2703-2710."
    organisme: JAMA
    annee: 2001
    type: article
    doi: "10.1001/jama.286.21.2703"
    url: ""
    verifiee: true
    remarque: "PMID 11730446."
  - id: S14
    reference: "Wilson JE, Mart MF, Cunningham C, et al. Delirium. Nat Rev Dis Primers. 2020;6(1):90."
    organisme: "Nature Reviews Disease Primers"
    annee: 2020
    type: article
    doi: "10.1038/s41572-020-00223-4"
    url: ""
    verifiee: true
    remarque: "PMID 33184265."
  - id: S15
    reference: "Loi n° 18-11 du 2 juillet 2018 relative à la santé (art. 21, 23, 86-87, 198, 343). JORADP n° 46 du 29 juillet 2018."
    organisme: "République algérienne (JORADP)"
    annee: 2018
    type: texte_officiel
    doi: ""
    url: "https://www.joradp.dz/FTP/JO-FRANCAIS/2018/F2018046.pdf"
    verifiee: true
    remarque: "DOC-00074, lu."
  - id: S16
    reference: "Devlin JW, Skrobik Y, Gélinas C, et al. Clinical practice guidelines for the prevention and management of pain, agitation/sedation, delirium, immobility, and sleep disruption in adult patients in the ICU (PADIS). Crit Care Med. 2018;46(9):e825-e873."
    organisme: "Society of Critical Care Medicine"
    annee: 2018
    type: recommandation
    doi: "10.1097/CCM.0000000000003299"
    url: ""
    verifiee: true
    remarque: "PMID 30113379 (existence vérifiée) ; formulation de la recommandation sur la prévention médicamenteuse non relue (texte intégral non accessible)."
  - id: S17
    reference: "National Institute for Health and Care Excellence. Alcohol-use disorders: diagnosis and management of physical complications. Clinical guideline CG100. Londres : NICE ; 2010 (mises à jour 2017)."
    organisme: NICE
    annee: 2010
    type: recommandation
    doi: ""
    url: "https://www.nice.org.uk/guidance/cg100"
    verifiee: true
    remarque: "Relu en ligne par l'audit : delirium tremens, lorazépam oral en 1re intention, lorazépam parentéral ou halopéridol si persistance ou refus de la voie orale (1.1.4.1, hors AMM au Royaume-Uni en 2017) ; thiamine parentérale au moins 5 jours en cas de Gayet-Wernicke suspecté, puis orale (1.2.1.4)."
  - id: S18
    reference: "Galvin R, Bråthen G, Ivashynka A, Hillbom M, Tanasescu R, Leone MA; EFNS. EFNS guidelines for diagnosis, therapy and prevention of Wernicke encephalopathy. Eur J Neurol. 2010;17(12):1408-1418."
    organisme: EFNS
    annee: 2010
    type: recommandation
    doi: "10.1111/j.1468-1331.2010.03153.x"
    url: ""
    verifiee: true
    remarque: "PMID 20642790 ; résumé relu : thiamine 200 mg trois fois par jour, de préférence IV, avant tout apport glucidique (niveau C)."
mots_cles: [confusion aiguë, syndrome confusionnel, delirium, sujet âgé, inattention, CAM, 4AT, DSM-5-TR, delirium hypoactif, iatrogénie, anticholinergiques, benzodiazépines, rétention urinaire, fécalome, prévention multicomposante, HELP, halopéridol, NICE CG103, HAS 2009]
---

# Troubles confusionnels du sujet âgé : syndrome confusionnel aigu (delirium)

> **Dossier pédagogique original Mediverse** — rédigé à partir de plusieurs sources citées ; ne reproduit aucun ouvrage, ni les critères diagnostiques ou les échelles dans leur formulation protégée (ils sont reformulés).
> Statut : **audité par l'IA (AUD-01/AUD-02/AUD-04, 2026-11-19), corrections requises** — relecture par un enseignant qualifié nécessaire. **Posologies** : la dose de thiamine est sourcée (EFNS 2010) ; les doses d'antipsychotique et de benzodiazépine restent à confronter au RCP et au protocole local (marqueurs maintenus).

**Item du programme couvert** : RES-MED-165 — « Troubles confusionnels chez le sujet âgé » (module Personnes âgées, DOC-00001).

**Objectifs pédagogiques** — le lecteur doit être capable de :
1. **Définir** le syndrome confusionnel aigu (delirium) selon les critères du DSM-5-TR et le **distinguer** de la démence, de la dépression et des troubles psychotiques.
2. **Expliquer** le modèle vulnérabilité × facteurs précipitants et les principales hypothèses physiopathologiques.
3. **Repérer** une confusion, y compris dans sa forme **hypoactive**, à l'aide du **4AT** et de la **CAM**, et **tester l'attention** au lit du patient.
4. **Conduire** un bilan étiologique hiérarchisé (« toute confusion a une cause organique jusqu'à preuve du contraire »), en commençant par la **iatrogénie**, la **rétention urinaire**, le **fécalome**, la **douleur**, la **déshydratation** et les **infections**.
5. **Prendre en charge** une confusion : traitement de la cause, mesures non médicamenteuses, place limitée et encadrée des psychotropes, éviter la contention.
6. **Prévenir** la confusion chez les patients à risque (intervention multicomposante).
7. **Connaître** le pronostic, le suivi après l'épisode et les divergences entre recommandations (NICE 2023, HAS 2009, réanimation).

---

## 1. Définitions et terminologie

### 1.1 Syndrome confusionnel aigu = delirium

Le **syndrome confusionnel aigu** (ou **confusion aiguë**, ou **état confusionnel**) correspond au *delirium* des classifications internationales. C'est une **défaillance cérébrale aiguë**, d'installation rapide et d'évolution fluctuante, caractérisée par une **perturbation de l'attention et de la conscience**, accompagnée d'autres troubles cognitifs, et due à une **cause organique** (affection médicale, médicament, intoxication ou sevrage) [S2, S7].

> **Attention à la terminologie** : en français, le « délire » désigne une idée délirante (trouble du contenu de la pensée, psychiatrique), alors que le *delirium* (anglais, latin) désigne la confusion aiguë. Ne pas confondre « delirium » et « délire ».

### 1.2 Critères diagnostiques (DSM-5-TR, reformulés) [S2]

| Critère | Contenu (reformulé) |
|---|---|
| A | Trouble de l'**attention** (capacité réduite à orienter, focaliser, maintenir et déplacer l'attention) et de la **conscience** (orientation réduite vis-à-vis de l'environnement) |
| B | Installation **rapide** (quelques heures à quelques jours), rupture avec l'état antérieur, **fluctuation** de l'intensité au cours de la journée |
| C | Au moins un autre **trouble cognitif** (mémoire, désorientation, langage, capacités visuo-spatiales, perception) |
| D | Les troubles A et C ne s'expliquent pas mieux par un trouble neurocognitif préexistant et ne surviennent pas dans un contexte de vigilance très abaissée (coma) |
| E | Arguments (anamnèse, examen, examens complémentaires) indiquant qu'ils sont la **conséquence physiologique directe** d'une affection médicale, d'une intoxication ou d'un sevrage, d'une exposition toxique, ou de causes multiples |

Spécifications : **aigu** (heures à jours) ou **persistant** (semaines à mois) ; selon l'activité psychomotrice : **hyperactif**, **hypoactif**, **mixte**. La CIM-11 classe le delirium parmi les troubles neurocognitifs (code 6D70, avec des sous-codes selon la cause : 6D70.0 affection classée ailleurs, 6D70.1 substance ou médicament, 6D70.2 causes multiples) ; code vérifié sur des sources secondaires concordantes (portail CISMeF ; vérification renouvelée par AUD-05 le 2026-11-19), le navigateur CIM-11 de l'OMS étant inaccessible pendant l'audit.

### 1.3 Notions associées

- **Confusion subsyndromique** : présence de certains symptômes sans tous les critères ; même signification pronostique, à un degré moindre.
- **Confusion superposée à une démence** : situation fréquente et difficile, car la démence est le principal facteur de vulnérabilité et brouille l'évaluation de l'état de base.
- **Confusion persistante** : symptômes persistant au-delà de plusieurs semaines ; elle doit faire rechercher une cause non résolue et/ou une démence sous-jacente.

La confusion est une **urgence médicale** : elle est le mode d'expression non spécifique, chez le sujet âgé, de nombreuses affections aiguës potentiellement graves [S6].

---

## 2. Historique (repères)

- Hippocrate décrivait déjà des états d'agitation fébrile (*phrenitis*) et de léthargie (*lethargus*), préfigurant les formes hyperactive et hypoactive.
- 1990 : la **Confusion Assessment Method (CAM)** propose un algorithme simple utilisable par des non-psychiatres [S3].
- 1996 : modèle prédictif **vulnérabilité × facteurs précipitants** [S9] ; 1999 : essai **HELP** démontrant l'efficacité d'une prévention multicomposante non médicamenteuse [S8].
- 2001 : **CAM-ICU** pour les patients de réanimation, y compris ventilés [S13].
- 2009 : recommandation HAS sur la prise en charge initiale de l'agitation dans la confusion aiguë [S6].
- 2010 : NICE CG103 ; **mise à jour 2023** qui fait du **4AT** l'outil de repérage par défaut [S1] ; 2014 : validation du 4AT [S5] ; 2021 : méta-analyse de sa précision diagnostique [S4].
- 2022 : DSM-5-TR [S2].

---

## 3. Épidémiologie

- Fréquence élevée et **sous-diagnostic** majeur, en particulier de la forme hypoactive. Les ordres de grandeur couramment rapportés sont d'environ **20 à 30 %** des patients hospitalisés en services de médecine, **10 à 50 %** des patients opérés selon le type de chirurgie, et moins de 20 % des résidents d'établissements de long séjour (contexte de la recommandation NICE, relu) [S1]. Les fréquences sont plus élevées encore en **réanimation**, notamment chez les patients ventilés [S13, S16], et en **soins palliatifs** de fin de vie [S7].
- Situations à très haut risque : **fracture de l'extrémité supérieure du fémur**, chirurgie cardiaque, AVC, sepsis, démence préexistante.
- En Algérie, aucune donnée épidémiologique nationale sourcée sur la confusion du sujet âgé n'a été identifiée `[À VÉRIFIER]` ; le vieillissement de la population (espérance de vie de 79,6 ans en 2023 selon l'ONS, voir DOS-GERI-0001) laisse prévoir une augmentation du nombre de patients à risque.

---

## 4. Rappels physiologiques : attention et conscience

L'**éveil** (vigilance) dépend du système réticulé activateur ascendant (tronc cérébral, thalamus) ; l'**attention** sélective et soutenue mobilise des réseaux fronto-pariétaux et thalamo-corticaux, modulés par de nombreux neurotransmetteurs (**acétylcholine**, dopamine, noradrénaline, sérotonine, GABA, glutamate). Le cerveau âgé dispose d'une **réserve** cognitive et neuronale diminuée (perte neuronale et synaptique, pathologie neurodégénérative infraclinique, lésions vasculaires), ce qui explique qu'une agression modeste (infection urinaire, médicament anticholinergique, déshydratation) suffise à provoquer une défaillance cérébrale aiguë.

---

## 5. Physiopathologie

### 5.1 Modèle multifactoriel : vulnérabilité × facteurs précipitants [S9]

```text
VULNÉRABILITÉ (terrain)                       FACTEURS PRÉCIPITANTS (agression)
grand âge, démence/troubles cognitifs,   ×    médicaments, infection, chirurgie,
déficits sensoriels, dénutrition,             déshydratation, troubles métaboliques,
polypathologie, dépendance, alcool,           douleur, rétention urinaire, fécalome,
antécédent de confusion                       contention, sonde, privation de sommeil
        │                                                   │
        └───────────────► DÉFAILLANCE CÉRÉBRALE AIGUË ◄─────┘
```

Un sujet très vulnérable (démence évoluée) peut devenir confus pour une cause minime (constipation, changement de chambre) ; un sujet robuste ne le devient que lors d'une agression majeure (sepsis grave, chirurgie lourde). Les causes sont souvent **multiples** et **cumulatives** : la recherche ne doit pas s'arrêter à la première cause trouvée.

### 5.2 Mécanismes (hypothèses non exclusives) [S7, S14]

- **Déficit cholinergique** et excès relatif de **dopamine** : explique la toxicité des médicaments **anticholinergiques** et l'effet confusiogène des agonistes dopaminergiques.
- **Neuro-inflammation** : les cytokines produites lors d'une infection ou d'une chirurgie activent la microglie, surtout sur un cerveau « amorcé » par une neurodégénérescence.
- **Réponse au stress** : hypercortisolémie, activation sympathique.
- **Troubles métaboliques et énergétiques** : hypoxie, hypoglycémie, troubles hydro-électrolytiques, insuffisance d'organe (urémie, encéphalopathie hépatique, hypercapnie).
- **Désorganisation des réseaux** cérébraux (perte de connectivité fonctionnelle) et perturbation du **rythme veille-sommeil** (mélatonine).

### 5.3 Liens avec la démence

La démence est le principal facteur de risque de confusion ; inversement, un épisode confusionnel est associé à un **déclin cognitif accéléré** et peut révéler une démence jusque-là méconnue [S7]. D'où l'intérêt d'une **réévaluation cognitive à distance** de l'épisode.

---

## 6. Facteurs de risque et causes

### 6.1 Facteurs de vulnérabilité (prédisposants)

Les recommandations NICE retiennent quatre facteurs de risque principaux justifiant une vigilance particulière dès l'admission : **âge ≥ 65 ans**, **troubles cognitifs** passés ou actuels et/ou démence, **fracture actuelle de l'extrémité supérieure du fémur**, **affection sévère** (état clinique qui se dégrade ou risque de se dégrader) [S1]. S'y ajoutent : déficits visuels et auditifs, dépendance fonctionnelle, dénutrition, déshydratation, polymédication, consommation d'alcool, dépression, antécédent de confusion, AVC, maladie de Parkinson.

### 6.2 Facteurs précipitants et causes : la grille à parcourir systématiquement

| Catégorie | Causes fréquentes chez le sujet âgé |
|---|---|
| **Médicaments** (à évoquer **en premier**) | **Anticholinergiques** (antispasmodiques urinaires, antihistaminiques de 1re génération, antidépresseurs tricycliques, certains antiparkinsoniens et neuroleptiques), **benzodiazépines** et hypnotiques, **opioïdes** (tramadol inclus), corticoïdes, antiépileptiques, antiparkinsoniens dopaminergiques, digoxine (surdosage), lithium, fluoroquinolones, antihistaminiques H2 ; **sevrage** en benzodiazépines ou en alcool ; introduction, augmentation ou arrêt récent d'un traitement [S1, S6, S10, S11] |
| **Infections** | Pneumopathie, infection urinaire (attention : bactériurie asymptomatique fréquente, ne pas conclure trop vite), infection cutanée, intra-abdominale, sepsis, méningite et encéphalite (plus rares) |
| **Métaboliques** | Déshydratation, hyponatrémie, hypernatrémie, hypercalcémie, hypoglycémie, hyperglycémie, insuffisance rénale, encéphalopathie hépatique, hypothyroïdie ou hyperthyroïdie, carence en thiamine (encéphalopathie de Gayet-Wernicke) |
| **Respiratoires / circulatoires** | Hypoxémie, **hypercapnie**, insuffisance cardiaque, infarctus du myocarde (parfois indolore), troubles du rythme, état de choc, anémie sévère |
| **Neurologiques** | AVC (notamment thalamique, pariétal droit), **hématome sous-dural** (chute, anticoagulant), état de mal épileptique **non convulsif**, état post-critique, tumeur, méningo-encéphalite |
| **« Mécaniques » et douleur** | **Rétention aiguë d'urine** (globe vésical), **fécalome**, **douleur** non traitée (fracture, rétention, ischémie), sondes et cathéters |
| **Environnement** | Hospitalisation, changements de chambre, privation sensorielle (lunettes et appareils auditifs absents), privation de sommeil, **contention physique**, isolement, environnement bruyant |
| **Chirurgie et anesthésie** | Confusion postopératoire (fracture du col, chirurgie cardiaque), douleur, hypoxie, anémie |
| **Toxiques / sevrage** | Alcool (sevrage : *delirium tremens*), intoxications |

L'étude princeps des facteurs précipitants à l'hôpital a mis en avant, chez le sujet âgé hospitalisé, la **contention physique**, la **dénutrition**, l'**ajout de plus de trois médicaments**, la **sonde urinaire** et tout **événement iatrogène** [S9].

---

## 7. Diagnostic positif

### 7.1 Clinique

| Domaine | Manifestations |
|---|---|
| **Début** | Brutal ou rapidement progressif (heures, jours) ; changement par rapport à l'état antérieur rapporté par l'entourage |
| **Fluctuations** | Intervalles de lucidité, aggravation vespérale et nocturne |
| **Attention** (signe central) | Distractibilité, incapacité à suivre une conversation, à maintenir le regard, persévérations |
| **Vigilance** | Hypervigilance (agitation) ou somnolence, obnubilation |
| **Désorganisation de la pensée** | Discours incohérent, coq-à-l'âne, réponses à côté |
| **Désorientation** | Temporelle surtout, puis spatiale |
| **Mémoire** | Troubles de la fixation, amnésie de l'épisode |
| **Perceptions** | Illusions, **hallucinations visuelles** (zoopsies), interprétations délirantes souvent à thème de persécution, peu structurées |
| **Psychomotricité** | Agitation, déambulation, gestes d'arrachement (perfusion, sonde) **ou** ralentissement, apathie, mutisme (forme hypoactive) |
| **Veille-sommeil** | Inversion du rythme (somnolence diurne, agitation nocturne) |
| **Émotions** | Anxiété, peur, irritabilité, labilité |
| **Signes associés** | Ceux de la cause (fièvre, déshydratation, globe vésical, signes de localisation) ; tremblement, astérixis (encéphalopathies métaboliques) |

### 7.2 Formes selon l'activité psychomotrice

- **Hyperactive** : agitation, hallucinations, agressivité ; la plus visible, la moins fréquente chez le sujet âgé.
- **Hypoactive** : somnolence, apathie, ralentissement, retrait ; la plus fréquente chez le sujet âgé, **la plus méconnue** (prise pour une dépression ou de la « fatigue ») et de **pronostic plus sombre** [S7].
- **Mixte** : alternance des deux.

### 7.3 Tester l'attention au lit du malade

- Réciter les **mois de l'année à l'envers** (de décembre à janvier) ; les jours de la semaine à l'envers ; épeler un mot à l'envers.
- **Empan** de chiffres (répéter une série de chiffres) ; test de la lettre (serrer la main à chaque fois qu'une lettre donnée est prononcée dans une série).

### 7.4 Outils de repérage et de diagnostic

**4AT** — outil court (< 2 minutes), sans formation spécifique, utilisable même chez un patient non testable ; recommandé par défaut par le NICE depuis 2023 [S1, S4, S5] :

| Item | Cotation (résumé) |
|---|---|
| 1. **Vigilance** | Normale (y compris brièvement somnolent puis normal au réveil) = 0 ; clairement anormale = 4 |
| 2. **AMT4** (âge, date de naissance, lieu, année en cours) | Aucune erreur = 0 ; 1 erreur = 1 ; ≥ 2 erreurs ou non testable = 2 |
| 3. **Attention** : mois de l'année à l'envers | ≥ 7 mois correctement = 0 ; débute mais < 7 mois, ou refuse = 1 ; non testable (trop somnolent, inattentif) = 2 |
| 4. **Changement aigu ou évolution fluctuante** (vigilance, cognition, autre fonction mentale) dans les 2 dernières semaines, encore présent dans les 24 dernières heures | Non = 0 ; oui = 4 |

Interprétation : **≥ 4** = confusion possible (± troubles cognitifs) ; **1 à 3** = troubles cognitifs possibles ; **0** = confusion ou troubles cognitifs sévères peu probables (sauf si l'item 4 n'a pu être renseigné). Méta-analyse : sensibilité et spécificité poolées d'environ **0,88** [S4].

**CAM (Confusion Assessment Method)** — algorithme diagnostique à 4 critères [S3] :
1. Début **aigu** et évolution **fluctuante** ;
2. **Inattention** ;
3. **Pensée désorganisée** ;
4. **Altération du niveau de conscience**.
→ Diagnostic de confusion si **1 et 2** sont présents, **et** **3 ou 4**. Dans l'étude princeps, sensibilité de 94 à 100 % et spécificité de 90 à 95 % par rapport au diagnostic psychiatrique, chez des évaluateurs formés [S3].

**Réanimation et salle de réveil** : **CAM-ICU** ou **ICDSC** (patients non communicants, ventilés) [S1, S13, S16] ; la sédation est évaluée par l'échelle **RASS**.

> Le repérage **systématique** (à l'admission puis quotidien chez les patients à risque) est nécessaire, car la confusion — surtout hypoactive — passe inaperçue chez une grande partie des patients si on ne la cherche pas [S1, S7].

---

## 8. Examens complémentaires et bilan étiologique

### 8.1 Principe

**Toute confusion est organique jusqu'à preuve du contraire.** Le bilan est **guidé par la clinique**, mais comporte un socle systématique. Il commence par une **revue exhaustive des médicaments** et par un **examen clinique complet** (vessie, rectum, peau, poumons, abdomen, signes neurologiques, douleur) [S1, S6].

### 8.2 Bilan initial (socle)

| Examen | Ce que l'on recherche |
|---|---|
| Revue des **médicaments** (ordonnance, automédication, changements récents) | Iatrogénie, sevrage |
| **Glycémie capillaire** | Hypoglycémie (immédiatement) |
| Température, SpO₂, PA, FC, FR, diurèse ; **recherche de globe vésical** (palpation, échographie vésicale) ; **toucher rectal** si suspicion de fécalome | Infection, hypoxie, état de choc, rétention, fécalome |
| NFS, CRP | Infection, anémie |
| **Ionogramme sanguin** (Na, K), **calcémie** (corrigée), urée, **créatinine** | Hyponatrémie, hypercalcémie, déshydratation, insuffisance rénale |
| Bilan hépatique | Encéphalopathie, cholestase infectieuse |
| **ECG** | Ischémie, troubles du rythme ou de la conduction, intoxication (digoxine) |
| Bandelette urinaire (± ECBU si signes urinaires ou fièvre sans autre cause) | Infection urinaire — **ne pas traiter une bactériurie asymptomatique** comme cause unique sans argument |

### 8.3 Examens orientés

| Examen | Indication |
|---|---|
| Gaz du sang | Hypoxémie, **hypercapnie** (BPCO, sédatifs), acidose |
| Hémocultures, radiographie thoracique | Fièvre, signes respiratoires |
| Troponine | Suspicion de syndrome coronarien (souvent atypique) |
| Dosages médicamenteux | Digoxine, lithium, antiépileptiques |
| TSH, vitamine B12, folates, ammoniémie | Selon le contexte |
| **Scanner cérébral** | **Pas systématique**. HAS 2009 : en 1re intention en cas de **signe de localisation**, de **suspicion d'hémorragie méningée** ou de **traumatisme crânien même mineur** (chute, surtout sous anticoagulant ou antiagrégant) ; en 2e intention si le bilan initial est négatif (AVC sans déficit moteur, hématome sous-dural) [S6]. Des troubles de la vigilance inexpliqués justifient aussi l'imagerie (avis d'expert) |
| **Ponction lombaire** | Fièvre sans point d'appel, syndrome méningé, suspicion de méningo-encéphalite (après imagerie si indiquée) |
| **EEG** | Suspicion d'**état de mal non convulsif** (fluctuations, myoclonies discrètes, antécédent d'épilepsie) ; ralentissement diffus non spécifique dans la plupart des confusions |

---

## 9. Formes cliniques particulières

- **Confusion postopératoire** : fréquente après fracture du col du fémur et chirurgie cardiaque ; facteurs : douleur, anémie, hypoxie, opioïdes, anticholinergiques, sonde, privation de sommeil ; prévention par une prise en charge **orthogériatrique** (exclue du champ de la recommandation HAS 2009) [S6].
- **Confusion superposée à une démence** : changement **par rapport à l'état habituel** décrit par l'aidant (le 4AT intègre cet item) ; ne pas attribuer l'aggravation à « l'évolution de la démence » sans bilan.
- **Delirium tremens** (sevrage alcoolique, 48-72 h après l'arrêt) : confusion, agitation, hallucinations, tremblements, sueurs, fièvre, tachycardie ; urgence ; traitement par **benzodiazépine** (NICE CG100 : lorazépam oral en 1re intention ; lorazépam parentéral ou halopéridol si persistance ou refus de la voie orale) [S17], dose titrée selon les symptômes `[POSOLOGIE À VÉRIFIER — RCP / protocole local]`, et **thiamine** avant tout apport glucosé ; c'est la principale situation où les benzodiazépines sont le traitement de choix [S10, S17].
- **Encéphalopathie de Gayet-Wernicke** : confusion, troubles oculomoteurs, ataxie (triade souvent incomplète) chez un patient dénutri ou alcoolique ; **thiamine 200 mg trois fois par jour, de préférence IV, avant tout apport glucidique** (EFNS 2010) [S18], par voie parentérale pendant au moins 5 jours, puis relais oral (NICE CG100) [S17].
- **Syndrome anticholinergique** : confusion, mydriase, sécheresse cutanéo-muqueuse, tachycardie, rétention urinaire, constipation, hyperthermie.
- **Syndrome sérotoninergique** (association d'antidépresseurs, tramadol, linézolide…) et **syndrome malin des neuroleptiques** (rigidité, hyperthermie, CPK élevées) : urgences.
- **État de mal épileptique non convulsif** : confusion fluctuante inexpliquée, parfois myoclonies discrètes ; diagnostic par EEG.
- **Confusion en réanimation** : très fréquente, souvent hypoactive, associée à la sédation ; dépistage par CAM-ICU ou ICDSC [S13, S16].
- **Confusion en fin de vie** : fréquente ; objectifs centrés sur le confort ; recherche des causes réversibles proportionnée à la situation.
- **Confusion et maladie de Parkinson / démence à corps de Lewy** : grande sensibilité aux neuroleptiques (risque d'aggravation sévère) ; avis spécialisé avant tout antipsychotique [S1].

---

## 10. Diagnostics différentiels

| Caractéristique | **Confusion (delirium)** | **Démence** | **Dépression** | **Psychose aiguë / manie** |
|---|---|---|---|---|
| Début | Brutal (heures, jours) | Insidieux (mois, années) | Subaigu (semaines) | Variable, souvent brutal |
| Évolution | **Fluctuante**, aggravation nocturne | Lentement progressive, relativement stable sur 24 h | Variation matinale possible | Variable |
| **Attention** | **Très altérée** | Préservée aux stades débutants | Peu altérée (effort réduit) | Souvent préservée |
| Vigilance | Altérée (hyper ou hypo) | Normale (sauf stade évolué) | Normale | Normale ou augmentée |
| Pensée | Désorganisée | Appauvrie | Ralentie, idées négatives | Délire structuré, logorrhée |
| Hallucinations | Fréquentes, **visuelles** | Rares (sauf démence à corps de Lewy) | Rares | Fréquentes, **auditives** |
| Cause organique | **Oui (recherche impérative)** | Neurodégénérative/vasculaire | Non (en général) | Non (sauf psychose secondaire) |
| Réversibilité | Souvent, avec traitement de la cause | Non | Oui, avec traitement | Oui |

Autres diagnostics à évoquer : **aphasie de Wernicke** (discours fluent incohérent, mais vigilance normale et pas d'inattention globale : AVC), **ictus amnésique** (amnésie antérograde isolée, durée < 24 h, sans autre trouble), **démence à corps de Lewy** (fluctuations cognitives, hallucinations visuelles, parkinsonisme : peut mimer une confusion persistante), troubles du comportement de la démence sans cause aiguë, surdité ou troubles visuels sévères (pseudo-confusion).

> Règle pratique : **devant une modification aiguë du comportement ou de la cognition d'une personne âgée, penser d'abord confusion (et rechercher sa cause), avant de conclure à une démence ou à un trouble psychiatrique.**

---

## 11. Évolution, complications et pronostic

- Durée habituelle de quelques jours à quelques semaines si la cause est traitée ; une **récupération incomplète** et des formes **persistantes** sont fréquentes chez les sujets les plus vulnérables [S7].
- **Complications de l'épisode** : chutes et fractures, déshydratation et dénutrition, escarres, pneumopathie d'inhalation, arrachement de dispositifs, iatrogénie (psychotropes), contention et ses complications, allongement de l'hospitalisation.
- **Pronostic à moyen et long terme** : la confusion est associée à une **surmortalité**, à un **déclin fonctionnel**, à un risque accru d'**institutionnalisation** et de **déclin cognitif durable** ou de démence [S7, S14]. Elle constitue un **marqueur de vulnérabilité** cérébrale.
- La forme **hypoactive** est associée à un pronostic plus défavorable (diagnostic tardif, gravité des causes).
- Retentissement sur les **aidants** et le personnel (détresse, souvenirs pénibles de l'épisode chez le patient lui-même).

---

## 12. Prise en charge

### 12.1 Objectifs

1. **Identifier et traiter** la (les) cause(s).
2. **Assurer la sécurité** du patient et de l'entourage, sans recourir à la contention.
3. **Réduire la souffrance** (anxiété, hallucinations) et prévenir les complications.
4. **Préserver l'autonomie** et préparer le suivi.

### 12.2 Lieu de prise en charge

La confusion est une urgence : l'**hospitalisation** est habituellement nécessaire pour le bilan étiologique, sauf cause évidente et rapidement réversible (ex. médicament identifié et arrêté) avec un entourage capable d'assurer la surveillance et un suivi médical rapproché à domicile. Les soins et l'hospitalisation à domicile prévus par la loi pour les personnes âgées (art. 87 de la loi 18-11) peuvent être une option selon les ressources locales [S15].

### 12.3 Traitement étiologique (priorité)

- **Arrêter ou réduire** les médicaments suspects (anticholinergiques, sédatifs, opioïdes mal adaptés…) ; **ne pas sevrer brutalement** une benzodiazépine prise au long cours (risque de sevrage confusiogène) : diminution progressive.
- Traiter l'infection, corriger l'hydratation et les troubles hydro-électrolytiques (correction **prudente** d'une hyponatrémie chronique), l'hypoxie, l'hypoglycémie.
- **Sonder** une rétention aiguë d'urine (puis retirer la sonde dès que possible), évacuer un **fécalome**, traiter la constipation.
- **Traiter la douleur** (paracétamol en première intention, réévaluation régulière ; la douleur non traitée est confusiogène, mais les opioïdes doivent être titrés prudemment).
- Thiamine en cas de suspicion de carence ; prise en charge spécifique des causes neurologiques, cardiaques, métaboliques.

### 12.4 Mesures non médicamenteuses (pour tous les patients) [S1, S6, S8]

| Domaine | Mesures |
|---|---|
| Communication | Parler calmement, phrases simples, se présenter, expliquer les soins, éviter la confrontation (ne pas contredire de front les idées délirantes) |
| Orientation | Horloge, calendrier, lumière du jour, rappels réguliers de la date, du lieu et de la raison de l'hospitalisation |
| Présence | Favoriser la **présence de proches**, mêmes soignants autant que possible ; éviter les changements de chambre |
| Sensoriel | Remettre **lunettes** et **appareils auditifs** |
| Sommeil | Respect du sommeil nocturne (regrouper les soins, réduire bruit et lumière la nuit), activité le jour |
| Mobilisation | Lever précoce, marche accompagnée, éviter l'alitement |
| Hydratation / nutrition | Aide aux repas et à la boisson, dentiers en place |
| Élimination | Surveillance de la diurèse et du transit, éviter la sonde urinaire |
| Sécurité | Lit bas, environnement dégagé, surveillance rapprochée ; **éviter la contention physique**, qui aggrave l'agitation et expose à des complications graves |

### 12.5 Traitement médicamenteux symptomatique : place limitée

- Il n'est **pas** un traitement de la confusion : il ne se discute que si le patient présente une **détresse importante** (hallucinations terrifiantes, angoisse majeure) ou un **danger** pour lui-même ou autrui, **après échec ou impossibilité** des mesures non médicamenteuses et de désescalade verbale [S1, S6].
- **NICE (CG103, 1.7.4)** : si les techniques de désescalade verbale et non verbale sont inefficaces ou inappropriées, envisager un **halopéridol à court terme** (habituellement une semaine ou moins), à la **dose la plus faible** cliniquement appropriée, titrée prudemment, en tenant compte de l'avis de l'agence britannique du médicament (MHRA) sur les risques cardiaques et neurologiques chez le sujet âgé, en particulier en cas de maladie de Parkinson ou de démence à corps de Lewy [S1]. Ni le NICE ni la HAS ne fixent de dose absolue `[POSOLOGIE À VÉRIFIER — RCP / protocole local]`.
- **HAS (2009)** : aucun médicament n'a d'AMM dans cette indication ; si un traitement est nécessaire (agitation sévère, anxiété majeure, danger, soins indispensables impossibles), **monothérapie** pour **24 à 48 heures au maximum** ; administrer une première dose et en évaluer l'effet avant de renouveler ; débuter à **1/4 à 1/2 de la dose de l'adulte** ; si l'**anxiété** prédomine, benzodiazépine orale d'action rapide et de durée d'action courte (alprazolam, lorazépam, oxazépam) ; si des **troubles productifs** (hallucinations, délire) prédominent, neuroleptique adapté au profil du patient, de préférence par voie orale (buvable ou orodispersible), en évitant la forme injectable ; réintroduire à faible dose une benzodiazépine arrêtée brutalement si un sevrage est suspecté [S6].
- **Benzodiazépines** : à éviter chez le sujet âgé confus ou à risque de confusion (Beers 2023 : elles peuvent la provoquer ou l'aggraver), **sauf** sevrage alcoolique ou en benzodiazépines, où elles peuvent être appropriées et sont le traitement de choix [S10, S17] ; la HAS 2009 admet toutefois, hors sevrage, une benzodiazépine de courte durée d'action quand l'anxiété prédomine (voir ci-dessus et § 20) [S6].
- Surveillance de tout antipsychotique : sédation excessive, chutes, fausses routes, syndrome extrapyramidal, allongement du QT (ECG), hypotension.
- **Prévention médicamenteuse** (antipsychotiques, mélatonine, etc.) : non recommandée de façon systématique en l'état des données ; en réanimation, les recommandations PADIS suggèrent de ne pas utiliser d'halopéridol ni d'antipsychotique atypique pour prévenir le delirium chez tous les patients [S16] `[À VÉRIFIER — formulation]`.

### 12.6 Révision de l'ordonnance : la charge anticholinergique

Les effets anticholinergiques **s'additionnent** : plusieurs médicaments faiblement anticholinergiques, pris ensemble, peuvent provoquer une confusion. Les critères de Beers 2023 recommandent d'éviter, chez le sujet âgé confus ou à haut risque de confusion, les **anticholinergiques**, les **antipsychotiques** (sauf échec des mesures non médicamenteuses et danger important), les **benzodiazépines**, les **hypnotiques apparentés** (« Z-drugs »), les **corticoïdes**, les **anti-H2** et les **opioïdes** (ajoutés en 2023), et de limiter le nombre de médicaments anticholinergiques associés (tableau relu dans le texte intégral) [S10] ; les critères STOPP/START v3 comportent des critères de même esprit [S11] `[libellés STOPP/START non relus]`.

| Classe | Exemples (molécules courantes) | Piste de remplacement (à discuter au cas par cas) |
|---|---|---|
| Antispasmodiques urinaires | Oxybutynine, toltérodine, solifénacine | Mesures comportementales (mictions programmées) ; alternatives non anticholinergiques selon avis spécialisé |
| Antihistaminiques de 1re génération | Hydroxyzine, dexchlorphéniramine, prométhazine | Antihistaminiques non sédatifs (allergie) ; mesures d'hygiène du sommeil (insomnie) |
| Antidépresseurs tricycliques | Amitriptyline, clomipramine, imipramine | Autres classes d'antidépresseurs selon le contexte |
| Antipsychotiques à forte activité anticholinergique | Phénothiazines (chlorpromazine…) | Éviter ; avis spécialisé |
| Antiparkinsoniens anticholinergiques | Trihexyphénidyle | Éviter chez le sujet âgé |
| Antispasmodiques digestifs, certains antiémétiques | Selon les spécialités | Réévaluer l'indication |

Démarche : **lister** tous les médicaments, **identifier** ceux qui sont anticholinergiques ou sédatifs, **arrêter** ce qui n'est pas indispensable, **substituer** ce qui peut l'être, **diminuer progressivement** ce qui expose à un sevrage (benzodiazépines, antidépresseurs), puis **réévaluer** la confusion. Les dosages pharmacologiques (digoxine, lithium) et l'adaptation à la fonction rénale (DFG estimé) font partie de cette révision.

### 12.7 Rôle de l'équipe soignante et des aidants

- **Infirmiers et aides-soignants** : repérage quotidien (4AT), surveillance de l'hydratation, du transit, de la diurèse, de la douleur et du sommeil, réorientation, signalement des fluctuations ; ils sont au premier plan de la prévention.
- **Médecin** : bilan étiologique, révision médicamenteuse, décision et réévaluation de tout psychotrope, information de la famille.
- **Kinésithérapeute** : lever précoce, prévention des chutes et du déconditionnement.
- **Aidants familiaux** : présence rassurante (surtout la nuit), apport d'objets familiers, lunettes et appareils auditifs, informations sur l'état antérieur ; ils doivent être **informés** que la confusion est une complication médicale souvent réversible, et non une « folie » ou une démence brutale.
- **Communication** : expliquer au patient, une fois l'épisode résolu, ce qui s'est passé (les souvenirs d'hallucinations ou de contention peuvent être traumatisants).

### 12.8 Confusion à domicile : conduite du médecin généraliste

1. Évaluer la gravité (paramètres vitaux, glycémie capillaire, vigilance, signes de localisation, fièvre, déshydratation, chute récente).
2. Relire l'ordonnance et rechercher les modifications récentes ; rechercher un globe vésical et un fécalome.
3. Hospitaliser si : signe de gravité, cause non évidente, impossibilité de surveillance, chute avec traumatisme crânien sous anticoagulant, suspicion d'AVC, de sepsis ou de syndrome coronarien.
4. Maintien à domicile envisageable seulement si la cause est évidente et rapidement corrigeable (médicament arrêté, rétention levée), avec un entourage présent et une réévaluation dans les 24 à 48 heures.
5. Prévenir la récidive : ordonnance simplifiée, éviter les anticholinergiques et sédatifs, informer l'entourage des signes d'alerte.

### 12.9 Aspects éthiques et légaux (Algérie)

- Le patient confus a souvent une **capacité de consentement altérée** : l'information est adaptée et répétée ; l'entourage est associé. La loi 18-11 pose le principe du **consentement libre et éclairé** (art. 343) et prévoit que les droits des personnes **incapables** sont exercés par les parents ou le représentant légal (art. 23) ; l'accès aux soins ne peut être refusé, notamment en urgence (art. 21) [S15].
- Le delirium est une **urgence somatique** : sa prise en charge relève d'abord d'un service de médecine ou de gériatrie, avec avis psychiatrique si besoin ; une réflexion collégiale et une traçabilité sont nécessaires pour toute mesure restrictive. Le cadre légal précis de la **contention physique** en milieu somatique n'a pas été retrouvé dans les textes consultés `[À VÉRIFIER]`.
- Signalement de **maltraitance** éventuelle d'une personne âgée vulnérable (art. 198) [S15].

---

## 13. Surveillance

- Repérage quotidien (4AT, CAM) et suivi des fluctuations ; vigilance, hydratation, alimentation, diurèse, transit, douleur, sommeil, chutes, état cutané.
- Efficacité et tolérance des traitements (sédation, ECG si antipsychotique).
- Contrôle de la résolution des causes (biologie, infection).
- À la sortie : **information** du patient et de la famille sur l'épisode (et le risque de récidive), liste des médicaments à éviter, transmission au médecin référent ; **réévaluation cognitive à distance** (classiquement quelques semaines à 3 mois après l'épisode) pour dépister un trouble neurocognitif sous-jacent [S1, S7].

---

## 14. Prévention

La confusion est **évitable** dans une proportion importante des cas à l'hôpital grâce à des **interventions multicomposantes non médicamenteuses**. Dans l'essai HELP, une telle intervention a réduit l'incidence de la confusion chez des patients hospitalisés de 70 ans et plus (9,9 % contre 15,0 % dans le groupe soins usuels ; OR apparié 0,60) [S8].

Le NICE recommande, chez les patients à risque, une **évaluation dans les 24 heures** suivant l'admission et une **intervention multicomposante** adaptée, délivrée par une équipe formée, ciblant notamment [S1] :
- désorientation et troubles cognitifs (orientation, activités stimulantes, visites) ;
- déshydratation et constipation ;
- hypoxie ;
- infections (et éviter les sondages urinaires inutiles) ;
- immobilité (lever et mobilisation précoces) ;
- douleur (évaluation, y compris chez les patients non communicants) ;
- polymédication (révision) ;
- nutrition ;
- déficits sensoriels (lunettes, appareils auditifs, bouchons de cérumen) ;
- sommeil (éviter les soins nocturnes, réduire le bruit).

Autres mesures : évaluation gériatrique et prise en charge **orthogériatrique** des fractures du col, anesthésie et analgésie adaptées, révision des prescriptions à l'aide des critères **Beers 2023** et **STOPP/START v3** (anticholinergiques, benzodiazépines) [S10, S11], formation des équipes, implication des familles.

---

## 15. Algorithmes décisionnels

### 15.1 Devant une modification aiguë du comportement ou de la cognition

```text
1. Urgences vitales immédiates ?
   - glycémie capillaire, SpO2, PA, FC, température, vigilance (score de Glasgow)
   - hypoglycémie → resucrage ; hypoxie → oxygène ; choc/sepsis → prise en charge urgente
2. Est-ce une confusion ? → repérage 4AT (≥ 4 : confusion possible) ; confirmer par CAM ou critères DSM-5-TR
   - inattention + début aigu/fluctuant = argument clé
   - interroger l'entourage sur l'état antérieur (démence connue ?)
3. Recherche de la cause (souvent multiple) :
   a. MÉDICAMENTS : introduction, arrêt, majoration récents ; anticholinergiques, sédatifs, opioïdes ; sevrage (alcool, benzodiazépines)
   b. Examen : globe vésical, fécalome, douleur, déshydratation, foyer infectieux, signes neurologiques, traumatisme
   c. Bilan socle : NFS, CRP, ionogramme, calcémie, glycémie, urée, créatinine, bilan hépatique, ECG, BU
   d. Bilan orienté : gaz du sang, hémocultures, radiographie thoracique, troponine, dosages médicamenteux
   e. Scanner cérébral si : signe focal, chute/traumatisme crânien (anticoagulant), vigilance altérée inexpliquée, cause non trouvée
   f. PL si fièvre sans foyer ou syndrome méningé ; EEG si suspicion d'état de mal non convulsif
4. Traiter chaque cause identifiée ; arrêter ou adapter les médicaments responsables
5. Mesures non médicamenteuses pour tous ; éviter contention et sonde urinaire
6. Détresse sévère ou danger persistant malgré ces mesures ?
   → traitement médicamenteux bref (24-48 h selon la HAS), à faible dose, réévalué au moins quotidiennement (halopéridol selon NICE ; benzodiazépine en cas de sevrage, ou d'anxiété prédominante selon la HAS)
   → prudence extrême si Parkinson / démence à corps de Lewy (avis spécialisé)
7. Surveillance quotidienne ; à la sortie : information, transmission, réévaluation cognitive à distance
```

### 15.2 Orientation diagnostique rapide selon le contexte

```text
- Fièvre                         → infection (poumon, urine, peau, abdomen) ; méningite si signes méningés
- Globe vésical / constipation   → rétention urinaire (anticholinergiques, adénome) ; fécalome (opioïdes)
- Médicament récent              → iatrogénie ; syndrome anticholinergique ou sérotoninergique
- Arrêt récent d'alcool / BZD    → sevrage (delirium tremens) → benzodiazépine + thiamine (avant tout glucide)
- Chute / anticoagulant          → hématome sous-dural (scanner)
- Signes de localisation         → AVC (imagerie urgente)
- Somnolence + BPCO / opioïdes   → hypercapnie (gaz du sang)
- Diurétique / ISRS              → hyponatrémie
- Diabétique traité              → hypoglycémie
- Confusion fluctuante inexpliquée → état de mal non convulsif (EEG)
```

---

## 16. Cas clinique commenté (fictif)

**Présentation.** Mme B., 87 ans, atteinte d'une maladie d'Alzheimer au stade léger (MMSE à 22/30 il y a 6 mois), vivant chez sa fille, est amenée aux urgences pour une **agitation nocturne** et des **propos incohérents** depuis 48 heures. Elle « voit des enfants dans la chambre », a tenté de sortir la nuit, et somnole le jour. Il y a 5 jours, son médecin a introduit de l'**oxybutynine** pour une incontinence par urgenturie et du **tramadol** pour des douleurs de gonarthrose. Traitements habituels : donépézil, amlodipine.

**Examen.** T 37,4 °C, PA 138/76 mmHg, FC 96/min, SpO₂ 95 % en air ambiant, glycémie capillaire 1,12 g/L. Patiente somnolente par moments, puis agitée ; elle ne peut pas dire les mois de l'année à l'envers au-delà de « décembre, novembre » ; se trompe sur l'année et le lieu. **Globe vésical** (échographie : 650 mL) ; **fécalome** au toucher rectal ; muqueuses sèches ; pas de signe de localisation neurologique ; pas de syndrome méningé ; auscultation pulmonaire normale.

**4AT** : vigilance anormale (4) + AMT4 : 2 erreurs (2) + mois à l'envers : débute mais < 7 mois (1) + changement aigu rapporté par la fille (4) = **11/12** → confusion probable. **CAM** : début aigu et fluctuant (+), inattention (+), pensée désorganisée (+), niveau de conscience altéré (+) → positif.

**Biologie.** Na 133 mmol/L, K 4,1 mmol/L, calcémie normale, urée 0,62 g/L, créatinine 13 mg/L (valeur habituelle 9 mg/L), CRP 12 mg/L, NFS normale, bilan hépatique normal ; BU : leucocytes +, nitrites − ; ECG : rythme sinusal, QTc 440 ms.

**Raisonnement et conduite.**
1. *Diagnostic* : **confusion mixte** (agitation nocturne, somnolence diurne) superposée à une démence légère.
2. *Causes probables, cumulées* : effet **anticholinergique** de l'oxybutynine (confusion + rétention urinaire), **tramadol** (confusiogène, constipant, abaisse le seuil épileptogène, risque sérotoninergique avec certains antidépresseurs), **rétention aiguë d'urine** et **fécalome** (aggravés par les deux médicaments), **déshydratation** modérée (insuffisance rénale fonctionnelle) ; l'association d'un **anticholinergique** et d'un **anticholinestérasique** (donépézil) est pharmacologiquement incohérente.
3. *Mesures* : **arrêt** de l'oxybutynine et du tramadol ; **sondage évacuateur** (puis ablation de la sonde dès que possible, avec contrôle du résidu) ; évacuation du fécalome et laxatifs ; réhydratation ; antalgie par **paracétamol** ; la leucocyturie isolée sans fièvre ni signes urinaires n'impose pas d'antibiotique d'emblée (prélever un ECBU, réévaluer).
4. *Environnement* : présence de la fille, lunettes, horloge, chambre calme et éclairée le jour, lever accompagné, pas de contention.
5. *Psychotrope* : la première nuit, malgré les mesures, la patiente est très angoissée par ses hallucinations et tente d'enjamber les barrières : un antipsychotique à **très faible dose** (1/4 à 1/2 de la dose de l'adulte, par voie orale, une première prise dont on évalue l'effet, 24 à 48 h au maximum selon la HAS 2009 [S6] ; halopéridol à la plus faible dose selon le NICE [S1]) est discuté et prescrit, avec réévaluation le lendemain et ECG de contrôle `[POSOLOGIE À VÉRIFIER — RCP / protocole local]`.
6. *Évolution* : amélioration nette en 72 heures ; 4AT à 2 au 5e jour (troubles cognitifs connus). Sortie avec une ordonnance révisée (pas d'anticholinergique ; prise en charge non médicamenteuse de l'incontinence), information de la famille et du médecin référent, **réévaluation cognitive à 3 mois**.

**Message pédagogique** : chez le sujet âgé, la confusion est souvent **iatrogène** et **multifactorielle** ; l'examen de la **vessie** et du **rectum** et la **lecture de l'ordonnance** valent souvent plus qu'un scanner.

---

## 17. Points clés à retenir

1. Le syndrome confusionnel aigu (**delirium**) associe **trouble de l'attention et de la conscience**, **début rapide**, **fluctuations**, autres troubles cognitifs, et une **cause organique**.
2. C'est une **urgence médicale**, fréquente, grave, **sous-diagnostiquée**, surtout dans sa forme **hypoactive**.
3. Modèle **vulnérabilité × facteurs précipitants** : chez un sujet très vulnérable (démence), une cause minime suffit ; les causes sont souvent **multiples**.
4. Repérage par le **4AT** (≥ 4 : confusion possible) ; diagnostic par la **CAM** (1 + 2 + [3 ou 4]) ou les critères DSM-5-TR ; tester l'**attention** (mois à l'envers).
5. Causes à rechercher en premier : **médicaments** (anticholinergiques, benzodiazépines, opioïdes, sevrages), **rétention urinaire**, **fécalome**, **douleur**, **déshydratation**, **infection**, troubles **métaboliques** (Na, Ca, glucose), hypoxie/hypercapnie, **hématome sous-dural**.
6. Bilan socle : glycémie, NFS, CRP, ionogramme, calcémie, urée, créatinine, bilan hépatique, ECG, BU ; **scanner cérébral non systématique**.
7. Traitement : **cause** + mesures **non médicamenteuses** ; **pas de contention** ; psychotrope seulement en cas de détresse ou de danger, **bref**, à **faible dose**, réévalué ; **benzodiazépines** réservées aux **sevrages**.
8. Prévention **multicomposante** non médicamenteuse chez les patients à risque (orientation, hydratation, mobilisation, sommeil, sensoriel, révision des médicaments, douleur).
9. Pronostic : surmortalité, perte d'autonomie, institutionnalisation, déclin cognitif → **suivi cognitif** après l'épisode.

---

## 18. Pièges classiques à l'examen

- Confondre **confusion** (delirium) et **délire** (idée délirante).
- Attribuer une agitation aiguë à « la démence » ou à « l'âge » sans rechercher de cause organique.
- Méconnaître la forme **hypoactive** (somnolence, apathie) en la prenant pour une dépression ou de la fatigue.
- Conclure à une **infection urinaire** sur une bandelette positive isolée sans fièvre ni signes urinaires (bactériurie asymptomatique fréquente) et arrêter là le bilan.
- Oublier le **globe vésical** et le **fécalome**.
- Prescrire une **benzodiazépine** pour calmer une confusion qui n'est pas liée à un sevrage.
- Prescrire un **neuroleptique** à un patient parkinsonien ou atteint de démence à corps de Lewy sans précaution.
- Recourir à la **contention physique**, qui aggrave l'agitation.
- Demander un **scanner cérébral** systématique… ou l'oublier après une chute sous anticoagulant.
- Arrêter **brutalement** une benzodiazépine prise depuis des années (sevrage confusiogène).
- Associer un **anticholinergique** à un **anticholinestérasique** chez un patient dément.

---

## 19. QCM d'auto-évaluation

**QCM 1.** Concernant le syndrome confusionnel aigu :
A. Le trouble de l'attention en est l'élément central
B. Le début est progressif sur plusieurs mois
C. Les symptômes fluctuent au cours de la journée
D. Une cause organique est présente par définition
E. Il ne peut pas survenir chez un patient dément

**QCM 2.** La forme hypoactive de la confusion :
A. Est rare chez le sujet âgé
B. Est souvent méconnue
C. Peut être prise à tort pour une dépression
D. A un pronostic plus défavorable que la forme hyperactive
E. Ne nécessite pas de bilan étiologique

**QCM 3.** Concernant le 4AT :
A. Il comporte une évaluation de la vigilance
B. Il comporte un test d'attention par les mois de l'année à l'envers
C. Un score ≥ 4 évoque une confusion possible
D. Il nécessite une formation spécifique longue
E. Il est l'outil de repérage recommandé par défaut par le NICE depuis 2023

**QCM 4.** Selon l'algorithme de la CAM, le diagnostic de confusion requiert :
A. Un début aigu et une évolution fluctuante
B. Une inattention
C. Une pensée désorganisée ou une altération du niveau de conscience
D. Des hallucinations visuelles
E. Une désorientation temporo-spatiale obligatoire

**QCM 5.** Médicaments fréquemment en cause dans une confusion du sujet âgé :
A. Oxybutynine
B. Hydroxyzine
C. Tramadol
D. Benzodiazépines
E. Paracétamol à dose usuelle

**QCM 6.** Bilan initial d'une confusion chez une femme de 85 ans sans signe de localisation ni chute :
A. Glycémie capillaire
B. Ionogramme sanguin et calcémie
C. ECG
D. Recherche d'un globe vésical
E. Scanner cérébral systématique

**QCM 7.** Concernant le traitement :
A. Le traitement étiologique est prioritaire
B. La contention physique est recommandée en première intention en cas d'agitation
C. Un antipsychotique peut être envisagé brièvement en cas de détresse sévère ou de danger
D. Les benzodiazépines sont le traitement de choix du delirium tremens
E. Les neuroleptiques doivent être évités ou utilisés avec une grande prudence dans la démence à corps de Lewy

**QCM 8.** Mesures de prévention de la confusion à l'hôpital :
A. Réorientation régulière (horloge, calendrier)
B. Remise des lunettes et des appareils auditifs
C. Mobilisation précoce
D. Pose systématique d'une sonde urinaire pour surveiller la diurèse
E. Respect du sommeil nocturne

**QCM 9.** Diagnostic différentiel confusion / démence :
A. La démence a un début insidieux
B. L'attention est très altérée dès le début de la démence d'Alzheimer
C. Les fluctuations marquées orientent vers une confusion
D. La démence à corps de Lewy peut comporter des fluctuations et des hallucinations visuelles
E. Une confusion peut révéler une démence méconnue

**QCM 10.** Après un épisode de confusion :
A. Le risque de déclin cognitif ultérieur est augmenté
B. Une réévaluation cognitive à distance est recommandée
C. Le pronostic vital n'est jamais modifié
D. Le patient et sa famille doivent être informés
E. Les médicaments responsables doivent être signalés au médecin référent

### Corrigé commenté

- **QCM 1 : A, C, D.** B faux (début rapide) ; E faux (la démence est le principal facteur de risque).
- **QCM 2 : B, C, D.** A faux (forme la plus fréquente chez le sujet âgé) ; E faux.
- **QCM 3 : A, B, C, E.** D faux (outil rapide, sans formation spécifique) [S1, S4].
- **QCM 4 : A, B, C** [S3]. D et E ne sont pas des critères obligatoires.
- **QCM 5 : A, B, C, D.** Oxybutynine et hydroxyzine : anticholinergiques ; tramadol : opioïde sérotoninergique ; benzodiazépines. E faux.
- **QCM 6 : A, B, C, D.** E faux : imagerie orientée (signe focal, chute, cause non trouvée) [S6].
- **QCM 7 : A, C, D, E.** B faux : la contention aggrave l'agitation et expose à des complications.
- **QCM 8 : A, B, C, E.** D faux (la sonde urinaire est un facteur précipitant).
- **QCM 9 : A, C, D, E.** B faux (attention relativement préservée aux stades initiaux).
- **QCM 10 : A, B, D, E.** C faux (surmortalité associée).

---

## 20. Divergences entre recommandations

| Sujet | Position 1 (organisme, date) | Position 2 (organisme, date) | Commentaire |
|---|---|---|---|
| Outil de repérage | NICE 2023 : **4AT** par défaut ; CAM-ICU ou ICDSC en réanimation et salle de réveil [S1] | HAS 2009 : décrit la **CAM**, mais en souligne les limites en pratique courante (traduction française non validée, formation formalisée nécessaire) et recommande sa validation ; MMSE dès que possible comme référence [S6] | Le 4AT, plus court et utilisable sans formation, s'est imposé dans les recommandations récentes |
| Psychotropes en cas d'agitation | NICE CG103 : halopéridol à court terme (≤ 1 semaine) si détresse ou danger, après échec de la désescalade [S1] ; Beers 2023 : benzodiazépines à éviter en cas de confusion, sauf sevrage [S10] | HAS 2009 : monothérapie de 24 à 48 h au maximum, à 1/4-1/2 de la dose adulte ; benzodiazépine orale de courte durée d'action (alprazolam, lorazépam, oxazépam) quand l'anxiété prédomine, neuroleptique quand les troubles productifs prédominent [S6] | Accord sur le principe « le moins possible, le plus court possible » ; désaccord sur la place des benzodiazépines hors sevrage |
| Prévention médicamenteuse | NICE CG103 : prévention par intervention multicomposante non médicamenteuse, sans prévention médicamenteuse recommandée [S1] ; SIGN 157 : position non relue `[À VÉRIFIER]` [S12] | Réanimation (PADIS 2018) : suggestion de ne pas utiliser halopéridol ni antipsychotique atypique en prévention chez tous les patients [S16] | Priorité aux interventions multicomposantes non médicamenteuses [S8] |
| Champ des recommandations | HAS 2009 : exclut la confusion postopératoire [S6] | NICE : hôpital (y compris chirurgie) et établissements de long séjour [S1] | Pour la chirurgie, se référer aux recommandations spécifiques (orthogériatrie, anesthésie) |
| Classification | DSM-5-TR : delirium dans les troubles neurocognitifs ; sous-types hyper/hypo/mixte [S2] | CIM-11 : delirium (6D70 ; code vérifié sur des sources secondaires, voir § 1.2) | Terminologie française : « syndrome confusionnel aigu » ≈ delirium |

---

## 21. Références

1. [S1] NICE. Delirium: prevention, diagnosis and management in hospital and long-term care (CG103). 2010, updated January 2023.
2. [S2] American Psychiatric Association. DSM-5-TR. 2022.
3. [S3] Inouye SK et al. Clarifying confusion: the confusion assessment method. Ann Intern Med 1990;113(12):941-948. doi:10.7326/0003-4819-113-12-941.
4. [S4] Tieges Z et al. Diagnostic accuracy of the 4AT for delirium detection in older adults. Age Ageing 2021;50(3):733-743. doi:10.1093/ageing/afaa224.
5. [S5] Bellelli G et al. Validation of the 4AT. Age Ageing 2014;43(4):496-502.
6. [S6] HAS. Confusion aiguë chez la personne âgée : prise en charge initiale de l'agitation. Mai 2009.
7. [S7] Inouye SK, Westendorp RGJ, Saczynski JS. Delirium in elderly people. Lancet 2014;383:911-922.
8. [S8] Inouye SK et al. A multicomponent intervention to prevent delirium in hospitalized older patients. N Engl J Med 1999;340:669-676.
9. [S9] Inouye SK, Charpentier PA. JAMA 1996;275(11):852-857.
10. [S10] American Geriatrics Society. 2023 updated AGS Beers Criteria. J Am Geriatr Soc 2023;71(7):2052-2081. doi:10.1111/jgs.18372.
11. [S11] O'Mahony D et al. STOPP/START version 3. Eur Geriatr Med 2023;14(4):625-632. doi:10.1007/s41999-023-00777-y.
12. [S12] SIGN 157. Risk reduction and management of delirium. 2019.
13. [S13] Ely EW et al. CAM-ICU. JAMA 2001;286(21):2703-2710.
14. [S14] Wilson JE et al. Delirium. Nat Rev Dis Primers 2020;6:90.
15. [S15] Loi n° 18-11 du 2 juillet 2018 relative à la santé (DOC-00074).
16. [S16] Devlin JW et al. PADIS guidelines. Crit Care Med 2018;46(9):e825-e873.
17. [S17] NICE. Alcohol-use disorders: diagnosis and management of physical complications (CG100). 2010, mises à jour 2017.
18. [S18] Galvin R et al. EFNS guidelines for diagnosis, therapy and prevention of Wernicke encephalopathy. Eur J Neurol 2010;17(12):1408-1418.
