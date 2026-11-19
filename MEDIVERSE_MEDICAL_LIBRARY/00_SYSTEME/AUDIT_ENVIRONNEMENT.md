# Audit de l'environnement technique — 2026-11-19

Réalisé avant tout lancement de tâches massives (§17, dernier alinéa).

## Machine d'exécution
| Élément | Constat | Conséquence |
|---|---|---|
| Type | Conteneur cloud Claude Code, éphémère (récupéré après inactivité) | Tout résultat doit être **commité et poussé** (branche `claude/new-session-mgmmgb`) |
| CPU / RAM | 4 cœurs, 15 Gio | Exports LibreOffice séquentiels, lots de 20 fichiers |
| Disque | ~58 Go disponibles (allocation de session) | Plafond d'acquisition fixé à 400 Mo par lot OMS, 40 Mo par fichier |
| Dépôt Git | `swaylee7/M-B`, **public**, contient par ailleurs une application d'aviation « Mass & Balance » | La bibliothèque est isolée dans `MEDIVERSE_MEDICAL_LIBRARY/` ; seuls des documents **redistribuables** sont versionnés |

## Outils disponibles
| Outil | État | Usage |
|---|---|---|
| pandoc 3.1.3 | présent | Markdown → ODT |
| LibreOffice 24.2 (soffice) | présent | ODT → PDF, XLSX → ODS |
| poppler (pdfinfo, pdftotext) | présent | contrôle d'intégrité des PDF, détection des PDF scannés |
| Python 3 + pypdf, openpyxl, pandas, PyYAML, requests, bs4, lxml | présents | scripts de la bibliothèque |
| SQLite FTS5 (module Python) | présent | index plein texte |
| Playwright + Chromium | présent | rendu HTML → PDF si besoin |
| Police arabe | DejaVu Sans (couverture arabe) + Amiri (OFL) installée dans `~/.fonts` à partir du paquet npm `@fontsource/amiri` | glossaire FR–EN–AR lisible en PDF |
| **tesseract / ocrmypdf** | **absents** ; installation système (apt) refusée par la politique de la session | **OCR indisponible** dans cette session : les PDF scannés sont détectés (`ocr_requis`) et mis en file pour OCR-02 |
| qpdf, ghostscript | absents | non bloquant |

## Réseau
| Constat | Action |
|---|---|
| Politique réseau « limitée » : seuls les registres de paquets étaient joignables ; téléchargements refusés (`CONNECT tunnel failed, 403`) | Création d'un environnement dédié « M-B – Bibliothèque médicale (sources ouvertes) » (approuvé) avec une liste d'hôtes exacts : OMS (iris/www), NCBI/PMC, Europe PMC, EBI, HAS, NICE, CDC, ECDC, JORADP, MESRS, MSPRH, Institut Pasteur d'Algérie, facultés de Tlemcen, Béjaïa, Mostaganem, Blida |
| Recherche web (WebSearch) et lecture de pages (WebFetch) | disponibles — utilisées pour la découverte et la vérification des références |
| `univ-bejaia.dz` : certificat TLS invalide côté serveur | non contourné (la vérification TLS n'est jamais désactivée) |
| Hôtes hors liste | notés par les agents (« hôtes bloqués ») pour ajout ultérieur ; aucun contournement |

## Quotas et limites
- Pas de quota d'API tiers utilisé (pas de clé requise pour OMS/NCBI/HAS en téléchargement simple).
- Concurrence : ~10 sous-agents simultanés au maximum (au-delà, coût et risque de saturation).
- Les « 100 agents » du cahier des charges sont des **postes** (mission, journal, état de reprise) exécutés par lots — voir `agents/registre_agents.json`.

## Sauvegarde
- Historique Git (chaque lot est commité et poussé) = sauvegarde principale et historique complet.
- `ecrire_json` copie toute version antérieure d'un catalogue dans `00_SYSTEME/sauvegardes/AAAAMMJJ/` avant écrasement.
- Journal append-only : `00_SYSTEME/journaux/operations.jsonl`.
