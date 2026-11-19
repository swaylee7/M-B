# Rapport d'audit — DOS-IMMU-0001 « Système HLA »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-13
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_valide`** (0 critique, 1 majeure corrigée, 3 mineures ; aucun marqueur restant ; aucune posologie) — relecture enseignante requise pour `valide_enseignant`.

## Documents lus pendant l'audit (résumés PubMed)
- IPD-IMGT/HLA 2020 [S9] : plus de 25 000 allèles pour 45 gènes.
- PREDICT-1 [S13] : 1 956 patients ; prévalence de B*57:01 5,6 % ; réactions confirmées 0 % contre 2,7 %.
- CHU Mustapha [S17] : 1 082 sujets ; 20 allèles A, 31 B, 13 DRB1, 5 DQB1.
- Dahmani 2018 [S18] : 81 cas, 123 témoins ; OR de B27 = 14,62.
- Aribi 2004 [S19] : 39 cas, 52 témoins ; association DR4 > DR3DR4 ; DR3 non associé.
- Ouederni 2011 [S20] : 35 patients ; mutation fondatrice de RFXANK datée d'environ 2 250 ans.
- Concordance avec DOS-HEMA-0006 (accidents transfusionnels).

## Contrôles des points prioritaires
- Structure des classes I et II :
  - classe I : α1-α2, sillon fermé, peptides de 8 à 10 acides aminés, CD8 sur α3, β2m codée sur le chromosome 15 ;
  - classe II : α1-β1, sillon ouvert, peptides de 12 à 25 acides aminés, CD4 sur β2.
  **Conformes.**
- Voies de présentation (protéasome, TAP, tapasine, ERAP ; chaîne invariante, CLIP, HLA-DM), présentation croisée (cDC1) et autophagie : **conformes**.
- Restriction (Zinkernagel-Doherty 1974), sélection thymique, KIR/HLA-C/Bw4, NKG2A/HLA-E, « soi manquant » : **conformes**.
- Polymorphisme, codominance, haplotypes (25/50/25 %), déséquilibre de liaison, nomenclature à champs (suffixes N, L, S, Q) : **conformes**.
- Typage, anticorps sur billes « single antigen », crossmatch CDC et cytométrique, crossmatch virtuel, cPRA : **conformes**.
- Associations HLA-maladies : **conformes**.
  - B27 et spondyloarthrites ; B51 et Behçet ; DQ2/DQ8 et maladie cœliaque (VPN) ; DR3/DR4 et diabète de type 1.
  - Épitope partagé et PR ; DQB1*06:02 et narcolepsie ; A29 et birdshot.
- Pharmacogénétique : B*57:01-abacavir, B*15:02-carbamazépine (Han), A*31:01, B*58:01-allopurinol, B*57:01-flucloxacilline : **conformes**.

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 11.2 | Réactions fébriles non hémolytiques attribuées aux anticorps anti-HLA/HNA **du donneur** | **Majeure** | RFNH : anticorps anti-HLA du **receveur** et cytokines du produit, réduites par la déleucocytation ; TRALI : anticorps anti-HLA/HNA **du donneur** | Cohérence DOS-HEMA-0006 ; [S1, S2] |
| 13 | Mécanisme de l'abacavir attribué à PREDICT-1 [S13] | Mineure | Mécanisme sourcé [S1] ; PREDICT-1 = intérêt clinique | [S1], [S13] |
| 17 (Q2) | « Très probablement présents chez le père de ses enfants » (spéculatif) | Mineure | Origine possible des grossesses ou des transfusions, non attribuable | — |
| 21 | `[À VÉRIFIER — référentiels nationaux de greffe]` | Mineure | Reformulé : aucun référentiel national consulté ; protocoles des centres | — |

## Lot (QCM, cas)
- 13 QCM (QCM-IMMU-1301 à 1313) relus sans erreur ; 13/13 `audite_valide`.
- CAS-IMMU-1301 (donneur de CSH) : haplotypes et probabilité 1 − (3/4)³ ≈ 58 % exacts ; marqueur sans dose retiré ; `audite_valide`.
- CAS-IMMU-1302 (abacavir) : exact, sans correction ; `audite_valide`.

## Reste à faire
- Aucun point bloquant. Relecture enseignante.
- Facultatif : textes algériens sur l'organisation de la greffe (Agence nationale des greffes) si acquis.
