# Rapport d'audit — DOS-NEON-0002 « Infections néonatales »

- Date : 2026-11-19 — Auditeurs : AUD-01 et AUD-02 (IA)
- Version auditée : 1.0 → version corrigée : 1.1
- Verdict : **audite_corrections_requises** (aucune erreur critique ; erreurs majeures corrigées ; 7 marqueurs de posologie restants)
- Documents lus : Pocket book OMS 2013, section 3.14 « doses des médicaments usuels du nouveau-né » (DOC-00063) ; recommandations OMS 2024 sur les infections bactériennes graves de 0 à 59 jours (DOC-00052) ; PCIME du nourrisson de 0 à 2 mois, 2019 (DOC-00034) ; AWaRe 2022 (DOC-00039). Recherche web : NICE NG195 (benzylpénicilline 25 mg/kg/12 h, rapprochée à 8 h si l'enfant est très malade ; gentamicine 5 mg/kg, 2ᵉ dose à 36 h, hors AMM ; drapeaux rouges), RBP SFN/SFP 2017 labellisée HAS, Kimberlin 2001 (PMID 11483782).

## Posologies (point prioritaire, AUD-02)
| Molécule | Dossier v1.0 | Constat | v1.1 |
|---|---|---|---|
| Ampicilline/amoxicilline | 50 mg/kg/12 h la 1ʳᵉ semaine ; méningite ≈ 100 mg/kg/dose | Conforme à l'OMS 2013 et 2024 (puis toutes les 8 h) ; l'OMS 2024 garde 50 mg/kg dans la méningite | Dose générale sourcée, marqueur levé ; dose méningée laissée à vérifier |
| Benzylpénicilline | 25 mg/kg/12 h (8 h si très malade) | Conforme à NICE NG195 | Sourcée + OMS 50 000 UI/kg (12 h puis 6 h) ; marqueur levé |
| Gentamicine | NICE 5 mg/kg/36 h ; OMS 5 mg/kg/24 h (3 mg/kg si petit poids de naissance) | Conforme ; manquait 7,5 mg/kg/24 h après la 1ʳᵉ semaine (OMS) et le caractère hors AMM du rythme de 36 h | Complétée ; marqueur levé |
| Céfotaxime | 50 mg/kg/12 h la 1ʳᵉ semaine, puis toutes les 8 h | Sources discordantes : OMS 2024 12 h puis 6 h ; Pocket book 2013 12 h chez le prématuré, 8 h la 1ʳᵉ semaine à terme, 6 h de 2 à 4 semaines | Rythmes sourcés ; dose méningée à vérifier |
| Aciclovir | 20 mg/kg/8 h ; 14 ou 21 j | Conforme (60 mg/kg/j ; 21 j dans l'essai ; 14 j pour la forme cutanéo-oculo-buccale dans les recommandations ultérieures) | Marqueur levé ; surveillance des neutrophiles ajoutée |
| Glucosé 10 % | 2 mL/kg puis perfusion | Conforme (OMS : 2 mL/kg IV, puis 5 mL/kg/h ; hypoglycémie < 2,2 mmol/L) | Marqueur levé |
| Antibioprophylaxie per partum (pénicilline G 5 MUI puis 2,5–3 MUI/4 h ; ampicilline 2 g puis 1 g/4 h) | Valeurs standard | CDC 2010 et ACOG 2020 non relus | Marqueur maintenu |

## Corrections
| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §7.3 Drapeaux rouges NICE | Liste de CG149 (2012) attribuée à NG195 | **Majeure** (actualité) | Liste NG195 : apnée, convulsions, réanimation cardiopulmonaire, ventilation mécanique, choc ; infection chez un jumeau (facteur de risque) ; ancienne liste signalée comme remplacée | S2 (vérifiée) |
| §6.2 Tableau | Infection invasive maternelle classée « drapeau rouge » | Mineure | Classée parmi les « autres » facteurs (NG195) | S2 |
| §8.3 Signes OMS d'infection grave possible | Seuil fébrile de 37,5 °C (ancienne PCIME) ; respiration rapide sans limite d'âge | **Majeure** | ≥ 38 °C ; ≥ 60/min de 0 à 6 jours ; signes de maladie critique ; conduite si la référence est impossible | S15, S16 (DOC-00052, DOC-00034) |
| §13.3 et §21, colonne OMS | OMS 2015 présentée comme actuelle ; colonne méningite « selon protocole » | **Majeure** (actualité) | OMS 2024 : ampicilline + gentamicine ≥ 10 j (sepsis) ; ampicilline, céfotaxime ou ceftriaxone + gentamicine ≥ 3 semaines (méningite) ; schémas ambulatoires actualisés (A.2–A.5) | S15 |
| §13.2 Amoxicilline/ampicilline | Marqueur unique sur une dose standard | Mineure | Dose générale sourcée ; dose méningée isolée (marqueur) | S8, S15 |
| §13.2 Benzylpénicilline | Marqueur | Mineure | Sourcée (NICE, OMS) | S2, S8 |
| §13.2 Gentamicine | Incomplet | Mineure | 7,5 mg/kg après la 1ʳᵉ semaine ; 36 h hors AMM | S2, S8, S15 |
| §13.2 Céfotaxime | Rythme après la 1ʳᵉ semaine non sourcé | Mineure | Rythmes OMS 2013/2024 détaillés | S8, S15 |
| §13.2 Aciclovir | Marqueur ; surveillance hématologique absente | Mineure | Schéma sourcé ; neutrophiles | S11 |
| §13.2 Glycémie | Marqueur | Mineure | Schéma OMS | S8 |
| Sources | S1 attribuée à la « HAS » (RBP SFN/SFP labellisée HAS) ; S2, S8, S9, S11 non vérifiées | Mineure | S1 corrigée et vérifiée ; S2, S8, S9, S11 vérifiées ; S15, S16 ajoutées ; mention du marqueur dans l'avertissement reformulée (comptage du validateur) | — |

Points jugés exacts : définitions (précoce < 72 h ; < 7 jours pour le SGB aux États-Unis), germes, facteurs de risque (fièvre ≥ 38 °C ; RPM ≥ 12 h HAS, ≥ 18 h CDC), Triple I, CRP (deux valeurs normales à 24 h d'intervalle), hémoculture ≥ 1 mL, Listeria et céphalosporines, ceftriaxone, antibioprophylaxie adéquate si ≥ 4 h, pas d'antibioprophylaxie en cas de césarienne avant travail à membranes intactes, durées (SGB 10 j ; méningite à SGB ≥ 14 j ; méningite à Gram négatif ≥ 21 j). QCM-NEON-0013 à 0024 : exacts (QCM-NEON-0021 : explication posologique sourcée). Cas CAS-NEON-0003/0004 exacts (dose d'aciclovir précisée dans CAS-NEON-0004).

## Reste à faire
1. **[POSOLOGIE À VÉRIFIER]** restants (7) : doses méningées d'amoxicilline et de céfotaxime, vancomycine, méropénem, antifongiques, remplissage et amines, antibioprophylaxie obstétricale.
2. Références non vérifiées : S3 et S4 (AAP 2018), S5, S6 (CDC 2010), S7 (ACOG 2020), S10.
3. Formulation exacte des posologies de la RBP SFN/SFP 2017 (gentamicine en particulier) ; durées NICE pour la listériose.
4. Écologie bactérienne et protocoles nationaux algériens ; politique de dépistage du SGB.
