# Rapport d'audit — DOS-CDIG-0004 « Appendicites aiguës »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01, AUD-02, AUD-04 (IA), indépendants du rédacteur DOS-04.
- **Objets audités** :
  - dossier v1.0 ;
  - QCM-CDIG-0463…0474 ;
  - CAS-CDIG-0453 et 0454 (lots DOS-04-lot2).
- **Verdict** : `audite_valide` (v1.1).
  - Aucune erreur critique ni majeure.
  - 10 corrections mineures.
  - Les 2 marqueurs de posologie sont levés.
  - 20/20 références vérifiées.
- **Moyens de vérification** :
  - **WSES 2020** (DOC-00082, pdftotext) : schémas antibiotiques de la WSES 2017 repris en 2020 ; recommandations 3.3 (8 h chez l'enfant), 1.4 et 1.9 ;
  - **AWaRe OMS 2022** (DOC-00039) : chapitres 31 (appendicite) et 40 (antibioprophylaxie) ;
  - **texte intégral de Sammalkorpi 2014** (PMC4087125 : barème de l'AAS) ;
  - **tableau AIR/Alvarado** de de Castro 2012 (PMC4714027) ;
  - **tableau du PAS** de Goulder 2008 (PMC2788473).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2.4 a | Molécule et dose de l'antibioprophylaxie sous marqueur | mineure (AUD-02) | Céfazoline 2 g IV + métronidazole 500 mg IV en dose unique ; second choix : amoxicilline-acide clavulanique 2 g/200 mg ; enfant : céfazoline 50 mg/kg + métronidazole 7,5 mg/kg. La WSES ne précise pas la molécule | AWaRe 2022 [S18] |
| § 13.2.4 c | Marqueur sur des doses pourtant sourcées (WSES) | mineure (AUD-02) | Doses WSES confirmées dans le texte. Ajout de la position de l'OMS : amoxicilline-acide clavulanique 1 g/200 mg toutes les 8 h ; métronidazole 500 mg toutes les 8 h ; 5 jours si forme compliquée opérée, 7 jours si antibiotiques seuls. Marqueur levé | [S1, S18] |
| § 7.2 | Barème de l'AIR non détaillé (`[À VÉRIFIER]`) | mineure | Barème complet (0–12) et interprétation 0–4 / 5–8 / 9–12 | de Castro 2012 [S19] |
| § 7.3 | Barème de l'AAS non détaillé | mineure | Tableau complet, dont la sensibilité de la FID pondérée selon le sexe et l'âge et la CRP selon la durée des symptômes ; spécificité de 92,7 % au seuil ≥ 16 | [S8] (texte intégral) |
| § 7.4 | Barème du PAS « À VÉRIFIER » | mineure | Barème confirmé ; ≤ 5 peu probable, ≥ 6 probable. Seuils de fièvre et de leucocytose `[À VÉRIFIER]` | [S20] |
| § 3 | Risque d'appendicite au cours de la vie « 7–8 %, À VÉRIFIER » | mineure | 8,6 % chez l'homme et 6,7 % chez la femme (Addiss 1990, cité par [S8]) | [S8] |
| § 17, question 1 | Barème AIR « À VÉRIFIER » | mineure | Calcul (6/12) confirmé | [S19] |
| § 21 | Divergence WSES/OMS non signalée | mineure | Lignes « schémas probabilistes » (rythmes de 6 h ou de 8 h) et « antibioprophylaxie » | [S1, S2, S18] |
| YAML, § 22 | Sources | mineure (AUD-04) | Ajout de S18 à S20 ; S7 à S9 précisées | — |
| CAS-CDIG-0453 | « Barème PAS à vérifier » ; température de 38,0 °C au seuil ambigu | mineure | Barème confirmé ; température portée à 38,4 °C | [S20] |

## Scores contrôlés

- **Alvarado** (MANTRELS, 10 points) : exact. Calcul du cas (10/10) exact.
- **AIR** : barème et calcul du cas (6/12) exacts.
- **AAS** et **PAS** : exacts.
- **Seuils de la WSES** : haut risque si âge < 40 ans avec AIR 9–12, Alvarado 9–10 ou AAS ≥ 16.

## Essais contrôlés

- APPAC : 530 patients ; 27,3 % opérés ; 39,1 % à 5 ans ; complications 6,5 % contre 24,4 %.
- CODA : 29 % d'appendicectomies, 41 % en cas d'appendicolithe, 25 % sans.
- APPAC II, Vons, Minneci (67,1 %), STOP-IT.
- Délais de la WSES : 24 h ; 8 h pour la forme compliquée de l'enfant.

## QCM et cas

- QCM-CDIG-0463…0474 : réponses exactes → `audite_valide`.
- CAS-CDIG-0453 (corrigé) et CAS-CDIG-0454 → `audite_valide`.

## Reste à faire (non bloquant)

1. Données algériennes : incidence, moyens disponibles (cœlioscopie, drainage percutané), écologie bactérienne (BLSE).
2. Points de pratique marqués `[À VÉRIFIER]` : analgésie précoce (source), installation de la femme enceinte, conduite devant une tumeur appendiculaire.
3. Publications princeps de l'AIR (Andersson 2008) et du PAS (Samuel 2002) : seuils de température.
4. Relecture par un enseignant.
