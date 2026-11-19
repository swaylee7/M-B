# Journal — RES-03 (partie b)

Mission : banque de QCM originaux de médecine du résidanat algérien — partie b
(60 items : RES-MED-102 à RES-MED-174, liste fixée par la mission ; 3 QCM/item ≈ 180 QCM).
Plage d'ids réservée : QCM-<CODE>-6001…6999. Lots : `RES-03-c.json` (items 102–137) et `RES-03-d.json` (items 138–174).
La partie a (items 001–098, ids 3001–3999, fichiers `journal.md`, `etat.json`, `RES-03-a/b.json`) est traitée par un autre agent : non modifiée ici.

- 2026-11-19 — démarrage : lecture de CONVENTIONS.md, schéma `schemas/qcm.md`, programme (60 items cibles, intitulés et spécialités),
  catalogue des recommandations (340) et des ouvrages (449), registre des acquisitions (102 documents).
- 2026-11-19 — lecture (pdftotext) des textes officiels algériens acquis : loi 18-11 relative à la santé (DOC-00074 : art. 11–28, 37–48,
  49–58, 69–80, 97–100, 126–139, 169, 178, 198–204, 258–264, 265–301, 329–338, 343–353, 362–369, 400–420), décret exécutif 22-250 (MDO, DOC-00072),
  décret exécutif 22-178 (certificat médical de décès, DOC-00077), arrêtés du calendrier vaccinal 2018 et 2026 (DOC-00070, DOC-00071),
  décret exécutif 24-366 (examens prénuptiaux, DOC-00075) ; lecture du guide ATS 2020 sarcoïdose (DOC-00102).
- 2026-11-19 — outil d'assemblage (définitions compactes Python → JSON, préfixe Vrai/Faux automatique, ids séquentiels 6001…) et validateur dans le scratchpad de session.
- 2026-11-19 — rédaction des 180 QCM (60 items × 3) en 7 fichiers de définitions ; vérification de la cohérence des gaz du sang
  (Henderson-Hasselbalch, formule de Winter) et des calculs (TMI, ratio de mortalité maternelle, incidence cumulée, RR, OR, différence de risques,
  fractions attribuables, seuil d'immunité collective, RDCR, QALY, loi de l'inverse du carré) — chaque calcul refait deux fois.
- 2026-11-19 — correction : le tableau du calendrier vaccinal complété en 2026 (DOC-00071) ajoute le VPO à 2 mois (lecture de la mise en page
  du JO, concordante avec la fiche REC-0002) ; la proposition correspondante a été réécrite.
- 2026-11-19 — diversification : 20 QCM ramenés à 2 réponses exactes, 3 à 5 réponses exactes ; 3 énoncés réécrits (doublons avec un autre lot
  ou internes) ; permutation déterministe des propositions (graine = CRC32 de l'énoncé ; QCS à options numériques laissés en ordre croissant).
- 2026-11-19 — écriture via `commun.ecrire_json` : `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/RES-03-c.json` (75 QCM, items 102–137,
  ids 6001–6075) et `RES-03-d.json` (105 QCM, items 138–174, ids 6076–6180). Validation python3 : 5 propositions A–E, réponses ⊂ propositions,
  QCS à réponse unique, ids uniques sur l'ensemble des lots (1 409 ids), items et spécialités existants, préfixes Vrai/Faux concordants,
  sources datées, aucun énoncé en double. Entrée `creation_qcm` ajoutée au journal global.

## Bilan
- 180 QCM : 153 QCM à réponses multiples, 27 QCS (15 %). Nombre de réponses exactes (QCM) : 2 → 20, 3 → 57, 4 → 73, 5 → 3.
- Difficulté : 1 → 25, 2 → 122, 3 → 33. Bonnes réponses par lettre : A 96, B 106, C 115, D 119, E 109.
- Par module : rhumatologie-MPR 12, réanimation 6, hématologie clinique 6, néphrologie 21, épidémiologie et médecine préventive 30,
  médecine légale 12, médecine du travail 21, psychiatrie 15, maladies systémiques 9, personnes âgées 21, thérapeutique 27.
- Législation algérienne : uniquement à partir des textes acquis et lus (DOC-00070, 00071, 00072, 00074, 00075, 00077), avec articles cités.
- Aucune question attribuée à une annale ; `origine: originale_mediverse` partout ; statut `brouillon_a_auditer`.

## Points à auditer
1. ERC/AHA 2025 (REC-0294/0295, non relus dans la session) : contenus supposés inchangés depuis 2021 — adrénaline après le 3e choc (ERC) /
   2e choc (AHA), pas d'adrénaline < 30 °C, cible SpO2 94–98 % après RACS, 5 insufflations initiales chez le noyé (QCM-MINT_REA-6014/6015, URGE-6016/6018).
2. Calendrier vaccinal 2026 (QCM-SPUB-6064) : VPO à 2 mois déduit de la mise en page du tableau du JORADP n°36/2026 — vérifier sur l'image du PDF.
3. HAS 2021 dénutrition ≥ 70 ans (QCM-GERI-6148/6150) : seuils IMC < 22 (sévère < 20), perte ≥ 5 %/1 mois ou ≥ 10 %/6 mois, albuminémie < 30 g/L
   pour la forme sévère — non relus dans le texte HAS.
4. KDIGO 2026 anémie (QCM-NEPH-6035) : « ne pas viser Hb > 13 g/dL sous ASE » repris du principe KDIGO 2012 — confirmer dans la version 2026.
5. OMS 2020 activité physique (QCM-GERI-6141 : intensité modérée = 5–6/10) et OMS 2024 sevrage tabagique (cigarette électronique non recommandée, QCM-EPID-6057).
6. AT/MP (QCM-MTRA-6088) : la loi 83-13 sur les accidents du travail n'est pas acquise ; l'assimilation de l'accident de trajet est présentée
   comme un principe général [À VÉRIFIER dans le texte].
7. Responsabilité médicale (QCM-MLEG-6082/6084) : « obligation de moyens », responsabilité administrative pour faute de service = principes
   doctrinaux, hors textes acquis (seuls les articles de la loi 18-11 sont cités comme droit positif).
8. Classification CIRC (QCM-MTRA-6096) : suppression du groupe 4 (préambule 2019) — à confirmer.
9. Équivalences de corticoïdes en mg (QCM-PHAR-6157) : seules valeurs de type posologique, équivalences pharmacologiques usuelles.
