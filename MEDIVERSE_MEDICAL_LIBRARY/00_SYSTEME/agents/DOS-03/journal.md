# Journal — DOS-03

Mission : Dossiers pédagogiques originaux approfondis — Endocrinologie-diabétologie-néphrologie

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19 — Démarrage de la mission DOS-03 : lecture CONVENTIONS.md, MODELE_DOSSIER.md, schemas/qcm.md, schemas/cas_clinique.md, programme_residanat.json (intitulés RES-MED-084, 091, 092, 122, 125 relevés).
- 2026-11-19 — Phase 1 : vérification des références par recherche web (WebSearch/WebFetch).
- 2026-11-19 — Vérification des références : PubMed E-utilities (esearch/esummary) + texte intégral PMC lorsque disponible (ADA Standards 2026 sections 2, 6, 9, 10, 11, 12, 16 ; consensus hyperglycémies aiguës 2024 ; ETA 2018 Basedow ; KDIGO AKI 2012 (synthèses Crit Care 2013) ; JBDS HHS 2023 ; revue algérienne Belhadj 2025 ; Kardalas 2018). WebSearch : ADA 2026, consensus 2024, KDIGO 2026 AKI/AKD (projet soumis à relecture publique), UKKA hyperkaliémie (2023, mise à jour juillet 2026), ATA 2026 grossesse. Budget WebSearch de session épuisé en cours de vérification ; kdigo.org et ukkidney.org non accessibles en lecture directe (hôtes hors liste autorisée).
- 2026-11-19 — DOS-DIAB-0001 rédigé (3 passes + QCM générés) : 07_MEDECINE_INTERNE/26_DIAB_DIABETOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-DIAB-0001__DIABETE_SUCRE_CLASSIFICATION_INSULINOTHERAPIE_COMPLICATIONS_DT2.md
- 2026-11-19 — DOS-DIAB-0002 rédigé (3 passes + QCM générés) : 07_MEDECINE_INTERNE/26_DIAB_DIABETOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-DIAB-0002__COMPLICATIONS_AIGUES_DU_DIABETE_ACIDOCETOSE_HYPOGLYCEMIE_ETAT_HYPEROSMOLAIRE.md
- 2026-11-19 — DOS-ENDO-0001 rédigé (3 passes + QCM générés) : 07_MEDECINE_INTERNE/25_ENDO_ENDOCRINOLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-ENDO-0001__HYPERTHYROIDIES.md
- 2026-11-19 — DOS-NEPH-0001 rédigé (3 passes + QCM générés) : 07_MEDECINE_INTERNE/20_NEPH_NEPHROLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-NEPH-0001__INSUFFISANCE_RENALE_AIGUE.md
- 2026-11-19 — DOS-NEPH-0002 rédigé (3 passes + QCM générés) : 07_MEDECINE_INTERNE/20_NEPH_NEPHROLOGIE/02_DOSSIERS_PEDAGOGIQUES/DOS-NEPH-0002__DYSKALIEMIES.md
- 2026-11-19 — Lots structurés écrits via commun.ecrire_json (validés par python3 : chargement JSON, unicité des id, propositions A–E, réponses ⊂ A–E, QCS à réponse unique, champs des cas) :
  - 21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/DOS-03.json — 60 QCM (12 par item : QCM-DIAB-0001…0024, QCM-ENDO-0001…0012, QCM-NEPH-0001…0024), origine "originale_mediverse", statut brouillon_a_auditer.
  - 20_CAS_CLINIQUES/lots/DOS-03.json — 10 cas (CAS-DIAB-0001…0004, CAS-ENDO-0001…0002, CAS-NEPH-0001…0004 ; niveaux etudiant, generaliste, resident, specialiste, residanat, dems).
- 2026-11-19 — Passe d'audit interne : YAML valide, 22 sections par dossier, toutes les citations [S#] présentes dans les sources et toutes les sources citées ; ajustement des volumes (ajouts NEPH-0001/0002, allègement DIAB-0001).
  - Mots hors YAML (tokens alphanumériques) : DIAB-0001 9 352 ; DIAB-0002 8 362 ; ENDO-0001 8 181 ; NEPH-0001 7 393 ; NEPH-0002 7 170.
- 2026-11-19 — Transparence : une commande `git status` en lecture seule (sortie masquée, aucune modification) a été exécutée par inadvertance lors d'une vérification de fichiers ; aucune autre commande git.
- 2026-11-19 — Points à auditer en priorité : seuil de bicarbonates des critères EHH (figure 2B du consensus 2024) ; modalités JBDS 2022 (débit d'insuline < 14 mmol/L) ; texte intégral UKKA 2026 (seuil glycémique du relais glucosé, séquence de surveillance) ; ERC 2025 hyperkaliémie ; ATA 2026 grossesse (résumés secondaires seulement) ; référence définitive KDIGO 2026 AKI/AKD ; SFD 2023 et HAS (non vérifiées) ; posologies marquées [POSOLOGIE À VÉRIFIER].
