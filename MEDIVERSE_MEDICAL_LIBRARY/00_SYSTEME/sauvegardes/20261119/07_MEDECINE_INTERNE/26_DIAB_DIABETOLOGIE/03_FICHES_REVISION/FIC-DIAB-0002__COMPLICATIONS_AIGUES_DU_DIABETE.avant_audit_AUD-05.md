---
id: FIC-DIAB-0002
titre: "Fiche — Complications aiguës du diabète : acidocétose, hypoglycémie, état hyperosmolaire"
specialite: DIAB
items_residanat: [RES-MED-092]
dossier_source: DOS-DIAB-0002
version_dossier_source: "1.1"
langue: fr
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent RES-06 (IA) — fiche dérivée du dossier audité"
statut: brouillon_a_auditer
sources:
  - id: S1
    reference: "Umpierrez GE, Davis GM, ElSayed NA, et al. Hyperglycemic Crises in Adults With Diabetes: A Consensus Report. Diabetes Care. 2024;47(8):1257-1275. (ADA, EASD, JBDS, AACE, DTS ; publication simultanée dans Diabetologia)"
    organisme: ADA/EASD/JBDS/AACE/DTS
    annee: 2024
    type: recommandation
    doi: "10.2337/dci24-0032"
    url: ""
    verifiee: true
  - id: S2
    reference: "American Diabetes Association Professional Practice Committee for Diabetes. 6. Glycemic Goals, Hypoglycemia, and Hyperglycemic Crises: Standards of Care in Diabetes—2026. Diabetes Care. 2026;49(Suppl 1):S132-S149."
    organisme: ADA
    annee: 2026
    type: recommandation
    doi: "10.2337/dc26-S006"
    url: ""
    verifiee: true
  - id: S4
    reference: "Dhatariya KK, et al. The management of diabetic ketoacidosis in adults — An updated guideline from the Joint British Diabetes Society for Inpatient Care. Diabet Med. 2022;39(6):e14788."
    organisme: JBDS-IP
    annee: 2022
    type: recommandation
    doi: "10.1111/dme.14788"
    url: ""
    verifiee: true
  - id: S5
    reference: "Mustafa OG, et al. Management of Hyperosmolar Hyperglycaemic State (HHS) in Adults: An updated guideline from the Joint British Diabetes Societies (JBDS) for Inpatient Care Group. Diabet Med. 2023;40(3):e15005."
    organisme: JBDS-IP
    annee: 2023
    type: recommandation
    doi: "10.1111/dme.15005"
    url: ""
    verifiee: true
  - id: S6
    reference: "Glaser N, Fritsch M, Priyambada L, et al. ISPAD clinical practice consensus guidelines 2022: Diabetic ketoacidosis and hyperglycemic hyperosmolar state. Pediatr Diabetes. 2022;23(7):835-856."
    organisme: ISPAD
    annee: 2022
    type: recommandation
    doi: "10.1111/pedi.13406"
    url: ""
    verifiee: true
  - id: S9
    reference: "Hassanein M, et al. Diabetes and Ramadan: Practical guidelines 2021. Diabetes Res Clin Pract. 2022;185:109185. (IDF-DAR)"
    organisme: IDF/DAR
    annee: 2021
    type: recommandation
    doi: "10.1016/j.diabres.2021.109185"
    url: ""
    verifiee: true
---

# Fiche — Complications aiguës du diabète (RES-MED-092)

> Fiche de révision **dérivée exclusivement** du dossier audité DOS-DIAB-0002 (v1.1, statut `audite_corrections_requises`). Aucun fait nouveau. Référentiels : **consensus international 2024** sur les crises hyperglycémiques de l'adulte [S1], ADA 2026 (hypoglycémie) [S2], JBDS [S4, S5], ISPAD 2022 (enfant) [S6]. Protocoles adultes ≠ pédiatriques.

## 1. Définition (2 lignes)

**Acidocétose (ACD)** : carence insulinique sévère → **D** (glycémie ≥ 200 mg/dL ou diabète connu) + **K** (β-OHB ≥ 3,0 mmol/L) + **A** (pH < 7,30 et/ou HCO₃ < 18) ; **état hyperosmolaire (EHH)** : hyperglycémie majeure + hyperosmolalité **sans cétose ni acidose significatives** ; **hypoglycémie** : glucose < 70 mg/dL (niveaux 1–3).

## 2. Chiffres et critères à connaître

| | ACD (2024) | EHH (2024) |
|---|---|---|
| Glycémie | **≥ 200 mg/dL** ou diabète connu | **≥ 600 mg/dL** (33,3 mmol/L) |
| Cétose | **β-OHB ≥ 3,0 mmol/L** (ou cétonurie ≥ 2+) | β-OHB < 3,0 |
| Acidose | **pH < 7,30 et/ou HCO₃ < 18** | pH ≥ 7,30 **et** HCO₃ ≥ 15 |
| Osmolalité | — | Efficace **> 300** (ou totale > 320) mOsm/kg |
| Particularités | ACD euglycémique ≈ 10 % | Forme mixte ACD/EHH > 1/3 des crises |

| Sévérité ACD | Légère | Modérée | Sévère |
|---|---|---|---|
| pH | > 7,25–< 7,30 | 7,00–7,25 | **< 7,00** |
| HCO₃ (mmol/L) | 15–18 | 10–< 15 | **< 10** |
| β-OHB | 3–6 | 3–6 | **> 6** |
| Conscience | Normale | ± somnolence | **Stupeur/coma** → soins intensifs |

| Hypoglycémie (ADA 2026) | Définition |
|---|---|
| Niveau 1 | < 70 et ≥ 54 mg/dL (< 3,9 et ≥ 3,0 mmol/L) |
| Niveau 2 | **< 54 mg/dL** (3,0 mmol/L) |
| Niveau 3 | Altération nécessitant **l'aide d'un tiers** (« coma hypoglycémique ») |

```text
Trou anionique   = Na − (Cl + HCO3)                    normal ≈ 8–12
Osm. efficace    = 2 × Na + glucose (mmol/L)           EHH si > 300
Osm. totale      = 2 × Na + glucose + urée             EHH si > 320 ; troubles neuro > 330
Na corrigée     ≈ Na + 1,6 × [(glucose mg/dL − 100) / 100]
```

## 3. Démarche diagnostique

```text
Hyperglycémie aiguë / malaise chez un diabétique
├─ Glycémie capillaire IMMÉDIATE (tout trouble neuro ou du comportement)
├─ β-OHB (PAS la cétonurie : mesure l'acéto-acétate, faux positifs, ne juge pas
│   la résolution) + gaz du sang VEINEUX + ionogramme (K+ !), urée, créatinine,
│   osmolalité, phosphore, magnésium, NFS, lipase, ECG
├─ ACD ? EHH ? mixte ? → sévérité → lieu de soins
└─ Facteur déclenchant : INFECTION (1re cause), omission d'insuline (jusqu'à 75 %
    des ACD récidivantes), DT1 inaugural, iSGLT2, corticoïdes, inhibiteurs de
    points de contrôle, infarctus, pancréatite, AVC, alcool, grossesse
```

- ACD : polyuro-polydipsie, **douleurs abdominales** (> 50 %), **dyspnée de Kussmaul**, **odeur acétonique**, déshydratation globale.
- EHH : sujet âgé, DT2 méconnu, installation en jours, **déshydratation majeure**, troubles neurologiques avec **signes focaux trompeurs**.
- Hypoglycémie : signes adrénergiques (sueurs, tremblements, palpitations, faim) puis neuroglucopéniques (confusion, agressivité, déficit focal, convulsions, coma) ; signes adrénergiques absents sous bêtabloquant, neuropathie, sujet âgé. Hors diabète : **triade de Whipple**.
- **ACD euglycémique** (< 200 mg/dL) : iSGLT2, grossesse, jeûne (**Ramadan**), alcool → doser la cétonémie.

## 4. Traitement

```text
ACD DE L'ADULTE (consensus 2024)
1. REMPLISSAGE : NaCl 0,9 % ou cristalloïde balancé 500–1 000 mL/h × 2–4 h
   (fragiles : bolus de 250 mL) ; déficit corrigé en 24–48 h
2. POTASSIUM AVANT L'INSULINE
   K < 3,5 → PAS D'INSULINE ; KCl 10 mmol/h jusqu'à K > 3,5
   K 3,5–5,0 → insuline + 20–30 mmol de K+ par litre
   K > 5,0 → pas de K+, recontrôle
3. INSULINE IV débit fixe 0,1 U/kg/h (bolus 0,1 U/kg seulement si accès retardé)
   glycémie < 250 mg/dL → + glucose 5–10 % et insuline 0,05 U/kg/h
   (glycémie autour de 200 mg/dL) ; NE PAS ARRÊTER tant que la cétose persiste
4. Bicarbonates SEULEMENT si pH < 7,0 ; phosphates si < 1,0 mmol/L symptomatique
5. RÉSOLUTION : β-OHB < 0,6 ET (pH ≥ 7,3 ou HCO3 ≥ 18)
6. RELAIS : basale SC 1–2 h AVANT l'arrêt de l'IV ; DQT 0,5–0,6 U/kg/j
   (≈ 0,3 si risque d'hypoglycémie) ; basal-bolus
```

| Élément | Détail |
|---|---|
| Bicarbonates (pH < 7,0) | 100 mmol de bicarbonate de sodium 8,4 % dans 400 mL d'eau stérile, toutes les 2 h jusqu'à pH > 7,0 `[POSOLOGIE À VÉRIFIER — protocole local ; présentation des solutés de bicarbonate disponibles localement]` |
| Phosphates | 20–30 mmol de phosphate de potassium (attention : seuil 2009 en mg/dL) |
| ACD légère/modérée non compliquée | Analogues rapides SC : 0,1 U/kg toutes les heures ou 0,2 U/kg toutes les 2 h (pas si sévère, compliquée ni EHH) |
| Mesures générales | Scope, surveillance horaire, **arrêt des iSGLT2**, **HBPM préventive**, traitement du déclencheur |

**EHH** : **remplissage d'abord** (NaCl 0,9 %, 500–1 000 mL/h ; JBDS : + 3 à 6 L en 12 h) ; corriger **lentement** : glycémie ≤ 90–120 mg/dL/h (JBDS ≤ 5 mmol/L/h), **osmolalité 3–8 mOsm/kg/h**, **natrémie ≤ 10 mmol/L/24 h** ; une hausse initiale de la natrémie n'impose pas de soluté hypotonique ; insuline **0,05 U/kg/h** (0,1 si cétose ≥ 3 ou acidose) — JBDS 2023 : seulement quand la glycémie ne baisse plus ; **HBPM** toute l'hospitalisation ; **protection des talons**.

**Hypoglycémie** :

| Situation | Conduite |
|---|---|
| Conscient | **15 g de glucose**, contrôle à **15 min**, répéter si < 70 mg/dL, puis collation (5–10 g sous délivrance automatisée ; **glucose pur sous acarbose**) |
| Inconscient | **Glucagon 1 mg IM/SC**, **3 mg nasal**, ou dasiglucagon 0,6 mg ; rien par la bouche ; **jamais d'insuline** |
| Milieu de soins | Glucose IV puis perfusion G5–10 % `[POSOLOGIE À VÉRIFIER — protocole local]` |
| Sulfamides | **Hospitalisation**, glucose prolongé (24–72 h) ; glucagon déconseillé comme traitement principal ; octréotide `[indication et POSOLOGIE À VÉRIFIER — protocole local / avis toxicologique]` |
| Après tout niveau 2–3 | Rechercher la cause, **réévaluer le traitement**, glucagon à domicile, éducation, MCG |

## 5. Surveillance et complications

- ACD : glycémie toutes les 1–2 h ; **kaliémie 2 h après l'insuline puis toutes les 4 h** ; gaz veineux, ionogramme, β-OHB toutes les 4 h ; conscience, diurèse horaires ; **feuille de surveillance**.
- EHH : glycémie horaire au début ; osmolalité toutes les 4 h (horaire au début selon le JBDS) ; pieds quotidiennement.

| Complication du traitement | Prévention |
|---|---|
| Hypoglycémie (16–28 %) | Glucose dès < 250 mg/dL, glycémie 1–2 h |
| **Hypokaliémie** (~55 %) | K+ précoce ; kaliémie à H2 |
| Acidose hyperchlorémique | Cristalloïdes balancés ; ne pas la prendre pour une ACD persistante |
| Thrombose (EHH) | HBPM |
| **Œdème cérébral** (enfant > adulte) | Correction lente, surveillance neuro ; mannitol/salé hypertonique |
| Démyélinisation osmotique | Osmolalité −3 à −8 mOsm/kg/h |

- Prévention : éducation, **jours de maladie** (**ne jamais arrêter la basale**, cétonémie toutes les 2–4 h, suspendre iSGLT2), MCG, suivi à 2–4 semaines ; **Ramadan** : rompre le jeûne si glycémie **< 70 ou > 300 mg/dL** [S9].

## 6. Pièges classiques

1. Exclure une ACD parce que la glycémie est basse (**ACD euglycémique** sous iSGLT2, grossesse, jeûne).
2. Juger la résolution sur la **cétonurie** ou le **trou anionique**.
3. Débuter l'insuline avec une **kaliémie < 3,5 mmol/L**.
4. **Arrêter l'insuline IV** quand la glycémie se normalise alors que la cétose persiste.
5. Arrêter la perfusion sans **chevauchement** avec la basale SC.
6. Prescrire des **bicarbonates** pour un pH à 7,10.
7. Corriger trop vite un EHH ou passer aux **solutés hypotoniques** parce que la natrémie monte.
8. Prendre l'hyponatrémie de l'ACD/EHH pour une hyponatrémie hypotonique (calculer la **natrémie corrigée**).
9. Oublier **HBPM et protection des talons** dans l'EHH.
10. **Glucagon** comme traitement principal d'une hypoglycémie au sulfamide, ou retour à domicile après simple resucrage ; attribuer un déficit focal à un AVC sans **glycémie capillaire**.

## 7. Moyens mnémotechniques (originaux)

- **« D-K-A : 200 – 3 – 7,30 »** : glycémie ≥ 200 mg/dL (ou diabète connu), β-OHB ≥ 3, pH < 7,30 (et/ou HCO₃ < 18).
- **« Potassium d'abord, insuline ensuite »** : pas d'insuline si K < 3,5.
- **« 0,1 puis 0,05 sous 250 »** : insuline 0,1 U/kg/h, réduite à 0,05 avec glucose sous 250 mg/dL.
- **« La cétone décide, pas le sucre »** : on arrête l'IV sur la résolution de la cétose, pas sur la glycémie.
- **« 15-15 »** : 15 g de glucose, contrôle à 15 min.
- **« EHH = eau, lentement »** : remplissage d'abord, correction lente de l'osmolalité.

## 8. Si je n'ai que 5 minutes

1. ACD : glycémie ≥ 200 (ou diabète connu) + β-OHB ≥ 3 + pH < 7,30/HCO₃ < 18.
2. EHH : glycémie ≥ 600, osmolalité efficace > 300, sans cétose ni acidose.
3. β-OHB et gaz veineux, pas la cétonurie.
4. Remplissage 500–1 000 mL/h × 2–4 h.
5. K < 3,5 → pas d'insuline ; 3,5–5 → 20–30 mmol/L ; kaliémie à H2.
6. Insuline 0,1 U/kg/h → 0,05 + glucose sous 250 mg/dL.
7. Bicarbonates si pH < 7,0 seulement.
8. Résolution : β-OHB < 0,6 + pH ≥ 7,3 ou HCO₃ ≥ 18 ; basale 1–2 h avant l'arrêt.
9. EHH : lent (osmolalité 3–8 mOsm/kg/h), HBPM, talons.
10. Hypoglycémie : 15 g/15 min ; glucagon si inconscient ; sulfamide = hospitalisation.

## 9. Sources (reprises du dossier DOS-DIAB-0002)

- [S1] Umpierrez GE, et al. Crises hyperglycémiques de l'adulte, consensus 2024. Diabetes Care 2024;47(8):1257-1275.
- [S2] ADA. Standards of Care 2026 — 6. Objectifs glycémiques, hypoglycémie et crises hyperglycémiques.
- [S4] Dhatariya KK, et al. JBDS — acidocétose de l'adulte (mise à jour).
- [S5] Mustafa OG, et al. JBDS — état hyperosmolaire de l'adulte (mise à jour).
- [S6] Glaser N, et al. ISPAD 2022 — acidocétose et EHH de l'enfant.
- [S9] Hassanein M, et al. Diabète et Ramadan, IDF-DAR 2021.
