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
- 2026-11-19T02:05:12+00:00 — **Session d'audit scientifique (AUD-01, tenue conjointement avec AUD-02)** des dossiers du rédacteur DOS-05 : DOS-PEDI-0001 (déshydratations), DOS-PEDI-0002 (vaccinations et PEV algérien), DOS-PEDI-0003 (malnutrition), DOS-NEON-0001 (ictère), DOS-NEON-0002 (infections néonatales), avec le lot QCM `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/DOS-05.json` (60 QCM) et le lot de cas `20_CAS_CLINIQUES/lots/DOS-05.json` (10 cas). Lecture préalable de PROTOCOLE_AUDIT.md et de CONVENTIONS.md, puis des 5 dossiers en entier et des 2 lots.
- Textes officiels relus avec `pdftotext -layout` : DOC-00070 (arrêté du 03/07/2018), DOC-00071 (arrêté du 28/04/2026) et DOC-00076 (arrêté de 2014, remplacé). Les tableaux du calendrier du dossier DOS-PEDI-0002 leur sont **conformes**. Restent ouverts : VPO à la naissance (absent des arrêtés), arrêté modificatif intermédiaire de 2018 (non retrouvé), modalités HPV (non précisées par l'arrêté).
- Documents OMS acquis lus pour l'audit : Pocket book 2013 (DOC-00063), émaciation/œdème nutritionnel 2023 (DOC-00033), infections bactériennes graves 0–59 j 2024 (DOC-00052), PCIME 0–2 mois 2019 (DOC-00034), AWaRe 2022 (DOC-00039).
- 9 recherches web : NICE NG195, AAP 2022 (deux recherches), ESPGHAN 2014, NICE CG98, Kimberlin 2001, RBP SFN/SFP 2017, arrêté modificatif de 2018 (infructueuse), note OMS BCG 2018. WebFetch a échoué : nice.org.uk et renaissance.stonybrookmedicine.edu sont hors du réseau autorisé.
- Résultats (tous les dossiers en version 1.1) :
  - DOS-PEDI-0001 : 9 corrections (0 critique / 0 majeure / 9 mineures) → audite_corrections_requises.
  - DOS-PEDI-0002 : 6 corrections (0/1/5 ; majeure : BCG et VIH selon l'OMS 2018) → audite_corrections_requises.
  - DOS-PEDI-0003 : 16 corrections (1/3/12) → audite_corrections_requises.
    - **Critique** : amoxicilline orale de relais dans la MAS compliquée à 15 mg/kg/8 h au lieu de 25–40 mg/kg/8 h (Pocket book 2013).
    - Majeures : critères de sortie et d'hospitalisation actualisés selon l'OMS 2023 ; divergence erronée sur les solutés du choc.
  - DOS-NEON-0001 : 7 corrections (0/0/7) → audite_corrections_requises.
  - DOS-NEON-0002 : 11 corrections (0/3/8) → audite_corrections_requises.
    - Majeures : drapeaux rouges de NICE NG195 (la liste de CG149 était présentée comme actuelle) ; seuil fébrile OMS des infections graves (38 °C et non 37,5 °C) ; recommandations OMS 2024 à la place de celles de 2015.
- Lots (sauvegardés et réécrits avec `ecrire_json`, JSON validé) :
  - QCM : 7 corrigés (QCM-PEDI-0008, 0009, 0023, 0031, 0033 réécrit selon l'OMS 2023, 0034 ; QCM-NEON-0021) ; 55 audite_valide, 5 audite_corrections_requises (mention « à vérifier » résiduelle).
  - Cas : 3 corrigés (CAS-PEDI-0005, CAS-NEON-0001, CAS-NEON-0004) ; 7 audite_valide, 3 audite_corrections_requises.
- Rapports : `00_SYSTEME/agents/AUD-01/rapports/DOS-PEDI-0001.md` à `0003.md`, `DOS-NEON-0001.md`, `DOS-NEON-0002.md`. Aucune commande git.
