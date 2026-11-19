# Rapport d'audit — DOS-HEMA-0006 « Transfusion de sang et dérivés : indications et accidents »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-14
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_corrections_requises`** (0 critique, 1 majeure, 10 mineures ; 1 marqueur de posologie restant sur 3)

## Documents consultés pendant l'audit
- Résumés PubMed : AABB 2023, globules rouges (PMID 37824153) et AABB/ICTMG 2025, plaquettes (PMID 40440268) : seuils du dossier **conformes** (7 g/dL ; 7,5 en chirurgie cardiaque ; 8 en chirurgie orthopédique ou maladie cardiovasculaire préexistante ; plaquettes < 10, 20, 25, 50 G/L selon le contexte).
- HAS/ANSM 2014, transfusion de globules rouges (recommandations, PDF lu) ; HAS 2015, plaquettes (argumentaire, PDF lu) ; ANSM/HAS 2012, plasma thérapeutique (recommandations et argumentaire, PDF lus).
- Loi algérienne n° 18-11 (document acquis) : art. 258–264 et 368–369 relus, citations exactes.
- Recherche web : décret exécutif n° 09-258 du 11 août 2009 relatif à l'Agence nationale du sang (titre repéré dans le sommaire du JORADP n° 47 ; texte non lu) ; décret de 1995 non confirmé.

## Points demandés
- Seuils de CGR : AABB 2023 = 7 g/dL ; **7,5 g/dL en chirurgie cardiaque** et 8 g/dL en chirurgie orthopédique ou cardiopathie préexistante (le dossier était exact) ; HAS 2014 ajoutée (8 g/dL en hématologie, 10 g/dL en cas d'insuffisance coronarienne aiguë).
- Plasma : 10–15 mL/kg (ANSM/HAS 2012) ; compatibilité ABO isogroupe, à défaut « en miroir » (AB universel, O réservé au receveur O).
- Plaquettes : 0,5–0,7 × 10¹¹/10 kg (HAS 2015) ; un CPA ≥ 2 × 10¹¹ plaquettes.
- TRALI (≤ 6 h, définition 2019, types I/II) et TACO (≤ 12 h, ISBT révisée) : conformes.
- Agence nationale du sang : sourcée (art. 264 de la loi 18-11) ; antériorité réglementaire (décret de 2009) signalée.

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 13.2, 21 | Seuils HAS 2014 non détaillés `[À VÉRIFIER]` alors qu'ils divergent de l'AABB (8 g/dL en hématologie, 10 g/dL dans l'insuffisance coronarienne aiguë, 8–9 g/dL en périopératoire chez le patient cardiovasculaire) | **Majeure** | Seuils HAS par population ; nouvelle ligne de divergence AABB/HAS | HAS 2014 [S3] |
| 13.3 | Dose plaquettaire : marqueur | Mineure | 0,5–0,7 × 10¹¹/10 kg ; néonatologie 0,1–0,2 × 10¹¹/kg ; CPA ≥ 2 × 10¹¹ ; marqueur levé | HAS 2015 [S4] |
| 13.4 | Dose de plasma : marqueur | Mineure | 10–15 mL/kg (accord professionnel), 15 mL/kg en chirurgie cardiaque, 40–60 mL/kg dans les microangiopathies ; marqueur levé | ANSM/HAS 2012 [S18] |
| 6 | Indications du plasma `[À VÉRIFIER]` | Mineure | Pas de plasma préventif d'un trouble modéré sans saignement ni de remplissage | [S18] |
| 8.4 | Règle isogroupe du plasma absente | Mineure | Isogroupe d'abord, compatibilité en miroir à défaut | [S18] |
| 8.1 | Validité de la RAI `[À VÉRIFIER]` | Mineure | France : 72 h si transfusion, grossesse ou greffe dans les 6 mois, sinon 21 jours ; règle algérienne à vérifier | [S3] |
| 7.1 | Conservation des CGR `[À VÉRIFIER]` | Mineure | +2 à +6 °C, 42 jours en SAG-mannitol (France) | [S3] |
| 8.6 | Délai de transfusion `[À VÉRIFIER]` | Mineure | BSH : fin dans les 4 h ; France : début dans les 6 h suivant l'arrivée dans le service | [S6, S3] |
| 2, 13.7, 22 | « La loi 18-11 crée l'Agence nationale du sang » sans mention de l'antériorité | Mineure | Art. 264 cité ; décret exécutif n° 09-258 de 2009 signalé (`verifiee: false`) | [S11, S19] |
| 17 (cas) | Seuil HAS en insuffisance cardiaque non mentionné | Mineure | 10 g/dL en périopératoire (HAS 2014) | [S3] |
| 22 | S3/S4 « contenu non lu » ; sources manquantes | Mineure | S3 et S4 lus ; S18 et S19 ajoutées ; points restants actualisés | — |

## Lots (QCM, cas)
- 12 QCM (QCM-HEMA-1401 à 1412) exacts, `audite_valide`.
- CAS-HEMA-1401 (incompatibilité ABO) : conforme, `audite_valide`.
- CAS-HEMA-1402 (TRALI) : distinction TRALI de type I / type II ajoutée (contexte hémorragique) ; `audite_valide`.

## Restant à faire (motifs du verdict)
1. Marqueur restant : posologie du fibrinogène (concentré, cryoprécipité) et cibles chiffrées du guide européen 2023 (texte non relu).
2. Textes algériens : décret de 2009 et texte d'application de l'art. 264 ; organisation de l'hémovigilance ; tests de qualification des dons ; validité de la RAI, contrôle ultime au lit, durées de conservation et délais.
3. Recommandations cardiologiques sur le seuil transfusionnel dans le SCA après MINT.
4. Relecture humaine qualifiée.
