# Rapport d'audit — DOS-PHAR-0003 « Corticoïdes : principes et règles d'utilisation »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-14
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_corrections_requises`** (0 critique, 0 majeure, 12 mineures ; 0 marqueur de posologie restant sur 3)

## Documents consultés pendant l'audit
- Résumés PubMed : ACR 2022 sur l'ostéoporose cortico-induite (PMID 37884467 : évaluation précoce, traitement fortement recommandé dès un risque moyen) ; Buttgereit 2002 (PMID 12117678 : nomenclature des doses).
- Recherche web sur l'ESE/ES 2024 : dose physiologique = hydrocortisone 15–25 mg ≈ prednisone 4–6 mg ≈ méthylprednisolone 3–5 mg ≈ dexaméthasone 0,25–0,5 mg ; décroissance vers 4–6 mg de prednisone.
- Texte intégral ESE/ES 2024 (PMC11180513) : inaccessible pendant l'audit (Europe PMC en erreur, PMC bloqué).
- Catalogue : SSC 2026 (REC-0266) et GOLD 2025/2026 (REC-0242 remplacée).
- Dossier audité DOS-MINT-0001 (schémas de bolus EULAR 2023 et PNDS 2024).

## Divergence demandée : équivalence de la dexaméthasone
- **0,5 mg ≈ prednisone 5 mg** (ESE/ES 2024), cohérent avec la dose physiologique de l'ESE/ES (dexaméthasone 0,25–0,5 mg pour prednisone 4–6 mg) ;
- **0,75 mg ≈ prednisone 5 mg** dans les tables classiques (enseignement français) ; référence nationale non retrouvée `[À VÉRIFIER]`.
La divergence était déjà présentée (§ 7.1, § 21, QCM-PHAR-1425) ; elle a été complétée.

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 7.1 | Déflazacort : dose équivalente 7,5 mg mais « puissance relative 1 » (incohérent : 20/7,5 ≈ 2,7) | Mineure | Puissance ≈ 3 déduite ; valeur 7,5 mg vs 6 mg `[À VÉRIFIER — tableau ESE/ES 2024]` | — |
| 1 | Dose physiologique sans équivalents | Mineure | Méthylprednisolone 3–5 mg, dexaméthasone 0,25–0,5 mg | [S1] |
| 1 | Niveaux de dose `[À VÉRIFIER]` | Mineure | Sourcés (nomenclature EULAR, Buttgereit 2002) | [S13] |
| 11 (tableau), 18 | Seuil de l'insuffisance surrénale « 5–7,5 mg/j » vs « 4–6 mg/j » ailleurs | Mineure | Harmonisé sur 4–6 mg/j (ESE/ES 2024) | [S1] |
| 13.2 | Choc septique : seuil de vasopresseur `[À VÉRIFIER]` | Mineure | SSC 2021 : noradrénaline ou adrénaline ≥ 0,25 µg/kg/min depuis ≥ 4 h ; SSC 2026 signalée, non analysée | [S4] |
| 13.2 | Exacerbation de BPCO : marqueur | Mineure | 40 mg/j d'équivalent prednisone pendant 5 jours ; marqueur levé ; GOLD 2026 non relu | [S12] |
| 13.2 | Bolus « 500 mg à 1 g/j pendant 1 à 3 j » : marqueur | Mineure | EULAR 2023 (lupus) : 125–1 000 mg/j pendant 1–3 j ; PNDS 2024 : 500–1 000 mg/j pendant 3 j ; marqueur levé | [S14] |
| 13.2 | « Maladies inflammatoires » : marqueur sans dose | Mineure | Remplacé par des renvois aux dossiers spécialisés | — |
| 13.8 | « shour » | Mineure | « sahour » | — |
| 21 | Divergence sur la dexaméthasone | Mineure | Cohérence avec la dose physiologique ESE/ES ajoutée | [S1] |
| 22 | GOLD 2023 présenté comme en vigueur | Mineure | Noté « remplacé » (GOLD 2025, 2026) ; sources S13 et S14 ajoutées | — |
| Bandeau | Statut | Mineure | Mis à jour | — |

Vérifications sans anomalie : substitution (hydrocortisone 15–25 mg/j), crise surrénale (hydrocortisone 100 mg IV/IM puis 200 mg/24 h + sérum salé), doses de stress ESE/ES, cortisol matinal (> 300 / 150–300 / < 150 nmol/L), absence de fludrocortisone dans l'insuffisance cortico-induite, COVID-19 (dexaméthasone 6 mg/j, 10 jours), APROCCHSS, IPNA 2022, ACR 2022 (≥ 2,5 mg/j > 3 mois), règles de décroissance.

## Lots (QCM, cas)
- 12 QCM (QCM-PHAR-1425 à 1436) exacts ; QCM-PHAR-1436 : explication B harmonisée (4–6 mg/j). Tous `audite_valide`.
- CAS-PHAR-1405 et CAS-PHAR-1406 : conformes (ACR 2022, ESE/ES 2024), `audite_valide`.

## Restant à faire (motifs du verdict)
1. Relire le texte intégral de l'ESE/ES 2024 : tableau des équivalences (déflazacort, bétaméthasone), tableau des doses de stress (seuils au-delà desquels aucune dose supplémentaire n'est nécessaire).
2. SSC 2026 : place des corticoïdes et de la fludrocortisone dans le choc septique (actualité).
3. Référence française de l'équivalence 0,75 mg de la dexaméthasone ; rapport GOLD 2026.
4. Seuils de prophylaxie de la pneumocystose, contre-indication des vaccins vivants (seuil de dose et de durée), dépistage de l'anguillulose et de la tuberculose latente selon les protocoles algériens.
5. Relecture humaine qualifiée.
