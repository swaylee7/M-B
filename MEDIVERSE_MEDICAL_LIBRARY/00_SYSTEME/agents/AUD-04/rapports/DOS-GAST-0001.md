# Rapport d'audit — DOS-GAST-0001 « Hémorragies digestives »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (scientifique), AUD-02 (posologies), AUD-04 (références) — IA
- **Objets audités** : dossier v1.0 (DOS-04) ; QCM-GAST-0401…0412 (lot `21_QCM_ANNALES/01_BANQUE_QCM_ORIGINALE/lots/DOS-04.json`) ; CAS-GAST-0401, CAS-GAST-0402 (lot `20_CAS_CLINIQUES/lots/DOS-04.json`).
- **Verdict** : `audite_valide` (v1.1). Aucune erreur critique. Trois erreurs majeures corrigées. Plus aucun marqueur `[POSOLOGIE À VÉRIFIER]`. Les 14 références sont vérifiées.
- **Moyens de vérification** :
  - résumés PubMed contenant les recommandations principales de l'ESGE 2021 et de l'ESGE 2022 ;
  - texte intégral de Baveno VII (PMC11090185, via NCBI E-utilities) ;
  - métadonnées PubMed et Europe PMC ;
  - recherche web pour la formulation ESGE du seuil transfusionnel du coronarien.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §13.4 | L'aspirine de prévention secondaire était « poursuivie si possible ou brièvement interrompue », alors que l'ESGE recommande de ne pas l'interrompre. Le délai de reprise était marqué à vérifier | majeure | Ne pas interrompre l'aspirine. Si elle a été interrompue, la reprendre dès que possible, de préférence dans les 3–5 jours. Même correction dans le cas clinique (Q2, Q6) | ESGE 2021, recommandation 2 (résumé PubMed 33567467) |
| §13.4 | Antagonisation des AVK et des AOD (vitamine K, CCP, antidote) attribuée à l'ACG 2023 [S4] sans vérification. Les recommandations ACG s'opposent plutôt à une antagonisation systématique | majeure | Reformulé : antagonisation seulement si l'hémorragie menace le pronostic vital, selon le protocole local. Attribution à [S4] retirée, marqueur `[À VÉRIFIER]`. Reprise de l'anticoagulation « dans les 7 jours ou peu après » | ESGE 2021, recommandation 10 |
| YAML / §22 | Six références `verifiee: false` (S9–S14), HALT-IT sans pagination ni DOI, DOI manquants | majeure (traçabilité) | S5, S7, S9–S14 confirmées, avec DOI et PMID | PubMed : 28053181, 32563378, 11073021, 8675081, 4136718, 28651935, 20573925, 35944925 |
| §13.2.1 | Villanueva : survie « à 45 jours » | mineure | Corrigé en survie à 6 semaines (95 % contre 91 %), aussi dans l'explication de QCM-GAST-0403 | Villanueva, NEJM 2013 |
| §13.2.1 | Seuil transfusionnel du coronarien marqué `[formulation exacte À VÉRIFIER]` | mineure | Confirmé : seuil ≤ 8 g/dL et cible ≥ 10 g/dL (recommandation forte, preuve faible) | ESGE 2021 |
| §13.2.1, §21 | Cible transfusionnelle de l'hémorragie variqueuse : divergence non signalée | mineure | Baveno VII retient 7–8 g/dL, l'ESGE 2022 7–9 g/dL. Ligne ajoutée au tableau des divergences | Baveno VII 6.2 ; ESGE 2022, recommandation 3 |
| §13.2.2 | IPP : alternatives incomplètes et marqueur de posologie | mineure | IPP avant l'endoscopie présentée comme une option « à envisager ». Après hémostase : 80 mg puis 8 mg/h pendant 72 h, ou forte dose IV ou orale 2 fois par jour. Marqueur levé, seule la disponibilité locale reste à vérifier | ESGE 2021, recommandation 9 ; RCP de l'ésoméprazole IV |
| §13.2.2 | Relais oral « double dose jusqu'à J14 » présenté comme ESGE 2021 | mineure | Ce schéma ne figure pas dans les recommandations principales de l'ESGE 2021. Signalé `[À VÉRIFIER — texte intégral]` | ESGE 2021 |
| §13.2.4 | Vasoactifs : marqueur de posologie ; dose de somatostatine imprécise ; hyponatrémie sous terlipressine non mentionnée | mineure | Marqueur levé : schémas EASL 2018. Durée de 2–5 jours (Baveno VII A.1) ou « jusqu'à 5 jours » (ESGE 2022). Surveillance de la natrémie ajoutée | EASL 2018 [S8] ; Baveno VII 6.5–6.6 ; ESGE 2022, recommandation 5 |
| §13.2.5 | Antibioprophylaxie : nuances de Baveno VII absentes | mineure | Prophylaxie dès l'admission. Ceftriaxone 1 g/j jusqu'à 7 jours (ESGE 2022), à privilégier en cas de cirrhose avancée, de résistance aux quinolones ou de prophylaxie antérieure par quinolone. Bénéfice incertain en Child-Pugh A | Baveno VII 6.7–6.9 ; ESGE 2022, recommandation 6 |
| §13.2.6 | Lactulose « éventuellement mannitol, peut être utilisé » | mineure | Corrigé : l'élimination rapide du sang par lactulose (orale ou en lavements) « doit être utilisée » (B.1) | Baveno VII 6.33 |
| §13.2.8 | TIPS préemptif incomplet | mineure | Ajouts : prothèse couverte en PTFE ; varices œsophagiennes et GOV1/2 ; l'ACLF, l'encéphalopathie et l'hyperbilirubinémie à l'admission ne sont pas des contre-indications ; critères de futilité (Child ≥ 14, ou MELD > 30 avec lactates > 12 mmol/L) | Baveno VII 6.27, 6.28, 6.31 |
| §13.2.9 | Formulation sur la prothèse œsophagienne | mineure | La prothèse auto-expansible est aussi efficace que le tamponnement par ballonnet et plus sûre | Baveno VII 6.29 |
| §13.3.2 (9) | Arrêt de l'IPP après l'endoscopie marqué à vérifier | mineure | Confirmé : arrêter l'IPP sauf indication stricte | Baveno VII 6.12 |
| §13.3.2, §16.3 | Prophylaxie secondaire : nadolol absent | mineure | BBNS traditionnel (propranolol, nadolol) ou carvédilol, associé aux ligatures | Baveno VII 7.8 ; ESGE 2022, recommandation 16 |
| §14.2 | Intervalles de surveillance des varices à vérifier | mineure | Ligatures toutes les 1–4 semaines, puis surveillance tous les 3–6 mois la première année | ESGE 2022, recommandations 2 et 15 |
| §16.3 | Algorithme | mineure | Antibioprophylaxie dès l'admission ; nadolol et carvédilol ajoutés | Baveno VII |
| §17 Q2 | Transfusion d'un coronarien à Hb 8,9 g/dL sans justification, alors que le seuil ESGE est ≤ 8 g/dL chez le patient stable | mineure | Transfusion justifiée ici par l'instabilité hémodynamique et un saignement probablement actif | ESGE 2021 |
| §18, §21 | Point clé 12 et lignes « reprise de l'anticoagulation » et « coronarien » | mineure | Alignés sur la formulation ESGE 2021 | ESGE 2021 |
| Lot QCM | QCM-GAST-0403 : « 45 jours » | mineure | Corrigé en 6 semaines ; QCM-GAST-0401…0412 passés en `audite_valide` | Villanueva 2013 |

**Erreurs critiques (posologie)** : aucune. Les posologies ont été confrontées aux recommandations et sont exactes :
- IPP : 80 mg puis 8 mg/h ;
- terlipressine : 2 mg toutes les 4 h, puis 1 mg toutes les 4 h ;
- somatostatine : 250 µg puis 250–500 µg/h ;
- octréotide : 50 µg puis 50 µg/h ;
- ceftriaxone : 1 g/j ;
- érythromycine : 250 mg.

## Contrôles des classifications et scores

Barèmes exacts :
- Glasgow-Blatchford (maximum 23) ; seuil ≤ 1 (sensibilité 98,6 %, spécificité 34,6 %) ;
- Rockall (pré-endoscopique 0–7, complet 0–11) ;
- AIMS65 ;
- Forrest (Ia à III) ;
- Child-Pugh ;
- Sarin ;
- seuils de gradient de pression veineuse hépatique.

Le calcul du score de Glasgow-Blatchford du cas (14 points) est juste.

## QCM et cas

- QCM-GAST-0401…0412 : réponses exactes ; `audite_valide`.
- CAS-GAST-0401 : Child-Pugh C12 exact, indication de TIPS préemptif exacte ; `audite_valide`.
- CAS-GAST-0402 : conforme à l'ACG 2023 et à l'ESGE 2021 ; `audite_valide`.

## Références (AUD-04)

- **Avant** : 8/14 vérifiées.
- **Après** : 14/14, avec DOI et PMID. HALT-IT : *Lancet* 2020;395(10241):1927-1936, doi:10.1016/S0140-6736(20)30848-5.

## Reste à faire (non bloquant)

1. Sourcer les ordres de grandeur épidémiologiques encore marqués `[À VÉRIFIER]` :
   - incidence de l'HDH ;
   - arrêt spontané d'environ 80 % ;
   - fréquences étiologiques ;
   - taux de récidive selon Forrest ;
   - proportion d'origines hautes devant une rectorragie.
2. Lire le texte intégral de l'ESGE 2021 :
   - durée du relais oral des IPP ;
   - seuil plaquettaire ;
   - prophylaxie de l'ulcère de stress (recommandation de réanimation à citer).
3. Lire le texte intégral de l'ACG 2023 (et de l'ACG-CAG 2022) : antagonisation des AVK et des AOD dans l'hémorragie digestive.
4. Données algériennes :
   - organisation de l'endoscopie d'urgence, de l'embolisation et du TIPS ;
   - prévalence de *H. pylori* ;
   - nomenclature des médicaments.
5. Relecture par un enseignant (statut `valide_enseignant`).
