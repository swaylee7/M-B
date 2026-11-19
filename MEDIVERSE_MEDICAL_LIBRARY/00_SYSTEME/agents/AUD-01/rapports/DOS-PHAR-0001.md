# Rapport d'audit — DOS-PHAR-0001 « Antibiotiques : classification, principes et règles d'utilisation, résistances bactériennes »

- Date : 2026-11-19 — Auditeur : AUD-01 / AUD-02 (IA), session d'audit du lot DOS-14
- Version auditée : 1.0 → version corrigée : 1.1
- **Verdict : `audite_corrections_requises`** (2 critiques — une même erreur de dose en deux endroits —, 1 majeure, 7 mineures ; 1 marqueur de posologie restant sur 2)

## Documents consultés pendant l'audit
- Liste modèle OMS 2025, section 6.2 (document acquis, pdftotext) : classement AWaRe molécule par molécule.
- Livre AWaRe de l'OMS 2022 (document acquis, pdftotext) : chapitres sepsis de l'adulte (24), infection urinaire basse (23) et haute (34), méningite (26), neutropénie fébrile (39), antibioprophylaxie chirurgicale (40), fiche fosfomycine IV.
- Recherche web : rapport AARN récent (non trouvé ; participation de l'Algérie au GLASS depuis 2020, Radio Algérie).
- PubMed : SSC 2026 (PMID 41870560, sans résumé).

## Tableau des corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| 13.2 (tableau des posologies) | Méropénème « 1 g toutes les 8 h » pour les infections graves, attribué au livre AWaRe ; le livre retient **2 g toutes les 8 h dans le sepsis** de l'adulte (1 g/8 h dans la neutropénie fébrile et les infections intra-abdominales) : sous-dosage potentiel | **Critique** | Posologies par indication ; méningite de l'adulte 2 g/8 h attribuée au RCP (le livre ne retient le méropénème en méningite que chez le nouveau-né) | Livre AWaRe [S1] |
| 17 (cas commenté, Q2) | Même erreur : choc septique d'origine urinaire, « méropénème 1 g/8 h » présenté comme posologie AWaRe | **Critique** | 2 g/8 h ; première dose non réduite, adaptation rénale ensuite | [S1] |
| 7.1 (tableau des familles) | Fosfomycine orale classée **Access** : elle n'est **pas inscrite** sur la liste modèle 2025 (seule la forme IV, **Reserve**) ni traitée dans le livre AWaRe | **Majeure** | Corrigé ; classement de la forme orale dans la base AWaRe (Watch) signalé `[À VÉRIFIER]` | [S1, S2] |
| 7.1 | Céfépime noté « Watch (liste complémentaire) » | Mineure | Céfépime non inscrit sur la liste 2025 ; ceftazidime en liste complémentaire | [S2] |
| 13.2 | Céfazoline (antibioprophylaxie) : marqueur | Mineure | 2 g en dose unique dans les 120 min avant l'incision ; réinjection si intervention prolongée ou pertes importantes ; marqueur levé | Livre AWaRe ch. 40 [S1], OMS ISO [S16] |
| 3.3 | AARN : rien sur l'état de la surveillance | Mineure | Participation au GLASS depuis 2020 ; aucun rapport AARN récent localisé ; aucun taux national cité | Radio Algérie [S19] |
| 1 | « I » présenté selon la seule terminologie EUCAST | Mineure | Précision : « intermédiaire » dans la terminologie CLSI | — |
| 8.1 | SSC 2021 présentée sans mention de sa mise à jour | Mineure (actualité) | SSC 2026 signalée (contenu non analysé) | [S18, S20] |
| 22 | Références | Mineure | S18 notée « remplacée » ; S19 et S20 ajoutées ; points restants actualisés | — |
| Bandeau | Statut | Mineure | Mis à jour | — |

Vérifications sans anomalie : classement AWaRe des autres molécules (amoxicilline, céfalexine, céfazoline, cloxacilline, clindamycine, doxycycline, gentamicine, amikacine, nitrofurantoïne, cotrimoxazole, spectinomycine : Access ; céfuroxime, ceftriaxone, céfotaxime, céfixime, ciprofloxacine, macrolides, pipéracilline-tazobactam, vancomycine : Watch ; méropénème et ceftazidime : Watch, liste complémentaire ; céfidérocol, ceftazidime-avibactam, ceftolozane-tazobactam, colistine, fosfomycine IV, linézolide, méropénème-vaborbactam, plazomicine, polymyxine B : Reserve) ; aztréonam et daptomycine non inscrits ; posologies AWaRe de l'amoxicilline, de la nitrofurantoïne, du cotrimoxazole, de l'amoxicilline-acide clavulanique, de la ceftriaxone, de la gentamicine, de l'amikacine et de la vancomycine ; cibles ONU 2024 (70 % d'Access, −10 % de décès) ; stratégies IDSA 2024 / ESCMID 2022 par mécanisme.

## Lots (QCM, cas)
- 12 QCM (QCM-PHAR-1401 à 1412) : exacts, `audite_valide`.
- **CAS-PHAR-1401** (cystite) : fosfomycine-trométamol présentée comme Access (majeure) → corrigé ; `audite_corrections_requises` (classement AWaRe de la forme orale et référentiel algérien à vérifier).
- CAS-PHAR-1402 (PAVM à OXA-48) : marqueur levé (ceftazidime-avibactam 2,5 g toutes les 8 h en perfusion prolongée si clairance > 50 mL/min, RCP et IDSA 2024) ; `audite_valide`.

## Restant à faire (motifs du verdict)
1. Marqueur restant : cibles de dosage de la vancomycine (résiduelle ou ASC) selon le protocole local.
2. Dernier rapport AARN (taux nationaux) ; contenu du plan stratégique national RAM 2024-2028.
3. SSC 2026 : délai de l'antibiothérapie, associations, durées.
4. Classement de la fosfomycine orale, de l'aztréonam et de la daptomycine dans la base de classification AWaRe en vigueur.
5. Disponibilité en Algérie des molécules Reserve et de la témocilline ; référentiel algérien de la cystite.
6. Relecture humaine qualifiée.
