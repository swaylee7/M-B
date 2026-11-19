# Rapport d'audit — DOS-SPUB-0001 « Organisation sanitaire et fonctionnement du système de santé algérien »

- **Date** : 2026-11-19
- **Auditeurs** : AUD-01 (audit scientifique, IA) et AUD-04 (références, IA), indépendants du rédacteur DOS-15. Pas de posologie (AUD-02 sans objet).
- **Version auditée** : 1.0 → **version produite : 1.1**
- **Verdict** : **audite_corrections_requises**. Aucune erreur critique ou majeure restante, mais des textes organisationnels importants n'ont toujours pas été consultés (voir « Reste à faire »).
- **Bilan** : 30 corrections (critiques 0, majeures 1, mineures 29). AUD-01 : 21 ; AUD-04 : 9 (S7, S8 et S18, S19 comptées séparément).

## Documents acquis par l'audit (ACQ-01, via `acquerir.py`)

Destination : `15_AUTRES_SPECIALITES/49_SPUB_SANTE_PUBLIQUE/00_PROGRAMME_OBJECTIFS/textes_officiels/` ; 5,2 Mo au total (plafond : 40 Mo).

| DOC | Numéro du JORADP | Texte(s) | Lecture |
|---|---|---|---|
| DOC-00114 | n° 33 du 20/05/2007 | Décret exécutif 07-140 (EPH, EPSP) | pdftotext |
| DOC-00115 | n° 81 du 10/12/1997 | Décrets exécutifs 97-465 (EHS), 97-466 (secteurs sanitaires), 97-467 (CHU) | OCR tesseract (scan) |
| DOC-00116 | n° 50 du 30/08/2020 | Ordonnance 20-02 modifiant la loi 18-11 | pdftotext |
| DOC-00117 | n° 1 du 01/01/1974 | Ordonnance 73-65 (médecine gratuite) | OCR (scan) |
| DOC-00118 | n° 2 de 1992 | Décret exécutif 92-07 (CNAS, CNR, CASNOS) | OCR (scan) |

## Conformité à la loi 18-11 (DOC-00074)

Articles relus un à un et trouvés conformes à leur reformulation :
- art. 1-8, 11-28 (l'art. 23, al. 2 vise les mineurs et incapables), 31, 35-48 ;
- art. 84-103, 120, 165-170, 189-198, 204 ;
- art. 265-345, dont l'art. 298 (CHU, EHS, circonscription sanitaire, établissement d'aide médicale d'urgence) ;
- art. 442-449 ; neuf titres.

Deux écarts ont été trouvés : la loi a été modifiée par l'ordonnance 20-02 (art. 308, 379, 381…), et l'art. 92 est mal rattaché (voir ci-dessous).

## Corrections

| Section | Problème | Gravité | Correction | Source |
|---|---|---|---|---|
| § 4.1 | Le ministre de la santé « délivre les autorisations d'études cliniques (art. 381) » : faux depuis 2020. | **majeure** | Ministre chargé de l'industrie pharmaceutique (art. 381 modifié), qui exerce aussi les compétences relatives aux produits pharmaceutiques. | Ordonnance 20-02 (DOC-00116) |
| § 2, ligne 2020 | Contenu de l'ordonnance 20-02 « à vérifier ». | mineure | Objet précisé (20 articles ; pharmacie et études cliniques). | DOC-00116 |
| § 2, ligne 1973-1974 | « Appliquée au 1er janvier 1974 » : le texte ne fixe pas de date d'application. | mineure | Art. 1er reformulé ; publication au JORADP du 1er janvier 1974. | DOC-00117 |
| § 2, lignes 1980-1990 et 1997 | Secteurs sanitaires datés des « années 1980-1990 [À VÉRIFIER] » : ils existaient dès 1973 (ordonnance 73-65), et leurs règles ont été fixées en 1997 par le décret 97-466. | mineure | Chronologie corrigée ; décret 97-466 ajouté. | DOC-00115, DOC-00117 |
| § 2, ligne 2007 | Abrogation de 97-466 non mentionnée. | mineure | Art. 35 du décret 07-140. | DOC-00114 |
| § 4.3 | Missions des services extérieurs non citées. | mineure | Art. 267 : répartition des ressources, coordination et suivi des programmes. | Loi 18-11 |
| § 4.3 | Tutelle des établissements omise. | mineure | Tutelle du wali sur les EPH, EPSP et EHS. | 07-140, art. 2 et 6 ; 97-465, art. 2 |
| § 5.4, ligne CHU | « Double tutelle [À VÉRIFIER] ». | mineure | EPA ; tutelle administrative de la santé et pédagogique de l'enseignement supérieur ; missions des art. 3-4. | 97-467 |
| § 5.4, ligne EHS | « Peut être érigé en structure de référence [À VÉRIFIER] » : non retrouvé dans le texte. | mineure | Agrément possible pour des activités hospitalo-universitaires (art. 7) ; définition (art. 3) ; 3 catégories (art. 8). | 97-465 |
| § 5.4, ligne EPH | Missions « à vérifier ». | mineure | Art. 2-4 du décret. | 07-140 |
| § 5.4, ligne EPSP | Missions « à vérifier ». | mineure | Art. 6-8 du décret. | 07-140 |
| § 5.4, paragraphe | Classement des établissements imprécis. | mineure | Arrêté interministériel (art. 23) ; 97-466 abrogé. | 07-140 |
| § 5.4, SEMEP et UDS | SEMEP présentés comme fonctionnant « au sein des EPSP et EPH » sans base réglementaire. | mineure | Formulation prudente (absents des textes consultés) ; structures de dépistage et de suivi en milieu éducatif (art. 94-96). | Loi 18-11 |
| § 6 | Liste de l'art. 308 périmée (« officines et établissements pharmaceutiques »). | mineure | « Officines » (art. 308 modifié). | DOC-00116 |
| § 7, ANPP | Tutelle de l'agence non précisée. | mineure | Tutelle du ministre chargé de l'industrie pharmaceutique (art. 224 modifié). | DOC-00116 |
| § 9.2 | CNAS et CASNOS « classiquement décrites », sans texte. | mineure | Décret 92-07, art. 1er à 3 : CNAS, CNR, CASNOS ; tutelle du ministre chargé de la sécurité sociale. | DOC-00118 |
| § 9.3 | Participation des bénéficiaires citée sans sa limite. | mineure | Art. 334, al. 2 : la non-contribution ne peut faire obstacle aux soins, notamment urgents. | Loi 18-11 |
| § 10, tableau | « Santé au travail : art. 92 et suivants » : l'art. 92 concerne les victimes de violences. | mineure | Art. 92, 94-96, 97-100, 101, 103 correctement répartis. | Loi 18-11 |
| § 11 | Mort violente : rôle du médecin légiste omis. | mineure | Partie médicale renseignée par le médecin légiste (art. 6). | Décret 22-178 |
| § 13, tableau des données | Chiffres ONS et STEPS présentés comme des données de l'ONS ou de l'OMS. | mineure | « Relayé par la presse » ou « communiqué » ; ce ne sont pas des chiffres officiels vérifiés ; marqueur ajouté. | — |
| § 20, bandeau | Divergence sur les modifications « selon le registre » ; statut « brouillon ». | mineure | Ordonnance 20-02 décrite ; statut d'audit. | DOC-00116 |
| S1 (AUD-04) | Ordonnance 20-02 « non consultée ». | mineure | Lue ; liste des articles modifiés. | DOC-00116 |
| S6 (AUD-04) | Décret 07-140 non consulté. | mineure | Acquis, URL, contenu. | DOC-00114 |
| S7, S8 (AUD-04) | Décrets 97-467 et 97-465 non consultés ; intitulé de 97-465 « à vérifier ». | mineure | Acquis ; intitulés et contenus confirmés. | DOC-00115 |
| S9 (AUD-04) | Ordonnance 73-65 : intitulé « à vérifier » ; date d'application inexacte. | mineure | Intitulé exact ; JORADP n° 1/1974. | DOC-00117 |
| S18, S19 (AUD-04) | Remarques sur l'accès aux sources. | mineure | Hôtes inaccessibles et marqueur. | — |
| S24 (AUD-04) | Source manquante. | mineure | Ordonnance 20-02 ajoutée. | DOC-00116 |
| S25 (AUD-04) | Source manquante. | mineure | Décret 92-07 ajouté. | DOC-00118 |

## Points vérifiés sans modification

- Principes (art. 3-6), gratuité (art. 13), médecin référent (art. 22).
- Carte sanitaire et schéma d'organisation sanitaire (art. 266, 269-271).
- Niveaux de soins (art. 283-285) ; statut de l'établissement public de santé (art. 297-304).
- Secteur privé (art. 305-315, hors art. 308) ; système national d'information sanitaire (art. 319-323) ; évaluation et audit (art. 324-328).
- Financement (art. 329-338) ; service civil (art. 196-197) ; formation continue (art. 170).
- Abrogation de la loi 85-05 et maintien de ses textes d'application (art. 449).
  - Les décrets 97-465, 97-467 et 07-140 visent bien la loi 85-05.
  - Ils restent donc applicables tant que les textes d'application de la loi de 2018 (art. 298) n'ont pas été pris.
- Liste des MDO (catégories 1 et 2 ; rougeole, brucellose et TIAC en catégorie 1).
- QCM 1 à 10 du dossier : exacts.

## QCM et cas associés

- **QCM-SPUB-1501 à 1513** → `audite_valide`. Explications corrigées :
  - 1502 : art. 7, 8 et 35 du décret 07-140 ;
  - 1508 : liste de l'art. 308 modifiée ;
  - 1512 E : ordonnance 73-65 sans date d'application.
- **CAS-SPUB-1501** (rougeole) → `audite_valide`.
  - **Marqueur posologique levé** : vitamine A 200 000 UI à J1 et à J2 entre 12 mois et 5 ans (100 000 UI entre 6 et 11 mois ; 50 000 UI avant 6 mois ; 3e dose si signes oculaires).
  - Source : OMS, Mémento de soins hospitaliers pédiatriques 2015 (DOC-00062) et aide-mémoire OMS sur la rougeole relu (deux doses pour tout cas suspect de moins de 5 ans).
- **CAS-SPUB-1502** (centre d'hémodialyse) → `audite_valide`.
  - Articles cités vérifiés ; l'autorisation relève toujours du ministre de la santé (art. 307 non modifié).
  - Modalités financières des conventions laissées « à vérifier ».

## Reste à faire

1. Texte de création et missions de l'**INSP** ; base réglementaire des **SEMEP** et des unités de dépistage et de suivi (probablement des arrêtés ministériels non publiés au JORADP).
2. Décret 11-379 (attributions du ministre) et organigramme de l'administration centrale ; texte d'organisation des directions de wilaya (dénomination DSP).
3. Modifications ultérieures des décrets 07-140 (dont 14-362), 97-465, 97-467 et 92-07 ; loi 20-12 approuvant l'ordonnance 20-02 ; modifications éventuelles de la loi 18-11 après 2020.
4. Sécurité sociale : carte Chifa, tiers payant, taux de remboursement, conventions hôpitaux–CNAS (« forfait hospitalier »).
5. Chiffres ONS 2023 et STEPS 2016-2017 : sources primaires (ons.dz, cdn.who.int inaccessibles).
6. S20 (OMS 2007) et S21 (Alma-Ata, Astana) : non revérifiées.
7. Relecture par un enseignant de santé publique.
