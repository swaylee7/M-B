# Rapport d'audit — DOS-PEDI-0002 « Vaccinations : bases immunologiques, contre-indications, PEV (calendrier algérien) »

- Date : 2026-11-19 — Auditeurs : AUD-01 et AUD-02 (IA)
- Version auditée : 1.0 → version corrigée : 1.1
- Verdict : **audite_corrections_requises** (aucune erreur critique ; erreur majeure corrigée ; aucun marqueur de posologie restant ; références internationales des contre-indications non vérifiées et points du calendrier encore ouverts)

## Contrôle du calendrier sur les textes officiels (`pdftotext -layout`)
- **DOC-00070, arrêté du 3/07/2018 (JORADP n° 49 du 8/08/2018, p. 29-30)** : naissance BCG + hépatite B ; 2 mois DTCa, Hib, VPI, hépatite B, « anti-pneumococcique 13 » ; 4 et 12 mois mêmes valences + VPO ; 11 et 18 mois ROR ; 6 ans DTCa (pédiatrique) + VPI ; 11–13 ans, 16–18 ans et tous les 10 ans dès 18 ans : dT (adulte). Le texte abroge l'arrêté de 2014. Le tableau du §13.4 est **conforme**.
- **DOC-00071, arrêté du 28/04/2026 (JORADP n° 36 du 17/05/2026, p. 39-40)** : « complète » le tableau ; 2 mois : ajout du VPO ; 2, 4 et 12 mois : « anti-pneumococcique » sans valence ; 11–13 ans : dT + « anti human papilloma-virus » ; reste sans changement. Les visas citent l'arrêté de 2018 « modifié » et la loi 18-11 « modifiée et complétée ». Le dossier est **conforme**.
- **DOC-00076, arrêté du 24/11/2014 (JORADP n° 75 du 28/12/2014, p. 30-31), remplacé** : naissance BCG, VPO, hépatite B ; 2, 4 et 12 mois D, T, coqueluche, Hib, hépatite B, VPO, pneumocoque ; 3 mois VPI ; ROR à 11 et 18 mois ; 6 ans D, T, coqueluche, VPO ; 11–13 ans dT + VPO ; 16–18 ans et tous les 10 ans dT ; abroge l'arrêté du 15/07/2007. Le tableau est **conforme** (6 doses de VPO), sauf deux qualificatifs que le texte ne contient pas (voir les corrections).
- **Points ouverts, traités sans rien affirmer au-delà des textes** : (1) **pas de VPO à la naissance** dans les arrêtés de 2018 et 2026 ; le guide pratique 2023 [S5], lu seulement par extraits, en mentionnerait un : discordance maintenue avec la mention [À VÉRIFIER] ; (2) **arrêté modificatif intermédiaire** de 2018 : une recherche web ciblée n'a retrouvé que l'arrêté de 2026 ; (3) **HPV** : l'arrêté ne précise ni le sexe, ni le nombre de doses, ni le cadre (scolaire) ; le dossier le dit.

## Corrections
| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §10.3 BCG et VIH | Position OMS 2018 mal restituée : pour le nourrisson de statut inconnu né de mère infectée, la décision était dite « selon la prévalence de la tuberculose… », alors que l'OMS recommande de le **vacciner** s'il n'a aucun signe d'infection par le VIH ; exception de l'enfant traité et stable omise | **Majeure** | Section réécrite selon la note OMS 2018 | S16 (vérifiée, REH 2018;93(8):73-96) |
| §7.3 BCG | Exception de l'enfant sous traitement antirétroviral non mentionnée | Mineure | Ajoutée | S16 |
| §13.4 Calendrier 2014 | « À germes entiers » et « pentavalente » présentés comme le contenu de l'arrêté, qui ne mentionne que « anti-coquelucheux » | Mineure | Reformulé : « en pratique », source CNPM [S9] | DOC-00076 |
| §12.3 Anaphylaxie | Marqueur de posologie sur l'adrénaline IM 0,01 mg/kg (max 0,5 mg), dose standard | Mineure | Marqueur levé ; ajout de la dose fixe OMS (0,15 mL de solution à 1 mg/mL IM, renouvelable toutes les 5–15 min) | S21 = Pocket book 2013, DOC-00063 |
| §13.4 Cadre réglementaire | Recherche de l'arrêté intermédiaire non tracée | Mineure | Résultat de la recherche de l'audit ajouté | — |
| Sources | S16 non vérifiée ; pas de source pour l'adrénaline | Mineure | S16 vérifiée (URL OMS) ; S21 ajoutée | — |
| Lot | QCM-PEDI-0023 : explication « posologie à vérifier » | Mineure | Explication sourcée (Pocket book) | DOC-00063 |

Points jugés exacts : réponses primaire et secondaire ; conjugaison ; corrélats de protection (Plotkin) ; contre-indications vraies et fausses (encéphalopathie dans les 7 jours, anaphylaxie, déficit immunitaire, grossesse ; allergie à l'œuf non contre-indiquante) ; précautions coquelucheuses (≥ 40 °C, comme dans le RCP européen) ; immunoglobulines et vaccins vivants (3–11 mois) ; chaîne du froid, pastille de contrôle, test d'agitation, flacons entamés (28 j / 6 h) ; maladies à déclaration obligatoire (décret 22-250). QCM-PEDI-0013 à 0024 et cas CAS-PEDI-0003/0004 : exacts.

## Reste à faire
1. Vérifier S13 (tableaux OMS), S14 (ACIP, fondement des contre-indications et des seuils de corticothérapie), S15 (Plotkin), S17 (OMS 2015/2014).
2. Lire en entier le guide pratique 2023 (S5) pour trancher la question du VPO à la naissance ; identifier l'éventuel arrêté modificatif de 2018 (JORADP 2018–2026).
3. Obtenir les instructions ministérielles sur le HPV (sexe, doses, cadre scolaire) et la valence du vaccin pneumococcique.
4. Colonnes « France » et « OMS » du §21 : nombreux [À VÉRIFIER] (calendrier français 2026 non lu).
