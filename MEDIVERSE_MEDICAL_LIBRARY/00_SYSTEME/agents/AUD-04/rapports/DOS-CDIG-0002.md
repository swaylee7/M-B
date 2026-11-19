# Rapport d'audit — DOS-CDIG-0002 « Pancréatite aiguë »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (scientifique), AUD-02 (posologies), AUD-04 (références) — IA
- **Objets audités** : dossier v1.0 (DOS-04) ; QCM-CDIG-0413…0424 ; CAS-CDIG-0403, CAS-CDIG-0404 (lots DOS-04).
- **Verdict** : `audite_valide` (v1.1). Aucune erreur critique. Une erreur majeure, de traçabilité, corrigée. Plus aucun marqueur `[POSOLOGIE À VÉRIFIER]`. Les 16 références sont vérifiées.
- **Moyens de vérification** :
  - texte intégral de l'ACG 2024 (PMC13221274) ;
  - résumés PubMed de WATERFALL, PONCHO, POINTER, APEC, TENSION, PYTHON, PANTER, IAP/APA 2013, Mortele 2004, ESGE 2020, Balthazar 1990 et BISAP 2008.

## Essais demandés : existence et conclusions (vérifiées)

| Essai | Référence | Conclusion vérifiée |
|---|---|---|
| WATERFALL | NEJM 2022;387:989-1000 | 249 patients, essai arrêté précocement. Pas de réduction des formes modérément sévères ou sévères (22,1 % contre 17,3 %). Surcharge hydrique plus fréquente avec le remplissage agressif (20,5 % contre 6,3 %) |
| PONCHO | Lancet 2015;386:1261-8 | Cholécystectomie pendant la même hospitalisation : complications biliaires récidivantes 5 % contre 17 % (RR 0,28) |
| POINTER | NEJM 2021;385:1372-81 | Drainage immédiat non supérieur au drainage différé. Moins d'interventions dans le bras différé (2,6 contre 4,4). 39 % des patients différés guéris sous antibiotiques seuls |
| APEC | Lancet 2020;396:167-76 | CPRE urgente sans bénéfice dans la PA biliaire prédite sévère sans angiocholite (38 % contre 44 %, NS). CPRE réservée à l'angiocholite ou à la cholestase persistante |
| TENSION | Lancet 2018;391:51-8 | Step-up endoscopique non supérieur (43 % contre 45 %). Moins de fistules pancréatiques et hospitalisation plus courte |
| PYTHON | NEJM 2014;371:1983-93 | Sonde nasoentérale précoce non supérieure à l'alimentation orale à 72 h. 69 % du bras « à la demande » n'ont pas eu besoin de sonde |
| PANTER | NEJM 2010;362:1491-502 | Step-up : complications majeures ou décès 40 % contre 69 % avec la nécrosectomie ouverte. 35 % des patients traités par drainage seul |

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| YAML / §22 | Onze références `verifiee: false` (S5–S14) sans DOI | majeure (traçabilité) | Toutes confirmées (DOI, PMID). Ajout de S15 (Mortele 2004, CTSI modifié) et de S16 (ESGE 2020, PA post-CPRE) | PubMed |
| §13.2.1 | Recommandation ACG 2024 imprécise ; marqueur de posologie sur le remplissage | mineure | ACG 2024, recommandation 3 : remplissage « modérément agressif » ; sans hypovolémie, ≤ 1,5 mL/kg/h ; bolus de 10 mL/kg si hypovolémie ; 3–4 L sur 24 h pour la plupart des patients ; Ringer lactate (recommandation 4). Marqueur levé | ACG 2024 ; WATERFALL |
| §7.4 | CTSI « ≥ 7 grave [À VÉRIFIER] » | mineure | Résultats de la série princeps : index élevé → morbidité 92 %, mortalité 17 % ; index bas → morbidité 2 % | Balthazar 1990 |
| §7.4 | CTSI modifié seulement cité (demandé par la mission) | mineure | Barème ajouté (0–10 : inflammation 0/2/4, nécrose 0/2/4, complications extrapancréatiques 2 ; légère 0–2, modérée 4–6, sévère 8–10). Barème tiré de la publication originale, texte intégral non relu | Mortele 2004 [S15] |
| §7.5 | BISAP | mineure | Calculé dans les 24 premières heures ; mortalité < 1 % à > 20 % selon le score | Wu 2008 |
| §6.1 | Fréquences étiologiques | mineure | Lithiase 40–70 %, alcool 25–35 % | ACG 2024 |
| §9.4 | Ponction à l'aiguille fine « à vérifier » | mineure | L'ACG 2024 suggère de ne pas la pratiquer (recommandation 9) | ACG 2024 |
| §13.2.2 | Innocuité des opioïdes attribuée à l'ACG 2024, qui ne traite pas de l'analgésie | mineure | Attribution retirée ; `[À VÉRIFIER — source à citer]` | ACG 2024 (texte intégral) |
| §13.2.4 | Marqueur de posologie sans posologie proposée | mineure | Reformulé (choix selon l'écologie locale, posologies selon le RCP). Antibiotiques diffusant dans la nécrose pour différer le drainage au-delà de 4 semaines | ACG 2024, concept clé 16 |
| §13.2.7 | Résultat de PONCHO non chiffré ; ACG citée sans vérification | mineure | PONCHO : 5 % contre 17 % | PONCHO |
| §13.2.9 | POINTER, TENSION et PANTER non chiffrés | mineure | Résultats chiffrés ajoutés | Résumés PubMed |
| §13.2.9 | Délai d'intervention | mineure | ACG 2024, recommandation 23 : différer de préférence de 4 semaines chez le patient stable | ACG 2024 |
| §15.2 | PA post-CPRE : AINS rectal « avant ou juste après » sous marqueur | mineure (actualité) | ESGE 2020 : 100 mg de diclofénac ou d'indométacine **immédiatement avant** la CPRE chez tous les patients sans contre-indication. ACG 2024 : indométacine chez les patients à haut risque. Marqueur levé ; seules les modalités d'hydratation restent `[À VÉRIFIER]` | ESGE 2020 [S16] ; ACG 2024, recommandation 6 |
| §21 | Divergence ESGE / ACG sur la prévention de la PA post-CPRE | mineure | Ligne ajoutée | [S16, S3] |
| Bandeau | Mention « essais non revérifiés » | mineure | Mise à jour | — |
| Lots | Statuts | mineure | QCM-CDIG-0413…0424 et CAS-CDIG-0403 : `audite_valide` ; CAS-CDIG-0404 : `audite_corrections_requises` (durée de l'antibiothérapie de l'angiocholite `[À VÉRIFIER]`) | — |

Total : 16 corrections (1 majeure), aucune erreur critique.

**Classifications et scores contrôlés et exacts** :
- Atlanta révisée 2012 : 2 critères sur 3 ; trois niveaux de gravité ; collections avant et après 4 semaines ;
- Marshall modifié : barème et seuil ≥ 2 ;
- Balthazar et CTSI ;
- Ranson (version non biliaire, ≥ 3) ;
- BISAP ;
- SIRS.

Les calculs du cas sont justes : Marshall respiratoire 2 ; CTSI 8.

## QCM et cas

- QCM-CDIG-0413…0424 : exacts ; `audite_valide`.
- CAS-CDIG-0403 (PA hypertriglycéridémique) : exact. Le protocole d'insuline reste « protocole local » ; `audite_valide`.
- CAS-CDIG-0404 : exact, mais la durée de l'antibiothérapie de l'angiocholite reste à sourcer ; `audite_corrections_requises`.

## Références (AUD-04)

- **Avant** : 4/14 vérifiées.
- **Après** : 16/16.

## Reste à faire (non bloquant)

1. Analgésie (opioïdes, péridurale) : citer une source (WSES 2019 [S14] ou une autre recommandation).
2. Seuils classiques : ALAT > 3 × LSN, hématocrite > 44 %, CRP > 150 mg/L ; probiotiques (PROPATRIA) ; syndrome du canal déconnecté ; hypertriglycéridémie (insuline, plasmaphérèse) ; grossesse.
3. ESGE 2020 : modalités de l'hydratation par Ringer lactate périprocédurale.
4. Durée de l'antibiothérapie de l'angiocholite après drainage (Tokyo Guidelines 2018) pour CAS-CDIG-0404.
5. Données algériennes : séries hospitalières, organisation de l'écho-endoscopie interventionnelle et de la radiologie interventionnelle.
