# Rapport d'audit AUD-03 — banque QCM RES-03 (médecine), lots a et b

- **Poste** : AUD-03 (IA) — audit des QCM et cas cliniques
- **Date** : 2026-11-19
- **Objet** : 225 QCM des lots `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/RES-03-a.json` (126 QCM, items RES-MED-001 → 052) et `RES-03-b.json` (99 QCM, items RES-MED-054 → 098). Les lots `RES-03-c` / `RES-03-d` (en cours d'écriture par un autre agent) n'ont pas été touchés.
- **Rédacteur audité** : RES-03 (statut initial `brouillon_a_auditer`)
- **Référentiels** : `00_SYSTEME/CONVENTIONS.md`, `00_SYSTEME/schemas/qcm.md`, `00_SYSTEME/agents/PROTOCOLE_AUDIT.md` (adapté aux QCM), catalogue `18_RECOMMANDATIONS/00_CATALOGUE/catalogue_recommandations.json`, catalogue des ouvrages.

## 1. Bilan

| Indicateur | Valeur |
|---|---|
| QCM audités | 225 (lot a : 126 ; lot b : 99) — 188 QCM / 37 QCS |
| Verdict `audite_valide` sans modification | 206 |
| Verdict `corrige` (corrigé avec certitude → statut `audite_valide`) | 19 (lot a : 10 ; lot b : 9) |
| Verdict `a_revoir` (statut `audite_corrections_requises`) | 0 |
| Erreurs **critiques** (clé erronée, proposition marquée vraie mais fausse) | **0** |
| dont erreurs de clé | **0** |
| Corrections **majeures** (QCM reposant sur un point non tranché) | 1 (QCM-RHUM-3225) |
| Corrections **mineures** (actualisation, précision, marqueurs levés, attribution de source) | 18 |
| Marqueurs `[À VÉRIFIER]` / `[POSOLOGIE À VÉRIFIER]` restant dans le contenu des QCM | 0 (6 levés) |
| QCM supprimés / ids modifiés / clés modifiées | 0 / 0 / 0 |

Tous les QCM ont `statut: audite_valide` et un bloc `audit` (`date`, `auditeur`, `verdict`, `note` — la note des QCM corrigés commence par la gravité entre crochets).

## 2. Méthode

1. Lecture intégrale de chaque QCM : énoncé, 5 propositions, clé, explication de chaque proposition, explication générale, piège, sources.
2. Vérification de la clé proposition par proposition (vrai sans ambiguïté / faux sans ambiguïté), des critères diagnostiques, scores et seuils (Sepsis-3/qSOFA, Truelove-Witts, Light, McDonald, ICHD-3, ILAE 2014, Brighton, GOLD, OLD, Silverman, Sarnat, ISPAD 2022, ESPGHAN 2020, IPNA 2022, ILAR, définition harmonisée du syndrome métabolique, ESC/ERS 2022, ESC/EACTS, ESC/EAS…).
3. Contrôle automatique : cohérence préfixe « Vrai/Faux » des explications ↔ clé, QCS = 1 réponse, 5 propositions A–E, formulations absolues dans les propositions vraies.
4. Contrôle des sources : les 120 recommandations `REC-xxxx` et les 43 ouvrages `OUV-xxxx` cités existent au catalogue ; décret exécutif n°22-250 (MDO) vérifié (REC-0004, JORADP n°47/2022 : fièvres typhoïdes, rage, paludisme, syphilis, urétrite gonococcique, TIAC, tuberculoses en catégorie 1).
5. Quatre recherches web (quota partagé) sur les points signalés non vérifiables autrement : ESC/EACTS 2025 valvulopathies, McDonald 2024, ESPGHAN 2017 (lait de vache), SSC 2026.
6. Écriture via `commun.ecrire_json` (agent AUD-03, `ensure_ascii=False`, indentation 2) ; validation python3 (ids et ordre inchangés, clés inchangées, A–E, cohérence explications/clé) ; `valider.py` : 0 erreur.

## 3. Points signalés par le rédacteur

| Point | QCM | Conclusion |
|---|---|---|
| SSC 2026 | INFE-3010, 3011, 3012 | Pages SCCM/ESICM : 129 énoncés dont 46 nouveaux ; antimicrobiens **immédiats, idéalement dans l'heure** confirmés ; **NEWS/MEWS/SIRS préférés au qSOFA** comme outil unique de dépistage. Clés exactes. Explications actualisées (qSOFA) ; la phrase non vérifiable « principes communs aux versions successives » remplacée : PAM ≥ 65 mmHg, noradrénaline, cristalloïdes rattachés explicitement à la SSC 2021 (objectif de PAM du texte 2026 non lu). |
| Valvulopathies ESC/EACTS 2025 | CARD-3120, 3126 (et 3115-3125) | Vérifié sur résumés (communiqué ESC, PCRonline, Rev Esp Cardiol) : intervention raisonnable (IIa) dans le RA sévère asymptomatique à haut gradient avec FEVG ≥ 50 % si risque faible ; TAVI à partir de 70 ans (75 en 2021) ; réparation chirurgicale précoce de l'IM primaire sévère asymptomatique. Marqueurs `[À VÉRIFIER]` levés **sans affirmer de seuil chiffré non vérifié** (seuils de diamètre télésystolique de l'IM non confirmés). Critères du RA sévère et RM ≤ 1,5 cm² inchangés. |
| Myocardite-péricardite ESC 2025 | CARD-3127, 3128, 3129 | Seule affirmation propre à 2025 (approche conjointe, « syndromes inflammatoires myopéricardiques ») conforme au catalogue ; critères diagnostiques présentés comme « classiques », traitement (AINS/aspirine + colchicine, corticoïdes en 2e intention, anti-IL-1) conforme. Aucune modification. |
| McDonald 2024 (SEP) | NEUR-3064 | Vérifié (résumé Lancet Neurol 2025;24(10):850-865 + synthèses) : nerf optique = 5e topographie (IRM, PEV, OCT), signe de la veine centrale et lésions à bord paramagnétique, dissémination temporelle non strictement exigée (BOC ou index kFLC). Marqueur levé ; B reste exacte car explicitement datée « McDonald 2017 ». |
| Durée du traitement du mal de Pott (OMS) | RHUM-3225 | **Point non tranché chez l'adulte** : OMS module 4 (2026) = 2HRZE/10HR pour la TB ostéo-articulaire de l'**enfant** ; ATS/CDC/IDSA 2016 = 6 à 9 mois chez l'adulte ; durées plus longues dans de nombreux programmes. La proposition A (« souvent prolongée au-delà de 6 mois, jusqu'à 12 mois ») a été **reformulée sur un point établi** (2 mois HRZE puis HR) ; divergence présentée dans l'explication (règle 7). |
| ESPGHAN et lait de vache < 12 mois | PEDI-3146 | Vérifié : Fewtrell et al., JPGN 2017;64(1):119-132 (PMID 28027215) — le lait de vache **entier** ne doit pas être la boisson principale avant 12 mois. La source citée (REC-0441, position ESPGHAN sur l'APLV) ne portait pas sur ce point : remplacée. Divergence OMS 2023 / ESPGHAN 2017 conservée avec organismes et dates. |
| Certification OMS « exempte de paludisme » (2019) | INFE-3004 | Fait vérifiable (certification OMS de l'Algérie, mai 2019) : conservé. |
| Rage canine endémique en Algérie | INFE-3007 | Fait établi (rage canine endémique, MDO catégorie 1) : conservé. |
| Hémoglobinopathies / G6PD | PEDI-3176, 3177 | Formulations non chiffrées (« fréquentes dans le bassin méditerranéen ») : conservées. |
| Maastricht VI (quadrithérapie bismuthée 10 jours en gélule combinée) | GAST-3042 | Conforme (14 jours, sauf schéma combiné « 3 en 1 » de 10 jours). Aucune modification. |
| Seuil français de l'IRC (PaO2 < 70 mmHg) | PNEU-3103 | Seuil des référentiels français, non universel : proposition A explicitement rattachée aux « référentiels français ». |

## 4. Correction majeure (détail)

**QCM-RHUM-3225 (mal de Pott — traitement).** A, marquée vraie, affirmait une durée « souvent prolongée au-delà de 6 mois (jusqu'à 12 mois) » : la durée chez l'adulte n'est pas tranchée (ATS/CDC/IDSA 2016 : 6 à 9 mois ; OMS : 12 mois documentés pour l'enfant ; programmes nationaux variables), ce qui rendait la clé contestable. A est reformulée sur la composition et la séquence de la polychimiothérapie (2 mois HRZE puis HR) ; l'explication expose les durées par organisme et renvoie au programme national. Clé inchangée (A, B, C).

## 5. Tableau des QCM corrigés

| Id | Item | Lot | Problème | Gravité | Correction | Source |
|---|---|---|---|---|---|---|
| QCM-INFE-3010 | RES-MED-004 | a | Explication générale : qSOFA présenté comme outil de repérage sans la réserve de la SSC | mineure | Ajout : SSC 2021/2026 déconseille le qSOFA comme outil unique de dépistage (NEWS/MEWS/SIRS). Clé inchangée. | SSC 2026 (SCCM, ESICM) |
| QCM-INFE-3011 | RES-MED-004 | a | Idem (explication générale) | mineure | Nuance qSOFA ajoutée. Clé inchangée. | SSC 2026 |
| QCM-INFE-3012 | RES-MED-004 | a | « Principes communs aux versions successives » : non vérifiable pour 2026 | mineure | Principes rattachés à SSC 2021 ; antimicrobiens dans l'heure confirmés en 2026. Clé inchangée. | SSC 2021, SSC 2026 |
| QCM-INFE-3013 | RES-MED-006 | a | Explication générale : toxoplasmose cérébrale « < 200 CD4 » | mineure | Surtout < 100/mm³ ; prophylaxie dès < 200/mm³. | Mandell, Harrison |
| QCM-NEUR-3064 | RES-MED-028 | a | Marqueur `[À VÉRIFIER]` McDonald 2024 | mineure | Contenu 2024 vérifié et intégré (nerf optique, veine centrale, DIT non obligatoire). Clé inchangée. | Montalban 2025 + synthèses |
| QCM-NEUR-3079 | RES-MED-034 | a | Explication A : mains atteintes quand les troubles atteignent « mi-jambe » | mineure | « environ le niveau des genoux ». | Adams & Victor |
| QCM-NEUR-3083 | RES-MED-035 | a | Explication D : la forme axonale présentée comme variable de l'EGOS | mineure | Variables EGOS/mEGOS correctes (âge, diarrhée, handicap/MRC) ; forme axonale citée à part. Clé inchangée. | EAN/PNS 2023 |
| QCM-PNEU-3103 | RES-MED-044 | a | A : seuil PaO2 < 70 mmHg présenté comme définition universelle ; explication C (« somme conservée ») | mineure | A rattachée aux référentiels français ; C précisée (≥ 120 mmHg environ). Clé inchangée. | Référentiels français, West |
| QCM-CARD-3120 | RES-MED-050 | a | Marqueur `[À VÉRIFIER]` (seuils ESC/EACTS 2025) | mineure | Marqueur levé ; ajout vérifié (réparation précoce de l'IM primaire sévère asymptomatique), sans seuil non vérifié. | ESC 2025 (communiqué), PCRonline |
| QCM-CARD-3126 | RES-MED-052 | a | Marqueur `[À VÉRIFIER]` (intervention plus précoce 2025) | mineure | Contenu vérifié : IIa si RA sévère asymptomatique, FEVG ≥ 50 %, risque faible ; TAVI ≥ 70 ans. | ESC 2025 (communiqué), PCRonline, Rev Esp Cardiol |
| QCM-PEDI-3146 | RES-MED-064 | b | Marqueur `[À VÉRIFIER]` ESPGHAN 2017 ; source inadaptée (REC-0441) ; dilution 1/30 sans renvoi à la notice | mineure | Fewtrell 2017 vérifié et cité (lait de vache entier) ; REC-0441 retiré de ce QCM ; C nuancée. Clé inchangée. | Fewtrell JPGN 2017 |
| QCM-PEDI-3156 | RES-MED-068 | b | `[POSOLOGIE À VÉRIFIER]` (traitement du rachitisme) | mineure | Levé : ≥ 2 000 UI/j ≥ 3 mois + calcium ≈ 500 mg/j (consensus 2016, REC-0332 vérifié). | Munns 2016 |
| QCM-PEDI-3173 | RES-MED-077 | b | Explication B : vitesse de réhydratation liée à l'œdème cérébral, non actualisée | mineure | ISPAD 2022 / essai PECARN FLUID ; étalement 24-48 h maintenu. Clé inchangée. | ISPAD 2022 |
| QCM-PEDI-3176 | RES-MED-078 | b | β-thalassémie majeure révélée « après 3 à 6 mois » (imprécis) | mineure | Habituellement entre 6 mois et 2 ans ; piège aligné. | Nelson |
| QCM-PEDI-3182 | RES-MED-080 | b | `[POSOLOGIE À VÉRIFIER]` (prednisone) | mineure | Levé : IPNA 2022 — 60 mg/m²/j (max 60 mg) 4 sem. puis 40 mg/m² 1 j/2 4 sem. ; protocoles nationaux parfois plus longs. | IPNA 2022 (REC-0308 vérifié) |
| QCM-PEDI-3185 | RES-MED-082 | b | Explication C : RAA = « polyarthrite migratrice » seulement, alors que le cas est une monoarthrite en population à risque | mineure | Critères de Jones révisés (AHA 2015) : monoarthrite = critère majeur en population à risque modéré/élevé. | AHA 2015 (Jones révisés) |
| QCM-ENDO-3191 | RES-MED-085 | b | Explication B : délai 6-8 semaines attribué à l'ATA 2014 | mineure | Rattaché à la HAS 2023 (6-8 sem.), fourchette 4-6 sem. signalée. | HAS 2023 |
| QCM-ENDO-3215 | RES-MED-095 | b | B : « stratégie séquentielle » non datée alors que la mise à jour 2025 existe | mineure | B datée « ESC/EAS 2019 ». Clé inchangée. | ESC/EAS 2019, 2025 |
| QCM-RHUM-3225 | RES-MED-098 | b | A reposant sur une durée non tranchée chez l'adulte | **majeure** | A reformulée sur un point établi ; durées par organisme dans l'explication. Clé inchangée. | OMS 2026 (module 4), ATS/CDC/IDSA 2016 |

## 6. Sources mobilisées pour l'audit (recherches web du 2026-11-19, résumés et pages de présentation — textes intégraux non lus)

- ESC, communiqué « New ESC/EACTS Guidelines for Valvular Heart Disease » (2025) : https://www.escardio.org/news/press/press-releases/New-ESC-EACTS-Guidelines-Guidelines-for-Valvular-Heart-Disease-will-help-prevent-under-treatment-of-patients-and-support/ ; PCRonline, « Key updates in valvular heart disease management: insights from the 2025 ESC/EACTS Guidelines » : https://www.pcronline.com/News/Congress-coverages/ESC/2025/Key-updates-in-valvular-heart-disease-management-insights-from-the-2025-ESC-EACTS-Guidelines ; Rev Esp Cardiol, « Insights into the 2025 ESC/EACTS guidelines » : https://www.revespcardiol.org/index.php/en-insights-into-the-2025-esceacts-guidelin-articulo-S1885585725003548
- McDonald 2024 : Practical Neurology : https://practicalneurology.com/news/2024-mcdonald-criteria-revisions-published-in-the-lancet-neurology/2483516/ ; MS Trust : https://mstrust.org.uk/news/criteria-used-diagnose-ms-updated
- ESPGHAN 2017 : PubMed 28027215 : https://pubmed.ncbi.nlm.nih.gov/28027215/ ; PDF ESPGHAN : https://www.espghan.org/dam/jcr%3A3d960daa-e2f3-499f-9df9-2da682976cec/2017%20Complementary_Feeding__A_Position_Paper_by_the.21.pdf
- SSC 2026 : SCCM : https://www.sccm.org/clinical-resources/guidelines/guidelines/surviving-sepsis-campaign-international-guidelines-for-management-of-sepsis-and-septic-shock-2026 ; ESICM : https://www.esicm.org/2026-surviving-

Les références de vérification ont été ajoutées aux `sources` des QCM concernés avec la mention « texte intégral non lu ».

## 7. Reste à faire (non bloquant)

- **Catalogue des recommandations (équipe REC)** : inscrire Fewtrell et al. 2017 (ESPGHAN, diversification) ; compléter REC-0219 (seuils chiffrés ESC/EACTS 2025 pour l'IM primaire), REC-0266 (objectif de PAM et place de la pression diastolique dans la SSC 2026), REC-0224 et REC-0415 à partir des textes intégraux.
- **Mal de Pott** : confronter QCM-RHUM-3225 au manuel du programme national algérien de lutte antituberculeuse (durée chez l'adulte) dès qu'il est acquis.
- **QCM-INFE-3012 (B)** : vérifier dans le texte SSC 2026 que l'objectif initial de PAM ≥ 65 mmHg est maintenu (proposition actuellement rattachée à la SSC 2021).
- Audit des lots `RES-03-c` et `RES-03-d` lorsqu'ils seront terminés.
- Relecture humaine qualifiée (statut `valide_enseignant`, jamais attribué par une IA).
- Sauvegardes de la version pré-audit : `00_SYSTEME/sauvegardes/20261119/21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/RES-03-a.avant_audit_AUD-03.json` et `RES-03-b.avant_audit_AUD-03.json`.
