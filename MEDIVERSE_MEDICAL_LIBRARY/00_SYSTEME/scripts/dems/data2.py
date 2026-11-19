# -*- coding: utf-8 -*-
# Données des parcours — lot 2 (autres spécialités médicales). Contenu original Mediverse (proposition pédagogique).
D = {}

D["DEMS-MED-02"] = dict(slug="ANESTHESIE_REANIMATION_PEDIATRIQUE", type="med",
 profil="Anesthésie et réanimation du nouveau-né, du nourrisson et de l'enfant : physiologie et pharmacologie pédiatriques, voies aériennes, chirurgie pédiatrique, réanimation pédiatrique et néonatale.",
 stages=["Anesthésie en chirurgie pédiatrique", "Réanimation pédiatrique", "Réanimation néonatale", "Urgences pédiatriques", "Anesthésie adulte (socle, stage court)", "Anesthésie en chirurgie cardiaque pédiatrique (si disponible)", "Consultation d'anesthésie pédiatrique"],
 annees=[
  ["Physiologie et pharmacologie de l'enfant selon l'âge (poids, volumes, clairances)", "Consultation préanesthésique de l'enfant, jeûne, prémédication, présence parentale", "Voies aériennes de l'enfant : particularités anatomiques, matériel adapté", "Réanimation cardio-pulmonaire pédiatrique et néonatale", "Remplissage, transfusion et besoins hydro-électrolytiques de l'enfant"],
  ["Anesthésie du nouveau-né et du prématuré", "Anesthésie locorégionale de l'enfant (caudale, blocs)", "Analgésie et sédation pédiatriques", "Ventilation mécanique de l'enfant", "Sepsis et états de choc de l'enfant"],
  ["Anesthésie pour chirurgie lourde (neurochirurgie, chirurgie thoracique, malformations digestives néonatales)", "Traumatisé grave de l'enfant", "Réanimation neurologique pédiatrique", "Défaillances d'organes et épuration extrarénale en pédiatrie"],
  ["Éthique en réanimation pédiatrique, accompagnement des familles", "Organisation et sécurité en anesthésie pédiatrique", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Ventilation au masque et intubation du nourrisson et de l'enfant", 1, 2), ("Pose de voie veineuse périphérique difficile et voie intra-osseuse", 1, 2), ("Calcul des doses et des volumes selon le poids", 1, 1), ("Intubation du nouveau-né", 2, 3), ("Anesthésie caudale et blocs périphériques échoguidés", 2, 3), ("Voie veineuse centrale et cathéter artériel chez l'enfant", 2, 4), ("Gestion d'un laryngospasme et d'un bronchospasme (simulation)", 1, 2)],
 urg=[("Laryngospasme et bronchospasme peranesthésiques", "A", ["laryngospasme"]), ("Arrêt cardio-respiratoire de l'enfant", "A", ["arret cardio"]), ("Inhalation de corps étranger", "A", ["corps etranger"]), ("Choc anaphylactique de l'enfant", "A", ["anaphyla"]), ("Déshydratation et choc hypovolémique", "A", ["deshydratation", "etats de choc"]), ("État de mal convulsif", "B", ["etat de mal"]), ("Détresse respiratoire du nouveau-né", "B", ["detresse respiratoire"]), ("Épiglottite et laryngite grave", "B", ["laryngite", "epiglottite"]), ("Hyperthermie maligne", "B", ["hyperthermie maligne"]), ("Traumatisé crânien grave de l'enfant", "C", ["traumatisme cranien"]), ("Choc septique et purpura fulminans", "C", ["purpura fulminans", "etats de choc"])],
 recos=["ADARPEF / SFAR (France) — anesthésie pédiatrique (jeûne, prémédication, ALR)", "ERC / ILCOR — réanimation pédiatrique et néonatale", "Surviving Sepsis Campaign — enfant", "ESAIC — anesthésie pédiatrique (sécurité, voies aériennes)", "Difficult Airway Society / Association of Paediatric Anaesthetists — voies aériennes difficiles de l'enfant"],
 pratique="cas de consultation d'anesthésie pédiatrique ou de crise peranesthésique (simulation) avec calculs de doses selon le poids")

D["DEMS-MED-03"] = dict(slug="BIOPHYSIQUE_MEDICALE", type="fond", gardes_type="anat",
 profil="Physique appliquée à la médecine : rayonnements ionisants et non ionisants, radioprotection, physique de l'imagerie et de la médecine nucléaire, biophysique des solutions, de la circulation et des signaux.",
 stages=["Laboratoire de biophysique (faculté)", "Médecine nucléaire", "Radiothérapie (physique médicale)", "Imagerie (scanner, IRM, échographie)", "Explorations fonctionnelles (signaux électrophysiologiques)", "Unité de radioprotection"],
 annees=[
  ["Biophysique des solutions et compartiments liquidiens", "Rayonnements ionisants : interactions avec la matière, dosimétrie", "Radiobiologie et effets biologiques des rayonnements", "Réglementation et principes de radioprotection", "Statistiques et traitement du signal (bases)"],
  ["Physique de la médecine nucléaire (détecteurs, gamma-caméra, TEP)", "Physique de la radiologie et du scanner", "Échographie et effet Doppler", "Bioélectricité et électrophysiologie", "Optique et vision, acoustique et audition"],
  ["IRM : principes physiques et sécurité", "Physique de la radiothérapie (notions de planification, contrôle qualité)", "Contrôle qualité des équipements", "Dosimétrie des patients et des travailleurs"],
  ["Recherche, modélisation, traitement d'images", "Enseignement de la biophysique", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Calcul de dose et d'activité ; lecture d'un dosimètre", 1, 2), ("Contrôle qualité d'un appareil d'imagerie", 2, 3), ("Mesure de contamination et gestion d'un incident radiologique (exercice)", 2, 3), ("Traitement d'images et de signaux (logiciels)", 2, 3), ("Préparation et animation de travaux pratiques", 1, 2)],
 urg=[("Incident de contamination radioactive (personne, surface)", "A", ["contamination"]), ("Exposition accidentelle d'un patient ou d'un travailleur aux rayonnements", "A", ["irradiation"]), ("Femme enceinte exposée à un examen irradiant : estimation de dose", "B", ["irradiation foetale"]), ("Incident en IRM (projectile ferromagnétique, brûlure, dispositif implanté)", "B", ["securite irm"]), ("Erreur d'administration d'un radiopharmaceutique", "C", ["radiopharmaceutique"])],
 recos=["Réglementation algérienne de radioprotection (textes à acquérir — Commissariat à l'énergie atomique)", "CIPR (ICRP) — recommandations fondamentales de radioprotection", "AIEA — normes fondamentales de sûreté et radioprotection en médecine", "AAPM / EFOMP — contrôle qualité des équipements"],
 pratique="épreuve pratique de biophysique (calcul dosimétrique, contrôle qualité, analyse d'image ou de signal) avec commentaire")

D["DEMS-MED-05"] = dict(slug="DERMATOLOGIE_VENEREOLOGIE", type="med",
 profil="Maladies de la peau, des muqueuses et des phanères, infections sexuellement transmissibles, oncodermatologie, dermatologie pédiatrique et allergologie cutanée.",
 stages=["Dermatologie (hospitalisation)", "Consultation de dermatologie", "Dermatopathologie (lecture des biopsies)", "Consultation IST", "Dermatologie pédiatrique", "Oncodermatologie / chirurgie dermatologique", "Allergologie cutanée"],
 annees=[
  ["Sémiologie dermatologique et lésions élémentaires", "Infections cutanées bactériennes, virales, mycosiques, parasitaires (gale, leishmaniose cutanée)", "Eczémas et urticaires", "Psoriasis", "Toxidermies", "Infections sexuellement transmissibles"],
  ["Dermatoses bulleuses auto-immunes", "Lupus et connectivites à expression cutanée", "Acné, rosacée, hidradénite", "Lèpre et mycobactérioses cutanées", "Dermatoscopie (bases)", "Traitements systémiques et biothérapies en dermatologie"],
  ["Tumeurs cutanées : carcinomes, mélanome, lymphomes cutanés", "Dermatologie pédiatrique et génodermatoses", "Maladies des phanères et des muqueuses", "Photodermatologie et photothérapie", "Dermatologie des maladies systémiques"],
  ["Chirurgie dermatologique et lasers (indications)", "Organisation du dépistage et santé publique (IST, leishmaniose)", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Biopsie cutanée", 1, 1), ("Prélèvements mycologiques et parasitologiques (grattage, frottis de leishmaniose)", 1, 1), ("Examen dermatoscopique", 2, 3), ("Cryothérapie", 1, 2), ("Exérèse simple et suture", 2, 3), ("Tests allergologiques (patch-tests)", 2, 3), ("Photothérapie : prescription et surveillance", 3, 4)],
 urg=[("Nécrolyse épidermique toxique / syndrome de Stevens-Johnson", "A", ["stevens", "necrolyse", "toxidermie"]), ("DRESS (syndrome d'hypersensibilité médicamenteuse)", "A", ["dress", "toxidermie"]), ("Dermohypodermite bactérienne nécrosante", "A", ["fasciite", "dermohypodermite"]), ("Angio-œdème et anaphylaxie", "A", ["angio oedeme", "anaphyla"]), ("Érythrodermie", "B", ["erythrodermie"]), ("Pemphigus et pemphigoïde étendus", "B", ["pemphigus", "pemphigoide"]), ("Purpura fulminans", "B", ["purpura fulminans"]), ("Psoriasis pustuleux généralisé", "C", ["psoriasis"]), ("Zona ophtalmique et zona de l'immunodéprimé", "C", ["zona"])],
 recos=["Ministère de la Santé (Algérie) — programmes nationaux (leishmanioses, IST) : textes à acquérir", "OMS — IST : gonocoque, chlamydia, syphilis (catalogue)", "SFD (France) — psoriasis, dermatite atopique, toxidermies", "EADV / EDF — mélanome, dermatoses bulleuses, urticaire", "OMS — lèpre et leishmaniose cutanée"],
 pratique="examen d'un patient réel avec description sémiologique, diagnostic différentiel, prélèvements utiles et traitement")

D["DEMS-MED-07"] = dict(slug="EPIDEMIOLOGIE_ET_MEDECINE_PREVENTIVE", type="med", gardes_type="anat",
 profil="Épidémiologie descriptive, analytique et évaluative, surveillance et investigation des maladies, prévention, hygiène hospitalière et organisation des programmes de santé publique (services d'épidémiologie et de médecine préventive).",
 stages=["Service d'épidémiologie et de médecine préventive (SEMEP)", "Hygiène hospitalière / comité de lutte contre les infections nosocomiales", "Direction de la santé de wilaya / programmes nationaux", "Institut national de santé publique (si accessible)", "Registre des cancers", "Unité de biostatistique et de recherche clinique"],
 annees=[
  ["Mesures en épidémiologie (incidence, prévalence, taux standardisés)", "Biostatistique de base et logiciels", "Surveillance épidémiologique et maladies à déclaration obligatoire", "Organisation du système de santé algérien et programmes nationaux", "Hygiène hospitalière (précautions standard et complémentaires)"],
  ["Épidémiologie analytique : cohortes, cas-témoins, biais, confusion", "Investigation d'épidémie", "Vaccinologie et programme élargi de vaccination", "Épidémiologie des maladies non transmissibles", "Enquêtes de couverture et sondages"],
  ["Essais cliniques et évaluation des interventions", "Revue systématique et méta-analyse (lecture)", "Registres et systèmes d'information sanitaire", "Économie de la santé (notions)", "Éducation et promotion de la santé"],
  ["Conduite d'un projet de recherche complet", "Planification et évaluation d'un programme de santé", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Calcul et interprétation d'indicateurs de santé", 1, 1), ("Analyse statistique d'une base de données", 1, 2), ("Rédaction d'un protocole d'enquête", 2, 3), ("Investigation d'un cas groupé sur le terrain", 2, 3), ("Audit d'hygiène hospitalière", 2, 3), ("Lecture critique d'un article", 1, 2), ("Rédaction d'un rapport de surveillance", 2, 3)],
 urg=[("Alerte épidémique (cas groupés de toxi-infection alimentaire collective, méningite, rougeole)", "A", ["toxi infection", "investigation d epidemie"]), ("Maladie à déclaration obligatoire urgente : déclaration et mesures autour d'un cas", "A", ["declaration obligatoire"]), ("Méningite à méningocoque : chimioprophylaxie de l'entourage", "A", ["meningite"]), ("Épidémie d'infections associées aux soins", "B", ["nosocomial", "associees aux soins"]), ("Rage : exposition et prophylaxie (organisation)", "B", ["antirabique", "morsures"]), ("Alerte de santé publique internationale (RSI) et maladies émergentes", "C", ["emergent"])],
 recos=["Ministère de la Santé (Algérie) — décret 22-250 sur les maladies à déclaration obligatoire, calendrier vaccinal (catalogue)", "OMS — Règlement sanitaire international ; prévention et contrôle des infections (catalogue)", "OMS — guides d'investigation des épidémies", "CDC — principles of epidemiology ; STROBE / CONSORT (rédaction scientifique)", "INSP (Algérie) — relevés épidémiologiques"],
 pratique="analyse commentée d'un jeu de données ou d'un article, ou conduite à tenir face à une alerte épidémique")

D["DEMS-MED-09"] = dict(slug="HEMATOLOGIE", type="med",
 profil="Hémopathies malignes et bénignes, hémostase et thrombose, transfusion : diagnostic cytologique, traitements intensifs, greffe de cellules souches et soins de support.",
 stages=["Hématologie clinique (hospitalisation)", "Hôpital de jour et consultation", "Laboratoire d'hématologie (cytologie, hémostase)", "Unité de soins intensifs hématologiques / greffe", "Centre de transfusion sanguine", "Hématologie pédiatrique (stage court)"],
 annees=[
  ["Lecture de l'hémogramme et du frottis sanguin", "Anémies carentielles, hémolytiques, aplasiques", "Neutropénies et fièvre du neutropénique", "Thrombopénies (dont PTI)", "Hémostase : exploration et anticoagulants", "Bases transfusionnelles"],
  ["Leucémies aiguës", "Syndromes myéloprolifératifs et myélodysplasiques", "Lymphomes hodgkiniens et non hodgkiniens", "Myélome et gammapathies", "Hémoglobinopathies (drépanocytose, thalassémies)", "Hémophilie et maladie de Willebrand"],
  ["Chimiothérapies, thérapies ciblées et immunothérapies", "Greffe de cellules souches hématopoïétiques : indications, complications", "Thromboses et thrombophilies", "Soins de support et infections de l'immunodéprimé", "Cytométrie, cytogénétique et biologie moléculaire (interprétation)"],
  ["Hématologie et grossesse, hématologie du sujet âgé", "Recherche clinique et essais thérapeutiques", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Lecture du frottis sanguin", 1, 1), ("Myélogramme : réalisation et lecture", 1, 2), ("Biopsie ostéo-médullaire", 2, 3), ("Ponction lombaire avec injection intrathécale", 2, 3), ("Prescription et surveillance d'une chimiothérapie", 2, 3), ("Prescription transfusionnelle et gestion d'un incident", 1, 2), ("Annonce d'un diagnostic d'hémopathie maligne", 2, 3)],
 urg=[("Neutropénie fébrile", "A", ["neutropeni"]), ("Anémie aiguë mal tolérée", "A", ["anemie"]), ("Accident transfusionnel", "A", ["transfusion"]), ("Hémorragie sous anticoagulant ; surdosage en antivitamine K", "A", ["anticoagul"]), ("Syndrome de lyse tumorale", "B", ["lyse tumorale"]), ("Hyperleucocytose et leucostase", "B", ["leucostase"]), ("Coagulation intravasculaire disséminée", "B", ["coagulation intravasculaire"]), ("Purpura thrombotique thrombocytopénique", "B", ["microangiopathie thrombotique", "purpura thrombotique"]), ("Crise drépanocytaire grave (syndrome thoracique aigu)", "B", ["drepanocytose"]), ("Compression médullaire du myélome", "C", ["compression medullaire"]), ("Hémorragie grave chez l'hémophile", "C", ["hemophilie"])],
 recos=["ELN (European LeukemiaNet) — leucémies aiguës myéloïdes, LMC", "ESMO / NCCN — lymphomes et myélome", "ASH / ISTH — thrombopénies, thrombose, hémophilie", "EBMT — greffe de cellules souches hématopoïétiques", "OMS — seuils d'hémoglobine pour l'anémie (catalogue) et classification des hémopathies", "Agence nationale du sang (Algérie) — bonnes pratiques transfusionnelles (textes à acquérir)"],
 pratique="lecture de lames (frottis, myélogramme) et dossier d'hémopathie avec décision thérapeutique")

D["DEMS-MED-13"] = dict(slug="MEDECINE_LEGALE_DROIT_MEDICAL_ETHIQUE", type="med",
 profil="Expertise médico-judiciaire : thanatologie et autopsie, traumatologie et victimologie, toxicologie médico-légale, droit médical, responsabilité et déontologie, éthique.",
 stages=["Service de médecine légale (levées de corps, autopsies)", "Unité médico-judiciaire / consultations de victimes", "Toxicologie (laboratoire)", "Anatomie pathologique", "Psychiatrie (expertise)", "Urgences (certificats)", "Établissement pénitentiaire (si organisé)"],
 annees=[
  ["Thanatologie : signes de la mort, levée de corps, délai post-mortem", "Certificat de décès (décret 22-178) et obstacles médico-légaux", "Coups et blessures : description, certificat, ITT", "Organisation de la justice et réquisitions", "Secret médical et déontologie"],
  ["Autopsie médico-légale : technique et protocoles", "Asphyxies, noyades, morts subites", "Traumatologie : armes blanches, armes à feu, accidents de la circulation", "Violences sexuelles et maltraitance", "Toxicologie médico-légale (prélèvements)"],
  ["Responsabilité médicale et réparation du dommage corporel", "Identification (odontologie, anthropologie, ADN)", "Psychiatrie médico-légale et expertise", "Médecine pénitentiaire et garde à vue", "Éthique clinique et bioéthique (loi sanitaire 18-11)"],
  ["Catastrophes et identification des victimes", "Rédaction d'un rapport d'expertise complet", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Levée de corps et rédaction du certificat de décès", 1, 1), ("Examen d'une victime de violences et certificat descriptif", 1, 1), ("Autopsie médico-légale", 1, 3), ("Prélèvements toxicologiques et histologiques post-mortem", 1, 2), ("Examen d'une victime d'agression sexuelle (prélèvements)", 2, 3), ("Rapport d'expertise", 2, 4)],
 urg=[("Victime d'agression sexuelle récente (prélèvements, prophylaxies)", "A", ["agression sexuelle"]), ("Enfant victime de maltraitance (protection, signalement)", "A", ["maltraitance"]), ("Réquisition urgente (garde à vue, examen de compatibilité)", "A", ["garde a vue"]), ("Décès suspect : levée de corps et obstacle médico-légal", "A", ["deces"]), ("Intoxication suspecte : prélèvements conservatoires", "B", ["intoxication"]), ("Afflux de décès (catastrophe) : identification", "C", ["catastrophe"])],
 recos=["Loi n°18-11 relative à la santé (Algérie), décret 22-178 (certificat médical de décès) — catalogue 18_RECOMMANDATIONS/01_ALGERIE", "Code de déontologie médicale (Algérie) — texte à acquérir", "Recommandation du Conseil de l'Europe R(99)3 — harmonisation des règles en matière d'autopsie médico-légale", "Interpol — guide d'identification des victimes de catastrophes", "OMS — prise en charge médico-légale des violences sexuelles"],
 pratique="levée de corps ou autopsie commentée, rédaction d'un certificat ou d'un rapport d'expertise")

D["DEMS-MED-14"] = dict(slug="MEDECINE_NUCLEAIRE_ET_IMAGERIE_MOLECULAIRE", type="img",
 profil="Imagerie fonctionnelle et moléculaire (scintigraphie, TEP) et thérapie par radionucléides (iode 131, radiothérapie interne vectorisée), avec radioprotection et radiopharmacie.",
 stages=["Médecine nucléaire (scintigraphie conventionnelle)", "TEP-scanner (si disponible)", "Radiothérapie interne (iode 131, autres)", "Radiopharmacie", "Endocrinologie (thyroïde)", "Cardiologie", "Oncologie"],
 annees=[
  ["Physique nucléaire, détection, gamma-caméra", "Radiopharmaceutiques et radiopharmacie", "Radioprotection des patients, du personnel et de l'environnement", "Scintigraphie thyroïdienne et osseuse", "Anatomie en coupes"],
  ["Scintigraphie de perfusion myocardique", "Scintigraphies pulmonaire, rénale, digestive", "TEP au FDG en oncologie : principes et lecture", "Traitement des hyperthyroïdies par l'iode 131", "Tomographie hybride (TEMP-TDM)"],
  ["Traitement des cancers thyroïdiens différenciés", "Radiothérapie interne vectorisée (orientation)", "Imagerie moléculaire en neurologie et en infectiologie", "Critères de réponse thérapeutique"],
  ["Assurance qualité et gestion d'un service", "Recherche et nouveaux traceurs", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Préparation et contrôle d'un radiopharmaceutique", 1, 2), ("Réalisation d'une scintigraphie standard", 1, 2), ("Interprétation et compte rendu de scintigraphies", 1, 3), ("Épreuve d'effort ou stimulation pharmacologique pour scintigraphie myocardique", 2, 3), ("Administration d'iode 131 et consignes de radioprotection", 2, 3), ("Lecture de TEP-scanner", 2, 4)],
 urg=[("Contamination radioactive (patient, personnel, local)", "A", ["contamination"]), ("Extravasation d'un radiopharmaceutique", "A", ["extravasation"]), ("Malaise ou réaction pendant une épreuve de stress pharmacologique", "A", []), ("Femme enceinte ou allaitante exposée à un radiopharmaceutique", "B", ["irradiation foetale"]), ("Scintigraphie pulmonaire en urgence (suspicion d'embolie)", "B", ["embolie pulmonaire"]), ("Complications aiguës après iode 131 (thyroïdite radique, sialadénite)", "C", ["iode 131"])],
 recos=["Arrêté 1140 du 07/10/2024 (programme du DEMS) — annexe non acquise", "EANM / SNMMI — procédures de scintigraphie et de TEP", "AIEA — radioprotection en médecine nucléaire", "ETA / ATA — iode 131 dans les hyperthyroïdies et les cancers thyroïdiens", "EANM — critères de lecture TEP en oncologie"],
 pratique="interprétation commentée d'examens scintigraphiques et TEP, et conduite à tenir de radioprotection")

D["DEMS-MED-16"] = dict(slug="MEDECINE_DU_TRAVAIL", type="med", gardes_type="anat",
 profil="Prévention des risques professionnels, surveillance médicale des travailleurs, maladies professionnelles et accidents du travail, aptitude, ergonomie et toxicologie industrielle.",
 stages=["Service de médecine du travail (hospitalo-universitaire)", "Entreprise industrielle (visites de postes)", "Toxicologie industrielle", "Pneumologie (pneumoconioses)", "Dermatologie (dermatoses professionnelles)", "ORL / audiologie", "Psychiatrie (risques psychosociaux)"],
 annees=[
  ["Législation du travail et organisation de la médecine du travail en Algérie", "Visites médicales : embauche, périodique, reprise ; aptitude", "Accidents du travail et maladies professionnelles : déclaration, réparation", "Risques chimiques (solvants, métaux lourds, pesticides)", "Risques physiques (bruit, vibrations, chaleur, rayonnements)"],
  ["Pneumopathies professionnelles (silicose, asbestose, asthme professionnel)", "Dermatoses professionnelles", "Troubles musculo-squelettiques et ergonomie", "Risques biologiques (personnel de santé, agriculteurs)", "Métrologie d'ambiance et biométrologie"],
  ["Cancers professionnels", "Risques psychosociaux et addictions en milieu de travail", "Maintien dans l'emploi et handicap", "Toxicologie industrielle avancée", "Évaluation des risques et document unique"],
  ["Conduite d'une étude de poste et d'une action de prévention", "Épidémiologie en santé au travail", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Visite médicale et avis d'aptitude argumenté", 1, 1), ("Audiométrie et spirométrie de dépistage", 1, 2), ("Étude de poste de travail", 1, 3), ("Interprétation de biométrologie (plombémie, cholinestérases…)", 2, 3), ("Rédaction d'un certificat de maladie professionnelle", 1, 2), ("Animation d'une action de formation à la sécurité", 2, 3)],
 urg=[("Accident d'exposition au sang du personnel de santé", "A", ["exposition au sang"]), ("Intoxication aiguë professionnelle (organophosphorés, monoxyde de carbone, gaz)", "A", ["intoxication"]), ("Brûlure chimique et projection oculaire", "A", ["brul"]), ("Accident du travail grave : premiers secours et déclaration", "B", ["accident du travail"]), ("Coup de chaleur au travail", "B", ["coup de chaleur"]), ("Crise suicidaire liée au travail", "C", ["suicid"])],
 recos=["Législation algérienne de la santé et sécurité au travail et tableaux des maladies professionnelles (textes à acquérir)", "OIT / OMS — santé au travail", "INRS (France) — fiches toxicologiques et guides de prévention", "ACGIH / valeurs limites d'exposition professionnelle", "HAS (France) — surveillance médico-professionnelle (amiante, bruit, cancérogènes)"],
 pratique="cas de médecine du travail (aptitude, déclaration, prévention) ou étude de poste commentée")

D["DEMS-MED-17"] = dict(slug="MEDECINE_PHYSIQUE_ET_READAPTATION", type="med",
 profil="Évaluation et prise en charge des déficiences, incapacités et handicaps : rééducation neurologique, locomotrice, cardio-respiratoire, appareillage, réinsertion.",
 stages=["MPR (hospitalisation)", "Rééducation neurologique (AVC, blessés médullaires)", "Rééducation de l'appareil locomoteur", "Appareillage", "Réadaptation cardio-respiratoire", "Rééducation pédiatrique", "Neurologie / orthopédie (stages courts)"],
 annees=[
  ["Classification internationale du fonctionnement (CIF), évaluation du handicap", "Examen clinique en MPR : testing, goniométrie, échelles", "Rééducation après fractures et chirurgie orthopédique", "Rééducation de l'hémiplégique", "Douleur et agents physiques"],
  ["Blessés médullaires : vessie et intestin neurologiques, escarres", "Traumatisés crâniens", "Spasticité : évaluation et traitements", "Lombalgies et rachis", "Amputés et appareillage"],
  ["Rééducation des maladies neuromusculaires et de la sclérose en plaques", "Réadaptation cardiaque et respiratoire", "Rééducation pédiatrique (paralysie cérébrale)", "Réinsertion socio-professionnelle et législation du handicap"],
  ["Analyse du mouvement, explorations urodynamiques (indications)", "Organisation d'une filière de soins de suite", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Bilan fonctionnel et rédaction d'un programme de rééducation", 1, 1), ("Prescription d'orthèses et de prothèses", 1, 2), ("Injections de toxine botulique", 2, 3), ("Infiltrations et blocs anesthésiques", 2, 3), ("Bilan urodynamique (interprétation)", 3, 4), ("Évaluation isocinétique / analyse de la marche (selon équipement)", 3, 4)],
 urg=[("Hyperréflexie autonome du blessé médullaire", "A", ["hyperreflexie"]), ("Thrombose veineuse profonde chez le patient immobilisé", "A", ["thrombose veineuse"]), ("Escarre infectée et sepsis", "B", ["escarre"]), ("Rétention urinaire et infection sur vessie neurologique", "B", ["vessie neurologique"]), ("Fausse route et pneumopathie d'inhalation", "B", ["inhalation"]), ("Chute avec fracture chez le patient en rééducation", "C", ["chute"])],
 recos=["OMS — Classification internationale du fonctionnement, du handicap et de la santé", "OMS — lombalgie chronique primaire (catalogue) ; réadaptation (Rehabilitation 2030)", "ESC / ERS — réadaptation cardiaque et respiratoire", "HAS (France) — rééducation après AVC, prise en charge des escarres", "Législation algérienne relative aux personnes handicapées (texte à acquérir)"],
 pratique="examen d'un patient en rééducation avec bilan fonctionnel, objectifs et programme de rééducation et d'appareillage")

D["DEMS-MED-20"] = dict(slug="ONCOLOGIE_MEDICALE", type="med",
 profil="Diagnostic, stadification et traitement médical des cancers solides (chimiothérapie, thérapies ciblées, immunothérapie, hormonothérapie), soins de support et décisions en RCP.",
 stages=["Oncologie médicale (hospitalisation et hôpital de jour)", "Consultation d'annonce", "Radiothérapie", "Anatomie pathologique", "Soins palliatifs et douleur", "Hématologie (stage court)", "Chirurgie oncologique (observation)"],
 annees=[
  ["Biologie du cancer, classification TNM, état général (OMS/ECOG)", "Pharmacologie des anticancéreux et toxicités", "Cancers du sein et colorectal", "Soins de support (douleur, nausées, nutrition)", "Urgences oncologiques"],
  ["Cancers du poumon, de l'estomac, du pancréas, du foie", "Cancers gynécologiques et urologiques", "Cancers de la tête et du cou", "Thérapies ciblées et immunothérapie : toxicités spécifiques", "Évaluation de la réponse (RECIST)"],
  ["Sarcomes, tumeurs germinales, cancers rares", "Oncogériatrie et cancer chez la femme enceinte", "Oncogénétique (orientation)", "Essais cliniques et méthodologie"],
  ["Soins palliatifs et fin de vie", "Organisation des RCP et du plan cancer national", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Prescription et vérification d'un protocole de chimiothérapie", 1, 2), ("Évaluation et traitement de la douleur cancéreuse", 1, 1), ("Ponction pleurale et d'ascite", 1, 2), ("Présentation d'un dossier en RCP", 1, 2), ("Consultation d'annonce", 2, 3), ("Gestion des toxicités de l'immunothérapie", 2, 3), ("Inclusion d'un patient dans un essai clinique", 3, 4)],
 urg=[("Neutropénie fébrile", "A", ["neutropeni"]), ("Compression médullaire métastatique", "A", ["compression medullaire"]), ("Hypercalcémie maligne", "A", ["hypercalcemie"]), ("Syndrome cave supérieur", "A", ["cave superieur"]), ("Syndrome de lyse tumorale", "B", ["lyse tumorale"]), ("Extravasation d'anticancéreux", "B", ["extravasation"]), ("Hypertension intracrânienne sur métastases", "B", ["hypertension intracranienne"]), ("Toxicités graves de l'immunothérapie", "C", ["immunotherapie"]), ("Occlusion digestive maligne", "C", ["occlusion"])],
 recos=["Arrêté du 01/04/2026 (programme du DEMS) — annexe non acquise", "Plan national cancer (Algérie) — documents à acquérir", "ESMO — guides de pratique clinique par localisation", "NCCN — guidelines par localisation", "OMS — douleur cancéreuse de l'adulte et de l'adolescent (catalogue)", "MASCC / ESMO — soins de support (neutropénie fébrile, antiémétiques)"],
 pratique="dossier de cancer avec décision thérapeutique argumentée (stade, état général, recommandations) et gestion d'une toxicité")

D["DEMS-MED-21"] = dict(slug="OPHTALMOLOGIE", type="chir",
 profil="Spécialité médico-chirurgicale de l'œil et de ses annexes : examen à la lampe à fente, urgences oculaires, cataracte, glaucome, rétine, neuro-ophtalmologie, ophtalmopédiatrie.",
 stages=["Consultation et urgences ophtalmologiques", "Bloc opératoire (cataracte)", "Rétine médicale et chirurgicale", "Glaucome", "Ophtalmopédiatrie et strabisme", "Neuro-ophtalmologie", "Explorations (angiographie, OCT, champ visuel)"],
 annees=[
  ["Anatomie et optique de l'œil, réfraction", "Examen à la lampe à fente et fond d'œil", "Œil rouge et urgences oculaires", "Traumatismes oculaires", "Pharmacologie oculaire"],
  ["Cataracte : bilan et technique chirurgicale", "Glaucomes", "Rétinopathie diabétique et hypertensive", "Uvéites", "Strabisme et amblyopie"],
  ["Décollement de rétine et pathologie maculaire", "Neuro-ophtalmologie", "Pathologie palpébrale et orbitaire", "Explorations : OCT, angiographie, champ visuel, électrophysiologie"],
  ["Chirurgie du glaucome et vitréo-rétinienne (orientation)", "Santé publique : cécité évitable, trachome", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Examen à la lampe à fente, tonométrie, fond d'œil", 1, 1), ("Réfraction et prescription de verres", 1, 1), ("Ablation de corps étranger cornéen", 1, 1), ("Suture de plaie palpébrale", 1, 2), ("Chirurgie de la cataracte", 2, 4), ("Photocoagulation au laser", 2, 3), ("Injections intravitréennes", 3, 4), ("Interprétation d'OCT, d'angiographie et de champ visuel", 2, 3)],
 urg=[("Glaucome aigu par fermeture de l'angle", "A", ["glaucome"]), ("Brûlure chimique oculaire", "A", ["brulure oculaire", "brulures oculaires"]), ("Plaie du globe et corps étranger intraoculaire", "A", ["plaie du globe", "traumatismes oculaires"]), ("Baisse brutale de vision (occlusion artérielle rétinienne)", "A", ["occlusion de l artere centrale"]), ("Endophtalmie", "B", ["endophtalmie"]), ("Kératite infectieuse grave", "B", ["keratite"]), ("Décollement de rétine", "B", ["decollement de retine"]), ("Cellulite orbitaire", "B", ["cellulite"]), ("Neuropathie optique ischémique (maladie de Horton)", "C", ["horton"]), ("Œdème papillaire et hypertension intracrânienne", "C", ["hypertension intracranienne"])],
 recos=["Ministère de la Santé (Algérie) — programmes de santé oculaire et de prévention de la cécité : textes à rechercher", "OMS — rapport mondial sur la vision ; trachome", "American Academy of Ophthalmology — Preferred Practice Patterns", "European Glaucoma Society — guide du glaucome", "SFO (France) — rapports et recommandations"],
 pratique="examen d'un patient réel à la lampe à fente avec diagnostic et conduite à tenir, ou interprétation d'examens complémentaires")

D["DEMS-MED-22"] = dict(slug="OTO_RHINO_LARYNGOLOGIE", type="chir",
 profil="Spécialité médico-chirurgicale de l'oreille, du nez et des sinus, du pharynx, du larynx et du cou : otologie, rhinologie, laryngologie, cancérologie cervico-faciale, audiologie.",
 stages=["Consultation et urgences ORL", "Bloc opératoire ORL", "Audiologie et vestibulologie", "Cancérologie cervico-faciale", "ORL pédiatrique", "Chirurgie cervicale (thyroïde)", "Explorations (endoscopie, audiométrie)"],
 annees=[
  ["Anatomie de la tête et du cou", "Examen ORL et nasofibroscopie", "Otites et leurs complications", "Angines et complications (phlegmon)", "Épistaxis", "Urgences laryngées"],
  ["Audiométrie, surdités de l'adulte et de l'enfant", "Vertiges", "Rhinosinusites et polypose", "Traumatismes de la face et du rocher", "Paralysie faciale", "Amygdalectomie et adénoïdectomie"],
  ["Cancers des voies aérodigestives supérieures et du cavum", "Pathologie thyroïdienne et cervicale chirurgicale", "Chirurgie de l'oreille moyenne", "Pathologie des glandes salivaires"],
  ["Implants auditifs (orientation)", "Chirurgie endoscopique endonasale", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Examen ORL complet et nasofibroscopie", 1, 1), ("Tamponnement antérieur et postérieur d'épistaxis", 1, 1), ("Ponction-drainage d'un phlegmon périamygdalien", 1, 2), ("Audiométrie tonale et vocale : réalisation et lecture", 1, 2), ("Trachéotomie", 2, 3), ("Amygdalectomie", 2, 3), ("Paracentèse et aérateurs transtympaniques", 2, 3), ("Cervicotomie et thyroïdectomie", 3, 4), ("Panendoscopie et biopsies", 2, 3)],
 urg=[("Dyspnée laryngée (épiglottite, laryngite, tumeur)", "A", ["laryngite", "epiglottite"]), ("Épistaxis grave", "A", ["epistaxis"]), ("Corps étranger des voies aériennes et de l'œsophage", "A", ["corps etranger"]), ("Phlegmon périamygdalien et cellulite cervicale", "A", ["cellulite"]), ("Mastoïdite et complications endocrâniennes des otites", "B", ["mastoidite", "otite"]), ("Surdité brusque", "B", ["surdite"]), ("Paralysie faciale périphérique aiguë", "B", ["paralysie faciale"]), ("Traumatisme laryngé ou du rocher", "C", ["traumatisme laryng"]), ("Hémorragie après amygdalectomie", "C", ["amygdalectomie"])],
 recos=["SFORL (France) — recommandations de pratique clinique", "AAO-HNS — surdité brusque, paralysie faciale, amygdalectomie", "ESMO / NCCN — cancers de la tête et du cou", "OMS — prévention de la surdité (rapport mondial sur l'audition)"],
 pratique="examen ORL d'un patient réel avec diagnostic et indication thérapeutique, ou lecture d'audiogramme et d'imagerie")

D["DEMS-MED-25"] = dict(slug="PEDOPSYCHIATRIE", type="med",
 profil="Troubles psychiques de l'enfant et de l'adolescent : troubles du neurodéveloppement, troubles émotionnels et du comportement, urgences psychiatriques de l'adolescent, travail avec les familles et les institutions.",
 stages=["Pédopsychiatrie (consultation et hôpital de jour)", "Unité pour adolescents", "Pédiatrie générale et neuropédiatrie", "Psychiatrie adulte (urgences)", "Centre médico-psycho-pédagogique / structures médico-sociales", "Périnatalité (unité mère-bébé si disponible)"],
 annees=[
  ["Développement psychomoteur, affectif et cognitif", "Entretien avec l'enfant et la famille ; examen psychiatrique de l'enfant", "Troubles du spectre de l'autisme", "Trouble du déficit de l'attention avec ou sans hyperactivité", "Troubles anxieux et dépressifs de l'enfant", "Cadre légal : protection de l'enfance"],
  ["Troubles des apprentissages et déficience intellectuelle", "Troubles des conduites et du comportement", "Troubles du comportement alimentaire de l'adolescent", "Psychoses précoces et trouble bipolaire de l'adolescent", "Psychopharmacologie pédiatrique"],
  ["Psychiatrie périnatale et du bébé", "Psychotraumatisme, maltraitance, deuil", "Addictions de l'adolescent", "Psychothérapies de l'enfant (comportementales, familiales, psychodynamiques)", "Liaison avec la pédiatrie (maladies chroniques)"],
  ["Travail en réseau : école, structures médico-sociales, justice", "Programme national de santé mentale", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Entretien avec l'enfant et ses parents ; observation de jeu", 1, 1), ("Évaluation du risque suicidaire chez l'adolescent", 1, 1), ("Utilisation d'outils de dépistage et d'évaluation (autisme, TDAH)", 1, 2), ("Guidance parentale", 2, 3), ("Prescription et surveillance d'un psychotrope chez l'enfant", 2, 3), ("Psychothérapie supervisée", 2, 4), ("Rédaction d'un signalement / information préoccupante", 1, 2)],
 urg=[("Crise suicidaire et tentative de suicide de l'adolescent", "A", ["suicid"]), ("Agitation et crise clastique", "A", ["agitation"]), ("Maltraitance et abus sexuel : protection immédiate", "A", ["maltraitance"]), ("Anorexie mentale avec critères de gravité somatique", "B", ["anorexie"]), ("Épisode psychotique aigu de l'adolescent", "B", ["psychotique", "delirant"]), ("Intoxication aiguë (alcool, cannabis, médicaments)", "B", ["intoxication"]), ("Refus scolaire anxieux sévère", "C", ["refus scolaire"])],
 recos=["Arrêté 1549 du 08/11/2025 (programme du DEMS) — annexe non acquise", "OMS — mhGAP (catalogue) ; CIM-11", "NICE — autisme, TDAH, dépression de l'enfant, troubles alimentaires", "HAS (France) — trouble du spectre de l'autisme (diagnostic, interventions), TDAH", "AACAP — practice parameters"],
 pratique="entretien avec un enfant/adolescent et sa famille (réel ou simulé), formulation diagnostique et projet de soins pluridisciplinaire")

D["DEMS-MED-27"] = dict(slug="RADIOTHERAPIE_ONCOLOGIE", type="med",
 profil="Traitement des cancers par les rayonnements (radiothérapie externe, curiethérapie) : indications, planification, dosimétrie avec les physiciens, toxicités et association aux autres traitements.",
 stages=["Radiothérapie (consultation, planification, traitement)", "Physique médicale et dosimétrie", "Curiethérapie", "Oncologie médicale", "Imagerie (contourage)", "Soins palliatifs"],
 annees=[
  ["Radiobiologie et physique des rayonnements", "Radioprotection", "Anatomie en coupes et contourage", "Principes de la planification et dosimétrie", "Cancers du sein et du rectum : indications de radiothérapie"],
  ["Cancers de la tête et du cou, du poumon, de la prostate, du col utérin", "Curiethérapie (gynécologique)", "Toxicités aiguës et tardives", "Radiothérapie palliative (métastases osseuses et cérébrales)"],
  ["Techniques avancées : modulation d'intensité, stéréotaxie (indications)", "Tumeurs cérébrales et pédiatriques", "Associations radio-chimiothérapie", "Contrôle qualité et sécurité"],
  ["Organisation d'un service et gestion des risques", "Recherche et essais", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Contourage des volumes cibles et organes à risque", 1, 3), ("Validation d'une dosimétrie avec le physicien", 2, 3), ("Consultation de surveillance et gestion des toxicités", 1, 2), ("Curiethérapie gynécologique", 2, 4), ("Prescription d'une radiothérapie palliative", 2, 3)],
 urg=[("Compression médullaire métastatique (radiothérapie urgente)", "A", ["compression medullaire"]), ("Syndrome cave supérieur", "A", ["cave superieur"]), ("Métastases cérébrales symptomatiques", "B", ["metastases cerebrales"]), ("Radiothérapie hémostatique (saignement tumoral)", "B", ["hemostatique"]), ("Toxicités aiguës graves (mucite, rectite, radiodermite)", "B", ["mucite"]), ("Erreur ou incident d'irradiation", "C", ["irradiation"])],
 recos=["ESTRO — recommandations de contourage et de technique", "ICRU — rapports de prescription et de dosimétrie", "ESMO / NCCN — indications par localisation", "AIEA — sûreté et assurance qualité en radiothérapie", "ASTRO — radiothérapie palliative"],
 pratique="dossier avec indication, dose et technique de radiothérapie argumentées ; contourage commenté ou gestion d'une toxicité")

D["DEMS-MED-28"] = dict(slug="RHUMATOLOGIE", type="med",
 profil="Maladies de l'appareil locomoteur : rhumatismes inflammatoires, arthrose, microcristallines, pathologie osseuse et rachidienne, connectivites, gestes intra-articulaires.",
 stages=["Rhumatologie (hospitalisation)", "Consultation et hôpital de jour (biothérapies)", "Rhumatologie interventionnelle (infiltrations)", "Imagerie ostéo-articulaire", "Médecine interne", "MPR / orthopédie (stages courts)"],
 annees=[
  ["Examen de l'appareil locomoteur ; analyse du liquide articulaire", "Polyarthrite rhumatoïde", "Spondyloarthrites", "Goutte et chondrocalcinose", "Lombalgies, sciatiques et cervicalgies", "Arthrites septiques"],
  ["Ostéoporose et ostéopathies fragilisantes", "Arthrose", "Lupus, Sjögren, sclérodermie (versant rhumatologique)", "Pseudopolyarthrite rhizomélique et maladie de Horton", "Échographie ostéo-articulaire (bases)", "Biothérapies : bilan et surveillance"],
  ["Spondylodiscites et tuberculose ostéo-articulaire", "Tumeurs osseuses et myélome (versant rhumatologique)", "Rhumatologie pédiatrique", "Pathologie abarticulaire et syndromes canalaires", "Ostéodensitométrie"],
  ["Rhumatologie et grossesse", "Éducation thérapeutique", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Ponction articulaire et analyse du liquide", 1, 1), ("Infiltrations articulaires et périarticulaires", 1, 2), ("Infiltrations rachidiennes", 2, 3), ("Échographie ostéo-articulaire", 2, 3), ("Interprétation d'ostéodensitométrie", 2, 3), ("Biopsie des glandes salivaires accessoires", 2, 3), ("Calcul des scores d'activité (DAS28, BASDAI…)", 1, 1)],
 urg=[("Arthrite septique", "A", ["arthrite septique"]), ("Crise de goutte sévère", "A", ["goutte"]), ("Syndrome de la queue de cheval / sciatique paralysante", "A", ["queue de cheval"]), ("Spondylodiscite", "B", ["spondylodiscite"]), ("Maladie de Horton avec menace visuelle", "B", ["horton"]), ("Infection grave sous biothérapie", "B", ["immunodeprime"]), ("Compression médullaire (tumeur, tuberculose)", "C", ["compression medullaire"]), ("Fracture vertébrale ostéoporotique compliquée", "C", ["ostéoporose", "osteoporose"])],
 recos=["EULAR — polyarthrite rhumatoïde, spondyloarthrites, goutte, pseudopolyarthrite", "ACR — mêmes thèmes (comparer les divergences)", "ASAS — critères et prise en charge des spondyloarthrites", "SFR (France) — ostéoporose, recommandations sur les biothérapies", "Société algérienne de rhumatologie — recommandations nationales si disponibles"],
 pratique="examen ostéo-articulaire d'un patient réel avec synthèse, lecture d'imagerie et décision thérapeutique")

D["DEMS-MED-29"] = dict(slug="REANIMATION_MEDICALE", type="med",
 profil="Prise en charge des défaillances vitales d'origine médicale : choc, insuffisance respiratoire aiguë, comas, défaillances rénales et métaboliques, intoxications graves, éthique de la réanimation.",
 stages=["Réanimation médicale (pivot)", "Urgences / SMUR", "Anesthésie (voies aériennes)", "Cardiologie (USIC)", "Néphrologie (épuration)", "Réanimation chirurgicale ou polyvalente", "Infectiologie"],
 annees=[
  ["Physiopathologie des défaillances d'organes", "États de choc et sepsis", "Insuffisance respiratoire aiguë et oxygénothérapie", "Comas et état de mal", "Troubles hydro-électrolytiques et acido-basiques graves", "Réanimation cardio-pulmonaire"],
  ["Ventilation mécanique invasive et non invasive, SDRA", "Insuffisance rénale aiguë et épuration extrarénale", "Intoxications graves", "Infections nosocomiales en réanimation", "Sédation, analgésie, délirium"],
  ["Neuroréanimation", "Hémostase et transfusion en réanimation", "Nutrition du patient de réanimation", "Échographie et monitorage hémodynamique avancé", "Mort encéphalique et prélèvement d'organes"],
  ["Éthique : limitation et arrêt des thérapeutiques", "Qualité, sécurité, gestion d'une unité", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Intubation orotrachéale", 1, 2), ("Pose de cathéter veineux central et artériel échoguidés", 1, 2), ("Réglage de la ventilation mécanique et sevrage", 1, 2), ("Mise en route d'une VNI", 1, 1), ("Épuration extrarénale : branchement et prescription", 2, 3), ("Échographie cardiaque et pulmonaire de réanimation", 2, 3), ("Fibroscopie bronchique en réanimation", 2, 4), ("Drainage thoracique", 2, 3), ("Entretien avec les proches et décision éthique collégiale", 2, 4)],
 urg=[("Choc septique", "A", ["choc septique", "sepsis", "etats de choc"]), ("Arrêt cardio-respiratoire et soins post-arrêt", "A", ["arret cardio"]), ("SDRA", "A", ["sdra"]), ("Coma et état de mal épileptique", "A", ["comas", "etat de mal"]), ("Intoxications graves", "A", ["intoxication"]), ("Acidocétose et troubles métaboliques graves", "A", ["acidocetose"]), ("Choc anaphylactique", "B", ["anaphyla", "etats de choc"]), ("Embolie pulmonaire grave", "B", ["embolie pulmonaire"]), ("Hémorragie digestive grave", "B", ["hemorragie digestive"]), ("Asthme aigu grave et exacerbation de BPCO", "B", ["asthme", "bpco"]), ("Envenimation scorpionique grave", "C", ["scorpion"]), ("Purpura fulminans", "C", ["purpura fulminans"])],
 recos=["Surviving Sepsis Campaign — sepsis et choc septique", "ESICM — SDRA, monitorage hémodynamique, liquides", "SRLF / SFAR (France) — thèmes de réanimation", "ERC / ILCOR — soins post-arrêt cardiaque", "KDIGO — insuffisance rénale aiguë", "Ministère de la Santé (Algérie) — envenimation scorpionique (textes à acquérir)"],
 pratique="cas de réanimation (réel ou simulé) : priorisation des défaillances, réglages ventilatoires et hémodynamiques, décision éthique")

D["DEMS-MED-31"] = dict(slug="GENETIQUE_MEDICALE", type="med",
 profil="Diagnostic et conseil génétique des maladies héréditaires et des anomalies du développement, génétique des cancers, interprétation des analyses chromosomiques et moléculaires, diagnostic prénatal.",
 stages=["Consultation de génétique clinique", "Laboratoire de cytogénétique", "Laboratoire de génétique moléculaire", "Pédiatrie / neuropédiatrie", "Médecine fœtale et diagnostic prénatal", "Oncologie (oncogénétique)"],
 annees=[
  ["Modes de transmission et calcul de risque", "Examen dysmorphologique et arbre généalogique", "Anomalies chromosomiques fréquentes (trisomies, Turner, Klinefelter)", "Techniques : caryotype, FISH, ACPA, séquençage", "Éthique et consentement en génétique"],
  ["Maladies monogéniques fréquentes en Algérie (hémoglobinopathies, maladies neuromusculaires, maladies métaboliques)", "Consanguinité et génétique des populations", "Déficience intellectuelle et syndromes polymalformatifs", "Interprétation des variants (classification)"],
  ["Oncogénétique : prédispositions héréditaires aux cancers", "Diagnostic prénatal et préimplantatoire (orientation)", "Pharmacogénétique", "Thérapies géniques et ciblées (notions)"],
  ["Organisation d'une consultation de conseil génétique", "Registres et maladies rares", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Arbre généalogique et calcul de risque", 1, 1), ("Examen dysmorphologique", 1, 2), ("Lecture d'un caryotype", 1, 2), ("Interprétation d'un rapport de séquençage", 2, 3), ("Consultation de conseil génétique (annonce)", 2, 3), ("Présentation d'un dossier en réunion pluridisciplinaire prénatale", 3, 4)],
 urg=[("Nouveau-né polymalformé : démarche diagnostique urgente", "A", ["polymalform"]), ("Suspicion de maladie métabolique héréditaire à révélation néonatale (orientation urgente)", "A", ["maladies hereditaires du metabolisme"]), ("Diagnostic prénatal dans des délais contraints (décision du couple)", "B", ["prenatal"]), ("Annonce d'un résultat génétique grave", "B", ["annonce d un diagnostic"])],
 recos=["Arrêté 850 du 30/06/2026 (création du DEMS) — programme non acquis", "ACMG/AMP — classification des variants", "ESHG — tests génétiques et éthique", "OMS — génomique en santé publique (hémoglobinopathies)", "HAS / Agence de la biomédecine (France) — information de la parentèle, diagnostic prénatal"],
 pratique="consultation de génétique (réelle ou simulée) avec arbre généalogique, interprétation d'analyses et conseil")

D["DEMS-MED-32"] = dict(slug="ALLERGOLOGIE_ET_IMMUNOLOGIE_CLINIQUE", type="med",
 profil="Diagnostic et traitement des maladies allergiques (respiratoires, alimentaires, médicamenteuses, venins) et des déficits immunitaires, immunothérapie allergénique.",
 stages=["Allergologie (consultation, hôpital de jour)", "Pneumologie (asthme)", "Dermatologie (allergies cutanées)", "Pédiatrie (allergie alimentaire)", "Laboratoire d'immunologie", "Médecine interne (déficits immunitaires)", "Urgences (anaphylaxie)"],
 annees=[
  ["Mécanismes de l'hypersensibilité", "Rhinite et asthme allergiques", "Anaphylaxie : diagnostic et traitement", "Tests cutanés et dosages d'IgE spécifiques", "Allergie alimentaire de l'enfant et de l'adulte"],
  ["Allergies médicamenteuses (bêtalactamines, AINS, produits de contraste, anesthésiques)", "Allergie aux venins d'hyménoptères", "Urticaires et angio-œdèmes (dont héréditaire)", "Dermatite atopique et eczéma de contact", "Immunothérapie allergénique"],
  ["Déficits immunitaires primitifs et secondaires", "Biothérapies en allergologie", "Allergies professionnelles", "Mastocytoses et syndromes d'activation mastocytaire"],
  ["Organisation d'un plateau de tests de provocation", "Éducation thérapeutique (auto-injecteur d'adrénaline)", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Prick-tests et intradermoréactions", 1, 2), ("Patch-tests", 1, 2), ("Test de provocation orale ou médicamenteuse sous surveillance", 2, 3), ("Initiation d'une immunothérapie allergénique", 2, 3), ("Spirométrie (interprétation)", 1, 2), ("Formation d'un patient à l'auto-injection d'adrénaline", 1, 1)],
 urg=[("Choc anaphylactique", "A", ["anaphyla", "etats de choc"]), ("Asthme aigu grave d'origine allergique", "A", ["asthme"]), ("Angio-œdème laryngé (dont héréditaire)", "A", ["angio oedeme"]), ("Réaction systémique pendant un test ou une immunothérapie", "B", ["immunotherapie"]), ("Toxidermie grave", "B", ["toxidermie", "stevens"]), ("Infection grave révélant un déficit immunitaire", "C", ["deficit immunitaire"])],
 recos=["Arrêté 851 du 30/06/2026 (création du DEMS) — programme non acquis", "WAO / EAACI — anaphylaxie, allergie alimentaire, immunothérapie allergénique", "GINA — asthme ; ARIA — rhinite allergique", "EAACI / ENDA — allergies médicamenteuses", "ESID — déficits immunitaires primitifs"],
 pratique="consultation d'allergologie avec interprétation de tests et plan d'action (éviction, auto-injecteur, immunothérapie)")
