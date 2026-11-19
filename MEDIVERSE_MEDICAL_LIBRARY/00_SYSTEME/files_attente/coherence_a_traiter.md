# File d'attente — incohérences à traiter (poste AUD-05)

Signalées par les agents des fiches de révision et par les auditeurs. À trancher **sur source**, puis à corriger dans le dossier, dans la fiche dérivée et dans les QCM/cas concernés.

## Signalées par RES-06 (lot 3), le 2026-11-19
- [ ] DOS-RHUM-0001 : méthotrexate « 20–30 » contre « 20–25 mg/semaine » ; DAS28 « < 2,6 » contre « ≤ 2,6 ».
- [ ] DOS-MINT-0001 : prednisone « 20–30 mg/j » contre ≈ 17–28 mg/j obtenus par calcul (0,3–0,5 mg/kg).
- [ ] DOS-MINT-0002 : anticoagulation du PNDS Behçet absente de l'algorithme (divergence EULAR/PNDS signalée ailleurs dans le dossier).
- [ ] DOS-PSYC-0001 : risque suicidaire « 5–6 % » contre « ≈ 5 % ».
- [ ] DOS-PSYC-0002 : fluoxétine 60 contre 80 mg/j au maximum ; unités de lithiémie (mmol/L, mEq/L) non harmonisées.
- [ ] DOS-MLEG-0001 / DOS-MTRA-0001 : immunoglobulines antitétaniques (500 UI après 24 h) présentes dans l'un, absentes de l'autre.
- [ ] Index : RES-MED-101 rattaché à RHUM dans `programme_residanat.json` alors que le dossier est en MINT (rattachement éditorial à revoir dans `importer_programme_residanat.py` : 101 → MINT,RHUM).

## Signalées par les auditeurs
- [ ] Remplissage dans l'anaphylaxie : 20 mL/kg (WAO 2020, DOS-IMMU-0002) contre 500–1 000 mL chez l'adulte (DOS-MINT_REA-0001, non vérifié). Probablement compatibles (enfant / adulte) : expliciter les deux, chacun avec sa source.
- [ ] DOS-PHYS-0002 et deux cas renvoient vers DOS-CARD-0007 pour les doses d'antiarythmiques : à vérifier une fois DOS-CARD-0007 audité.
- [ ] DOS-OBST-0001 : cible de l'HTA sévère gravidique < 160/105 (ESC/ESH) contre < 160/110 : divergence entre recommandations, déjà signalée ; vérifier la cohérence de la fiche.
