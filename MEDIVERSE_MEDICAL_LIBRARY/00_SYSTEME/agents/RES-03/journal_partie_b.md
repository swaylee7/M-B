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
