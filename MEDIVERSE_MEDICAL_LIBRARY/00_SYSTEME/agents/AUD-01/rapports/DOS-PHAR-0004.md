# Rapport d'audit — DOS-PHAR-0004 « Antalgiques : principes et règles d'utilisation »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-14
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_corrections_requises`** (0 critique, 1 majeure, 10 mineures ; 2 marqueurs de posologie restants sur 4)

## Documents consultés pendant l'audit
- OMS 2018, douleur cancéreuse (document acquis, pdftotext), annexe 6 : profils de l'aspirine, de la codéine, du fentanyl, de l'hydromorphone, de l'ibuprofène, de la méthadone, de la morphine, de la naloxone, de l'oxycodone et du paracétamol ; tableau A6.1 (doses de départ) ; tableaux A6.2 à A6.4 (équianalgésie, ratios de voie) ; règle de réduction de 50 % lors d'une rotation.
- HAS, fiche mémo « Prise en charge médicamenteuse de la douleur chez l'enfant : alternatives à la codéine » (janvier 2016), téléchargée et lue (préambule ANSM 2013, tableau des posologies, propositions par situation clinique).
- Résumé PubMed de Finnerup 2015 (NeuPSIG).

## Vérification des posologies du dossier (conformes à l'OMS 2018)
Paracétamol (0,5–1 g/4–6 h, max 4 g/j ; 3 g/j si facteur de risque ; IV 15 mg/kg entre 10 et 50 kg ; intervalle ≥ 6 h si clairance < 30) ; ibuprofène 400–800 mg/8 h (tableau A6.1) ; aspirine 300–900 mg/4–6 h, max 4 g ; codéine 30–60 mg/4 h, max 240 mg/j ; morphine orale 5 mg/4 h, IV/SC 2 mg/4 h (naïf), douleur aiguë 2–10 mg/4 h, orale ≈ 2 × parentérale ; fentanyl TD 12–25 µg/h ; amitriptyline 10–25 mg, max 100 mg ; naloxone 0,08–0,12 mg IV toutes les 2–3 min puis toutes les 20–60 min ou perfusion ; puissances relatives (codéine 1/10, oxycodone 1,5 [2], hydromorphone 4–5 [5–7,5], fentanyl TD 100 [150], buprénorphine SL 80) ; ratios oral → SC/IV (morphine 2:1, hydromorphone 3:1, morphine → hydromorphone parentérale 10:1, morphine → fentanyl 100–150:1). Aucune erreur de dose.

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 10.1 | Aucune posologie pédiatrique (objectif pédagogique 7) ; restrictions de la codéine non sourcées | **Majeure** (lacune) | Paracétamol 60 mg/kg/j en 4 prises (max 80 mg/kg/j) ; ibuprofène 20–30 mg/kg/j en 3–4 prises (max 400 mg/prise, dès 3 mois) ; tramadol 1 (à 2) mg/kg/prise toutes les 6–8 h (≥ 3 ans, max 100 mg/prise, 400 mg/j) ; morphine orale 0,2 mg/kg/prise × 6/j (0,1 mg/kg avant 1 an) ; association plutôt qu'alternance | HAS 2016 [S13] |
| 10.1 | Codéine : « restreinte dans de nombreux pays » `[À VÉRIFIER]` | Mineure | ANSM 2013 : pas avant 12 ans, ni après amygdalectomie/adénoïdectomie, ni pendant l'allaitement ; statut algérien à vérifier | [S13] |
| 13.3 | Oxycodone, hydromorphone : marqueur | Mineure | Doses de départ OMS (oxycodone LI 2,5–5 mg/4 h, LP 10 mg/12 h ; hydromorphone 1–4 mg/4 h PO, 0,3–0,7 mg SC/IV) ; marqueur levé | [S1] |
| 13.3 | Tramadol, gabapentine, prégabaline, duloxétine : marqueur | Mineure | Doses efficaces NeuPSIG (tramadol 200–400 mg/j ; gabapentine 1 200–3 600 mg/j en 3 prises ; prégabaline 300–600 mg/j en 2 prises ; duloxétine 60–120 mg/j) ; réduction rénale des gabapentinoïdes ; marqueur levé | [S6] |
| 12.2 | AINS « contre-indiqués au 3e trimestre (≥ 24 SA) » : incohérent (24 SA = début du 6e mois) | Mineure | « à partir du 6e mois (≥ 24 SA) » | — |
| 17 (cas) | Rotation vers l'oxycodone : marqueur ; accumulation rénale de l'oxycodone non signalée | Mineure | Calcul indicatif d'après l'OMS ; clairance ≈ 35 mL/min ; excrétion de l'oxycodone retardée en insuffisance rénale ; avis soins palliatifs ; marqueur levé | [S1] |
| 21 | Ratio morphine orale/IV : seule la convention OMS (2:1) | Mineure | Divergence avec l'enseignement français (3:1 pour l'IV) `[À VÉRIFIER — référentiel français]` | [S1] |
| 21 | Codéine chez l'enfant | Mineure | Divergence ANSM/HAS vs liste OMS | [S13, S2] |
| 13.3 | Amitriptyline chez le sujet âgé | Mineure | Mention des critères de Beers | [S8] |
| 22 | Source pédiatrique absente | Mineure | S13 ajoutée ; points restants actualisés | — |
| Bandeau | Statut | Mineure | Mis à jour | — |

## Lots (QCM, cas)
- 12 QCM (QCM-PHAR-1437 à 1448) exacts, `audite_valide`.
- CAS-PHAR-1407 (amygdalectomie) : marqueur levé (posologies HAS 2016 à 20 kg ; conduite en cas de SAOS ; restrictions ANSM 2013) ; `audite_valide`.
- CAS-PHAR-1408 (titration, voie SC) : calculs conformes à l'OMS (90 mg PO → 45 mg/24 h SC ; interdoses ≈ 4–7,5 mg) ; marqueur levé ; convention française de l'IV mentionnée ; `audite_valide`.

## Restant à faire (motifs du verdict)
1. Marqueurs restants : titration de la morphine IV aux urgences (protocole) ; méthylnaltrexone (RCP).
2. Statut réglementaire de la codéine et du tramadol en Algérie ; réglementation des stupéfiants.
3. Référence ANSM de la contre-indication des AINS à partir de 24 SA ; seuil du DN4 ; ratio oral/IV de la morphine dans les référentiels français.
4. Relecture humaine qualifiée.
