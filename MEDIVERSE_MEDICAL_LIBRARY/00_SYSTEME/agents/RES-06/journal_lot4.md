# Journal — RES-06 (lot 4)

Mission : fiches de révision (mémo, tableaux, pièges classiques) dérivées des dossiers v1.1 audités — lot 4 :
urologie, traumatologie, orthopédie, ORL, neurochirurgie, ophtalmologie (10 fiches)
+ compilation `16_RESIDANAT_ALGERIE/07_PIEGES_CLASSIQUES/PIEGES_CLASSIQUES_LOT4.md`.
Les fichiers des lots 1 à 3 (`journal.md`, `etat.json`, `journal_lot2.md`, `etat_lot2.json`, `journal_lot3.md`,
fiches existantes, PIEGES_CLASSIQUES_LOT1/LOT2/LOT3) ne sont pas modifiés. Pas d'opération Git (consigne).

- 2026-11-19 — démarrage du lot 4. Lecture de `00_SYSTEME/CONVENTIONS.md`, de FIC-CARD-0001 et FIC-PEDI-0001 (format de référence : en-tête YAML, sections 1 à 9), de PIEGES_CLASSIQUES_LOT2 (format de renvoi item + fiche) et des rapports/état AUD-01 (`etat_DOS-11.json`, `etat_DOS-12.json`) : les 10 dossiers sources sont en **v1.1** (DOS-ORL-0001 `audite_valide`, les 9 autres `audite_corrections_requises`).
- 2026-11-19 — outils de contrôle (scratchpad de session, non versionnés) : `inject_sources.py` (copie à l'identique, depuis l'en-tête YAML du dossier, des blocs [Sx] cités dans la fiche) ; `check_numbers.py` (vérifie que chaque nombre du corps de la fiche figure dans le dossier, puis que chaque couple « nombre(s) + unité » y figure tel quel, après normalisation des espaces et tirets) ; `wc.py` (mots hors balises Markdown et hors YAML).
- 2026-11-19 — FIC-UROL-0001 (lithiase urinaire et colique néphrétique ; items RES-CHI-023 et RES-CHI-030) créée depuis DOS-UROL-0001 v1.1 ; contrôle chiffres/doses : 0 écart (« 0,4 mg/j » réécrit « 0,4 mg une fois par jour » comme dans le dossier) ; 1 996 mots.
- 2026-11-19 — FIC-UROL-0002 (adénome de la prostate / HBP et STBAU ; item RES-CHI-025) créée depuis DOS-UROL-0002 v1.1 ; contrôle chiffres/doses : 0 écart (« 30 et 80 mL » du mnémotechnique réécrit « 30–80 mL ») ; 1 883 mots.
