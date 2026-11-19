# Journal — ANA-19

Mission : Catalogue vérifié des ouvrages de référence et structuration des contenus — Pédiatrie-néonatologie

- 2026-11-19T00:49:09+00:00 — poste créé (aucune exécution encore).
- 2026-11-19T01:25:21+00:00 — poste couvert par ANA-01 (catalogue consolidé, 440 ouvrages en 5 lots ANA-*.json) ; voir journal ANA-01.

## 2026-11-19T02:29:28+00:00 — Volet encyclopédie (§11) : référentiel des pathologies, lots ENC-2

Mission (postes ANA-19 + ANA-20, volet encyclopédie) : référentiel des pathologies des spécialités pédiatriques,
gynéco-obstétricales, chirurgicales et transversales. Spécialités médicales traitées en parallèle par ENC-1 (non traitées ici).

**Produits** (agent des lots : `ENC-2`, statut de chaque entrée : `referentiel_a_auditer`, `dossier: null`) :
  - `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-2-PEDIATRIE.json` — 112 pathologies (PEDI 38, NEON 41, CPED 33)
  - `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-2-GYNECO_OBSTETRIQUE_UROLOGIE.json` — 113 pathologies (GYNE 35, OBST 45, UROL 33)
  - `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-2-CHIRURGIE_VISCERALE_THORACIQUE_VASCULAIRE.json` — 86 pathologies (CGEN 21, CDIG 36, CTHO 13, CCVA 16)
  - `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-2-LOCOMOTEUR_NEUROCHIRURGIE_PLASTIQUE_MPR.json` — 139 pathologies (ORTH 36, TRAU 43, NCHI 32, CPLA 15, MPR 13)
  - `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-2-TETE_ET_COU.json` — 104 pathologies (ORL 37, OPHT 46, DENT 21)
  - `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-2-URGENCES_REANIMATION_ANESTHESIE.json` — 64 pathologies (URGE 33, MINT_REA 14, ANES 17)
  - `22_ENCYCLOPEDIE_PATHOLOGIES/00_REFERENTIEL/lots/ENC-2-TRANSVERSAL_MLEG_MTRA_SPUB_EPID_ANAP.json` — 66 pathologies (MLEG 17, MTRA 18, SPUB 10, EPID 4, ANAP 17)

**Chiffres** : 684 pathologies ; 86 maladies rares (`maladie_rare: true`) ; CIM-10 renseignée pour 554 (81.0 %) ;
241 entrées reliées à au moins un item du résidanat (90 items distincts) ; 1960 liens `pathologies_liees` (symétriques).

**Méthode**
- Sources compactes rédigées puis compilées par script (ids `PATH-<CODE>-nnnn` attribués par spécialité, sous-spécialités contrôlées
  contre `config/specialites.yaml`, items contrôlés contre `programme_residanat.json`).
- Contenu factuel standard (symptômes, signes, examens clés, traitements par classes/techniques, **aucune posologie**).
- CIM-10 OMS renseignée **uniquement si certaine** ; sinon `null` (codes à 3 caractères préférés en cas de doute sur la 4e position).
- Validation : JSON relu, unicité des ids (aucune collision avec ENC-1), existence de chaque id de `pathologies_liees`
  (liens restreints aux ids ENC-2 ; 232 références vers des entrées retirées ont été supprimées), champs obligatoires non vides.

**Dédoublonnage avec ENC-1** (lots ENC-1 lus le 2026-11-19 vers 02:20 UTC, 885 entrées) :
136 entrées rédigées ont été **retirées** car l'entité existait déjà chez ENC-1 (même maladie, même portée). Ont été **conservées**
les entités à angle distinct : formes néonatales/pédiatriques (ex. SN idiopathique de l'enfant, RGO du nourrisson, tétanos néonatal),
complications chirurgicales (ex. complications du kyste hydatique du foie, ulcère perforé, rupture d'AAA), localisations d'organe
(kyste hydatique du rein, cérébral, osseux). Recouvrements résiduels à arbitrer par l'audit : obésité de l'enfant / obésité morbide
(vs PATH-ENDO-0049), asthme du nourrisson (vs PATH-PNEU-0001), canal artériel du prématuré (vs PATH-CARD-0059), rupture de la coiffe
(vs PATH-RHUM-0037), intoxication au paracétamol (vs PATH-HEPA-0022), méthémoglobinémie aux nitrates (vs PATH-HEMA-0019), amylose (ANAP).
Ajouts compensatoires (59 entités absentes du référentiel ENC-1) : CDIG (complications postopératoires, carcinose, stomies…),
PEDI (rhinopharyngite, PIMS, épilepsie rolandique, troubles du langage…), UROL, ORTH, NCHI, CPLA, MPR, MINT_REA.

Correspondance des entrées retirées → entité ENC-1 de référence (pour le recâblage des liens lors de la fusion) :

| Spécialité | Entrée retirée | Entité ENC-1 |
|---|---|---|
| PEDI | Rachitisme carentiel en vitamine D | PATH-ENDO-0037 Carence en vitamine D et rachitisme carentiel |
| PEDI | Scarlatine | PATH-INFE-0059 Scarlatine |
| PEDI | Rhumatisme articulaire aigu de l'enfant | PATH-CARD-0028 Rhumatisme articulaire aigu |
| PEDI | Glomérulonéphrite aiguë post-streptococcique de l'enfant | PATH-NEPH-0001 Glomérulonéphrite aiguë post-infectieuse (syndrome néphritique aigu) |
| PEDI | Syndrome hémolytique et urémique de l'enfant | PATH-NEPH-0013 Syndrome hémolytique et urémique typique (STEC) |
| PEDI | Convulsions fébriles du nourrisson | PATH-NEUR-0014 Convulsions fébriles du nourrisson |
| PEDI | Épilepsie-absences de l'enfant | PATH-NEUR-0011 Épilepsie-absences de l'enfant |
| PEDI | Syndrome de West | PATH-NEUR-0013 Syndrome de West (spasmes infantiles) |
| PEDI | Diabète de l'enfant (type 1) | PATH-DIAB-0001 Diabète de type 1 |
| PEDI | Hypothyroïdie congénitale | PATH-ENDO-0009 Hypothyroïdie congénitale |
| PEDI | Hyperplasie congénitale des surrénales (déficit en 21-hydroxylase) | PATH-ENDO-0027 Hyperplasie congénitale des surrénales (déficit en 21-hydroxylase) |
| PEDI | Puberté précoce | PATH-ENDO-0047 Puberté précoce |
| PEDI | Retard pubertaire | PATH-ENDO-0046 Retard pubertaire |
| PEDI | Mucoviscidose | PATH-GENE-0024 Mucoviscidose |
| PEDI | Maladie cœliaque de l'enfant | PATH-GAST-0020 Maladie cœliaque |
| PEDI | Glycogénose de type I (maladie de von Gierke) | PATH-GENE-0028 Glycogénose de type I (maladie de von Gierke) |
| PEDI | Anémie ferriprive de l'enfant | PATH-HEMA-0001 Anémie par carence martiale |
| PEDI | Histiocytose langerhansienne de l'enfant | PATH-HEMA-0055 Histiocytose langerhansienne |
| PEDI | Arthrite juvénile idiopathique | PATH-RHUM-0006 Arthrite juvénile idiopathique |
| NEON | Toxoplasmose congénitale | PATH-PARA-0009 Toxoplasmose congénitale |
| NEON | Phénylcétonurie | PATH-GENE-0025 Phénylcétonurie |
| NEON | Galactosémie congénitale | PATH-GENE-0026 Galactosémie congénitale |
| CPED | Atrésie des voies biliaires | PATH-HEPA-0047 Atrésie des voies biliaires |
| CPED | Néphroblastome (tumeur de Wilms) | PATH-ONCO-0028 Néphroblastome (tumeur de Wilms) |
| CPED | Neuroblastome | PATH-ONCO-0027 Neuroblastome |
| CPED | Hépatoblastome | PATH-HEPA-0048 Hépatoblastome |
| GYNE | Syndrome des ovaires polykystiques | PATH-ENDO-0042 Syndrome des ovaires polykystiques |
| GYNE | Insuffisance ovarienne prématurée | PATH-ENDO-0043 Insuffisance ovarienne prématurée |
| GYNE | Cancer du col de l'utérus | PATH-ONCO-0009 Cancer du col de l'utérus |
| GYNE | Cancer de l'endomètre | PATH-ONCO-0010 Cancer de l'endomètre |
| GYNE | Cancer de l'ovaire | PATH-ONCO-0008 Cancer de l'ovaire |
| GYNE | Cancer de la vulve | PATH-ONCO-0011 Cancer de la vulve |
| GYNE | Choriocarcinome gestationnel | PATH-ONCO-0013 Tumeurs trophoblastiques gestationnelles (môle hydatiforme, choriocarcinome) |
| GYNE | Sarcome utérin | PATH-ONCO-0012 Sarcomes utérins (léiomyosarcome) |
| GYNE | Cancer du sein | PATH-ONCO-0001 Cancer du sein |
| OBST | Diabète gestationnel | PATH-DIAB-0010 Diabète gestationnel |
| OBST | Diabète préexistant et grossesse | PATH-DIAB-0011 Diabète préexistant et grossesse |
| OBST | Môle hydatiforme | PATH-ONCO-0013 Tumeurs trophoblastiques gestationnelles (môle hydatiforme, choriocarcinome) |
| OBST | Troubles psychiques du post-partum (dépression et psychose puerpérales) | PATH-PSYC-0011 Dépression du post-partum ; PATH-PSYC-0012 Psychose puerpérale |
| UROL | Lithiase urinaire | PATH-NEPH-0032 Lithiase urinaire |
| UROL | Anurie obstructive | PATH-NEPH-0019 Uropathie obstructive (insuffisance rénale aiguë obstructive) |
| UROL | Cancer de la prostate | PATH-ONCO-0002 Adénocarcinome de la prostate |
| UROL | Cancer de la vessie | PATH-ONCO-0003 Cancer de la vessie |
| UROL | Cancer du rein de l'adulte | PATH-ONCO-0004 Cancer du rein (carcinome à cellules rénales) |
| UROL | Tumeur de la voie excrétrice urinaire supérieure | PATH-ONCO-0005 Tumeurs urothéliales de la voie excrétrice supérieure |
| UROL | Cancer du testicule | PATH-ONCO-0006 Tumeurs germinales du testicule |
| UROL | Cancer du pénis | PATH-ONCO-0007 Cancer de la verge |
| UROL | Prostatite aiguë | PATH-INFE-0054 Prostatite aiguë |
| UROL | Tuberculose uro-génitale | PATH-NEPH-0036 Tuberculose urogénitale |
| CGEN | Nodule thyroïdien | PATH-ENDO-0011 Nodule thyroïdien |
| CGEN | Adénome parathyroïdien (hyperparathyroïdie primaire chirurgicale) | PATH-ENDO-0032 Hyperparathyroïdie primaire |
| CDIG | Cancer de l'œsophage | PATH-GAST-0007 Cancer de l'œsophage |
| CDIG | Cancer de l'estomac | PATH-GAST-0012 Adénocarcinome de l'estomac |
| CDIG | Achalasie de l'œsophage | PATH-GAST-0004 Achalasie de l'œsophage |
| CDIG | Diverticule de Zenker | PATH-GAST-0005 Diverticule de Zenker |
| CDIG | Lésions caustiques de l'œsophage et de l'estomac | PATH-GAST-0008 Œsophagite caustique (ingestion de caustiques) |
| CDIG | Tumeur stromale gastro-intestinale (GIST) | PATH-GAST-0014 Tumeur stromale gastro-intestinale |
| CDIG | Kyste hydatique du foie | PATH-HEPA-0042 Kyste hydatique du foie |
| CDIG | Lithiase vésiculaire | PATH-HEPA-0032 Lithiase vésiculaire |
| CDIG | Cholécystite aiguë lithiasique | PATH-HEPA-0033 Cholécystite aiguë lithiasique |
| CDIG | Lithiase de la voie biliaire principale | PATH-HEPA-0034 Lithiase de la voie biliaire principale |
| CDIG | Angiocholite aiguë | PATH-HEPA-0035 Angiocholite aiguë |
| CDIG | Pancréatite aiguë | PATH-GAST-0042 Pancréatite aiguë |
| CDIG | Cancer du pancréas | PATH-GAST-0043 Adénocarcinome du pancréas |
| CDIG | Cancer de la vésicule biliaire | PATH-HEPA-0036 Cancer de la vésicule biliaire |
| CDIG | Cholangiocarcinome (cancer des voies biliaires) | PATH-HEPA-0037 Cholangiocarcinome (cancer des voies biliaires) |
| CDIG | Ampullome vatérien | PATH-HEPA-0038 Ampullome vatérien |
| CDIG | Abcès hépatique à pyogènes | PATH-HEPA-0043 Abcès hépatique à pyogènes |
| CDIG | Métastases hépatiques (prise en charge chirurgicale) | PATH-HEPA-0044 Métastases hépatiques |
| CDIG | Cancer du côlon | PATH-GAST-0035 Cancer du côlon |
| CDIG | Cancer du rectum | PATH-GAST-0036 Cancer du rectum |
| CDIG | Ischémie mésentérique aiguë | PATH-GAST-0038 Ischémie mésentérique aiguë |
| CDIG | Polypose adénomateuse familiale | PATH-GAST-0034 Polypose adénomateuse familiale |
| CDIG | Maladie hémorroïdaire | PATH-GAST-0045 Maladie hémorroïdaire |
| CDIG | Fissure anale | PATH-GAST-0046 Fissure anale |
| CDIG | Fistule anale | PATH-GAST-0047 Abcès et fistule anale |
| CDIG | Abcès de la marge anale | PATH-GAST-0047 Abcès et fistule anale |
| CDIG | Cancer du canal anal | PATH-GAST-0037 Cancer du canal anal |
| CDIG | Tuberculose péritonéale | PATH-GAST-0031 Tuberculose abdominale (péritonéale et intestinale) |
| CTHO | Syndrome cave supérieur | PATH-ONCO-0034 Syndrome cave supérieur |
| ORTH | Ostéogenèse imparfaite | PATH-GENE-0017 Ostéogenèse imparfaite |
| ORTH | Ostéomyélite aiguë hématogène | PATH-INFE-0060 Ostéomyélite aiguë hématogène |
| ORTH | Arthrite septique | PATH-RHUM-0023 Arthrite septique |
| ORTH | Spondylodiscite infectieuse | PATH-RHUM-0026 Spondylodiscite à pyogènes |
| ORTH | Ostéosarcome | PATH-ONCO-0022 Ostéosarcome |
| ORTH | Sarcome d'Ewing | PATH-ONCO-0023 Sarcome d'Ewing |
| ORTH | Chondrosarcome | PATH-ONCO-0024 Chondrosarcome |
| ORTH | Métastases osseuses | PATH-ONCO-0025 Métastases osseuses |
| ORTH | Coxarthrose | PATH-RHUM-0014 Coxarthrose |
| ORTH | Gonarthrose | PATH-RHUM-0013 Gonarthrose |
| ORTH | Ostéonécrose aseptique de la tête fémorale | PATH-RHUM-0019 Ostéonécrose aseptique de la tête fémorale |
| ORTH | Spondylolisthésis | PATH-RHUM-0030 Spondylolisthésis |
| NCHI | Glioblastome | PATH-NEUR-0055 Glioblastome |
| NCHI | Gliome diffus de bas grade | PATH-NEUR-0056 Gliomes diffus de bas grade |
| NCHI | Méningiome | PATH-NEUR-0057 Méningiome |
| NCHI | Craniopharyngiome | PATH-ENDO-0021 Craniopharyngiome |
| NCHI | Médulloblastome | PATH-NEUR-0059 Médulloblastome |
| NCHI | Métastases cérébrales | PATH-NEUR-0058 Métastases cérébrales |
| NCHI | Abcès cérébral | PATH-INFE-0053 Abcès cérébral |
| NCHI | Hémorragie méningée par rupture d'anévrisme | PATH-NEUR-0004 Hémorragie sous-arachnoïdienne (hémorragie méningée) |
| NCHI | Hernie discale lombaire (lombosciatique) | PATH-RHUM-0027 Lombosciatique par hernie discale |
| NCHI | Hernie discale cervicale (névralgie cervico-brachiale) | PATH-RHUM-0031 Névralgie cervico-brachiale |
| NCHI | Canal lombaire étroit | PATH-RHUM-0029 Canal lombaire rétréci |
| NCHI | Myélopathie cervicarthrosique | PATH-NEUR-0064 Myélopathie cervicarthrosique |
| NCHI | Syndrome de la queue de cheval | PATH-NEUR-0061 Syndrome de la queue de cheval |
| NCHI | Compression médullaire non traumatique | PATH-NEUR-0060 Compression médullaire non traumatique |
| NCHI | Hydrocéphalie à pression normale | PATH-NEUR-0053 Hydrocéphalie chronique de l'adulte (à pression normale) |
| CPLA | Lymphœdème du membre supérieur après cancer du sein | PATH-ONCO-0044 Lymphœdème secondaire (après cancer du sein) |
| CPLA | Syndrome du canal carpien | PATH-NEUR-0042 Syndrome du canal carpien |
| MPR | Paralysie cérébrale (infirmité motrice cérébrale) | PATH-NEUR-0070 Paralysie cérébrale (infirmité motrice cérébrale) |
| MPR | Syndrome douloureux régional complexe (algodystrophie) | PATH-RHUM-0022 Syndrome douloureux régional complexe (algodystrophie) |
| MPR | Escarres | PATH-GERI-0010 Escarres (lésions de pression) |
| ORL | Presbyacousie | PATH-GERI-0019 Presbyacousie |
| ORL | Vertige positionnel paroxystique bénin | PATH-NEUR-0071 Vertige positionnel paroxystique bénin |
| ORL | Névrite vestibulaire | PATH-NEUR-0072 Névrite vestibulaire (déficit vestibulaire unilatéral aigu) |
| ORL | Cancer du cavum (carcinome nasopharyngé) | PATH-ONCO-0014 Cancer du cavum (carcinome du nasopharynx) |
| ORL | Cancer du larynx | PATH-ONCO-0015 Cancer du larynx |
| ORL | Cancer de la cavité buccale | PATH-ONCO-0016 Cancer de la cavité buccale |
| ORL | Cancer de l'oropharynx | PATH-ONCO-0017 Cancer de l'oropharynx |
| ORL | Cancer de l'hypopharynx | PATH-ONCO-0018 Cancer de l'hypopharynx |
| ORL | Cancers des glandes salivaires | PATH-ONCO-0019 Tumeurs malignes des glandes salivaires |
| OPHT | Rétinopathie diabétique | PATH-DIAB-0016 Rétinopathie diabétique |
| OPHT | Rétinoblastome | PATH-ONCO-0029 Rétinoblastome |
| DENT | Candidose buccale (muguet) | PATH-DERM-0035 Candidoses cutanéomuqueuses |
| DENT | Lichen plan buccal | PATH-DERM-0009 Lichen plan |
| URGE | Syndrome sérotoninergique | PATH-PSYC-0050 Syndrome sérotoninergique |
| MINT_REA | Choc septique | PATH-INFE-0005 Sepsis et choc septique (états septicémiques) |
| MINT_REA | Syndrome de renutrition inappropriée | PATH-GAST-0049 Syndrome de renutrition inappropriée |
| MINT_REA | Rhabdomyolyse aiguë | PATH-NEPH-0020 Rhabdomyolyse |
| ANES | Hyperthermie maligne peranesthésique | PATH-GENE-0039 Hyperthermie maligne peranesthésique |
| ANES | Accident hémolytique transfusionnel par incompatibilité ABO | PATH-HEMA-0058 Accidents de la transfusion sanguine |
| SPUB | Troubles dus à la carence en iode (goitre endémique) | PATH-ENDO-0012 Goitre simple et goitre endémique par carence iodée |
| EPID | Bactériémie liée au cathéter vasculaire | PATH-INFE-0056 Infections liées aux cathéters vasculaires |
| EPID | Colonisations et infections à bactéries multirésistantes (SARM, EBLSE) | PATH-INFE-0057 Infections à bactéries multirésistantes et hautement résistantes |
| EPID | Bactéries hautement résistantes émergentes (entérobactéries productrices de carbapénémases) | PATH-INFE-0057 Infections à bactéries multirésistantes et hautement résistantes |
| EPID | Toxi-infection alimentaire collective | PATH-INFE-0017 Toxi-infections alimentaires collectives |

**Limites**
- Contenu rédigé sans source citée par entrée (le schéma n'en prévoit pas) : à auditer (statut `referentiel_a_auditer`).
- SPUB (10) et EPID (4) sous le seuil de 12 chacun (14 cumulés) : la plupart des MDO et des infections associées aux soins
  spécifiques existent déjà chez ENC-1 (INFE) ; seules les entités à angle « santé publique » ont été gardées.
- Items du résidanat de mon périmètre portés uniquement par des entités ENC-1 (doublons retirés) : RES-CHI-001 à 006, 008, 009, 024, 026,
  027, 049, 050 et RES-MED-068, 071, 077, 078, 079, 082, 092 ; items non nosologiques (indicateurs, enquêtes, organisation, économie,
  responsabilité, secret, contraception, MNT, maladies vectorielles) non reliés.
- Les liens inter-agents (ENC-2 ↔ ENC-1) ne sont pas posés : à faire à la fusion à partir du tableau ci-dessus.
- 2026-11-19T02:30:11+00:00 — correctif : réécriture des 7 lots ENC-2 (découpage des listes respectant les parenthèses ; 3 entrées concernées : PATH-OPHT-0035, PATH-URGE-0021, PATH-URGE-0031). Ids inchangés ; revalidation OK (684 ids uniques, 0 lien invalide).
