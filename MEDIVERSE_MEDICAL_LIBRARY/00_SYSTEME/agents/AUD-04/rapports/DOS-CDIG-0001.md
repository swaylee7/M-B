# Rapport d'audit — DOS-CDIG-0001 « Kyste hydatique du foie »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01 (scientifique), AUD-02 (posologies), AUD-04 (références) — IA
- **Objets audités** : dossier v1.0 (DOS-04) ; QCM-CDIG-0401…0412 ; CAS-CDIG-0401, CAS-CDIG-0402 (lots DOS-04).
- **Verdict** : `audite_corrections_requises` (v1.1). Aucune erreur critique. Quatre erreurs majeures corrigées, dont une **mise à jour majeure** : le dossier ignorait les **lignes directrices OMS du 16 juin 2025**. Plus aucun marqueur `[POSOLOGIE À VÉRIFIER]`.
- **Ce qui manque pour valider** : la référence S8 (estimation de 3,6–4,6/100 000) n'est pas identifiée ; les auteurs de S7 (série oranaise) sont inconnus ; S4 (manuel PAIR 2001) n'est pas vérifiée ; les données algériennes de lutte (programme national, déclaration obligatoire) manquent.
- **Moyens de vérification** :
  - PDF des lignes directrices OMS 2025 téléchargé depuis iris.who.int et lu (ISBN 978-92-4-011047-2) ;
  - PubMed et PMC (texte intégral de S5 et S6) ;
  - deux recherches web.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| Bandeau, §13.3, §16.2, §21 | **Actualité** : le consensus OMS-IWGE de 2010 était présenté comme la référence alors que l'OMS a publié en 2025 des lignes directrices GRADE qui modifient la stratégie | majeure | Stratégie réécrite selon l'OMS 2025 : CE1/CE3a < 5 cm → albendazole ; 5–10 cm → PAIR + albendazole ; > 10 cm → percutané (PAIR de préférence) + albendazole ; CE2/CE3b ≤ 5 cm → albendazole seul d'abord ; CE2/CE3b > 5 cm → chirurgie + albendazole ; kyste pulmonaire < 5 cm → chirurgie sans albendazole préopératoire. Les positions de 2010 sont conservées et datées dans le tableau des divergences | OMS 2025 [S12], recommandations 1–7 |
| §13.2.1 | Albendazole : durées péri-interventionnelles imprécises et marqueur de posologie | majeure (posologie) | 10–15 mg/kg/j en 2 prises (≤ 400 mg × 2/j), avec un repas gras, **en continu**. Seul : 3–6 mois. Autour d'un geste : 1–7 jours avant, 1–3 mois après. Déversement : ≥ 3 mois (habituellement 6–12) + praziquantel 40–50 mg/kg/j pendant 2 semaines. Contre-indications : kystes à risque de rupture, 1ᵉʳ trimestre de grossesse ; prudence en cas d'hépatopathie ; à éviter en cas d'insuffisance médullaire. Marqueur levé | OMS 2025 [S12] ; consensus 2010 [S1] pour le mébendazole |
| §3.2, §18, §21 | **Données algériennes** : l'étude de Sétif (2026) était présentée comme rapportant une « incidence chirurgicale élevée ». Le chiffre qu'elle cite (12,7/100 000) est **tunisien** (Chahed 2010) | majeure (attribution) | Les trois chiffres sont conservés, chacun avec sa source et sa date, sans en privilégier un : 1,78–2,26/100 000 (cité en 2023, de seconde main) ; 3,6–4,6/100 000 (revue tunisienne non identifiée) ; 12,7/100 000 = Tunisie. Prévalences animales algériennes ajoutées | Texte intégral PMC10714594 et PMC13447339 |
| YAML / §22 | S5 sans auteurs ; S6 sans titre ni revue ; S3, S9, S10 et S11 non vérifiées | majeure (traçabilité) | S5 : Benchikh El Fegoun et coll., *Med Trop Sante Int* 2023 (doi:10.48327/mtsi.v3i3.2023.416). S6 : Kheninef et coll., *Parasitol Res* 2026 (doi:10.1007/s00436-026-08703-4). S3, S9–S11 confirmées avec DOI. S12 (OMS 2025) ajoutée | PubMed 38094490, 12606104, 14726458, 30760475, 32500855 |
| §7.2, §7.3 | Activité des stades selon le seul consensus 2010 | mineure | Viabilité selon l'OMS 2025 ajoutée : CE3b viable ; CE3a viable ou non ; le CL n'est pas un stade | OMS 2025 |
| §7.4 | Seuil de taille unique (5 cm) | mineure | Seuils de 5 et 10 cm | OMS 2025 |
| §10.3 | Grossesse : contre-indication de l'albendazole « pendant la grossesse » | mineure | Contre-indiqué au 1ᵉʳ trimestre ; ensuite, balance bénéfice-risque ; contraception sous traitement prolongé | OMS 2025 |
| §10.3 | Enfant : marqueur « RCP pédiatrique » | mineure | Même posologie en mg/kg. L'âge minimal et la forme galénique restent `[À VÉRIFIER]` | OMS 2025 |
| §13.2.2 | Durée de contact du scolicide « environ 15 min » à vérifier | mineure | 10–20 minutes. Liquide bilieux : pas de scolicide ; drainage par cathéter avec albendazole pendant 6 mois, ou chirurgie | OMS 2025, glossaire et recommandation 2 |
| §13.2.2 | Indications de la PAIR et place du Mo-CAT | mineure | Mises à jour (PAIR pour 5–10 cm et > 10 cm ; Mo-CAT dans de rares centres) | OMS 2025 |
| §13.2.3 | Place de la cœlioscopie marquée à vérifier | mineure | Cœlioscopie pour les kystes périphériques et superficiels (notamment chez l'enfant) ; chirurgie ouverte pour les kystes profonds ; segments 7–8 difficiles | OMS 2025 |
| §13.2.4 | Abstention-surveillance | mineure | Précision : hors du champ de l'OMS 2025, chirurgie seulement si complication | OMS 2025 |
| §14 | Suivi « 1, 3, 6, 12 mois, durée à vérifier » | mineure | Imagerie à 3–6 mois puis annuelle pendant au moins 5 ans après l'inactivation ; absence de réponse = aucun changement à 3 mois | OMS 2025 |
| §2 | Historique | mineure | Ajout des lignes directrices OMS 2025 | OMS 2025 |
| §3.2 | Lecture critique | mineure | Insistance sur le caractère de seconde main des chiffres | — |
| §17 Q5 | Durée de l'albendazole postopératoire `[À VÉRIFIER]` | mineure | 1–3 mois ; ≥ 3 mois avec praziquantel si déversement | OMS 2025 |
| §18 | Points clés 2, 5, 9 et 10 | mineure | Actualisés | OMS 2025 |
| §19 | Piège « albendazole chez la femme enceinte » | mineure | Précisé : au premier trimestre | OMS 2025 |
| §20 | QCM 3 ambigu depuis l'OMS 2025 | mineure | Énoncé limité au consensus 2010, avec une note sur l'OMS 2025 | — |
| §21 | Lignes « albendazole continu » (à vérifier), « CE2/CE3b » et « incidence » | mineure | Actualisées ; nouvelle ligne « gros kystes CE1/CE3a » | OMS 2025 |
| Lot QCM | QCM-CDIG-0404 : CE3b « transitionnel » sans référentiel daté | mineure | Énoncé « selon le consensus 2010 », note sur l'OMS 2025 | OMS 2025 |
| Lot QCM | QCM-CDIG-0406, 0407, 0410, 0411 : explications à actualiser (grossesse, indications de la PAIR, stratégie 2025) | mineure | Actualisées ; source OMS 2025 ajoutée | OMS 2025 |
| Lot cas | CAS-CDIG-0401 : durées d'albendazole `[À VÉRIFIER]` ; suivi | mineure | 1–7 jours avant la PAIR, 1–3 mois après ; suivi pendant au moins 5 ans | OMS 2025 |
| Lot cas | CAS-CDIG-0402 : durée de l'albendazole après rupture `[À VÉRIFIER]` ; kyste pulmonaire | mineure | ≥ 3 mois (6–12) + praziquantel pendant 2 semaines. Pas d'albendazole avant la chirurgie d'un kyste pulmonaire selon l'OMS : séquence à discuter en réunion multidisciplinaire | OMS 2025 |
| Divers | Références des QCM et des cas | mineure | Source OMS 2025 ajoutée | — |

Total : 28 corrections (4 majeures), aucune erreur critique. La posologie de l'albendazole (10–15 mg/kg/j, 400 mg × 2/j) était exacte. Seules les durées et les modalités péri-interventionnelles étaient imprécises.

**Classifications contrôlées** :
- Gharbi (I–V) : exacte ;
- OMS-IWGE (CL, CE1–CE5) : exacte ;
- correspondance Gharbi I = CE1, II = CE3a, III = CE2 (± CE3b), IV = CE4, V = CE5 : exacte.

Les lignes directrices OMS 2025 rappellent que la classification a été établie par Gharbi puis modifiée par l'OMS-IWGE.

## QCM et cas

- QCM-CDIG-0401…0412 : réponses exactes ; `audite_valide`.
- CAS-CDIG-0401 et 0402 : corrigés ; `audite_valide`.

## Références (AUD-04)

- **Avant** : 5/11 vérifiées.
- **Après** : 10/12.
  - S4 (manuel OMS sur la PAIR, 2001) : non retrouvée.
  - S8 (revue tunisienne) : non identifiée.
  - S7 : existence admise d'après DOS-04, auteurs inconnus.

## Reste à faire

1. **Acquisition** : les lignes directrices OMS 2025 sur l'échinococcose kystique sont redistribuables (CC BY-NC-SA 3.0 IGO) et ne figurent pas encore dans `18_RECOMMANDATIONS/04_OMS/` ni dans le catalogue. À confier à un agent ACQ ou REC (URL du PDF : iris.who.int, bitstream 9f8adf1f-7f84-4d05-a13a-9c1adb503020).
2. S8 : identifier la revue tunisienne (estimation de 3,6–4,6/100 000 pour l'Algérie), avec sa date et la période étudiée.
3. S7 : auteurs et titre de la série oranaise (e-Mémoires de l'Académie nationale de chirurgie, 2025).
4. S4 : vérifier le manuel OMS sur la PAIR (WHO/CDS/CSR/APH/2001.6) et les scolicides recommandés (concentrations).
5. Données algériennes :
   - existence d'un programme national de lutte ;
   - statut de maladie à déclaration obligatoire ;
   - disponibilité de l'albendazole et du Western blot ;
   - vaccin EG95.
6. Taux de récidive selon la technique (séries et méta-analyses) ; mortalité des formes compliquées.
7. RCP de l'albendazole disponible en Algérie : vérifier sa concordance avec le traitement continu (certains RCP prévoient encore des cures de 28 jours).
