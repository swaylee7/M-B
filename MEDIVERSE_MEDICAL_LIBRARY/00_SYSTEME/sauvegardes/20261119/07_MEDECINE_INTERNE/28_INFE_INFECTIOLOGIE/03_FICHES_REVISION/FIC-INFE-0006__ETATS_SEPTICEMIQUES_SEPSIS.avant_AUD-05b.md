---
id: FIC-INFE-0006
titre: "Fiche — États septicémiques (sepsis) : diagnostic, pronostic, traitement"
specialite: INFE
items_residanat: [RES-MED-004]
dossier_source: DOS-INFE-0006
version_dossier_source: "1.1"
langue: fr
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent RES-06 (IA) — fiche dérivée du dossier audité"
statut: brouillon_a_auditer
sources:
  - id: S1
    reference: "Singer M, Deutschman CS, Seymour CW, et al. The Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810."
    organisme: "SCCM / ESICM (Sepsis-3 Task Force)"
    annee: 2016
    type: recommandation
    doi: "10.1001/jama.2016.0287"
    url: "https://doi.org/10.1001/jama.2016.0287"
    verifiee: true
  - id: S2
    reference: "Evans L, Rhodes A, Alhazzani W, et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2021. Intensive Care Med. 2021;47(11):1181-1247 (copublication : Crit Care Med. 2021;49(11):e1063-e1143)."
    organisme: "Surviving Sepsis Campaign (SCCM / ESICM)"
    annee: 2021
    type: recommandation
    doi: "10.1007/s00134-021-06506-y"
    url: ""
    verifiee: true
  - id: S3
    reference: "Prescott HC, Antonelli M, Alhazzani W, et al. Surviving Sepsis Campaign: international guidelines for management of sepsis and septic shock 2026. Intensive Care Med. 2026;52(5):863-936 (copublication : Crit Care Med. 2026;54(4):725-812)."
    organisme: "Surviving Sepsis Campaign (SCCM / ESICM)"
    annee: 2026
    type: recommandation
    doi: "10.1007/s00134-026-08361-1"
    url: "https://doi.org/10.1007/s00134-026-08361-1"
    verifiee: true
  - id: S4
    reference: "World Health Organization. The WHO AWaRe (Access, Watch, Reserve) antibiotic book. Geneva: WHO; 2022. Chapitre 24 « Sepsis in adults (including septic shock) » (p. 295-318)."
    organisme: OMS
    annee: 2022
    type: recommandation
    doi: ""
    url: "https://iris.who.int/handle/10665/365237"
    verifiee: true
  - id: S5
    reference: "National Institute for Health and Care Excellence. Suspected sepsis: recognition, diagnosis and early management. NICE guideline NG51. Publié en 2016, mis à jour le 19 mars 2024."
    organisme: NICE
    annee: 2024
    type: recommandation
    doi: ""
    url: "https://www.nice.org.uk/guidance/ng51"
    verifiee: true
  - id: S6
    reference: "Schlapbach LJ, Watson RS, Sorce LR, et al. International consensus criteria for pediatric sepsis and septic shock. JAMA. 2024;331(8):665-674."
    organisme: "SCCM Pediatric Sepsis Definition Task Force"
    annee: 2024
    type: recommandation
    doi: ""
    url: "https://jamanetwork.com/journals/jama/fullarticle/2814297"
    verifiee: true
  - id: S8
    reference: "Décret exécutif n°22-250 du 30 juin 2022 fixant la liste des maladies transmissibles soumises à déclaration obligatoire. JORADP n°47 du 11 juillet 2022."
    organisme: "Gouvernement algérien / Ministère de la Santé"
    annee: 2022
    type: texte_officiel
    doi: ""
    url: "https://www.joradp.dz/FTP/JO-FRANCAIS/2022/F2022047.pdf"
    verifiee: true
  - id: S10
    reference: "Weiss SL, Peters MJ, Oczkowski SJW, et al. Surviving Sepsis Campaign International Guidelines for the Management of Sepsis and Septic Shock in Children 2026. Pediatr Crit Care Med. 2026;27(4):379-434 (copublication : Intensive Care Med. 2026;52(5):937-983)."
    organisme: "Surviving Sepsis Campaign (SCCM / ESICM)"
    annee: 2026
    type: recommandation
    doi: "10.1097/PCC.0000000000003927"
    url: ""
    verifiee: true
---

# Fiche — États septicémiques (sepsis) : diagnostic, pronostic, traitement (RES-MED-004)

> Fiche de révision **dérivée exclusivement** du dossier audité DOS-INFE-0006 (v1.1, statut `audite_corrections_requises`). Aucun fait nouveau ; posologies **identiques** au dossier (OMS, livre AWaRe 2022 [S4] ; SSC 2021 [S2]) ; marqueur posologique de la noradrénaline conservé. SSC 2026 adulte [S3] et enfant [S10] : existence vérifiée, **texte non lu** (positions rapportées par des synthèses `[À VÉRIFIER]`). Réanimation hémodynamique détaillée : DOS-MINT_REA-0001.

## 1. Définition (2 lignes)

**Sepsis (Sepsis-3, 2016)** : **dysfonction d'organe menaçant le pronostic vital, causée par une réponse dérégulée de l'hôte à une infection** = infection + **ΔSOFA ≥ 2** [S1]. **Choc septique** : **vasopresseur pour PAM ≥ 65 mmHg** **et** **lactate > 2 mmol/L (> 18 mg/dL)** malgré un remplissage adéquat ; « sepsis sévère » **abandonné** ; SRIS = simple outil de dépistage [S1, S4].

## 2. Chiffres et critères à connaître

| Paramètre | Valeur |
|---|---|
| Épidémiologie (GBD 2017) | ≈ **49 millions** de cas, **11 millions** de décès ; ≈ **20 millions** de cas chez les < 5 ans ; sepsis maternel ≈ **12 millions** [S4] |
| Mortalité hospitalière (cohortes Sepsis-3) | **> 10 %** (sepsis) ; **> 40 %** (choc septique) [S1] |
| **qSOFA** (≥ 2 = risque élevé hors réanimation) | **FR ≥ 22/min**, **conscience altérée** (Glasgow < 15), **PAS ≤ 100 mmHg** [S1] — **pas un outil de dépistage isolé** (SSC 2021 ; 2026 `[À VÉRIFIER — texte 2026]`) [S2, S3] |
| SRIS (1991) | ≥ 2 critères : T > 38 °C ou < 36 °C, FC > 90/min, FR > 20/min (ou PaCO₂ < 32 mmHg), leucocytes > 12 000 ou < 4 000/mm³ `[À VÉRIFIER — libellés exacts]` |
| NEWS2 | Score d'alerte du NICE (adulte hospitalisé) [S5] `[À VÉRIFIER — seuils]` |
| Enfant (Phoenix 2024) | Sepsis = suspicion d'infection + **score ≥ 2** ; choc = **≥ 1 point cardiovasculaire** [S6] |

**SOFA** (d'après [S1, S4]) :

| Système | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| PaO₂/FiO₂ (mmHg) | < 400 | < 300 | < 200 avec assistance ventilatoire | < 100 avec assistance ventilatoire |
| Plaquettes (/mm³) | < 150 000 | < 100 000 | < 50 000 | < 20 000 |
| Bilirubine (mg/dL) | 1,2–1,9 | 2,0–5,9 | 6,0–11,9 | > 12,0 |
| Cardiovasculaire | PAM < 70 mmHg | Dopamine < 5 ou dobutamine | Noradrénaline ≤ 0,1 µg/kg/min (ou dopamine 5,1–15, adrénaline ≤ 0,1) | Noradrénaline > 0,1 µg/kg/min (ou dopamine > 15, adrénaline > 0,1) |
| Glasgow | 13–14 | 10–12 | 6–9 | < 6 |
| Créatinine (mg/dL) ou diurèse | 1,2–1,9 | 2,0–3,4 | 3,5–4,9 ou < 500 mL/j | > 5,0 ou < 200 mL/j |

## 3. Démarche diagnostique

```text
PATIENT FÉBRILE (ou hypotherme) avec suspicion d'infection
├─ Dépistage : NEWS2 / SIRS / qSOFA (le qSOFA seul ne suffit pas pour exclure)
├─ Dysfonction d'organe (ΔSOFA ≥ 2) ?
│   ├─ NON → infection sans sepsis : traiter le foyer, surveiller
│   └─ OUI → SEPSIS → vasopresseur pour PAM ≥ 65 après remplissage ET lactate > 2 → CHOC SEPTIQUE
├─ Foyer ? examen complet + imagerie ciblée → contrôle de la source
└─ Pronostic : SOFA, lactate et sa cinétique, délai/adéquation des antibiotiques, source, terrain
```

- **Clinique** : fièvre ou **hypothermie**, frissons ; **polypnée**, **confusion**, hypotension, **oligurie** (< 0,5 mL/kg/h), **marbrures**, **TRC > 3 s**, purpura. Terrain trompeur : sujet âgé, immunodéprimé, bêtabloquant, nourrisson.
- **Porte d'entrée** (examen « de la tête aux pieds », cathéters, souffle, toucher rectal) : urinaire (*E. coli* ; **obstacle à drainer**), pulmonaire (pneumocoque), intra-abdominal (entérobactéries, anaérobies ; triade de Charcot), peau (fasciite → chirurgie), cathéter (*S. aureus*, *Candida*), endocarde, méninges/**purpura fulminans** (C3G immédiate), post-partum, neutropénie, asplénie. **Algérie** : typhoïde (DOS-INFE-0003), brucellose (DOS-INFE-0002), méningococcémie, **paludisme grave** au retour du Sahel (DOS-INFE-0004).
- **Microbiologie** : **≥ 2 paires d'hémocultures avant la première dose si cela ne retarde pas substantiellement** les antibiotiques [S2] ; prélèvements du foyer ; frottis/TDR au retour d'une zone d'endémie. ***S. aureus*** dans une seule hémoculture = **toujours significatif** → échocardiographie.
- **Gravité** : **lactate** (> 2 mmol/L = hypoperfusion ; > 4 mmol/L = gravité marquée `[À VÉRIFIER]`), gaz du sang, NFS, hémostase (CIVD), créatinine, bilirubine, glycémie. **PCT** : pas pour décider de **débuter**, mais avec la clinique pour décider de l'**arrêt** (SSC 2021) [S2]. Imagerie orientée, **jamais avant les antibiotiques**.
- **Différentiels** : chocs cardiogénique, hypovolémique, embolie pulmonaire, anaphylaxie, pancréatite, insuffisance surrénale, intoxications, paludisme grave, syndrome d'activation macrophagique.

## 4. Traitement

### 4.1 Délais et règles (SSC 2021) [S2]
- **Choc possible ou sepsis probable** : antibiotiques **immédiatement, idéalement dans l'heure** ; **sepsis possible sans choc** : évaluation rapide puis antibiotiques **dans les 3 heures** si la suspicion persiste.
- **SARM** couvert si risque élevé ; **deux molécules anti-BGN** si risque élevé de multirésistance ; antifongique si risque élevé ; **perfusion prolongée** des bêta-lactamines en entretien.

### 4.2 Antibiothérapie probabiliste (OMS, AWaRe 2022 ; adulte, fonction rénale normale) [S4]

| Foyer | Options OMS | Durée |
|---|---|---|
| **Sans foyer identifié** | **Céfotaxime 2 g/8 h IV** ou **ceftriaxone 2 g/24 h IV** + **amikacine 15 mg/kg/24 h IV** ou **gentamicine 5 mg/kg/24 h IV** (amikacine : épargne des carbapénèmes) | 7 jours |
| **Méningite** | **Céfotaxime 2 g/6 h** ou **ceftriaxone 2 g/12 h** IV | 10 jours (variable) |
| **Respiratoire basse** | Céfotaxime 2 g/8 h ou ceftriaxone 2 g/24 h **+ clarithromycine 500 mg/12 h** IV | 5 jours |
| **Intra-abdominale** | C3G **+ métronidazole 500 mg/8 h** ou **pipéracilline-tazobactam 4 g/0,5 g toutes les 6 h** ; si BLSE fréquentes : **méropénem 2 g/8 h** | ≈ 7 jours si source contrôlée |
| **Peau, tissus mous** | Ceftriaxone 2 g/24 h + métronidazole 500 mg/8 h, ou pipéracilline-tazobactam **+ clindamycine 900 mg/8 h** (fasciite) ; **+ vancomycine 15–20 mg/kg/12 h** si SARM | ≈ 7 jours |
| **Urinaire** | Céfotaxime 2 g/8 h ou ceftriaxone 2 g/24 h **+ amikacine 15 mg/kg/24 h** | 7 jours |
| **Fièvre entérique** | **Ceftriaxone 2 g/24 h** | 10 jours |

Aminosides en **dose unique journalière** ; adapter à l'**écologie locale** (BLSE, carbapénémases, *Pseudomonas*, SARM) ; protocole national algérien non retrouvé `[À VÉRIFIER]`.

### 4.3 Contrôle de la source [S2]
Geste **dès que possible** : **dérivation des urines** (JJ, néphrostomie), **drainage biliaire** (CPRE), laparotomie, **débridement** d'une fasciite ; **retrait des cathéters** suspects.

### 4.4 Réanimation (SSC 2021 ; 2026 d'après synthèses) [S2, S3]
- **Cristalloïdes ≥ 30 mL/kg dans les 3 premières heures** si hypoperfusion ou choc (suggestion, certitude faible ; maintenu en 2026, poids ajusté si IMC > 30 `[À VÉRIFIER]`) ; **solutés balancés** ; albumine si grands volumes ; **pas d'hydroxyéthylamidons** (forte) ni de gélatines ; remplissage guidé par indices dynamiques, TRC, lactate.
- **PAM cible 65 mmHg** ; **noradrénaline en 1re intention** (voie périphérique possible) ; **vasopressine** ajoutée plutôt qu'escalade (noradrénaline à 0,25–0,5 µg/kg/min) ; dysfonction cardiaque : **dobutamine** ajoutée ou **adrénaline seule** `[POSOLOGIE À VÉRIFIER — protocole local de la noradrénaline (base/tartrate)]`.
- **Hydrocortisone 200 mg/j** (50 mg IV toutes les 6 h ou continu) si noradrénaline ou adrénaline **≥ 0,25 µg/kg/min au moins 4 h après le début** (suggestion) ; certitude abaissée en 2026 `[À VÉRIFIER]`.
- Ventilation protectrice (**6 mL/kg** de poids idéal, plateau **≤ 30 cmH₂O**, décubitus ventral) ; transfusion si **Hb < 7 g/dL** ; bicarbonate seulement si **pH ≤ 7,20** avec insuffisance rénale aiguë ; insuline si glycémie **≥ 180 mg/dL**, cible 144–180 ; HBPM ; **pas de vitamine C** ; nutrition entérale précoce.

```text
≤ 45 min : hémocultures (2 paires) + foyer + lactate, gaz du sang, NFS, hémostase, créatinine, bilirubine
≤ 60 min : ANTIBIOTHÉRAPIE IV (foyer, lieu d'acquisition, terrain, risque BMR/SARM)
Hypotension ou lactate ≥ 4 : cristalloïdes 30 mL/kg (≤ 3 h) → PAM < 65 : NORADRÉNALINE
CONTRÔLE DE LA SOURCE → réévaluation H6–H12 puis quotidienne (lactate, diurèse, SOFA)
J2–J3 : microbiologie → DÉSESCALADE, durée courte, relais oral, PCT pour l'arrêt
(délais en minutes indicatifs [À VÉRIFIER])
```

## 5. Surveillance et complications

- **Surveillance** : PAM, FC, marbrures, TRC, **diurèse horaire**, **décroissance du lactate** ; **SOFA quotidien** ; hémocultures de contrôle (*S. aureus*, candidémie) ; résultats à **48–72 h** ; **réévaluation quotidienne** de la désescalade, dosages des aminosides et de la vancomycine ; suivi post-sepsis (fonctionnel, cognitif, psychologique).
- **Complications** : défaillances multiviscérales (SDRA, insuffisance rénale aiguë, CIVD, encéphalopathie), localisations secondaires (endocardite, abcès, spondylodiscite), infections nosocomiales (immunoparalysie), thromboses, **syndrome post-sepsis**.
- **Algérie** : **BMR, infections du site opératoire et PAVM à déclaration obligatoire** (catégorie 1, décret 22-250) [S8] ; écologie BLSE/carbapénémases `[À VÉRIFIER — données du réseau national de surveillance de la résistance]` ; disponibilité de la vasopressine, des carbapénèmes, de la colistine `[À VÉRIFIER]`.
- **Prévention** : vaccinations (pneumocoque, *Haemophilus* b, méningocoque, grippe) `[À VÉRIFIER — recommandations nationales adultes]`, hygiène des mains, retrait précoce des cathéters et sondes, **bon usage AWaRe**, éducation des splénectomisés et neutropéniques, « code sepsis ».

## 6. Pièges classiques

1. Définir encore le sepsis par le **SRIS** ou parler de « **sepsis sévère** ».
2. Attendre un **qSOFA ≥ 2** pour évoquer un sepsis.
3. **Retarder les antibiotiques** pour l'imagerie, la PL ou les résultats.
4. Oublier le **contrôle de la source** (pyélonéphrite obstructive, angiocholite, fasciite).
5. Utiliser des **hydroxyéthylamidons** ou la **dopamine** en première intention.
6. Confondre la dose de noradrénaline en **base** et en **tartrate** (facteur ≈ 2) `[À VÉRIFIER — protocole local]`.
7. Négliger une hémoculture à ***S. aureus*** et oublier l'**échocardiographie**.
8. Ne pas **réévaluer** l'antibiothérapie à 48–72 h, ou la prolonger inutilement.
9. Omettre le **frottis** chez un patient revenant du Sahel (paludisme grave).
10. Prescrire une **C3G seule** là où les entérobactéries **BLSE** sont fréquentes, chez un patient à risque `[À VÉRIFIER — écologie locale]`.

## 7. Moyens mnémotechniques (originaux)

- **« 2-65-2 »** : ΔSOFA ≥ 2 (sepsis) ; PAM 65 sous vasopresseur et lactate > 2 (choc).
- **« 22-100-15 »** : qSOFA (FR ≥ 22, PAS ≤ 100, Glasgow < 15) — pronostic, pas dépistage.
- **« Une heure, deux paires, trois heures »** : antibiotiques dans l'heure (choc/probable), 2 paires d'hémocultures, 3 h si sepsis possible.
- **« Drainer bat doubler »** : le contrôle de la source compte autant que l'antibiotique.
- **« 30 – 65 – 0,25 »** : 30 mL/kg, PAM 65, hydrocortisone dès 0,25 µg/kg/min.

## 8. Si je n'ai que 5 minutes

1. Sepsis = dysfonction d'organe par réponse dérégulée à une infection ; ΔSOFA ≥ 2.
2. Choc septique = vasopresseur pour PAM ≥ 65 et lactate > 2 mmol/L malgré remplissage.
3. qSOFA : pronostic, pas outil de dépistage isolé.
4. Hémocultures avant antibiotiques, sans les retarder.
5. Antibiotiques dans l'heure (choc, sepsis probable) ; dans les 3 heures (sepsis possible).
6. OMS : C3G + aminoside (sans foyer, urinaire) ; C3G + métronidazole ou pipéracilline-tazobactam (abdomen) ; C3G + clarithromycine (poumon).
7. Contrôle de la source dès que possible.
8. Cristalloïdes balancés 30 mL/kg en 3 h, PAM 65, noradrénaline ± vasopressine, hydrocortisone 200 mg/j.
9. Désescalade, durée courte, PCT pour l'arrêt.
10. Enfant : Phoenix ≥ 2 ; Algérie : BMR, ISO, PAVM à déclaration obligatoire.

## 9. Sources (reprises du dossier DOS-INFE-0006)

- [S1] Singer M, et al. Sepsis-3. JAMA. 2016;315(8):801-810. doi:10.1001/jama.2016.0287.
- [S2] Evans L, et al. Surviving Sepsis Campaign 2021. Intensive Care Med. 2021;47(11):1181-1247. doi:10.1007/s00134-021-06506-y.
- [S3] Prescott HC, et al. Surviving Sepsis Campaign 2026. Intensive Care Med. 2026;52(5):863-936. doi:10.1007/s00134-026-08361-1.
- [S4] OMS. The WHO AWaRe antibiotic book. 2022 — chapitre « Sepsis in adults » (DOC-00039).
- [S5] NICE. Suspected sepsis (NG51). 2016, mise à jour 2024.
- [S6] Schlapbach LJ, et al. Critères de Phoenix. JAMA. 2024;331(8):665-674.
- [S8] Décret exécutif n° 22-250 du 30 juin 2022 (MDO) (DOC-00072).
- [S10] Weiss SL, et al. SSC enfant 2026. Pediatr Crit Care Med. 2026;27(4):379-434.
