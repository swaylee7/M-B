# -*- coding: utf-8 -*-
# Données des parcours — lot 4 (fondamentales, médecine dentaire, pharmaceutiques). Contenu original Mediverse (proposition pédagogique).
D = {}
LABO1 = "Organisation du laboratoire, hygiène et sécurité, phases pré-analytique, analytique et post-analytique"

D["DEMS-FON-01"] = dict(slug="ANATOMIE_GENERALE", type="anat",
 profil="Anatomie descriptive, topographique, fonctionnelle et radiologique du corps humain ; dissection, enseignement et recherche morphologique au service de la clinique et de la chirurgie.",
 stages=["Laboratoire d'anatomie (dissection, enseignement)", "Imagerie médicale (anatomie en coupes)", "Chirurgie générale et spécialités chirurgicales (anatomie opératoire)", "Médecine légale (autopsie)", "Laboratoire de recherche morphologique / imagerie 3D"],
 annees=[
  ["Ostéologie, arthrologie et myologie", "Membres supérieur et inférieur", "Techniques de dissection et de conservation", "Éthique du don du corps", "Terminologie anatomique internationale"],
  ["Tête et cou", "Thorax et abdomen", "Pelvis et périnée", "Neuroanatomie", "Embryologie appliquée à l'anatomie"],
  ["Anatomie radiologique (scanner, IRM, échographie)", "Anatomie chirurgicale et voies d'abord", "Variations anatomiques", "Méthodologie de recherche morphologique"],
  ["Conception pédagogique et évaluation", "Anatomie numérique et simulation", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Dissection régionale complète", 1, 2), ("Préparation de pièces anatomiques", 1, 2), ("Animation de travaux pratiques", 1, 2), ("Identification des structures sur imagerie en coupes", 2, 3), ("Conduite d'un travail de recherche morphologique", 3, 4)],
 urg=[("Accident d'exposition (coupure, projection) en salle de dissection", "A", ["exposition au sang"]), ("Exposition aux produits de conservation (formol) : conduite à tenir", "A", ["formol"])],
 recos=["Terminologia Anatomica (FIPAT) — terminologie de référence", "IFAA — recommandations sur le don du corps et l'éthique en anatomie", "Loi 18-11 relative à la santé — dispositions sur les prélèvements et dons d'organes (catalogue) ; cadre du don du corps à la science : texte à rechercher"],
 pratique="épreuve pratique de dissection ou d'identification sur pièce et sur imagerie, avec exposé anatomo-clinique")

D["DEMS-FON-02"] = dict(slug="ANATOMIE_ET_CYTOLOGIE_PATHOLOGIQUES_PATHOLOGIE_MOLECULAIRE", type="fond",
 profil="Diagnostic morphologique des maladies sur prélèvements cytologiques et tissulaires, examen extemporané, immunohistochimie et pathologie moléculaire, autopsie clinique ; acteur central des RCP de cancérologie.",
 stages=["Histopathologie générale (macroscopie et microscopie)", "Cytopathologie (gynécologique et non gynécologique)", "Immunohistochimie", "Pathologie moléculaire", "Neuropathologie, dermatopathologie, néphropathologie (stages courts)", "Autopsie clinique"],
 annees=[
  [LABO1, "Techniques histologiques (fixation, inclusion, coupes, colorations)", "Macroscopie : description et échantillonnage des pièces", "Pathologie générale (inflammation, nécrose, tumeurs)", "Cytologie cervico-vaginale"],
  ["Pathologie tumorale par organes (sein, côlon, col, poumon, thyroïde)", "Immunohistochimie : principes et panels", "Classification TNM et compte rendu standardisé", "Examen extemporané"],
  ["Pathologie hématologique (ganglion, moelle)", "Pathologie rénale, hépatique et cutanée médicales", "Pathologie moléculaire : techniques et biomarqueurs prédictifs", "Cytoponction et cytologie des épanchements"],
  ["Pathologie pédiatrique et fœto-placentaire", "Assurance qualité et accréditation", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Examen macroscopique et prélèvement des pièces opératoires", 1, 2), ("Lecture de lames et compte rendu", 1, 3), ("Lecture de frottis cervico-vaginaux", 1, 2), ("Examen extemporané", 2, 3), ("Interprétation d'un panel d'immunohistochimie", 2, 3), ("Interprétation d'un résultat de biologie moléculaire", 3, 4), ("Autopsie clinique", 2, 3)],
 urg=[("Examen extemporané peropératoire", "A", ["extemporane"]), ("Diagnostic urgent : suspicion de lymphome ou de tumeur à traitement immédiat", "B", ["lymphome"]), ("Biopsie rénale ou hépatique en urgence (glomérulonéphrite rapidement progressive, rejet)", "B", ["biopsie renale"]), ("Discordance clinico-pathologique ou erreur d'identification d'un prélèvement", "B", []), ("Exposition au formol ou accident de coupe", "A", ["formol"])],
 recos=["Arrêtés 1500 et 1501 du 08-09/12/2024 (intitulé et programme du DEMS) — annexe non acquise", "OMS — classification des tumeurs (WHO Blue Books, édition en vigueur)", "UICC — classification TNM", "ICCR / CAP — comptes rendus standardisés", "ASCO/CAP — biomarqueurs (HER2, récepteurs hormonaux)", "Système de Bethesda (cytologie cervicale et thyroïdienne)"],
 pratique="lecture de lames (histologie, cytologie) avec diagnostic, diagnostic différentiel et compte rendu structuré")

D["DEMS-FON-03"] = dict(slug="BIOCHIMIE", type="fond",
 profil="Biochimie clinique et moléculaire : exploration des métabolismes et des fonctions d'organes, hormonologie, marqueurs, toxicologie analytique, biologie moléculaire et assurance qualité.",
 stages=["Biochimie générale et urgences", "Hormonologie", "Protéines et immunochimie", "Biochimie spécialisée (maladies héréditaires du métabolisme)", "Biologie moléculaire", "Toxicologie et pharmacologie analytiques", "Services cliniques (réanimation, endocrinologie, néphrologie) en lien"],
 annees=[
  [LABO1, "Équilibre hydro-électrolytique et acido-basique", "Exploration rénale et hépatique", "Glucides et lipides : exploration du diabète et des dyslipidémies", "Contrôle de qualité interne et externe"],
  ["Enzymologie clinique et marqueurs cardiaques", "Protéines sériques et électrophorèse", "Exploration thyroïdienne, surrénalienne, gonadique", "Métabolisme phosphocalcique et du fer", "Gaz du sang"],
  ["Maladies héréditaires du métabolisme (dépistage, orientation)", "Marqueurs tumoraux", "Biologie moléculaire (PCR, séquençage)", "Dosages de médicaments et toxicologie"],
  ["Validation de méthodes et accréditation", "Biochimie et nutrition", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Validation biologique d'un bilan courant", 1, 2), ("Gaz du sang et ionogramme : interprétation", 1, 1), ("Électrophorèse des protéines et immunofixation", 2, 3), ("Vérification d'une méthode analytique", 2, 3), ("Interprétation d'explorations dynamiques hormonales", 2, 3), ("Technique de biologie moléculaire", 3, 4)],
 urg=[("Hyperkaliémie et hyponatrémie critiques : communication immédiate", "A", ["hyperkaliemie", "hyponatremie"]), ("Hypoglycémie et acidocétose : valeurs critiques", "A", ["acidocetose", "hypoglycemie"]), ("Acidose métabolique sévère (trou anionique, lactates)", "A", ["acidose"]), ("Troponine et marqueurs de nécrose en urgence", "B", ["infarctus"]), ("Intoxication (paracétamol, méthanol, lithium) : dosage urgent", "B", ["intoxication"]), ("Hyperammoniémie du nouveau-né (maladie métabolique)", "C", ["maladies hereditaires du metabolisme", "hyperammoniemie"])],
 recos=["IFCC / EFLM — bonnes pratiques et valeurs critiques", "Norme ISO 15189 — laboratoires de biologie médicale", "KDIGO — estimation du débit de filtration glomérulaire", "ADA — critères biologiques du diabète", "SFBC (France) — recommandations de biochimie clinique"],
 pratique="épreuve pratique de laboratoire (dosage, validation, interprétation d'un dossier biologique) avec commentaire clinique")

D["DEMS-FON-04"] = dict(slug="HEMOBIOLOGIE_ET_TRANSFUSION_SANGUINE", type="fond",
 profil="Biologie hématologique (cytologie, hémostase, immuno-hématologie) et médecine transfusionnelle : collecte, préparation et qualification des produits sanguins, sécurité transfusionnelle et hémovigilance.",
 stages=["Laboratoire d'hématologie (cytologie)", "Hémostase", "Immuno-hématologie", "Centre / poste de transfusion sanguine", "Hématologie clinique", "Réanimation et obstétrique (transfusion massive)"],
 annees=[
  [LABO1, "Hémogramme et frottis sanguin", "Groupes sanguins ABO, Rh et autres systèmes", "Bonnes pratiques transfusionnelles", "Don de sang : sélection des donneurs"],
  ["Hémostase et explorations", "Préparation et qualification des produits sanguins labiles", "Recherche d'anticorps irréguliers et compatibilité", "Incompatibilités fœto-maternelles"],
  ["Cytologie médullaire et hémopathies", "Hémovigilance et effets indésirables receveurs", "Transfusion massive et hémorragies graves", "Cytométrie en flux (bases)"],
  ["Gestion d'un centre de transfusion et assurance qualité", "Thérapie cellulaire et aphérèses (orientation)", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Groupage sanguin et contrôle ultime pré-transfusionnel", 1, 1), ("Lecture du frottis sanguin", 1, 2), ("Recherche et identification d'anticorps irréguliers", 2, 3), ("Bilan d'hémostase et interprétation", 1, 2), ("Enquête transfusionnelle après incident", 2, 3), ("Lecture de myélogramme", 2, 4)],
 urg=[("Incident transfusionnel immédiat (hémolyse aiguë, choc)", "A", ["transfusion"]), ("Délivrance en urgence vitale (sang O, protocole de transfusion massive)", "A", ["transfusion massive"]), ("Coagulation intravasculaire disséminée : bilan urgent", "B", ["coagulation intravasculaire"]), ("Hyperleucocytose et blastes au frottis : alerte", "B", ["leucemie", "leucostase"]), ("Schizocytes (microangiopathie thrombotique) : alerte", "B", ["microangiopathie"]), ("Anticoagulant circulant et hémorragie", "C", ["anticoagul"])],
 recos=["Agence nationale du sang (Algérie) — bonnes pratiques transfusionnelles et hémovigilance (textes à acquérir)", "OMS — sécurité transfusionnelle et sélection des donneurs", "Conseil de l'Europe (EDQM) — guide de préparation et d'utilisation des composants sanguins", "ISTH — hémostase", "BSH — transfusion massive et compatibilité"],
 pratique="épreuve pratique d'immuno-hématologie ou de cytologie avec interprétation et conduite à tenir transfusionnelle")

D["DEMS-FON-05"] = dict(slug="HISTOLOGIE_EMBRYOLOGIE_ET_GENETIQUE_CLINIQUE", type="fond", gardes_type="anat",
 profil="Histologie normale, biologie du développement et de la reproduction, cytogénétique et génétique clinique : de l'enseignement fondamental au diagnostic chromosomique et au conseil génétique.",
 stages=["Laboratoire d'histologie (techniques et enseignement)", "Cytogénétique", "Génétique moléculaire", "Consultation de génétique clinique", "Biologie de la reproduction (si disponible)", "Médecine fœtale"],
 annees=[
  ["Histologie générale et des tissus", "Techniques histologiques et microscopie", "Gamétogenèse, fécondation et développement embryonnaire précoce", "Bases de cytogénétique et caryotype", LABO1],
  ["Histologie des appareils et des organes", "Organogenèse et malformations congénitales", "Anomalies chromosomiques de nombre et de structure", "Génétique formelle et calcul de risque"],
  ["Cytogénétique moléculaire (FISH, ACPA)", "Génétique moléculaire et interprétation des variants", "Biologie de la reproduction et infertilité", "Diagnostic prénatal"],
  ["Consultation de génétique et conseil génétique", "Recherche et enseignement", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Préparation et lecture de lames d'histologie", 1, 2), ("Culture cellulaire et caryotype", 1, 3), ("Lecture d'un caryotype et formule chromosomique", 1, 2), ("FISH : réalisation et interprétation", 2, 3), ("Spermogramme (si activité)", 2, 3), ("Arbre généalogique et conseil génétique supervisé", 2, 4)],
 urg=[("Caryotype urgent chez un nouveau-né à sexe indéterminé ou polymalformé", "A", ["polymalform"]), ("Diagnostic prénatal dans des délais contraints", "B", ["prenatal"]), ("Annonce d'un résultat chromosomique défavorable", "B", ["annonce d un diagnostic"])],
 recos=["Arrêté 233 du 21/02/2024 (programme du DEMS) — annexe non acquise", "ISCN — nomenclature internationale de cytogénétique (édition en vigueur)", "ACMG/AMP — classification des variants", "ESHG — tests génétiques ; ESHRE — biologie de la reproduction", "OMS — manuel d'analyse du sperme (édition en vigueur)"],
 pratique="épreuve pratique de lecture (lames histologiques, caryotypes) et interprétation génétique d'un dossier")

D["DEMS-FON-06"] = dict(slug="IMMUNOLOGIE", type="fond",
 profil="Immunologie biologique et clinique : auto-immunité, déficits immunitaires, allergie, immunochimie, histocompatibilité et transplantation, immunologie des tumeurs.",
 stages=["Laboratoire d'immunologie (auto-immunité, protéines)", "Histocompatibilité (HLA) et transplantation", "Cytométrie en flux", "Allergologie", "Médecine interne / rhumatologie", "Néphrologie (greffe)"],
 annees=[
  [LABO1, "Immunité innée et adaptative", "Immunoglobulines et électrophorèse", "Auto-anticorps : techniques (immunofluorescence, ELISA, immunoblot)", "Complément"],
  ["Diagnostic biologique des maladies auto-immunes systémiques et d'organe", "Déficits immunitaires primitifs et secondaires", "Hypersensibilités et allergie (IgE spécifiques)", "Cytométrie en flux (populations lymphocytaires)"],
  ["Système HLA, typage et cross-match", "Immunologie de la transplantation", "Gammapathies monoclonales et cryoglobulines", "Immunothérapies et biothérapies (surveillance biologique)"],
  ["Vaccinologie", "Assurance qualité et accréditation", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Lecture d'immunofluorescence indirecte (anticorps antinucléaires)", 1, 2), ("Électrophorèse et immunofixation des protéines", 1, 2), ("Immunophénotypage lymphocytaire", 2, 3), ("Typage HLA et cross-match", 2, 4), ("Interprétation d'un bilan d'auto-immunité", 2, 3)],
 urg=[("Cross-match avant greffe de donneur décédé", "A", ["transplantation renale"]), ("Suspicion de déficit immunitaire sévère du nourrisson (lymphopénie)", "B", ["deficit immunitaire"]), ("Anti-MBG / ANCA en urgence (syndrome pneumo-rénal)", "B", ["vascularite"]), ("Tryptase sérique après anaphylaxie", "B", ["anaphyla"])],
 recos=["EULAR / ACR — critères de classification utilisant les auto-anticorps", "ICAP — nomenclature des aspects d'immunofluorescence (anticorps antinucléaires)", "ESID / IUIS — déficits immunitaires primitifs", "EFI / ASHI — histocompatibilité", "Norme ISO 15189"],
 pratique="épreuve pratique de laboratoire (lecture d'immunofluorescence, électrophorèse, cytométrie) et interprétation d'un dossier")

D["DEMS-FON-08"] = dict(slug="MICROBIOLOGIE", type="fond",
 profil="Diagnostic bactériologique et virologique, antibiogramme et résistances, hygiène hospitalière, surveillance épidémiologique et biosécurité.",
 stages=["Bactériologie (hémocultures, LCR, urines, prélèvements profonds)", "Mycobactériologie", "Virologie et sérologie", "Biologie moléculaire", "Hygiène hospitalière", "Services cliniques (infectiologie, réanimation)"],
 annees=[
  [LABO1, "Biosécurité et niveaux de confinement", "Examen direct, coloration de Gram, cultures", "Identification bactérienne", "Antibiogramme et règles de lecture"],
  ["Hémocultures et LCR : circuit urgent", "Mycobactéries : microscopie, culture, tests moléculaires", "Bactéries multirésistantes et surveillance", "Sérologies infectieuses (VIH, hépatites, brucellose)"],
  ["Virologie : charge virale, génotypage", "Diagnostic moléculaire syndromique", "Hygiène hospitalière : enquêtes et environnement", "Épidémiologie microbiologique"],
  ["Assurance qualité et accréditation", "Réseaux de surveillance des résistances", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Examen direct et coloration de Gram", 1, 1), ("Ensemencement, identification et antibiogramme", 1, 2), ("Coloration de Ziehl-Neelsen et auramine", 1, 2), ("Test moléculaire (PCR, Xpert)", 2, 3), ("Interprétation d'un antibiogramme et phénotype de résistance", 2, 3), ("Enquête d'hygiène (prélèvements d'environnement)", 2, 3)],
 urg=[("LCR purulent : examen direct urgent et communication", "A", ["meningite"]), ("Hémoculture positive : Gram et appel du clinicien", "A", ["sepsis"]), ("Accident d'exposition au laboratoire (biosécurité)", "A", ["exposition au sang"]), ("Bactérie multirésistante émergente : alerte et isolement", "B", ["multiresist"]), ("Suspicion d'agent hautement pathogène (charbon, peste) : circuit sécurisé", "C", ["charbon"])],
 recos=["CA-SFM / EUCAST — règles de lecture de l'antibiogramme (version annuelle)", "CLSI — standards d'antibiogramme", "OMS — biosécurité au laboratoire (manuel en vigueur)", "OMS — tuberculose : diagnostic (catalogue)", "Réseau algérien de surveillance de la résistance des bactéries aux antibiotiques (AARN) — rapports à acquérir"],
 pratique="épreuve pratique de bactériologie (examen direct, identification, antibiogramme) avec interprétation clinique")

D["DEMS-FON-09"] = dict(slug="PARASITOLOGIE_MYCOLOGIE", type="fond",
 profil="Diagnostic des parasitoses et mycoses (paludisme, leishmanioses, hydatidose, toxoplasmose, mycoses superficielles et invasives), entomologie médicale et épidémiologie des maladies parasitaires.",
 stages=["Parasitologie (examens directs, sérologies)", "Mycologie médicale", "Biologie moléculaire", "Infectiologie et dermatologie (lien clinique)", "Entomologie / terrain (si organisé)", "Hématologie (patients neutropéniques)"],
 annees=[
  [LABO1, "Examen parasitologique des selles", "Paludisme : frottis, goutte épaisse, tests rapides", "Leishmanioses : diagnostic direct", "Mycoses superficielles : prélèvements et culture"],
  ["Sérologies parasitaires (toxoplasmose, hydatidose, leishmaniose viscérale)", "Helminthoses tissulaires", "Candidoses et cryptococcose", "Toxoplasmose congénitale"],
  ["Mycoses invasives (aspergillose, mucormycose) chez l'immunodéprimé", "Diagnostic moléculaire en parasitologie et mycologie", "Antifongigramme", "Entomologie médicale et vecteurs"],
  ["Épidémiologie et programmes de lutte (paludisme, leishmanioses)", "Assurance qualité", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Frottis et goutte épaisse : lecture et parasitémie", 1, 1), ("Examen parasitologique des selles", 1, 1), ("Ponction de moelle ou de lésion cutanée pour leishmanies (lecture)", 1, 2), ("Prélèvement et culture mycologique", 1, 2), ("Interprétation de sérologies parasitaires", 2, 3), ("PCR parasitaire ou fongique", 3, 4)],
 urg=[("Paludisme : diagnostic en urgence et parasitémie", "A", ["paludisme"]), ("Leishmaniose viscérale chez l'enfant : diagnostic urgent", "B", ["leishmaniose"]), ("Infection fongique invasive chez le neutropénique", "B", ["neutropeni"]), ("Cryptococcose neuroméningée", "B", ["cryptococ"]), ("Choc anaphylactique et kyste hydatique (examen d'un liquide de kyste)", "C", ["kyste hydatique"])],
 recos=["OMS — paludisme : lignes directrices (catalogue)", "Ministère de la Santé (Algérie) — programmes de lutte contre le paludisme et les leishmanioses (textes à acquérir)", "OMS — échinococcose kystique ; leishmanioses", "ECMM / ESCMID / IDSA — infections fongiques invasives", "CDC — DPDx (identification des parasites)"],
 pratique="épreuve pratique de lecture (frottis, goutte épaisse, selles, cultures fongiques) avec interprétation")

D["DEMS-FON-10"] = dict(slug="PHARMACOLOGIE_CLINIQUE", type="fond", gardes_type="anat",
 profil="Bon usage des médicaments chez le patient : pharmacocinétique clinique et suivi thérapeutique, pharmacovigilance, interactions, populations particulières, essais cliniques et information sur le médicament.",
 stages=["Pharmacologie clinique / centre de pharmacovigilance", "Laboratoire de dosage des médicaments (suivi thérapeutique)", "Centre antipoison / toxicovigilance", "Services cliniques (réanimation, infectiologie, transplantation)", "Unité de recherche clinique"],
 annees=[
  ["Pharmacocinétique et pharmacodynamie cliniques", "Effets indésirables : imputabilité et déclaration", "Interactions médicamenteuses", "Prescription chez l'insuffisant rénal et hépatique", "Réglementation du médicament en Algérie"],
  ["Suivi thérapeutique pharmacologique (anti-infectieux, immunosuppresseurs, antiépileptiques)", "Médicament et grossesse, allaitement, enfant, sujet âgé", "Pharmacogénétique", "Iatrogénie et analyse des causes"],
  ["Méthodologie des essais cliniques et éthique", "Pharmaco-épidémiologie", "Médicaments génériques et biosimilaires", "Information sur le médicament et lecture critique"],
  ["Bon usage, comités du médicament", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Analyse d'imputabilité d'un effet indésirable", 1, 1), ("Avis pharmacologique écrit (adaptation de posologie, interaction)", 1, 2), ("Interprétation d'un dosage de médicament", 1, 2), ("Revue de prescriptions (iatrogénie)", 2, 3), ("Rédaction d'un protocole d'essai clinique", 3, 4)],
 urg=[("Effet indésirable grave : déclaration et conduite à tenir", "A", ["effet indesirable"]), ("Surdosage médicamenteux (digoxine, lithium, aminosides, antivitamine K)", "A", ["intoxication"]), ("Exposition médicamenteuse pendant la grossesse : avis urgent", "B", ["medicaments et grossesse"]), ("Toxidermie grave : imputabilité", "B", ["toxidermie"])],
 recos=["Centre national de pharmacovigilance et de matériovigilance (Algérie) — bonnes pratiques (textes à acquérir)", "OMS / Uppsala Monitoring Centre — pharmacovigilance", "ICH — bonnes pratiques cliniques (E6)", "EMA — guides de pharmacovigilance (GVP)", "OMS — liste modèle des médicaments essentiels (catalogue)"],
 pratique="analyse commentée d'un cas d'iatrogénie ou d'un dosage, avec avis pharmacologique argumenté")

D["DEMS-FON-11"] = dict(slug="PHYSIOLOGIE_CLINIQUE_EXPLORATIONS_METABOLIQUES_NUTRITIONNELLES", type="fond", gardes_type="anat",
 profil="Physiologie appliquée et explorations fonctionnelles du métabolisme et de la nutrition : composition corporelle, dépense énergétique, explorations du métabolisme glucidique, lipidique et phosphocalcique, nutrition clinique.",
 stages=["Laboratoire de physiologie / explorations fonctionnelles métaboliques", "Nutrition clinique", "Endocrinologie-diabétologie", "Pédiatrie (croissance, nutrition)", "Réanimation (nutrition artificielle)"],
 annees=[
  ["Physiologie de la nutrition et du métabolisme énergétique", "Évaluation de l'état nutritionnel", "Composition corporelle (impédancemétrie, absorptiométrie)", "Régulation de la glycémie", LABO1],
  ["Explorations du métabolisme glucidique (hyperglycémie provoquée, insulinosécrétion)", "Calorimétrie indirecte", "Dénutrition et obésité : explorations", "Métabolisme phosphocalcique et osseux"],
  ["Nutrition artificielle entérale et parentérale", "Nutrition de l'enfant, de la femme enceinte et du sujet âgé", "Exploration du métabolisme lipidique et hépatique", "Physiologie de l'exercice et métabolisme"],
  ["Recherche en nutrition et santé publique", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Évaluation nutritionnelle complète", 1, 1), ("Mesure de composition corporelle", 1, 2), ("Épreuve d'hyperglycémie provoquée et interprétation", 1, 2), ("Calorimétrie indirecte", 2, 3), ("Prescription d'une nutrition artificielle", 2, 3)],
 urg=[("Hypoglycémie pendant une épreuve fonctionnelle", "A", ["hypoglycemie"]), ("Syndrome de renutrition inappropriée", "B", ["renutrition", "malnutrition"]), ("Dénutrition sévère de l'enfant", "B", ["malnutrition"])],
 recos=["ESPEN — nutrition clinique (dénutrition, nutrition artificielle)", "OMS — malnutrition aiguë (catalogue) ; besoins nutritionnels", "ADA — critères diagnostiques du diabète", "SFNCM (France) — nutrition clinique"],
 pratique="épreuve pratique d'exploration fonctionnelle (réalisation et interprétation) et dossier nutritionnel")

D["DEMS-FON-12"] = dict(slug="PHYSIOLOGIE_CLINIQUE_EXPLORATIONS_CARDIO_RESPIRATOIRES_ET_EXERCICE", type="fond", gardes_type="anat",
 profil="Physiologie appliquée et explorations fonctionnelles respiratoires, cardiovasculaires et de l'exercice : EFR, gaz du sang, épreuves d'effort cardio-respiratoires, explorations du sommeil et vasculaires.",
 stages=["Explorations fonctionnelles respiratoires", "Épreuve d'effort cardio-respiratoire", "Explorations du sommeil", "Explorations cardiovasculaires (ECG, Holter, MAPA)", "Pneumologie et cardiologie (lien clinique)", "Médecine du sport / réadaptation"],
 annees=[
  ["Physiologie respiratoire et cardiovasculaire", "Spirométrie et courbes débit-volume", "Gaz du sang", "ECG de repos", "Contrôle qualité et calibration des appareils"],
  ["Pléthysmographie et diffusion du CO", "Tests de provocation bronchique", "Épreuve d'effort cardio-respiratoire (VO2 max)", "Test de marche de six minutes"],
  ["Polygraphie et polysomnographie", "Explorations de la pression artérielle (MAPA) et vasculaires", "Physiologie de l'exercice et du sport", "Évaluation préopératoire fonctionnelle"],
  ["Explorations en altitude, plongée, hyperbarie (notions)", "Recherche en physiologie", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Spirométrie conforme aux normes", 1, 1), ("Gaz du sang artériel", 1, 1), ("Pléthysmographie et DLCO", 1, 2), ("Test de provocation bronchique", 2, 3), ("Conduite d'une épreuve d'effort cardio-respiratoire", 2, 3), ("Lecture de polysomnographie", 3, 4)],
 urg=[("Bronchospasme sévère lors d'un test de provocation", "A", ["asthme"]), ("Malaise, douleur thoracique ou arythmie pendant une épreuve d'effort", "A", ["arret cardio", "coronarien"]), ("Hypoxémie sévère découverte en exploration", "B", ["insuffisance respiratoire"])],
 recos=["ATS/ERS — standardisation de la spirométrie, de la DLCO et des volumes", "ERS — normes de référence (GLI)", "ATS/ACCP — épreuve d'effort cardio-respiratoire", "AASM — scoring du sommeil", "ESC — épreuves d'effort"],
 pratique="réalisation et interprétation d'une exploration fonctionnelle (EFR, épreuve d'effort, polygraphie) avec conclusion clinique")

D["DEMS-FON-13"] = dict(slug="NEUROPHYSIOLOGIE_CLINIQUE_EXPLORATIONS_FONCTIONNELLES_SYSTEME_NERVEUX", type="fond", gardes_type="anat",
 profil="Exploration électrophysiologique du système nerveux central et périphérique : EEG, potentiels évoqués, électroneuromyographie, explorations du sommeil et monitorage peropératoire.",
 stages=["EEG (adulte et enfant)", "Électroneuromyographie", "Potentiels évoqués", "Explorations du sommeil", "Neurologie et neuropédiatrie", "Réanimation (EEG continu)"],
 annees=[
  ["Neurophysiologie fondamentale", "EEG normal de l'adulte et de l'enfant", "Techniques d'enregistrement et artefacts", "Sémiologie EEG des épilepsies", "Sécurité électrique et hygiène"],
  ["Électroneuromyographie : conduction nerveuse et détection", "Neuropathies, atteintes de la jonction neuromusculaire, myopathies", "EEG en réanimation (coma, état de mal)", "Potentiels évoqués (visuels, auditifs, somesthésiques)"],
  ["EEG néonatal", "Polysomnographie et pathologie du sommeil", "Monitorage neurophysiologique peropératoire (orientation)", "Diagnostic de mort encéphalique : place de l'EEG"],
  ["Vidéo-EEG et bilan préchirurgical des épilepsies (orientation)", "Recherche", "Synthèse du programme et préparation de l'examen final"],
 ],
 sf=[("Pose d'électrodes et enregistrement EEG standard", 1, 1), ("Lecture et compte rendu d'EEG", 1, 2), ("Mesures de conduction nerveuse", 1, 2), ("Détection à l'aiguille", 2, 3), ("Stimulation répétitive / jitter", 2, 3), ("Potentiels évoqués", 2, 3), ("EEG de réanimation et de mort encéphalique", 2, 3)],
 urg=[("EEG en urgence : état de mal non convulsif", "A", ["etat de mal"]), ("Coma : EEG pronostique", "B", ["comas"]), ("EEG de confirmation de mort encéphalique", "B", ["mort encephalique"]), ("ENMG en urgence (syndrome de Guillain-Barré, myasthénie)", "B", ["guillain", "myasthen"])],
 recos=["IFCN — standards d'enregistrement EEG et ENMG", "ACNS — terminologie EEG en réanimation", "ILAE — classification des crises et des épilepsies", "AASM — scoring du sommeil", "Réglementation algérienne du constat de la mort encéphalique (texte à rechercher)"],
 pratique="lecture et compte rendu d'enregistrements (EEG, ENMG, potentiels évoqués) avec conclusion clinique")

# ---------------- Médecine dentaire ----------------
D["DEMS-DEN-01"] = dict(slug="ODONTOLOGIE_CONSERVATRICE", type="dent",
 profil="Prévention et traitement des lésions carieuses et non carieuses, endodontie et restauration de la dent, dentisterie esthétique.",
 stages=["Odontologie conservatrice et endodontie", "Urgences dentaires", "Pédodontie", "Prothèse (restaurations)", "Radiologie dentaire"],
 annees=[["Cariologie et prévention", "Matériaux de restauration", "Diagnostic pulpaire et douleur dentaire", "Radiologie dentaire"], ["Endodontie : préparation et obturation canalaires", "Restaurations directes et indirectes", "Traumatismes dentaires"], ["Retraitement endodontique et chirurgie endodontique (orientation)", "Dentisterie esthétique", "Dent et maladies générales"], ["Synthèse du programme et préparation de l'examen final", "Recherche et enseignement clinique"]],
 sf=[("Restauration composite et amalgame", 1, 1), ("Traitement endodontique monoradiculé", 1, 2), ("Traitement endodontique pluriradiculé", 2, 3), ("Retraitement endodontique", 3, 4), ("Restauration indirecte (inlay/onlay)", 2, 3)],
 urg=[("Pulpite aiguë et douleur dentaire intense", "A", ["pulpite"]), ("Abcès apical et cellulite d'origine dentaire", "A", ["cellulite"]), ("Traumatisme dentaire (fracture, luxation, expulsion)", "A", ["traumatisme dentaire"]), ("Syncope et malaise au fauteuil", "B", ["malaise"]), ("Réaction allergique aux anesthésiques locaux", "B", ["anaphyla"])],
 recos=["ESE (European Society of Endodontology) — qualité du traitement endodontique", "IADT — traumatismes dentaires", "FDI — prévention de la carie", "OMS — santé bucco-dentaire"],
 pratique="cas clinique au fauteuil (diagnostic, plan de traitement, réalisation d'un geste) avec radiographies")
D["DEMS-DEN-02"] = dict(slug="ORTHOPEDIE_DENTO_FACIALE", type="dent",
 profil="Diagnostic et traitement des anomalies dento-maxillo-faciales : croissance crânio-faciale, malocclusions, traitements orthodontiques et orthopédiques, collaboration chirurgicale.",
 stages=["Orthopédie dento-faciale", "Pédodontie", "Chirurgie maxillo-faciale (lien ortho-chirurgical)", "ORL (ventilation, fentes)", "Radiologie (céphalométrie)"],
 annees=[["Croissance crânio-faciale", "Examen clinique et céphalométrie", "Classification des malocclusions", "Prévention et interception"], ["Appareils amovibles et fonctionnels", "Techniques multi-attaches", "Biomécanique orthodontique"], ["Traitements ortho-chirurgicaux", "Fentes labio-palatines", "Orthodontie de l'adulte"], ["Contention et récidive", "Synthèse du programme et préparation de l'examen final"]],
 sf=[("Analyse céphalométrique", 1, 1), ("Empreintes et modèles d'étude", 1, 1), ("Pose d'un appareil amovible", 1, 2), ("Collage multi-attaches", 2, 3), ("Plan de traitement ortho-chirurgical", 3, 4)],
 urg=[("Blessure muqueuse par appareil orthodontique", "A", ["orthodont"]), ("Traumatisme dentaire chez un patient appareillé", "B", ["traumatisme dentaire"]), ("Ingestion ou inhalation d'un élément d'appareil", "B", ["corps etranger"])],
 recos=["EOS (European Orthodontic Society) — recommandations", "AAO (American Association of Orthodontists) — guides cliniques", "OMS — santé bucco-dentaire de l'enfant"],
 pratique="analyse d'un dossier orthodontique (céphalométrie, modèles) et plan de traitement argumenté")
D["DEMS-DEN-03"] = dict(slug="PARODONTOLOGIE", type="dent",
 profil="Diagnostic et traitement des maladies parodontales et péri-implantaires, liens avec les maladies générales, chirurgie parodontale et implantaire.",
 stages=["Parodontologie", "Implantologie", "Médecine interne / diabétologie (lien parodonte-santé générale)", "Radiologie dentaire"],
 annees=[["Classification des maladies parodontales", "Examen parodontal et indices", "Traitement non chirurgical (détartrage, surfaçage)", "Hygiène bucco-dentaire et motivation"], ["Parodontites et maladies générales (diabète, grossesse)", "Chirurgie parodontale d'assainissement", "Antibiothérapie en parodontologie"], ["Chirurgie régénératrice et muco-gingivale", "Implantologie et maladies péri-implantaires"], ["Maintenance parodontale", "Synthèse du programme et préparation de l'examen final"]],
 sf=[("Charting parodontal complet", 1, 1), ("Détartrage-surfaçage", 1, 1), ("Lambeau d'assainissement", 2, 3), ("Greffe gingivale", 3, 4), ("Pose d'implant (aide)", 3, 9)],
 urg=[("Gingivite ulcéro-nécrotique", "A", ["gingivite"]), ("Abcès parodontal", "A", ["abces parodontal"]), ("Hémorragie après chirurgie parodontale", "B", []), ("Patient sous anticoagulant : gestion du risque hémorragique", "B", ["anticoagul"])],
 recos=["EFP (European Federation of Periodontology) — S3 guidelines du traitement des parodontites", "Classification AAP/EFP des maladies et affections parodontales et péri-implantaires (World Workshop 2017)", "OMS — santé bucco-dentaire"],
 pratique="cas clinique parodontal (diagnostic selon la classification en vigueur, plan de traitement, geste)")
D["DEMS-DEN-04"] = dict(slug="PATHOLOGIE_ET_CHIRURGIE_BUCCALE", type="dent",
 profil="Pathologie de la muqueuse buccale et des maxillaires, chirurgie buccale (extractions complexes, kystes, tumeurs bénignes), prise en charge des patients à risque médical.",
 stages=["Pathologie et chirurgie buccale", "Chirurgie maxillo-faciale", "Anatomie pathologique (lésions buccales)", "Médecine interne / hématologie (patients à risque)", "Radiologie (cone beam)"],
 annees=[["Anesthésie locale et extraction", "Patients à risque médical (anticoagulés, cardiopathes, diabétiques, irradiés)", "Infections bucco-dentaires", "Radiologie"], ["Dents incluses et extractions chirurgicales", "Kystes et tumeurs bénignes des maxillaires", "Lésions de la muqueuse buccale"], ["Lésions précancéreuses et cancers de la cavité buccale (dépistage)", "Ostéoradionécrose et ostéonécrose médicamenteuse", "Traumatologie alvéolo-dentaire"], ["Synthèse du programme et préparation de l'examen final", "Recherche et enseignement"]],
 sf=[("Extraction simple sous anesthésie locale", 1, 1), ("Avulsion de dent de sagesse incluse", 1, 2), ("Biopsie de la muqueuse buccale", 1, 2), ("Énucléation de kyste", 2, 3), ("Hémostase locale chez le patient anticoagulé", 1, 2)],
 urg=[("Cellulite cervico-faciale d'origine dentaire", "A", ["cellulite"]), ("Hémorragie post-extractionnelle", "A", ["hemorragie post extraction"]), ("Malaise, syncope, crise d'angor au fauteuil", "A", ["malaise"]), ("Anaphylaxie aux anesthésiques ou antibiotiques", "B", ["anaphyla"]), ("Communication bucco-sinusienne et alvéolite", "B", ["alveolite"]), ("Fracture alvéolo-dentaire et de la mandibule", "C", ["fracture"])],
 recos=["SFCO (France) — patients sous antithrombotiques, antibiothérapie en odontologie", "AHA — prophylaxie de l'endocardite (procédures dentaires)", "AAOMS — ostéonécrose des mâchoires liée aux médicaments", "OMS — cancer de la cavité buccale"],
 pratique="cas clinique de chirurgie buccale chez un patient à risque (évaluation, geste, prescription)")
D["DEMS-DEN-05"] = dict(slug="PROTHESE_DENTAIRE", type="dent",
 profil="Réhabilitation prothétique : prothèse fixée, amovible partielle et complète, prothèse sur implants, prothèse maxillo-faciale, occlusodontie.",
 stages=["Prothèse fixée", "Prothèse amovible", "Prothèse sur implants", "Prothèse maxillo-faciale", "Laboratoire de prothèse", "Occlusodontie"],
 annees=[["Occlusion et articulateurs", "Empreintes et matériaux", "Prothèse amovible complète", "Préparations périphériques"], ["Prothèse fixée unitaire et plurale", "Prothèse amovible partielle", "Esthétique et couleur"], ["Prothèse sur implants", "Prothèse maxillo-faciale (obturateurs, épithèses)", "Dysfonctionnements de l'appareil manducateur"], ["Réhabilitations globales", "Synthèse du programme et préparation de l'examen final"]],
 sf=[("Empreintes primaires et secondaires", 1, 1), ("Prothèse complète : étapes cliniques", 1, 2), ("Préparation pour couronne", 1, 2), ("Bridge", 2, 3), ("Prothèse supra-implantaire", 3, 4), ("Obturateur maxillaire", 3, 4)],
 urg=[("Blessure muqueuse prothétique", "A", ["prothese dentaire"]), ("Descellement ou fracture de prothèse fixée", "A", ["prothese dentaire"]), ("Ingestion ou inhalation d'un élément prothétique", "B", ["corps etranger"]), ("Luxation de l'articulation temporo-mandibulaire", "B", ["temporo mandibulaire"])],
 recos=["Arrêté 1399 du 21/11/2024 (programme du DEMS) — annexe non acquise", "EPA / ACP — recommandations en prothèse", "ITI — consensus en implantologie", "Glossary of Prosthodontic Terms (édition en vigueur)"],
 pratique="cas clinique de réhabilitation prothétique (diagnostic, plan de traitement, étape clinique)")

# ---------------- Pharmaceutiques (correspondance avec la bibliothèque) ----------------
D["DEMS-PHA-01"] = dict(slug="BIOPHYSIQUE_PHARMACEUTIQUE", type="fond", gardes_type="anat",
 profil="Biophysique appliquée aux sciences pharmaceutiques : méthodes physiques d'analyse, radiopharmacie et radioprotection, biophysique des formes pharmaceutiques et des membranes.",
 stages=["Laboratoire de biophysique pharmaceutique", "Radiopharmacie / médecine nucléaire", "Laboratoire de contrôle des médicaments", "Unité de radioprotection"],
 annees=[["Rayonnements et radioprotection", "Méthodes spectroscopiques", "Biophysique des solutions et des membranes", LABO1], ["Radiopharmaceutiques : préparation et contrôle", "Méthodes physiques d'analyse (RMN, spectrométrie de masse : principes)", "Cinétique et transport membranaire"], ["Contrôle qualité en radiopharmacie", "Biophysique des formes galéniques", "Méthodologie de recherche"], ["Enseignement et recherche", "Synthèse du programme et préparation de l'examen final"]],
 sf=[("Contrôle de pureté radiochimique", 1, 2), ("Mesure d'activité et calcul de décroissance", 1, 1), ("Analyse spectroscopique", 1, 2), ("Gestion d'une contamination de surface", 2, 3)],
 urg=[("Contamination radioactive au laboratoire", "A", ["contamination"]), ("Erreur de préparation d'un radiopharmaceutique", "B", ["radiopharmaceutique"])],
 recos=["Pharmacopée européenne / internationale — monographies des radiopharmaceutiques", "AIEA — radiopharmacie et radioprotection", "EANM — bonnes pratiques de radiopharmacie"],
 pratique="épreuve pratique de laboratoire (contrôle, mesure, analyse) avec interprétation")
D["DEMS-PHA-07"] = dict(slug="PHARMACOLOGIE_PHARMACEUTIQUE", type="fond", gardes_type="anat",
 profil="Pharmacologie fondamentale et appliquée dans la filière pharmaceutique : mécanismes d'action, pharmacocinétique, évaluation préclinique, pharmacovigilance et bon usage du médicament.",
 stages=["Laboratoire de pharmacologie", "Pharmacovigilance", "Pharmacie hospitalière", "Laboratoire de dosage des médicaments", "Unité de recherche clinique"],
 annees=[["Pharmacodynamie et récepteurs", "Pharmacocinétique", "Pharmacologie des grandes classes", LABO1], ["Évaluation préclinique et toxicologie réglementaire", "Interactions médicamenteuses", "Pharmacovigilance"], ["Pharmacocinétique de population et suivi thérapeutique", "Essais cliniques", "Biomédicaments"], ["Enseignement et recherche", "Synthèse du programme et préparation de l'examen final"]],
 sf=[("Modélisation pharmacocinétique simple", 1, 2), ("Analyse d'imputabilité", 1, 2), ("Dosage d'un médicament", 2, 3), ("Protocole d'étude préclinique", 3, 4)],
 urg=[("Effet indésirable grave : déclaration", "A", ["effet indesirable"]), ("Surdosage médicamenteux : avis et dosage", "B", ["intoxication"])],
 recos=["OMS — pharmacovigilance ; liste des médicaments essentiels (catalogue)", "ICH — lignes directrices (sécurité, efficacité)", "EMA — guides de pharmacovigilance"],
 pratique="épreuve pratique de pharmacologie (expérimentation, calcul pharmacocinétique, analyse d'un cas) avec commentaire")
