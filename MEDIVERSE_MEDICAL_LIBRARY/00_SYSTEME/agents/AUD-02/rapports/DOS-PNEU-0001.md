# Rapport d'audit — DOS-PNEU-0001 « Tuberculose pulmonaire et programme national algérien »

- **Date** : 2026-11-19 — **Auditeurs** : AUD-01, AUD-02, AUD-04 (IA)
- **Objets audités** : dossier v1.0 (DOS-02), QCM-PNEU-0001…0013, CAS-PNEU-0001, CAS-PNEU-0002
- **Verdict** : `audite_corrections_requises` (v1.1) — aucune erreur critique ; contenu de l'instruction n°07/2024 non confirmable ; marqueurs de posologie restants (tranches de poids nationales, formes pédiatriques, pyridoxine, insuffisance rénale).

## Instruction MS (DGPPS) n°07 du 21/03/2024
- WebFetch sur sapp.dz : **échec** (hôte non résolu dans la session) ; recherche web : texte non retrouvé.
- Existence du document : confirmée par le rédacteur (DOS-02) ; **contenu (2HRZE/4HR pour tous les nouveaux cas, abandon de 2SHRZE/1HRZE/5HRE) non confirmé par l'audit**. Toutes les mentions sont désormais formulées « selon les extraits disponibles, à confirmer » (état au 19/11/2026). L'abandon du schéma de retraitement par l'OMS reste, lui, établi.
- Instruction ITL 2024 et manuel MSPRH/INSP 2011 : non consultés (même limite).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| §13.3 a, §18, §21 (×2), QCM 5 du dossier, QCM-PNEU-0005, QCM-PNEU-0013, CAS-PNEU-0002 | Contenu de l'instruction n°07/2024 présenté comme établi alors que le texte n'a pas été lu | majeure (traçabilité d'un texte officiel) | Formulation « selon les extraits disponibles, à confirmer » | — |
| §14.3 | Schéma provisoire non hépatotoxique « éthambutol + streptomycine ou fluoroquinolone » (bithérapie) | mineure | Au moins 3 médicaments non hépatotoxiques (ex. éthambutol + fluoroquinolone + aminoside), avis spécialisé | ATS 2006 [S16] (connaissance établie ; texte non relu) |
| §13.2 | Marqueurs sur la dose maximale du pyrazinamide et de l'éthambutol | mineure | Pas de plafond dans le dosage OMS par tranches de poids ; 2 g/j (Z) et 1,6 g/j (E) dans le tableau ATS/CDC/IDSA [S15] | ATS/CDC/IDSA 2016 |
| YAML / §22 | S15, S16 non vérifiées | mineure | Vérifiées (PubMed 27516382 ; URL ATS) | Recherche web |
| YAML S2 | Remarque de vérification incomplète | mineure | Ajout de l'échec d'accès de l'audit | — |
| En-tête, « reste à faire » | Traçabilité | mineure | Mise à jour | — |

## Vérifications sans correction
- Doses OMS par kg (adulte H 5, R 10, Z 25, E 15 ; enfant H 10, R 15, Z 35, E 20, avec intervalles) : exactes.
- Comprimés RHZE 150/75/400/275 et RH 150/75 ; tranches 30–39 / 40–54 / 55–70 / ≥ 71 kg (2/3/4/5) : conformes aux tranches OMS classiques ; non recoupées en ligne (recherche infructueuse) → marqueur conservé (la borne basse varie selon les éditions et les guides : à confirmer dans le manuel opérationnel OMS et le protocole national).
- Formes pédiatriques RHZ 75/50/150, RH 75/50, E 100 : exactes ; tableau par poids absent → marqueur conservé.
- Schémas 4 mois : 2HPZM/2HPM dès 12 ans (Study 31/A5349 : 15,5 % contre 14,6 %) ; SHINE 2HRZ(E)/2HR de 3 mois à 16 ans, 1 204 enfants : exacts.
- Échelle de lecture des BAAR, définitions des résultats, seuils d'hépatotoxicité ATS, TPT (6H, 3HR, 3HP, 1HP, 4R), définitions pré-XDR/XDR : exacts.

**Erreurs critiques** : aucune.

## QCM et cas
QCM-PNEU-0001…0013 exacts ; `audite_valide` sauf QCM-PNEU-0005, 0010, 0013 (`audite_corrections_requises` : dépendent du contenu non confirmé de l'instruction 2024 ou du manuel 2011). CAS-PNEU-0001 (tranches de poids) et 0002 (instruction) : `audite_corrections_requises`.

## Références (AUD-04)
Avant : 13/16 vérifiées. Après : 15/16 (S15, S16 ajoutées) ; S14 (OMS module 3) non vérifiée. Sources de presse S5, S13 : vérifiées comme existantes mais secondaires, à remplacer.

## Reste à faire
1. Autoriser l'hôte sapp.dz et lire l'instruction n°07/2024 (schémas, durées par localisation, retraitement, tranches de poids, calendrier des contrôles M2/M4/M6 ou M2/M5/M6) et l'instruction ITL 2024.
2. Lire le manuel 2011 (TPM+/TPM0, seuil de toux, organisation, objectifs).
3. Tableaux de poids OMS (adulte et enfant) : confronter au manuel opérationnel OMS module 4 (2025).
4. Pyridoxine et adaptation à l'insuffisance rénale : protocole national.
5. Remplacer S5 et S13 (presse) par les publications INSP/MSPRH ; vérifier S14.
