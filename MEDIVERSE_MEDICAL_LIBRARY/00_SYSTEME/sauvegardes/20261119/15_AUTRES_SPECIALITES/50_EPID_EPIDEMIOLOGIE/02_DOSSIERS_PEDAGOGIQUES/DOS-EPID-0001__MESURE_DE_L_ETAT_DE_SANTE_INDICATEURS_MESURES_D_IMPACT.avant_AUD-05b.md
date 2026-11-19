---
id: DOS-EPID-0001
titre: "Mesure de l'état de santé de la population : indicateurs de santé et mesures d'impact"
specialite: EPID
sous_specialite: "Épidémiologie descriptive — indicateurs de santé, mesures d'association et d'impact"
items_residanat: [RES-MED-128]
niveaux: [etudiant, generaliste, resident, residanat, dems]
langue: fr
version: "1.1"
date_creation: 2026-11-19
date_revision: 2026-11-19
auteur: "Agent DOS-15 (IA) — dossier pédagogique original"
statut: audite_corrections_requises
audit:
  - date: 2026-11-19
    auditeur: "AUD-01 (IA)"
    verdict: audite_corrections_requises
    corrections: 4
    rapport: 00_SYSTEME/agents/AUD-01/rapports/DOS-EPID-0001.md
    remarque: "Tous les calculs refaits par script (exacts) ; définitions conformes. Restent : chiffres ONS 2023 et STEPS 2016-2017 non confrontés aux publications primaires (hôtes ons.dz, ambassade-algerie.ch, cdn.who.int et afro.who.int inaccessibles)."
  - date: 2026-11-19
    auditeur: "AUD-04 (IA)"
    verdict: audite_corrections_requises
    corrections: 8
    rapport: 00_SYSTEME/agents/AUD-01/rapports/DOS-EPID-0001.md
    remarque: "Références vérifiées par PubMed (eutils) : S6, S8, S13, S14, S15 ; Gordis 6e éd. confirmée (WorldCat). S11, S12, S16, S17 non revérifiées."
sources:
  - id: S1
    reference: "Loi n° 18-11 du 2 juillet 2018 relative à la santé. JORADP n° 46 du 29 juillet 2018 (art. 11, 36, 38-39, 47, 204, 293-294, 319-323, 338)."
    organisme: "République algérienne (JORADP)"
    annee: 2018
    type: texte_officiel
    doi: ""
    url: "https://www.joradp.dz/FTP/JO-FRANCAIS/2018/F2018046.pdf"
    verifiee: true
    remarque: "Document acquis DOC-00074, lu (pdftotext) pendant la session."
  - id: S2
    reference: "Décret exécutif n° 22-178 du 28 avril 2022 relatif au certificat médical de décès. JORADP n° 32 du 14 mai 2022."
    organisme: "Ministère de la santé (Algérie)"
    annee: 2022
    type: texte_officiel
    doi: ""
    url: "https://www.joradp.dz/FTP/JO-FRANCAIS/2022/F2022032.pdf"
    verifiee: true
    remarque: "Document acquis DOC-00077, lu pendant la session."
  - id: S3
    reference: "Décret exécutif n° 22-250 du 30 juin 2022 fixant la liste des maladies transmissibles soumises à déclaration obligatoire. JORADP n° 47 du 11 juillet 2022."
    organisme: "Ministère de la santé (Algérie)"
    annee: 2022
    type: texte_officiel
    doi: ""
    url: "https://www.joradp.dz/FTP/JO-FRANCAIS/2022/F2022047.pdf"
    verifiee: true
    remarque: "Document acquis DOC-00072, lu pendant la session."
  - id: S4
    reference: "Office national des statistiques (ONS). Démographie algérienne 2020-2023 (publication n° 1030). Alger : ONS ; 2024."
    organisme: ONS
    annee: 2024
    type: site_institutionnel
    doi: ""
    url: ""
    verifiee: true
    remarque: "Existence confirmée par recherche web (2026-11-19). Publication primaire non consultée, ni par DOS-15 ni par l'audit AUD-01 (ons.dz et le miroir ambassade-algerie.ch inaccessibles) : les chiffres cités proviennent de reprises de presse (TSA, Algérie-Eco, Radio Algérie, juillet 2024) [À VÉRIFIER — source primaire non consultée]."
  - id: S5
    reference: "Ministère de la Santé, de la Population et de la Réforme Hospitalière / OMS. Enquête nationale sur la mesure du poids des facteurs de risque des maladies non transmissibles selon l'approche STEPwise de l'OMS — Algérie 2016-2017 (fascicule des principaux résultats, 2018)."
    organisme: "MSPRH / OMS"
    annee: 2018
    type: site_institutionnel
    doi: ""
    url: "https://www.who.int/publications/m/item/2016-2017-steps-fact-sheet-algeria"
    verifiee: true
    remarque: "Existence confirmée : fiche OMS « 2016-2017 STEPS Fact Sheet Algeria » (page who.int consultée par AUD-01) ; le PDF (cdn.who.int) et le fascicule national (afro.who.int) n'ont pas pu être ouverts. Les chiffres (diabète 14,4 %, hyperglycémie modérée 8,2 %, tabac fumé 16,5 %, 7 450 personnes de 18-69 ans) proviennent d'un communiqué OMS Afrique repris par recherche web [À VÉRIFIER — source primaire non consultée]."
  - id: S6
    reference: "Moussouni A, Sidi-Yakhlef A, Hamdaoui H, Aouar A, Belkhatir D. Prevalence and risk factors of prehypertension and hypertension in Algeria. BMC Public Health. 2022;22(1):1571."
    organisme: "BMC Public Health"
    annee: 2022
    type: article
    doi: "10.1186/s12889-022-13942-y"
    url: ""
    verifiee: true
    remarque: "PMID 35982441 ; résumé relu (PubMed, audit AUD-04) : analyse secondaire de la base STEPS 2016-2017 ; pré-HTA 36,2 % (IC 95 % 35,2-37,5), HTA 31,6 % (30,5-32,7). Effectif de 6 989 non relu dans le résumé [À VÉRIFIER — texte intégral]."
  - id: S7
    reference: "Ministère de la Santé, de la Population et de la Réforme Hospitalière / UNICEF. Enquête par grappes à indicateurs multiples (MICS6) 2019 — Rapport final des résultats. Alger, décembre 2020."
    organisme: "MSPRH / UNICEF"
    annee: 2020
    type: site_institutionnel
    doi: ""
    url: "https://www.unicef.org/algeria/rapports/suivi-de-la-situation-des-enfants-et-des-femmes-en-alg%C3%A9rie-0"
    verifiee: true
    remarque: "Existence confirmée (UNICEF Algérie ; microdonnées Banque mondiale DZA_2018_MICS_v01_M). Aucun chiffre MICS n'est repris dans ce dossier."
  - id: S8
    reference: "GBD 2021 Diseases and Injuries Collaborators. Global incidence, prevalence, years lived with disability (YLDs), disability-adjusted life-years (DALYs), and healthy life expectancy (HALE) for 371 diseases and injuries in 204 countries and territories and 811 subnational locations, 1990-2021. Lancet. 2024;403(10440):2133-2161."
    organisme: "IHME / The Lancet"
    annee: 2024
    type: article
    doi: "10.1016/S0140-6736(24)00757-8"
    url: ""
    verifiee: true
    remarque: "PMID 38642570 ; résumé relu (audit) : DALY 2,63 → 2,88 milliards (2010-2021) ; COVID-19 1re cause de DALY en 2021 ; HALE 61,3 → 62,2 ans, baisse de 2,2 % entre 2019 et 2021."
  - id: S9
    reference: "Lash TL, VanderWeele TJ, Haneuse S, Rothman KJ. Modern Epidemiology. 4th ed. Philadelphia: Wolters Kluwer; 2021."
    organisme: "Wolters Kluwer"
    annee: 2021
    type: ouvrage
    doi: ""
    url: ""
    verifiee: true
    remarque: "Ouvrage protégé : cité comme référence de concepts, aucun extrait reproduit."
  - id: S10
    reference: "Celentano DD, Szklo M. Gordis Epidemiology. 6th ed. Philadelphia: Elsevier; 2019."
    organisme: Elsevier
    annee: 2019
    type: ouvrage
    doi: ""
    url: ""
    verifiee: true
    remarque: "6e édition confirmée (WorldCat OCLC 1079273274, Elsevier 2019 ; mise en vente fin 2018). Aucun extrait reproduit."
  - id: S11
    reference: "Porta M (ed.). A Dictionary of Epidemiology. 6th ed. Oxford: Oxford University Press; 2014."
    organisme: "IEA / Oxford University Press"
    annee: 2014
    type: ouvrage
    doi: ""
    url: ""
    verifiee: false
  - id: S12
    reference: "World Health Organization. 2018 Global Reference List of 100 Core Health Indicators (plus health-related SDGs). Geneva: WHO; 2018."
    organisme: OMS
    annee: 2018
    type: recommandation
    doi: ""
    url: ""
    verifiee: false
  - id: S13
    reference: "Laupacis A, Sackett DL, Roberts RS. An assessment of clinically useful measures of the consequences of treatment. N Engl J Med. 1988;318(26):1728-1733."
    organisme: NEJM
    annee: 1988
    type: article
    doi: "10.1056/NEJM198806303182605"
    url: ""
    verifiee: true
    remarque: "Article princeps du NNT ; PMID 3374545 (vérifié, audit AUD-04)."
  - id: S14
    reference: "Levin ML. The occurrence of lung cancer in man. Acta Unio Int Contra Cancrum. 1953;9(3):531-541."
    organisme: "UICC"
    annee: 1953
    type: article
    doi: ""
    url: ""
    verifiee: true
    remarque: "Origine de la formule de la fraction attribuable dans la population ; PMID 13124110 (vérifié, audit AUD-04)."
  - id: S15
    reference: "Murray CJL. Quantifying the burden of disease: the technical basis for disability-adjusted life years. Bull World Health Organ. 1994;72(3):429-445."
    organisme: OMS
    annee: 1994
    type: article
    doi: ""
    url: ""
    verifiee: true
    remarque: "PMID 8062401 (vérifié, audit AUD-04)."
  - id: S16
    reference: "Organisation mondiale de la santé. Classification statistique internationale des maladies et des problèmes de santé connexes, 10e révision (CIM-10), volume 2 (définitions de la mortalité maternelle et périnatale) ; CIM-11 en vigueur depuis le 1er janvier 2022."
    organisme: OMS
    annee: 2019
    type: recommandation
    doi: ""
    url: ""
    verifiee: false
  - id: S17
    reference: "Assemblée générale des Nations unies. Transformer notre monde : le Programme de développement durable à l'horizon 2030 (A/RES/70/1), 2015 — objectif 3 (cibles 3.1 et 3.2)."
    organisme: ONU
    annee: 2015
    type: texte_officiel
    doi: ""
    url: ""
    verifiee: false
  - id: S18
    reference: "Arrêté du 3 juillet 2018 fixant le calendrier de vaccination obligatoire contre certaines maladies transmissibles (JORADP n° 49/2018), complété par l'arrêté du 28 avril 2026 (JORADP n° 36/2026)."
    organisme: "Ministère de la santé (Algérie)"
    annee: 2018
    type: texte_officiel
    doi: ""
    url: ""
    verifiee: true
    remarque: "Documents acquis DOC-00070 et DOC-00071 (métadonnées du registre) ; cités uniquement comme base du dénominateur de la couverture vaccinale."
mots_cles: [indicateurs de santé, prévalence, incidence, densité d'incidence, mortalité infantile, mortalité maternelle, standardisation, SMR, espérance de vie, DALY, QALY, risque relatif, risque attribuable, fraction attribuable, NNT, efficacité vaccinale, Algérie, ONS, STEPS]
---

# Mesure de l'état de santé de la population : indicateurs de santé et mesures d'impact

> **Dossier pédagogique original Mediverse** — rédigé à partir de plusieurs sources citées ; ne reproduit aucun ouvrage.
> Statut : **audité par l'IA (AUD-01/AUD-04, 2026-11-19), corrections requises** — calculs et définitions vérifiés ; chiffres algériens de source secondaire à confronter aux publications ONS et STEPS ; relecture par un enseignant qualifié nécessaire. Tous les exemples numériques sont **fictifs** (sauf mention explicite d'une source) et ont été recalculés deux fois ; les données algériennes sont citées avec leur source et leurs limites.

**Item du programme couvert** : RES-MED-128 — « Mesure de l'état de santé de la population : indicateurs de santé - mesures d'impact » (module Épidémiologie et médecine préventive, programme du concours de résidanat, DOC-00001).

**Objectifs pédagogiques** — à l'issue de ce dossier, le lecteur doit être capable de :
1. **Distinguer** ratio, proportion, taux et indice, et identifier pour chaque indicateur son numérateur, son dénominateur et sa période de référence.
2. **Calculer et interpréter** une prévalence, une incidence cumulée, une densité d'incidence (personnes-temps) et un taux d'attaque ; **relier** prévalence, incidence et durée.
3. **Calculer** les principaux indicateurs de mortalité (taux brut, spécifique, létalité, mortalité proportionnelle, mortalité infantile et ses composantes, mortinatalité, mortalité périnatale, ratio de mortalité maternelle, années potentielles de vie perdues).
4. **Réaliser** une standardisation directe et indirecte et **expliquer** pourquoi un taux brut peut être trompeur.
5. **Définir** les indicateurs démographiques (natalité, fécondité, accroissement naturel, espérance de vie) et **critiquer** les données algériennes disponibles (ONS, STEPS, MICS).
6. **Expliquer** les indicateurs composites (espérance de vie sans incapacité, HALE, DALY/AVCI, QALY/AVAQ) et leurs usages respectifs.
7. **Calculer** les mesures d'association (RR, OR) et d'impact (différence de risque, fraction étiologique chez les exposés, risque et fraction attribuables dans la population, fraction prévenue, efficacité vaccinale, RRR, RAR, NNT, NNH).
8. **Choisir** l'indicateur adapté à une question de santé publique et **identifier** les sources de données réglementaires algériennes (état civil, certificat de décès, MDO, registres, système national d'information sanitaire).

---

## 1. Définitions et généralités

### 1.1 Qu'est-ce que « mesurer l'état de santé » ?

La santé d'une population ne se mesure pas directement : on l'approche par des **indicateurs**, c'est-à-dire des variables quantifiables, définies de façon standardisée, qui résument une dimension de la santé (mortalité, morbidité, incapacité, déterminants, recours aux soins, ressources) et permettent des comparaisons dans le temps et dans l'espace. La définition de la santé adoptée par la Constitution de l'OMS (1946) — un état de complet bien-être physique, mental et social, et pas seulement l'absence de maladie — explique qu'aucun indicateur isolé ne suffise ; on raisonne toujours sur un **tableau de bord**. La loi algérienne n° 18-11 reprend cette approche globale en liant la protection de la santé au « bien-être physique, mental et social » de la personne (art. 2) et en créant un **observatoire national de la santé** chargé d'élaborer un rapport annuel sur l'état de santé de la population (art. 11) [S1].

Les indicateurs servent à :
- **décrire** la situation sanitaire (diagnostic communautaire) ;
- **hiérarchiser** les problèmes et fixer des priorités (programmation sanitaire) ;
- **surveiller** les tendances et détecter des phénomènes anormaux (épidémies) ;
- **évaluer** l'efficacité d'un programme ou d'une intervention ;
- **comparer** des régions, des pays ou des périodes ;
- **générer des hypothèses** étiologiques (épidémiologie descriptive → analytique).

### 1.2 Qualités d'un bon indicateur

| Qualité | Définition opérationnelle | Exemple de défaut |
|---|---|---|
| Validité | Mesure réellement ce qu'il prétend mesurer | « Nombre de consultations » comme indicateur de morbidité (reflète aussi l'offre) |
| Fiabilité (reproductibilité) | Même résultat si la mesure est répétée dans les mêmes conditions | Causes de décès codées différemment selon les médecins |
| Sensibilité | Varie quand le phénomène varie | Taux brut de mortalité peu sensible à une amélioration de la prise en charge néonatale |
| Spécificité | Ne varie que si le phénomène étudié varie | Mortalité infantile influencée par l'exhaustivité de l'état civil |
| Disponibilité / faisabilité | Données recueillies en routine, à coût acceptable | Incidence de l'insuffisance cardiaque sans registre |
| Comparabilité | Définitions standardisées (OMS, CIM) | Seuil de mortinaissance variable selon les pays |
| Opportunité | Disponible à temps pour décider | Données de recensement décennales |
| Acceptabilité / éthique | Recueil compatible avec la confidentialité | Données nominatives non protégées |

Le décret n° 22-178 illustre la recherche de fiabilité et de confidentialité : le certificat médical de décès comporte une **partie supérieure nominative** (état civil) et une **partie inférieure anonyme** réservée aux autorités sanitaires, où le médecin indique la cause directe et les états morbides antérieurs, puis la ferme avant transmission à la direction de wilaya chargée de la santé (art. 5-6) [S2].

### 1.3 Ratio, proportion, taux, indice : le vocabulaire de base

| Mesure | Forme | Bornes | Exemple |
|---|---|---|---|
| **Ratio** | a / b, a n'est pas inclus dans b | 0 à +∞ | Sex-ratio à la naissance (garçons/filles) |
| **Proportion** | a / (a + b), le numérateur fait partie du dénominateur | 0 à 1 (ou %) | Prévalence ; létalité ; mortalité proportionnelle |
| **Taux (au sens strict)** | Nombre d'événements / somme des temps d'exposition au risque | 0 à +∞, dimension = temps⁻¹ | Densité d'incidence (cas pour 1 000 personnes-années) |
| **Taux (au sens usuel)** | Événements d'une période / population moyenne de la période | Exprimé pour 1 000, 100 000… | Taux brut de mortalité annuel |
| **Indice** | Ratio ou combinaison de mesures, souvent × 100 | variable | Indice de vieillissement, indice comparatif de mortalité |

> **Piège terminologique** : le « taux de mortalité infantile » est en réalité un **quotient** (décès < 1 an rapportés aux naissances vivantes, qui ne sont pas toutes des personnes ayant vécu un an), et le « ratio de mortalité maternelle » n'est pas un taux car son dénominateur (naissances vivantes) n'est pas la population à risque (grossesses). L'usage consacre ces appellations ; l'essentiel est de connaître exactement numérateur et dénominateur [S9, S11].

Trois questions à se poser pour **tout** indicateur :
1. **Qui** est au numérateur (définition du cas, de l'événement) ?
2. **Qui** est au dénominateur (population totale, population à risque, naissances vivantes, personnes-temps) ?
3. **Quand** (instant, période, année civile) et **où** (zone géographique) ?

---

## 2. Historique (repères)

- **XVIIe siècle** : John Graunt analyse les registres de décès de Londres (*Bills of Mortality*) et ébauche les premières tables de mortalité — naissance de la statistique sanitaire.
- **XIXe siècle** : William Farr organise l'enregistrement des causes de décès en Angleterre ; John Snow utilise des taux de décès par compagnie de distribution d'eau pour mettre en évidence la transmission hydrique du choléra (1854) — premier usage analytique d'indicateurs de mortalité.
- **1893-1900** : classification internationale des causes de décès (Bertillon), ancêtre de la **CIM** ; la CIM-11 est entrée en vigueur le 1er janvier 2022 [S16].
- **1953** : Levin propose la formule de la **fraction attribuable dans la population** à propos du cancer du poumon et du tabac [S14].
- **1971** : Sullivan propose une méthode de calcul de l'espérance de vie sans incapacité.
- **1988** : Laupacis, Sackett et Roberts introduisent le **nombre de sujets à traiter (NNT)** [S13].
- **1993-1994** : Banque mondiale et OMS lancent l'étude de la charge mondiale de morbidité (Global Burden of Disease) et l'indicateur **DALY** [S15] ; les éditions successives (GBD 2021 publiée en 2024) couvrent 371 maladies et traumatismes dans 204 pays [S8].
- **2015** : les Objectifs de développement durable (ODD) fixent des cibles chiffrées de mortalité maternelle et infanto-juvénile pour 2030 [S17].

---

## 3. Sources des données sanitaires (monde et Algérie)

### 3.1 Typologie des sources

| Source | Données produites | Forces | Limites |
|---|---|---|---|
| **Recensement de la population** | Effectifs par âge, sexe, lieu (dénominateurs) | Exhaustif | Périodicité longue (≈ 10 ans) ; projections entre deux recensements |
| **État civil** | Naissances, décès, mariages | Continu, exhaustif si l'enregistrement est bon | Sous-enregistrement possible (décès néonatals précoces, mort-nés) |
| **Certificats médicaux de décès** | Causes médicales de décès | Base de la mortalité par cause | Qualité du remplissage, causes mal définies, codage CIM |
| **Déclaration obligatoire (MDO)** | Cas de maladies transmissibles | Alerte et tendances | Sous-déclaration fréquente |
| **Registres de morbidité** | Incidence (cancers, malformations…) | Exhaustivité sur un territoire | Coût, couverture partielle |
| **Enquêtes en population** | Prévalences, facteurs de risque, couverture des interventions | Représentativité si échantillonnage correct | Ponctuelles, biais de déclaration |
| **Données hospitalières et d'activité** | Admissions, journées, actes | Disponibles en routine | Reflètent le recours aux soins, pas la morbidité réelle |
| **Systèmes de surveillance sentinelle** | Tendances (grippe, IST…) | Réactifs | Non représentatifs de toute la population |

### 3.2 Cadre réglementaire algérien des données sanitaires [S1, S2, S3]

- **Réseaux de surveillance et d'alerte** pour les maladies transmissibles et non transmissibles, et **registres** de surveillance des maladies non transmissibles (loi 18-11, art. 36 et 47 ; la liste des maladies faisant l'objet d'un registre est fixée par le ministre).
- **Déclaration obligatoire** : tout praticien médical déclare sans délai tout cas **suspect ou confirmé** d'une maladie de la liste (art. 38-39) ; la liste actuelle est fixée par le décret exécutif n° 22-250 (catégorie 1 : surveillance nationale ; catégorie 2 : surveillance internationale). Fait notable pour la mesure de la qualité des soins : cette liste inclut les **infections du site opératoire**, les **pneumopathies acquises sous ventilation mécanique** et les **infections à bactéries multirésistantes** [S3].
- **Obligation des établissements** de communiquer les informations nécessaires aux enquêtes épidémiologiques et aux statistiques sanitaires (art. 293) et de déclarer naissances et décès à la commune (art. 294).
- **Certificat médical de décès** (art. 204 de la loi ; décret 22-178) : modèle unique, partie médicale anonyme, possibilité de certificat numérique interconnecté au registre national électronique de l'état civil (art. 8-9 du décret) [S2].
- **Système national d'information sanitaire** intégrant toutes les données sanitaires, auquel les structures publiques et privées ont l'obligation d'adhérer (art. 319-323) ; **comptes nationaux de la santé** publiés annuellement (art. 338) [S1].
- **Enquêtes nationales** : enquête STEPS 2016-2017 sur les facteurs de risque des maladies non transmissibles (18-69 ans) [S5] ; enquête MICS6 2019 sur la situation des enfants et des femmes [S7] ; publications démographiques annuelles de l'ONS [S4].
- Le nom et le rôle exacts des autres producteurs de données (Institut national de santé publique, observatoires régionaux) relèvent de textes d'organisation non consultés ici : voir le dossier DOS-SPUB-0001 et les mentions `[À VÉRIFIER]`.

---

## 4. Mesures de morbidité

### 4.1 Prévalence

**Définition** : proportion de personnes atteintes d'une maladie (ou porteuses d'une caractéristique) dans une population à un moment donné.

- **Prévalence ponctuelle** = nombre de cas existants à l'instant t / effectif de la population à l'instant t.
- **Prévalence de période** = nombre de personnes ayant été malades à un moment quelconque de la période (cas présents au début + nouveaux cas) / population moyenne de la période.

C'est une **proportion** (sans unité, entre 0 et 1). Elle mesure le **fardeau** d'une maladie à un instant et sert à planifier les ressources (nombre de patients dialysés, de diabétiques à suivre). Elle dépend à la fois de la fréquence d'apparition (incidence) et de la **durée** de la maladie (guérison, décès, émigration). Un traitement qui prolonge la survie sans guérir **augmente** la prévalence : une prévalence qui monte n'est donc pas forcément une mauvaise nouvelle.

### 4.2 Incidence cumulée (risque)

**Définition** : proportion de sujets **indemnes et à risque** au début d'une période qui développent la maladie pendant cette période.

IC = nouveaux cas pendant la période / nombre de sujets à risque au début de la période.

- C'est une **probabilité** (risque individuel moyen) ; elle n'a de sens qu'accompagnée de la durée (risque à 1 an, à 5 ans).
- Elle suppose une population **fermée** (pas d'entrées, peu de perdus de vue) ; sinon, on utilise la densité d'incidence.
- Les personnes déjà malades ou non susceptibles (immunisées, hystérectomisées pour le cancer du col…) sont exclues du dénominateur.

**Taux d'attaque** : incidence cumulée en situation d'épidémie, sur une durée courte (TIAC, rougeole). **Taux d'attaque secondaire** : nombre de cas secondaires parmi les contacts réceptifs d'un cas index / nombre de contacts réceptifs ; il mesure la contagiosité.

### 4.3 Densité d'incidence (taux d'incidence)

**Définition** : nombre de nouveaux cas rapporté à la **somme des temps de suivi à risque** des sujets (personnes-temps).

DI = nouveaux cas / Σ personnes-temps à risque — unité : cas par personne-année (ou pour 1 000 personnes-années).

Chaque sujet contribue au dénominateur **jusqu'à** la survenue de la maladie, sa sortie d'étude (perdu de vue, décès d'une autre cause) ou la fin de l'étude. Elle convient aux **populations dynamiques** et aux suivis de durées inégales.

**Exemple 1 (fictif) — calcul des personnes-temps**

| Sujet | Durée de suivi (années) | Issue |
|---|---|---|
| 1 | 5,0 | indemne en fin d'étude |
| 2 | 5,0 | indemne en fin d'étude |
| 3 | 3,0 | malade à 3 ans |
| 4 | 4,0 | perdu de vue à 4 ans |
| 5 | 1,5 | malade à 1,5 an |
| 6 | 5,0 | indemne en fin d'étude |
| **Total** | **23,5 personnes-années** | **2 cas** |

DI = 2 / 23,5 = 0,0851 cas par personne-année, soit **85,1 pour 1 000 personnes-années**. Si l'on avait calculé une incidence cumulée « naïve » (2/6 = 33 % en 5 ans), on aurait ignoré que les sujets 3, 4 et 5 n'ont pas été suivis 5 ans.

### 4.4 Relations entre prévalence, incidence et durée

En situation **stationnaire** (incidence et durée stables, population stable) :

P / (1 − P) = DI × D̄ (D̄ = durée moyenne de la maladie) ; si la prévalence est faible (< 10 %), **P ≈ DI × D̄**.

**Exemple 2 (fictif)** : DI = 2 pour 1 000 personnes-années et durée moyenne = 10 ans → P/(1 − P) = 0,002 × 10 = 0,02 → P = 0,02/1,02 = **0,0196 (≈ 2 %)**.

Par ailleurs, pour une période courte et un risque faible, IC ≈ DI × Δt ; de façon plus exacte, si le taux est constant, IC = 1 − e^(−DI × Δt).

**Exemple 3 (fictif) — prévalence et incidence dans une commune**
Une commune compte 20 000 adultes au 1er janvier, dont 1 000 diabétiques connus. Au cours de l'année, 190 nouveaux diabètes sont diagnostiqués ; 30 diabétiques décèdent et 10 quittent la commune (population totale supposée constante).
- Prévalence au 1er janvier = 1 000 / 20 000 = **5,0 %**.
- Population à risque au 1er janvier = 20 000 − 1 000 = 19 000 ; incidence cumulée annuelle = 190 / 19 000 = **1,0 %**.
- Cas présents au 31 décembre = 1 000 + 190 − 30 − 10 = 1 150 ; prévalence au 31 décembre = 1 150 / 20 000 = **5,75 %**.
- Prévalence de période (année) = (1 000 + 190) / 20 000 = **5,95 %**.

### 4.5 Comparaison prévalence / incidence

| | Prévalence | Incidence cumulée | Densité d'incidence |
|---|---|---|---|
| Numérateur | Cas existants (anciens + nouveaux) | Nouveaux cas | Nouveaux cas |
| Dénominateur | Population totale | Population à risque au début | Personnes-temps à risque |
| Nature | Proportion | Proportion (probabilité) | Taux (temps⁻¹) |
| Type d'enquête | Transversale | Cohorte fermée | Cohorte ouverte / dynamique |
| Usage | Fardeau, planification | Risque individuel, pronostic | Vitesse d'apparition, étiologie |
| Influencée par la durée | Oui | Non | Non |

---

## 5. Mesures de mortalité

### 5.1 Indicateurs généraux

| Indicateur | Numérateur | Dénominateur | Multiplicateur usuel |
|---|---|---|---|
| Taux brut de mortalité (TBM) | Décès de l'année (toutes causes, tous âges) | Population moyenne (au 1er juillet) | ‰ |
| Taux spécifique (âge, sexe, cause, lieu) | Décès du sous-groupe | Population moyenne du sous-groupe | ‰ ou pour 100 000 |
| Létalité | Décès dus à la maladie (pendant une période ou un suivi défini) | Nombre de cas de cette maladie | % |
| Mortalité proportionnelle | Décès d'une cause | Ensemble des décès | % |
| Années potentielles de vie perdues (APVP) | Σ (âge limite − âge au décès) pour les décès avant l'âge limite | — (ou rapporté à la population) | années |

**La létalité n'est pas un taux de mortalité** : c'est une proportion de malades qui meurent, indicateur de **gravité** (ou de qualité de prise en charge), alors que la mortalité spécifique rapporte les décès à toute la population et mesure l'**impact** de la maladie sur la population.

**Exemple 4 (fictif)** : épidémie de méningite à méningocoque dans une zone de 500 000 habitants : 250 cas, 20 décès.
- Taux d'attaque (incidence) = 250 / 500 000 = **50 pour 100 000**.
- Mortalité spécifique = 20 / 500 000 = **4 pour 100 000**.
- Létalité = 20 / 250 = **8 %**.

**Mortalité proportionnelle** : si une wilaya enregistre 5 400 décès dont 1 620 de cause cardiovasculaire, la mortalité proportionnelle cardiovasculaire est 1 620 / 5 400 = **30 %**. Ce chiffre ne dit rien du **risque** de mourir d'une cause cardiovasculaire (le dénominateur n'est pas la population) : une mortalité proportionnelle élevée peut simplement refléter la faible mortalité par d'autres causes.

**APVP** : avec un âge limite de 75 ans, trois décès à 25, 50 et 70 ans représentent (75 − 25) + (75 − 50) + (75 − 70) = 50 + 25 + 5 = **80 APVP**. Cet indicateur donne plus de poids aux décès **prématurés** (accidents de la route, suicides, mortalité maternelle) et sert à hiérarchiser les priorités de prévention ; l'âge limite (65, 70, 75 ans) est conventionnel et doit être précisé.

### 5.2 Mortalité de l'enfant et mortalité périnatale

Définitions (OMS, CIM) [S16] :
- **Mortalité infantile** : décès d'enfants nés vivants avant l'âge d'un an.
- **Néonatale** : de 0 à 27 jours révolus ; **néonatale précoce** : 0 à 6 jours ; **néonatale tardive** : 7 à 27 jours.
- **Post-néonatale** : de 28 jours à moins d'un an.
- **Mortinatalité** : enfants mort-nés ; les seuils d'âge gestationnel ou de poids diffèrent selon les usages (la CIM-10 fait débuter la période périnatale à 22 semaines révolues ou 500 g ; l'OMS utilise un seuil plus élevé — 28 semaines ou 1 000 g — pour les comparaisons internationales). Le seuil appliqué en Algérie doit être précisé dans chaque source `[À VÉRIFIER]`.
- **Mortalité périnatale** : mort-nés + décès néonatals précoces.
- **Mortalité des moins de 5 ans** : probabilité de décéder entre la naissance et le 5e anniversaire, exprimée pour 1 000 naissances vivantes.

| Indicateur | Formule | Expression |
|---|---|---|
| Taux (quotient) de mortalité infantile (TMI) | Décès < 1 an / naissances vivantes de la même année | ‰ NV |
| Mortalité néonatale | Décès 0-27 j / naissances vivantes | ‰ NV |
| Mortalité néonatale précoce | Décès 0-6 j / naissances vivantes | ‰ NV |
| Mortalité post-néonatale | Décès 28 j - < 1 an / naissances vivantes | ‰ NV |
| Mortinatalité | Mort-nés / (naissances vivantes + mort-nés) | ‰ naissances totales |
| Mortalité périnatale | (Mort-nés + décès 0-6 j) / (naissances vivantes + mort-nés) | ‰ naissances totales |

Interprétation : la mortalité **néonatale précoce et périnatale** reflète surtout les facteurs **endogènes** et la qualité des soins obstétricaux et néonatals (prématurité, asphyxie, malformations) ; la mortalité **post-néonatale** reflète davantage les facteurs **exogènes** (infections, diarrhées, malnutrition, conditions de vie, vaccination). Quand un pays progresse, la part néonatale de la mortalité infantile augmente.

### 5.3 Mortalité maternelle

**Décès maternel** (définition OMS, CIM) : décès d'une femme survenu au cours de la grossesse ou dans un délai de **42 jours** après sa terminaison, quelles que soient la durée et la localisation de la grossesse, pour une cause quelconque déterminée ou aggravée par la grossesse ou les soins qu'elle a motivés, mais **ni accidentelle ni fortuite** [S16]. On distingue les causes **obstétricales directes** (hémorragie, éclampsie, infection, complications d'avortement) et **indirectes** (cardiopathie aggravée par la grossesse…). Le **décès maternel tardif** survient entre 42 jours et un an.

- **Ratio de mortalité maternelle (RMM)** = décès maternels / naissances vivantes × 100 000 (indicateur de référence des ODD).
- **Taux de mortalité maternelle** = décès maternels / femmes en âge de procréer (15-49 ans) × 100 000 ; il dépend aussi de la fécondité.
- Cibles ODD 3.1 et 3.2 pour 2030 : RMM mondial < 70 pour 100 000 NV ; mortalité néonatale ≤ 12 ‰ NV et mortalité des moins de 5 ans ≤ 25 ‰ NV dans tous les pays [S17].

### 5.4 Exemple 5 (fictif) — tableau de bord de mortalité d'une wilaya

Population moyenne : 1 200 000 ; naissances vivantes : 24 000 ; mort-nés : 300 ; décès (tous âges) : 5 400 ; décès < 1 an : 420, dont 270 entre 0 et 27 jours et, parmi eux, 180 entre 0 et 6 jours ; décès maternels : 12.

| Indicateur | Calcul | Résultat |
|---|---|---|
| Taux brut de natalité | 24 000 / 1 200 000 | **20 ‰** |
| Taux brut de mortalité | 5 400 / 1 200 000 | **4,5 ‰** |
| Taux d'accroissement naturel | (24 000 − 5 400) / 1 200 000 | **1,55 %** |
| Mortalité infantile | 420 / 24 000 | **17,5 ‰ NV** |
| Mortalité néonatale | 270 / 24 000 | **11,25 ‰ NV** |
| Mortalité néonatale précoce | 180 / 24 000 | **7,5 ‰ NV** |
| Mortalité post-néonatale | (420 − 270) / 24 000 = 150 / 24 000 | **6,25 ‰ NV** |
| Mortinatalité | 300 / (24 000 + 300) = 300 / 24 300 | **12,3 ‰** (12,35) |
| Mortalité périnatale | (300 + 180) / 24 300 = 480 / 24 300 | **19,8 ‰** (19,75) |
| Ratio de mortalité maternelle | 12 / 24 000 × 100 000 | **50 pour 100 000 NV** |

Vérifications : néonatale + post-néonatale = 11,25 + 6,25 = 17,5 ‰ = mortalité infantile ✔ ; dans cet exemple, 64 % (270/420) des décès infantiles sont néonatals.

---

## 6. Standardisation : comparer des populations de structures différentes

### 6.1 Pourquoi standardiser ?

Le taux brut de mortalité est une **moyenne pondérée** des taux spécifiques par âge, les poids étant la structure d'âge de la population. Deux populations dont la structure d'âge diffère (une wilaya jeune du Sud et une wilaya plus âgée du Nord) ne peuvent pas être comparées sur leurs taux bruts : l'âge est un **facteur de confusion**. La standardisation neutralise cet effet [S9, S10].

### 6.2 Méthode directe (population type)

On applique les **taux spécifiques observés** de chaque population à une **même population de référence** (population type) ; on obtient le nombre de décès « attendus » si chaque population avait la structure de la population type, puis un **taux standardisé**. Le rapport des taux standardisés est l'**indice comparatif de mortalité (ICM)**. Condition : disposer des taux spécifiques par âge, donc d'effectifs suffisants dans chaque strate.

### 6.3 Méthode indirecte (ratio standardisé de mortalité, RSM / SMR)

On applique des **taux de référence** (ceux d'une population connue, par exemple nationale) à la **structure** de la population étudiée pour calculer le nombre de décès attendus E ; on le compare au nombre observé O. **RSM = O / E** (souvent × 100). Méthode préférée quand les effectifs par strate sont faibles (petite population, cohorte professionnelle) ou quand on ne connaît que le nombre total de décès observés.

### 6.4 Exemple 6 (fictif) — standardisation pas à pas

| Âge | Pop. A | Décès A | Taux A | Pop. B | Décès B | Taux B |
|---|---|---|---|---|---|---|
| 0-39 ans | 300 000 | 300 | 1 ‰ | 200 000 | 160 | 0,8 ‰ |
| 40-64 ans | 150 000 | 750 | 5 ‰ | 200 000 | 800 | 4 ‰ |
| ≥ 65 ans | 50 000 | 2 000 | 40 ‰ | 100 000 | 3 500 | 35 ‰ |
| **Total** | **500 000** | **3 050** | **6,1 ‰** | **500 000** | **4 460** | **8,92 ‰** |

Constat paradoxal : la population B a des taux **plus faibles dans chaque tranche d'âge**, mais un taux brut **plus élevé**, parce qu'elle est plus âgée (20 % de ≥ 65 ans contre 10 %).

**Standardisation directe** — population type = A + B (500 000 ; 350 000 ; 150 000) :
- Décès attendus avec les taux de A : 500 000 × 0,001 + 350 000 × 0,005 + 150 000 × 0,040 = 500 + 1 750 + 6 000 = 8 250 → taux standardisé A = 8 250 / 1 000 000 = **8,25 ‰**.
- Décès attendus avec les taux de B : 500 000 × 0,0008 + 350 000 × 0,004 + 150 000 × 0,035 = 400 + 1 400 + 5 250 = 7 050 → taux standardisé B = **7,05 ‰**.
- ICM (B/A) = 7,05 / 8,25 = **0,855** : à structure d'âge égale, la mortalité de B est inférieure d'environ 15 % à celle de A.

**Standardisation indirecte** — taux de référence = taux de A, appliqués à la structure de B :
- Décès attendus dans B : 200 000 × 0,001 + 200 000 × 0,005 + 100 000 × 0,040 = 200 + 1 000 + 4 000 = **5 200**.
- RSM de B = 4 460 / 5 200 = **0,858 (85,8 %)** : B a 14 % de décès en moins que ce qu'on attendrait si elle avait la mortalité par âge de A.

Remarques : le taux standardisé est un **indice de comparaison** (sa valeur absolue dépend de la population type choisie, OMS, nationale, européenne…) ; on ne compare deux taux standardisés que s'ils utilisent la même population type. Deux RSM calculés sur des populations différentes avec des taux de référence communs ne sont pas, en toute rigueur, comparables entre eux (chacun est pondéré par sa propre structure).

---

## 7. Indicateurs démographiques

### 7.1 Natalité, fécondité, accroissement

| Indicateur | Définition |
|---|---|
| Taux brut de natalité (TBN) | Naissances vivantes de l'année / population moyenne (‰) |
| Taux de fécondité générale | Naissances vivantes / femmes de 15-49 ans (‰) |
| Taux de fécondité par âge | Naissances de mères d'un âge donné / femmes de cet âge |
| Indice synthétique de fécondité (ISF) | Somme des taux de fécondité par âge (× 5 si groupes quinquennaux) : nombre moyen d'enfants par femme d'une génération fictive ; seuil de remplacement ≈ 2,1 |
| Taux brut / net de reproduction | Nombre moyen de filles par femme (brut), en tenant compte de la mortalité féminine (net) |
| Taux d'accroissement naturel | TBN − TBM (exprimé en %) ; l'accroissement total ajoute le solde migratoire |

### 7.2 Espérance de vie

L'**espérance de vie à la naissance** (e₀) est la durée moyenne de vie d'une génération **fictive** qui serait soumise, à chaque âge, aux quotients de mortalité observés une année donnée (**table de mortalité du moment**). Ce n'est **pas** une prévision de la durée de vie des nouveau-nés de l'année, ni l'âge moyen au décès des personnes décédées cette année-là. Avantage majeur : elle est **indépendante de la structure d'âge** de la population, donc directement comparable entre pays. L'espérance de vie à 60 ou 65 ans est l'indicateur pertinent pour la planification gériatrique.

### 7.3 Structure de la population

- **Pyramide des âges** : base large (population jeune, forte fécondité), forme en « meule » ou en « urne » (vieillissement).
- **Rapport de dépendance** = (0-14 ans + ≥ 65 ans) / (15-64 ans) × 100.
- **Indice de vieillissement** = (≥ 65 ans, ou ≥ 60 ans selon les sources) / (< 15 ans, ou < 20 ans) × 100 : préciser les bornes utilisées.
- **Transition démographique** : baisse de la mortalité puis de la natalité ; **transition épidémiologique** : passage d'une prédominance des maladies infectieuses et carentielles à celle des maladies non transmissibles, avec souvent une phase de **double charge**.

### 7.4 Données algériennes récentes (ONS) et lecture critique

Les chiffres suivants sont ceux de la publication ONS « Démographie algérienne 2020-2023 » tels que **relayés par la presse en juillet 2024** ; ce ne sont pas des chiffres officiels vérifiés : ils doivent être confrontés au document original [S4] `[À VÉRIFIER — source primaire non consultée]` :

| Indicateur (Algérie) | Valeur relayée par la presse (source secondaire) | Année |
|---|---|---|
| Population au 1er janvier | ≈ 46,7 millions | 2024 |
| Naissances vivantes | ≈ 895 000 (première fois sous 900 000 depuis 2010) | 2023 |
| Décès | ≈ 192 000 | 2023 |
| Taux brut de mortalité | 4,15 ‰ (4,45 ‰ en 2022 ; pic de 5,75 ‰ en 2021, contemporain de la pandémie de COVID-19) | 2023 |
| Taux brut de natalité | 19,32 ‰ selon une reprise de presse (une base secondaire donne 19,63 ‰ : divergence à vérifier) | 2023 |
| Taux d'accroissement naturel | 1,52 % (≈ 703 000 personnes) | 2023 |
| Mortalité infantile | 19,9 ‰ | 2023 |
| Espérance de vie à la naissance | 79,6 ans (hommes 78,2 ; femmes 81,0) | 2023 |

**Exercice de cohérence** (bon réflexe de lecture critique) :
- Accroissement naturel = naissances − décès = 895 000 − 192 000 = **703 000** ✔.
- Population moyenne implicite ≈ 703 000 / 0,0152 ≈ 46,25 millions ; TBN ≈ 895 000 / 46,25 M ≈ **19,35 ‰** (cohérent avec 19,32 ‰) ; TBM ≈ 192 000 / 46,25 M ≈ **4,15 ‰** ✔.
- Le pic de mortalité 2021 illustre qu'un taux brut annuel est sensible aux événements exceptionnels (épidémies) : pour analyser une tendance, il faut des séries longues et des taux standardisés.

**Facteurs de risque des maladies non transmissibles** — enquête STEPS Algérie 2016-2017, échantillon représentatif de 7 450 personnes de 18 à 69 ans [S5, S6] :
- diabète : **14,4 %** ; hyperglycémie modérée à jeun : **8,2 %** ;
- tabac fumé (consommation actuelle) : **16,5 %** ;
- ces trois chiffres proviennent d'un communiqué de l'OMS Afrique et non du fascicule officiel, qui n'a pas pu être consulté `[À VÉRIFIER — source primaire non consultée]` ;
- hypertension artérielle : **31,6 %** (IC 95 % : 30,5-32,7) et pré-hypertension : **36,2 %** (IC 95 % : 35,2-37,5), selon une analyse secondaire publiée et vérifiée de la base STEPS [S6] ; ses définitions et son effectif analysé peuvent différer de ceux du fascicule officiel.

Ces prévalences sont des **indicateurs de déterminants** ; leur niveau, associé au vieillissement mesuré par l'ONS, documente la **transition épidémiologique** de l'Algérie et justifie les plans nationaux multisectoriels de lutte contre les maladies non transmissibles prévus par la loi (art. 45-48) [S1]. L'enquête MICS6 (2019) fournit de son côté les indicateurs de santé de l'enfant et de la femme (couvertures, nutrition, mortalité estimée) [S7] — aucun de ses chiffres n'est repris ici faute de consultation directe du rapport.

---

## 8. Indicateurs composites : intégrer mortalité et qualité de vie

### 8.1 Espérances de santé

- **Espérance de vie sans incapacité (EVSI)** : nombre moyen d'années qu'une personne peut espérer vivre sans incapacité, calculé (méthode de Sullivan) en combinant la table de mortalité et la prévalence de l'incapacité par âge issue d'enquêtes.
- **Espérance de vie en bonne santé (HALE, OMS)** : espérance de vie pondérée par l'état de santé (poids d'incapacité). Selon GBD 2021, la HALE mondiale à la naissance est passée de 61,3 ans (2010) à 62,2 ans (2021) avec une baisse de 2,2 % entre 2019 et 2021 [S8].
- Intérêt : savoir si les années gagnées sont vécues en bonne santé (« compression » ou « expansion » de la morbidité).

### 8.2 DALY (AVCI — années de vie corrigées de l'incapacité)

Un DALY représente **une année de vie en bonne santé perdue**. C'est une mesure du **fardeau** (charge) d'une maladie dans une population, qui additionne la mortalité prématurée et la morbidité :

**DALY = YLL + YLD**
- **YLL** (*years of life lost*, années de vie perdues par décès prématuré) = nombre de décès × espérance de vie **résiduelle de référence** à l'âge du décès (table de vie standard du GBD).
- **YLD** (*years lived with disability*, années vécues avec incapacité) = dans les éditions récentes du GBD, **prévalence** des séquelles × **poids d'incapacité** (0 = santé parfaite, 1 = état équivalent au décès) [S8] ; dans la formulation initiale (1994), incidence × durée × poids [S15].
- Depuis GBD 2010, la pondération par l'âge et l'actualisation (*discounting*) ne sont plus appliquées.

**Exemple 7 (fictif)** : une maladie cause 100 décès à 60 ans ; on suppose, pour l'exercice, une espérance de vie résiduelle de référence de 25 ans à cet âge (valeur fictive). Par ailleurs, 2 000 personnes vivent avec la maladie pendant l'année, avec un poids d'incapacité de 0,2.
- YLL = 100 × 25 = 2 500 ; YLD = 2 000 × 0,2 × 1 an = 400 ; **DALY = 2 900**.
- Lecture : la maladie « coûte » 2 900 années de vie en bonne santé à la population cette année ; 86 % de ce fardeau vient de la mortalité.

Selon GBD 2021, le nombre mondial de DALY toutes causes est passé de 2,63 milliards (2010) à 2,88 milliards (2021) ; en 2021, la COVID-19 était la première cause de DALY, devant la cardiopathie ischémique, les affections néonatales et l'AVC [S8].

### 8.3 QALY (AVAQ — années de vie ajustées sur la qualité)

Un QALY est une année de vie **gagnée** pondérée par sa qualité (utilité de 0 = décès à 1 = santé parfaite ; utilités mesurées par des questionnaires de type EQ-5D). On l'utilise en **évaluation économique** (analyse coût-utilité) pour comparer des interventions : **rapport différentiel coût-résultat (RDCR, ICER)** = Δ coût / Δ QALY.

**Exemple 8 (fictif)** : le traitement A procure 4 ans de survie avec une utilité de 0,75 (= 3,0 QALY) ; le traitement B procure 5 ans avec une utilité de 0,5 (= 2,5 QALY). A coûte 600 000 DA de plus que B. Gain = 0,5 QALY ; **ICER = 600 000 / 0,5 = 1 200 000 DA par QALY gagné**. Le décideur compare ce chiffre à un seuil de disposition à payer (non défini officiellement en Algérie `[À VÉRIFIER]`).

| | DALY | QALY |
|---|---|---|
| Ce qu'on compte | Années de vie en bonne santé **perdues** | Années de vie **gagnées** pondérées par la qualité |
| Objectif | À **réduire** | À **maximiser** |
| Usage principal | Charge de morbidité, priorités de santé publique (GBD) | Évaluation économique (coût-utilité) |
| Pondération | Poids d'incapacité (0 = santé parfaite) | Utilité (1 = santé parfaite) |

### 8.4 Autres indices composites

L'**indice de développement humain** (PNUD) combine espérance de vie, éducation et revenu ; il situe la santé parmi les déterminants du développement mais n'est pas un indicateur sanitaire au sens strict.

---

## 9. Indicateurs du système de soins et des déterminants

L'OMS propose une liste de référence de 100 indicateurs de base, organisée en quatre domaines : état de santé, facteurs de risque, couverture des services, systèmes de santé [S12].

| Domaine | Exemples d'indicateurs | Formule / remarque |
|---|---|---|
| Déterminants / facteurs de risque | Prévalence du tabagisme, de l'obésité, de l'HTA, de la sédentarité | Enquêtes (STEPS) |
| Ressources | Densité de médecins, de sages-femmes, d'infirmiers pour 10 000 habitants ; lits pour 1 000 habitants | Effectifs / population |
| Couverture | Couverture vaccinale (ex. 3e dose de vaccin combiné) ; % d'accouchements assistés par du personnel qualifié ; consultations prénatales | Bénéficiaires / population cible (cible définie par le calendrier vaccinal réglementaire [S18]) |
| Utilisation / activité hospitalière | Taux d'occupation des lits = journées d'hospitalisation réalisées / journées-lits disponibles ; durée moyenne de séjour (DMS) = journées / sorties ; taux de rotation = sorties / lits | Données d'activité |
| Qualité / sécurité | Taux d'infections du site opératoire, incidence des PAVM pour 1 000 jours de ventilation, taux de BMR | Désormais MDO en Algérie [S3] |
| Financement | Dépense courante de santé en % du PIB, dépense par habitant, part des paiements directs des ménages | Comptes nationaux de la santé (art. 338) [S1] |

**Exemple 9 (fictif)** : un service de 40 lits réalise 12 410 journées sur l'année et 2 482 sorties. Journées disponibles = 40 × 365 = 14 600 ; taux d'occupation = 12 410 / 14 600 = **85 %** ; DMS = 12 410 / 2 482 = **5,0 jours** ; taux de rotation = 2 482 / 40 ≈ **62 patients par lit et par an** (62,05).

---

## 10. Mesures d'association et mesures d'impact

### 10.1 Tableau de contingence de référence (cohorte)

| | Malades | Non malades | Total | Incidence |
|---|---|---|---|---|
| Exposés | a | b | a + b | Ie = a / (a + b) |
| Non exposés | c | d | c + d | I₀ = c / (c + d) |
| Total | a + c | b + d | N | It = (a + c) / N |

### 10.2 Mesures d'association (force du lien)

- **Risque relatif (RR)** = Ie / I₀ : combien de fois le risque est multiplié chez les exposés. RR = 1 : pas d'association ; RR > 1 : facteur de risque ; RR < 1 : facteur protecteur. Calculable dans les cohortes et les essais.
- **Rapport des taux d'incidence** (*incidence rate ratio*) quand on utilise des personnes-temps.
- **Odds ratio (OR)** = (a × d) / (b × c) : mesure d'association des enquêtes cas-témoins (et des régressions logistiques). Il approche le RR quand la maladie est **rare** (voir DOS-EPID-0002).

### 10.3 Mesures d'impact chez les exposés

- **Différence de risque** (risque attribuable chez les exposés, « excès de risque ») : **RA = Ie − I₀** — nombre de cas en excès dus à l'exposition, parmi les exposés. C'est la mesure d'**impact individuel absolu**.
- **Fraction étiologique (attribuable) chez les exposés** : **FEE = (Ie − I₀) / Ie = (RR − 1) / RR** — proportion des cas survenant chez les exposés qui sont attribuables à l'exposition (et seraient évités si l'exposition était supprimée, en l'absence de biais et de confusion).

### 10.4 Mesures d'impact dans la population

- **Risque attribuable dans la population** : **RAP = It − I₀ = Pe × (Ie − I₀)** (Pe = proportion d'exposés dans la population).
- **Fraction attribuable dans la population (FAP, fraction étiologique du risque)** : **FAP = (It − I₀) / It**.
  - Formule de **Levin** (à partir de la prévalence de l'exposition dans la population) : FAP = Pe (RR − 1) / [1 + Pe (RR − 1)] [S14].
  - Formule de **Miettinen** (à partir de la proportion d'exposés **parmi les cas**, pc) : FAP = pc × (RR − 1) / RR — utilisable avec un OR dans une étude cas-témoins si la maladie est rare.
- La FAP dépend **à la fois** de la force de l'association (RR) et de la **fréquence** de l'exposition : un facteur modérément associé mais très répandu (sédentarité) peut avoir un impact de population supérieur à un facteur fortement associé mais rare.
- Les FAP de plusieurs facteurs ne s'additionnent pas (leur somme peut dépasser 100 %), car un même cas peut être évitable par la suppression de plusieurs facteurs.

### 10.5 Exemple 10 (fictif) — tabac et une maladie respiratoire, cohorte de 10 000 personnes suivies 5 ans

| | Malades | Non malades | Total |
|---|---|---|---|
| Fumeurs | 60 | 1 940 | 2 000 |
| Non-fumeurs | 40 | 7 960 | 8 000 |
| Total | 100 | 9 900 | 10 000 |

- Ie = 60 / 2 000 = **3 %** ; I₀ = 40 / 8 000 = **0,5 %** ; It = 100 / 10 000 = **1 %** ; Pe = 2 000 / 10 000 = 0,2.
- **RR** = 3 / 0,5 = **6** (IC 95 % par la méthode logarithmique : ln RR = 1,792 ; ES = √(1/60 − 1/2 000 + 1/40 − 1/8 000) = 0,2026 ; IC = e^(1,792 ± 1,96 × 0,2026) = **4,03 à 8,92**).
- **RA** = 3 % − 0,5 % = **2,5 %**, soit 25 cas en excès pour 1 000 fumeurs sur 5 ans.
- **FEE** = (6 − 1) / 6 = **83,3 %** : chez les fumeurs malades, 5 cas sur 6 sont attribuables au tabac.
- **RAP** = 1 % − 0,5 % = **0,5 %** (5 cas pour 1 000 habitants) ; vérification : Pe × RA = 0,2 × 2,5 % = 0,5 % ✔.
- **FAP** = 0,5 / 1 = **50 %** ; Levin : 0,2 × 5 / (1 + 0,2 × 5) = 1 / 2 = **50 %** ✔ ; Miettinen : pc = 60/100 = 0,6 → 0,6 × 5/6 = **50 %** ✔.
- Interprétation : supprimer le tabac éviterait la moitié des cas de la population (si la relation est causale et non confondue).

### 10.6 Mesures d'impact d'une intervention (essais thérapeutiques et préventifs)

Soit un risque d'événement de 20 % dans le groupe contrôle (Rc) et de 15 % dans le groupe traité (Rt), sur 2 ans :

| Mesure | Formule | Exemple 11 |
|---|---|---|
| Risque relatif | Rt / Rc | 0,15 / 0,20 = **0,75** |
| Réduction relative du risque (RRR) | (Rc − Rt) / Rc = 1 − RR | **25 %** |
| Réduction absolue du risque (RAR) | Rc − Rt | **5 %** (5 points) |
| Nombre de sujets à traiter (NNT) | 1 / RAR | 1 / 0,05 = **20 patients pendant 2 ans** pour éviter 1 événement |
| Augmentation absolue d'un effet indésirable | Rt(EI) − Rc(EI) | 3 % − 1 % = 2 % |
| Nombre nécessaire pour nuire (NNH) | 1 / augmentation absolue | 1 / 0,02 = **50** |

Messages clés [S13] :
- la RRR est souvent constante d'une population à l'autre, mais la **RAR et le NNT dépendent du risque de base** : le même traitement (RRR 25 %) chez des patients dont le risque de base est 4 % donne RAR = 1 % et NNT = 100 ;
- un NNT doit toujours être accompagné de la **durée** et de l'**événement** considérés ; on arrondit à l'entier **supérieur** ;
- la présentation des résultats en relatif (« réduit le risque de 25 % ») impressionne davantage que la présentation absolue : piège de communication.

### 10.7 Fractions prévenues et efficacité vaccinale

Quand l'exposition est **protectrice** (vaccin, programme), on utilise :
- **Fraction prévenue chez les exposés** = (I₀ − Ie) / I₀ = 1 − RR ;
- **Efficacité vaccinale (EV)** = (TA non vaccinés − TA vaccinés) / TA non vaccinés = 1 − RR ;
- **Fraction prévenue dans la population** = (I attendue sans intervention − I observée) / I attendue = **couverture × EV** (si la couverture est la proportion de vaccinés).

**Exemple 12 (fictif)** : taux d'attaque de 10 % chez les non-vaccinés et 1 % chez les vaccinés → RR = 0,1 → **EV = 90 %**. Avec une couverture de 80 %, le taux d'attaque global est 0,8 × 1 % + 0,2 × 10 % = **2,8 %** au lieu de 10 % sans vaccination ; fraction prévenue dans la population = (10 − 2,8) / 10 = **72 %** = 0,8 × 0,9 ✔.

### 10.8 Synthèse des mesures

| Question posée | Mesure | Type d'étude |
|---|---|---|
| Fréquence d'une maladie à un instant | Prévalence | Transversale |
| Vitesse d'apparition | Incidence (cumulée, densité) | Cohorte, registre |
| Gravité d'une maladie | Létalité | Suivi des cas |
| Force d'une association | RR, rapport de taux, OR | Cohorte, cas-témoins |
| Impact chez les exposés | RA, FEE | Cohorte |
| Impact dans la population | RAP, FAP | Cohorte + prévalence d'exposition |
| Bénéfice d'un traitement | RRR, RAR, NNT | Essai randomisé |
| Fardeau global | DALY, APVP | Synthèses (GBD) |
| Efficience | Coût par QALY (ICER) | Évaluation économique |

---

## 11. Biais et limites des indicateurs

- **Qualité du numérateur** : sous-déclaration des MDO, causes de décès mal définies (« arrêt cardio-respiratoire » n'est pas une cause), certificat incomplet ; le décret 22-178 impose au médecin de renseigner la cause directe **et** tous les états morbides antérieurs (art. 6) [S2].
- **Qualité du dénominateur** : projections de population entre deux recensements, populations mobiles (nomades, migrants), naissances non enregistrées.
- **Artefacts** : une hausse de l'incidence peut traduire une amélioration du dépistage ou un changement de définition de cas (ex. abaissement d'un seuil diagnostique) ; une hausse de prévalence peut traduire un allongement de la survie.
- **Erreur écologique** : une corrélation entre indicateurs agrégés (wilayas) ne prouve pas l'association au niveau individuel.
- **Petits effectifs** : un taux calculé sur quelques événements fluctue fortement ; on regroupe plusieurs années ou on calcule un intervalle de confiance.
- **Effet de structure** : toujours se demander si l'âge (ou une autre variable) explique la différence observée → standardiser.

---

## 12. Algorithmes décisionnels

### 12.1 Choisir l'indicateur de fréquence

```text
1. L'événement est-il un état durable (maladie chronique, caractéristique) ou un événement ponctuel (survenue, décès) ?
   1a. État durable, question = « combien de personnes sont concernées maintenant ? » → PRÉVALENCE (enquête transversale)
   1b. Survenue, question = « à quelle vitesse apparaissent les nouveaux cas ? » → aller en 2
2. Le suivi est-il identique pour tous et la population fermée ?
   2a. Oui → INCIDENCE CUMULÉE (préciser la durée : risque à n ans)
   2b. Non (entrées/sorties, durées inégales) → DENSITÉ D'INCIDENCE (personnes-temps)
3. Contexte épidémique, période courte → TAUX D'ATTAQUE (± taux d'attaque secondaire chez les contacts)
4. L'événement est un décès :
   4a. Gravité de la maladie → LÉTALITÉ
   4b. Impact sur la population → MORTALITÉ SPÉCIFIQUE (pour 100 000)
   4c. Comparaison de populations d'âges différents → TAUX STANDARDISÉS (directe) ou RSM (indirecte)
   4d. Décès prématurés → APVP ; fardeau global → DALY
```

### 12.2 Choisir la mesure d'association ou d'impact

```text
1. Type d'étude ?
   1a. Cohorte / essai → RR (ou rapport de taux) ; impact individuel → RA ; part des cas des exposés → FEE
   1b. Cas-témoins → OR (≈ RR si maladie rare) ; impact population → FAP de Miettinen (pc × (OR−1)/OR)
   1c. Transversale → rapport de prévalences (ou OR de prévalence)
2. Question de santé publique « combien de cas éviterait-on dans la population ? »
   → RAP (absolu) ou FAP (relatif) ; nécessite la prévalence de l'exposition (Levin) ou la proportion d'exposés parmi les cas (Miettinen)
3. Question thérapeutique « combien de patients traiter pour éviter un événement ? »
   → RAR puis NNT = 1/RAR (arrondi à l'entier supérieur, durée et événement précisés) ; balance avec NNH
4. Exposition protectrice (vaccin) → EV = 1 − RR ; fraction prévenue dans la population = couverture × EV
```

---

## 13. Situation de santé publique commentée (cas fictif)

**Contexte** : vous êtes médecin au service d'épidémiologie d'un établissement public de santé de proximité couvrant une daïra fictive de 150 000 habitants. La direction de wilaya chargée de la santé vous demande un état de santé de la population pour préparer le projet d'établissement (art. 290 de la loi 18-11) [S1].

**Données disponibles (année N, fictives)** : 3 000 naissances vivantes ; 54 décès d'enfants de moins d'un an, dont 36 dans les 28 premiers jours ; 760 décès toutes causes, alors que l'application des taux nationaux par âge à la structure de la daïra prévoit 800 décès ; prévalence du diabète connu passée de 8 % à 10 % en 5 ans ; enquête locale : 25 % d'adultes obèses ; on admet un RR de diabète de 3 chez les obèses.

**Questions et réponses commentées**
1. *Calculez la mortalité infantile et sa composante néonatale.* — TMI = 54 / 3 000 = **18 ‰** ; mortalité néonatale = 36 / 3 000 = **12 ‰** ; post-néonatale = 18 / 3 000 = **6 ‰**. Deux tiers des décès infantiles sont néonatals : la priorité est la qualité de la prise en charge périnatale (surveillance de la grossesse, accouchement, réanimation néonatale), plus que les seuls facteurs exogènes.
2. *La mortalité générale de la daïra est-elle anormale ?* — RSM = 760 / 800 = **0,95** : la mortalité est 5 % inférieure à ce que prédisent les taux nationaux, compte tenu de la structure d'âge. Il ne faut **pas** comparer le taux brut de la daïra au taux brut national (structures d'âge différentes). Avec de petits effectifs, l'écart de 5 % n'est probablement pas significatif (calculer un intervalle de confiance).
3. *Interprétez la hausse de la prévalence du diabète connu.* — Trois explications non exclusives : hausse de l'**incidence** (obésité, sédentarité), **meilleur dépistage** (diabète connu ≠ diabète réel), **survie prolongée** des diabétiques (P ≈ I × D). Il faut des données d'incidence ou une enquête avec mesure de la glycémie (type STEPS [S5]) pour trancher.
4. *Quelle part des diabètes est attribuable à l'obésité ?* — FAP (Levin) = 0,25 × (3 − 1) / [1 + 0,25 × (3 − 1)] = 0,5 / 1,5 = **33 %** (si la relation est causale et non confondue).
5. *Un programme réduit la prévalence de l'obésité de 25 % à 20 %. Quelle baisse de l'incidence du diabète attendre ?* — L'incidence totale est proportionnelle à 1 + Pe (RR − 1) : elle passe de 1,5 à 1,4 (× I₀), soit une baisse de **6,7 %** — bien moins que ce qu'imaginent souvent les décideurs, et différée dans le temps.
6. *Quels indicateurs retenir pour évaluer le programme ?* — Indicateurs de **processus** (nombre de séances d'éducation, de personnes dépistées), de **résultat intermédiaire** (prévalence de l'obésité, de la sédentarité), d'**impact** (incidence du diabète, complications, DALY) ; préciser pour chacun numérateur, dénominateur, source et périodicité.

**Message pédagogique** : un état de santé de la population se construit avec des indicateurs **définis, sourcés, comparés avec prudence** (standardisation), complétés par des mesures d'impact qui orientent les priorités.

---

## 14. Points clés à retenir

1. Tout indicateur se définit par un **numérateur**, un **dénominateur**, une **période** et un **lieu** ; la prévalence et la létalité sont des proportions, la densité d'incidence est un vrai taux (personnes-temps).
2. **Prévalence ≈ incidence × durée** (situation stable, prévalence faible) : un meilleur traitement non curatif augmente la prévalence.
3. Mortalité infantile = néonatale (0-27 j) + post-néonatale (28 j - 1 an), rapportées aux **naissances vivantes** ; mortinatalité et mortalité périnatale sont rapportées aux **naissances totales**.
4. Le **ratio de mortalité maternelle** se calcule pour 100 000 **naissances vivantes** ; le décès maternel survient pendant la grossesse ou dans les **42 jours**, de cause ni accidentelle ni fortuite.
5. Un taux **brut** n'est pas comparable entre populations de structures différentes : standardisation **directe** (population type, ICM) ou **indirecte** (RSM = observés / attendus).
6. L'**espérance de vie** est indépendante de la structure d'âge ; elle décrit une génération fictive.
7. **DALY = YLL + YLD** (fardeau à réduire) ; **QALY** = années gagnées × utilité (gain à maximiser, évaluation économique).
8. RR = force de l'association ; **RA = Ie − I₀** = impact absolu chez les exposés ; **FEE = (RR − 1)/RR** ; **FAP** dépend du RR **et** de la fréquence de l'exposition.
9. **NNT = 1/RAR**, dépend du risque de base ; toujours préciser durée et critère.
10. **EV = 1 − RR** ; fraction prévenue dans la population = couverture × EV.
11. En Algérie, les données proviennent notamment de l'état civil, du certificat de décès (décret 22-178), des MDO (décret 22-250), des registres (art. 47), du système national d'information sanitaire (art. 319-323) et des enquêtes nationales (ONS, STEPS, MICS).

---

## 15. Pièges classiques à l'examen

- Confondre **létalité** (proportion de malades qui décèdent) et **mortalité spécifique** (décès rapportés à la population).
- Mettre au dénominateur de l'incidence cumulée la **population totale** au lieu de la population **à risque** (exclure les malades prévalents et les non-susceptibles).
- Rapporter la mortinatalité aux **naissances vivantes** au lieu des naissances totales.
- Croire que la **mortalité proportionnelle** mesure un risque.
- Comparer deux **taux bruts** de mortalité entre populations d'âges différents.
- Interpréter une hausse de **prévalence** comme une hausse d'incidence sans considérer la durée et le dépistage.
- Calculer un **NNT** sans durée, ou l'arrondir à l'entier inférieur.
- Additionner des **FAP** de plusieurs facteurs.
- Confondre **RRR** et **RAR** : « réduit le risque de 25 % » peut correspondre à 1 point absolu.
- Confondre **DALY** (perdues) et **QALY** (gagnées), ou YLL et APVP (les APVP utilisent un âge limite arbitraire, les YLL une table de vie de référence).
- Oublier qu'un RSM se compare à 1 (ou 100) **par rapport à sa référence**, pas à un autre RSM calculé sur une autre population.

---

## 16. QCM d'auto-évaluation (corrigé en fin de section)

**QCM 1.** Concernant la prévalence :
A. C'est une proportion sans unité
B. Elle augmente si un traitement prolonge la survie sans guérir
C. Elle se mesure idéalement par une enquête transversale
D. Elle est le meilleur indicateur du risque individuel de tomber malade
E. En situation stable et pour une maladie rare, elle est approximativement égale à l'incidence multipliée par la durée moyenne de la maladie

**QCM 2.** Une population de 8 000 personnes indemnes est suivie 2 ans ; 160 nouveaux cas apparaissent. L'incidence cumulée à 2 ans est :
A. 2 % B. 1 % par an exactement C. 20 pour 1 000 D. 160 pour 100 000 E. 4 %

**QCM 3.** Une wilaya enregistre 30 000 naissances vivantes, 450 mort-nés, 540 décès avant 1 an dont 330 avant 28 jours et 240 avant 7 jours. Indiquez les propositions exactes :
A. Mortalité infantile = 18 ‰
B. Mortalité néonatale = 11 ‰
C. Mortalité post-néonatale = 7 ‰
D. Mortinatalité = 15 ‰
E. Mortalité périnatale ≈ 22,7 ‰

**QCM 4.** À propos de la standardisation :
A. La méthode directe applique les taux spécifiques de chaque population à une population type
B. La méthode indirecte nécessite les taux spécifiques par âge de la population étudiée
C. Le RSM est le rapport des décès observés aux décès attendus
D. Un taux standardisé a une valeur absolue indépendante de la population type choisie
E. La méthode indirecte est préférée pour les petites populations

**QCM 5.** Dans une cohorte, Ie = 4 % chez les exposés et I₀ = 1 % chez les non-exposés ; 25 % de la population est exposée. Indiquez les propositions exactes :
A. RR = 4
B. Différence de risque = 3 %
C. Fraction étiologique chez les exposés = 75 %
D. FAP ≈ 43 %
E. Risque attribuable dans la population = 3 %

**QCM 6.** Dans un essai, l'événement survient chez 10 % des témoins et 8 % des traités en 3 ans. Indiquez les propositions exactes :
A. RRR = 20 %
B. RAR = 2 %
C. NNT = 50 sur 3 ans
D. RR = 1,25
E. Le NNT serait identique chez des patients à risque de base deux fois plus élevé

**QCM 7.** Concernant les DALY :
A. Ils additionnent les années de vie perdues par décès prématuré et les années vécues avec incapacité
B. Un DALY correspond à une année de vie en bonne santé gagnée
C. Le poids d'incapacité vaut 0 pour une santé parfaite
D. Les éditions récentes du GBD appliquent une pondération par l'âge
E. Ils servent à hiérarchiser les problèmes de santé publique

**QCM 8.** Concernant la mortalité maternelle :
A. Le décès maternel inclut les décès accidentels survenant pendant la grossesse
B. Le délai retenu est de 42 jours après la fin de la grossesse
C. Le ratio de mortalité maternelle est exprimé pour 100 000 naissances vivantes
D. La cible ODD mondiale pour 2030 est un ratio inférieur à 70 pour 100 000 naissances vivantes
E. Une hémorragie de la délivrance est une cause obstétricale directe

**QCM 9.** Un vaccin a une efficacité de 80 % ; la couverture est de 90 %. Indiquez les propositions exactes :
A. Le RR vaccinés/non-vaccinés est 0,2
B. La fraction prévenue dans la population est 72 %
C. Si le taux d'attaque chez les non-vaccinés est 5 %, il est de 1 % chez les vaccinés
D. L'efficacité vaccinale se calcule (TA vaccinés − TA non-vaccinés)/TA vaccinés
E. Le taux d'attaque global attendu (TA non-vaccinés = 5 %) est 1,4 %

**QCM 10.** Selon la loi algérienne n° 18-11 relative à la santé :
A. Tout praticien médical doit déclarer sans délai tout cas suspect ou confirmé de MDO
B. La liste des MDO est fixée par voie réglementaire
C. Les structures privées sont dispensées d'intégrer le système national d'information sanitaire
D. Un observatoire national de la santé élabore un rapport annuel sur l'état de santé de la population
E. Les comptes nationaux de la santé sont publiés annuellement

### Corrigé commenté

- **QCM 1 : A, B, C, E.** D est faux : le risque individuel est mesuré par l'incidence cumulée.
- **QCM 2 : A, C.** 160/8 000 = 2 % = 20 pour 1 000 sur 2 ans. B est faux : diviser par 2 donne une approximation (≈ 1 % par an), pas une valeur exacte ; E est faux.
- **QCM 3 : A, B, C, E.** TMI = 540/30 000 = 18 ‰ ; néonatale = 330/30 000 = 11 ‰ ; post-néonatale = 210/30 000 = 7 ‰ ; mortinatalité = 450/30 450 = 14,8 ‰ (D faux : 15 ‰ correspondrait au dénominateur erroné des naissances vivantes) ; périnatale = (450 + 240)/30 450 = 690/30 450 = 22,66 ‰.
- **QCM 4 : A, C, E.** B est faux (c'est la méthode directe qui exige les taux spécifiques de la population étudiée) ; D est faux (la valeur dépend de la population type).
- **QCM 5 : A, B, C, D.** RR = 4 ; RA = 3 % ; FEE = 3/4 = 75 % ; FAP (Levin) = 0,25 × 3 / (1 + 0,75) = 0,75/1,75 = 42,9 % ; RAP = It − I₀ avec It = 0,25 × 4 % + 0,75 × 1 % = 1,75 % → RAP = 0,75 % (E faux).
- **QCM 6 : A, B, C.** RR = 0,8 (D faux) ; RRR = 20 % ; RAR = 2 % ; NNT = 50. E faux : à risque de base double (20 %), la RAR serait 4 % et le NNT 25.
- **QCM 7 : A, C, E.** B décrit le QALY (gagné) ; D est faux depuis GBD 2010.
- **QCM 8 : B, C, D, E.** A est faux : les causes accidentelles ou fortuites sont exclues.
- **QCM 9 : A, B, C, E.** RR = 1 − 0,8 = 0,2 ; fraction prévenue = 0,9 × 0,8 = 72 % ; TA vaccinés = 0,2 × 5 % = 1 % ; TA global = 0,9 × 1 % + 0,1 × 5 % = 0,9 + 0,5 = 1,4 %. D est faux (le dénominateur est le TA des non-vaccinés).
- **QCM 10 : A, B, D, E.** C est faux : l'article 321 oblige les structures publiques **et privées** à intégrer le système national d'information sanitaire [S1].

---

## 17. Divergences entre sources et recommandations

| Sujet | Position 1 | Position 2 | Conséquence pratique |
|---|---|---|---|
| Méthode DALY | GBD initial (Murray, 1994) : YLD fondés sur l'incidence, pondération par l'âge et actualisation à 3 % [S15] | GBD depuis 2010 (GBD 2021, 2024) : YLD fondés sur la prévalence, sans pondération par l'âge ni actualisation [S8] | Les DALY de différentes éditions ne sont pas directement comparables : comparer des séries recalculées dans une même édition |
| Seuil de la période périnatale / mortinatalité | CIM-10 : dès 22 semaines révolues (500 g) [S16] | OMS, comparaisons internationales : ≥ 28 semaines (≥ 1 000 g) | Préciser le seuil avant toute comparaison ; seuil réglementaire algérien `[À VÉRIFIER]` |
| Indice de vieillissement | ≥ 65 ans / < 15 ans | ≥ 60 ans / < 20 ans | Valeurs très différentes ; toujours citer les bornes |
| TBN algérien 2023 | 19,32 ‰ (reprise de presse de l'ONS) [S4] | 19,63 ‰ (base de données secondaire) | Se référer à la publication ONS n° 1030 ; cohérence interne favorisant ≈ 19,3 ‰ (voir § 7.4) |
| Terminologie « risque attribuable » | Usage anglo-saxon : *attributable risk* = différence de risque (Ie − I₀) | Nombreux textes francophones : « risque attribuable » = fraction attribuable (%) | Toujours écrire la formule utilisée |
| Mortalité maternelle | Ratio (pour 100 000 NV, ODD) [S17] | Taux (pour 100 000 femmes de 15-49 ans) | Le ratio mesure le risque obstétrical par naissance, le taux intègre aussi la fécondité |

---

## 18. Références

1. [S1] Loi n° 18-11 du 2 juillet 2018 relative à la santé. JORADP n° 46, 29 juillet 2018 (DOC-00074).
2. [S2] Décret exécutif n° 22-178 du 28 avril 2022 relatif au certificat médical de décès. JORADP n° 32, 14 mai 2022 (DOC-00077).
3. [S3] Décret exécutif n° 22-250 du 30 juin 2022 fixant la liste des MDO. JORADP n° 47, 11 juillet 2022 (DOC-00072).
4. [S4] ONS. Démographie algérienne 2020-2023 (n° 1030). Alger, 2024 — chiffres via reprises de presse, à confronter à l'original `[À VÉRIFIER — source primaire non consultée]`.
5. [S5] MSPRH / OMS. Enquête STEPwise Algérie 2016-2017 — principaux résultats (2018).
6. [S6] Moussouni A, Sidi-Yakhlef A, Hamdaoui H, Aouar A, Belkhatir D. Prevalence and risk factors of prehypertension and hypertension in Algeria. BMC Public Health 2022;22(1):1571. doi:10.1186/s12889-022-13942-y.
7. [S7] MSPRH / UNICEF. MICS6 Algérie 2019 — rapport final (décembre 2020).
8. [S8] GBD 2021 Diseases and Injuries Collaborators. Lancet 2024;403(10440):2133-2161. doi:10.1016/S0140-6736(24)00757-8.
9. [S9] Lash TL, VanderWeele TJ, Haneuse S, Rothman KJ. Modern Epidemiology. 4th ed. Wolters Kluwer; 2021.
10. [S10] Celentano DD, Szklo M. Gordis Epidemiology. 6th ed. Elsevier; 2019.
11. [S11] Porta M. A Dictionary of Epidemiology. 6th ed. Oxford University Press; 2014.
12. [S12] WHO. 2018 Global Reference List of 100 Core Health Indicators (plus health-related SDGs).
13. [S13] Laupacis A, Sackett DL, Roberts RS. N Engl J Med 1988;318:1728-1733.
14. [S14] Levin ML. Acta Unio Int Contra Cancrum 1953;9:531-541.
15. [S15] Murray CJL. Bull World Health Organ 1994;72(3):429-445.
16. [S16] OMS. CIM-10, volume 2 ; CIM-11 (en vigueur au 1er janvier 2022).
17. [S17] Nations unies. Résolution A/RES/70/1 (2015), objectif de développement durable n° 3.
18. [S18] Arrêtés du 3 juillet 2018 et du 28 avril 2026 fixant le calendrier de vaccination obligatoire (DOC-00070, DOC-00071).
