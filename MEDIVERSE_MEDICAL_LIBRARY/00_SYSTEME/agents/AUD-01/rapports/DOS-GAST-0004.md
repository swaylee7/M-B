# Rapport d'audit — DOS-GAST-0004 « Maladie de Crohn »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01, AUD-02, AUD-04 (IA), indépendants du rédacteur DOS-04.
- **Objets audités** :
  - dossier v1.0 ;
  - QCM-GAST-0475…0486 ;
  - CAS-GAST-0455 et 0456 (lots DOS-04-lot2).
- **Verdict** : `audite_corrections_requises` (v1.1).
  - Aucune erreur critique.
  - Une erreur majeure dans le lot de cas, corrigée.
  - 12 corrections au total.
  - 4 marqueurs de posologie levés sur 5. Reste : les antibiotiques des lésions anopérinéales.
  - Le texte intégral de l'ECCO 2024 (référence principale), de l'ACG 2025 et de la BSG 2025 n'a pas été lu.
- **Moyens de vérification** :
  - BSG 2019 en texte intégral : acide folique, IM-UNITI, essai adalimumab + ciprofloxacine, budésonide, thiopurines, méthotrexate et grossesse ;
  - résumés PubMed de CLASSIC-I et du SES-CD (Daperno 2004) ;
  - recherche web : RCP de Humira, Stelara, Skyrizi et Rinvoq ; synthèses de l'ACG 2025 ; extraits de la BSG 2025.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| CAS-GAST-0455 | Phénotype classé **B1** malgré un syndrome de Koenig et une « discrète sténose » à l'entéro-IRM : la clé de correction était incohérente avec une maladie sténosante | **majeure** (lot) | Scénario rendu cohérent : pas de signes obstructifs, pas de rétrécissement luminal. B1 justifié par « ni sténose ni fistule » | Montréal [S7] |
| § 13.2.4 | Acide folique du méthotrexate sous marqueur | mineure (AUD-02) | 5 mg une fois par semaine (1–2 jours après le MTX) ou 1 mg/j | BSG 2019 [S5] |
| § 13.2.5 | Adalimumab dans la MC sous marqueur | mineure (AUD-02) | 160/80 mg puis 40 mg toutes les 2 semaines ; 80/40 mg possible selon le RCP européen, moins efficace à S4 (36 % contre 24 %, placebo 12 %) | CLASSIC-I [S27] ; RCP [S26] |
| § 13.2.5 | Entretien de l'ustékinumab sous marqueur | mineure (AUD-02) | 90 mg SC à S8, puis toutes les 12 semaines, ou toutes les 8 semaines en cas de perte de réponse. IM-UNITI : 53,1 % / 48,8 % / 35,9 % | [S5, S26] |
| § 13.2.5 | Risankizumab et upadacitinib « selon RCP » | mineure (AUD-02) | Risankizumab : 600 mg IV à S0-S4-S8, puis 360 mg SC à S12 et toutes les 8 semaines. Upadacitinib : 45 mg/j × 12 semaines, puis 15 ou 30 mg/j (15 mg au maximum après 65 ans) | RCP [S26] |
| § 13.2.7 | Antibiotiques périanaux sans schéma | mineure | Données de l'essai ciprofloxacine 500 mg × 2/j × 12 semaines + adalimumab (71 % contre 47 % à S12, pas de différence à S24). **Marqueur maintenu** pour le métronidazole et les abcès | BSG 2019 [S5] |
| § 13.2.6 | ECCO 2026 « infections » non décrite ; BSG 2025 absente | mineure | Structure de l'ECCO 2026 ; points de la BSG 2025 (pneumocoque avec rappel à 5 ans, prophylaxie thromboembolique, coprocultures, corticoïdes avant chirurgie) | [S25, S6] |
| § 7.4 | SES-CD imprécis | mineure | 4 variables cotées 0–3, score = somme, corrélation au CDEIS r = 0,92. Définition de chaque cotation et seuils `[À VÉRIFIER]` | Daperno 2004 [S12] |
| Bandeau | Actualité | mineure (AUD-04) | Statut des sources 2024–2026 précisé | PubMed |
| § 21 | Positions de l'ACG 2025 absentes | mineure | Contre la mésalazine ; contre le budésonide en entretien ; thérapie avancée d'emblée possible ; upadacitinib, mirikizumab ; endoscopie postopératoire à 6–12 mois (synthèses de l'ACG, à confirmer) ; ligne « pneumocoque » | [S3, S6] |
| YAML, § 22 | Sources | mineure (traçabilité) | Ajout de S26 (RCP) et S27 (CLASSIC-I) | — |
| QCM-GAST-0481 | Arrêt du MTX avant conception sans précision de sexe | mineure | Femme : 6 mois (forte) ; homme : arrêt probablement inutile (faible) | BSG 2019 |

## Scores contrôlés

- **Montréal** (A1 ≤ 16 ans, A2 17–40 ans, A3 > 40 ans ; L1–L4 ; B1–B3 + p) : exact. Cas du dossier : A2 L1 B2p, exact.
- **CDAI** : 8 variables et coefficients exacts. Seuils 150/450 (seuils des essais `[À VÉRIFIER]`).
- **Harvey-Bradshaw** : exact.
- **Rutgeerts i0–i4** : exact ; seuil ≥ i2 conforme à la BSG 2019.
- **SONIC** : 56,8 / 44,4 / 30,0 % exacts.
- **Cohérence avec DOS-RHUM-0001/0002 et DOS-GAST-0003** : ITL selon l'OMS 2024, instruction algérienne « à confirmer », restrictions EMA des inhibiteurs de JAK. Aucune divergence nouvelle.

## QCM et cas

- QCM-GAST-0475…0486 : réponses exactes → `audite_valide`.
- CAS-GAST-0455 (corrigé) et CAS-GAST-0456 → `audite_valide`.

## Reste à faire

1. Schémas antibiotiques des lésions anopérinéales et des abcès : métronidazole, durée (ECCO 2024 ou protocole). **Dernier marqueur de posologie.**
2. Lire les textes intégraux de l'ECCO 2024 (médical et chirurgical), de l'ACG 2025 et de la BSG 2025 :
   - prévention de la récidive postopératoire (place de la biothérapie) ;
   - liste des facteurs de mauvais pronostic.
3. Instruction algérienne ITL 2024 (S21).
4. Seuils du SES-CD et du CDAI (sources) ; chiffres de Cosnes 2002 et de Rutgeerts 1990.
5. Relecture par un enseignant.
