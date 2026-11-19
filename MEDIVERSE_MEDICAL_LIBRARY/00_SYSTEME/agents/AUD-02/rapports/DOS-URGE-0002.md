# Rapport d'audit — DOS-URGE-0002 « Morsures et envenimations »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, auditeur indépendant du rédacteur (DOS-06)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1), QCM-URGE-0013 à 0024, CAS-URGE-0003 et 0004
- **Verdict** : `audite_corrections_requises` (aucune erreur critique ; 1 erreur majeure corrigée ; marqueurs du sérum antiscorpionique et des antivenins **conservés**, conformément à la consigne)

## Vérifications effectuées
- **Envenimation scorpionique** : classes I (locale), II (signes généraux), III (défaillance vitale) — conformes à la classification maghrébine usuelle, libellés exacts du guide national non consultés [À VÉRIFIER] ; physiopathologie (canaux sodiques, orage neurovégétatif), dobutamine pour la dysfonction VG, remplissage prudent — **exacts** ; données épidémiologiques Laïd et al. 2012 — vérifiées par le rédacteur.
- **Vipères** : grades 0–3 (Audebert) — **exacts** ; test de coagulation sur tube sec à 20 minutes (OMS SEARO 2016, vérifiée) ; antivenin si grade ≥ 2, coagulopathie, saignement, choc ou neurotoxicité — conforme.
- **Rage (OMS 2018)** : catégories I/II/III ; schémas ID 1 semaine (2 sites J0, J3, J7), IM J0-J3-J7-J14/28, Zagreb 2-1-1 ; immunoglobulines humaines 20 UI/kg ou équines 40 UI/kg infiltrées localement, jusqu'à J7 ; sujet déjà vacciné : J0 et J3 sans immunoglobulines ; pré-exposition J0 et J7 ; observation de 10 jours — **exacts** ; S11 et S12 vérifiées via le catalogue (REC-0531, REC-0280).
- **Morsures animales** : lavage 15 min, amoxicilline–acide clavulanique, suture prudente, *Pasteurella*, *Capnocytophaga* — conformes.
- QCM (12) et cas (2) : réponses exactes.

## Corrections apportées

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 13.2-d, § 21 | Essai tunisien présenté comme montrant l'absence de bénéfice du SAS « sur les envenimations graves » : l'essai portait sur l'**administration systématique**, tous grades confondus, chez 825 patients **de plus de 10 ans** (enfants de moins de 10 ans exclus, alors qu'ils concentrent les décès) | **Majeure** | Description corrigée et limite d'extrapolation à l'enfant ajoutée | Abroug et al., Lancet 1999;354:906-909 (vérifiée) |
| YAML S8, § 22 | Abroug 1999 non vérifiée | Mineure | Vérifiée (doi 10.1016/S0140-6736(98)12083-4) | Recherche |
| YAML S11, S12, § 2, 3.3, 7.3, 13.4, 21, 22 | Position OMS 2018 et TRS 1012 marquées non vérifiées ; nombreux [À VÉRIFIER] sur des données OMS exactes | Mineure | Sources vérifiées ; [À VÉRIFIER] levés sur les catégories, schémas, immunoglobulines, observation de 10 jours | Catalogue REC-0531, REC-0280 |
| § 13.4-d, CAS-URGE-0004 | Immunoglobulines 20/40 UI/kg sous [POSOLOGIE À VÉRIFIER] | Mineure (levée) | Marqueur levé (OMS 2018) ; schéma vaccinal national laissé [À VÉRIFIER] | S11 |
| YAML S13, § 8.2, § 22 | SEARO 2016 et AFRO 2010 non vérifiées | Mineure | SEARO 2016 vérifiée (20WBCT) ; AFRO 2010 signalée non confirmée | Recherche |
| § 21 | Approche marocaine attribuée à S8 | Mineure | Attribution retirée, [À VÉRIFIER] conservé | — |
| En-tête | Statut, version, bloc `audit` | — | v1.1 | Protocole |

## Reste à faire
1. **Sérum antiscorpionique** : indication, posologie, producteur et circuit — à lire dans le guide national algérien en vigueur (2003, mise à jour annoncée en 2022) ; marqueurs conservés (dossier, CAS-URGE-0003, QCM-URGE-0016 à 0018 en `audite_corrections_requises`).
2. **Antivenins ophidiens** : produit disponible en Algérie et posologie selon la notice ; marqueur conservé.
3. Autres marqueurs : lidocaïne locale, amoxicilline–acide clavulanique (et alternatives), schéma vaccinal antirabique national, statut antitétanique selon le calendrier algérien.
4. Sources non vérifiées : S2 (guide national 2003), S9 (Bawaskar 2011), S10 (Chippaux 2008), S14 (stratégie OMS 2019), S15 (IDSA 2014), S16 (Audebert 1992), guide OMS-AFRO 2010.
5. Espèces de scorpions et de serpents d'Algérie, données récentes sur la rage [À VÉRIFIER].
