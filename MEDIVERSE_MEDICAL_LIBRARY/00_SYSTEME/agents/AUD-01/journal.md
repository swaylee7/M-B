# Journal — AUD-01

Mission : Audit scientifique des dossiers (exactitude, cohérence, actualité)

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19T01:56:59+00:00 — Audit scientifique conjoint (AUD-01/02/04) des dossiers DOS-02 (DOS-INFE-0001, DOS-INFE-0002, DOS-PNEU-0001, DOS-PNEU-0002, DOS-PNEU-0003) ; rapports dans 00_SYSTEME/agents/AUD-02/rapports/ ; verdict audite_corrections_requises pour les 5 dossiers.
- 2026-11-19T01:45+00:00 — **Session d'audit scientifique (AUD-01, tenu conjointement avec AUD-02)** des dossiers du rédacteur DOS-01 : DOS-CARD-0001 à 0005, avec le lot QCM `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/DOS-01.json` (60 QCM) et le lot cas `20_CAS_CLINIQUES/lots/DOS-01.json` (10 cas). J'ai d'abord lu PROTOCOLE_AUDIT.md et CONVENTIONS.md, puis l'intégralité des 5 dossiers et des 2 lots.
- Sauvegardes avant modification : `00_SYSTEME/sauvegardes/20261119/` pour les 5 dossiers ; les lots étaient déjà sauvegardés à l'identique.
- 9 recherches web au total. Elles ont servi à recouper le contenu ESC 2026 de l'IC (sources secondaires concordantes ; texte intégral inaccessible) et à vérifier STRONG-HF (Lancet 2022;400:1938), Collet ESC 2020 (ehaa575), les chiffres de Moussouni 2022 et l'aspirine dans la pré-éclampsie (ESC/ESH 2018). Le tableau des schémas probabilistes de l'EI selon l'ESC 2023 et le schéma de la bromocriptine n'ont pas été trouvés. WebFetch était bloqué : escardio.org et tctmd.com sont hors du réseau autorisé.
- Résultats :
  - DOS-CARD-0001 : 11 corrections (1 majeure : contre-indication de l'ivabradine) → audite_corrections_requises, version 1.1.
  - DOS-CARD-0002 : 10 corrections mineures → **audite_valide**, version 1.1.
  - DOS-CARD-0003 : 8 corrections mineures → **audite_valide**, version 1.1.
  - DOS-CARD-0004 : 8 corrections mineures → audite_corrections_requises (HNF), version 1.1.
  - DOS-CARD-0005 : 12 corrections mineures → audite_corrections_requises (antibiothérapie probabiliste ESC 2023, prophylaxie du RAA), version 1.1.
  - Aucune erreur critique.
- Lots JSON corrigés avec `ecrire_json` (JSON validé avec python3) : 1 QCM précisé (QCM-CARD-0012) ; 6 cas corrigés (CAS-CARD-0001, 0002, 0004, 0005, 0008, 0010) ; champ `audit` et `statut` ajoutés à chaque élément.
- Rapports : `00_SYSTEME/agents/AUD-01/rapports/DOS-CARD-0001.md` à `DOS-CARD-0005.md`. Aucune commande git.
