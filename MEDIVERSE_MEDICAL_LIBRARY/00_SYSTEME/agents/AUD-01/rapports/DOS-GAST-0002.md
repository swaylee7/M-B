# Rapport d'audit — DOS-GAST-0002 « Maladie ulcéreuse gastroduodénale »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (scientifique), AUD-02 (posologies), AUD-04 (références) — IA, indépendants du rédacteur DOS-04.
- **Objets audités** :
  - dossier v1.0 ;
  - QCM-GAST-0451…0462 (lot `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/DOS-04-lot2.json`) ;
  - CAS-GAST-0451 et 0452 (lot `20_CAS_CLINIQUES/lots/DOS-04-lot2.json`).
- **Verdict** : `audite_valide` (v1.1).
  - Aucune erreur critique ni majeure.
  - 11 corrections mineures.
  - Les 4 marqueurs `[POSOLOGIE À VÉRIFIER]` sont levés, chacun avec une source nommée.
  - 18/18 références vérifiées.
- **Moyens de vérification** :
  - fiches HAS 2021 *H. pylori* (traitement probabiliste et traitement guidé), relues sur has-sante.fr : amoxicilline 50 mg/kg/j en 3 ou 4 prises, IPP matin et soir « pendant le repas », bismuth 10 jours ;
  - rapport de réévaluation des IPP de la Commission de la transparence (HAS 2020, PDF téléchargé et lu) ;
  - synthèse officielle de l'ACG 2024, par recherche web ;
  - liste OMS 2024 des pathogènes prioritaires et lettre de *Microbial Genomics* 2025 (PMC12452171).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2.1 | Durées des IPP de cicatrisation sous marqueur | mineure (AUD-02) | Pleine dose : 4 semaines pour l'UD, 4 à 8 semaines pour l'UG, durée prolongeable selon la taille. Marqueur levé | HAS, CT 2020 [S17] |
| § 13.2.1 | IPP « avant le repas » alors que la fiche HAS d'éradication indique « pendant le repas » | mineure | Les deux modalités sont précisées | HAS 2021 [S3, S4] |
| § 13.2.2 | Bithérapie P-CAB et trithérapie à la rifabutine sans posologie, sous marqueur | mineure (AUD-02) | Vonoprazan 20 mg × 2/j + amoxicilline 1 g × 3/j ; oméprazole 40 mg + amoxicilline 1 g + rifabutine 50 mg × 3/j ; 14 jours. Marqueur levé ; disponibilité en Algérie `[À VÉRIFIER]` | ACG 2024 [S2] |
| § 13.3.2 | IPP de l'ulcère gastrique sous marqueur | mineure (AUD-02) | 4 à 8 semaines à pleine dose, prolongé si l'ulcère est volumineux | [S17] |
| § 13.3.3 | IPP de l'ulcère aux AINS sous marqueur | mineure (AUD-02) | Pleine dose 4 à 8 semaines ; ésoméprazole à demi-dose | [S17] |
| § 15.1 | Facteurs de risque de la gastroprotection imprécis | mineure | ≥ 65 ans (HAS) ; demi-dose (sauf oméprazole) ; arrêt avec l'AINS | [S17] |
| § 3.1 | Liste OMS 2017 présentée sans actualisation | mineure (actualité) | *H. pylori* résistant à la clarithromycine n'est pas repris dans la liste OMS 2024 (retrait contesté) | [S18] |
| YAML, § 22 | Sources manquantes | mineure (traçabilité) | Ajout de S17 (HAS 2020) et S18 (OMS 2024) | — |
| QCM-GAST-0459 | Durées « selon RCP » | mineure | Durées HAS 2020 ; source ajoutée | [S17] |
| QCM-GAST-0462 | Proposition D vraie en 2017 mais caduque depuis 2024 | mineure | Énoncé daté (« En 2017… ») ; explication actualisée | [S18] |
| CAS-GAST-0451 | IPP « durée selon RCP » | mineure | 4 à 8 semaines à pleine dose, puis demi-dose tant que l'aspirine est maintenue | [S17] |

## Points vérifiés sans modification

- **Éradication de *H. pylori*** : schémas exacts.
  - Quadrithérapie concomitante 14 jours : IPP × 2, amoxicilline 50 mg/kg/j, clarithromycine 500 mg × 2, métronidazole 500 mg × 2.
  - Quadrithérapie bismuthée : oméprazole 20 mg × 2 + 3 gélules × 4/j ; 10 jours selon la HAS, 14 jours selon Maastricht VI et l'ACG.
  - Traitements guidés de la HAS (trithérapie à la clarithromycine ou à la lévofloxacine, bismuth en cas de double résistance).
  - Délais du contrôle d'éradication : ≥ 4 semaines après les antibiotiques, ≥ 2 semaines après l'IPP.
- **Données algériennes de résistance** : six séries, chiffres conformes aux résumés.
  - Clarithromycine : 23–33 %.
  - Métronidazole : 45–61 %.
  - Amoxicilline et tétracycline : 0 %.
  - Le raisonnement en faveur de la quadrithérapie bismuthée est cohérent avec le seuil de 15 % de Maastricht VI.
- **Classifications** : Johnson modifiée (I–V), Forrest (renvoi à DOS-GAST-0001), score de Boey (3 items).
- **Ulcère perforé** : conduite WSES 2020 exacte.
- **Sténose** : alcalose hypochlorémique hypokaliémique.
- **Cohérence avec DOS-GAST-0001** : aucune divergence (aspirine non interrompue, IPP IV, ESGE 2021).

## QCM et cas

- QCM-GAST-0451…0462 : réponses exactes → `audite_valide`.
- CAS-GAST-0451 et 0452 : exacts → `audite_valide`.

## Reste à faire (non bloquant)

1. Recommandation écrite sur la poursuite de l'IPP après éradication dans l'UD non compliqué (§ 13.3.1).
2. Chiffres d'usage :
   - risque d'ulcère chez le sujet infecté ;
   - nombre de biopsies.
3. Publications princeps de la classification de Johnson et du score de Boey.
4. Disponibilité en Algérie : gélule bismuth-métronidazole-tétracycline, P-CAB, rifabutine, tests de résistance. Rechercher une éventuelle recommandation algérienne.
5. Texte intégral de Maastricht VI et de l'ACG 2024.
6. Relecture par un enseignant (`valide_enseignant`).
