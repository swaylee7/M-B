---
id: FIC-CARD-0004
titre: "Fiche — Syndromes coronariens aigus sans sus-décalage du ST"
specialite: CARD
items_residanat: [RES-MED-057]
dossier_source: DOS-CARD-0004
version_dossier_source: "1.1"
langue: fr
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent RES-06 (IA) — fiche dérivée du dossier audité"
statut: brouillon_a_auditer
sources:
  - id: S1
    reference: "Byrne RA, Rossello X, Coughlan JJ, et al. 2023 ESC Guidelines for the management of acute coronary syndromes. Eur Heart J. 2023;44(38):3720-3826."
    organisme: ESC
    annee: 2023
    type: recommandation
    doi: "10.1093/eurheartj/ehad191"
    url: ""
    verifiee: true
  - id: S2
    reference: "Thygesen K, Alpert JS, Jaffe AS, et al. Fourth universal definition of myocardial infarction (2018). Eur Heart J. 2019;40(3):237-269."
    organisme: ESC/ACC/AHA/WHF
    annee: 2018
    type: article
    doi: "10.1093/eurheartj/ehy462"
    url: ""
    verifiee: true
  - id: S3
    reference: "Rao SV, O'Donoghue ML, Ruel M, et al. 2025 ACC/AHA/ACEP/NAEMSP/SCAI Guideline for the Management of Patients With Acute Coronary Syndromes. Circulation. 2025 (en ligne le 27 février 2025). Co-publication : J Am Coll Cardiol. 2025;85(22):2135-2237 (doi 10.1016/j.jacc.2024.11.009)."
    organisme: ACC/AHA
    annee: 2025
    type: recommandation
    doi: "10.1161/CIR.0000000000001309"
    url: ""
    verifiee: true
  - id: S4
    reference: "Collet JP, Thiele H, Barbato E, et al. 2020 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation. Eur Heart J. 2021;42(14):1289-1367."
    organisme: ESC
    annee: 2020
    type: recommandation
    doi: "10.1093/eurheartj/ehaa575"
    url: ""
    verifiee: true
---

# Fiche — SCA sans sus-décalage du ST (RES-MED-057)

> Fiche de révision **dérivée exclusivement** du dossier audité DOS-CARD-0004 (v1.1, statut `audite_corrections_requises`). Aucun fait nouveau. Référentiel d'examen : **ESC 2023** [S1] ; posologies à confronter au RCP et au protocole local.

## 1. Définition (2 lignes)

**SCA ST−** : symptômes d'ischémie myocardique aiguë **sans sus-décalage persistant** du ST (≥ 20 min) ; ECG avec sous-décalage, T négatives, sus-décalage transitoire ou **normal** [S1]. Selon la troponine ultrasensible : **NSTEMI** (élevée avec cinétique) ou **angor instable** (normale).

## 2. Chiffres et critères à connaître

| Paramètre | Valeur |
|---|---|
| ECG | ≤ 10 min, **répété** (récidive, H3, sortie) ; V7–V9 au moindre doute |
| Sous-décalage significatif | ≥ 0,5 mm dans 2 dérivations contiguës |
| Ondes T négatives | > 1 mm en dérivations à R dominante |
| Algorithme troponine | **0 h/1 h** (ou 0 h/2 h), seuils **propres à chaque dosage** |
| hs-cTnT Elecsys | Très bas < 5 ng/L (douleur > 3 h) ; bas < 12 et Δ1h < 3 ; élevé ≥ 52 ; Δ1h ≥ 5 ng/L |
| hs-cTnI Architect | Très bas < 4 ng/L ; bas < 5 et Δ1h < 2 ; élevé ≥ 64 ; Δ1h ≥ 6 ng/L |
| GRACE | **> 140** = haut risque |
| Très haut risque | Coronarographie **immédiate < 2 h** |
| Haut risque | Coronarographie **précoce < 24 h** à envisager (IIa en 2023, I en 2020) |
| Arrêt P2Y12 avant pontage | Ticagrélor ≥ 3 j · clopidogrel ≥ 5 j · prasugrel ≥ 7 j (aspirine poursuivie) |
| Cible LDL | < 1,4 mmol/L et baisse ≥ 50 % |

| Niveau de risque (ESC 2023) | Critères (au moins un) |
|---|---|
| **Très haut** | Instabilité hémodynamique/choc, douleur réfractaire, arythmie menaçante/arrêt, complication mécanique, IC aiguë liée au SCA, ST-T dynamiques récidivants (sus-décalage intermittent) |
| **Haut** | NSTEMI confirmé, ST-T dynamiques, sus-décalage transitoire, GRACE > 140 |
| **Aucun critère** | Coronarographie hospitalière si forte suspicion ; sinon stratégie invasive **sélective** |

## 3. Démarche diagnostique

```text
Douleur thoracique → ECG ≤ 10 min
├─ Sus-décalage persistant / équivalent (postérieur, de Winter) → SCA ST+
└─ Pas de sus-décalage → SCA ST− suspecté
    ├─ Très haut risque → coronarographie < 2 h
    └─ hs-troponine H0/H1
        ├─ EXCLUSION (H0 très basse + douleur > 3 h, ou H0 basse + Δ non significatif)
        │     → autre diagnostic, test non invasif/coroscanner, sortie possible
        ├─ OBSERVATION → troponine H3, écho, réévaluation
        └─ INCLUSION (H0 élevée ou Δ significatif) → NSTEMI → haut risque → < 24 h
```

- Troponine élevée **≠ SCA** : EP, sepsis, IRC (élévation chronique), IC, myocardite, Takotsubo, tachyarythmie, AVC, dissection → raisonner sur la **cinétique** ; penser à l'**infarctus de type 2**.
- Sus-décalage en **aVR** + sous-décalage étendu → tronc commun/tritronculaire.

## 4. Traitement

```text
Traitement initial commun
├─ Aspirine pour tous
├─ Anticoagulant parentéral : HNF/énoxaparine si coronarographie rapide ;
│    FONDAPARINUX si coronarographie différée (> 24 h) + bolus d'HNF en salle
├─ Anti-ischémiques selon symptômes (nitrés, bêtabloquant si pas d'IC) ; O2 si SpO2 < 90 %
├─ P2Y12 APRÈS la coronarographie (pas de prétraitement si < 24 h ;
│    prétraitement envisageable si délai > 24 h et risque hémorragique non élevé)
└─ PAS DE FIBRINOLYSE
Revascularisation : angioplastie radiale + stent actif ; pontage si tronc commun /
pluritronculaire complexe (diabétique, dysfonction VG) — décision Heart Team
```

| Médicament | Charge | Entretien / remarques |
|---|---|---|
| Aspirine | 150–300 mg per os (75–250 mg IV) | 75–100 mg/j |
| Prasugrel | 60 mg | 10 mg/j (5 mg si ≥ 75 ans ou < 60 kg) ; CI si AVC/AIT ; préféré si angioplastie |
| Ticagrélor | 180 mg | 90 mg × 2/j |
| Clopidogrel | 300–600 mg | 75 mg/j ; si anticoagulant oral |
| HNF | Bolus IV 70–100 UI/kg pendant l'angioplastie (50–70 avec anti-GP IIb/IIIa) | En attente de coronarographie : bolus puis perfusion adaptée au TCA `[POSOLOGIE À VÉRIFIER — protocole local]` |
| Énoxaparine | 1 mg/kg SC/12 h | 1 mg/kg/24 h si clairance < 30 mL/min |
| Fondaparinux | 2,5 mg SC/24 h | CI si clairance < 20 mL/min |
| Bivalirudine | 0,75 mg/kg IV | puis 1,75 mg/kg/h |
| Anti-GP IIb/IIIa | — | **Uniquement en sauvetage** (« bailout ») |

**DAPT** : **12 mois** par défaut ; haut risque hémorragique → DAPT 1 mois puis monothérapie, ou désescalade vers le clopidogrel ; après 3–6 mois sans événement → monothérapie P2Y12 envisageable ; haut risque ischémique au-delà de 12 mois → aspirine + ticagrélor 60 mg × 2/j ou rivaroxaban 2,5 mg × 2/j (IIa). IPP si risque digestif.

**Patient en FA** : triple thérapie (AOD + aspirine + **clopidogrel**) **≤ 1 semaine** → AOD + clopidogrel **jusqu'à 12 mois** → AOD seul. AOD préférés aux AVK ; **pas de prasugrel ni de ticagrélor** en triple thérapie.

**Prévention secondaire** = celle du SCA ST+ : statine forte intensité (± ézétimibe, anti-PCSK9), bêtabloquant et IEC selon FEVG, ARM si FEVG ≤ 40 % + IC ou diabète, réadaptation, tabac, vaccin antigrippal.

## 5. Surveillance et complications

- USIC pour très haut/haut risque ; monitorage du rythme ≥ 24 h pour les NSTEMI à risque d'arythmie.
- ECG répétés, troponine (cinétique), **hémoglobine, plaquettes** (TIH sous HNF prolongée), créatinine (produit de contraste).
- Échocardiographie avant la sortie ; bilan lipidique à 4–6 semaines ; observance/tolérance de la DAPT, saignements.
- Risque hémorragique (ARC-HBR, PRECISE-DAPT) : âge ≥ 75 ans, anticoagulation orale, IR sévère, anémie, thrombopénie, cancer actif… — **l'hémorragie est un facteur pronostique majeur**.
- Populations : sujet âgé non fragile = même stratégie ; femme = symptômes atypiques ; IRC = cinétique de troponine, énoxaparine adaptée, éviter le fondaparinux si IR sévère.

## 6. Pièges classiques

1. **Exclure un SCA sur un ECG normal.**
2. Exclure un infarctus sur **une troponine unique** prélevée < 3 h après la douleur (hors seuil « très bas »).
3. Retenir un SCA devant **toute troponine élevée**.
4. **Fibrinolyser un SCA ST−.**
5. Méconnaître un **infarctus postérieur** (sous-décalage V1–V3).
6. **Prétraiter systématiquement par prasugrel** avant la coronarographie.
7. Oublier le **bolus d'HNF en salle** sous fondaparinux ; **changer d'anticoagulant** en cours de route.
8. Prescrire **prasugrel/ticagrélor en triple thérapie**, ou la prolonger sans raison.
9. **Bêtabloquant seul** dans un angor vasospastique ou lié à la cocaïne.
10. Confondre les délais : **< 2 h** (très haut risque) vs **< 24 h** (haut risque) ; négliger le risque hémorragique.

## 7. Moyens mnémotechniques (originaux)

- **« Très haut = 2, haut = 24 »** : coronarographie < 2 h vs < 24 h.
- **« Fonda attend, l'HNF entre en salle »** : fondaparinux si coronarographie différée, bolus d'HNF obligatoire à l'angioplastie.
- **« 3-5-7 avant le pontage »** : ticagrélor 3 j, clopidogrel 5 j, prasugrel 7 j.
- **« FA : 1 semaine à trois, 1 an à deux, puis seul »** : triple thérapie ≤ 1 semaine → AOD + clopidogrel jusqu'à 12 mois → AOD seul.
- **« ST− : artère ouverte, pas de lyse »** : thrombus plaquettaire **non occlusif** → antiagrégants au centre, fibrinolyse inutile et dangereuse.

## 8. Si je n'ai que 5 minutes

1. SCA ST− = ischémie sans sus-décalage persistant ; ECG normal possible.
2. NSTEMI = troponine ↑ avec cinétique ; angor instable = troponine normale.
3. Troponine hs 0 h/1 h : exclusion / observation / inclusion, seuils propres au dosage.
4. Troponine ↑ ≠ SCA (EP, sepsis, IRC, myocardite, type 2).
5. Très haut risque → < 2 h ; haut risque (NSTEMI, GRACE > 140) → < 24 h.
6. Aspirine + anticoagulant ; fondaparinux si délai, bolus d'HNF en salle.
7. P2Y12 après l'anatomie ; prasugrel préféré si angioplastie ; pas de fibrinolyse.
8. Anti-GP IIb/IIIa en sauvetage seulement.
9. DAPT 12 mois, adaptée au risque hémorragique ; FA : triple ≤ 1 semaine.
10. Pontage si tronc commun/pluritronculaire complexe (diabétique) ; prévention secondaire comme le ST+.

## 9. Sources (reprises du dossier DOS-CARD-0004)

- [S1] Byrne RA, et al. ESC 2023 — syndromes coronariens aigus. doi:10.1093/eurheartj/ehad191.
- [S2] Thygesen K, et al. 4e définition universelle de l'infarctus (2018). Eur Heart J 2019.
- [S3] Rao SV, et al. ACC/AHA 2025 — syndromes coronariens aigus. Circulation 2025.
- [S4] Collet JP, et al. ESC 2020 — SCA sans sus-décalage persistant du ST (remplacée par S1).
