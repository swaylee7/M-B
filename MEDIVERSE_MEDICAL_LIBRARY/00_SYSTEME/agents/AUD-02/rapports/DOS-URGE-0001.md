# Rapport d'audit — DOS-URGE-0001 « Conduite à tenir devant une intoxication aiguë »

- **Postes** : AUD-01 (audit scientifique) et AUD-02 (posologies) — IA, auditeur indépendant du rédacteur (DOS-06)
- **Date** : 2026-11-19
- **Objets audités** : dossier (v1.0 → v1.1), QCM-URGE-0001 à 0012, CAS-URGE-0001 et 0002
- **Verdict** : `audite_corrections_requises` (aucune erreur critique ; 1 erreur majeure corrigée ; marqueurs de posologie conservés pour les antidotes dépendant du produit ou du protocole)

## Vérifications effectuées
- **Paracétamol** : seuil ANZ ≥ 200 mg/kg ou ≥ 10 g ; nomogramme à partir de H4, droite ANZ 150 mg/L à 4 h, droite britannique 100 mg/L ; NAC sans attendre au-delà de 8 h ; **schéma en 2 poches** 200 mg/kg/4 h puis 100 mg/kg/16 h ; **schéma en 3 poches** 150/50/100 mg/kg ; réactions anaphylactoïdes non contre-indicatives — **exacts**. Calcul du cas CAS-URGE-0001 (≈ 273 mg/kg ; droite ≈ 53 mg/L à H10 ; 85 mg/L au-dessus) — **exact**.
- **Naloxone** titrée sur la FR ; **flumazénil** et ses contre-indications (proconvulsivants, QRS large, épilepsie, dépendance) — **exacts**.
- **Organophosphorés** : atropine 1–2 mg puis doublement toutes les 5 min jusqu'aux critères d'atropinisation (poumons secs, FC > 80, PAS > 80, aisselles sèches, pupilles non punctiformes), succinylcholine proscrite, syndrome intermédiaire — **exacts** ; référence Eddleston 2008 vérifiée.
- **CO** : oxygène normobare immédiat, SpO₂ trompeuse, oxygénothérapie hyperbare dans les formes graves, syndrome post-intervallaire — **exact** ; ECHM 2016 vérifiée (existence).
- **Hydroxocobalamine**, **bleu de méthylène**, **bicarbonate** (QRS ≥ 120 ms), **fomépizole/éthanol**, **charbon activé** (50 g ; 1 g/kg ; < 1 h ; non adsorbés) — conformes ; ajustements ci-dessous.
- **Centre National de Toxicologie** : aucun numéro de téléphone n'était reproduit ; existence attestée par la littérature, coordonnées non vérifiées.
- QCM (12) et cas (2) : réponses exactes, sauf la formulation de QCM-URGE-0006 E.

## Corrections apportées

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 10.2, § 13.2-d, QCM-URGE-0006 (dossier et JSON) | Flumazénil : « sans dépasser 1 mg » présenté comme maximum général (limite propre à la réversion d'une sédation) ; QCM-URGE-0006 E (« dose totale usuelle ≤ 1 mg ») jugée vraie sur une donnée non sourcée | **Majeure** | Titration jusqu'à réveil suffisant, maximum selon l'indication et le RCP ; proposition E reformulée (« titration IV de petites doses successives », toujours vraie) | RCP flumazénil (marqueur maintenu) |
| § 10.1, § 13.2-d, § 21 | NAC en 3 poches sous [POSOLOGIE À VÉRIFIER] | Mineure (levée) | Schéma du RCP (150 mg/kg en 15–60 min, 50 mg/kg/4 h, 100 mg/kg/16 h ; 300 mg/kg sur ≈ 21 h) — marqueur levé | RCP acétylcystéine IV |
| § 10.7, § 13.2-d | Atropine sous marqueur ; entretien non chiffré | Mineure (levée) | Doublement toutes les 5 min, puis perfusion ≈ 10–20 % de la dose de charge par heure — marqueur levé | Eddleston et al., Lancet 2008 [S8] |
| § 10.7, § 13.2-d, § 21, CAS-URGE-0002 | Pralidoxime « schéma OMS » non chiffré | Mineure | 30 mg/kg (chlorure) en 20–30 min puis 8 mg/kg/h ; marqueur maintenu (sel et RCP) | S8 (schéma OMS) |
| § 10.10, § 13.2-d | Hydroxocobalamine « en 15–30 min » sous marqueur | Mineure | 5 g IV en 15 min (enfant 70 mg/kg, max 5 g), seconde dose possible — marqueur levé | RCP hydroxocobalamine |
| § 10.10, § 13.2-d | Bleu de méthylène sous marqueur | Mineure (levée) | 1–2 mg/kg IV en 5 min, contre-indiqué si déficit en G6PD | RCP bleu de méthylène |
| § 13.2-d | Fomépizole non chiffré | Mineure (levée) | 15 mg/kg puis 10 mg/kg/12 h (4 doses) puis 15 mg/kg/12 h, rapproché pendant l'hémodialyse ; éthanol laissé sous marqueur | RCP fomépizole |
| YAML S8, § 22 | Eddleston 2008 non vérifiée | Mineure | Vérifiée (Lancet 2008;371(9612):597-607, doi) | Recherche |
| YAML S9, § 21, § 22, QCM-URGE-0008 | ECHM 2016 non vérifiée | Mineure | Mathieu et al., Diving Hyperb Med 2017;47(1):24-32 ; critères cliniques détaillés laissés [À VÉRIFIER] | Recherche |
| YAML S13, § 2, § 13.2-f, § 13.4 | CNT : coordonnées non vérifiées | Mineure | Aucun numéro reproduit ; renvoi au site officiel du ministère de la Santé ou du CNT | Consigne du propriétaire |
| QCM-URGE-0002 C | « Schéma ANZ 2019 » (publication 2020) | Mineure | « Chiew et al., Med J Aust 2020 » | S4 |
| En-tête | Statut, version, bloc `audit` | — | v1.1 | Protocole |

## Reste à faire
1. Marqueurs de posologie conservés (produit ou protocole dépendants) : naloxone (titration, perfusion), flumazénil (maximum selon RCP), bicarbonate de sodium (1–2 mmol/kg), glucagon, sels de calcium, insuline à forte dose, émulsion lipidique, fragments Fab antidigoxine, pyridoxine, vitamine K1, pralidoxime (sel), éthanol, hémodialyse et alcools toxiques (EXTRIP).
2. Sources non vérifiées : S10 (EXTRIP), S11 (Rumack-Matthew, MHRA 2012), S12 (RCP non consultés pendant la session).
3. CNT : obtenir les coordonnées officielles (site du ministère ou du CNT) avant toute publication d'un numéro.
4. Points [À VÉRIFIER] maintenus : seuil français de dose toxique de paracétamol, critères du King's College, Atractylis gummifera, chloroquine, octréotide, durées d'observation.
