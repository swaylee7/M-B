# Journal — ANA-07

Mission : Catalogue vérifié des ouvrages de référence et structuration des contenus — Médecine interne-gériatrie

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19T01:25:21+00:00 — poste couvert par ANA-01 (catalogue consolidé, 440 ouvrages en 5 lots ANA-*.json) ; voir journal ANA-01.

## Volet encyclopédie — agent ENC-1 (postes ANA-07 à ANA-18), 2026-11-19
- Lecture : CONVENTIONS.md, schemas/pathologie.md, config/specialites.yaml, programme_residanat.json (314 items).
- Méthode : saisie dans un format source compact (clés symboliques), puis script de construction qui attribue les ids `PATH-<CODE>-nnnn` par spécialité, convertit les items (RES-MED/CHI/SF), valide sous-spécialités, catégories, codes CIM-10 (format) et items, et résout `pathologies_liees` (liens vers des ids inexistants retirés). Écriture via `commun.ecrire_json` (sauvegarde + journal global).
- Lot 1 écrit : `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-1-CARD-PNEU-MINT-IMPA.json` (CARD 68, PNEU 50, MINT 34, IMPA 25 = 177) — liens inter-lots à compléter à la reconstruction finale.
- Lot 2 écrit : `ENC-1-GAST-HEPA-NEPH.json` (GAST 49, HEPA 48, NEPH 52).
- Lot 3 écrit : `ENC-1-NEUR-PSYC-GERI.json` (NEUR, PSYC, GERI).
- Lot 4 écrit : `ENC-1-DERM-RHUM-GENE.json`.
