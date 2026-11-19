# Rapport d'audit — DOS-PHAR-0002 « Anticoagulants : principes, modalités de surveillance, règles d'utilisation »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-14
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_corrections_requises`** (0 critique, 4 majeures, 17 mineures ; 2 marqueurs de posologie restants sur 9)

## Documents consultés pendant l'audit
- Liste modèle OMS 2025, section 10.2 (document acquis, pdftotext) : contenu cité conforme.
- Résumés PubMed (eutils) : ACCP 2012 « Parenteral anticoagulants » (Garcia, PMID 22315264) ; ACCP 2012 « Evidence-based management of anticoagulant therapy » (Holbrook, PMID 22315259 : génotypage non recommandé, grade 1B) ; ESC/EACTS 2025 valvulopathies (PMID 40878295, sans résumé).
- Recherches web : harmonisation européenne du RCP de Lovenox (Vidal) ; retrait de l'andexanet du marché américain (AABB 23/12/2025, communication FDA du 18/12/2025) ; ESC/EACTS 2025 (synthèses : AVK à vie, cibles d'INR individualisées ; tableau chiffré non trouvé).
- Inaccessibles : texte intégral EHRA 2021 (Europe PMC en erreur 500), academic.oup.com, EMA, base publique des médicaments, Vidal.

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 5.2 | HBPM « contre-indiquées à dose curative dans la plupart des RCP » sous 30 mL/min : obsolète pour l'énoxaparine | **Majeure** | RCP européen harmonisé : 15–30 mL/min → curatif 100 UI/kg × 1/j, préventif 2 000 UI/j ; < 15 mL/min non recommandé ; autres HBPM selon RCP ; HNF souvent préférée | RCP [S26] |
| 10.1 (tableau rénal) | Même erreur ; ligne préventive absente | **Majeure** | Lignes HBPM curative et préventive réécrites | [S26] |
| 10.1 (tableau rénal) | Fondaparinux curatif « dose réduite selon RCP » entre 30 et 50 mL/min : inexact | **Majeure** | Curatif : pas de réduction (7,5 mg à envisager après 10 mg si > 100 kg), contre-indiqué < 30 ; préventif 1,5 mg/j entre 20 et 50 mL/min, contre-indiqué < 20 | RCP Arixtra [S26] |
| 5.5, 13.4.4, 17, 18, 21 | Andexanet présenté sans l'actualité 2025 | **Majeure** (actualité) | Retrait du marché américain (décembre 2025) après la communication de sécurité de la FDA (thromboses) ; AMM européenne limitée à l'apixaban et au rivaroxaban ; CCP 50 UI/kg à défaut | AABB/FDA [S25], ANNEXA-I [S17], EHRA [S5] |
| 13.2.1 | Énoxaparine 1,5 mg/kg × 1/j : marqueur | Mineure | Marqueur levé : schéma réservé par le RCP harmonisé au patient non compliqué à faible risque de récidive ; AMM nationale à vérifier | ESC 2019 [S2], RCP [S26] |
| 13.2.2 | Énoxaparine 20 mg (chirurgie à risque modéré) : marqueur | Mineure | Marqueur levé ; 40 mg en chirurgie à haut risque ; 20 mg si 15–30 mL/min | [S26] |
| 13.2.2 | Fondaparinux 2,5 mg : marqueur | Mineure | Marqueur levé ; 1,5 mg si 20–50 mL/min ; contre-indiqué < 20 | [S26] |
| 13.2.2 | HNF SC 5 000 UI : marqueur | Mineure | 5 000 UI toutes les 8 à 12 h ; marqueur levé | ACCP 2012 [S23] |
| 13.4.1 | Protamine (HNF) : marqueur | Mineure | 1 mg/100 UI d'HNF des 2–3 h précédentes (ex. 1 250 UI/h → ≈ 30 mg), IV lente, ≤ 50 mg par injection ; marqueur levé | [S23] |
| 13.4.1 | Protamine (HBPM) : marqueur | Mineure | < 8 h : 1 mg/100 UI anti-Xa ; seconde dose 0,5 mg/100 UI ; neutralisation ≤ 60 % ; marqueur levé | [S23] |
| 13.4.4 | CCP pour les anti-Xa : marqueur | Mineure | 50 UI/kg (+ 25 UI/kg si besoin), 25–50 UI/kg selon les protocoles ; marqueur levé | EHRA 2021 [S5] |
| 5.5 | Antidote de l'édoxaban | Mineure | Aucun antidote autorisé dans l'UE ; à vérifier sur le RCP | [S25] |
| 9.3 | Cibles d'INR des valves mécaniques approximatives | Mineure | Tableau ESC/EACTS 2021 (thrombogénicité × facteurs de risque, 2,5 à 4) et facteurs de risque ; 2025 : AVK à vie réaffirmés, valeurs à confirmer | [S19, S24] |
| 8.2 | Génotypage VKORC1/CYP2C9 attribué à l'ASH 2018 [À VÉRIFIER] | Mineure | ACCP 2012, grade 1B | [S13] |
| 9.2 | Anti-Xa de l'HNF 0,3–0,7 UI/mL [À VÉRIFIER] | Mineure | Sourcé | [S23] |
| 13.2.4 | Critères du dabigatran 110 mg incomplets | Mineure | « À envisager » : 75–80 ans, clairance 30–50, gastrite/RGO, risque hémorragique | RCP, EHRA [S5] |
| 13.2.4 (MTEV) | Édoxaban 30 mg « si clairance 30–50 » | Mineure | 15–50 mL/min, poids ≤ 60 kg ou inhibiteurs de la P-gp | RCP |
| 13.3.3 | Relais AVK → AOD : seuils des RCP non précisés | Mineure | Dabigatran et apixaban < 2 ; édoxaban ≤ 2,5 ; rivaroxaban ≤ 3 (FA) / ≤ 2,5 (MTEV) | RCP, EHRA [S5] |
| 10.1 | Apixaban 15–29 mL/min [À VÉRIFIER] | Mineure | 2,5 mg × 2 (RCP européen) | [S1, S5] |
| 16.1, 18, 19 | Algorithme, point clé 3 et piège alignés sur la correction rénale ; point clé 10 complété (idarucizumab 5 g, CCP 50 UI/kg) | Mineure | Réécrits | [S5, S26] |
| 3, 21, 22 | « Chapitre » 10.2 → section ; divergences (andexanet, cibles d'INR) ; sources S23–S26 ; points restants | Mineure | Ajouts | — |

## Lots (QCM, cas)
- **QCM-PHAR-1424** (interactions des AVK) : **corrigé erroné** — la rifampicine (inducteur) était marquée « augmente l'INR » et le fluconazole « faux », contrairement aux explications. Réponses corrigées : **A, B, D** (majeure).
- QCM-PHAR-1423 (TVP et clairance 20 mL/min) : proposition B précisée (« dose curative usuelle ») et explications alignées sur le RCP européen de l'énoxaparine (mineure).
- Les 10 QCM intégrés (QCM-PHAR-1413 à 1422) sont conformes au dossier ; 12/12 `audite_valide`.
- CAS-PHAR-1403 (EP non provoquée) : conforme, `audite_valide`. CAS-PHAR-1404 (TIH) : score 4T et conduite conformes ; marqueur de posologie maintenu (argatroban, bivalirudine, danaparoïde) → `audite_corrections_requises`.

## Restant à faire (motifs du verdict)
1. Marqueurs de posologie restants : anticoagulants de la TIH (argatroban, bivalirudine, danaparoïde) ; dose initiale de warfarine en pratique française et algérienne.
2. Vérifier sur les RCP en vigueur (EMA, ANSM) et l'AMM algérienne : schéma d'énoxaparine en une injection, ajustements rénaux de l'énoxaparine et du fondaparinux (source S26 marquée `verifiee: false`).
3. Lire le tableau des cibles d'INR du texte intégral ESC/EACTS 2025.
4. Statut européen de l'andexanet et disponibilité en Algérie de l'idarucizumab, de l'andexanet et des CCP.
5. Recommandation AHA/ACC 2026 sur l'embolie pulmonaire (catalogue REC-0221) non analysée.
6. Relecture humaine qualifiée (statut `valide_enseignant`).
