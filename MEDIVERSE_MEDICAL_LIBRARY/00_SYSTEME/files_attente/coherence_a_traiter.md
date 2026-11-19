# File d'attente — incohérences à traiter (poste AUD-05)

Signalées par les agents des fiches de révision et par les auditeurs. À trancher **sur source**, puis à corriger dans le dossier, dans la fiche dérivée et dans les QCM/cas concernés.

## Signalées par RES-06 (lot 3), le 2026-11-19
- [x] DOS-RHUM-0001 : méthotrexate « 20–30 » contre « 20–25 mg/semaine » ; DAS28 « < 2,6 » contre « ≤ 2,6 ».
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : harmonisé — MTX du cas aligné sur l'initiative 3E (10–15 mg/semaine, jusqu'à 20–30 mg/semaine ; Visser, Ann Rheum Dis 2009 [S5]) ; DAS28 : seuil usuel < 2,6, le « ≤ 2,6 » étant le libellé propre à la série algérienne (Slimani 2014 [S9], formulation confirmée par recherche) — explicité aux § 3, 7.3, 21. DOS-RHUM-0001 v1.2, FIC-RHUM-0001 (déjà conforme) ; QCM-RHUM-0912 exact.
- [x] DOS-MINT-0001 : prednisone « 20–30 mg/j » contre ≈ 17–28 mg/j obtenus par calcul (0,3–0,5 mg/kg).
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : harmonisé — calcul corrigé (≈ 17 à 28 mg/j pour 56 kg ; EULAR/ERA-EDTA 2019 [S4]). DOS-MINT-0001 v1.2 ; fiche, QCM et cas non concernés.
- [x] DOS-MINT-0002 : anticoagulation du PNDS Behçet absente de l'algorithme (divergence EULAR/PNDS signalée ailleurs dans le dossier).
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : divergence réelle présentée — EULAR 2018 (anticoagulant « pouvant être ajouté ») vs PNDS HAS 2019 (anticoagulation curative recommandée 3–6 mois ; TVC 12–18 mois) reportée dans le tableau § 13.2 et les algorithmes § 13.3 et § 16. DOS-MINT-0002 v1.2, FIC-MINT-0002, QCM-MINT-0926 (explication).
- [x] DOS-PSYC-0001 : risque suicidaire « 5–6 % » contre « ≈ 5 % ».
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : harmonisé à « environ 5 à 6 % » (DSM-5-TR, APA 2022 [S1]). DOS-PSYC-0001 v1.2 ; fiche déjà conforme.
- [x] DOS-PSYC-0002 : fluoxétine 60 contre 80 mg/j au maximum ; unités de lithiémie (mmol/L, mEq/L) non harmonisées.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : fluoxétine : divergence réelle présentée (CANMAT 2023, tableau 3.3 relu sur DOC-00099 : 20–60 mg/j issus des monographies ; mhGAP-IG OMS 2016 : max 80 mg/j ; RCP prévaut) ; lithium : 1 mEq/L = 1 mmol/L explicité. DOS-PSYC-0002 v1.2, FIC-PSYC-0002, QCM-PSYC-1018.
- [x] DOS-MLEG-0001 / DOS-MTRA-0001 : immunoglobulines antitétaniques (500 UI après 24 h) présentes dans l'un, absentes de l'autre.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : harmonisé — 250 UI IM, 500 UI au-delà de 24 h (MSF, Médicaments essentiels, HTIG ; même seuil dans le guide australien d'immunisation). DOS-MTRA-0001 v1.2, FIC-MTRA-0001, CAS-MTRA-1001 ; DOS-MLEG-0001 déjà exact.
- [x] Index : RES-MED-101 rattaché à RHUM dans `programme_residanat.json` alors que le dossier est en MINT (rattachement éditorial à revoir dans `importer_programme_residanat.py` : 101 → MINT,RHUM).
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : `101: "MINT,RHUM"` ajouté à `SURCHARGE_MED` ; `importer_programme_residanat.py` puis `indexer.py` relancés sans erreur (0 anomalie) ; RES-MED-101 = [MINT, RHUM], aucun lien perdu (dossiers, fiches, QCM, cas).

## Signalées par les auditeurs
- [x] Remplissage dans l'anaphylaxie : 20 mL/kg (WAO 2020, DOS-IMMU-0002) contre 500–1 000 mL chez l'adulte (DOS-MINT_REA-0001, non vérifié). Probablement compatibles (enfant / adulte) : expliciter les deux, chacun avec sa source.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : explicité source par source — WAO 2020 (texte relu, DOC-00086) : 20 mL/kg quel que soit l'âge ; RCUK 2021 : 500–1 000 mL adulte, 10 mL/kg enfant (extraits de documents RCUK dérivés, texte intégral non relu : marqueur maintenu). Voisins chez l'adulte, divergents chez l'enfant (20 vs 10 mL/kg) : ligne ajoutée au § 21. DOS-MINT_REA-0001 v1.3, DOS-IMMU-0002 v1.2 et leurs fiches.
- [x] DOS-PHYS-0002 et deux cas renvoient vers DOS-CARD-0007 pour les doses d'antiarythmiques : à vérifier une fois DOS-CARD-0007 audité.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : vérifié — DOS-CARD-0007 audité (v1.1) contient au § 13.2.2 le magnésium 2 g IV, l'atropine 0,5 mg (≤ 3 mg) et l'isoprénaline 5 µg/min (ERC 2021) ; renvois précisés (DOS-PHYS-0002 v1.2, FIC-PHYS-0002, CAS-PHYS-1303, CAS-PHYS-1304) ; l'énergie de défibrillation n'y figure pas (renvoi à l'algorithme de réanimation).
- [x] DOS-OBST-0001 : cible de l'HTA sévère gravidique < 160/105 (ESC/ESH) contre < 160/110 : divergence entre recommandations, déjà signalée ; vérifier la cohérence de la fiche.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : vérifié, aucune modification — FIC-OBST-0001 présente la divergence (< 160/110 ; ESC/ESH 2018 : < 160/105, renvoi FIC-CARD-0002) ; CAS du lot DOS-07 et FIC-CARD-0002 cohérents avec leurs référentiels.

## Signalées par RES-06 (lot 4), le 2026-11-19
Détail dans `00_SYSTEME/agents/RES-06/journal_lot4.md` et `etat_lot4.json`.
- [x] DOS-UROL-0001 : délai d'imagerie de la colique néphrétique simple, « 24–48 h » contre « 12–48 h ».
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : harmonisé — dans les 48 h, entre la 12e et la 48e heure selon l'actualisation SFMU 2008 [S9] (échographie + ASP ou scanner non injecté ; sources secondaires concordantes) ; aucune source pour « 24–48 h » ; délai du CLAFU 2022 `[À VÉRIFIER]`. DOS-UROL-0001 v1.2, FIC-UROL-0001.
- [x] DOS-UROL-0002 : renvoi interne erroné.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : corrigé (§ 13.2.2 → § 13.3.2, RAU). DOS-UROL-0002 v1.2.
- [x] DOS-ORL-0001 : plafond pédiatrique du cotrimoxazole douteux.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : vérifié sur source — « sans dépasser 800 mg/160 mg par jour » est le libellé de la fiche HAS de l'enfant (versions 2021 et 2024) ; valeur conservée, précision ajoutée (atteint vers 27 kg, inférieur à la dose adulte de la fiche HAS de l'adulte). DOS-ORL-0001 v1.2, FIC-ORL-0001.
- [x] Les 5 autres points sont listés dans le journal du lot 4.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : traités — (3) TRAU-0001 : Pauwels I ≤ 30°, III ≥ 50° (Bartoníček 2001), AAOS adoptée 2021/publiée 2022 ; (4) TRAU-0002 : paracétamol < 50 kg = 15 mg/kg/prise, 60 mg/kg/j, ≤ 3 g/j (RCP), aligné sur TRAU-0001 ; (6) ORL-0003 : tabac associé aux formes différenciées, pas à l'UCNT (Feng, Br J Cancer 2009 [S12]) ; (7) NCHI-0001 : SpO2 ≥ 90 % rattachée à la BTF 2007, seuil SFAR `[À VÉRIFIER]` ; (8) OPHT-0001 : CI des bêtabloquants = asthme, antécédent de BPCO (EGS 2017), 6e éd. EGS = 2025. Fiches, QCM-TRAU-1112, QCM-TRAU-4098, CAS-TRAU-1102/1103, CAS-NCHI-1202, CAS-OPHT-1201 et PIEGES_CLASSIQUES_LOT4 alignés.

## Signalées par RES-06 (lot 5), le 2026-11-19
- [x] Demi-vies des facteurs vitamine K-dépendants : valeurs différentes entre DOS-HEMA-0007 et DOS-PHAR-0002.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : imprécision harmonisée — DOS-PHAR-0002 reprend les ordres de grandeur de DOS-HEMA-0007 § 4.4 (VII ≈ 4–6 h ; protéine C ≈ 6–8 h ; IX ≈ 18–24 h ; X ≈ 40 h ; II ≈ 60–70 h ; ouvrages de référence Hoffbrand 2024, Williams 2021). DOS-PHAR-0002 v1.2, FIC-PHAR-0002 ; DOS-HEMA-0007 inchangé.
- [x] DOS-PHYS-0001 : le delta ratio du tableau ne concorde pas avec celui du cas clinique.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : harmonisé — tableau complété (≈ 1 attendu dans l'acidocétose, fuite urinaire des cétoanions ; Rastegar, JASN 2007 [S10]) et réponse 5 du cas reformulée. DOS-PHYS-0001 v1.2, FIC-PHYS-0001.
- [x] DOS-PHAR-0002 : seuil d'INR pour le relais AVK→AOD, « ≤ 2 » (EHRA) et « < 2 » (RCP) côte à côte : présenter explicitement la divergence.
   → résolu (AUD-05, 2026-11-19, rapport `00_SYSTEME/agents/AUD-05/rapports/COHERENCE_FINALE_2026-11-19.md`) : divergence présentée (§ 13.3.3 et ligne du § 21) — EHRA 2021 [S5] : ≤ 2,0 (2,0–2,5 le jour même ou le lendemain) ; RCP européens : dabigatran/apixaban < 2, édoxaban ≤ 2,5, rivaroxaban ≤ 3 (FA) / ≤ 2,5 (MTEV) ; le RCP prévaut. DOS-PHAR-0002 v1.2, FIC-PHAR-0002.
