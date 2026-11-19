# Rapport d'audit AUD-03 — banque QCM RES-02 (sciences fondamentales)

- **Poste** : AUD-03 (IA) — audit des QCM et cas cliniques
- **Date** : 2026-11-19
- **Objet** : 272 QCM des lots `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/RES-02-a.json` et `RES-02-b.json`
- **Rédacteur audité** : RES-02 (statut initial `brouillon_a_auditer`)
- **Référentiels** : `00_SYSTEME/CONVENTIONS.md`, `00_SYSTEME/schemas/qcm.md`, `00_SYSTEME/agents/PROTOCOLE_AUDIT.md` (adapté aux QCM), intitulés des items `16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json`

## 1. Bilan

| Indicateur | Valeur |
|---|---|
| QCM audités | 272 (lot a : 124, items RES-SF-001 → 034 ; lot b : 148, items RES-SF-037 → 073) |
| Verdict `audite_valide` sans modification | 242 |
| Verdict `corrige` (corrigé avec certitude → statut `audite_valide`) | 30 (lot a : 16 ; lot b : 14) |
| Verdict `a_revoir` (statut `audite_corrections_requises`) | 0 |
| Erreurs **critiques** (clé erronée, y compris proposition marquée vraie mais inexacte telle que rédigée) | 3 |
| dont erreur de clé franche (inversion vrai/faux) | 1 (QCM-ANAP-5033, E) |
| Corrections **majeures** (ambiguïté pouvant inverser la réponse attendue) | 1 |
| Corrections **mineures** (précision, actualisation, explication, coquille) | 26 |
| QCM supprimés / ids modifiés | 0 / 0 |

Tous les QCM ont désormais `statut: audite_valide` et un bloc `audit` (`date`, `auditeur`, `verdict`, `note`).

## 2. Méthode

1. Lecture intégrale de chaque QCM : énoncé, 5 propositions, clé, explication par proposition, explication générale, piège classique, sources.
2. Vérification de la clé proposition par proposition (vrai sans ambiguïté / faux sans ambiguïté), des valeurs numériques et unités, des équations (Nernst, Laplace, Poiseuille, Friedewald, Jurin, clairance, ventilation alvéolaire, vergence…).
3. Recherche des formulations absolues ou ambiguës (« toujours », « jamais », « seul », « tous ») dans les propositions marquées vraies ; contrôle automatique de cohérence entre préfixe « Vrai/Faux » des explications et clé.
4. Contrôle de la cohérence avec l'intitulé de l'item du programme (68 items, 4 QCM chacun) : aucun hors-sujet relevé.
5. Contrôle des sources : les 42 ouvrages distincts cités `[catalogue OUV-xxxx]` existent dans `24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/catalogue_ouvrages.json` avec titre et édition concordants ; aucune annale attribuée (`origine: originale_mediverse`).
6. Une seule recherche web (seuil de validité de la formule de Friedewald).
7. Validation JSON après écriture (python3) : 5 propositions A–E, explications A–E, réponses ⊂ propositions, QCS = 1 réponse, ids et ordre inchangés, explications cohérentes avec la clé.

## 3. Points signalés par le rédacteur

| Point | QCM | Conclusion |
|---|---|---|
| Formule de Friedewald | QCM-BIOC-5019 (B, D) | Clé exacte (B vraie). Explication réécrite avec les deux seuils **correctement convertis** : usage français TG < 3,4 g/L (≈ 3,9 mmol/L, documents Afssaps/ANSM) ; publication originale et ESC/EAS 2019 : TG < 4 g/L (400 mg/dL ≈ 4,5 mmol/L). **L'équivalence suggérée « 3,4 g/L ≈ 4,5 mmol/L » est inexacte** (facteur ≈ 1,14 mmol par g de triglycérides) et n'a pas été reprise. Formule donnée en g/L (TG/5) et mmol/L (TG/2,2). |
| Puissance optique de l'œil | QCM-BIOP-5001 (A, B, C) | Exact : ≈ 60 D (œil réduit ; Gullstrand ≈ 58,6 D), cornée ≈ 2/3 (40–43 D), cristallin ≈ 20 D au repos. Aucune modification. |
| Vascularisation du nœud sinusal | QCM-ANAT-5003 (D) | Exact : branche de la coronaire droite dans ≈ 55–60 % des cas, circonflexe sinon ; « dans la majorité des cas » est correct. Aucune modification. |
| Tours de spire de la cochlée | QCM-ANAT-5002 (D) | Exact : 2,5 à 2,75 tours (2,5 dans les manuels français, 2,75 dans Gray's) ; la fourchette lève l'ambiguïté. Aucune modification. |

## 4. Erreurs critiques et majeure (détail)

1. **QCM-ANAP-5033 — erreur de clé.** E « L'amylose peut être localisée ou systémique » est exacte (l'explication de E et l'explication générale l'affirment) mais était marquée fausse. Clé corrigée : A, B, C, **E**.
2. **QCM-PARA-5001 — C marquée vraie mais inexacte.** « paroi contenant de la chitine et des stérols (ergostérol) » : l'ergostérol est un stérol de la **membrane** cytoplasmique, non de la paroi. Proposition réécrite (chitine pariétale, ergostérol membranaire), clé conservée.
3. **QCM-BIOP-5032 — C marquée vraie mais physiquement inexacte.** « La tension superficielle tend à stabiliser les petites bulles » : la surpression de Laplace favorise au contraire la dissolution des petites bulles. Le mécanisme de l'embolie gazeuse enseigné en biophysique est la contre-pression due à l'asymétrie des ménisques amont/aval (ΔP = 2T(1/r1 − 1/r2)), additive pour des bulles en chapelet (effet Jamin). Proposition, explication et explication générale réécrites.
4. **QCM-ANAP-5003 (majeure).** D « métaplasie = remplacement par un autre tissu différencié *de même type* » : contradictoire, pouvait faire juger fausse une proposition marquée vraie. Reformulée « de même lignée ».

## 5. Tableau des QCM corrigés

| Id | Item | Lot | Problème | Gravité | Correction |
|---|---|---|---|---|---|
| QCM-HIST-5002 | RES-SF-004 | RES-02-a | B : « sont à l'origine de la grande majorité des fibres afférentes » — les fibres afférentes naissent des neurones du ganglion spiral ; formulation impropre. | mineure | B reformulée : « sont innervées par la grande majorité des fibres afférentes ». Clé inchangée. |
| QCM-PHYS-5017 | RES-SF-011 | RES-02-a | A : « Le pic de LH précède l'ovulation d'environ 24 à 36 heures » — ambigu (début ou sommet du pic ?) ; le délai classique est d'environ 36 h après le début du pic et 10–12 h après son sommet. | mineure | A reformulée sur le début du pic (34–36 h) ; explication complétée (sommet : 10–12 h). Clé inchangée. |
| QCM-PHYS-5035 | RES-SF-019 | RES-02-a | Explication B : « stades N3 » (pluriel erroné). | mineure | Explication B corrigée (stade N3, anciens stades 3 et 4). |
| QCM-PHYS-5037 | RES-SF-019 | RES-02-a | C : « à l'exception des muscles respiratoires » — trop large (intercostaux et muscles des voies aériennes supérieures sont atoniques en sommeil paradoxal) ; l'explication générale disait déjà « sauf diaphragme ». | mineure | C reformulée (diaphragme et muscles oculomoteurs) ; explication précisée. Clé inchangée. |
| QCM-BIOC-5003 | RES-SF-020 | RES-02-a | Explication C : entrée cellulaire des hormones thyroïdiennes attribuée à leur seule lipophilie (transport actif par MCT8/OATP omis). | mineure | Explication C actualisée (transporteurs membranaires, récepteurs TR). |
| QCM-GENE-5001 | RES-SF-021 | RES-02-a | A : affirmation générale « il est constitué d'une alternance d'exons et d'introns » contestable (gènes sans intron, ex. histones). | mineure | A nuancée (« le plus souvent ») ; explication complétée. Clé inchangée. |
| QCM-GENE-5002 | RES-SF-021 | RES-02-a | Explication A : « ARN polymérase I = ARN ribosomiques » sans exception (l'ARNr 5S est transcrit par l'ARN polymérase III). | mineure | Explication A précisée. |
| QCM-GENE-5004 | RES-SF-021 | RES-02-a | Explication D : affirme que l'empreinte concerne des gènes « liés à l'X », donnée non établie chez l'homme. | mineure | Explication D corrigée (gènes soumis à empreinte essentiellement autosomiques). |
| QCM-GENE-5009 | RES-SF-023 | RES-02-a | Explication E : assimile la codominance à une expression « intermédiaire » (confusion avec la dominance incomplète). | mineure | Explication E corrigée (dominance incomplète vs codominance). |
| QCM-GENE-5018 | RES-SF-025 | RES-02-a | Explication E : « en général sans effet sur la séquence protéique » — par définition, la séquence n'est jamais modifiée (l'effet éventuel porte sur l'épissage). | mineure | Explication E précisée. |
| QCM-BIOC-5011 | RES-SF-027 | RES-02-a | C et D : seuils exacts mais référentiel non précisé (HbA1c diagnostique non retenue par tous les référentiels ; borne basse de l'hyperglycémie modérée à jeun différente OMS/ADA) → risque d'ambiguïté. | mineure | C et D rattachées explicitement à l'OMS/ADA ; divergence ADA (1,00 g/L) signalée. Clé inchangée. |
| QCM-BIOC-5013 | RES-SF-027 | RES-02-a | C : « La découverte d'une hyperglycémie impose d'en rechercher les complications et le type de diabète » — une hyperglycémie isolée (stress) n'est pas un diabète : proposition défendable dans les deux sens. | mineure | C reformulée (« découverte d'un diabète ») ; explication complétée. Clé inchangée. |
| QCM-BIOC-5019 | RES-SF-029 | RES-02-a | Point signalé (Friedewald) : explication B « au-delà d'environ 4 g/L (parfois 3,4 g/L) » imprécise, sans unités molaires ni référentiel. N.B. : l'équivalence suggérée « 3,4 g/L ≈ 4,5 mmol/L » est inexacte (3,4 g/L ≈ 3,9 mmol/L ; 4,5 mmol/L ≈ 4 g/L = 400 mg/dL). Explication D : exigence de jeûne présentée sans la nuance ESC/EAS 2019. | mineure | Explication B réécrite avec les deux seuils correctement convertis (France 3,4 g/L ≈ 3,9 mmol/L ; publication originale/ESC-EAS 4 g/L ≈ 4,5 mmol/L) et la formule en g/L et mmol/L ; explication D nuancée ; explication générale alignée ; source ANSM ajoutée. Clé inchangée (B vraie). |
| QCM-MICR-5003 | RES-SF-031 | RES-02-a | E : distracteur contenant une erreur factuelle (« bleue sur fond rouge comme à la coloration de Ziehl-Neelsen » : les BAAR sont rouges sur fond bleu). Explication C : « la coloration de Gram colore toutes les bactéries » (faux : mycobactéries, mycoplasmes, tréponèmes). | mineure | E reformulée (rouge sur fond bleu, BAAR) ; explications C et E corrigées. Clé inchangée (A). |
| QCM-PARA-5001 | RES-SF-031 | RES-02-a | C marquée vraie mais inexacte telle que rédigée : « paroi contenant de la chitine et des stérols (ergostérol) » — l'ergostérol est membranaire, non pariétal (l'explication générale le disait d'ailleurs). | critique | C réécrite (chitine pariétale, ergostérol membranaire) ; explication corrigée. Clé conservée (A, B, C, D), désormais exacte. |
| QCM-MICR-5004 | RES-SF-032 | RES-02-a | B : « idéalement lors des pics fébriles » présenté comme règle — les recommandations actuelles insistent surtout sur le volume prélevé et l'absence de retard au traitement ; formulation discutable. | mineure | B reformulée (asepsie, volume suffisant) ; explication et explication générale nuancées. Clé inchangée. |
| QCM-ANAP-5003 | RES-SF-039 | RES-02-b | D marquée vraie : « remplacement d'un tissu différencié par un autre tissu différencié de même type » — « de même type » est contradictoire (le type tissulaire change ; c'est la lignée qui est conservée) et peut faire juger la proposition fausse. | majeure | D reformulée (même lignée, exemple épithélium → autre épithélium) ; explication complétée. Clé inchangée. |
| QCM-PHYS-5042 | RES-SF-044 | RES-02-b | Explication C contradictoire : « croisent dès leur entrée dans la moelle (quelques métamères au-dessus) ». | mineure | Explication C corrigée (commissure blanche antérieure, 1–2 métamères au-dessus). |
| QCM-BIOP-5014 | RES-SF-051 | RES-02-b | B : « perd son potentiel de repos » — trop absolu (la cellule lésée est partiellement dépolarisée). | mineure | B reformulée (dépolarisation partielle). Clé inchangée. |
| QCM-HIST-5012 | RES-SF-052 | RES-02-b | Explication C : origine des cellules C (crêtes neurales) présentée comme certaine alors qu'une origine endoblastique est discutée. | mineure | Explication C nuancée (origine classique, débat signalé). |
| QCM-BIOC-5026 | RES-SF-055 | RES-02-b | Explication B : omet le rôle de la protéine StAR (étape limitante réelle de la stéroïdogenèse). | mineure | Explication B complétée (StAR). Clé inchangée. |
| QCM-ANAP-5031 | RES-SF-059 | RES-02-b | Coquille dans l'explication générale (« héredité »). | mineure | Coquille corrigée. |
| QCM-ANAP-5035 | RES-SF-059 | RES-02-b | Coquille dans l'explication C (« anevrisme »). | mineure | Coquille corrigée. |
| QCM-ANAP-5033 | RES-SF-060 | RES-02-b | ERREUR DE CLÉ : E « L'amylose peut être localisée ou systémique » est exacte (l'explication et l'explication générale le confirment) mais était marquée fausse. | critique | E ajoutée aux réponses correctes (A, B, C, E) ; explication E réécrite (« Vrai : … »). |
| QCM-BIOP-5022 | RES-SF-067 | RES-02-b | A : attribue la focalisation à la cohérence « temporelle et spatiale » ; seule la cohérence spatiale (faible divergence) conditionne la focalisation. | mineure | A reformulée (cohérence spatiale) ; explication précisée. Clé inchangée. |
| QCM-ANAT-5009 | RES-SF-069 | RES-02-b | Explication A confuse sur la limite axillaire/brachiale (« au bord inférieur du grand pectoral puis du grand rond »). | mineure | Explication A clarifiée (deux conventions de limite). |
| QCM-ANAT-5010 | RES-SF-069 | RES-02-b | B : « puis se divise en artères tibiales » — sujet ambigu et terminaison imprécise (l'artère poplitée donne l'artère tibiale antérieure et le tronc tibio-fibulaire). | mineure | B reformulée ; explication et explication générale précisées. Clé inchangée. |
| QCM-ANAT-5011 | RES-SF-069 | RES-02-b | Explication B incomplète (territoire sensitif : moitié latérale du 4e doigt ; part ulnaire des fléchisseurs). | mineure | Explication B précisée. |
| QCM-BIOP-5030 | RES-SF-071 | RES-02-b | A : « la pression interne est P = 2T/r » — la loi de Laplace donne la surpression (différence de pression), non la pression interne absolue. | mineure | A, explication E et explication générale réécrites en ΔP. Clé inchangée. |
| QCM-BIOP-5032 | RES-SF-072 | RES-02-b | C marquée vraie mais physiquement inexacte : « la tension superficielle tend à stabiliser les petites bulles » — la surpression de Laplace favorise au contraire la dissolution des petites bulles ; le mécanisme de l'embolie gazeuse est la résistance au déplacement de la bulle (asymétrie des ménisques, effet Jamin). | critique | C réécrite selon le mécanisme correct (contre-pression de Laplace, effet Jamin) ; explication C et explication générale corrigées. Clé conservée (A–D), désormais exacte. |

## 6. Sources mobilisées pour l'audit

- Ouvrages catalogués cités par le rédacteur (Guyton & Hall, Boron, West, Gray's, Moore, Langman, Robbins, Rubin, Junqueira, Ross, Lehninger, Tietz, Thompson & Thompson, Abbas, Murray, Hobbie & Roth, Bushberg, Cherry…), métadonnées vérifiées dans le catalogue.
- Mach F et al. 2019 ESC/EAS Guidelines for the management of dyslipidaemias. Eur Heart J 2020;41(1):111-188 (seuil de Friedewald 4,5 mmol/L) — déjà cité dans QCM-BIOC-5019.
- Recherche web du 2026-11-19 (seuil français de Friedewald 3,4 g/L = 3,9 mmol/L) : documents de l'ANSM (archive.ansm.sante.fr) et sources secondaires, par ex. [Mediately – calcul LDL Friedewald](https://mediately.co/fr/tools/CalculatedLDL-C), [Le Quotidien du Pharmacien – dépister une dyslipidémie](https://www.lequotidiendupharmacien.fr/comment-depister-une-dyslipidemie), [EM-Consulte – méthodes de détermination du LDL-c](https://www.em-consulte.com/article/673042/resume/le-point-sur-les-differentes-methodes-pour-determi), [Merck Manual – Friedewald (SI)](https://www.merckmanuals.com/iframe/manual/medical-calculators/friedewald_si-fr.htm). Une source ANSM a été ajoutée à QCM-BIOC-5019 avec la mention honnête « document non téléchargé, date non précisée ».

## 7. Reste à faire (non bloquant)

- QCM-BIOC-5019 : compléter le titre exact et la date du document ANSM/Afssaps cité (seuil 3,4 g/L) après téléchargement du document.
- Relecture humaine qualifiée de la banque (statut `valide_enseignant`, jamais attribué par une IA).
- Sauvegardes de la version pré-audit : `00_SYSTEME/sauvegardes/20261119/21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/RES-02-a.avant_audit_AUD-03.json` et `RES-02-b.avant_audit_AUD-03.json`.
