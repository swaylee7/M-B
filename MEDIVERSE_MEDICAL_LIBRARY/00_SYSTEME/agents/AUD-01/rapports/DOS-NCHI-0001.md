# Rapport d'audit — DOS-NCHI-0001 « Traumatisme crânio-encéphalique : diagnostic, traitement »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-02 (posologies, IA), indépendants du rédacteur DOS-12.
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**.
  - 4 marqueurs posologiques restants : SSH de l'adulte (aucune dose standard), phénytoïne, CCP pour antagoniser un anti-Xa, SSH dans le cas.
  - Le texte intégral des RFE SFAR 2016 (S2) est resté inaccessible (sfar.org, HAL) : seuils SFAR toujours « à vérifier ».
- **Bilan** : 9 corrections (critiques 0, majeures 0, mineures 9). AUD-01 : 5 ; AUD-02 : 4.
- **Vérifications** :
  - **NICE NG232** relue sur nice.org.uk :
    - recommandations 1.5.8 à 1.5.13 (TDM dans l'heure et dans les 8 heures, enfant, anticoagulants) ;
    - 1.9.1 (fracture linéaire isolée) ;
    - 1.9.11 à 1.9.13 (rythme de surveillance, critères d'aggravation) ;
  - BTF 4e édition : seuils confirmés par une source secondaire en accès libre (PMC9263560) ;
  - BTF 2007, osmothérapie : notice PubMed et source secondaire (PMC9234368) ;
  - BTF pédiatrique 2019 : SSH 3 % confirmé par PMC8914575 ;
  - HAS 2008 sur les AVK : synthèse lue en texte intégral ;
  - guide européen 2026 sur les hémorragies sous anticoagulants : texte intégral lu.

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| S17 et § 7.2, Marshall | Référence `verifiee: false`. | mineure | Métadonnées confirmées par une citation exacte dans une revue de 2026 en accès libre (PMC13221341) ; article de supplément non indexé dans PubMed. Mention « non vérifiée » retirée. | PMC13221341 |
| § 13.2.2, mannitol (AUD-02) | Marqueur posologique. | mineure | Levé : 0,25 à 1 g/kg en bolus IV (1,25 à 5 mL/kg de mannitol 20 %), selon la BTF 3e édition (2007), source nommée (S18 ajoutée). La 4e édition ne donne plus de posologie. | [S18], [S1] |
| § 13.2.2, SSH de l'enfant (AUD-02) | Marqueur posologique. | mineure | Levé. Bolus de SSH 3 % : 2 à 5 mL/kg en 10-20 min (niveau II). Perfusion continue : 0,1 à 1 mL/kg/h (niveau III). | [S7] |
| § 13.2.6, antagonisation (AUD-02) | Marqueur posologique. | mineure | AVK : CCP adapté à l'INR ou 25 UI/kg + vitamine K 10 mg ; INR à 30 min (< 1,5) et à 6-8 h. Dabigatran : idarucizumab 5 g. Anti-Xa : andexanet alfa selon le RCP (ANNEXA-I : plus d'événements thrombotiques ; retrait du marché américain). Marqueur maintenu pour la dose du CCP. | [S19], [S20] |
| § 17, cas, question 1 | Mécanisme du motard déclaré « non listé » : l'indication de TDM dans les 8 h était omise. | mineure | Nuance : un motard projeté est assimilable à l'« occupant éjecté ». Avec la perte de connaissance, TDM dans les 8 h selon NICE (risque moyen de la règle canadienne). | [S3], [S4] |
| § 17, cas, traitement (AUD-02) | Marqueur posologique. | mineure | Mannitol 0,25-1 g/kg (18-72 g pour 72 kg) ; marqueur maintenu pour le SSH. | [S18] |
| § 21, divergences | Position française absente pour le TC sous AVK. | mineure | HAS 2008 : hospitalisation systématique ≥ 24 h ; TDM immédiate si symptômes neurologiques, sinon différée de 4 à 6 h. NICE 2023 : TDM à envisager dans les 8 h. | [S19], [S3] |
| § 13.4, Algérie | Affirmation non sourcée (« les traumatismes de la voie publique dominent »). | mineure | Reformulée : donnée africaine de S15 (56 %), `[À VÉRIFIER]` pour l'Algérie. | [S15] |
| Sources et vérification | — | mineure | S18 à S20 ajoutées ; note de vérification mise à jour. | — |

## Points vérifiés sans modification

- **Score de Glasgow** (composantes, VT, GCS-P de 1 à 15) ; classification de Marshall (seuils de 25 cm³ et de 5 mm).
- **Règle canadienne** :
  - haut risque : GCS < 15 à 2 h, fracture ouverte ou embarrure, signe de fracture de la base, ≥ 2 vomissements, ≥ 65 ans ;
  - risque moyen : amnésie > 30 min, mécanisme dangereux.
- **PECARN** : groupes avant et après 2 ans ; mécanisme sévère (0,9 m / 1,5 m).
- **BTF 4e édition** :
  - PIC > 22 mmHg ; PPC 60-70 mmHg ;
  - PAS ≥ 100 mmHg (50-69 ans) et ≥ 110 mmHg (15-49 ans et > 70 ans) ;
  - pas d'hyperventilation prophylactique (PaCO2 ≤ 25 mmHg) ; craniectomie avec volet ≥ 12 × 15 cm ;
  - prophylaxie anticomitiale des crises précoces seulement ; nutrition entre J5 et J7 ; pas d'hypothermie prophylactique.
- **BTF 2006** : critères chirurgicaux de l'HED et de l'HSDA.
- **Essais** : CRASH (corticoïdes), CRASH-3, RESCUEicp, BEST-TRIP.

## QCM et cas associés

- **QCM-NCHI-1201 à 1212** : exactes ; QCM-NCHI-1203 (TDM dans les 8 h), 1204 (NICE 1.5.13 et 1.9.1) et 1205 (PECARN, groupe intermédiaire) vérifiées sur les textes → 12 `audite_valide`.
- **CAS-NCHI-1201** : question 1 nuancée ; marqueur maintenu pour le SSH → `audite_corrections_requises`.
- **CAS-NCHI-1202** :
  - objectifs BTF et Marshall III exacts ;
  - correction de la coagulopathie non chiffrée (marqueur maintenu) → `audite_corrections_requises`.

## Reste à faire

1. Texte intégral des RFE SFAR 2016 : PAS, seuil de PIC, PPC, SpO2/PaO2, seuil transfusionnel, seuils du Doppler transcrânien, doses d'osmothérapie.
2. SSH de l'adulte : protocole local ; prophylaxie par phénytoïne (RCP) ; dose du CCP dans la réversion des anti-Xa.
3. Actualisation de la SFMU (2022, non vérifiée) ; données algériennes (sécurité routière, INSP).
4. Relecture enseignant (neurochirurgien ou neuro-réanimateur).
