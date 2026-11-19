# Rapport d'audit — DOS-GAST-0003 « Rectocolite hémorragique »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01, AUD-02, AUD-04 (IA), indépendants du rédacteur DOS-04.
- **Objets audités** :
  - dossier v1.0 ;
  - QCM-GAST-0463…0474 ;
  - CAS-GAST-0453 et 0454 (lots DOS-04-lot2).
- **Verdict** : `audite_corrections_requises` (v1.1).
  - Aucune erreur critique ni majeure trouvée.
  - 15 corrections mineures.
  - Les 6 marqueurs de posologie sont levés.
  - Le verdict reste « corrections requises » pour deux raisons :
    - la stratégie médicale repose encore sur l'**ECCO 2022** et la **BSG 2019**, remplacées par l'ECCO 2026 et la BSG 2025, dont le texte intégral n'a pas pu être lu ;
    - l'instruction algérienne de 2024 sur l'ITL (S19) n'est pas relue.
- **Moyens de vérification** :
  - texte intégral de la BSG 2019 (PMC6872448), relu pour toutes les posologies qui lui sont attribuées : 5-ASA 2–3 g/j puis 4–4,8 g/j, suppositoire de 1 g, prednisolone 40 mg, méthylprednisolone 60 mg, ciclosporine 2 mg/kg, thiopurines, budésonide MMX 9 mg, définition de la CAG, vancomycine ;
  - résumé de l'essai ACT (PubMed) ;
  - livre AWaRe de l'OMS 2022 (DOC-00039, chapitre 33) ;
  - avis de la Commission de la transparence sur la Salazopyrine (HAS 2014, PDF lu) ;
  - métadonnées PubMed des ECCO 2026 (jjag066, jjag071, jjag072), de l'ACG 2025 et de la BSG 2025 ;
  - recherche web : RCP de Simponi, Stelara, Rinvoq et Skyrizi ; extraits de la BSG 2025 ; communiqué de l'ECCO sur les infections.
- **Hôtes inaccessibles** : orbi.uliege.be, res.cloudinary.com, ueaeprints.uea.ac.uk, eprints.whiterose.ac.uk (PDF des ECCO 2026 et de la BSG 2025), ema.europa.eu.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 7.3, § 12.2, § 17 Q4, § 18, § 20 (QCM 3), § 21 | La CAG était définie par « > 6 selles » alors que le tableau du § 7.3 et Montréal S3 indiquent « ≥ 6 ». La source de l'écart n'était pas signalée | mineure | Divergence explicitée : Montréal (et le tableau) retiennent ≥ 6, la BSG 2019 écrit « > 6 » (Statement 15, texte vérifié) ; à 6 selles sanglantes avec un signe systémique, traiter comme une CAG | [S5, S9] |
| § 13.2.1 | Sulfasalazine sous marqueur | mineure (AUD-02) | Attaque 4–6 g/j en 3–6 prises ; entretien 2 g/j | HAS CT 2014 / RCP [S26] |
| § 13.2.2 | Budésonide MMX sous marqueur | mineure (AUD-02) | 9 mg/j pendant 8 semaines (essais CORE ; recommandation forte de la BSG 2019 ; 6 mg inefficace) | [S5, S27] |
| § 13.2.6 | Rythme d'entretien de l'infliximab sous marqueur | mineure (AUD-02) | Toutes les 8 semaines (protocole ACT) | [S12, S27] |
| § 13.2.6 | Golimumab « selon le RCP » | mineure (AUD-02) | 200 mg à S0, 100 mg à S2, puis 50 mg toutes les 4 semaines si < 80 kg ou 100 mg si ≥ 80 kg (RCP britannique) | [S27] |
| § 13.2.6 | Entretien de l'ustékinumab sous marqueur | mineure (AUD-02) | 90 mg SC à S8, puis toutes les 12 semaines, ou toutes les 8 semaines en cas de perte de réponse | RCP [S27] |
| § 13.2.6 | Upadacitinib et risankizumab sans dose | mineure (AUD-02) | Upadacitinib : 45 mg/j × 8 semaines, puis 15 ou 30 mg/j (15 mg au maximum après 65 ans). Risankizumab : 1 200 mg IV à S0-S4-S8, puis 180 mg SC (360 mg si amélioration insuffisante) toutes les 8 semaines | RCP [S27] |
| § 13.3.3 | Vancomycine orale sous marqueur | mineure (AUD-02) | 125 mg × 4/j pendant 10 jours, jusqu'à 500 mg × 4/j dans les formes graves ; sans interrompre les corticoïdes | AWaRe 2022 [S25] ; BSG 2019 |
| Bandeau | Actualité non vérifiée | mineure (AUD-04) | ECCO 2026 (médical, chirurgical, infections), BSG 2025 et ACG 2025 : existence et métadonnées vérifiées | PubMed |
| § 13.2.7 | Contenu de l'ECCO 2026 sur les infections inconnu ; BSG 2025 absente | mineure | ECCO 2026 : structure (4 groupes de travail, algorithmes vaccinaux). BSG 2025 : prophylaxie thromboembolique pour toute hospitalisation, coprocultures, corticoïdes avant chirurgie | [S17, S6] |
| § 13.2.7 | Vaccin antipneumococcique sans rappel | mineure | Rappel après 5 ans (BSG 2025) | [S6] |
| § 21 | Divergences à actualiser | mineure | Lignes « version de référence », « définition de la colite grave », « infections » et « pneumocoque » | — |
| YAML, § 22 | Sources manquantes | mineure (traçabilité) | Ajout de S25 (AWaRe), S26 (HAS Salazopyrine) et S27 (RCP) ; statut de S2 précisé | — |
| QCM-GAST-0465 | « > 6 selles » dans l'explication | mineure | Seuil ≥ 6 et libellé de la BSG précisés | [S5, S9] |
| CAS-GAST-0454 | Vaccin antipneumococcique | mineure | Rappel après 5 ans (BSG 2025). Statut `audite_corrections_requises` maintenu à cause de l'ITL (instruction nationale à confirmer, comme dans DOS-RHUM-0001) | [S6] |

## Scores contrôlés

- **Montréal E1–E3, S0–S3** : exact.
- **Mayo** : 4 items cotés 0–3, total 0–12, score partiel 0–9 ; définition de la rémission d'usage. Calcul du cas (8) exact.
- **Truelove-Witts modifiés (BSG)** : exact. Seuils de la publication de 1955 `[À VÉRIFIER]`.
- **Critères d'Oxford** : J3, > 8 selles, ou 3–8 selles avec CRP > 45 mg/L.
- **Scores de Ho et de Lindgren** ; **PUCAI ≥ 65** ; **Lichtiger > 10** (CYSIF).
- **Essais** : CYSIF (60 % contre 54 %), UC SUCCESS, Eaden (2/8/18 %) exacts.

## QCM et cas

- QCM-GAST-0463…0474 : réponses exactes → `audite_valide`.
- CAS-GAST-0453 → `audite_valide`.
- CAS-GAST-0454 → `audite_corrections_requises` (ITL).

## Reste à faire

1. **Lire l'ECCO 2026 (jjag066), la BSG 2025 et l'ACG 2025** :
   - mettre à jour la stratégie (place des thérapies avancées, CAG, désescalade) ;
   - préciser la place des anti-IL-23 et des modulateurs de S1P.
2. Lire l'ECCO 2026 « infections » : schéma de l'ITL, délai avant biothérapie, *C. difficile*.
3. Lire l'instruction ministérielle algérienne ITL 2024 (S19).
4. Seuils de 1955 (température), définition du Mayo modifié, modalités de surveillance de la CSP (ECCO 2023, texte intégral).
5. Données épidémiologiques algériennes ; disponibilité des biothérapies.
6. Relecture par un enseignant.
