# Journal — AUD-02

Mission : Audit des posologies et contre-indications

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19T01:56:59+00:00 — Audit des dossiers DOS-02 (posologies, contre-indications) : DOS-INFE-0001, DOS-INFE-0002, DOS-PNEU-0001, DOS-PNEU-0002, DOS-PNEU-0003, avec leurs QCM (lot DOS-02, 62 QCM) et cas (lot DOS-02, 10 cas). Protocole PROTOCOLE_AUDIT.md suivi.
- 2026-11-19T01:56:59+00:00 — Recherches web : 18 (SPILF 2018, ESCMID 2016, OMS 2025, NICE NG240, de Gans 2002, van de Beek 2004, Tunkel 2004, Ioannina 2007, OMS 2006 et aide-mémoire, Cochrane 2012, Solís 2012, Pappas 2005/2006, Dean 2012, instruction algérienne n°07/2024, tranches de poids OMS, Nahid 2016/Saukkonen 2006, GINA 2025, ERS/ESICM 2023). WebFetch impossible (infectiologie.com, ncbi.nlm.nih.gov, sapp.dz non résolus).
- 2026-11-19T01:56:59+00:00 — Erreurs critiques (dose) : aucune. Majeures corrigées : indications de la dexaméthasone (SPILF 2018 : méningocoque de l'adulte, non-indication listériose/immunodéprimé, rattrapage ≤ 12 h) et cas clinique associé ; présentation du consensus d'Ioannina (doxycycline-rifampicine également schéma optimal) ; contenu de l'instruction algérienne n°07/2024 présenté comme établi (reformulé « selon les extraits disponibles, à confirmer »).
- 2026-11-19T01:56:59+00:00 — Posologies : gentamicine (Listeria) 5 mg/kg/j ; doses françaises de C3G et durées méningocoque/pneumocoque confirmées ; marqueurs levés (Z/E maxima ATS, tableaux CSI GINA, MART adulte, doses faibles ≤ 5 ans) ; exacerbation pédiatrique complétée (marqueurs conservés).
- 2026-11-19T01:56:59+00:00 — Verdicts : les 5 dossiers en audite_corrections_requises (v1.1) ; corrections 14 / 12 / 9 / 4 / 5. Rapports : AUD-02/rapports/DOS-*.md. Lots JSON corrigés via commun.ecrire_json (sauvegarde 00_SYSTEME/sauvegardes/20261119/) et validés (python3 json + valider.py : 0 erreur).
- 2026-11-19T01:45+00:00 — **Session d'audit des posologies et contre-indications (AUD-02, tenu conjointement avec AUD-01)** des dossiers DOS-CARD-0001 à 0005 et des lots QCM et cas DOS-01. Les rapports sont communs avec AUD-01 : `00_SYSTEME/agents/AUD-01/rapports/DOS-CARD-000N.md`.
- Les postes suivants ont été confrontés aux tableaux ESC et aux RCP :
  - antithrombotiques : aspirine, prasugrel, ticagrélor, clopidogrel, HNF, énoxaparine, fondaparinux, bivalirudine ;
  - ténectéplase selon le poids, altéplase, rétéplase, streptokinase ;
  - antihypertenseurs IV ;
  - fer IV ;
  - inotropes et vasopresseurs ;
  - diurétiques ;
  - doses initiales et cibles des IEC, ARNI, BB, ARM et iSGLT2 ;
  - antibiothérapies de l'EI (curatives et EI à hémocultures négatives) ;
  - antibioprophylaxie.
- **Erreur majeure corrigée** : contre-indication de l'ivabradine donnée à « FC < 60/min » au lieu de « FC de repos < 70/min » (DOS-CARD-0001). La rifampicine sur prothèse a été complétée (900–1 200 mg/j en 2–3 prises). Aucune erreur de dose critique n'a été trouvée.
- Marqueurs `[POSOLOGIE À VÉRIFIER]` dans les dossiers : 15 → 4 (12 levés avec leur source nommée ; 1 marqueur générique converti en marqueur explicite). Restent :
  - bromocriptine (0001) ;
  - HNF IV en attente de coronarographie (0004) ;
  - antibiothérapie probabiliste ESC 2023 et prophylaxie secondaire du RAA (0005).
- Dans les cas : 4 → 1 (reste l'adaptation à l'hémodialyse, CAS-CARD-0009).
- 19 corrections de posologie ou de contre-indication au total. Aucune commande git.
- 2026-11-19T02:05:12+00:00 — **Session d'audit des posologies (AUD-02, tenue conjointement avec AUD-01)** des dossiers DOS-PEDI-0001 à 0003 et DOS-NEON-0001 à 0002 et des lots DOS-05. Rapports communs : `00_SYSTEME/agents/AUD-01/rapports/`.
- Postes confrontés aux sources : plans A, B et C de l'OMS ; SRO et zinc ; ReSoMal ; remplissage du malnutri ; F-75 et F-100 ; ATPE ; antibiothérapie de la MAS ; vitamine A, acide folique, fer ; transfusion ; IgIV ; photothérapie et exsanguinotransfusion (AAP 2004/2022, NICE, OMS) ; ampicilline/amoxicilline, benzylpénicilline, gentamicine, céfotaxime, aciclovir et glucosé chez le nouveau-né ; adrénaline.
- **Erreur critique corrigée** : DOS-PEDI-0003, amoxicilline orale de relais 15 → 25–40 mg/kg toutes les 8 h pendant 5 jours (Pocket book OMS 2013, DOC-00063).
- Marqueurs `[POSOLOGIE À VÉRIFIER]` dans les dossiers : 8 levés avec leur source nommée (adrénaline ; amoxicilline de la MAS non compliquée ; IgIV ; glucosé, ampicilline, benzylpénicilline, gentamicine et aciclovir chez le nouveau-né). Le marqueur anti-D a été normalisé pour être compté par le validateur. Restent 15 :
  - 5 dans PEDI-0001 : NaCl 3 % ×3, ondansétron, racécadotril ;
  - 2 dans PEDI-0003 : thiamine, albendazole ;
  - 1 dans NEON-0001 : anti-D à 28 SA ;
  - 7 dans NEON-0002 : doses méningées d'amoxicilline et de céfotaxime, vancomycine, méropénem, antifongiques, remplissage et amines, antibioprophylaxie per partum.
- Dans les cas, 3 posologies ont été précisées (CAS-PEDI-0005, CAS-NEON-0001, CAS-NEON-0004). Aucune commande git.
