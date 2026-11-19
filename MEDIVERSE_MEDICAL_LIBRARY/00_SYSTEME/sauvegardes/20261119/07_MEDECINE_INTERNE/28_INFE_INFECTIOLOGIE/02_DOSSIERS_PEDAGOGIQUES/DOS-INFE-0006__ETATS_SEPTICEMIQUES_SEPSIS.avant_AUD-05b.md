---
id: DOS-INFE-0006
titre: "États septicémiques (sepsis) : diagnostic, pronostic, traitement"
specialite: INFE
sous_specialite: "Infections systémiques — sepsis, bactériémies et choc septique"
items_residanat: [RES-MED-004]
niveaux: [etudiant, generaliste, resident, residanat, dems]
langue: fr
version: "1.1"
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent DOS-02 (IA) — dossier pédagogique original"
statut: audite_corrections_requises
audit:
  - date: 2026-11-19
    auditeur: "AUD-01 / AUD-02 (IA)"
    verdict: audite_corrections_requises
    corrections: 14
    rapport: 00_SYSTEME/agents/AUD-01/rapports/DOS-INFE-0006.md
sources:
  - id: S1
    reference: "Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810."
    organisme: "SCCM / ESICM (Sepsis-3 Task Force)"
    annee: 2016
    type: recommandation
    doi: "10.1001/jama.2016.0287"
    url: "https://doi.org/10.1001/jama.2016.0287"
    verifiee: true
    remarque: "Référence vérifiée dans le catalogue (REC-0268 ; Europe PMC, PMID 26903338) ; définitions reprises également par le livre AWaRe [S4], lu."
  - id: S2
    reference: "Evans L, Rhodes A, Alhazzani W, et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2021. Intensive Care Med. 2021;47(11):1181-1247 (copublication : Crit Care Med. 2021;49(11):e1063-e1143)."
    organisme: "Surviving Sepsis Campaign (SCCM / ESICM)"
    annee: 2021
    type: recommandation
    doi: "10.1007/s00134-021-06506-y"
    url: ""
    verifiee: true
    remarque: "Référence, pages et DOI confirmés par recherche web (PubMed 34605781) ; statut « remplacée » par la SSC 2026 dans le catalogue (REC-0265). Audit AUD-01/AUD-02 (2026-11-19) : texte intégral en libre accès lu (Europe PMC, PMC8486643) — formulations vérifiées : qSOFA (rec. 2, forte), lactate (rec. 3), 30 mL/kg en 3 h (rec. 5, faible), délais des antimicrobiens (rec. 12–15), PCT (rec. 16), bithérapie anti-BGN (rec. 19), antifongiques (rec. 22), perfusion prolongée (rec. 25), contrôle de la source (rec. 27–28), désescalade (rec. 29), cristalloïdes balancés, albumine, amidons, gélatines (rec. 32–36), PAM 65 mmHg, vasopressine (0,25–0,5 µg/kg/min), dobutamine/adrénaline (rec. 41), voie périphérique (rec. 44), hydrocortisone 200 mg/j à partir de 0,25 µg/kg/min au moins 4 h après le début (rec. 58), bicarbonate, insuline, vitamine C."
  - id: S3
    reference: "Prescott HC, Antonelli M, Alhazzani W, et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2026. Intensive Care Med. 2026;52(5):863-936 (copublication : Crit Care Med. 2026;54(4):725-812)."
    organisme: "Surviving Sepsis Campaign (SCCM / ESICM)"
    annee: 2026
    type: recommandation
    doi: "10.1007/s00134-026-08361-1"
    url: "https://doi.org/10.1007/s00134-026-08361-1"
    verifiee: true
    remarque: "Existence et métadonnées vérifiées (catalogue REC-0266, Europe PMC PMID 41870560 ; rapport d'audit AUD-02 de DOS-MINT_REA-0001). Contenu NON lu : les modifications citées (30 mL/kg maintenu avec certitude faible et poids ajusté si IMC > 30 ; NEWS/MEWS/SIRS préférés au qSOFA ; certitude des corticoïdes abaissée ; noradrénaline en 1re intention) proviennent de résumés secondaires rapportés par l'audit [À VÉRIFIER]."
  - id: S4
    reference: "World Health Organization. The WHO AWaRe (Access, Watch, Reserve) antibiotic book. Geneva: WHO; 2022. Chapitre 24 « Sepsis in adults (including septic shock) » (p. 295-318)."
    organisme: OMS
    annee: 2022
    type: recommandation
    doi: ""
    url: "https://iris.who.int/handle/10665/365237"
    verifiee: true
    remarque: "Document acquis (DOC-00039) ; chapitre 24 lu (pdftotext) : définitions, épidémiologie (GBD 2017), antibiothérapie probabiliste par foyer, posologies et durées."
  - id: S5
    reference: "National Institute for Health and Care Excellence. Suspected sepsis: recognition, diagnosis and early management. NICE guideline NG51. Publié en 2016, mis à jour le 19 mars 2024."
    organisme: NICE
    annee: 2024
    type: recommandation
    doi: ""
    url: "https://www.nice.org.uk/guidance/ng51"
    verifiee: true
    remarque: "Vérifiée dans le catalogue (REC-0488) ; contenu détaillé (seuils NEWS2) non lu [À VÉRIFIER]."
  - id: S6
    reference: "Schlapbach LJ, Watson RS, Sorce LR, et al. International consensus criteria for pediatric sepsis and septic shock. JAMA. 2024;331(8):665-674."
    organisme: "SCCM Pediatric Sepsis Definition Task Force"
    annee: 2024
    type: recommandation
    doi: ""
    url: "https://jamanetwork.com/journals/jama/fullarticle/2814297"
    verifiee: true
    remarque: "Confirmée par recherche web : sepsis de l'enfant = score de Phoenix ≥ 2 chez un enfant suspect d'infection ; choc septique = sepsis avec ≥ 1 point cardiovasculaire ; article compagnon Sanchez-Pinto et al., JAMA 2024;331:675-686."
  - id: S7
    reference: "Weiss SL, Peters MJ, Alhazzani W, et al. Surviving Sepsis Campaign international guidelines for the management of septic shock and sepsis-associated organ dysfunction in children. Pediatr Crit Care Med. 2020;21(2):e52-e106."
    organisme: "Surviving Sepsis Campaign (SCCM / ESICM)"
    annee: 2020
    type: recommandation
    doi: "10.1097/PCC.0000000000002198"
    url: ""
    verifiee: true
    remarque: "Vérifiée dans le catalogue (REC-0267, Europe PMC PMID 32032273) ; points clés repris de la fiche du catalogue ; texte non lu. REMPLACÉE par la SSC enfant 2026 [S10] (audit 2026-11-19)."
  - id: S8
    reference: "Décret exécutif n°22-250 du 30 juin 2022 fixant la liste des maladies transmissibles soumises à déclaration obligatoire. JORADP n°47 du 11 juillet 2022."
    organisme: "Gouvernement algérien / Ministère de la Santé"
    annee: 2022
    type: texte_officiel
    doi: ""
    url: "https://www.joradp.dz/FTP/JO-FRANCAIS/2022/F2022047.pdf"
    verifiee: true
    remarque: "Document acquis (DOC-00072) et lu : infections à bactéries multirésistantes, infections du site opératoire et pneumopathies acquises sous ventilation mécanique en catégorie 1 ; méningites bactériennes, typhoïde, brucellose."
  - id: S9
    reference: "Seymour CW, Liu VX, Iwashyna TJ, et al. Assessment of clinical criteria for sepsis: for the Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):762-774."
    organisme: "Sepsis-3 Task Force"
    annee: 2016
    type: article
    doi: ""
    url: ""
    verifiee: true
    remarque: "Article de validation du qSOFA cité de mémoire. Audit 2026-11-19 : vérifié par l'API PubMed (PMID 26903335 ; doi 10.1001/jama.2016.0288) ; texte intégral non lu."
  - id: S10
    reference: "Weiss SL, Peters MJ, Oczkowski SJW, et al. Surviving Sepsis Campaign International Guidelines for the Management of Sepsis and Septic Shock in Children 2026. Pediatr Crit Care Med. 2026;27(4):379-434 (copublication : Intensive Care Med. 2026;52(5):937-983)."
    organisme: "Surviving Sepsis Campaign (SCCM / ESICM)"
    annee: 2026
    type: recommandation
    doi: "10.1097/PCC.0000000000003927"
    url: ""
    verifiee: true
    remarque: "Audit 2026-11-19 : existence et métadonnées vérifiées par l'API PubMed (PMID 41869844 ; ICM : PMID 41870559, doi 10.1007/s00134-026-08360-2). Remplace la SSC enfant 2020 [S7]. Contenu non lu [À VÉRIFIER]."
mots_cles: [sepsis, choc septique, Sepsis-3, SOFA, qSOFA, NEWS2, bactériémie, lactate, hémocultures, antibiothérapie probabiliste, contrôle de la source, noradrénaline, hydrocortisone, Surviving Sepsis Campaign, Phoenix, Algérie]
---

# États septicémiques (sepsis) : diagnostic, pronostic, traitement

> **Dossier pédagogique original Mediverse** — rédigé à partir de plusieurs sources citées ; ne reproduit aucun ouvrage.
> Statut : audité par AUD-01/AUD-02 (IA) le 2026-11-19 — corrections requises (bloc `audit` et rapport). Les posologies doivent être confrontées au RCP et aux protocoles locaux avant usage clinique. **Traçabilité** : le chapitre « Sepsis in adults » du livre AWaRe de l'OMS [S4] et le décret 22-250 [S8] ont été **lus** ; le texte intégral de la SSC 2021 [S2] a été lu lors de l'audit (libre accès) ; la SSC 2026 adulte [S3] et la SSC enfant 2026 [S10] ont été **vérifiées quant à leur existence** mais leur texte n'a pas pu être lu (la SSC 2026 est citée d'après les synthèses rapportées par l'audit de DOS-MINT_REA-0001). La réanimation hémodynamique détaillée est traitée dans le dossier `DOS-MINT_REA-0001` (États de choc).

**Items du programme couverts** : RES-MED-004 — « États septicémiques : Diagnostic - pronostic - traitement ».

**Objectifs pédagogiques** — être capable de :
1. **Définir** le sepsis et le choc septique selon Sepsis-3, et **situer** les termes historiques (septicémie, bactériémie, SRIS, sepsis sévère).
2. **Repérer** précocement un sepsis (outils de dépistage : NEWS2, SIRS, qSOFA) et **évaluer** les dysfonctions d'organe (SOFA, lactate).
3. **Rechercher** la porte d'entrée et le foyer infectieux, et **prescrire** les prélèvements microbiologiques avant les antibiotiques.
4. **Prescrire dans l'heure** une antibiothérapie probabiliste adaptée au foyer, au terrain et au risque de bactéries multirésistantes.
5. **Mettre en œuvre** le contrôle de la source et la réanimation initiale (remplissage, noradrénaline, hydrocortisone).
6. **Évaluer** le pronostic et **organiser** la réévaluation (désescalade, durée, relais oral).
7. **Connaître** les spécificités pédiatriques (critères de Phoenix) et le contexte algérien (BMR à déclaration obligatoire).

---

## 1. Définitions et généralités

### 1.1 Définitions actuelles (Sepsis-3, 2016) [S1]
- **Sepsis** : **dysfonction d'organe menaçant le pronostic vital, causée par une réponse dérégulée de l'hôte à une infection**. Opérationnellement : infection suspectée ou documentée **+ augmentation aiguë du score SOFA ≥ 2 points** (score de base supposé nul en l'absence de dysfonction préexistante connue) [S1, S4].
- **Choc septique** : sous-groupe du sepsis où les anomalies circulatoires et cellulaires/métaboliques sont assez profondes pour augmenter nettement la mortalité ; opérationnellement : **nécessité de vasopresseurs pour maintenir une PAM ≥ 65 mmHg** **et** **lactate > 2 mmol/L (> 18 mg/dL)** **malgré un remplissage adéquat** [S1, S4].
- Le terme « **sepsis sévère** » est **abandonné** ; les critères du **SRIS** (syndrome de réponse inflammatoire systémique) ne définissent plus le sepsis mais restent utilisés comme **outil de dépistage** [S1, S2].

### 1.2 Termes classiques (programme algérien : « états septicémiques »)
- **Bactériémie** : présence de bactéries viables dans le sang, attestée par une **hémoculture positive** ; elle peut être transitoire et asymptomatique (soins dentaires, par exemple).
- **Septicémie** (« état septicémique », définition classique) : décharges bactériennes répétées dans le sang **à partir d'un foyer** infectieux, avec un retentissement général — notion aujourd'hui intégrée dans le sepsis et la « bactériémie avec sepsis ».
- **Porte d'entrée** : site par lequel le micro-organisme a pénétré ; **foyer primitif** : site infectieux d'où partent les décharges ; **localisations secondaires (métastatiques)** : endocardite, abcès, spondylodiscite, arthrite.
- **SRIS** (anciennes définitions, 1991) : au moins 2 critères parmi température > 38 °C ou < 36 °C, FC > 90/min, FR > 20/min (ou PaCO₂ < 32 mmHg), leucocytes > 12 000 ou < 4 000/mm³ (ou > 10 % de formes immatures) `[À VÉRIFIER — libellés exacts]`.

### 1.3 Pourquoi c'est une urgence
Le sepsis est une **urgence médicale** : la mortalité augmente avec le **délai** d'administration des antibiotiques et de la réanimation, en particulier en cas de choc [S2, S4]. L'OMS rappelle que les **résultats des examens ne doivent pas retarder** les antibiotiques [S4].

## 2. Repères historiques

- 1914 : Schottmüller définit la septicémie comme un foyer d'où des germes pathogènes passent dans le sang de façon continue ou périodique `[À VÉRIFIER]`.
- 1991 : conférence de consensus ACCP/SCCM (SRIS, sepsis, sepsis sévère, choc septique) ; 2001 : révision (Sepsis-2) `[À VÉRIFIER]`.
- 2004 : premières recommandations de la *Surviving Sepsis Campaign* (SSC), révisées en 2008, 2012, 2016, **2021** et **2026** [S3].
- 2016 : **Sepsis-3** — définition fondée sur la **dysfonction d'organe** (SOFA) [S1].
- 2024 : **critères de Phoenix** pour le sepsis de l'enfant [S6].

## 3. Épidémiologie

- **Monde** (étude *Global Burden of Disease*, 2017) : environ **49 millions** de cas de sepsis et **11 millions** de décès liés au sepsis, la charge la plus lourde étant en **Afrique subsaharienne** ; près de **20 millions** de cas chez les enfants de moins de 5 ans ; la cause sous-jacente la plus fréquente de sepsis est la **diarrhée**, et la première cause de décès lié au sepsis les **infections respiratoires basses** [S4].
- **Sepsis maternel** : environ **12 millions** de nouveaux cas en 2017 ; troisième cause de mortalité maternelle dans le monde (2003–2009) [S4].
- La **résistance aux antibiotiques** complique de plus en plus la prise en charge, surtout dans les pays à revenu faible et intermédiaire [S4].
- **Algérie** : pas de données nationales de sepsis consultées `[À VÉRIFIER]` ; le **décret 22-250** a rendu à déclaration obligatoire les **infections à bactéries multirésistantes**, les **infections du site opératoire** et les **pneumopathies acquises sous ventilation mécanique** [S8] — témoins du poids des infections associées aux soins. Les données du réseau national de surveillance de la résistance (entérobactéries productrices de BLSE, carbapénémases, SARM) doivent orienter les choix probabilistes `[À VÉRIFIER]`.

## 4. Rappels physiologiques

- **Réponse de l'hôte** : reconnaissance de motifs microbiens (PAMP : lipopolysaccharide, peptidoglycane…) et de signaux de danger (DAMP) par les récepteurs de l'immunité innée (TLR…) → cytokines pro-inflammatoires (TNF-α, IL-1, IL-6), activation du complément et de la coagulation.
- **Endothélium** : régulation du tonus vasculaire (NO), de la perméabilité (glycocalyx) et de la coagulation ; il est au cœur des défaillances du sepsis.
- **Transport de l'oxygène** : DO₂ = débit cardiaque × contenu artériel en O₂ ; le **lactate** reflète un déséquilibre entre apports et besoins, mais aussi une production adrénergique et une clairance hépatique diminuée — ce n'est pas un marqueur exclusif d'hypoxie.

## 5. Physiopathologie

```text
INFECTION (porte d'entrée → foyer → décharges bactériennes)
   │
   ▼
Reconnaissance (PAMP/DAMP) → cascade inflammatoire ET anti-inflammatoire
   │
   ├─► Endothélium : vasodilatation (NO), fuite capillaire, altération du glycocalyx
   │        → HYPOVOLÉMIE relative + VASOPLÉGIE → hypotension (choc distributif)
   ├─► Coagulation : activation, consommation → CIVD, microthromboses
   ├─► Myocarde : dysfonction systolique/diastolique (cardiomyopathie septique)
   ├─► Microcirculation : shunts, hétérogénéité, hypoxie tissulaire
   ├─► Mitochondries : dysoxie cellulaire (« hibernation »)
   └─► Immunoparalysie secondaire → infections nosocomiales, réactivations virales
   │
   ▼
DYSFONCTIONS D'ORGANES : encéphalopathie, SDRA, insuffisance rénale aiguë,
cholestase, thrombopénie, iléus, hyperglycémie, acidose lactique → DÉCÈS
```

Points clés [S1, S4] : ce n'est pas la bactérie seule, mais la **réponse dérégulée de l'hôte** qui fait le sepsis ; elle associe hyper-inflammation précoce et immunodépression ; la **susceptibilité génétique** intervient aussi [S4].

## 6. Étiologies et facteurs de risque

### 6.1 Terrain [S4]
Âges extrêmes (nouveau-nés, personnes âgées), **immunodépression** (VIH, cancer, chimiothérapie, corticothérapie, immunosuppresseurs, asplénie), **cirrhose**, **alcoolisme**, **diabète mal équilibré**, **dispositifs invasifs** (cathéters, sondes), **dénutrition**, chirurgie récente, grossesse et post-partum.

### 6.2 Principaux foyers et micro-organismes

| Foyer (porte d'entrée) | Micro-organismes prédominants | Indices cliniques |
|---|---|---|
| **Urinaire** (pyélonéphrite, prostatite, obstacle) | *E. coli*, autres entérobactéries, entérocoque ; *Pseudomonas* si soins | Signes fonctionnels urinaires, lombalgie, sonde ; **obstacle à drainer** |
| **Pulmonaire** (pneumonie) | Pneumocoque, *Haemophilus*, *Legionella*, *S. aureus* ; BGN en réanimation | Toux, crépitants, hypoxémie |
| **Intra-abdominal** (péritonite, cholangite, abcès) | Entérobactéries, anaérobies (*Bacteroides*), entérocoques | Douleur, défense, ictère (triade de Charcot) ; **chirurgie / drainage** |
| **Peau et tissus mous** (dermohypodermite, fasciite nécrosante) | *S. pyogenes*, *S. aureus*, flore polymicrobienne | Douleur disproportionnée, nécrose, crépitation → **chirurgie** |
| **Cathéter vasculaire** | *S. aureus*, staphylocoques à coagulase négative, BGN, *Candida* | Cathéter, inflammation au point d'insertion |
| **Endocarde** | *S. aureus*, streptocoques, entérocoques | Souffle, emboles, terrain valvulaire |
| **Méninges / purpura** | Méningocoque, pneumocoque | Syndrome méningé, **purpura fulminans** (C3G immédiate) |
| **Gynéco-obstétrical** (post-partum, post-abortum) | Streptocoque A, entérobactéries, anaérobies | Endométrite, rétention |
| **Neutropénie fébrile** | Entérobactéries, *Pseudomonas aeruginosa*, staphylocoques, *Candida* | Chimiothérapie récente |
| **Asplénie** | Pneumocoque (infection fulminante), méningocoque, *Haemophilus* | Splénectomie, drépanocytose |

**Bactériémies « sans foyer » évident à évoquer en Algérie** : **fièvre typhoïde** (voir DOS-INFE-0003), **brucellose** (DOS-INFE-0002), staphylococcie maligne de la face (furoncle manipulé), **méningococcémie** ; et, devant une fièvre au retour du Sahel, le **paludisme grave** (DOS-INFE-0004), diagnostic différentiel ou associé.

## 7. Classifications

### 7.1 Niveaux de gravité

| Situation | Définition | Enjeu |
|---|---|---|
| **Infection non compliquée** | Pas de dysfonction d'organe | Traitement du foyer |
| **Sepsis** | Infection + ΔSOFA ≥ 2 | Urgence : antibiotiques rapides, réanimation |
| **Choc septique** | Vasopresseur pour PAM ≥ 65 mmHg + lactate > 2 mmol/L malgré le remplissage | Antibiotiques **dans l'heure**, réanimation |

### 7.2 Score SOFA (Sequential Organ Failure Assessment) — d'après [S1, S4]

| Système | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| **Respiratoire** PaO₂/FiO₂ (mmHg) | ≥ 400 | < 400 | < 300 | < 200 avec assistance ventilatoire | < 100 avec assistance ventilatoire |
| **Coagulation** plaquettes (/mm³) | ≥ 150 000 | < 150 000 | < 100 000 | < 50 000 | < 20 000 |
| **Foie** bilirubine (mg/dL) | < 1,2 | 1,2–1,9 | 2,0–5,9 | 6,0–11,9 | > 12,0 |
| **Cardiovasculaire** | PAM ≥ 70 mmHg | PAM < 70 mmHg | Dopamine < 5 ou dobutamine (toute dose) | Dopamine 5,1–15 ou adrénaline ≤ 0,1 ou noradrénaline ≤ 0,1 µg/kg/min | Dopamine > 15 ou adrénaline > 0,1 ou noradrénaline > 0,1 µg/kg/min |
| **Neurologique** Glasgow | 15 | 13–14 | 10–12 | 6–9 | < 6 |
| **Rénal** créatinine (mg/dL) ou diurèse | < 1,2 | 1,2–1,9 | 2,0–3,4 | 3,5–4,9 ou < 500 mL/j | > 5,0 ou < 200 mL/j |

Bornes conformes au tableau 24.1 du livre AWaRe [S4] (catécholamines administrées depuis au moins 1 h, doses en µg/kg/min ; créatinine 1,2 mg/dL ≈ 110 µmol/L, 2,0 ≈ 171, 3,5 ≈ 300, 5,0 ≈ 440 µmol/L).

### 7.3 Outils de repérage au lit du patient
- **qSOFA** (≥ 2 critères = risque élevé de mauvaise évolution hors réanimation) : **FR ≥ 22/min**, **altération de la conscience** (Glasgow < 15), **PAS ≤ 100 mmHg** [S1, S4]. Les scores de ce type n'ont pas été largement validés dans les pays à revenu faible et intermédiaire [S4].
- La **SSC 2021** recommande de **ne pas utiliser le qSOFA seul** comme outil de dépistage, en comparaison du SRIS, du **NEWS** ou du **MEWS** (recommandation forte, certitude modérée) [S2] ; la **SSC 2026** confirmerait cette position (recommandation forte) [S3] `[À VÉRIFIER — texte 2026]`.
- **NEWS2** : score d'alerte précoce recommandé par le NICE pour stratifier le risque chez l'adulte hospitalisé (mise à jour 2024) [S5] `[À VÉRIFIER — seuils]`.

### 7.4 Enfant — critères de Phoenix (2024) [S6]
- **Sepsis** : enfant **suspect d'infection** avec un **score de Phoenix ≥ 2** (dysfonction respiratoire, cardiovasculaire, de la coagulation et/ou neurologique).
- **Choc septique** : sepsis avec **au moins 1 point cardiovasculaire**.
- Remplacent les critères pédiatriques de 2005 fondés sur le SRIS.

## 8. Diagnostic positif — clinique

### 8.1 Reconnaître le sepsis
- **Signes infectieux** : fièvre ou **hypothermie** (< 36 °C, de mauvais pronostic), **frissons** (décharges bactériémiques), sueurs ; signes du foyer.
- **Signes de dysfonction d'organe** : **polypnée** (FR ≥ 22/min), **confusion**, agitation ou somnolence, **hypotension** (PAS ≤ 100 mmHg, PAM < 65), **tachycardie**, **oligurie** (< 0,5 mL/kg/h), **marbrures** (score de marbrures), **temps de recoloration capillaire allongé** (> 3 s), extrémités froides, ictère, purpura, saignements.
- **Terrain trompeur** : sujet âgé (confusion, chute, sans fièvre), immunodéprimé, corticothérapie, bêtabloquant (pas de tachycardie), nourrisson.

### 8.2 Rechercher systématiquement la porte d'entrée et le foyer
Examen complet « de la tête aux pieds » : peau (plaies, escarres, cellulite, purpura), points de ponction et **cathéters**, auscultation cardiaque (souffle → **endocardite**) et pulmonaire, abdomen, fosses lombaires, **toucher rectal** (prostatite), examen gynécologique, méninges, articulations et rachis.

### 8.3 Situations d'extrême urgence
- **Purpura fulminans** : C3G immédiate (voir DOS-INFE-0001).
- **Fasciite nécrosante**, péritonite, **pyélonéphrite obstructive**, cholangite : **contrôle chirurgical ou radiologique de la source**.
- **Neutropénie fébrile** : antibiothérapie anti-*Pseudomonas* sans délai.
- **Splénectomisé** fébrile : risque de sepsis fulminant à pneumocoque.

## 9. Examens complémentaires et interprétation

### 9.1 Microbiologie — **avant** les antibiotiques, **sans les retarder**
- **Hémocultures** : au moins **2 paires** (flacons aérobie et anaérobie), prélevées **avant** la première dose d'antibiotique **si cela ne retarde pas de façon substantielle** son administration (bonne pratique de la SSC 2016, rappelée dans le texte de 2021) [S2] ; volume suffisant (le rendement dépend du volume) ; prélèvement sur cathéter **et** en périphérie si infection de cathéter suspectée.
- **Prélèvements du foyer** : ECBU, prélèvements respiratoires (expectoration, aspiration, LBA), liquide pleural ou d'ascite, **LCR**, pus, prélèvements chirurgicaux, **antigénuries** pneumocoque et *Legionella* selon le contexte.
- **Paludisme** : frottis/TDR systématiques au retour d'une zone d'endémie.
- Interprétation : **staphylocoque doré** dans une seule hémoculture = toujours significatif ; staphylocoque à coagulase négative dans une seule paire = contamination probable (sauf matériel) ; **streptocoques, entérocoques, *S. aureus*** → rechercher une **endocardite** (échocardiographie).

### 9.2 Évaluation de la gravité
- **Lactate** artériel ou veineux : **mesure suggérée** par la SSC [S2] ; > 2 mmol/L = hypoperfusion (critère du choc avec le vasopresseur) ; à recontrôler pour guider la réanimation [S2] ; **> 4 mmol/L** = gravité marquée `[À VÉRIFIER]`.
- **Gaz du sang** (acidose, hypoxémie, PaO₂/FiO₂), **NFS** (hyperleucocytose ou **leucopénie**, thrombopénie), **hémostase** (TP, fibrinogène, D-dimères → CIVD), **créatinine**, **urée**, ionogramme, **bilirubine**, transaminases, **glycémie**, troponine si besoin.
- **CRP** et **procalcitonine** (PCT) : marqueurs d'inflammation et d'infection bactérienne, non spécifiques ; la SSC 2021 **suggère de ne pas utiliser** la PCT associée à l'évaluation clinique pour **décider de débuter** les antibiotiques, mais **suggère** de l'utiliser avec la clinique pour décider de leur **arrêt** [S2].

### 9.3 Imagerie (orientée par le foyer)
Radiographie thoracique ; **échographie** rénale et des voies urinaires (obstacle), abdominale et biliaire ; **scanner** thoraco-abdomino-pelvien (abcès, péritonite) ; échographie des parties molles ; **échocardiographie** (endocardite, fonction ventriculaire) ; échographie au lit (POCUS) pour l'évaluation hémodynamique. L'imagerie ne doit **jamais retarder** les antibiotiques.

## 10. Formes cliniques

### 10.1 Selon le micro-organisme

| Agent | Particularités |
|---|---|
| ***Staphylococcus aureus*** | Porte d'entrée cutanée ou cathéter ; localisations secondaires (endocardite, ostéo-articulaires, pulmonaires) ; **échocardiographie** systématique ; « staphylococcie maligne de la face » après manipulation d'un furoncle ; durée prolongée `[À VÉRIFIER — durées]` |
| **Entérobactéries** | Foyers urinaires et digestifs ; **BLSE** et carbapénémases à prendre en compte selon l'écologie locale [S4] |
| ***Pseudomonas aeruginosa*** | Neutropénie, infections associées aux soins, ventilation mécanique |
| **Streptocoque A** | Choc toxique, fasciite nécrosante, post-partum |
| **Méningocoque** | Purpura fulminans, méningite |
| **Anaérobies** | Foyers digestifs, gynécologiques, nécrosants |
| ***Candida*** | Réanimation, nutrition parentérale, cathéter, chirurgie digestive ; antifongique empirique si **risque élevé** (SSC) [S2] |

### 10.2 Selon le terrain
- **Personne âgée** : apyrexie fréquente, confusion, chute ; mortalité élevée.
- **Neutropénique** : signes inflammatoires frustes ; urgence absolue.
- **Cirrhotique** : infection du liquide d'ascite, hémorragie digestive.
- **Femme enceinte / post-partum** : sepsis maternel [S4].
- **Enfant** : critères de Phoenix [S6] ; remplissage prudent selon l'accès à la réanimation [S7] ; la SSC enfant 2026 remplace la version 2020 (contenu non lu) [S10].
- **Personne vivant avec le VIH** : pneumocoque, salmonelles non typhiques, tuberculose disséminée.

## 11. Diagnostics différentiels

| Situation mimant un sepsis | Éléments d'orientation |
|---|---|
| **Choc cardiogénique** (infarctus, myocardite) | ECG, troponine, échocardiographie (pressions de remplissage élevées) |
| **Choc hypovolémique / hémorragique** | Contexte, hémoglobine, pertes |
| **Embolie pulmonaire grave** | Dyspnée, cœur droit dilaté, D-dimères, angioscanner |
| **Anaphylaxie** | Exposition, urticaire, bronchospasme |
| **Pancréatite aiguë grave** | Lipase, scanner (SRIS non infectieux) |
| **Insuffisance surrénale aiguë** | Contexte, natrémie, kaliémie |
| **Intoxications** (salicylés, cocaïne…), **syndrome malin des neuroleptiques**, **coup de chaleur** | Anamnèse |
| **Paludisme grave** | Séjour en zone d'endémie, thrombopénie, frottis |
| **Hémopathie, syndrome d'activation macrophagique** | Cytopénies, ferritine, triglycérides |

## 12. Évolution, complications, pronostic

### 12.1 Complications
**Défaillances multiviscérales** (SDRA, insuffisance rénale aiguë, CIVD, encéphalopathie, cholestase, iléus), **localisations secondaires** (endocardite, abcès, spondylodiscite), **infections nosocomiales** secondaires (immunoparalysie), **complications thromboemboliques**, myopathie et neuropathie de réanimation, **séquelles cognitives et fonctionnelles** au long cours (« syndrome post-sepsis »).

### 12.2 Pronostic
- **Mortalité hospitalière** : **plus de 10 %** pour le sepsis (ΔSOFA ≥ 2) et **plus de 40 %** pour le choc septique dans les cohortes ayant servi à Sepsis-3 [S1].
- **Facteurs pronostiques** : nombre et sévérité des dysfonctions (**SOFA**, ΔSOFA), **lactate** élevé et sa non-décroissance, **choc**, retard aux antibiotiques ou antibiothérapie **inadaptée** (micro-organisme résistant), absence de **contrôle de la source**, âge, comorbidités, immunodépression [S1, S2].
- Hors réanimation, un **qSOFA ≥ 2** identifie des patients à plus haut risque de décès ou de séjour prolongé en réanimation [S1, S9] ; un **NEWS2** élevé signale un risque élevé de dégradation [S5].

## 13. Traitement

### 13.1 Objectifs
1. **Éradiquer l'infection** : antibiothérapie **précoce et adaptée**, **contrôle de la source** [S2, S4].
2. **Restaurer la perfusion tissulaire** : remplissage, vasopresseurs (PAM ≥ 65 mmHg) [S2].
3. **Suppléer les organes défaillants** (ventilation, épuration extrarénale).
4. **Prévenir** les complications de réanimation et **préserver** l'écologie (désescalade, durée courte) [S2].

### 13.2 Moyens et délais

**a) Antibiothérapie — délais (SSC 2021) [S2]**
- **Choc septique possible ou sepsis probable** : antibiotiques **immédiatement, idéalement dans l'heure** suivant la reconnaissance.
- **Sepsis possible sans choc** : évaluation rapide (cause infectieuse ou non) ; si la suspicion persiste, antibiotiques **dans les 3 heures**.
- **Faible probabilité d'infection sans choc** : différer les antibiotiques en poursuivant la surveillance (suggestion).
- Couvrir le **SARM** si le risque est élevé (bonne pratique) ; **deux molécules actives sur les bacilles à Gram négatif** si **risque élevé de multirésistance** (suggestion) ; **antifongique** empirique si risque fongique élevé (suggestion) [S2].
- **Perfusion prolongée** des bêta-lactamines en entretien (après une dose de charge) suggérée [S2].

**b) Antibiothérapie probabiliste selon le foyer — options de l'OMS (livre AWaRe 2022, adulte, fonction rénale normale ; options citées par ordre alphabétique, considérées comme équivalentes) [S4]**

| Foyer | Options de l'OMS | Durée indicative (OMS) |
|---|---|---|
| **Sepsis sans foyer identifié** | **Céfotaxime 2 g/8 h IV** ou **ceftriaxone 2 g/24 h IV**, **associée à** **amikacine 15 mg/kg/24 h IV** ou **gentamicine 5 mg/kg/24 h IV** (l'amikacine garde une activité sur les souches BLSE : option d'épargne des carbapénèmes) | 7 jours |
| **Méningite** | 1er choix : **céfotaxime 2 g/6 h** ou **ceftriaxone 2 g/12 h** IV ; 2e choix : amoxicilline ou ampicilline 2 g/4 h, benzylpénicilline 4 MUI/4 h, chloramphénicol 1 g/6 h (en dernier recours) | 10 jours (variable) |
| **Infection respiratoire basse** | **Céfotaxime 2 g/8 h** ou **ceftriaxone 2 g/24 h** **+ clarithromycine 500 mg/12 h** IV | 5 jours |
| **Infection intra-abdominale** | **C3G + métronidazole 500 mg/8 h** ou **pipéracilline-tazobactam 4 g/0,5 g toutes les 6 h** ; 2e choix (seulement là où les BLSE sont fréquentes) : **méropénem 2 g/8 h** (dose du tableau du sepsis ; 1 g/8 h dans le chapitre des infections intra-abdominales hors sepsis) | ≈ 7 jours si contrôle de la source |
| **Peau et tissus mous** | **Ceftriaxone 2 g/24 h + métronidazole 500 mg/8 h** (si *S. pyogenes* exclu en cas de fasciite) ou **pipéracilline-tazobactam + clindamycine 900 mg/8 h** (option préférée si fasciite nécrosante) ; **+ vancomycine 15–20 mg/kg/12 h** si SARM suspecté | ≈ 7 jours |
| **Infection urinaire** | **Céfotaxime 2 g/8 h** ou **ceftriaxone 2 g/24 h** **+ amikacine 15 mg/kg/24 h** | 7 jours |
| **Fièvre entérique** | **Ceftriaxone 2 g/24 h** (attention à la résistance croissante) | 10 jours |

> Ces schémas de l'OMS sont des options « de santé publique » ; ils doivent être **adaptés à l'écologie locale** (BLSE, *Pseudomonas*, SARM, carbapénémases), au terrain (neutropénie, soins récents) et aux **protocoles de l'établissement** ; aucun protocole national algérien d'antibiothérapie probabiliste du sepsis n'a été retrouvé pendant l'audit `[À VÉRIFIER]`. Les doses supposent une fonction rénale normale ; les aminosides se donnent en **dose unique journalière**, avec surveillance de la fonction rénale.

**c) Contrôle de la source** [S2]
- Identifier ou éliminer **rapidement** un foyer nécessitant un geste (abcès, péritonite, cholangite, obstacle urinaire, fasciite nécrosante, matériel infecté) et réaliser le geste **dès que possible sur le plan médical et logistique** (bonne pratique) ; **retirer les cathéters** suspects une fois un autre accès obtenu (bonne pratique).
- Exemples : **dérivation des urines** (sonde JJ, néphrostomie) d'une pyélonéphrite obstructive ; **drainage biliaire** (CPRE) d'une cholangite ; **laparotomie** d'une péritonite ; **débridement** d'une fasciite.

**d) Réanimation hémodynamique** (détails : DOS-MINT_REA-0001) [S2, S3]
- **Remplissage** par **cristalloïdes** : **au moins 30 mL/kg dans les 3 premières heures** en cas d'hypoperfusion ou de choc (suggestion, faible niveau de certitude) [S2] ; suggestion maintenue en 2026, avec un **poids ajusté** en cas d'IMC > 30 [S3] `[À VÉRIFIER]` ; **solutés balancés** préférés au sérum salé isotonique (suggestion) ; **albumine** si grands volumes ; **pas d'hydroxyéthylamidons** (recommandation forte) ni de gélatines (suggestion) [S2] ; guider le remplissage par des **indices dynamiques**, le **temps de recoloration capillaire** et la décroissance du **lactate** [S2].
- **PAM cible initiale 65 mmHg** (recommandation) [S2].
- **Noradrénaline en première intention** [S2] ; ajout de **vasopressine** plutôt qu'escalade de la noradrénaline (en pratique quand la noradrénaline atteint 0,25–0,5 µg/kg/min) [S2] ; en cas de **dysfonction cardiaque** avec hypoperfusion persistante : **dobutamine** ajoutée à la noradrénaline **ou adrénaline seule** (suggestion) [S2, S3] ; début possible des vasopresseurs sur **voie périphérique** plutôt que d'attendre une voie centrale (suggestion) [S2]. `[POSOLOGIE À VÉRIFIER — protocole local de la noradrénaline (base/tartrate)]`
- **Hydrocortisone 200 mg/j** (50 mg IV toutes les 6 h ou perfusion continue) si besoin persistant de vasopresseurs, à partir d'une dose de **noradrénaline ou d'adrénaline ≥ 0,25 µg/kg/min au moins 4 h après le début** du vasopresseur (suggestion) [S2] ; niveau de certitude abaissé en 2026 [S3] `[À VÉRIFIER]`.

**e) Autres mesures (SSC 2021)** [S2]
Oxygénation et ventilation protectrice (volume courant 6 mL/kg de poids idéal, pression de plateau ≤ 30 cmH₂O, décubitus ventral si SDRA modéré à sévère) ; **transfusion** si Hb < 7 g/dL ; **bicarbonate** seulement si pH ≤ 7,20 avec insuffisance rénale aiguë ; **insulinothérapie** si glycémie ≥ 180 mg/dL (10 mmol/L), cible 144–180 mg/dL ; **prévention thromboembolique** par HBPM ; prévention de l'ulcère de stress si facteurs de risque ; **pas de vitamine C** ; nutrition entérale précoce ; information des familles et suivi post-sepsis.

### 13.3 Stratégie de la première heure

```text
SUSPICION D'INFECTION + SIGNE(S) DE GRAVITÉ (NEWS2 élevé, SIRS, qSOFA ≥ 2,
lactate > 2, PAS ≤ 100, confusion, marbrures, oligurie)
│
├─ 0 min : alerter, monitorer, O2 si SpO2 basse, 2 voies veineuses
├─ ≤ 45 min : hémocultures (2 paires) + prélèvements du foyer + lactate,
│            gaz du sang, NFS, hémostase, créatinine, bilirubine
├─ ≤ 60 min : ANTIBIOTHÉRAPIE IV probabiliste selon :
│            foyer présumé + lieu d'acquisition (communautaire / soins)
│            + terrain (neutropénie, immunodépression) + risque BMR/SARM
├─ Hypotension ou lactate ≥ 4 : cristalloïdes 30 mL/kg (≤ 3 h), réévaluer
├─ PAM < 65 malgré remplissage : NORADRÉNALINE (voie périphérique possible)
│     → choc septique (si lactate > 2) → réanimation
├─ CONTRÔLE DE LA SOURCE : imagerie ciblée, geste dès que possible
└─ Réévaluation H6–H12 puis quotidienne : lactate, diurèse, SOFA
      → J2–J3 : résultats microbiologiques → DÉSESCALADE, durée courte,
        relais oral si possible, PCT pour décider de l'arrêt
```
Sources : [S2] (délais, réanimation, désescalade) ; [S4] (choix des molécules) ; délais en minutes indicatifs `[À VÉRIFIER]`.

### 13.4 Particularités algériennes
- **Écologie bactérienne** : les entérobactéries productrices de **BLSE** et la diffusion de **carbapénémases** dans les hôpitaux du Maghreb imposent de connaître les **données locales** avant de choisir une C3G seule `[À VÉRIFIER — données du réseau national de surveillance de la résistance]`.
- **Déclaration obligatoire** des infections à **bactéries multirésistantes**, des **infections du site opératoire** et des **pneumopathies acquises sous ventilation** [S8] ; comités de lutte contre les infections nosocomiales `[À VÉRIFIER]`.
- Disponibilité de la noradrénaline, de la vasopressine, de l'hydrocortisone injectable, des carbapénèmes et de la **colistine** variable selon les établissements `[À VÉRIFIER]`.
- Penser aux étiologies **endémiques** : typhoïde, brucellose, méningococcie, paludisme d'importation au Sud, leptospirose, rickettsioses.

## 14. Surveillance

| Domaine | Paramètres |
|---|---|
| **Hémodynamique** | PA (PAM ≥ 65), FC, marbrures, TRC, diurèse horaire, **lactate** (décroissance), échocardiographie |
| **Organes** | Glasgow, SpO₂, PaO₂/FiO₂, créatinine, bilirubine, plaquettes, hémostase → **SOFA quotidien** |
| **Infection** | Température, foyer, **hémocultures de contrôle** (*S. aureus*, candidémie), résultats microbiologiques à **48–72 h** |
| **Antibiotiques** | **Réévaluation quotidienne** de la désescalade (suggestion SSC) ; dosages des aminosides et de la vancomycine ; fonction rénale ; durée **courte** plutôt que longue (suggestion) ; PCT pour décider de l'arrêt [S2] |
| **Complications** | Thrombose, saignements, infections nosocomiales, escarres, dénutrition |
| **Après la sortie** | Évaluation fonctionnelle, cognitive et psychologique (syndrome post-sepsis) [S2] |

## 15. Prévention

- **Vaccinations** : pneumocoque, *Haemophilus* b, méningocoque (calendrier national, sujets aspléniques), grippe `[À VÉRIFIER — recommandations nationales adultes]`.
- **Prévention des infections associées aux soins** : hygiène des mains, asepsie et retrait précoce des **cathéters** et **sondes**, prévention des pneumopathies sous ventilation, antibioprophylaxie chirurgicale adaptée ; surveillance des **BMR** [S8].
- **Bon usage des antibiotiques** (classification AWaRe : privilégier les antibiotiques *Access*, réserver les *Reserve*) [S4].
- **Éducation** des patients à risque (splénectomisés, neutropéniques, cirrhotiques) : consulter en urgence en cas de fièvre.
- **Reconnaissance précoce** dans les services (scores d'alerte, protocoles de type « code sepsis ») [S2, S5].

## 16. Algorithme diagnostique et pronostique

```text
PATIENT FÉBRILE (ou hypotherme) avec suspicion d'infection
│
├─ Dépistage : NEWS2 / SIRS / qSOFA (le qSOFA seul ne suffit pas pour exclure)
│
├─ Dysfonction d'organe ? (ΔSOFA ≥ 2 : PaO2/FiO2, plaquettes, bilirubine,
│   PAM/vasopresseurs, Glasgow, créatinine/diurèse)
│     ├─ NON → infection sans sepsis : traiter le foyer, surveiller
│     └─ OUI → SEPSIS
│            ├─ Vasopresseur nécessaire pour PAM ≥ 65 après remplissage
│            │   ET lactate > 2 mmol/L → CHOC SEPTIQUE
│            └─ Sinon → sepsis sans choc
│
├─ Foyer ? → examen complet + imagerie ciblée → contrôle de la source
│
└─ Pronostic : SOFA, lactate et sa cinétique, délai et adéquation des
   antibiotiques, contrôle de la source, terrain
```
Sources : [S1, S2, S5].

---

## 17. Cas clinique commenté

<!--CAS17:start-->
> Cas repris de la banque `20_CAS_CLINIQUES/lots/DOS-02-lot2.json` (un second cas, `CAS-INFE-0208`, y figure également).

**Fièvre, ictère et hypotension chez un diabétique de 64 ans** — *scénario fictif* (`CAS-INFE-0207`, niveau residanat)

**Présentation.** Scénario fictif : homme, 64 ans, retraité, diabétique de type 2 sous metformine, porteur d'une lithiase vésiculaire connue. Amené aux urgences pour fièvre à 39,8 °C avec frissons, douleur de l'hypochondre droit et confusion depuis 12 heures.

**Antécédents.** Diabète de type 2, HTA traitée par IEC. Hospitalisé il y a 2 mois (antibiothérapie par amoxicilline-acide clavulanique pour pneumonie).

**Histoire et symptômes.** Douleur de l'hypochondre droit depuis 3 jours, puis fièvre avec frissons, urines foncées, ictère apparu la veille, somnolence.

**Examen clinique.** T 39,6 °C, FC 122/min, PA 82/46 mmHg (PAM 58), FR 26/min, SpO2 93 % en air ambiant, Glasgow 13 ; marbrures des genoux, TRC 4 s ; ictère cutanéo-muqueux ; défense de l'hypochondre droit ; diurèse 20 mL sur la première heure.

**Biologie.** Lactate 4,8 mmol/L (N < 2) ; leucocytes 18 600/mm3 ; plaquettes 88 000/mm3 ; bilirubine totale 82 µmol/L (4,8 mg/dL) ; ALAT 4 × N ; GGT 9 × N ; lipase normale ; créatinine 196 µmol/L (2,2 mg/dL ; base 80 µmol/L) ; PaO2/FiO2 290 ; CRP 280 mg/L ; glycémie 14 mmol/L. Hémocultures (2 paires) : E. coli producteur de BLSE à H20, résistant à la ceftriaxone, sensible à l'amikacine et au méropénem.

**Imagerie.** Échographie au lit : voie biliaire principale dilatée (12 mm) avec calcul enclavé dans le bas cholédoque ; vésicule lithiasique.

**Question 1 — Ce patient est-il en choc septique ?**
> Oui après remplissage : hypotension persistante nécessitant de la noradrénaline pour une PAM ≥ 65 mmHg avec un lactate > 2 mmol/L (Sepsis-3).

**Question 2 — Quel est le geste clé en dehors des antibiotiques ?**
> Le drainage biliaire en urgence (CPRE) : contrôle de la source dès que possible sur le plan médical et logistique (SSC 2021).

**Question 3 — Pourquoi envisager d'emblée une molécule active sur les BLSE ?**
> Antibiothérapie récente et hospitalisation récente augmentent le risque d'entérobactérie BLSE, et le choc rend toute inadéquation initiale très délétère ; la stratégie dépend de l'écologie locale.

**Question 4 — Quand ajouter l'hydrocortisone ?**
> Si le besoin en noradrénaline (ou adrénaline) atteint au moins 0,25 µg/kg/min au moins 4 h après le début du vasopresseur : hydrocortisone 200 mg/j.

**Diagnostic retenu.** Choc septique (vasopresseur nécessaire pour PAM ≥ 65 mmHg et lactate > 2 mmol/L) compliquant une angiocholite lithiasique à E. coli BLSE ; SOFA augmenté de ≥ 2 points (hémodynamique, rein, plaquettes, foie, conscience).

**Traitement.** Dans l'heure : hémocultures puis antibiothérapie IV probabiliste ; compte tenu d'une antibiothérapie récente et d'un risque de BLSE, une option active sur les BLSE est justifiée d'emblée (par exemple méropénem 2 g toutes les 8 h IV, ou C3G + métronidazole 500 mg/8 h associée à l'amikacine 15 mg/kg en une injection, selon l'écologie locale — doses de l'OMS pour l'adulte, première dose pleine puis adaptation à la fonction rénale) ; cristalloïdes balancés 30 mL/kg dans les 3 premières heures, puis noradrénaline pour PAM ≥ 65 mmHg ; drainage biliaire en urgence (CPRE avec sphinctérotomie et extraction ou prothèse) dès la stabilisation ; arrêt de la metformine et de l'IEC ; insuline si glycémie ≥ 10 mmol/L ; hydrocortisone 200 mg/j si la noradrénaline dépasse 0,25 µg/kg/min au-delà de 4 h ; adaptation à l'antibiogramme (méropénem ou relais selon la sensibilité) ; déclaration de l'infection à BMR.

**Surveillance.** PAM, lactate à 2–4 h, diurèse horaire, Glasgow, SOFA quotidien, bilan hépatique et rénal, hémocultures, tolérance de l'amikacine ou des carbapénèmes ; réévaluation de l'antibiothérapie à 48–72 h.

**Évolution.** CPRE à H8 : extraction d'un calcul et issue de bile purulente ; sevrage de la noradrénaline à H36 ; lactate normalisé à H24 ; méropénem poursuivi puis durée totale courte (environ 7 jours après le drainage) ; cholécystectomie programmée à distance.

**Commentaire pédagogique.** Le cas illustre les définitions de Sepsis-3 (sepsis et choc septique), la recherche de la porte d'entrée, l'urgence du contrôle de la source (drainage biliaire), la prise en compte du risque de BLSE (antibiothérapie récente) et la séquence de réanimation (cristalloïdes, noradrénaline, hydrocortisone selon la dose), ainsi que la désescalade et la déclaration des BMR en Algérie.

<!--CAS17:end-->

---

## 18. Points clés à retenir

1. **Sepsis (Sepsis-3)** = dysfonction d'organe menaçant le pronostic vital due à une réponse dérégulée de l'hôte à une infection ; **ΔSOFA ≥ 2** [S1].
2. **Choc septique** = vasopresseur pour **PAM ≥ 65 mmHg** **et lactate > 2 mmol/L** malgré un remplissage adéquat [S1].
3. Le **qSOFA** (FR ≥ 22, conscience altérée, PAS ≤ 100) est un outil pronostique, **non un outil de dépistage isolé** (SSC 2021, confirmé en 2026) [S2, S3].
4. **Hémocultures avant antibiotiques, sans retarder** ceux-ci [S2, S4].
5. **Antibiotiques dans l'heure** si choc ou sepsis probable ; dans les **3 heures** si sepsis possible sans choc après évaluation [S2].
6. Choix probabiliste guidé par le **foyer**, le **lieu d'acquisition**, le **terrain** et le **risque de BMR** ; options OMS : **C3G + aminoside** (sans foyer, urinaire), **C3G + métronidazole** ou pipéracilline-tazobactam (abdomen), **C3G + clarithromycine** (poumon) [S4].
7. **Contrôle de la source** dès que possible (drainage, chirurgie, retrait de cathéter) [S2].
8. Réanimation : **cristalloïdes balancés 30 mL/kg en 3 h**, **PAM 65**, **noradrénaline**, ± vasopressine, **hydrocortisone 200 mg/j** si choc réfractaire (NA ≥ 0,25 µg/kg/min) [S2].
9. **Désescalade**, **durée courte**, PCT pour l'arrêt [S2].
10. Enfant : **critères de Phoenix** (score ≥ 2 ; choc = ≥ 1 point cardiovasculaire) [S6] ; Algérie : **BMR, ISO et PAVM à déclaration obligatoire** [S8].

## 19. Pièges classiques à l'examen

- Définir encore le sepsis par le **SRIS** ou parler de « sepsis sévère » (abandonné par Sepsis-3) [S1].
- Attendre un **qSOFA ≥ 2** pour évoquer un sepsis [S2].
- **Retarder les antibiotiques** pour attendre l'imagerie, la PL ou les résultats [S2, S4].
- Oublier le **contrôle de la source** (pyélonéphrite obstructive, angiocholite, fasciite) : les antibiotiques seuls ne suffisent pas [S2].
- Utiliser des **hydroxyéthylamidons** (proscrits) ou débuter la **dopamine** en première intention [S2].
- Confondre la **dose** de noradrénaline exprimée en **base** et en **tartrate** (facteur ≈ 2) `[À VÉRIFIER — protocole local]`.
- Négliger une hémoculture à ***S. aureus*** (jamais une contamination) et oublier l'**échocardiographie**.
- Ne pas **réévaluer** l'antibiothérapie à 48–72 h (désescalade) ou la prolonger inutilement [S2].
- Chez un patient revenant du Sahel, omettre le **frottis** (paludisme grave).
- Prescrire une **C3G seule** dans un service où les entérobactéries **BLSE** sont fréquentes, chez un patient à risque `[À VÉRIFIER — écologie locale]`.

---

## 20. QCM d'auto-évaluation (corrigés commentés)

<!--QCM20:start-->
> 10 QCM originaux Mediverse (cinq propositions A–E ; QCM = une ou plusieurs réponses exactes, QCS = une seule). La banque complète de l'item (13 questions : `QCM-INFE-0240` à `QCM-INFE-0252`) figure dans `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/DOS-02-lot2.json`.

### QCM 1 — Définitions — bactériémie, septicémie, sepsis (QCM, difficulté 1/3)

Concernant la terminologie des états infectieux graves, quelles propositions sont exactes ?

- **A.** Une bactériémie correspond à la présence de bactéries viables dans le sang, attestée par une hémoculture positive.
- **B.** Selon Sepsis-3, le sepsis est une dysfonction d'organe menaçant le pronostic vital liée à une réponse dérégulée de l'hôte à une infection.
- **C.** Le terme « sepsis sévère » a été conservé par Sepsis-3 pour désigner le sepsis avec hypotension.
- **D.** Les critères du SRIS ne définissent plus le sepsis mais peuvent servir au dépistage.
- **E.** Une bactériémie transitoire peut être asymptomatique.

**Réponse(s) exacte(s) : A, B, D, E**

*Corrigé commenté.* Sepsis-3 (2016) définit le sepsis par la dysfonction d'organe (ΔSOFA ≥ 2) liée à une réponse dérégulée de l'hôte ; le terme « sepsis sévère » est abandonné ; le SRIS reste un outil de repérage. La bactériémie est un constat microbiologique, parfois transitoire et sans conséquence.

- A — Vrai.
- B — Vrai.
- C — Faux : terme abandonné.
- D — Vrai.
- E — Vrai : par exemple après des soins dentaires.

*Banque : `QCM-INFE-0240`*

### QCM 2 — Score SOFA (QCM, difficulté 2/3)

Quels paramètres font partie du score SOFA utilisé pour définir le sepsis ?

- **A.** Rapport PaO2/FiO2.
- **B.** Numération plaquettaire.
- **C.** Bilirubinémie.
- **D.** Lactatémie.
- **E.** Créatininémie ou diurèse.

**Réponse(s) exacte(s) : A, B, C, E**

*Corrigé commenté.* Le SOFA explore six systèmes : respiratoire (PaO2/FiO2), coagulation (plaquettes), foie (bilirubine), cardiovasculaire (PAM, catécholamines), neurologique (Glasgow), rénal (créatinine ou diurèse). Le lactate n'en fait pas partie ; il intervient dans la définition du choc septique.

- A — Vrai.
- B — Vrai.
- C — Vrai.
- D — Faux : critère du choc septique, non du SOFA.
- E — Vrai.

> Piège : Confondre les composantes du SOFA avec les critères du choc septique.

*Banque : `QCM-INFE-0241`*

### QCM 3 — Outils de dépistage (QCM, difficulté 2/3)

Concernant le qSOFA et les outils de repérage du sepsis, quelles propositions sont exactes ?

- **A.** Le qSOFA comprend une fréquence respiratoire ≥ 22/min, une altération de la conscience et une PAS ≤ 100 mmHg.
- **B.** Un qSOFA ≥ 2 hors réanimation identifie des patients à risque accru de mauvaise évolution.
- **C.** La SSC 2021 recommande de ne pas utiliser le qSOFA comme outil de dépistage unique, en comparaison du SIRS, du NEWS ou du MEWS.
- **D.** Un qSOFA à 0 permet d'exclure un sepsis.
- **E.** Le NICE recommande le score NEWS2 pour stratifier le risque chez l'adulte hospitalisé.

**Réponse(s) exacte(s) : A, B, C, E**

*Corrigé commenté.* Le qSOFA est un outil pronostique simple, peu sensible : il ne doit pas être utilisé seul pour dépister (SSC 2021, recommandation forte maintenue en 2026). Le NICE utilise le NEWS2. Un qSOFA négatif n'exclut pas un sepsis.

- A — Vrai.
- B — Vrai.
- C — Vrai.
- D — Faux : sensibilité insuffisante.
- E — Vrai : mise à jour 2024 de la NG51.

*Banque : `QCM-INFE-0242`*

### QCM 4 — Prélèvements microbiologiques (QCM, difficulté 2/3)

Concernant les prélèvements microbiologiques au cours d'un sepsis, quelles propositions sont exactes ?

- **A.** Les hémocultures doivent être prélevées avant les antibiotiques si cela ne retarde pas leur administration.
- **B.** Une hémoculture positive à Staphylococcus aureus doit toujours être considérée comme significative.
- **C.** Une bactériémie à S. aureus, à streptocoque ou à entérocoque doit faire rechercher une endocardite.
- **D.** Un staphylocoque à coagulase négative dans une seule paire chez un patient sans matériel est le plus souvent une contamination.
- **E.** La sensibilité des hémocultures est indépendante du volume de sang prélevé.

**Réponse(s) exacte(s) : A, B, C, D**

*Corrigé commenté.* Hémocultures (au moins 2 paires) avant les antibiotiques sans les retarder ; S. aureus n'est jamais un contaminant ; streptocoques, entérocoques et S. aureus imposent la recherche d'une endocardite ; les staphylocoques à coagulase négative isolés une seule fois sont souvent des contaminants ; le rendement dépend du volume prélevé.

- A — Vrai.
- B — Vrai.
- C — Vrai : échocardiographie.
- D — Vrai.
- E — Faux : le volume est un déterminant majeur du rendement.

*Banque : `QCM-INFE-0243`*

### QCM 5 — Délai de l'antibiothérapie (SSC 2021) (QCM, difficulté 2/3)

Selon la Surviving Sepsis Campaign 2021, quelles propositions concernant le délai d'administration des antibiotiques sont exactes ?

- **A.** En cas de choc septique possible ou de sepsis probable, les antibiotiques sont administrés immédiatement, idéalement dans l'heure.
- **B.** En cas de sepsis possible sans choc, une évaluation rapide est réalisée et, si la suspicion persiste, les antibiotiques sont donnés dans les 3 heures.
- **C.** Chez un patient sans choc avec une faible probabilité d'infection, il est suggéré de différer les antibiotiques en poursuivant la surveillance.
- **D.** La procalcitonine est recommandée pour décider du début de l'antibiothérapie.
- **E.** Les résultats de l'imagerie doivent être obtenus avant la première dose d'antibiotique.

**Réponse(s) exacte(s) : A, B, C**

*Corrigé commenté.* La SSC 2021 propose une approche graduée selon la probabilité d'infection et la présence d'un choc : ≤ 1 h (choc ou sepsis probable), ≤ 3 h (sepsis possible sans choc), report possible si faible probabilité. Elle suggère de ne pas utiliser la PCT pour décider du début des antibiotiques ; l'imagerie ne doit pas retarder le traitement.

- A — Vrai.
- B — Vrai.
- C — Vrai.
- D — Faux : utilisation suggérée pour l'arrêt, non pour le début.
- E — Faux.

*Banque : `QCM-INFE-0244`*

### QCM 6 — Antibiothérapie probabiliste — foyer intra-abdominal (QCM, difficulté 2/3)

Un patient présente un choc septique sur péritonite communautaire. Parmi les options proposées par l'OMS (livre AWaRe 2022), lesquelles sont exactes ?

- **A.** Céfotaxime 2 g toutes les 8 h IV + métronidazole 500 mg toutes les 8 h IV.
- **B.** Ceftriaxone 2 g/24 h IV + métronidazole 500 mg toutes les 8 h IV.
- **C.** Pipéracilline-tazobactam 4 g/0,5 g toutes les 6 h IV.
- **D.** Méropénem en deuxième choix lorsque des entérobactéries productrices de BLSE sont à craindre.
- **E.** Amoxicilline orale seule.

**Réponse(s) exacte(s) : A, B, C, D**

*Corrigé commenté.* Pour les infections intra-abdominales graves, l'OMS propose C3G + métronidazole ou pipéracilline-tazobactam en premier choix, et le méropénem en second choix (activité sur les BLSE). Le contrôle chirurgical de la source reste indispensable.

- A — Vrai.
- B — Vrai.
- C — Vrai.
- D — Vrai.
- E — Faux : inadaptée à une péritonite avec choc.

*Banque : `QCM-INFE-0245`*

### QCM 7 — Sepsis sans foyer identifié (QCM, difficulté 2/3)

Selon l'OMS (AWaRe 2022), quelle est l'approche probabiliste d'un sepsis de l'adulte sans foyer identifié (fonction rénale normale) ?

- **A.** Céfotaxime 2 g/8 h ou ceftriaxone 2 g/24 h IV.
- **B.** Associée à l'amikacine 15 mg/kg/24 h ou à la gentamicine 5 mg/kg/24 h IV.
- **C.** L'amikacine conserve une activité sur de nombreuses souches productrices de BLSE et constitue une option d'épargne des carbapénèmes.
- **D.** Durée indicative de 7 jours.
- **E.** La vancomycine doit être associée systématiquement.

**Réponse(s) exacte(s) : A, B, C, D**

*Corrigé commenté.* Pour le sepsis sans foyer, l'OMS propose une C3G associée à un aminoside en dose unique journalière, 7 jours ; la vancomycine n'est ajoutée qu'en cas de suspicion de SARM (par exemple infection cutanée).

- A — Vrai.
- B — Vrai.
- C — Vrai.
- D — Vrai.
- E — Faux : seulement si SARM suspecté.

*Banque : `QCM-INFE-0246`*

### QCM 8 — Contrôle de la source (QCS, difficulté 1/3)

Une femme de 55 ans présente un choc septique sur pyélonéphrite avec une dilatation pyélocalicielle droite due à un calcul urétéral. En plus de l'antibiothérapie et de la réanimation, quelle mesure est prioritaire ?

- **A.** Une échographie de contrôle à J7.
- **B.** Le drainage urgent des urines en amont de l'obstacle (sonde JJ ou néphrostomie).
- **C.** La lithotritie extracorporelle immédiate.
- **D.** L'attente des résultats de l'antibiogramme avant tout geste.
- **E.** Une corticothérapie à forte dose.

**Réponse(s) exacte(s) : B**

*Corrigé commenté.* La pyélonéphrite obstructive est une urgence de contrôle de la source : drainage des urines (sonde double J ou néphrostomie percutanée) dès que possible, le traitement du calcul étant différé.

- A — Faux : retard inacceptable.
- B — Vrai.
- C — Faux : contre-indiquée en phase infectieuse.
- D — Faux.
- E — Faux : hors indication (l'hydrocortisone ne concerne que le choc réfractaire).

> Piège : Croire que les antibiotiques suffisent en présence d'un obstacle.

*Banque : `QCM-INFE-0247`*

### QCM 9 — Remplissage vasculaire (QCM, difficulté 2/3)

Concernant le remplissage initial au cours d'un sepsis avec hypoperfusion selon la SSC 2021, quelles propositions sont exactes ?

- **A.** Il est suggéré d'administrer au moins 30 mL/kg de cristalloïdes dans les 3 premières heures.
- **B.** Les solutés balancés sont suggérés de préférence au sérum salé isotonique.
- **C.** Les hydroxyéthylamidons sont recommandés en cas de choc.
- **D.** L'albumine peut être utilisée chez les patients ayant reçu de grands volumes de cristalloïdes.
- **E.** La réévaluation repose sur des indices dynamiques, le temps de recoloration capillaire et l'évolution du lactate.

**Réponse(s) exacte(s) : A, B, D, E**

*Corrigé commenté.* SSC 2021 : ≥ 30 mL/kg de cristalloïdes en 3 h (suggestion, certitude faible ; maintenue en 2026 avec un poids ajusté si IMC > 30), solutés balancés, albumine si grands volumes, pas d'hydroxyéthylamidons (recommandation forte), réévaluation dynamique.

- A — Vrai.
- B — Vrai.
- C — Faux : proscrits (recommandation forte contre).
- D — Vrai.
- E — Vrai.

*Banque : `QCM-INFE-0248`*

### QCM 10 — Vasopresseurs et corticoïdes (QCM, difficulté 3/3)

Concernant le traitement du choc septique de l'adulte (SSC 2021), quelles propositions sont exactes ?

- **A.** La cible initiale de PAM est de 65 mmHg.
- **B.** La noradrénaline est le vasopresseur de première intention.
- **C.** L'ajout de vasopressine est suggéré plutôt que l'escalade de la noradrénaline.
- **D.** L'hydrocortisone 200 mg/j est suggérée si la noradrénaline ou l'adrénaline atteint au moins 0,25 µg/kg/min au moins 4 heures après le début du vasopresseur.
- **E.** La dopamine est préférée à la noradrénaline chez le sujet âgé.

**Réponse(s) exacte(s) : A, B, C, D**

*Corrigé commenté.* PAM 65 mmHg ; noradrénaline en première ligne ; vasopressine ajoutée (en pratique vers 0,25–0,5 µg/kg/min de noradrénaline) ; dobutamine ou adrénaline en cas de dysfonction cardiaque ; hydrocortisone 200 mg/j (50 mg/6 h ou continu) si besoin persistant de vasopresseurs. La dopamine n'est pas recommandée en première intention.

- A — Vrai.
- B — Vrai.
- C — Vrai.
- D — Vrai : certitude abaissée en 2026 selon les synthèses.
- E — Faux.

*Banque : `QCM-INFE-0249`*

<!--QCM20:end-->

---

## 21. Divergences entre recommandations

| Thème | SSC 2021 [S2] | SSC 2026 [S3] (d'après synthèses — texte non lu) | Autres (NICE 2016/2024 [S5] ; OMS AWaRe 2022 [S4]) | Commentaire |
|---|---|---|---|---|
| **Dépistage** | Ne pas utiliser le qSOFA seul (vs SIRS, NEWS, MEWS) | Position maintenue (recommandation forte, certitude modérée ; NEWS/NEWS2, MEWS ou SIRS préférés) `[À VÉRIFIER]` | NICE : **NEWS2** pour l'adulte hospitalisé ; OMS : scores peu validés dans les pays à ressources limitées | Choisir un score validé localement |
| **Remplissage initial** | ≥ 30 mL/kg en 3 h (suggestion, certitude faible) | Maintenu, certitude faible, poids ajusté si IMC > 30 `[À VÉRIFIER]` | — | Débat sur les stratégies restrictives |
| **Corticoïdes** | Hydrocortisone si choc avec NA/adrénaline ≥ 0,25 µg/kg/min ≥ 4 h | Certitude abaissée à « faible » `[À VÉRIFIER]` | — | Bénéfice surtout sur la résolution du choc |
| **Délai des antibiotiques** | ≤ 1 h (choc / sepsis probable) ; ≤ 3 h (sepsis possible sans choc) | `[À VÉRIFIER]` | NICE : antibiotiques dans l'heure chez les patients à haut risque [S5] ; OMS : le plus tôt possible [S4] | Approche graduée selon la probabilité d'infection |
| **Bithérapie anti-BGN** | Si risque élevé de BMR | `[À VÉRIFIER]` | OMS : **C3G + aminoside** en probabiliste sans foyer et pour l'urinaire grave [S4] | L'OMS fait de l'aminoside une option d'épargne des carbapénèmes |
| **Inotropes** | Dobutamine ajoutée ou adrénaline seule si dysfonction cardiaque | Idem, certitude très faible | — | — |
| **Enfant** | SSC enfant 2020 [S7] : antibiotiques ≤ 1 h (choc), ≤ 3 h (dysfonction sans choc) ; bolus de 10–20 mL/kg (jusqu'à 40–60 mL/kg en 1 h) si réanimation disponible | SSC enfant 2026 publiée (Pediatr Crit Care Med 2026;27(4):379-434) [S10] : contenu non lu `[À VÉRIFIER]` | Critères de Phoenix 2024 [S6] | Prudence du remplissage sans accès à la réanimation |

---

## 22. Références

Détail complet (statut de vérification) dans l'en-tête YAML.

1. [S1] Singer M, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). *JAMA*. 2016;315(8):801-810. doi:10.1001/jama.2016.0287.
2. [S2] Evans L, et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2021. *Intensive Care Med*. 2021;47(11):1181-1247. doi:10.1007/s00134-021-06506-y.
3. [S3] Prescott HC, et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2026. *Intensive Care Med*. 2026;52(5):863-936. doi:10.1007/s00134-026-08361-1. (Texte non lu.)
4. [S4] World Health Organization. *The WHO AWaRe antibiotic book*. 2022 — chapitre 24 « Sepsis in adults ». (DOC-00039, lu.)
5. [S5] NICE. *Suspected sepsis: recognition, diagnosis and early management* (NG51), mise à jour 2024.
6. [S6] Schlapbach LJ, et al. International consensus criteria for pediatric sepsis and septic shock. *JAMA*. 2024;331(8):665-674.
7. [S7] Weiss SL, et al. Surviving Sepsis Campaign international guidelines for the management of septic shock and sepsis-associated organ dysfunction in children. *Pediatr Crit Care Med*. 2020;21(2):e52-e106. **[remplacée par S10]**
8. [S8] Décret exécutif n°22-250 du 30 juin 2022 (MDO). JORADP n°47/2022. (DOC-00072, lu.)
9. [S9] Seymour CW, et al. Assessment of clinical criteria for sepsis. *JAMA*. 2016;315(8):762-774. doi:10.1001/jama.2016.0288.
10. [S10] Weiss SL, et al. Surviving Sepsis Campaign International Guidelines for the Management of Sepsis and Septic Shock in Children 2026. *Pediatr Crit Care Med*. 2026;27(4):379-434. (Texte non lu.)

> **Points à auditer en priorité** (audit du 2026-11-19 : SSC 2021, tableau SOFA et méropénem traités ; SSC 2026 et noradrénaline en suspens, voir le rapport) : (1) lecture du texte intégral de la SSC 2026 (remplissage, corticoïdes, délais, dépistage, bithérapie) et de la SSC 2021 pour les formulations exactes ; (2) bornes du tableau SOFA ; (3) dose et unité de la noradrénaline selon le protocole local (marqueur) ; (4) méropénem 2 g/8 h proposé par l'OMS pour les infections intra-abdominales à BLSE (dose « méningée » : vérifier la dose usuelle selon le RCP) ; (5) données algériennes de résistance (BLSE, carbapénémases, SARM) et protocoles nationaux d'antibiothérapie.
