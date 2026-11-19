# Journal — ACQ-01

Mission : Algérie — textes officiels (MESRS, MSPRH, JORADP), programmes du résidanat et du DEMS

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19T00:54:59+00:00 — Session de travail (postes ACQ-01/02/03, REC-01, DEMS-01/02). Lecture CONVENTIONS, schéma recommandation, acquerir.py.
- 2026-11-19T00:54:59+00:00 — Test réseau : joradp.dz, mesrs.dz, fmed.univ-tlemcen.dz, univ-mosta.dz, pasteur.dz OK ; univ-blida.dz → 403 proxy ; univ-bejaia.dz → échec TLS (chaîne de certificat incomplète, non contourné) ; www.sante.gov.dz → connexion réinitialisée / DNS.
- 2026-11-19T00:54:59+00:00 — Acquis DOC-00004 : JORADP 2011 n°38 (décret exécutif 11-236 statut du résident, p. 12-15), redistribuable.
- 2026-11-19T01:08:22+00:00 — www.mesrs.dz : page « Textes juridiques » chap. III (liste des textes sur la formation en sciences médicales) ; PDF des textes hébergés sur services.mesrs.dz → bloqué (403 proxy), non contourné.
- 2026-11-19T01:08:22+00:00 — Téléchargé 14 Bulletins officiels MESRS (2022-T3 → 2026-T2, www.mesrs.dz) ; extraction texte arabe, repérage des arrêtés résidanat/DEMS ; extraits de pages (pypdf) acquis avec --fichier + --url source.
- 2026-11-19T01:08:22+00:00 — Acquis DOC-00005 à DOC-00012 (16_RESIDANAT : arrêté 1144/1397 conditions d'accès, calendriers 2023→2027, postes Sud 2023) et DOC-00013 à DOC-00020 (17_DEMS : programmes nationaux, nomenclature arrêté 173 modifié, création DEMS urgences, CPRS/CPNS, jurys DEMS 2024-2025), tous redistribuables (texte officiel).
- 2026-11-19T01:08:22+00:00 — Acquis DOC-00021 (JO 1982 n°54, décret 82-492) et DOC-00022 (JO 1971 n°100, décret 71-275 création du DEMS), scannés, OCR requis, vérifiés visuellement.
- 2026-11-19T01:23:46+00:00 — Acquis DOC-00023 (arrêté 844/2023, Tlemcen), DOC-00066 (arrêté 1137/2015 + annexe spécialités/durées), DOC-00067 (arrêté 594/2001, historique, abrogé), DOC-00068 (note d'inscription résidanat Mostaganem 2026), DOC-00069 (annexe programme 6e année) — via fmed.univ-tlemcen.dz et l'API WordPress publique de www.univ-mosta.dz/medecine.
- 2026-11-19T01:23:46+00:00 — Hôtes bloqués notés (non contournés) : services.mesrs.dz, fntic.univ-ouargla.dz, www.univ-sba.dz, www.ummto.dz, univ-blida.dz, elearn/entfmed.univ-tlemcen.dz, facmed.univ-alger.dz, www.insp.dz ; univ-bejaia.dz : TLS non vérifiable ; www.sante.gov.dz : connexion réinitialisée.
- 2026-11-19T01:23:46+00:00 — Rédigé 16_RESIDANAT_ALGERIE/00_TEXTES_OFFICIELS/ETAT_DES_SOURCES_RESIDANAT.md.
- 2026-11-19T01:23:46+00:00 — Budget WebSearch de la session épuisé en cours de mission : la recherche s'est poursuivie par exploration directe des sites autorisés (JORADP, MESRS, facultés).
- 2026-11-19T03:44:50+00:00 — Session ACQ-01 + AUD-01/AUD-02 (lot DOS-10). Numéros du JORADP identifiés par lecture des sommaires (curl sur www.joradp.dz, format FTP/jo-francais/AAAA/FAAAANNN.pdf) ; OCR tesseract (fra) des numéros scannés pour vérifier les intitulés et les articles.
- 2026-11-19T03:44:50+00:00 — Acquis (MTRA, 00_PROGRAMME_OBJECTIFS/textes_officiels, redistribuables) : DOC-00103 JORADP 1983-28 (loi 83-13 AT/MP, 32 p.) ; DOC-00104 JORADP 1996-42 (ordonnance 96-19 modifiant la loi 83-13, 26 p.) ; DOC-00105 JORADP 1988-04 (loi 88-07, 32 p.) ; DOC-00106 JORADP 1997-16 (arrêté interministériel du 5 mai 1996 fixant la liste des maladies présumées d'origine professionnelle et ses annexes 1 et 2, 59 p. — intitulé exact vérifié).
- 2026-11-19T03:44:50+00:00 — Acquis (MLEG, 00_PROGRAMME_OBJECTIFS/textes_officiels, redistribuables) : DOC-00107 JORADP 1992-52 (décret exécutif 92-276, code de déontologie médicale, 39 p.) ; DOC-00108 JORADP 1966-49 (ordonnance 66-156, code pénal, rédaction d'origine, 35 p.) ; DOC-00109 JORADP 2006-84 (loi 06-23 : art. 264, 266, 442 — seuil d'ITT de 15 jours) ; DOC-00110 JORADP 2015-71 (loi 15-19 : art. 266 bis, 266 bis 1) ; DOC-00111 JORADP 2024-30 (loi 24-06 : art. 264, 265, 269, 272, 288, 289). Condition posée pour le code pénal remplie : JO des modifications des articles sur les coups et blessures trouvés ; aucune version consolidée officielle au JORADP.
- 2026-11-19T03:44:50+00:00 — Acquis hors liste, pour l'audit de DOS-MLEG-0002 : DOC-00112 JORADP 1975-78 (ordonnance 75-58, code civil, 55 p.) ; DOC-00113 JORADP 2005-44 (loi 05-10 modifiant le code civil). Total de la session : 11 documents, 22,9 Mo (plafond de 60 Mo respecté ; aucun fichier > 30 Mo).
- 2026-11-19T03:44:50+00:00 — Autres JO examinés sans acquisition (aucune modification des art. 264 ou 442 du code pénal) : 2011-44, 2014-07, 2016-37, 2020-25, 2021-84. Hôtes bloqués notés, non contournés : www.ema.europa.eu, www.medicines.org.uk, base-donnees-publique.medicaments.gouv.fr, ansm.sante.fr, apps.who.int, cdn.who.int, bnf.nice.org.uk ; iris.who.int renvoie une page de contrôle anti-robot.
- 2026-11-19T04:05:26+00:00 — Acquisitions réalisées par AUD-01 pour l'audit de DOS-SPUB-0001, sous l'identité ACQ-01 (`acquerir.py --type texte_officiel --redistribution redistribuable`) dans `15_AUTRES_SPECIALITES/49_SPUB_SANTE_PUBLIQUE/00_PROGRAMME_OBJECTIFS/textes_officiels/` :
  - DOC-00114 : JORADP 2007-33 (décret 07-140, EPH et EPSP) ;
  - DOC-00115 : JORADP 1997-81, scanné (décrets 97-465 EHS, 97-466 secteurs sanitaires, 97-467 CHU) ;
  - DOC-00116 : JORADP 2020-50 (ordonnance 20-02 modifiant la loi 18-11) ;
  - DOC-00117 : JORADP 1974-01, scanné (ordonnance 73-65, médecine gratuite) ;
  - DOC-00118 : JORADP 1992-02, scanné (décret 92-07, caisses de sécurité sociale).
  Total 5,2 Mo (plafond de 40 Mo). Contenus vérifiés par pdftotext ou OCR (tesseract fra).
