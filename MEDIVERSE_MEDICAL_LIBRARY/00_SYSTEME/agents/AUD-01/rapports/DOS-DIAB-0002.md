# Rapport d'audit — DOS-DIAB-0002 « Complications aiguës du diabète : acidocétose, hypoglycémie, état hyperosmolaire »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-03.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Il reste 3 marqueurs posologiques (bicarbonate, glucose IV de l'hypoglycémie, octréotide).
- **Bilan** : 10 corrections (critiques 0, majeures 1, mineures 9).
- **Vérifications** : catalogue REC-INT (REC-0318 consensus 2024, REC-0319 ISPAD) ; 6 recherches web (critères de l'EHH, conduite JBDS sous 14 mmol/L, insuline SC, potassium, critères de résolution, JBDS EHH). WebFetch et Europe PMC inaccessibles depuis la session (hôtes hors du réseau autorisé).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 21, ligne « Insuline quand la glycémie passe sous ~14 mmol/L » | Divergence inventée : le JBDS était présenté comme maintenant 0,1 U/kg/h. En réalité, la révision JBDS 2021 (publiée en 2022) **envisage** aussi de réduire à 0,05 U/kg/h et ajoute du glucose 10 % à 125 mL/h. | **majeure** | Ligne réécrite : positions convergentes (réduction systématique dans le consensus, laissée au jugement clinique par le JBDS) ; cible 150–200 mg/dL. | [S1] ; [S4] ; parcours de soins JBDS (recherche web) |
| § 1.2 (critères de l'EHH) | Seuil de bicarbonates marqué « À VÉRIFIER » (15 ou 18 mmol/L). | mineure | Seuil **≥ 15 mmol/L** confirmé ; rappel que 18 mmol/L concerne le diagnostic et la résolution de l'ACD. | [S1] ; revue Cleveland Clin J Med 2025 (secondaire) |
| § 13.2 7) (résolution de l'ACD) | « Idéalement glycémie < 200 mg/dL » présenté comme un critère. La glycémie n'est plus un critère obligatoire depuis 2024. | mineure | Précision : critère du consensus 2009, souhaitable mais non obligatoire en 2024. | [S1] ; résumés secondaires concordants |
| § 20, QCM-DIAB-0017 (dossier et lot) | La proposition E (« glycémie idéalement < 200 mg/dL ») était comptée juste : formulation ambiguë. | mineure | E reformulée (« critère obligatoire »), comptée fausse ; réponses A, B ; explications mises à jour. | [S1] |
| § 13.3 5) (résolution de l'EHH) | Critères JBDS absents. | mineure | Ajout : glycémie < 15 mmol/L et retour à l'état cognitif antérieur (JBDS 2023). | [S5] |
| § 21 et § 22 (références JBDS) | Plusieurs positions JBDS (NaCl 0,9 %, poursuite de la basale) marquées « à vérifier ». | mineure | Marqueurs levés (positions JBDS établies) ; note de vérification ajoutée à S4. | [S4] |
| § 13.2 2) (insuline SC) | Doses absentes pour l'alternative sous-cutanée. | mineure | Ajout : **0,1 U/kg toutes les heures ou 0,2 U/kg toutes les 2 h** (ACD légère à modérée). | [S1] ; revue CCJM |
| § 13.2 5) (phosphates) | Risque de confusion d'unités avec le seuil historique. | mineure | Note : seuil 2024 < 1,0 mmol/L ; seuil 2009 < 1,0 mg/dL (≈ 0,32 mmol/L). | [S1] ; consensus ADA 2009 |
| § 13.3 2) (insuline de l'EHH) | Seuil de cétonémie du JBDS sans mention des versions. | mineure | Ajout : 0,05 U/kg/h ; le JBDS 2012 (encore repris localement) retenait > 1 mmol/L. | [S5] ; protocoles dérivés du JBDS |
| § 21 (nouvelle ligne) | Seuils potassiques du JBDS non comparés. | mineure | Ajout : JBDS K > 5,5 → pas de K⁺ ; 3,5–5,5 → 40 mmol/L. | [S1, S4] |

## Points vérifiés sans modification

- Critères D-K-A 2024 (≥ 200 mg/dL ou diabète connu ; β-OHB ≥ 3,0 ; pH < 7,30 et/ou HCO₃ < 18) ; gradation de sévérité ; osmolalité efficace > 300 et glycémie ≥ 600 mg/dL pour l'EHH.
- Insuline IV 0,1 U/kg/h ; glucose 5–10 % et 0,05 U/kg/h sous 250 mg/dL (13,9 mmol/L) ; potassium : insuline différée et KCl ~10 mmol/h si K < 3,5 ; bicarbonate seulement si pH < 7,0 ; résolution β-OHB < 0,6 + (pH ≥ 7,3 ou HCO₃ ≥ 18).
- Remplissage 500–1 000 mL/h × 2–4 h (bolus de 250 mL chez les fragiles) ; vitesses de correction de l'EHH (osmolalité 3–8 mOsm/kg/h, glycémie ≤ 5 mmol/L/h JBDS, natrémie ≤ 10 mmol/L/24 h) ; bilan positif de 3–6 L à 12 h.
- Hypoglycémie : niveaux 1–3 (ADA 2026), 15 g de glucose, glucagon 1 mg / 3 mg nasal / dasiglucagon 0,6 mg.
- Cas clinique (calculs : trou anionique 27, natrémie corrigée, 5,5 puis 2,75 U/h pour 55 kg) : exact.

## QCM et cas associés

- QCM-DIAB-0013 à 0024 : réponses exactes ; QCM-DIAB-0017 corrigé (voir ci-dessus). Tous passés en `audite_valide`.
- CAS-DIAB-0003 (ACD) et CAS-DIAB-0004 (EHH) : conformes ; `audite_valide`.

## Reste à faire

1. **Bicarbonate** (pH < 7,0) : schéma « 100 mmol dans 400 mL d'eau stérile » à confronter au texte intégral du consensus 2024 et aux présentations disponibles en Algérie (marqueur maintenu).
2. **Glucose IV de l'hypoglycémie en milieu de soins** et **octréotide** (hypoglycémie aux sulfamides) : protocole local ou recommandation JBDS sur l'hypoglycémie hospitalière à consulter (marqueurs maintenus).
3. Lire le texte intégral du consensus 2024 (pmc.ncbi.nlm.nih.gov à autoriser) pour confirmer la quantité de potassium par litre (20–30 mmol/L) et le délai de la basale avant l'arrêt de l'IV.
4. Données algériennes d'incidence de l'ACD/EHH : non trouvées.
5. Relecture enseignant (`valide_enseignant`).
