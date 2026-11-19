# Rapport d'audit — DOS-NEPH-0002 « Dyskaliémies : physiopathologie, diagnostic et traitement »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-03.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Il reste 3 marqueurs posologiques (polystyrène sulfonate, KCl par voie centrale, paralysie périodique thyrotoxique) et un renvoi au protocole local (nombre maximal de doses de calcium). Le texte intégral de l'UKKA et l'ERC 2025 n'ont pas été lus.
- **Bilan** : 5 corrections (critiques 0, majeures 0, mineures 5).
- **Vérifications** : catalogue REC-INT (REC-0293 ERC 2021, REC-0294 ERC 2025, REC-0302 KDIGO 2024) ; 2 recherches web (UKKA 2023 : calcium, insuline-glucose, surveillance glycémique ; limites du KCl IV).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2 (insuline-glucose) | `[POSOLOGIE À VÉRIFIER]` sur la présentation du glucose ; relais glucosé « à vérifier ». | mineure | Marqueur levé : 25 g de glucose (250 mL de G10 % selon l'ERC 2021 ; G20 % ou G50 % équivalents selon le protocole) ; **G10 % 50 mL/h pendant 5 h si la glycémie avant traitement est < 7 mmol/L** ; surveillance glycémique de **6 h** (UKKA 2023, retour de 12 h à 6 h). | UKKA 2023 [S1] ; ERC 2021 [S2] |
| § 13.2 (étape « Surveiller ») | Marqueur « séquence exacte ». | mineure | Glycémie au moins horaire pendant 6 h ; horaires précis : protocole local. | [S1] |
| § 17.1 Q2 (et CAS-NEPH-0003) | Relais glucosé non chiffré, « modalités à vérifier ». | mineure | G10 % 50 mL/h pendant 5 h (glycémie initiale 5,8 mmol/L). | [S1, S2] |
| § 13.5 (KCl IV) | Concentration périphérique et voie centrale sous marqueur global. | mineure | Voie périphérique ≤ 40 mmol/L ; 10 mmol/h, jusqu'à 20 mmol/h sous scope ; > 40 mmol/L : voie centrale ; marqueur maintenu pour les débits et concentrations par voie centrale, hétérogènes selon les protocoles (20–40 mmol/h). | [S5] ; politiques hospitalières concordantes (recherche web) |
| Sources, S1 | Référence UKKA sans URL ; contenu non recoupé. | mineure | URL de la version de juillet 2026 ajoutée ; modifications de 2023 recoupées (calcium 30 mL en 10 min au lieu de 15 ; surveillance de 6 h ; seuil de 7 mmol/L). | Recherche web (documents UKKA) |

## Points vérifiés sans modification

- Gradation (légère 5,5–5,9 ; modérée 6,0–6,4 ; sévère ≥ 6,5) ; signes ECG ; pseudohyperkaliémies.
- Gluconate de calcium 10 % 30 mL en 10 min (UKKA 2023, confirmé) ou chlorure de calcium 10 % 10 mL ; insuline 10 UI + 25 g de glucose en 15 min ; salbutamol nébulisé 10–20 mg ; cyclosilicate de zirconium sodique 10 g × 3/j jusqu'à 72 h ; patiromer en entretien ; plus de résine calcique en aigu (UKKA 2023) ; arrêt hyperkaliémique (ERC 2021 : CaCl₂ 10 mL, insuline-glucose, bicarbonate 50 mmol selon le contexte, EER).
- Hypokaliémie : jamais de bolus de KCl, dilution dans du NaCl 0,9 %, 1 g de KCl ≈ 13,4 mmol, MgSO₄ 8 mmol en 20 min, kaliurèse et rapport K/créatinine, démarche étiologique, Gitelman/Bartter.
- Cas cliniques (hyperkaliémie sévère iatrogène ; vignette hyperaldostéronisme) : exacts.

## QCM et cas associés

- QCM-NEPH-0013 à 0024 : réponses exactes ; QCM-NEPH-0016 (calcium en 10 min) confirmé ; explication de QCM-NEPH-0017 précisée ; `audite_valide`.
- CAS-NEPH-0003 (relais glucosé précisé) et CAS-NEPH-0004 : `audite_valide`.

## Reste à faire

1. Lire le texte intégral de l'UKKA (juillet 2026 ; hôte ukkidney.org hors du réseau de la session) : nombre de doses de calcium, place du bicarbonate, nouvelles positions sur le polystyrène sulfonate et le cyclosilicate de zirconium sodique.
2. Lire l'**ERC 2025** (circonstances particulières) et noter ses éventuelles modifications.
3. Posologies maintenues sous marqueur : polystyrène sulfonate (RCP), KCl par voie centrale, KCl dans la paralysie périodique thyrotoxique.
4. iSGLT2 et risque d'hyperkaliémie : ajouter une source (méta-analyses d'essais) ou laisser `[À VÉRIFIER]`.
5. Disponibilité en Algérie (SZC, patiromer, poches de KCl prémélangées) : `[À VÉRIFIER]`.
6. Relecture enseignant.
