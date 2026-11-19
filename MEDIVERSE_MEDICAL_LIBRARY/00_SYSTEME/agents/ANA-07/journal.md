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
- Lot 5 écrit : `ENC-1-ENDO-DIAB-ONCO.json`.
- Lot 6 écrit : `ENC-1-INFE-PARA-HEMA.json` (INFE 60, PARA 35, HEMA 58).
- Reconstruction finale des 6 lots avec résolution des liens inter-lots ; ajouts de couverture d'items (vertiges C047, ostéomyélite C038, génétique S023/S025).
- Validation indépendante (python3) : 6 JSON valides, 885 ids uniques `PATH-<CODE>-nnnn`, 3 725 liens `pathologies_liees` tous résolus (liens vers des pathologies hors périmètre retirés : uvéite, appendicite, nocardiose, cyphoscoliose, conjonctivite allergique), items tous présents dans programme_residanat.json, aucune fiche sans lien.
- Bilan : CARD 68, PNEU 50, MINT 34, IMPA 25, GAST 49, HEPA 48, NEPH 52, NEUR 72, PSYC 50, GERI 19, DERM 65, RHUM 43, GENE 39, ENDO 53, DIAB 21, ONCO 44, INFE 60, PARA 35, HEMA 58 = 885 ; maladies rares 220 ; CIM-10 renseigné 736 (83,2 %) ; 562 pathologies reliées à ≥ 1 item.
- Règles appliquées : CIM-10 OMS seulement si certain (null pour les entités composites, codes spécifiques à la CIM-10-CM, ou incertains : ex. dengue, SJS/Lyell, complications du diabète, cholangiocarcinome) ; aucune posologie ; contenu standard et concis ; `dossier: null`, `statut: referentiel_a_auditer`.
- Limites : codes CIM-10 non vérifiés en ligne pendant la session (connaissance établie) ; 6 fiches sans sous-spécialité adaptée dans specialites.yaml (IRC, MNI, CMV, encéphalite herpétique, VPPB, névrite vestibulaire) ; périmètre limité aux 19 spécialités demandées ; indexer.py non lancé (fusion laissée au pipeline).
