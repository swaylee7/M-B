# Rapport d'audit AUD-03 — banque QCM RES-04 (pathologie chirurgicale)

- **Poste** : AUD-03 (IA) — audit des QCM et cas cliniques
- **Date** : 2026-11-19
- **Objet** : 180 QCM des lots `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/RES-04-a.json` et `RES-04-b.json`
- **Rédacteur audité** : RES-04 (statut initial `brouillon_a_auditer`)
- **Référentiels** : `00_SYSTEME/CONVENTIONS.md`, `00_SYSTEME/schemas/qcm.md`, `00_SYSTEME/agents/PROTOCOLE_AUDIT.md` (adapté aux QCM), intitulés des items `16_RESIDANAT_ALGERIE/01_PROGRAMME_ITEMS/programme_residanat.json`, catalogue `18_RECOMMANDATIONS/00_CATALOGUE/catalogue_recommandations.json`

## 1. Bilan

| Indicateur | Valeur |
|---|---|
| QCM audités | 180 (lot a : 90, items RES-CHI-001 → 032 ; lot b : 90, items RES-CHI-033 → 067), 3 QCM par item |
| Spécialités | UROL 30, CDIG 27, ORL 21, CGEN 15, NCHI 15, ORTH 12, TRAU 12, OPHT 12, GYNE 12, CPED 9, OBST 9, CPLA 3, CCVA 3 |
| Verdict `audite_valide` sans modification | 155 |
| Verdict `corrige` (corrigé avec certitude → statut `audite_valide`) | 25 (lot a : 14 ; lot b : 11) |
| Verdict `a_revoir` (statut `audite_corrections_requises`) | 0 |
| Erreurs **critiques** (clé erronée, ou proposition marquée vraie mais inexacte) | **0** |
| Corrections **majeures** (ambiguïté pouvant inverser la réponse attendue) | 1 (QCM-UROL-4071) |
| Corrections **mineures** (actualisation, explication inexacte, référence, précision, coquille) | 24 |
| Clés de réponse modifiées | 0 |
| QCM supprimés / ids modifiés / ordre modifié | 0 / 0 / 0 |

Tous les QCM ont désormais `statut: audite_valide` et un bloc `audit` (`date`, `auditeur`, `verdict`, `note`). Les notes des QCM validés sans modification précisent les classifications et chiffres contrôlés.

## 2. Méthode

1. Lecture intégrale de chaque QCM : énoncé, 5 propositions, clé, explication de chaque proposition, explication générale, piège classique, sources.
2. Vérification de la clé proposition par proposition (vrai sans ambiguïté / faux sans ambiguïté), puis relecture critique ciblée : recherche des termes absolus (« toujours », « seul », « tous », « impose »…) dans les propositions marquées vraies, et des formulations nuancées (« peut », « possible », « souvent ») dans les propositions marquées fausses.
3. Contrôle des classifications : Garden, Pauwels, Gustilo-Anderson, Cauchoix-Duparc, Thompson-Epstein, Pipkin, Ladd, Sher, Rutherford (ischémie aiguë), Glasgow, Hunt et Hess, Bismuth-Corlette, Hinchey, Tokyo 2018, EU-TIRADS, Bethesda 2023, ISUP 2014, FIGO (myomes), IOTA, Keith-Wagener-Barker, classification internationale de la rétinopathie diabétique (règle 4-2-1), Kellgren-Lawrence, règle des neuf de Wallace, Alvarado.
4. Contrôle des chiffres : formule de Parkland (4 mL/kg/% SCB sur 24 h, moitié dans les 8 premières heures depuis la brûlure) ; indice de Baux et Baux révisé (+17 si inhalation) ; seuil de PIC 22 mmHg et PPC 60-70 mmHg (Brain Trauma Foundation, 4e éd.) ; durées d'antibiothérapie de l'OMA (HAS 2021 : 8-10 j avant 2 ans, 5 j après) ; seuils IADPSG ; objectifs glycémiques ADA ; RCOG (20 mm) ; ESC 2024 (baisse de 20-25 % de la PAM dans l'HTA maligne). Tous exacts.
5. Contrôle automatique : 5 propositions A–E et 5 explications, réponses ⊂ propositions, QCS = 1 réponse, préfixe « Vrai/Faux » des explications cohérent avec la clé (180/180 avant et après audit).
6. Contrôle des sources : cohérence avec le catalogue des recommandations (statut actuelle/remplacée) ; 7 recherches web (voir § 6) ; 2 tentatives de lecture directe des recommandations EAU (uroweb.org, cloudfront) bloquées par le réseau de la session.
7. Validation JSON après écriture (python3) : JSON valide, `ensure_ascii=False`, indentation 2, ids et ordre inchangés, clés inchangées, aucun champ supprimé, QCM `audite_valide` strictement identiques à l'original hors `statut` et `audit`.

## 3. Points signalés dans la mission

| Point | QCM | Conclusion |
|---|---|---|
| ESMO œsophage/estomac 2022 vs version récente | QCM-CDIG-4001 à 4006 | Les deux recommandations ESMO 2022 sont remplacées par la recommandation ESMO 2026 unifiée (REC-0371). Les 4 QCM qui ne citaient que la version 2022 renvoient désormais aussi à REC-0371 (contenu non lu : mention explicite). **QCM-CDIG-4003** : la proposition B et les explications présentaient radiochimiothérapie préopératoire et chimiothérapie périopératoire comme équivalentes pour l'adénocarcinome ; elles ont été mises à jour selon l'essai ESOPEC (Hoeppner et al., N Engl J Med 2025;392(4):323-335 : FLOT périopératoire supérieure à CROSS en survie globale), avec mention du nivolumab adjuvant (CheckMate 577). **QCM-CDIG-4006** : mention de l'immunothérapie périopératoire (durvalumab, MATTERHORN 2025). Clés inchangées et exactes. |
| Drainage dans la prostatite aiguë | QCM-UROL-4081 | Clé C exacte quel que soit le mode de drainage (A, B, D, E faux sans ambiguïté). La mention « point à vérifier » de l'explication générale a été supprimée. C, son explication et l'explication générale disent maintenant : cathéter sus-pubien privilégié dans l'usage français (AFU : sondage urétral = contre-indication relative en phase aiguë) ; sondage urétral de courte durée admis par d'autres référentiels. Source AFU ajoutée avec mention honnête (document repéré par recherche web, non téléchargé). Le texte EAU n'a pas pu être lu (domaine bloqué). |
| Formule de Parkland, Baux révisé | QCM-CPLA-4045 | Exacts (4 mL/kg/% SCB, moitié en 8 h depuis la brûlure ; +17 points en cas d'inhalation). Aucune modification. |
| Seuil de PIC | QCM-NCHI-4147 | Exact : > 22 mmHg (BTF 4e édition, 2016/2017) ; PPC 60-70 mmHg. Aucune modification. |
| Durées d'antibiothérapie de l'OMA | QCM-ORL-4125 | Exactes (HAS 2021 : 8-10 jours avant 2 ans, 5 jours après ; amoxicilline-acide clavulanique pour le syndrome otite-conjonctivite ; abstention possible après 2 ans si peu symptomatique). Aucune modification. |
| Classifications (Garden, Pauwels, Gustilo, Cauchoix, Ladd, Sher, Rutherford, Glasgow…) | QCM-TRAU-4098, 4100, 4102 ; CPED-4053 ; OBST-4170 ; CCVA-4047 ; NCHI-4145… | Toutes exactes ; aucune modification. |

## 4. Correction majeure (détail)

**QCM-UROL-4071 (RES-CHI-026, tumeur de vessie).** La proposition C, marquée vraie, affirmait « Un uroscanner est indiqué pour explorer le haut appareil urinaire » dans le cadre général du diagnostic d'une tumeur de vessie. Les recommandations EAU sur les TVNIM réservent l'uroscanner aux cas sélectionnés (tumeur trigonale, multiple ou à haut risque) : un candidat appliquant l'EAU pouvait juger C fausse. C est reformulée (« Un uroscanner permet d'explorer le haut appareil urinaire à la recherche d'une tumeur urothéliale associée »), et son explication précise les indications. La clé (A, B, C, E) est inchangée.

## 5. Tableau des QCM corrigés

| Id | Item | Lot | Problème | Gravité | Correction |
|---|---|---|---|---|---|
| QCM-CDIG-4001 | RES-CHI-001 | a | Seule recommandation citée : ESMO œsophage 2022, remplacée. | mineure | Ajout de la référence ESMO 2026 en vigueur (REC-0371). Clé (A, C) inchangée. |
| QCM-CDIG-4002 | RES-CHI-001 | a | Coquille (explication D : « une envahissement ») ; seule source ESMO 2022, remplacée. | mineure | Coquille corrigée ; REC-0371 ajoutée. |
| QCM-CDIG-4003 | RES-CHI-001 | a | Actualité : radiochimiothérapie préopératoire et chimiothérapie périopératoire présentées comme équivalentes pour l'adénocarcinome (dépassé depuis ESOPEC 2025). | mineure | B reformulée (FLOT privilégiée, radiochimiothérapie restant une option) ; explication B et explication générale mises à jour (ESOPEC, CheckMate 577) ; source ESOPEC ajoutée. Clé (B) inchangée. |
| QCM-CDIG-4004 | RES-CHI-002 | a | Seule recommandation citée : ESMO estomac 2022, remplacée. | mineure | REC-0371 ajoutée. |
| QCM-CDIG-4005 | RES-CHI-002 | a | Idem. | mineure | REC-0371 ajoutée. |
| QCM-CDIG-4006 | RES-CHI-002 | a | Actualité : immunothérapie périopératoire non mentionnée. | mineure | Explication D et explication générale complétées (MATTERHORN 2025 ; renvoi à ESMO 2026). |
| QCM-CDIG-4014 | RES-CHI-005 | a | D : « preuve histologique » trop restrictive (la ponction sous écho-endoscopie donne souvent une cytologie). | mineure | D : « histologique (ou cytologique) » ; explication alignée. Clé inchangée. |
| QCM-CDIG-4022 | RES-CHI-008 | a | Source TG18 citée pour l'angiocholite : texte consacré à la cholécystite. | mineure | Ajout de Kiriyama et al., TG18 angiocholite (J Hepatobiliary Pancreat Sci 2018;25(1):17-30, PMID 29032610). |
| QCM-CDIG-4024 | RES-CHI-008 | a | Idem. | mineure | Source TG18 angiocholite ajoutée ; explication générale rattachée au grade III TG18. |
| QCM-CGEN-4031 | RES-CHI-013 | a | Source ATA 2015 marquée « remplacée » sans précision, alors que seul le volet « cancer » est remplacé (ATA 2025). | mineure | Statut de la source précisé (volet « nodules » toujours de référence). |
| QCM-CGEN-4033 | RES-CHI-013 | a | Explication D (Bethesda VI → chirurgie) sans la nuance de la surveillance active ; même imprécision de source ATA. | mineure | Explication D nuancée (microcarcinome papillaire à très faible risque) ; source précisée. Clé inchangée. |
| QCM-UROL-4071 | RES-CHI-026 | a | C ambiguë (voir § 4). | **majeure** | C reformulée ; explication complétée. Clé inchangée. |
| QCM-UROL-4072 | RES-CHI-026 | a | Actualité : immunothérapie périopératoire des TVIM non mentionnée. | mineure | Explication générale complétée (NIAGARA 2024, renvoi à l'EAU en vigueur). |
| QCM-UROL-4081 | RES-CHI-029 | a | Explication générale laissant un « point à vérifier » sur le mode de drainage (voir § 3). | mineure | C, explication C et explication générale réécrites ; source AFU ajoutée. Clé (C) inchangée. |
| QCM-ORTH-4106 | RES-CHI-038 | b | Explication A inexacte (« S. aureus domine à tous les âges ») et contradictoire avec E (Kingella kingae, premier germe entre 6 mois et 4 ans par PCR). | mineure | Explication A corrigée. Clé inchangée. |
| QCM-ORL-4130 | RES-CHI-046 | b | Référence non confirmée (« AAO-HNSF… Pediatrics 2020;145(4):e20200283 [PMID 32229621] »). | mineure | Remplacée par la publication princeps vérifiée : Tunkel DE et al., Otolaryngol Head Neck Surg 2020;162(1_suppl):S1-S38 (PMID 31910111). |
| QCM-ORL-4131 | RES-CHI-046 | b | Idem. | mineure | Idem. |
| QCM-NCHI-4152 | RES-CHI-053 | b | Explication B (immobilisation, plan dur) non actualisée. | mineure | Notion de restriction des mouvements du rachis ; plan dur limité à l'extraction. Clé inchangée. |
| QCM-NCHI-4154 | RES-CHI-054 | b | Référence ESCMID 2024 incomplète (« volume/pages À VÉRIFIER »). | mineure | Référence complétée (Clin Microbiol Infect 2024;30(1):66-89, DOI, PMID 37648062, corrigendum) ; marqueur levé. |
| QCM-NCHI-4155 | RES-CHI-054 | b | Idem. | mineure | Idem. |
| QCM-NCHI-4156 | RES-CHI-054 | b | Idem ; explications A et D imprécises par rapport à l'ESCMID 2024. | mineure | Référence complétée ; explications A (corticoïdes : œdème sévère ou risque d'engagement) et D (6 à 8 semaines) alignées sur l'ESCMID 2024. |
| QCM-GYNE-4165 | RES-CHI-060 | b | Actualité : traitement médical prolongé par antagonistes oraux de la GnRH avec add-back non mentionné. | mineure | Explication générale complétée (relugolix en association fixe, autorisé dans l'UE depuis 2021). B (agonistes) reste fausse. |
| QCM-GYNE-4175 | RES-CHI-065 | b | Manuel OMS 2021 : « ISBN/URL À VÉRIFIER ». | mineure | ISBN 978-92-4-003078-7 et URL OMS vérifiés ; marqueur levé. |
| QCM-GYNE-4177 | RES-CHI-065 | b | Idem. | mineure | Idem. |
| QCM-OBST-4178 | RES-CHI-067 | b | E (glycémie à jeun ≥ 0,92 g/L en début de grossesse = diabète gestationnel) : exacte selon l'IADPSG, critère de l'énoncé, mais non retenue par l'ADA ; nuance absente. | mineure | Explication E complétée (IADPSG, CNGOF-SFD / divergence ADA). Clé inchangée. |

## 6. Sources mobilisées pour l'audit (recherches web du 2026-11-19)

- ESOPEC : Hoeppner J et al. N Engl J Med 2025;392(4):323-335, doi:10.1056/NEJMoa2409408 — confirmé ([ASCO Post](https://ascopost.com/news/january-2025/perioperative-chemotherapy-vs-preoperative-chemoradiotherapy-in-resectable-locally-advanced-esophageal-carcinoma), [ESMO](https://www.esmo.org/oncology-news/perioperative-chemotherapy-with-flot-improves-survival-among-patients-with-resectable-oesophageal-adenocarcinoma), [ClinicalTrials.gov NCT02509286](https://clinicaltrials.gov/study/NCT02509286)).
- TG18 angiocholite : Kiriyama S et al. J Hepatobiliary Pancreat Sci 2018;25(1):17-30 — confirmé ([PubMed 29032610](https://pubmed.ncbi.nlm.nih.gov/29032610/)).
- Épistaxis AAO-HNSF : Tunkel DE et al. Otolaryngol Head Neck Surg 2020;162(1_suppl):S1-S38 — confirmé ([PubMed 31910111](https://pubmed.ncbi.nlm.nih.gov/31910111/)) ; la citation « Pediatrics 2020;145(4):e20200283 » n'a pas pu être confirmée.
- ESCMID abcès cérébraux : Bodilsen J et al. Clin Microbiol Infect 2024;30(1):66-89 ; corrigendum 2024;30(5):698 — confirmé ([BVS / MEDLINE 37648062](https://pesquisa.bvsalud.org/ses/resource/pt/mdl-37648062), [Amsterdam UMC](https://pure.amsterdamumc.nl/en/publications/european-society-of-clinical-microbiology-and-infectious-diseases-4/)).
- Manuel OMS du sperme, 6e éd. 2021, ISBN 978-92-4-003078-7 — confirmé ([OMS](https://who.int/publications/i/item/9789240030787)).
- Drainage de la prostatite aiguë : [AFU — Livret de l'interne, Urgences en urologie (2023)](https://www.urofrance.org/wp-content/uploads/2023/01/Livret-de-linterne-Urgences-en-urologie.pdf) (sondage urétral = contre-indication relative ; document non téléchargé, position rapportée par la synthèse de recherche) ; [Le Quotidien du Médecin — FMC prostatites](https://pneumologie.lequotidiendumedecin.fr/fmc-recos/les-prostatites-aigue-et-chronique) ; [GPnotebook (référence NICE)](https://gpnotebook.com/fr/pages/infectiologie/prostatite-aigue/prise-en-charge-de-la-prostatite-aigue) ; [cgo.mod.uk](https://cgo.mod.uk/clinical-guidelines-for-operations/treatment-guidelines/emergenciesresuscitation/prostatitis/) (sondage urétral de courte durée admis). Texte EAU (uroweb.org) non accessible depuis la session.
- Sans recherche web (connaissances de l'auditeur, citées sans pagination dans les explications) : MATTERHORN (Janjigian et al., N Engl J Med 2025), CheckMate 577 (Kelly et al., N Engl J Med 2021), NIAGARA (Powles et al., N Engl J Med 2024), autorisation européenne du relugolix en association fixe (2021).

## 7. Reste à faire (non bloquant)

- QCM-UROL-4081 : lire le texte de l'AFU (livret 2023) et le chapitre « Bacterial prostatitis » des recommandations EAU sur les infections urologiques pour confirmer la formulation rapportée ; autoriser `uroweb.org` dans le réseau de la session si nécessaire.
- QCM-CDIG-4001 à 4006 : lire la recommandation ESMO 2026 estomac-œsophage (REC-0371, contenu non lu) et vérifier l'intégration de FLOT/ESOPEC et de l'immunothérapie périopératoire.
- Les recommandations EAU citées (lithiase 2016, rein 2022) sont des résumés anciens d'une recommandation mise à jour chaque année ; aucun contenu des QCM n'est contredit, mais les références pourront être actualisées lors de la prochaine mise à jour du catalogue.
- Relecture humaine qualifiée de la banque (statut `valide_enseignant`, jamais attribué par une IA).
- Sauvegardes de la version pré-audit : `00_SYSTEME/sauvegardes/20261119/21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/RES-04-a.avant_audit_AUD-03.json` et `RES-04-b.avant_audit_AUD-03.json`.
