---
id: FIC-NEON-0002
titre: "Fiche — Infections néonatales"
specialite: NEON
items_residanat: [RES-MED-081]
dossier_source: DOS-NEON-0002
version_dossier_source: "1.2"
revisions:
  - date: 2026-11-19
    auteur: "AUD-05 (IA)"
    objet: "Version source mise à jour (DOS-NEON-0002 v1.2 : avertissement de vérification actualisé, attribution de la définition « triple I » corrigée)."
    rapport: 00_SYSTEME/agents/AUD-05/rapports/COHERENCE_2026-11-19.md
langue: fr
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent RES-06 (IA) — fiche dérivée du dossier audité"
statut: brouillon_a_auditer
sources:
  - id: S1
    reference: "Société française de néonatologie, Société française de pédiatrie. Prise en charge du nouveau-né à risque d'infection néonatale bactérienne précoce (≥ 34 SA). Recommandation de bonne pratique, septembre 2017, ayant reçu le label méthodologique de la HAS (décision n° 2017.0098/DC/SBPP du 12 juillet 2017) ; actualise les recommandations ANAES 2002. Existence confirmée par recherche web (audit AUD-01) ; désignée « HAS 2017 » dans le texte."
    organisme: SFN/SFP (label HAS)
    annee: 2017
    type: recommandation
    doi: ""
    url: "https://www.has-sante.fr/jcms/c_2803349/"
    verifiee: true
  - id: S2
    reference: "National Institute for Health and Care Excellence. Neonatal infection: antibiotics for prevention and treatment. NICE guideline NG195. Londres : NICE ; avril 2021 (remplace CG149, 2012 ; mises à jour ultérieures). Existence, posologies de benzylpénicilline et de gentamicine et liste des drapeaux rouges confirmées par recherche web (audit AUD-01)."
    organisme: NICE
    annee: 2021
    type: recommandation
    doi: ""
    url: "https://www.nice.org.uk/guidance/ng195"
    verifiee: true
  - id: S3
    reference: "Puopolo KM, Benitz WE, Zaoutis TE; Committee on Fetus and Newborn; Committee on Infectious Diseases. Management of neonates born at ≥35 0/7 weeks' gestation with suspected or proven early-onset bacterial sepsis. Pediatrics. 2018;142(6):e20182894."
    organisme: AAP
    annee: 2018
    type: recommandation
    doi: ""
    url: ""
    verifiee: false
  - id: S8
    reference: "Organisation mondiale de la Santé. Pocket book of hospital care for children. 2e éd. Genève : OMS ; 2013 (chapitre 3 : problèmes du nouveau-né et du jeune nourrisson ; section 3.14, doses des médicaments usuels du nouveau-né). ISBN 978 92 4 154837 3. Document acquis DOC-00063 (stockage local) — texte lu par l'audit."
    organisme: OMS
    annee: 2013
    type: recommandation
    doi: ""
    url: ""
    verifiee: true
  - id: S11
    reference: "Kimberlin DW, Lin CY, Jacobs RF, et al. Safety and efficacy of high-dose intravenous acyclovir in the management of neonatal herpes simplex virus infections. Pediatrics. 2001;108(2):230-238. PMID 11483782 (existence et schéma 60 mg/kg/j en 3 doses confirmés par recherche web, audit AUD-01)."
    organisme: ""
    annee: 2001
    type: article
    doi: ""
    url: "https://pubmed.ncbi.nlm.nih.gov/11483782/"
    verifiee: true
  - id: S15
    reference: "Organisation mondiale de la Santé. WHO recommendations for management of serious bacterial infections in infants aged 0–59 days. Genève : OMS ; 2024. ISBN 978-92-4-010290-3. Document acquis DOC-00052 (texte lu par l'audit)."
    organisme: OMS
    annee: 2024
    type: recommandation
    doi: ""
    url: ""
    verifiee: true
---

# Fiche — Infections néonatales (RES-MED-081)

> Fiche de révision **dérivée exclusivement** du dossier audité DOS-NEON-0002 (v1.2, statut `audite_corrections_requises`). Aucun fait nouveau ; doses identiques au dossier (doses dépendant de l'âge gestationnel, de l'âge postnatal et du poids). Références : **SFN/SFP-HAS 2017** [S1], **NICE NG195 (2021)** [S2], **AAP 2018** [S3], **OMS** (Pocket book 2013 [S8], recommandations 2024 [S15]). Recommandations nationales algériennes non identifiées `[À VÉRIFIER — ACQ-01, ACQ-03, REC-01]`.

## 1. Définition (2 lignes)

Infection survenant pendant les **28 premiers jours de vie**. **Précoce** (< 72 h ; < 7 j pour CDC/AAP) = **materno-fœtale** ; **tardive** (≥ 72 h) = **nosocomiale** ou communautaire. Prouvée (germe sur site stérile), probable (clinique + biologie, cultures négatives), nouveau-né « à risque » (facteurs sans signe).

## 2. Chiffres et critères à connaître

| Germe | Précoce | Tardive | À retenir |
|---|---|---|---|
| **Streptocoque B** | **1er à terme** | SGB tardif (7 j–3 mois) : **méningite**, ostéo-arthrite | Portage 10–30 % `[À VÉRIFIER]` ; sensible pénicilline/amoxicilline |
| ***E. coli*** (K1) | **1er chez le prématuré** | Méningite, **infection urinaire** | Résistances (ampicilline, **BLSE**) |
| ***Listeria*** | LA **teinté** chez un prématuré, syndrome pseudo-grippal maternel | Méningite | **Résistance naturelle aux céphalosporines** |
| SCN, *S. aureus* | Rares | **1er nosocomial** (cathéter central) | Méti-R fréquents |
| Entérobactéries, *Pseudomonas*, *Acinetobacter*, *Candida* | — | Nosocomiales | **Multirésistance** ; *Candida* : grands prématurés |
| HSV, entérovirus, paréchovirus | HSV per-partum | Jusqu'à 6 semaines (HSV) | Tableau de sepsis |

| Repère | Valeur |
|---|---|
| Facteurs de risque précoces | **Portage SGB sans APP adéquate**, bactériurie SGB, **antécédent d'enfant infecté**, **fièvre maternelle ≥ 38 °C** / chorioamniotite (le plus fort), **RPM ≥ 12 h (HAS) / ≥ 18 h (CDC/AAP)** `[seuils À VÉRIFIER]`, **prématurité spontanée**, infection invasive maternelle, jumeau infecté |
| Drapeaux rouges NICE NG195 | Jumeau infecté ; **apnée, convulsions, réanimation cardiopulmonaire, ventilation mécanique, choc** → 1 drapeau rouge ou ≥ 2 autres facteurs = hémoculture + antibiotiques ; 1 autre facteur = surveillance 12 h |
| PCIME (0–59 j, PSBI) | S'alimente mal, convulsions, FR ≥ 60/min (0–6 j), tirage sous-costal marqué, **T ≥ 38 °C ou < 35,5 °C**, ne bouge que stimulé |
| Hémoculture | **≥ 1 mL**, avant antibiotiques ; positive en 24–36 h |
| CRP | Monte à **6–12 h**, pic 36–48 h ; **2 CRP < 10 mg/L à 24 h d'intervalle** + cultures − = arrêt |
| PCT | Monte à 3–4 h ; pic physiologique 24–48 h (normes horaires) |
| NFS | Leucocytes < 5 000, PNN < 1 500/mm³, I/T > 0,2, thrombopénie : évocateurs, **peu sensibles** |
| LCR néonatal | ≤ 15–20 éléments/mm³, protéines ≤ 1–1,5 g/L, glycorachie ≥ 60–70 % `[seuils À VÉRIFIER]` |
| Méningite associée | 10–20 % des bactériémies `[À VÉRIFIER]` |
| APP adéquate | β-lactamine débutée **≥ 4 h** avant la naissance |

## 3. Démarche diagnostique

```text
« Tout nouveau-né qui va mal est infecté jusqu'à preuve du contraire »
Signes : fièvre OU HYPOTHERMIE (< 36 °C), refus de téter, léthargie, détresse respiratoire,
         apnées, FC > 160, TRC > 3 s, teint gris, marbrures, intolérance digestive,
         convulsions, fontanelle bombée, purpura, ictère précoce, hypo/hyperglycémie, acidose
│
├─ Symptomatique → HÉMOCULTURE (≥ 1 mL) ± PL (si stable) → ANTIBIOTIQUES IMMÉDIATS
│     CRP H0 (référence) puis 24–48 h ; ECBU seulement si > 72 h
│     PL : hémoculture +, signes neurologiques, sepsis — DIFFÉRÉE si instabilité,
│          sans jamais retarder les antibiotiques
├─ Asymptomatique à risque (≥ 34–35 SA)
│     ├─ chorioamniotite / drapeau rouge → conduite active (hémoculture ± ATB, calculateur)
│     └─ autres → surveillance clinique standardisée 48 h (HAS) ou calculateur de Kaiser (AAP)
└─ Prélèvements périphériques et liquide gastrique : ABANDONNÉS (HAS 2017)
```

Différentiels : tachypnée transitoire, maladie des membranes hyalines, inhalation méconiale, **cardiopathie ducto-dépendante** (choc J2–J10, pouls fémoraux faibles → PGE1), **maladies du métabolisme** (intervalle libre, hyperammoniémie), **hyperplasie des surrénales** (J7–J15, hypoNa + hyperK), hypoglycémie/hypocalcémie, hémorragie intracrânienne, sevrage.

## 4. Traitement

### Probabiliste

| Situation | HAS 2017 | NICE 2021 | OMS |
|---|---|---|---|
| Précoce sans méningite | **Amoxicilline + gentamicine** | **Benzylpénicilline + gentamicine** | Ampicilline (ou pénicilline) + gentamicine, ≥ 10 j si sepsis (2024) |
| Méningite / sepsis grave / BGN | **Amoxicilline + céfotaxime** (± gentamicine) | Céfotaxime + amoxicilline `[À VÉRIFIER]` | Ampicilline, céfotaxime ou ceftriaxone + gentamicine ≥ 3 semaines |
| Tardive communautaire | Amoxicilline + céfotaxime (± aminoside) `[À VÉRIFIER — S2]` ; chercher une IU | | |
| Tardive nosocomiale | Vancomycine + anti-Gram négatif selon l'**écologie de l'unité** (carbapénème si BLSE) ; retrait du cathéter ; antifongique si risque | | |
| Suspicion d'herpès | **+ aciclovir sans attendre** (vésicules, convulsions, hépatite, CIVD, LCR lymphocytaire sans germe) | | |

### Molécules (nouveau-né à terme, 1re semaine)

| Molécule | Posologie (dossier) |
|---|---|
| Amoxicilline/ampicilline | **50 mg/kg/dose IV/IM /12 h la 1re semaine, /8 h ensuite** (OMS 2013/2024) ; méningite : OMS 2024 même dose ≥ 3 semaines, nombreux protocoles ≈ 100 mg/kg/dose `[POSOLOGIE À VÉRIFIER — dose méningée ; RCP / protocole local]` |
| Benzylpénicilline | NICE **25 mg/kg/dose /12 h** (/8 h si très malade) ; OMS **50 000 UI/kg/dose /12 h** la 1re semaine, /6 h ensuite |
| Gentamicine | NICE **5 mg/kg, 2e dose à 36 h** (hors AMM), selon taux résiduel ; OMS **5 mg/kg/24 h** (**3 mg/kg/24 h** petit poids), **7,5 mg/kg/24 h** après la 1re semaine ; **taux résiduels** |
| Céfotaxime | **50 mg/kg/dose** ; /12 h la 1re semaine puis /6 h (OMS 2024, méningite) — Pocket book 2013 : /12 h prématuré, /8 h à terme 1re semaine, /6 h de 2 à 4 semaines ; doses méningées majorées `[POSOLOGIE À VÉRIFIER — dose méningée]` ; inactif sur *Listeria*/entérocoques |
| Ceftriaxone | **Évitée** si ictère (déplace la bilirubine), **contre-indiquée** avec le calcium IV |
| Vancomycine, méropénem, fluconazole/amphotéricine B | Selon protocole `[POSOLOGIE À VÉRIFIER]` |
| **Aciclovir** | **20 mg/kg /8 h IV** (60 mg/kg/j) : **21 j** (neurologique, disséminé), **14 j** (cutanéo-oculo-buccal) ; surveiller rein et **neutrophiles** |
| Symptomatique | NaCl 0,9 % **10–20 mL/kg** en 10–20 min (prudence) puis amines `[POSOLOGIE À VÉRIFIER — protocole de réanimation néonatale]` ; hypoglycémie (< 2,2 mmol/L, OMS) : **G10 % 2 mL/kg IV** puis ≈ 5 mL/kg/h |

### Durées

| Situation | Durée |
|---|---|
| Asymptomatique/amélioré, hémoculture −, CRP normales | **Arrêt à 36 h (NICE) – 48 h (HAS)** |
| Infection probable | 5–7 j `[À VÉRIFIER]` |
| Bactériémie sans méningite | **7–10 j** (SGB souvent 10 j) `[À VÉRIFIER]` |
| Méningite SGB / BGN / *Listeria* | **≥ 14 j / ≥ 21 j** (PL de contrôle, imagerie) / 14–21 j `[À VÉRIFIER]` |
| Herpès | 14 j / 21 j |

## 5. Surveillance, complications, prévention

- Clinique rapprochée ; CRP 24–48 h ; hémocultures de contrôle si bactériémie ; **taux d'aminoside/vancomycine** ; méningite à BGN : PL à 48–72 h, ETF/IRM, PC ; **dépistage auditif** et suivi neurodéveloppemental.
- Complications : choc, HTAP persistante, **CIVD**, ECUN, ventriculite, abcès (*E. coli* K1), hydrocéphalie, **surdité**, épilepsie ; iatrogènes (aminosides, résistances, candidose).
- **Prévention SGB** : dépistage **36⁰–37⁶ SA** (ACOG 2020 ; 35–37 SA CDC 2010) `[politique algérienne À VÉRIFIER]` ; **APP** si portage, bactériurie SGB, antécédent d'enfant infecté, statut inconnu + facteur (< 37 SA, RPM ≥ 18 h, T ≥ 38 °C) ; **pas d'APP** pour césarienne programmée avant travail à membranes intactes ; pénicilline G ≈ 5 MUI puis 2,5–3 MUI /4 h ou amoxicilline 2 g puis 1 g /4 h ; allergie : céfazoline, clindamycine ou vancomycine `[POSOLOGIE À VÉRIFIER — protocole obstétrical]`.
- **Nosocomiales** : **hygiène des mains** (mesure n° 1), bundles cathéters, lait maternel, kangourou, durées courtes.
- **Algérie** : **BCG + VHB à la naissance** ; mère AgHBs+ → vaccin + IgHBs ≤ 12 h `[protocole et disponibilité nationaux À VÉRIFIER]` ; **tétanos néonatal, listériose, syphilis, infections à BMR** à **déclaration obligatoire** (décret 22-250) ; prévention du tétanos néonatal par dT maternel et soins propres du cordon.

## 6. Pièges classiques

1. Attendre la **fièvre** (l'hypothermie est aussi évocatrice).
2. Antibiotiques **avant l'hémoculture** ou volume < 1 mL.
3. **Retarder l'antibiothérapie** pour une PL chez un enfant instable.
4. Se rassurer sur une **CRP normale à H0**.
5. **Céphalosporine seule** (inactive sur *Listeria* et entérocoques).
6. **Ceftriaxone** chez un nouveau-né ictérique ou sous calcium IV.
7. **ECBU** dans une infection précoce (< 72 h).
8. Poursuivre **7–10 j** chez un enfant non infecté (cultures −, CRP normales).
9. Juger adéquate une APP débutée **< 4 h** avant la naissance ; APP pour **césarienne programmée à membranes intactes**.
10. Oublier l'**herpès** (sepsis à cultures négatives + convulsions/hépatite, sans lésion cutanée) ; négliger les **taux d'aminosides** et l'audition.

## 7. Moyens mnémotechniques (originaux)

- **« B à terme, E chez le prématuré, L dans le liquide teinté »** (SGB, *E. coli*, *Listeria*).
- **« Listeria se moque des céphalos »** → toujours l'amoxicilline dans le probabiliste précoce.
- **« 72 h sépare la mère de l'hôpital »** : < 72 h materno-fœtale, ≥ 72 h nosocomiale/communautaire.
- **« Deux CRP calmes, cultures muettes : on arrête à 48 h »**.
- **« APP : 4 heures ou rien »**.
- **« 14 pour le B, 21 pour le Gram − et l'herpès profond »** (durées des méningites et de l'herpès neurologique/disséminé).

## 8. Si je n'ai que 5 minutes

1. Précoce < 72 h (SGB, *E. coli*, *Listeria*) ; tardive ≥ 72 h (SCN, BGN multirésistants, *Candida*).
2. FdR : SGB sans APP, fièvre maternelle/chorioamniotite, RPM prolongée, prématurité, enfant antérieur infecté.
3. Signes non spécifiques, hypothermie incluse.
4. Hémoculture ≥ 1 mL avant ATB ; PL si possible ; ECBU seulement après 72 h.
5. Amoxicilline + gentamicine ; + céfotaxime si méningite ou sepsis grave.
6. CRP retardée (6–12 h) ; 2 CRP normales + cultures − → arrêt à 36–48 h.
7. Bactériémie 7–10 j ; méningite SGB ≥ 14 j, BGN ≥ 21 j ; aciclovir 20 mg/kg/8 h.
8. Asymptomatique à risque : surveillance standardisée 48 h ou calculateur.
9. APP ≥ 4 h avant la naissance ; pas pour césarienne programmée membranes intactes.
10. Hygiène des mains ; BCG + VHB à la naissance ; déclaration obligatoire (tétanos néonatal, listériose, syphilis, BMR).

## 9. Sources (reprises du dossier DOS-NEON-0002)

- [S1] SFN/SFP (label HAS). Nouveau-né à risque d'infection néonatale bactérienne précoce (≥ 34 SA), 2017.
- [S2] NICE NG195 — *Neonatal infection: antibiotics for prevention and treatment*, 2021.
- [S3] Puopolo KM, et al. AAP — nouveau-nés ≥ 35 SA, 2018 (non vérifiée en session).
- [S8] OMS. *Pocket book of hospital care for children*, 2ᵉ éd., 2013, chapitre 3 (DOC-00063).
- [S11] Kimberlin DW, et al. Aciclovir à forte dose. *Pediatrics* 2001.
- [S15] OMS. *Recommendations for management of serious bacterial infections in infants aged 0–59 days*, 2024 (DOC-00052).
