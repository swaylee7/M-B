# Journal — ANA-01

Mission : Catalogue vérifié des ouvrages de référence et structuration des contenus — Sciences fondamentales I

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19T00:50 (heure approximative) — démarrage mission catalogue ouvrages (postes ANA-01 à ANA-20 tenus par un seul agent). Lecture CONVENTIONS.md, schemas/ouvrage.md, config/specialites.yaml.
- 2026-11-19T00:55 (heure approximative) — recherches web (WebSearch) sur les ouvrages OPU / éditeurs algériens (catalogues BU Souk Ahras, Blida, Annaba, UMMTO). Budget WebSearch de la session épuisé après ~21 requêtes (limite partagée de 200/tour).
- 2026-11-19T01:05 (heure approximative) — réseau sortant restreint (WebFetch/curl : seuls les hôtes NCBI sont joignables). Vérification poursuivie via le NLM Catalog (NCBI E-utilities, catalogue de la National Library of Medicine) et la liste « LitArch Open Access » de NCBI Bookshelf (licences lues dans les métadonnées XML des paquets).
- 2026-11-19T01:16:38+00:00 — lot ANA-algerie-france.json écrit : 112 ouvrages (56 Algérie, 56 France), OUV-0001 à OUV-0112 ; JSON validé (python3).
- 2026-11-19T01:18:42+00:00 — lot ANA-fondamentales.json écrit : 77 ouvrages (OUV-0150 à OUV-0226 ; porté ensuite à 80, OUV-0229), sciences fondamentales et biologie ; JSON validé.
- 2026-11-19T01:21:19+00:00 — lot ANA-medicales.json écrit : 115 ouvrages (OUV-0300 à OUV-0414 ; porté ensuite à 116, OUV-0415) ; JSON validé.
- 2026-11-19T01:22:07+00:00 — lot ANA-chirurgicales.json écrit (OUV-0500 et suivants) ; JSON validé.
- 2026-11-19T01:23:14+00:00 — lot ANA-transversales.json écrit (OUV-0650 et suivants) ; JSON validé.
- 2026-11-19T01:25:21+00:00 — renforcement des spécialités les plus faibles (IMPA, CCVA, CTHO, MFAM) ; contrôle des clés ISBN (1 numéro algérien invalide écarté) ; dédoublonnage des auteurs.
- 2026-11-19T01:25:21+00:00 — bilan : 440 ouvrages (Algérie 56, France 58, international 326) ; vérifié 253 (57,5 %), partiel 139, non vérifié 48 ; 59/59 spécialités couvertes (min. 6) ; 26 ouvrages en accès ouvert légal + 2 en lecture gratuite. etat.json mis à jour ; postes ANA-02 à ANA-20 marqués « couvert_par_ANA-01 ».
