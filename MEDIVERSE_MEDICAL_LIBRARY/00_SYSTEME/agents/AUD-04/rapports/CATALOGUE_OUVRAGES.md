# AUD-04 — Audit du catalogue des ouvrages (éditions, années, ISBN, doublons)

- **Date** : 2026-11-19 — **Agent** : AUD-04 (audit des références)
- **Périmètre** : `24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/lots/*.json` (6 lots, 449 entrées avant audit)
- **Sauvegardes préalables** : `00_SYSTEME/sauvegardes/20261119/24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/lots/<lot>.avant_audit_AUD-04.json` (6 fichiers, identiques aux lots d'origine — contrôle md5)
- **Méthode** : recherche web (WebSearch) ciblée sur les sites des éditeurs (shop.elsevier.com, evolve/inspectioncopy.elsevier.com, mheducation/mhprofessional, shop.lww.com, wwnorton, Macmillan Learning, Springer, OUP, AAP, ACS), des grands libraires (Blackwell's, Lehmanns, Readings, Mollat, livres-medicaux.com…) et des catalogues de bibliothèques (BnF, WorldCat, BU algériennes). La consultation directe des pages (WebFetch) était bloquée par le réseau de la session (mheducation.com, elsevier.com) : les informations proviennent des extraits de pages renvoyés par le moteur de recherche. Quota de 200 recherches atteint en fin de session.
- **Règles appliquées** : aucune édition remplacée silencieusement — l'état catalogué avant audit est conservé intégralement dans `edition_cataloguee_avant_audit` (édition, année, ISBN, statut, sources, titre/auteurs/éditeur si modifiés) et résumé dans `notes` ; `edition_precedente` décrit l'édition immédiatement antérieure à l'édition courante ; seuls des ISBN relevés pendant la session sont inscrits (contrôle de clé ISBN-10/13 : 0 erreur) ; les éditions seulement annoncées (pré-publication, date future ou non confirmée) ne sont **pas** retenues comme édition courante mais consignées dans `edition_annoncee`. Aucun ouvrage protégé téléchargé.

## Synthèse chiffrée

| Indicateur | Avant audit | Après audit |
|---|---|---|
| Entrées dans les lots | 449 | 442 (7 doublons retirés) |
| `verifie` | 257 | 388 |
| `partiel` | 144 | 54 |
| `non_verifie` | 48 | 0 |
| **Taux de vérification** | **57.2 %** | **87.8 %** |

- Entrées auditées (constats appliqués) : **189** — dont **147** avec édition nouvelle ou identifiée (**97** remplacements d'une édition déjà cataloguée par une édition plus récente ; 50 éditions identifiées là où aucune n'était renseignée) et **42** confirmations/compléments sans changement d'édition.
- Éditions annoncées mais non retenues (consignées dans `edition_annoncee`) : **24**.
- Doublons fusionnés : **7** (entrées archivées dans `24_BIBLIOGRAPHIE/00_CATALOGUE_OUVRAGES/doublons_retires.json`).
- Deux entrées passent de `verifie` à `partiel` parce qu'une édition plus récente existe chez l'éditeur mais que son année n'a pas pu être confirmée : OUV-0402 (Williams Obstetrics 27e) et OUV-0354 (Fitzpatrick's Dermatology 10e).

## 1. Ouvrages majeurs (priorité 1) — éditions mises à jour

| id | titre | édition avant → après | statut | source principale |
|---|---|---|---|---|
| OUV-0064 | Endocrinologie, diabétologie et maladies métaboliques | 2e (2011) → **6e (2024)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/endocrinologie-diabetologie-et-maladies-metaboliques/college-des-enseignants-dendocrinologie-diabete-et-maladie/978-2-294-78227-5) |
| OUV-0076 | E. Pilly : Maladies infectieuses et tropicales | 16e (1997) → **28e (2025)** | partiel → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/infectiologie-virologie-bacteriologie/62132-e-pilly-2025-maladies-infectieuses-et-tropicales-28e-ed.html) |
| OUV-0077 | Médecine cardiovasculaire (Les référentiels des Collèges — Réussir ses EDN) | éd. non renseignée (année non renseignée) → **3e (2025)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/medecine-cardiovasculaire/college-national-des-enseignants-de-card/978-2-294-78661-7) |
| OUV-0078 | Pneumologie : référentiel pour la préparation de l'EDN (Collège des enseignants  | éd. non renseignée (année non renseignée) → **8e (2023)** | non_verifie → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/pneumologie/54367-referentiel-edn-du-college-de-pneumologie-r2c.html) |
| OUV-0079 | Hépato-gastro-entérologie – Chirurgie digestive (Les référentiels des Collèges) | éd. non renseignée (année non renseignée) → **5e (2022)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/hepato-gastro-enterologie-chirurgie-digestive/cdu-hge/978-2-294-77112-5) |
| OUV-0080 | Néphrologie (Collège universitaire des enseignants de néphrologie — EDN, les réf | éd. non renseignée (année non renseignée) → **11e (2024)** | non_verifie → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/nephrologie/61175-college-nephrologie-r2c-11e-ed.html) |
| OUV-0081 | Neurologie | éd. non renseignée (année non renseignée) → **7e (2025)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/neurologie/college-des-enseignants-de-neurologie/978-2-294-78607-5) |
| OUV-0082 | Référentiel de psychiatrie et addictologie : psychiatrie de l'adulte, psychiatri | éd. non renseignée (année non renseignée) → **4e (2024)** | non_verifie → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/psychiatrie/58052-ecn-referentiel-de-psychiatrie-et-addictologie-4e-edition-conforme-a-la-r2c-psychiatrie-de-l-adu.html) |
| OUV-0083 | Dermatologie | éd. non renseignée (année non renseignée) → **8e (2022)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/dermatologie/cedef/978-2-294-76707-4) |
| OUV-0084 | Rhumatologie | éd. non renseignée (année non renseignée) → **8e (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/rhumatologie/cofer/978-2-294-78261-9) |
| OUV-0085 | Hématologie | éd. non renseignée (année non renseignée) → **5e (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/hematologie/societe-francaise-dhematologie/978-2-294-78280-0) |
| OUV-0086 | Cancérologie (Collège national des enseignants en cancérologie — R2C/EDN) | éd. non renseignée (année non renseignée) → **4e (2024)** | non_verifie → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/cancerologie/60579-college-cancerologie-4eme-edition-R2C.html) |
| OUV-0087 | Pédiatrie | éd. non renseignée (année non renseignée) → **9e (2023)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/pediatrie/cnpu-college-national-des-pediatres-universitaires/978-2-294-77983-1) |
| OUV-0088 | Gynécologie obstétrique | éd. non renseignée (année non renseignée) → **6e (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/gynecologie-obstetrique/college-national-des-gynecologues-et-obstetriciens-francais/978-2-294-78091-2) |
| OUV-0089 | Gériatrie | éd. non renseignée (année non renseignée) → **5e (2021)** | non_verifie → verifie | [www.elsevier.com](https://www.elsevier.com/connect/referentiel-des-colleges-geriatrie-edition-2021) |
| OUV-0090 | Urologie | éd. non renseignée (année non renseignée) → **6e (2024)** | non_verifie → verifie | [www.elsevier.com](https://www.elsevier.com/en-au/connect/referentiel-des-colleges-urologie-6e-edition-2024) |
| OUV-0091 | ORL et chirurgie cervico-faciale | éd. non renseignée (année non renseignée) → **5e (2022)** | non_verifie → verifie | [www.elsevier.com](https://www.elsevier.com/en-au/connect/nouvelle-edition-2022-du-referentiel-des-colleges-orl) |
| OUV-0092 | Ophtalmologie | éd. non renseignée (année non renseignée) → **6e (2025)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/ophtalmologie/college-des-ophtalmologistes-universitaires-de-france/978-2-294-78662-4) |
| OUV-0093 | Imagerie médicale : radiologie et médecine nucléaire (Les référentiels des Collè | éd. non renseignée (année non renseignée) → **3e (2022)** | non_verifie → verifie | [www.elsevier.com](https://www.elsevier.com/en-au/connect/referentiel-des-colleges-imagerie-medicale-edition-2022) |
| OUV-0094 | Médecine physique et de réadaptation | éd. non renseignée (année non renseignée) → **8e (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/medecine-physique-et-de-readaptation/cofemer/978-2-294-78263-3) |
| OUV-0095 | Médecine intensive, réanimation, urgences et défaillances viscérales aiguës | éd. non renseignée (année non renseignée) → **8e (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/medecine-intensive-reanimation-urgences-et-defaillances-viscerales-aigues/college-des-enseignants-de-medecine/978-2-294-78167-4) |
| OUV-0096 | Santé publique | éd. non renseignée (année non renseignée) → **5e (2022)** | non_verifie → partiel | [bibliotheques-numeriques.defense.gouv.fr](https://bibliotheques-numeriques.defense.gouv.fr/index.php/impression/document/33f1d0a4-2387-409f-886a-be664a24e5e6) |
| OUV-0097 | Médecine légale – Médecine du travail | éd. non renseignée (année non renseignée) → **3e (2025)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/medecine-legale-medecine-du-travail/college-national-des-enseignants-de/978-2-294-78743-0) |
| OUV-0098 | Chirurgie maxillo-faciale et stomatologie (Les référentiels des Collèges — Réuss | éd. non renseignée (année non renseignée) → **6e (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/chirurgie-maxillo-faciale/cnecmf-college-national-des-enseignants-de-chirurgie-maxill/978-2-294-78543-6) |
| OUV-0099 | Orthopédie, traumatologie (EDN, les référentiels) | éd. non renseignée (année non renseignée) → **4e (2024)** | non_verifie → verifie | [unitheque.com](https://unitheque.com/UploadFile/DocumentPDF/R/E/9782340093850-referentiel-college-orthopedie-traumatologie-sommaire.pdf) |
| OUV-0100 | Immunopathologie (Les référentiels des Collèges) | éd. non renseignée (année non renseignée) → **3e (2022)** | non_verifie → verifie | [www.elsevier.com](https://www.elsevier.com/connect/referentiel-des-colleges-immunopathologie-2022) |
| OUV-0101 | Anatomie et cytologie pathologiques | éd. non renseignée (année non renseignée) → **4e (2023)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/anatomie-et-cytologie-pathologiques/college-francais-des-pathologistes/978-2-294-77830-8) |
| OUV-0102 | Génétique médicale | éd. non renseignée (année non renseignée) → **3e (2026)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/genetique-medicale/cnepgm-college-national-des-enseignants-et-praticiens-de-ge/978-2-294-78970-0) |
| OUV-0103 | Nutrition | éd. non renseignée (année non renseignée) → **5e (2024)** | non_verifie → verifie | [www.elsevier.com](https://www.elsevier.com/connect/nouvelle-edition-du-referentiel-des-colleges-nutrition) |
| OUV-0104 | Médecine générale (Les référentiels des Collèges — Réussir ses EDN) | éd. non renseignée (année non renseignée) → **1re (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/medecine-generale/cnge/978-2-294-78183-4) |
| OUV-0105 | Le bon usage du médicament et des thérapeutiques non médicamenteuses | éd. non renseignée (année non renseignée) → **6e (actualisée) (2024)** | non_verifie → verifie | [www.mollat.com](https://www.mollat.com/livres/2562719/college-national-de-pharmacologie-medicale-france-le-bon-usage-du-medicament-et-des-therapeutiques-non-medicamenteuses-r2c) |
| OUV-0106 | Chirurgie générale, viscérale et digestive (référentiel du Collège — R2C/EDN) | éd. non renseignée (année non renseignée) → **3e (année non renseignée)** | non_verifie → partiel | [www.livres-medicaux.com](https://www.livres-medicaux.com/chirurgie-generale-et-viscerale/23338-chirurgie-generale-viscerale-et-digestive.html) |
| OUV-0107 | Neurochirurgie (Les référentiels des Collèges) | éd. non renseignée (année non renseignée) → **4e (2025)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/neurochirurgie/college-de-neurochirurgie/978-2-294-78744-7) |
| OUV-0108 | PILLY Étudiant 2023 : maladies infectieuses & tropicales (R2C, EDN) | éd. non renseignée (année non renseignée) → **2e (Pilly Étudiant 2023) (2023)** | non_verifie → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/maladies-infectieuses/52034-pilly-etudiant-2023-r2c-ecni-edn.html) |
| OUV-0150 | Gray's Anatomy: The Anatomical Basis of Clinical Practice | 42e (2020) → **43e (2025)** | verifie → verifie | [www.inspectioncopy.elsevier.com](https://www.inspectioncopy.elsevier.com/book/details/9780443124785) |
| OUV-0152 | Gray's Anatomy for Students | éd. non renseignée (année non renseignée) → **5e (2023)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/grays-anatomy-for-students/drake/978-0-323-93423-7) |
| OUV-0162 | Junqueira's Basic Histology: Text and Atlas | 17e (2024) → **18e (2026)** | verifie → verifie | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/junqueira-s-basic-histology-text-atlas-18th-edition.html) |
| OUV-0166 | Langman's Medical Embryology | 12e (2012) → **15e (2023)** | partiel → verifie | [shop.lww.com](https://shop.lww.com/Langman-s-Medical-Embryology/p/9781975179960) |
| OUV-0170 | Guyton and Hall Textbook of Medical Physiology | 14e (2021) → **15e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-443-11101-3) |
| OUV-0182 | Lehninger Principles of Biochemistry | 7e (2017) → **8e (2021)** | partiel → verifie | [macmillanlearning.com](https://macmillanlearning.com/ed/au/product/Lehninger-Principles-of-Biochemistry-/p/1319381499) |
| OUV-0187 | Harper's Illustrated Biochemistry | éd. non renseignée (année non renseignée) → **32e (2022)** | non_verifie → verifie | [www.mhprofessional.com](https://www.mhprofessional.com/harper-s-illustrated-biochemistry-thirty-second-edition-9781260469943-usa) |
| OUV-0188 | Janeway's Immunobiology | 9e (2017) → **10e (2022)** | partiel → verifie | [wwnorton.co.uk](https://wwnorton.co.uk/books/9780393884913-janeway-s-immunobiology-2c7aa902-41ed-4ba8-8f6a-a79e3e0308ab) |
| OUV-0189 | Cellular and Molecular Immunology (Abbas, Lichtman, Pillai) | 9e (2018) → **11e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/cellular-and-molecular-immunology/abbas/978-0-443-28358-1) |
| OUV-0194 | Thompson & Thompson Genetics and Genomics in Medicine | 8e (2016) → **9e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/thompson-and-thompson-genetics-and-genomics-in-medicine/cohn/978-0-323-54762-8) |
| OUV-0201 | Rang & Dale's Pharmacology | 8e (2016) → **10e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/rang-and-dales-pharmacology/ritter/978-0-323-87395-6) |
| OUV-0220 | Robbins, Cotran & Kumar Pathologic Basis of Disease | 10e (2021) → **11e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/robbins-cotran-and-kumar-pathologic-basis-of-disease/kumar/978-0-443-26452-8) |
| OUV-0221 | Robbins & Kumar Basic Pathology | 10e (2018) → **11e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/robbins-kumar-basic-pathology/kumar/978-0-323-79018-5) |
| OUV-0301 | Goldman-Cecil Medicine | 26e (2020) → **27e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/goldman-cecil-medicine-2-volume-set/goldman/978-0-323-93038-3) |
| OUV-0319 | Braunwald's Heart Disease: A Textbook of Cardiovascular Medicine | 11e (2019) → **13e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/braunwald-s-heart-disease-2-volume-set/bonow/978-0-443-24974-7) |
| OUV-0327 | Murray & Nadel's Textbook of Respiratory Medicine | 6e (2016) → **7e (2021)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/murray-and-nadels-textbook-of-respiratory-medicine-2-volume-set/broaddus/978-0-323-65587-3) |
| OUV-0331 | Sleisenger and Fordtran's Gastrointestinal and Liver Disease | 11e (2021) → **12e (2025)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/sleisenger-and-fordtrans-gastrointestinal-and-liver-disease-2-volume-set/chung/978-0-443-11657-5) |
| OUV-0339 | Brenner & Rector's The Kidney | 11e (2020) → **12e (2026)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/brenner-and-rectors-the-kidney-2-volume-set/luyckx/978-0-443-10641-5) |
| OUV-0354 | Fitzpatrick's Dermatology | 9e (2019) → **10e (année non renseignée)** | verifie → partiel | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/fitzpatrick-s-dermatology-tenth-edition-bundle.html) |
| OUV-0360 | Firestein & Kelley's Textbook of Rheumatology | 11e (2021) → **12e (2024)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/firestein-and-kelley-s-textbook-of-rheumatology-2-volume-set/firestein/978-0-323-93540-1) |
| OUV-0366 | Williams Textbook of Endocrinology | 14e (2020) → **15e (2024)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/williams-textbook-of-endocrinology/melmed/978-0-323-93230-1) |
| OUV-0381 | Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases | 9e (2020) → **10e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/mandell-douglas-and-bennetts-principles-and-practice-of-infectious-diseases/blaser/978-0-323-93499-2) |
| OUV-0402 | Williams Obstetrics | 26e (2022) → **27e (année non renseignée)** | verifie → partiel | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/williams-obstetrics-27e.html) |
| OUV-0500 | Sabiston Textbook of Surgery: The Biological Basis of Modern Surgical Practice | 20e (2017) → **22e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/sabiston-textbook-of-surgery/scott-tyler/978-0-443-12434-1) |
| OUV-0510 | Campbell-Walsh-Wein Urology | 12e (2021) → **13e (2025)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/campbell-walsh-wein-urology/dmochowski/978-0-323-88405-1) |
| OUV-0530 | Cummings Otolaryngology: Head and Neck Surgery | 7e (2021) → **8e (2025)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/cummings-otolaryngology/francis/978-0-443-11984-2) |
| OUV-0534 | Kanski's Clinical Ophthalmology: A Systematic Approach | 9e (2020) → **10e (2024)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/kanskis-clinical-ophthalmology/salmon/978-0-443-11099-3) |
| OUV-0650 | Miller's Anesthesia | 9e (2020) → **10e (2024)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/millers-anesthesia-2-volume-set/gropper/978-0-323-93592-0) |
| OUV-0655 | Rosen's Emergency Medicine: Concepts and Clinical Practice | 9e (2018) → **10e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/rosens-emergency-medicine-concepts-and-clinical-practice/walls/978-0-323-75789-8) |

## 2. Ouvrages majeurs — confirmés sans changement d'édition

| id | titre | édition avant → après | statut | source principale |
|---|---|---|---|---|
| OUV-0057 | Anatomie clinique | 4e (2009) → **4e (2009)** | partiel → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/etudiants-medecine/1679-kamina-anatomie-clinique-4-edition-tome-1-anatomie-generale-membres.html) |
| OUV-0200 | Goodman & Gilman's The Pharmacological Basis of Therapeutics | 14e (2023) → **14e (2023)** | verifie → verifie | [blackwells.co.uk](https://blackwells.co.uk/bookshop/product/Goodman--Gilmans-The-Pharmacological-Basis-of-Therapeutics-by-Laurence-L-Brunton-editor-Bjrn-C-Knollmann-editor-Louis-S-Goodman/9781264258079) |
| OUV-0343 | Adams and Victor's Principles of Neurology | 12e (2023) → **12e (2023)** | verifie → verifie | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/adams-victor-s-principles-neurology-twelfth-edition.html) |
| OUV-0386 | Nelson Textbook of Pediatrics | 22e (2025) → **22e (2025)** | verifie → verifie | [evolve.elsevier.com](https://evolve.elsevier.com/cs/product/9780323883054?role=student) |
| OUV-0396 | Williams Gynecology | 4e (2020) → **4e (2020)** | verifie → verifie | [www.mhprofessional.com](https://www.mhprofessional.com/williams-gynecology-fourth-edition-9781260456868-usa) |
| OUV-0501 | Schwartz's Principles of Surgery | 11e (2019) → **11e (2019)** | verifie → verifie | [www.mhprofessional.com](https://www.mhprofessional.com/schwartz-s-principles-of-surgery-2-volume-set-11th-edition-9781259835353-usa-group) |

Ouvrages majeurs **non re-contrôlés** dans cette session (déjà `verifie` sur page éditeur par le premier catalogueur, édition récente : quota de recherche épuisé) : OUV-0300, OUV-0520, OUV-0312, OUV-0374, OUV-0347 (Harrison's 22e 2025, Rockwood and Green's 10e 2025, Wintrobe's 15e 2024, DeVita 12e 2023, Kaplan & Sadock's 11e 2025).

## 3. Priorité 2 et autres ouvrages — éditions mises à jour ou identifiées

| id | titre | édition avant → après | statut | source principale |
|---|---|---|---|---|
| OUV-0058 | Anatomie humaine : descriptive, topographique et fonctionnelle | 13e (1991) → **15e (révisée par V. Delmas) (2002)** | partiel → verifie | [nantilus.univ-nantes.fr](https://nantilus.univ-nantes.fr/vufind/Record/PPN067332838/TOC?lng=en) |
| OUV-0060 | Embryologie humaine : de la molécule à la clinique | 3e (2003) → **4e (année non renseignée)** | partiel → partiel | [syngeb.centre-univ-mila.dz](https://syngeb.centre-univ-mila.dz/fr/opac/download_document/925833) |
| OUV-0063 | Dermatologie et infections sexuellement transmissibles | 6e (2017) → **7e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/dermatologie-et-infections-sexuellement-transmissibles/thomas/978-2-294-77608-3) |
| OUV-0069 | Pédiatrie pour le praticien | 5e (2008) → **7e (2020)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/pediatrie-pour-le-praticien/benoist/978-2-294-76068-6) |
| OUV-0070 | Traité de médecine | 4e (2004) → **5e (2018)** | partiel → partiel | [www.livres-medicaux.com](https://www.livres-medicaux.com/medecine-generale/16464-traite-de-medecine-5-edition-tome-1.html) |
| OUV-0071 | Traité de médecine légale et criminalistique | éd. non renseignée (2008) → **3e (2022)** | partiel → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/medecine-legale/48035-traite-de-medecine-legale-et-criminalistique.html) |
| OUV-0073 | Dorosz : guide pratique des médicaments 2026 | 22e (2002) → **45e (Dorosz 2026) (2025)** | partiel → verifie | [www.mollat.com](https://www.mollat.com/livres/3405769/philippe-dorosz-guide-pratique-des-medicaments-2026) |
| OUV-0075 | Échocardiographie clinique | 6e (2010) → **7e (2016)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/echocardiographie-clinique/klimczak/978-2-294-74896-7) |
| OUV-0109 | Atlas Netter d'anatomie humaine (traduction française) | éd. non renseignée (année non renseignée) → **8e (2023)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/atlas-netter-danatomie-humaine/netter/978-2-294-77369-3) |
| OUV-0110 | Gray's Anatomie – Le Manuel pour les étudiants (traduction française) | éd. non renseignée (année non renseignée) → **5e (2025)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/grays-anatomie-le-manuel-pour-les-etudiants/drake/978-2-294-77925-1) |
| OUV-0111 | Précis de physiologie médicale (traduction française de Guyton & Hall) | éd. non renseignée (année non renseignée) → **2e éd. française (2003)** | non_verifie → partiel | [bibliotheques-numeriques.defense.gouv.fr](https://bibliotheques-numeriques.defense.gouv.fr/shd/impression/document/ba7f853a-7fa7-481b-bc22-d5b7f112aa14) |
| OUV-0112 | Harrison : principes de médecine interne (traduction française) | éd. non renseignée (année non renseignée) → **18e (traduction française) (2013)** | non_verifie → verifie | [bibliotheques-numeriques.defense.gouv.fr](https://bibliotheques-numeriques.defense.gouv.fr/impression/document/08bea950-f5d1-4dc6-b3f3-3bdcbe84d9d6) |
| OUV-0153 | Netter Atlas of Human Anatomy: Classic Regional Approach | 7e (2019) → **9e (2026)** | partiel → verifie | [www.us.elsevierhealth.com](https://www.us.elsevierhealth.com/netter-atlas-of-human-anatomy-classic-regional-approach-9780443118685.html) |
| OUV-0157 | Sobotta Atlas of Anatomy (17th ed., English/Latin) — 3 volumes | 14e (2008) → **17e (English/Latin) (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/sobotta-atlas-of-anatomy-package-17th-ed-english-latin/paulsen/978-0-7020-6764-8) |
| OUV-0160 | Snell's Clinical Anatomy by Regions | 10e (2019) → **11e (2024)** | verifie → verifie | [www.wolterskluwer.com](https://www.wolterskluwer.com/en/solutions/ovid/clinical-anatomy-by-regions-15374) |
| OUV-0163 | Histology: A Text and Atlas, with Correlated Cell and Molecular Biology (Ross &  | 8e (2020) → **9e (2023)** | partiel → verifie | [shop.lww.com](https://shop.lww.com/Histology--A-Text-and-Atlas/p/9781975181512) |
| OUV-0164 | Wheater's Functional Histology: A Text and Colour Atlas | 6e (2014) → **7e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/wheaters-functional-histology/odowd/978-0-7020-8334-1) |
| OUV-0167 | Larsen's Human Embryology | 4e (2009) → **6e (2020)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/larsens-human-embryology/schoenwolf/978-0-323-69604-3) |
| OUV-0168 | The Developing Human: Clinically Oriented Embryology | 11e (2020) → **12e (2024)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/the-developing-human/torchia/978-0-443-11698-8) |
| OUV-0171 | Ganong's Review of Medical Physiology | éd. non renseignée (année non renseignée) → **27e (2025)** | non_verifie → verifie | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/ganong-s-review-medical-physiology-27th-edition.html) |
| OUV-0173 | Berne & Levy Physiology | 7e (2018) → **8e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/berne-and-levy-physiology/koeppen/978-0-323-84790-2) |
| OUV-0174 | Costanzo Physiology | 6e (2018) → **7e (2021)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/costanzo-physiology/costanzo/978-0-323-79333-9) |
| OUV-0177 | West's Respiratory Physiology: The Essentials | 10e (2016) → **11e (2020)** | partiel → verifie | [shop.lww.com](https://shop.lww.com/West-s-Respiratory-Physiology/p/9781975139186) |
| OUV-0178 | Intermediate Physics for Medicine and Biology | 4e (2007) → **5e (2015)** | partiel → verifie | [www.springer.com](https://www.springer.com/de/book/9783319126814) |
| OUV-0183 | Biochemistry (Berg, Tymoczko, Gatto, Stryer) | 9e (2019) → **10e (2023)** | partiel → verifie | [store.macmillanlearning.com](https://store.macmillanlearning.com/us/p/9781319333621) |
| OUV-0190 | Basic Immunology: Functions and Disorders of the Immune System | 6e (2020) → **7e (2023)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/basic-immunology/abbas/978-0-443-10519-7) |
| OUV-0191 | Roitt's Essential Immunology | 12e (2011) → **13e (2017)** | partiel → verifie | [www.sack.de](https://www.sack.de/delves-martin-burton-roitts-essential-immunology/9781118415771) |
| OUV-0193 | The Immune System (Parham) | 4e (2015) → **5e (2021)** | partiel → verifie | [www.barnesandnoble.com](https://www.barnesandnoble.com/w/the-immune-system-peter-parham/1119682852) |
| OUV-0195 | Emery's Elements of Medical Genetics and Genomics | 14e (2012) → **16e (2021)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/emerys-elements-of-medical-genetics-and-genomics/turnpenny/978-0-7020-7966-5) |
| OUV-0202 | Katzung's Basic and Clinical Pharmacology | éd. non renseignée (année non renseignée) → **16e (2023)** | non_verifie → verifie | [www.mhprofessional.com](https://www.mhprofessional.com/katzung-s-basic-and-clinical-pharmacology-16th-edition-9781260463309-usa) |
| OUV-0206 | Medical Microbiology (Murray, Rosenthal, Pfaller) | 9e (2021) → **10e (2025)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/medical-microbiology/murray/978-0-443-26133-6) |
| OUV-0208 | Jawetz, Melnick & Adelberg's Medical Microbiology | éd. non renseignée (année non renseignée) → **29e (2025)** | non_verifie → verifie | [www.mhprofessional.com](https://www.mhprofessional.com/jawetz-melnick-adelbergs-medical-microbiology-twenty-ninth-edition-9781265109509-usa) |
| OUV-0209 | Manual of Clinical Microbiology | 12e (2019) → **13e (2023)** | partiel → verifie | [www.schweitzer-online.de](https://www.schweitzer-online.de/en/buch/Manual-Clinical-Microbiology-Multi-Volume/9781683674290/B612853/) |
| OUV-0214 | Clinical Immunology: Principles and Practice (Rich) | 5e (2019) → **6e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/clinical-immunology/rich/978-0-7020-8165-1) |
| OUV-0219 | The Autoimmune Diseases (Rose & Mackay) | 5e (2014) → **6e (2019)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/the-autoimmune-diseases/rose/978-0-12-812102-3) |
| OUV-0223 | Mills and Sternberg's Diagnostic Surgical Pathology | 5e (2010) → **7e (2022)** | partiel → verifie | [shop.lww.com](https://shop.lww.com/Mills-and-Sternberg-s-Diagnostic-Surgical-Pathology/p/9781975150723) |
| OUV-0226 | Tietz Fundamentals of Clinical Chemistry and Molecular Diagnostics | 8e (2019) → **9e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/tietz-fundamentals-of-clinical-chemistry-and-molecular-diagnostics/rifai/978-0-323-93583-8) |
| OUV-0227 | Tietz Textbook of Laboratory Medicine | éd. non renseignée (année non renseignée) → **7e (2022)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/tietz-textbook-of-laboratory-medicine/rifai/978-0-323-77572-4) |
| OUV-0303 | Davidson's Principles and Practice of Medicine | 24e (2023) → **25e (2026)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/davidsons-principles-and-practice-of-medicine/strachan/978-0-443-28760-2) |
| OUV-0304 | Kumar & Clark's Clinical Medicine | 10e (2021) → **11e (2025)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/kumar-and-clarks-clinical-medicine/randall/978-0-443-12594-2) |
| OUV-0305 | Cecil Essentials of Medicine | 9e (2015) → **10e (2021)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/cecil-essentials-of-medicine/wing/978-0-323-72271-1) |
| OUV-0306 | Oxford Handbook of Clinical Medicine | 9e (2014) → **11e (2024)** | partiel → verifie | [www.oup.com.au](https://www.oup.com.au/books/higher-education/medicine-dentistry/9780198844013) |
| OUV-0307 | Macleod's Clinical Examination | 14e (2018) → **15e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/macleods-clinical-examination/dover/978-0-323-84770-4) |
| OUV-0309 | CURRENT Medical Diagnosis & Treatment 2026 | éd. non renseignée (année non renseignée) → **65e (CMDT 2026) (2025)** | non_verifie → verifie | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/current-medical-diagnosis-treatment-2026.html) |
| OUV-0314 | Hematology: Basic Principles and Practice (Hoffman) | 7e (2018) → **8e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/hematology/hoffman/978-0-323-73388-5) |
| OUV-0330 | West's Pulmonary Pathophysiology: The Essentials | 9e (2017) → **10e (2021)** | partiel → verifie | [shop.lww.com](https://shop.lww.com/West-s-Pulmonary-Pathophysiology/p/9781975152819) |
| OUV-0340 | Comprehensive Clinical Nephrology | 6e (2019) → **7e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/comprehensive-clinical-nephrology/johnson/978-0-323-82592-4) |
| OUV-0344 | Bradley and Daroff's Neurology in Clinical Practice | 7e (2016) → **9e (2026)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/bradley-and-daroffs-neurology-in-clinical-practice-2-volume-set/jankovic/978-0-443-28403-8) |
| OUV-0346 | Swaiman's Pediatric Neurology: Principles and Practice | 6e (2018) → **7e (2025)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/swaimans-pediatric-neurology/ashwal/978-0-443-10944-7) |
| OUV-0352 | Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revis | éd. non renseignée (année non renseignée) → **5e, révision du texte (DSM-5-TR) (2022)** | non_verifie → verifie | [www.barnesandnoble.com](https://www.barnesandnoble.com/w/diagnostic-and-statistical-manual-of-mental-disorders-fifth-edition-text-revision-american-psychiatric/1147203778) |
| OUV-0357 | Andrews' Diseases of the Skin: Clinical Dermatology | 13e (2020) → **14e (2024)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/andrews-diseases-of-the-skin/james/978-0-323-87870-8) |
| OUV-0359 | Paller and Mancini – Hurwitz Clinical Pediatric Dermatology | 5e (2016) → **6e (2021)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/paller-and-mancini-hurwitz-clinical-pediatric-dermatology/paller/978-0-323-54988-2) |
| OUV-0361 | Rheumatology (Hochberg) | 7e (2019) → **8e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/rheumatology-2-volume-set/hochberg/978-0-7020-8133-0) |
| OUV-0368 | DeGroot's Endocrinology: Basic Science and Clinical Practice | éd. non renseignée (année non renseignée) → **8e (2023)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/degroots-endocrinology/robertson/978-0-323-69412-4) |
| OUV-0382 | Manson's Tropical Diseases | 23e (2014) → **24e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/mansons-tropical-diseases/farrar/978-0-7020-7959-7) |
| OUV-0385 | Red Book: 2024–2027 Report of the Committee on Infectious Diseases | éd. non renseignée (année non renseignée) → **33e (2024–2027) (2024)** | non_verifie → verifie | [aap.org](https://aap.org/Red-Book-2024-Report-of-the-Committee-on-Infectious-Diseases-33rd-Edition-Paperback) |
| OUV-0389 | Nelson Essentials of Pediatrics | 8e (2019) → **9e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/nelson-essentials-of-pediatrics/marcdante/978-0-323-77562-5) |
| OUV-0391 | Avery's Diseases of the Newborn | 10e (2018) → **11e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/averys-diseases-of-the-newborn/sawyer/978-0-323-82823-9) |
| OUV-0399 | Te Linde's Operative Gynecology | 12e (2020) → **13e (2023)** | verifie → verifie | [shop.lww.com](https://shop.lww.com/Te-Linde-s-Operative-Gynecology/p/9781975200091) |
| OUV-0400 | Comprehensive Gynecology | 7e (2017) → **8e (2021)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/comprehensive-gynecology/gershenson/978-0-323-65399-2) |
| OUV-0403 | Gabbe's Obstetrics: Normal and Problem Pregnancies | 8e (2021) → **9e (2024)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/gabbes-obstetrics-normal-and-problem-pregnancies/landon/978-0-323-93727-6) |
| OUV-0404 | Creasy and Resnik's Maternal-Fetal Medicine: Principles and Practice | 8e (2019) → **9e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/creasy-and-resniks-maternal-fetal-medicine/lockwood/978-0-323-82849-9) |
| OUV-0412 | Murtagh General Practice | 6e (2015) → **8e (2021)** | partiel → verifie | [www.mheducation.com.au](https://www.mheducation.com.au/murtagh-general-practice-8th-edition-9781743768235-aus) |
| OUV-0504 | The Washington Manual of Surgery | 7e (2016) → **9e (2023)** | partiel → verifie | [shop.lww.com](https://shop.lww.com/The-Washington-Manual-of-Surgery/p/9781975201258) |
| OUV-0508 | Blumgart's Surgery of the Liver, Biliary Tract, and Pancreas | 6e (2017) → **7e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/blumgarts-surgery-of-the-liver-biliary-tract-and-pancreas-2-volume-set/jarnagin/978-0-323-69784-2) |
| OUV-0514 | Campbell's Operative Orthopaedics | 13e (2017) → **15e (2026)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/campbells-operative-orthopaedics-4-volume-set/azar/978-0-443-11763-3) |
| OUV-0517 | Tachdjian's Pediatric Orthopaedics: From the Texas Scottish Rite Hospital for Ch | 5e (2014) → **6e (2021)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/tachdjians-pediatric-orthopaedics-from-the-texas-scottish-rite-hospital-for-children-6th-edition/herring/978-0-323-56769-5) |
| OUV-0523 | AO Principles of Fracture Management | éd. non renseignée (2000) → **3e (2017)** | partiel → verifie | [www.aofoundation.org](https://www.aofoundation.org/what-we-do/education/topic-areas/publishing-and-faculty-support-media/ao-principles-of-fracture-management) |
| OUV-0524 | Advanced Trauma Life Support (ATLS): Student Course Manual | 8e (2008) → **11e (ATLS 11) (2025)** | partiel → verifie | [store.facs.org](https://store.facs.org/atls-11th-edition-printed-manual-english) |
| OUV-0525 | Youmans and Winn Neurological Surgery | 7e (2017) → **8e (2022)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/youmans-and-winn-neurological-surgery/winn/978-0-323-66192-8) |
| OUV-0535 | Ophthalmology (Yanoff & Duker) | 5e (2019) → **6e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/ophthalmology/yanoff/978-0-323-79515-9) |
| OUV-0537 | Basic and Clinical Science Course (BCSC), 2026–2027 — Complete Print Set | éd. non renseignée (année non renseignée) → **2026–2027 (2026)** | non_verifie → verifie | [mngbookshop.co.uk](https://mngbookshop.co.uk/9798897300167/2026-2027-basic-and-clinical-science-course-complete-print-set/) |
| OUV-0541 | Rutherford's Vascular Surgery and Endovascular Therapy | 9e (2019) → **11e (2026)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/rutherfords-vascular-surgery-and-endovascular-therapy-2-volume-set/sidawy/978-0-443-28617-9) |
| OUV-0550 | Holcomb and Ashcraft's Pediatric Surgery | 7e (2020) → **8e (2026)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/holcomb-and-ashcrafts-pediatric-surgery/st-peter/978-0-443-12431-0) |
| OUV-0555 | Plastic Surgery (Neligan) | 4e (2018) → **5e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/plastic-surgery-6-volume-set/neligan/978-0-323-81037-1) |
| OUV-0556 | Green's Operative Hand Surgery | 7e (2017) → **8e (2021)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/greens-operative-hand-surgery/wolfe/978-0-323-69793-4) |
| OUV-0560 | Newman and Carranza's Clinical Periodontology and Implantology | 13e (2019) → **14e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/newman-and-carranzas-clinical-periodontology-and-implantology/newman/978-0-323-87887-6) |
| OUV-0565 | Cohen's Pathways of the Pulp | 11e (2016) → **12e (2020)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/cohens-pathways-of-the-pulp/berman/978-0-323-67303-7) |
| OUV-0567 | Shafer's Textbook of Oral Pathology | éd. non renseignée (année non renseignée) → **10e (2024)** | non_verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/shafers-textbook-of-oral-pathology/sivapathasundharam/978-81-312-6935-0) |
| OUV-0661 | Marino's The ICU Book | 4e (2014) → **5e (2024)** | partiel → verifie | [shop.lww.com](https://shop.lww.com/Marino-s-The-ICU-Book--Print---eBook-with-Updates/p/9781975176709) |
| OUV-0662 | Textbook of Critical Care (Vincent, Abraham, Moore, Kochanek, Fink) | 7e (2017) → **8e (2023)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/textbook-of-critical-care/vincent/978-0-323-75929-8) |
| OUV-0687 | Spitz and Fisher's Medicolegal Investigation of Death | 4e (2006) → **5e (2020)** | partiel → verifie | [test.blackwells.co.uk](https://test.blackwells.co.uk/bookshop/product/Spitz-and-Fishers-Medicolegal-Investigation-of-Death-by-Werner-U-Spitz-editor-Francisco-J-Diaz-editor-Russell-S-Fisher-past-editor/9780398093129) |
| OUV-0695 | Oxford Textbook of Global Public Health | 6e (2015) → **7e (2021)** | partiel → verifie | [ph.ucla.edu](https://ph.ucla.edu/news-events/magazine/faculty-books/oxford-textbook-global-public-health-seventh-edition) |
| OUV-0708 | Braddom's Physical Medicine & Rehabilitation | 5e (2016) → **7e (2025)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/braddoms-physical-medicine-and-rehabilitation/cifu/978-0-443-26438-2) |

## 4. Priorité 2 et autres — confirmations / compléments (édition inchangée)

| id | titre | édition avant → après | statut | source principale |
|---|---|---|---|---|
| OUV-0011 | Antibiotiques | 2e (actualisée) (année non renseignée) → **2e (actualisée) (année non renseignée)** | partiel → partiel | [bibliotheque.univ-annaba.dz](https://bibliotheque.univ-annaba.dz/fr/opac/download_document/813363) |
| OUV-0012 | Plantes médicinales d'Algérie | éd. non renseignée (1998) → **éd. non renseignée (1998)** | partiel → partiel | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/44183) |
| OUV-0021 | Précis de sémiologie | éd. non renseignée (2015) → **éd. non renseignée (2015)** | partiel → partiel | [di.univ-blida.dz](https://di.univ-blida.dz/jspui/handle/123456789/32245) |
| OUV-0027 | Néphrologie | éd. non renseignée (2009) → **éd. non renseignée (2009)** | partiel → verifie | [di.univ-blida.dz](https://di.univ-blida.dz/jspui/handle/123456789/32320) |
| OUV-0028 | Maladies rénales | éd. non renseignée (2015) → **éd. non renseignée (2015)** | partiel → verifie | [di.univ-blida.dz](https://di.univ-blida.dz/jspui/handle/123456789/36821) |
| OUV-0029 | Les maladies endocriniennes et métaboliques par illustration | éd. non renseignée (2010) → **éd. non renseignée (2010)** | partiel → verifie | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/44161) |
| OUV-0032 | Cancer du poumon en Algérie | éd. non renseignée (2005) → **éd. non renseignée (2005)** | partiel → verifie | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/44016) |
| OUV-0037 | Urgences en pédiatrie | éd. non renseignée (2017) → **éd. non renseignée (2017)** | partiel → verifie | [di.univ-blida.dz](https://di.univ-blida.dz/jspui/handle/123456789/16882) |
| OUV-0038 | Guide thérapeutique en pédiatrie | 2e (2012) → **2e (2012)** | partiel → verifie | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/44218) |
| OUV-0039 | Guide diagnostique en pédiatrie | éd. non renseignée (2011) → **éd. non renseignée (2011)** | partiel → verifie | [di.univ-blida.dz](https://di.univ-blida.dz/jspui/handle/123456789/34996) |
| OUV-0040 | L'essentiel en pédiatrie (3 tomes) | éd. non renseignée (2015) → **éd. non renseignée (2015)** | partiel → verifie | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/44185) |
| OUV-0041 | Nutrition pédiatrique | éd. non renseignée (2014) → **éd. non renseignée (2014)** | partiel → verifie | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/44137) |
| OUV-0048 | 168 exercices corrigés d'épidémiologie et de biostatistique | 3e (2010) → **3e (2010)** | partiel → verifie | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/43889) |
| OUV-0049 | Épidémiologie et biostatistique à l'usage des étudiants en sciences médicales | éd. non renseignée (2009) → **éd. non renseignée (2009)** | partiel → verifie | [di.univ-blida.dz](https://di.univ-blida.dz/jspui/handle/123456789/31662) |
| OUV-0053 | Système de santé et population en Algérie | éd. non renseignée (2002) → **éd. non renseignée (2002)** | partiel → verifie | [lib.univ-soukahras.dz](https://lib.univ-soukahras.dz/bib/42222) |
| OUV-0065 | Traité de diabétologie | 2e (2009) → **2e (2009)** | partiel → partiel | [unitheque.com](https://unitheque.com/UploadFile/DocumentPDF/T/R/9782257000286-traite-diabetologie.pdf) |
| OUV-0068 | Précis d'obstétrique | 6e (2001) → **6e (2001)** | partiel → verifie | [www.livres-medicaux.com](https://www.livres-medicaux.com/obstetrique/17993-precis-d-obstetrique-9782294008979.html) |
| OUV-0172 | Medical Physiology (Boron & Boulpaep) | 3e (2017) → **3e (2017)** | verifie → verifie | [evolve.elsevier.com](https://evolve.elsevier.com/cs/product/9781455743773?role=faculty) |
| OUV-0192 | Kuby Immunology | 8e (2018) → **8e (2018)** | verifie → verifie | [blackwells.co.uk](https://blackwells.co.uk/bookshop/product/Kuby-Immunology-by-Jenni-Punt-Sharon-A-Stranford-Patricia-P-Jones-Judith-A-Owen/9781464189784) |
| OUV-0222 | Rosai and Ackerman's Surgical Pathology | 11e (2018) → **11e (2018)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/rosai-and-ackermans-surgical-pathology-2-volume-set/goldblum/978-0-323-26339-9) |
| OUV-0228 | Henry's Clinical Diagnosis and Management by Laboratory Methods | 24e (2022) → **24e (2022)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/henrys-clinical-diagnosis-and-management-by-laboratory-methods/mcpherson/978-0-323-67320-4) |
| OUV-0229 | Dacie and Lewis Practical Haematology | 12e (2017) → **12e (2017)** | verifie → verifie | [www.us.elsevierhealth.com](https://www.us.elsevierhealth.com/dacie-and-lewis-practical-haematology-9780702066962.html) |
| OUV-0302 | Oxford Textbook of Medicine | 6e (2020) → **6e (2020)** | verifie → verifie | [Www.wikipedia.org](https://Www.wikipedia.org/wiki/Oxford_Textbook_of_Medicine) |
| OUV-0313 | Williams Hematology | 10e (2021) → **10e (2021)** | verifie → verifie | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/williams-hematology-10th-edition.html) |
| OUV-0323 | Feigenbaum's Echocardiography | 8e (2019) → **8e (2019)** | verifie → verifie | [shop.lww.com](https://shop.lww.com/Feigenbaum-s-Echocardiography/p/9781975244316) |
| OUV-0336 | Sherlock's Diseases of the Liver and Biliary System | 13e (2018) → **13e (2018)** | verifie → verifie | [lib.ecu.edu](https://lib.ecu.edu/catalog-preview/catalog/5101210) |
| OUV-0358 | Habif's Clinical Dermatology: A Color Guide to Diagnosis and Therapy | 7e (2021) → **7e (2021)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/habifs-clinical-dermatology/dinulos/978-0-323-61269-2) |
| OUV-0367 | Greenspan's Basic & Clinical Endocrinology | 10e (2018) → **10e (2018)** | verifie → verifie | [lib.ecu.edu](https://lib.ecu.edu/catalog-preview/catalog/5209159) |
| OUV-0375 | Abeloff's Clinical Oncology | 6e (2020) → **6e (2020)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/abeloffs-clinical-oncology/niederhuber/978-0-323-47674-4) |
| OUV-0411 | Textbook of Family Medicine (Rakel) | 9e (2016) → **9e (2016)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/textbook-of-family-medicine/rakel/978-0-323-23990-5) |
| OUV-0502 | Bailey & Love's Short Practice of Surgery | 28e (2022) → **28e (2022)** | verifie → verifie | [www.routledge.com](https://www.routledge.com/Bailey--Loves-Short-Practice-of-Surgery---28th-Edition/OConnell-McCaskie-Sayers/p/book/9780367548117) |
| OUV-0511 | Smith & Tanagho's General Urology | 19e (2020) → **19e (2020)** | verifie → verifie | [www.porchlightbooks.com](https://www.porchlightbooks.com/products/smith-and-tanaghos-general-urology-19th-edition-jack-w-mcaninch-9781259834332) |
| OUV-0551 | Pediatric Surgery (Coran) | 7e (2012) → **7e (2012)** | partiel → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/pediatric-surgery-2-volume-set/coran/978-0-323-07255-7) |
| OUV-0656 | Tintinalli's Emergency Medicine: A Comprehensive Study Guide | 9e (2020) → **9e (2020)** | verifie → verifie | [www.mheducation.com](https://www.mheducation.com/highered/mhp/product/tintinalli-s-emergency-medicine-comprehensive-study-guide-9th-edition.html) |
| OUV-0657 | Goldfrank's Toxicologic Emergencies | 11e (2019) → **11e (2019)** | verifie → verifie | [www.mhprofessional.com](https://www.mhprofessional.com/goldfrank-s-toxicologic-emergencies-eleventh-edition-9781259859618-usa) |
| OUV-0666 | Grainger & Allison's Diagnostic Radiology: A Textbook of Medical Imaging | 7e (2021) → **7e (2021)** | verifie → verifie | [shop.elsevier.com](https://shop.elsevier.com/books/grainger-and-allisons-diagnostic-radiology/adam/978-0-7020-7524-7) |

## 5. Éditions annoncées, non retenues comme édition courante

| id | édition retenue | édition annoncée | ISBN annoncé | statut de l'annonce |
|---|---|---|---|---|
| OUV-0073 | 45e (Dorosz 2026) (2025) | 46e (Dorosz 2027) (2026) | 9782224037314 | fiche libraire datée du 05/11/2026 (2160 p.) — parution effective à confirmer |
| OUV-0078 | 8e (2023) | 9e (2026) | 9782356403735 | annoncée chez un libraire (fiche « à paraître » / « nouveauté ») — parution effective à confirmer |
| OUV-0083 | 8e (2022) | 9e (2027) | 9782294790843 | annoncée par Elsevier (sortie prévue 22/09/2027) — non parue au 2026-11-19 |
| OUV-0086 | 4e (2024) | 5e (2026) | — | présentée par un libraire comme mise à jour avec les données 2026 ; ISBN et date de parution non relevés en session |
| OUV-0099 | 4e (2024) | 5e (2026) | 9782340115637 | listée « bientôt disponible » chez un libraire — parution à confirmer |
| OUV-0172 | 3e (2017) | 4e (date ?) | 9780323794862 | fiches Elsevier discordantes : parution 15/03/2025 (educate.elsevier.com) vs disponibilité prévue 01/12/2027 (autre fiche Elsevier) — non confirmée |
| OUV-0222 | 11e (2018) | 12e (2027) | 9780443278051 | annoncée par Elsevier pour le 01/05/2027 (coffret 2 volumes ; Goldblum, Lamps, McKenney) |
| OUV-0228 | 24e (2022) | 25e (2027) | 9780443287831 | annoncée par Elsevier pour le 01/03/2027 (éd. R. A. McPherson, M. R. Pincus) |
| OUV-0229 | 12e (2017) | 13e (date ?) | 9780443117886 | édition internationale annoncée chez un libraire (Churchill Livingstone, « vers octobre 2025 », non parue lors de la fiche) — non confirmée sur le site Elsevier |
| OUV-0301 | 27e (2023) | 28e (2027) | 9780443386848 | annoncée par Elsevier pour le 01/04/2027 — non parue au 2026-11-19 |
| OUV-0305 | 10e (2021) | 11e (2026) | 9780443287916 | annoncée par Elsevier (25/09/2026 sur shop.elsevier.com ; décembre 2026 sur une autre fiche) — parution non confirmée au 2026-11-19 |
| OUV-0309 | 65e (CMDT 2026) (2025) | CMDT 2027 (66e) (date ?) | 9781264824717 | fiche libraire (Blackwell's) sans date ni numéro d'édition ; ISBN relevé uniquement dans l'URL — à confirmer |
| OUV-0313 | 10e (2021) | 11e (2026) | 9781266134203 | page produit McGraw Hill « Williams Hematology 11e » ; date de parution libraire 20/11/2026 — non parue au 2026-11-19 |
| OUV-0323 | 8e (2019) | 9e (2026) | 9781975244316 | page LWW marquée « pre-publication » (parution 30/09/2026 ; libraires : octobre 2026) — parution effective non confirmée au 2026-11-19 |
| OUV-0336 | 13e (2018) | 14e (date ?) | 9781394360000 | Wiley ; dates discordantes chez les libraires (30/07/2026 ou 07/01/2027) — parution non confirmée |
| OUV-0340 | 7e (2023) | 8e (date ?) | 9780443285516 | pré-annonce Elsevier (« expected availability 12-01-2026 ») — non confirmée |
| OUV-0375 | 6e (2020) | 7e (2027) | 9780443380303 | pré-annonce Elsevier (disponibilité prévue 05/03/2027, © 2028) |
| OUV-0389 | 9e (2022) | 10e (2026) | 9780443287060 | pré-annonce Elsevier (evolve : « expected availability 06-01-2026 », ISBN eBook) — non confirmée |
| OUV-0400 | 8e (2021) | 9e (2026) | 9780443249099 | pré-annonce Elsevier (« expected availability 06-27-2026 ») — parution non confirmée au 2026-11-19 |
| OUV-0404 | 9e (2022) | 10e (2027) | 9780443407895 | annoncée par Elsevier pour le 01/05/2027 |
| OUV-0411 | 9e (2016) | 10e (2027) | 9780443127243 | annoncée par Elsevier pour le 30/07/2027 (« Rakel's Textbook of Family Medicine », éd. D. P. Rakel) |
| OUV-0525 | 8e (2022) | 9e (date ?) | 9780443399329 | fiche Elsevier (relié 9780443399329, eBook 9780443399336) sans date relevée — parution non confirmée |
| OUV-0565 | 12e (2020) | 13e (2027) | 9780443112850 | pré-annonce Elsevier (disponibilité prévue 19/03/2027) |
| OUV-0657 | 11e (2019) | 12e (date ?) | — | page produit McGraw Hill « Goldfrank's Toxicologic Emergencies, Twelfth Edition » existante ; date et ISBN non relevés en session |

À re-vérifier en priorité lors du prochain audit : Williams Hematology 11e (parution annoncée le 20/11/2026), Dorosz 2027 (46e), Feigenbaum 9e, Cecil Essentials 11e, Comprehensive Gynecology 9e, Nelson Essentials 10e, Sherlock 14e, Medical Physiology (Boron) 4e, Goldfrank's 12e, Pneumologie (CEP) 9e, Orthopédie (CFCOT) 5e, Cancérologie (CNEC) 5e.

## 6. Doublons fusionnés

Règle : même ouvrage, même édition ; l'entrée conservée est la plus ancienne (lots ANA, identifiants OUV-03xx/05xx/06xx) ; l'entrée retirée (lot ACQ-05, plage OUV-0950…0999) est archivée intégralement dans `doublons_retires.json` ; ses sources (inspection des paquets NCBI LitArch), ISBN et notes de licence sont reportés dans l'entrée conservée (`ids_fusionnes` + `notes`).

| id retiré (lot) | fusionné dans (lot) | motif |
|---|---|---|
| OUV-0950 (ACQ-05) | OUV-0390 (ANA-medicales) | même titre (DCP3 vol. 2, Reproductive, Maternal, Newborn, and Child Health), même édition (3e, 2016), mêmes ISBN, même NCBI Bookshelf NBK361907 |
| OUV-0951 (ACQ-05) | OUV-0353 (ANA-medicales) | même titre (DCP3 vol. 4, Mental, Neurological, and Substance Use Disorders), même édition (3e, 2016), mêmes ISBN, même NBK361945 |
| OUV-0952 (ACQ-05) | OUV-0505 (ANA-chirurgicales) | même titre (DCP3 vol. 1, Essential Surgery), même édition (3e, 2015), même NBK333500 |
| OUV-0953 (ACQ-05) | OUV-0380 (ANA-medicales) | même titre (DCP3 vol. 3, Cancer), même édition (3e, 2015), même NBK343628 |
| OUV-0954 (ACQ-05) | OUV-0699 (ANA-transversales) | même titre (DCP3 vol. 9, Improving Health and Reducing Poverty), même édition (3e, 2017), même NBK525289 |
| OUV-0957 (ACQ-05) | OUV-0310 (ANA-medicales) | même ressource (StatPearls, mise à jour continue), même NBK430685 |
| OUV-0958 (ACQ-05) | OUV-0369 (ANA-medicales) | même ressource (Endotext, mise à jour continue), même NBK278943 |

Aucun autre doublon évident (même titre normalisé + même édition, ou ISBN partagé) n'a été détecté après fusion. Homonymies non fusionnées car ouvrages distincts : OUV-0024/0077 « Cardiologie » (OPU, S. Ayoub vs référentiel CNEC), OUV-0025/0078, OUV-0027/0080, OUV-0043/0087, OUV-0551/0553 (Pediatric Surgery, Coran vs Puri).

## 7. Entrées restant non vérifiées (`partiel` : 54)

Essentiellement des ouvrages algériens de l'OPU et d'éditeurs nationaux (pas de site éditeur interrogeable ; vérification possible via les catalogues des BU algériennes — 15 d'entre eux ont été confirmés ainsi pendant l'audit) et quelques entrées françaises à éditeur/année discordants.

| id | titre | édition | année | éditeur |
|---|---|---|---|---|
| OUV-0001 | Atlas d'anatomie | — | 1994 | OPU (Office des publications universitai |
| OUV-0002 | Ostéologie, arthrologie, myologie, vaisseaux, nerfs : à l'usage des ét | — | 2004 | OPU (Office des publications universitai |
| OUV-0003 | Cytologie : troncs communs sciences de la nature, bio-médical | 2e | 1990 | Office des publications universitaires |
| OUV-0004 | Cytologie et physiologie cellulaire | — | — | OPU (Office des publications universitai |
| OUV-0005 | Embryologie : troncs communs bio-médical (S1), sciences de la nature ( | — | 1999 | OPU (Office des publications universitai |
| OUV-0006 | Embryologie expérimentale et moléculaire | — | — | OPU (Office des publications universitai |
| OUV-0007 | Lexique d'embryologie : français-arabe | — | 1992 | Office des publications universitaires |
| OUV-0008 | Biophysique : radiations, radiobiologie | — | 1987 | Office des publications universitaires |
| OUV-0009 | Éléments de neurobiologie | — | — | OPU (Office des publications universitai |
| OUV-0010 | Techniques de pharmacologie | — | 1989 | Office des publications universitaires |
| OUV-0011 | Antibiotiques | 2e (actualisée) | — | OPU (Office des publications universitai |
| OUV-0012 | Plantes médicinales d'Algérie | — | 1998 | Office des publications universitaires |
| OUV-0013 | Manuel de microbiologie clinique : bactériologie-virologie | — | — | OPU (Office des publications universitai |
| OUV-0014 | Microbiologie S1 clinique | 5e | — | OPU (Office des publications universitai |
| OUV-0015 | Manuel de microbiologie à l'usage des étudiants | — | — | OPU (Office des publications universitai |
| OUV-0016 | Cours de parasitologie. T. 1 : Protozooses | — | — | OPU (Office des publications universitai |
| OUV-0017 | Cours de parasitologie. 2 : Helminthiases | — | 1992 | OPU (Office des publications universitai |
| OUV-0018 | Guide pratique du laboratoire de parasitologie. 1 : Examens directs | — | 1989 | OPU (Office des publications universitai |
| OUV-0019 | Diagnostic immunologique de l'hydatidose | — | 1989 | Office des Publications Universitaires |
| OUV-0020 | Les lymphomes malins : classifications histologiques, extension et mét | — | 1988 | Office des publications universitaires |
| OUV-0021 | Précis de sémiologie | — | 2015 | OPU (Office des publications universitai |
| OUV-0022 | Sémiologie : carnet de l'externe en sémiologie (série) | — | 2014 | OPU (Office des publications universitai |
| OUV-0023 | Médecine interne | — | 2012 | OPU (Office des publications universitai |
| OUV-0024 | Cardiologie | — | 2012 | OPU (Office des publications universitai |
| OUV-0025 | Pneumologie | — | 2012 | OPU (Office des publications universitai |
| OUV-0026 | Appareil digestif | — | 2012 | OPU (Office des publications universitai |
| OUV-0030 | Abrégé d'hématologie | — | 1999 | OPU (Office des publications universitai |
| OUV-0031 | Les cancers colorectaux : notions fondamentales (1re partie) | — | — | OPU (Office des publications universitai |
| OUV-0033 | L'infection VIH-sida : l'expérience algérienne | — | 2004 | Éditions FOREM, Alger |
| OUV-0034 | Psychologie médicale | — | — | OPU (Office des publications universitai |
| OUV-0035 | La santé mentale : un guide à l'attention des étudiants en médecine | — | — | OPU (Office des publications universitai |
| OUV-0036 | Drogues et toxicomanie en Algérie | — | 2004 | Éditions FOREM, Alger |
| OUV-0042 | La nutrition chez l'enfant | — | 2004 | Éditions FOREM, Alger |
| OUV-0043 | Pédiatrie | — | 1998 | Éditions Dahlab, Alger |
| OUV-0044 | Audition et équilibre vestibulaire | — | — | OPU (Office des publications universitai |
| OUV-0045 | Pathologie médiastinale en Algérie : rapport du groupe de travail plur | — | 1989 | Office des publications universitaires |
| OUV-0046 | Guide pratique en orthodontie | — | 1988 | Office des publications universitaires |
| OUV-0047 | Les dysmorphoses maxillo-faciales | — | 1988 | Office des publications universitaires |
| OUV-0050 | Compléments en techniques épidémiologiques de base | — | 2003 | OPU (Office des publications universitai |
| OUV-0051 | Géographie et santé en Algérie | — | 1992 | Office des publications universitaires |
| OUV-0052 | Nutrition appliquée à la santé publique | — | — | OPU (Office des publications universitai |
| OUV-0054 | La santé publique : une profession de foi | — | 2014 | ENAG Éditions, Alger |
| OUV-0055 | La silicose en Algérie : travail collectif des sociétés algériennes de | — | 1988 | Office des publications universitaires |
| OUV-0056 | L'éthique biomédicale | — | 2000 | Dar El Gharb, Oran |
| OUV-0059 | Anatomie topographique, descriptive et fonctionnelle | — | 1969 | Lyon, SIMEP |
| OUV-0060 | Embryologie humaine : de la molécule à la clinique | 4e | — | Elsevier Masson |
| OUV-0065 | Traité de diabétologie | 2e | 2009 | Flammarion médecine-sciences |
| OUV-0070 | Traité de médecine | 5e | 2018 | Tam éditions / TDM éditions [à confirmer |
| OUV-0096 | Santé publique | 5e | 2022 | Elsevier Masson |
| OUV-0106 | Chirurgie générale, viscérale et digestive (référentiel du Collège — R | 3e | — | Med-Line [éditeur déduit du préfixe ISBN |
| OUV-0111 | Précis de physiologie médicale (traduction française de Guyton & Hall) | 2e éd. française | 2003 | Piccin (Padoue) |
| OUV-0569 | Dictionnaire francophone des termes d'odontologie conservatrice : endo | 2e | 2010 | Éditions Espace ID |
| OUV-0354 | Fitzpatrick's Dermatology | 10e | — | McGraw-Hill Education |
| OUV-0402 | Williams Obstetrics | 27e | — | McGraw Hill |

## 8. Limites et suites

- Les dates de parution diffèrent souvent selon les fiches (éditeur, libraires, copyright) : l'année retenue est celle de la parution indiquée par l'éditeur ; les divergences sont détaillées dans `notes`.
- Les listes complètes d'auteurs/éditeurs scientifiques n'ont pas toujours été relevées : les mentions `[À VÉRIFIER]` sont conservées.
- Les ouvrages « vérifiés » par le premier catalogueur via le NLM Catalog et non re-contrôlés ici peuvent avoir une édition plus récente (ex. Fuster & Hurst, Moore's Clinically Oriented Anatomy, Tintinalli confirmé, Hunter's Tropical Medicine, Avery's Neonatology, Brocklehurst, etc.) : à traiter dans un audit ultérieur (quota de recherche épuisé).
- Le catalogue fusionné `catalogue_ouvrages.json` n'a pas été régénéré par AUD-04 (pas d'exécution d'`indexer.py` pour ne pas interférer avec les autres agents) : relancer `python3 00_SYSTEME/scripts/indexer.py` pour propager les lots audités.
- Entrées fusionnées retirées du lot ACQ-05 : l'agent ACQ-05 doit en être informé (les identifiants OUV-0950/0951/0952/0953/0954/0957/0958 ne doivent pas être réattribués).

