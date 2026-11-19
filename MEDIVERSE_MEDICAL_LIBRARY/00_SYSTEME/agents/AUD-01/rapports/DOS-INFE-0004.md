# Rapport d'audit — DOS-INFE-0004 « Paludisme : parasitologie, étiologie, diagnostic, prévention, traitement »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, indépendants du rédacteur (DOS-02, lot 2)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1) ; QCM-INFE-0214 à 0226 ; CAS-INFE-0203 et 0204 (`DOS-02-lot2.json`)
- **Verdict** : `audite_valide` — 0 erreur critique ; 1 erreur majeure corrigée ; 16 corrections mineures ; **0 marqueur `[POSOLOGIE À VÉRIFIER]` restant** (3 levés, plus le schéma horaire de l'artésunate)
- **Sauvegarde** : `00_SYSTEME/sauvegardes/20261119/07_MEDECINE_INTERNE/28_INFE_INFECTIOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-INFE-0004__PALUDISME.avant_audit.md`

## Vérifications sur les textes (pdftotext)
- **OMS, WHO guidelines for malaria, 10 septembre 2026 (DOC-00024)** : définition du paludisme grave (Glasgow < 11, Blantyre < 3, > 2 convulsions/24 h, acidose, glycémie < 2,2 mmol/L, Hb ≤ 5 g/dL chez l'enfant < 12 ans et < 7 g/dL chez l'adulte avec parasitémie > 10 000/µL, créatinine > 265 µmol/L, bilirubine > 50 µmol/L avec > 100 000/µL, OAP, saignement, choc, hyperparasitémie > 10 %) ; artésunate 2,4 mg/kg par dose, **3 mg/kg si < 20 kg**, au moins 24 h puis CTA de 3 jours, tous les trimestres de grossesse ; artéméther 3,2 puis 1,6 mg/kg ; quinine 20 mg de sel/kg puis 10 mg/kg/8 h, réduction d'un tiers à 48 h, ≤ 5 mg/kg/h, jamais en bolus ; hémolyse retardée (19 voyageurs, 7 % d'enfants) ; primaquine (0,5 mg/kg/j 14 ou 7 jours si G6PD > 30 % ; 1 mg/kg/j 7 jours si > 70 % ; recommandations de 2024) ; tafénoquine (Amérique du Sud) ; vaccins chez l'enfant vivant en zone d'endémie ; chimioprophylaxie : renvoi au guide des voyages internationaux, atovaquone-proguanil arrêtée peu après le retour, molécules suppressives ≥ 4 semaines. **Conformes.**
- **OMS, Pocket book of hospital care for children 2013 (DOC-00063) et Mémento 2015 (DOC-00062)** : artésunate 2,4 mg/kg IV ou IM **à l'admission, à 12 h et à 24 h, puis une fois par jour**.
- **OMS, International travel and health — Module 3 : Malaria, 2024** (téléchargé depuis IRIS pendant l'audit, lu) : tableau 1 (chimioprophylaxie) et tableau 3 (traitement), répulsifs, incubation ≥ 7 jours, perte de la semi-immunité après ≥ 6 mois hors zone d'endémie.
- **Communiqué OMS du 22 mai 2019** (relu sur who.int) : certification de l'Algérie, derniers cas autochtones en 2013, critère de 3 années, 2e pays de la Région africaine après Maurice ; découverte du parasite par Laveran « en Algérie en 1880 » (ville non précisée).
- QCM-INFE-0214 à 0226 et CAS-INFE-0203/0204 : réponses et explications exactes.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 15.1 (tableau de chimioprophylaxie) | Méfloquine « débutée 10 jours avant, poursuivie **3 semaines** après le retour » : schéma français non sourcé, en contradiction avec le principe énoncé au § 4.2 et au § 15.1 (molécules suppressives ≥ 4 semaines) et avec l'OMS ; marqueur de posologie sur tout le tableau | **Majeure** | Tableau refait selon l'OMS 2024 : atovaquone-proguanil 1 cp/j de la veille du départ à 7 jours après ; doxycycline 100 mg/j, 1 jour avant à 4 semaines après ; méfloquine 250 mg/semaine, ≥ 1 semaine (2–3 semaines) avant à 4 semaines après ; contre-indications ; divergence HCSP signalée `[À VÉRIFIER]` ; marqueur levé | S7 (OMS ITH 2024, tableau 1) |
| § 13.2 c | Schéma horaire de l'artésunate sous `[À VÉRIFIER]` | Mineure (levée) | H0, H12, H24 puis toutes les 24 h | S9 (Pocket book 2013) |
| § 13.2 b | Atovaquone-proguanil curatif sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | 4 cp à 250/100 mg/j pendant 3 jours (> 40 kg), avec repas ; CI si clairance < 30 mL/min ; pas seule en cas d'hyperparasitémie | S7 (tableau 3), S1 |
| § 13.2 b | Quinine orale sous `[POSOLOGIE À VÉRIFIER]` | Mineure (levée) | 8 mg base/kg × 3/j pendant 7 jours, + doxycycline ou clindamycine | S7 (tableau 3) |
| § 13.2 a | Prise de l'artéméther-luméfantrine avec un aliment gras `[À VÉRIFIER]` | Mineure | Sourcée (absorption de la luméfantrine) | S1 |
| § 15.1 | Répulsifs non précisés | Mineure | DEET, IR3535, icaridine, renouvellement 3–4 h ; concentrations `[À VÉRIFIER]` | S7 |
| § 15.2 | « Sans indication pour le voyageur » `[À VÉRIFIER]` | Mineure | Recommandation OMS limitée aux enfants vivant en zone d'endémie | S1 |
| § 4.2 | Incubation minimale `[À VÉRIFIER — SPILF]` | Mineure | ≥ 7 jours (OMS) | S7 |
| § 5 | Délai de perte de la prémunition `[À VÉRIFIER]` | Mineure | Séjour ≥ 6 mois hors zone d'endémie | S7 |
| § 10 | Hyperparasitémie sans gravité non chiffrée | Mineure | 4–10 % (> 2 % chez le non-immun) : surveillance, hospitalisation ; > 10 % = grave | S1 |
| § 2 | Laveran « à Constantine » présenté comme certain | Mineure | « En Algérie » (OMS) ; ville `[À VÉRIFIER]` | S3 |
| § 3.2 | Chiffres 2020 de presse insuffisamment signalés | Mineure | Mention explicite « non confirmés par une publication officielle » | S6 |
| § 13.4, § 15.1, § 21 | Protocoles nationaux non qualifiés | Mineure | « Protocole national de traitement » et « schéma national de chimioprophylaxie » **non retrouvés** | Recherche (audit) |
| § 21 | Ligne « chimioprophylaxie » imprécise | Mineure | OMS 2024 vs HCSP (divergence datée) | S7, S8 |
| YAML, § 22 | S7 non consultée ; pas de source du schéma horaire | Mineure | S7 remplacée par l'ITH 2024 (lue) ; S9 ajoutée | — |
| § 17 et CAS-INFE-0203 | `[À VÉRIFIER — schéma horaire]` | Mineure (levée) | H12, H24 puis /24 h | S9 |
| CAS-INFE-0204 ; QCM-INFE-0225 | « OMS 2024 » imprécis ; explication renvoyant à des recommandations non lues | Mineure | Datation précisée ; explication sourcée (OMS 2024) | S1, S7 |

## Reste à faire (sans incidence sur le verdict)
1. Lire la SPILF 2017 (texte intégral) : seuils de gravité français (hyperparasitémie), critères d'hospitalisation, calendrier des frottis de contrôle (`[À VÉRIFIER]` conservés aux § 8.3, 9.1, 12, 13.3 b, 14, 21).
2. HCSP, recommandations aux voyageurs (édition 2026) : délais français de la méfloquine (S8 non vérifiée).
3. Données officielles algériennes (INSP, programme de prévention de la réintroduction, entomologie, sécurité transfusionnelle) : non retrouvées.
