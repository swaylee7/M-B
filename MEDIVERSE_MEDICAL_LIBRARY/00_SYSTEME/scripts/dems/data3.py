# -*- coding: utf-8 -*-
# Données des parcours — lot 3 (spécialités chirurgicales). Contenu original Mediverse (proposition pédagogique).
D = {}
SOCLE_CHIR = ["Asepsie, bloc opératoire, instrumentation, sutures et cicatrisation", "Évaluation préopératoire, consentement, check-list de sécurité"]

D["DEMS-CHI-02"] = dict(slug="CHIRURGIE_CARDIAQUE", type="chir",
 profil="Chirurgie du cœur et des gros vaisseaux intrathoraciques : revascularisation coronaire, chirurgie valvulaire, aorte thoracique, cardiopathies congénitales, assistance circulatoire.",
 stages=["Chirurgie cardiaque adulte", "Réanimation postopératoire de chirurgie cardiaque", "Circulation extracorporelle (perfusion)", "Cardiologie (échocardiographie, coronarographie)", "Chirurgie cardiaque pédiatrique (si disponible)", "Chirurgie thoracique et vasculaire (stages courts)", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Anatomie chirurgicale du cœur et du médiastin", "Physiologie cardiovasculaire et circulation extracorporelle", "Surveillance postopératoire et complications précoces"],
  ["Chirurgie coronaire : indications, greffons, techniques", "Valvulopathies : indications opératoires, prothèses mécaniques et biologiques", "Anticoagulation des porteurs de prothèses", "Échocardiographie peropératoire (lecture)"],
  ["Chirurgie de l'aorte thoracique (anévrysmes, dissections)", "Endocardite : indications chirurgicales", "Cardiopathies congénitales : principes", "Protection myocardique"],
  ["Chirurgie valvulaire conservatrice (réparation mitrale)", "Assistance circulatoire et ECMO", "Techniques mini-invasives et percutanées (indications partagées)"],
  ["Synthèse du programme ; autonomie opératoire sur les interventions courantes", "Réunions médico-chirurgicales (Heart Team)", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Sternotomie et fermeture sternale", 1, 3), ("Canulation et mise en route de la circulation extracorporelle (aide)", 2, 4), ("Prélèvement de greffons (veine saphène, artère mammaire)", 2, 4), ("Remplacement valvulaire aortique", 3, 5), ("Pontages coronaires", 3, 5), ("Drainage péricardique et reprise pour tamponnade", 2, 3), ("Pose d'ECMO", 4, 9)],
 urg=[("Tamponnade postopératoire et saignement après chirurgie cardiaque", "A", ["tamponnade"]), ("Arrêt cardiaque après chirurgie cardiaque (réouverture thoracique)", "A", ["arret cardio"]), ("Bas débit cardiaque postopératoire", "A", ["choc cardiogenique", "etats de choc"]), ("Dissection aortique de type A", "B", ["dissection aortique"]), ("Complication mécanique de l'infarctus (rupture septale, insuffisance mitrale aiguë)", "B", ["infarctus"]), ("Thrombose de prothèse valvulaire", "B", ["prothese valvulaire"]), ("Endocardite avec indication chirurgicale urgente", "B", ["endocardite"]), ("Plaie du cœur", "C", ["plaie du coeur"]), ("Médiastinite postopératoire", "C", ["mediastinite"])],
 recos=["Arrêté 1199 du 23/10/2024 (programme du DEMS) — annexe non acquise", "ESC / EACTS — revascularisation myocardique, valvulopathies", "ESC — endocardite infectieuse ; pathologies de l'aorte", "EACTS / ELSO — assistance circulatoire et ECMO", "STS (Society of Thoracic Surgeons) — évaluation du risque opératoire"],
 pratique="dossier de chirurgie cardiaque (indication, technique, gestion d'une complication) et/ou évaluation gestuelle en simulation")

D["DEMS-CHI-04"] = dict(slug="NEUROCHIRURGIE", type="chir",
 profil="Chirurgie du système nerveux central et périphérique et du rachis : traumatologie crânio-rachidienne, tumeurs, pathologie vasculaire, hydrocéphalie, rachis dégénératif, neurochirurgie pédiatrique.",
 stages=["Neurochirurgie (urgences et traumatologie)", "Neurochirurgie programmée (tumeurs, rachis)", "Neuroréanimation", "Neuroradiologie", "Neurologie (stage court)", "Neurochirurgie pédiatrique", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Neuroanatomie chirurgicale", "Examen neurologique, score de Glasgow, hypertension intracrânienne", "Traumatismes crâniens : hématomes extra- et sous-duraux"],
  ["Traumatismes du rachis et de la moelle", "Hydrocéphalies et dérivations", "Lecture du scanner et de l'IRM cérébro-médullaires", "Hernies discales et canal lombaire étroit"],
  ["Tumeurs cérébrales et médullaires", "Hémorragie méningée et anévrysmes (prise en charge multidisciplinaire)", "Infections neurochirurgicales (abcès, empyèmes)", "Malformations de la charnière, dysraphismes"],
  ["Chirurgie du rachis instrumentée", "Nerfs périphériques", "Neurochirurgie fonctionnelle (orientation)"],
  ["Synthèse ; autonomie sur les urgences neurochirurgicales", "Organisation de la garde et des transferts", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Trou de trépan et évacuation d'hématome sous-dural chronique", 1, 2), ("Pose de dérivation ventriculaire externe", 1, 3), ("Craniotomie pour hématome extradural", 2, 3), ("Dérivation ventriculo-péritonéale", 2, 4), ("Discectomie lombaire", 2, 4), ("Exérèse de tumeur cérébrale", 3, 5), ("Ostéosynthèse rachidienne", 3, 5)],
 urg=[("Hématome extradural", "A", ["hematome extradural", "traumatisme cranien"]), ("Traumatisme crânien grave et hypertension intracrânienne", "A", ["traumatisme cranien", "hypertension intracranienne"]), ("Hématome sous-dural aigu", "A", ["sous dural"]), ("Compression médullaire traumatique ou tumorale", "A", ["compression medullaire"]), ("Syndrome de la queue de cheval", "A", ["queue de cheval"]), ("Hydrocéphalie aiguë / dysfonction de valve", "B", ["hydrocephalie"]), ("Hémorragie méningée par rupture d'anévrysme", "B", ["hemorragie meningee"]), ("Abcès cérébral et empyème", "B", ["abces cerebral"]), ("Plaie crânio-cérébrale", "C", ["plaie cranio"]), ("Engagement cérébral", "C", ["engagement cerebral"])],
 recos=["Brain Trauma Foundation — traumatisme crânien grave", "EANS / AANS-CNS — traumatismes rachidiens et médullaires", "ESO / AHA-ASA — hémorragie méningée anévrysmale", "EANO — tumeurs cérébrales", "NICE — head injury (évaluation et imagerie)"],
 pratique="dossier neurochirurgical avec lecture d'imagerie, indication opératoire et technique, ou gestion d'une urgence")

D["DEMS-CHI-05"] = dict(slug="CHIRURGIE_ORTHOPEDIQUE_ET_TRAUMATOLOGIQUE", type="chir",
 profil="Chirurgie de l'appareil locomoteur : traumatologie des membres, du bassin et du rachis, polytraumatisé, chirurgie orthopédique programmée (arthroplasties, rachis, orthopédie pédiatrique), infections et tumeurs osseuses.",
 stages=["Traumatologie et urgences", "Orthopédie programmée (hanche, genou)", "Chirurgie de la main et du membre supérieur", "Chirurgie du rachis", "Orthopédie pédiatrique", "Chirurgie septique", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Examen ostéo-articulaire et lecture radiographique", "Fractures : classification, principes de traitement orthopédique et chirurgical", "Plâtres, attelles et tractions"],
  ["Fractures des membres (radius, humérus, fémur, jambe, cheville)", "Luxations et entorses graves", "Fractures de l'extrémité proximale du fémur du sujet âgé", "Plaies de la main", "Fractures ouvertes"],
  ["Traumatismes du bassin et du rachis", "Polytraumatisé : stratégie orthopédique", "Infections ostéo-articulaires et sur matériel", "Arthrose de la hanche et du genou : arthroplasties"],
  ["Orthopédie pédiatrique (luxation congénitale de hanche, pied bot, épiphysiolyse)", "Tumeurs osseuses (orientation)", "Chirurgie arthroscopique et ligamentaire", "Chirurgie du rachis dégénératif"],
  ["Synthèse ; autonomie sur la traumatologie courante", "Organisation de la garde et du bloc", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Réduction et contention plâtrée des fractures et luxations", 1, 1), ("Parage de fracture ouverte", 1, 2), ("Embrochage et ostéosynthèse simple", 1, 3), ("Enclouage centromédullaire", 2, 4), ("Prothèse intermédiaire de hanche", 2, 4), ("Fixateur externe", 2, 3), ("Prothèse totale de hanche et de genou", 3, 5), ("Arthroscopie du genou", 3, 5)],
 urg=[("Fracture ouverte", "A", ["fracture ouverte"]), ("Luxation à réduire en urgence (hanche, épaule, coude)", "A", ["luxation"]), ("Syndrome des loges", "A", ["syndrome des loges"]), ("Polytraumatisé : fixation du bassin et des fractures", "A", ["polytraumatis"]), ("Fracture avec complication vasculo-nerveuse", "A", ["vasculo nerveuse"]), ("Arthrite septique et ostéomyélite aiguë", "B", ["arthrite septique", "osteomyelite"]), ("Traumatisme du rachis avec signes neurologiques", "B", ["traumatismes du rachis", "traumatisme du rachis"]), ("Plaie de la main (tendons, nerfs)", "B", ["plaies de la main"]), ("Embolie graisseuse", "C", ["embolie graisseuse"]), ("Infection aiguë sur prothèse", "C", ["infection sur prothese", "infections ostéo-articulaires sur", "infections osteo articulaires sur"])],
 recos=["AO Foundation — principes de traitement des fractures", "BOA / BAPRAS — fractures ouvertes", "ATLS — polytraumatisé", "SOFCOT (France) — conférences d'enseignement et recommandations", "NICE — fracture de l'extrémité proximale du fémur", "ICM — infections ostéo-articulaires sur prothèse"],
 pratique="cas de traumatologie ou d'orthopédie avec lecture radiographique, indication et technique, et/ou évaluation gestuelle")

D["DEMS-CHI-06"] = dict(slug="CHIRURGIE_PEDIATRIQUE", type="chir",
 profil="Chirurgie du nouveau-né, de l'enfant et de l'adolescent : malformations congénitales, chirurgie viscérale et urologique pédiatrique, traumatologie et orthopédie de l'enfant, oncologie chirurgicale pédiatrique.",
 stages=["Chirurgie viscérale pédiatrique et urgences", "Chirurgie néonatale", "Urologie pédiatrique", "Orthopédie et traumatologie de l'enfant", "Réanimation pédiatrique et néonatale", "Oncologie pédiatrique", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Particularités physiologiques de l'enfant opéré (thermorégulation, volumes, douleur)", "Appendicite, invagination, hernies de l'enfant", "Traumatologie de l'enfant (fractures spécifiques)"],
  ["Urgences néonatales : atrésies, occlusions, hernie diaphragmatique, laparoschisis", "Sténose du pylore", "Uropathies malformatives (reflux, jonction pyélo-urétérale, valves)", "Ectopie testiculaire, hypospadias"],
  ["Malformations anorectales et maladie de Hirschsprung", "Tumeurs solides de l'enfant (néphroblastome, neuroblastome)", "Orthopédie pédiatrique (hanche, pied bot, scoliose)", "Brûlures de l'enfant"],
  ["Cœliochirurgie pédiatrique", "Chirurgie thoracique de l'enfant", "Diagnostic anténatal et consultation prénatale"],
  ["Synthèse ; autonomie sur les urgences pédiatriques courantes", "Organisation de la garde", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Appendicectomie de l'enfant", 1, 2), ("Cure de hernie inguinale de l'enfant", 1, 3), ("Réduction pneumatique ou hydrostatique d'invagination (avec le radiologue)", 2, 3), ("Pylorotomie extramuqueuse", 2, 3), ("Orchidopexie", 2, 4), ("Chirurgie néonatale (atrésie de l'œsophage, du grêle)", 3, 5), ("Pyéloplastie", 3, 5)],
 urg=[("Invagination intestinale aiguë", "A", ["invagination"]), ("Appendicite et péritonite de l'enfant", "A", ["appendicite", "peritonite"]), ("Torsion du testicule", "A", ["torsion du testicule", "torsion testiculaire"]), ("Hernie inguinale étranglée de l'enfant", "A", ["hernie"]), ("Occlusion néonatale (volvulus du grêle sur mésentère commun)", "A", ["volvulus", "occlusion"]), ("Atrésie de l'œsophage", "B", ["atresie"]), ("Hernie diaphragmatique congénitale", "B", ["hernie diaphragmatique"]), ("Traumatisme abdominal de l'enfant (rate, foie)", "B", ["traumatisme abdominal"]), ("Corps étranger ingéré (pile bouton, aimants)", "B", ["corps etranger"]), ("Entérocolite ulcéro-nécrosante (avis chirurgical)", "C", ["enterocolite"]), ("Brûlure étendue de l'enfant", "C", ["brul"])],
 recos=["SFCP / GECI (France) — thèmes de chirurgie pédiatrique", "APSA / EUPSA — recommandations de chirurgie pédiatrique", "SIOP — tumeurs solides de l'enfant (néphroblastome, neuroblastome)", "ATLS / recommandations pédiatriques — traumatisé grave de l'enfant", "OMS — soins chirurgicaux essentiels"],
 pratique="cas de chirurgie pédiatrique (urgence néonatale ou de l'enfant) avec indication, technique et réanimation péri-opératoire")

D["DEMS-CHI-07"] = dict(slug="CHIRURGIE_THORACIQUE", type="chir",
 profil="Chirurgie du poumon, de la plèvre, du médiastin, de la paroi thoracique et de la trachée : cancers thoraciques, kyste hydatique, empyèmes, traumatismes thoraciques.",
 stages=["Chirurgie thoracique", "Pneumologie et endoscopie bronchique", "Réanimation", "Urgences / traumatologie thoracique", "Oncologie thoracique (RCP)", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Anatomie chirurgicale du thorax", "Drainage thoracique et pathologie pleurale", "Traumatismes thoraciques"],
  ["Kyste hydatique du poumon", "Pneumothorax récidivants et bulles", "Empyèmes et séquelles de tuberculose (aspergillome, poumon détruit)", "Exploration fonctionnelle préopératoire"],
  ["Cancer bronchique : bilan, résécabilité, techniques (lobectomie, pneumonectomie)", "Tumeurs du médiastin", "Thoracoscopie vidéo-assistée", "Chirurgie de la paroi thoracique"],
  ["Chirurgie trachéale et sténoses", "Hyperhidrose et chirurgie sympathique", "Transplantation pulmonaire (orientation)"],
  ["Synthèse ; autonomie sur la chirurgie thoracique courante", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Drainage thoracique", 1, 1), ("Thoracotomie : ouverture et fermeture", 1, 3), ("Kystectomie pulmonaire (kyste hydatique)", 2, 3), ("Décortication pleurale", 2, 4), ("Thoracoscopie et talcage", 2, 4), ("Lobectomie", 3, 5), ("Médiastinoscopie", 3, 5)],
 urg=[("Pneumothorax compressif", "A", ["pneumothorax"]), ("Hémothorax massif", "A", ["hemothorax"]), ("Plaie thoracique pénétrante", "A", ["plaie thoracique", "traumatismes thoraciques"]), ("Volet thoracique", "A", ["volet"]), ("Hémoptysie massive (chirurgie d'hémostase)", "B", ["hemoptysie"]), ("Rupture de kyste hydatique pulmonaire", "B", ["kyste hydatique du poumon", "hydatique pulmonaire"]), ("Empyème pleural", "B", ["pleur"]), ("Rupture trachéo-bronchique", "C", ["rupture tracheo"]), ("Fistule broncho-pleurale postopératoire", "C", ["fistule broncho"])],
 recos=["ESTS / ERS — évaluation préopératoire et chirurgie du cancer bronchique", "ESMO / NCCN — cancer bronchique (stratégies multimodales)", "BTS — pathologie pleurale et pneumothorax", "ATLS — traumatismes thoraciques", "OMS — échinococcose kystique (classification et prise en charge)"],
 pratique="dossier de chirurgie thoracique avec imagerie, évaluation fonctionnelle, indication et technique")

D["DEMS-CHI-08"] = dict(slug="CHIRURGIE_UROLOGIQUE", type="chir",
 profil="Chirurgie de l'appareil urinaire et génital masculin : lithiase, tumeurs urologiques, hypertrophie prostatique, urologie fonctionnelle, traumatismes, transplantation rénale, urologie pédiatrique.",
 stages=["Urologie (urgences et hospitalisation)", "Endo-urologie", "Oncologie urologique", "Urologie fonctionnelle et urodynamique", "Transplantation rénale", "Urologie pédiatrique", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Sémiologie urologique, échographie de l'appareil urinaire", "Colique néphrétique et obstruction", "Rétention aiguë d'urine, sondage et cathétérisme sus-pubien"],
  ["Lithiase urinaire : stratégies (urétéroscopie, néphrolithotomie percutanée, lithotritie)", "Hypertrophie bénigne de la prostate", "Infections urinaires masculines et abcès", "Traumatismes de l'appareil urinaire"],
  ["Cancers de la vessie, du rein, de la prostate, du testicule", "Urologie fonctionnelle : incontinence, vessie neurologique", "Andrologie et infertilité masculine"],
  ["Laparoscopie urologique", "Transplantation rénale : prélèvement et greffe", "Uropathies de l'enfant"],
  ["Synthèse ; autonomie sur les interventions courantes", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Sondage difficile et cathétérisme sus-pubien", 1, 1), ("Montée de sonde JJ / néphrostomie (aide)", 1, 2), ("Cystoscopie", 1, 2), ("Résection transurétrale de vessie et de prostate", 2, 4), ("Urétéroscopie", 2, 4), ("Néphrectomie", 3, 5), ("Cystectomie et dérivation urinaire", 4, 9)],
 urg=[("Pyélonéphrite obstructive (drainage en urgence)", "A", ["pyelonephrite"]), ("Rétention aiguë d'urine", "A", ["retention aigue d urine"]), ("Colique néphrétique compliquée", "A", ["colique nephretique"]), ("Torsion du cordon spermatique", "A", ["torsion du testicule", "torsion testiculaire"]), ("Hématurie macroscopique avec caillotage", "B", ["hematurie"]), ("Traumatisme rénal", "B", ["traumatisme renal"]), ("Rupture de l'urètre", "B", ["uretre"]), ("Priapisme", "B", ["priapisme"]), ("Gangrène de Fournier", "C", ["fournier"]), ("Anurie obstructive", "C", ["anurie"])],
 recos=["EAU — guidelines (lithiase, cancers urologiques, infections, traumatismes, incontinence) — mise à jour annuelle", "AFU (France) — recommandations du comité de cancérologie et du comité lithiase", "AUA — mêmes thèmes", "Société algérienne d'urologie — recommandations nationales si disponibles"],
 pratique="dossier urologique avec imagerie, indication et technique opératoire, et gestion d'une complication")

D["DEMS-CHI-09"] = dict(slug="CHIRURGIE_VASCULAIRE", type="chir",
 profil="Chirurgie des artères et des veines hors cœur : artériopathie oblitérante, ischémie aiguë, anévrysmes, chirurgie carotidienne, abords de dialyse, traumatismes vasculaires, maladie veineuse.",
 stages=["Chirurgie vasculaire", "Explorations vasculaires (écho-doppler)", "Radiologie interventionnelle vasculaire", "Réanimation", "Néphrologie (abords de dialyse)", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Anatomie et abords vasculaires", "Examen vasculaire, index de pression systolique", "Ischémie aiguë des membres"],
  ["Artériopathie oblitérante des membres inférieurs", "Écho-doppler artériel et veineux", "Fistules artério-veineuses de dialyse", "Traumatismes vasculaires"],
  ["Anévrysmes de l'aorte abdominale et périphériques", "Sténoses carotidiennes", "Pied diabétique (revascularisation)", "Techniques endovasculaires"],
  ["Ischémie mésentérique", "Maladie veineuse chronique et thrombose", "Infections de prothèses vasculaires"],
  ["Synthèse ; autonomie sur les urgences vasculaires courantes", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Abord et contrôle vasculaire, sutures vasculaires", 1, 2), ("Embolectomie par sonde de Fogarty", 1, 3), ("Création de fistule artério-veineuse", 2, 3), ("Amputation de membre", 1, 3), ("Pontage fémoro-poplité", 3, 5), ("Endartériectomie carotidienne", 4, 9), ("Angioplastie percutanée (aide)", 3, 9)],
 urg=[("Ischémie aiguë de membre", "A", ["ischemie aigue des membres", "ischemie aigue de membre"]), ("Rupture d'anévrysme de l'aorte abdominale", "A", ["anevrysme de l aorte", "anevrysmes de l aorte"]), ("Traumatisme vasculaire des membres", "A", ["traumatisme vasculaire"]), ("Hémorragie sur fistule de dialyse", "B", ["fistule arterio"]), ("Ischémie mésentérique aiguë", "B", ["ischemie mesenterique"]), ("Dissection aortique compliquée de malperfusion", "B", ["dissection aortique"]), ("Phlegmatia caerulea", "C", ["phlegmatia"]), ("Infection de prothèse vasculaire", "C", ["prothese vasculaire"])],
 recos=["ESVS (European Society for Vascular Surgery) — ischémie aiguë, anévrysmes, carotides, abords de dialyse, maladie veineuse", "ESC — maladies artérielles périphériques et aortiques", "SVS (Society for Vascular Surgery) — mêmes thèmes", "Global Vascular Guidelines — ischémie chronique menaçant le membre"],
 pratique="dossier vasculaire avec lecture d'écho-doppler et d'angioscanner, indication et technique")

D["DEMS-CHI-10"] = dict(slug="CHIRURGIE_PLASTIQUE_RECONSTRUCTRICE_ESTHETIQUE_BRULOLOGIE", type="chir",
 profil="Réparation des pertes de substance et des malformations, chirurgie de la main, brûlologie, chirurgie reconstructrice après cancer ou traumatisme, chirurgie esthétique.",
 stages=["Chirurgie plastique et reconstructrice", "Centre des brûlés", "Chirurgie de la main", "Chirurgie maxillo-faciale / ORL (stage court)", "Sénologie reconstructrice", "Dermatologie (tumeurs cutanées)", "Chirurgie générale (socle, 1re année)"],
 annees=[
  SOCLE_CHIR + ["Cicatrisation, greffes de peau, plaies chroniques", "Brûlures : évaluation, réanimation initiale, pansements", "Plaies de la main"],
  ["Lambeaux locaux et régionaux", "Chirurgie de la main (tendons, nerfs, fractures)", "Séquelles de brûlures et cicatrices pathologiques", "Tumeurs cutanées : exérèse et reconstruction"],
  ["Microchirurgie et lambeaux libres", "Fentes labio-palatines et malformations", "Reconstruction mammaire", "Escarres et pertes de substance complexes"],
  ["Chirurgie esthétique : indications, éthique, complications", "Chirurgie de la face", "Chirurgie des membres (reconstruction après traumatisme)"],
  ["Synthèse ; autonomie sur les interventions courantes", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Parage et suture des plaies complexes", 1, 1), ("Greffe de peau mince et totale", 1, 2), ("Excision-greffe du brûlé", 1, 3), ("Escarrotomie", 1, 2), ("Réparation tendineuse de la main", 2, 3), ("Lambeaux locaux", 2, 4), ("Suture microchirurgicale", 3, 5)],
 urg=[("Brûlé grave : réanimation initiale", "A", ["brul"]), ("Brûlures circulaires et escarrotomie", "A", ["brul"]), ("Brûlures par inhalation, électriques, chimiques", "A", ["brul"]), ("Plaie de la main (tendons, nerfs, vaisseaux)", "A", ["plaies de la main"]), ("Amputation traumatique de doigt (réimplantation)", "B", ["amputation"]), ("Morsures de la face et des mains", "B", ["morsures"]), ("Dermohypodermite nécrosante", "B", ["fasciite", "dermohypodermite"]), ("Souffrance de lambeau", "C", ["lambeau"]), ("Phlegmon des gaines de la main", "C", ["phlegmon"])],
 recos=["Arrêté 1400 du 21/11/2024 (programme du DEMS) — annexe non acquise", "ISBI (International Society for Burn Injuries) — prise en charge des brûlures", "ABA (American Burn Association) — critères de transfert et réanimation", "SFETB (France) — brûlologie", "BAPRAS / BSSH — chirurgie de la main et fractures ouvertes"],
 pratique="cas de brûlé ou de reconstruction avec planification chirurgicale argumentée")

D["DEMS-CHI-11"] = dict(slug="CHIRURGIE_VISCERALE_ET_DIGESTIVE", type="chir",
 profil="Chirurgie de l'appareil digestif et de la paroi : chirurgie œso-gastrique, hépato-bilio-pancréatique, colorectale, proctologique, cancérologie digestive, urgences abdominales.",
 stages=["Urgences chirurgicales viscérales", "Chirurgie œso-gastrique", "Chirurgie hépato-bilio-pancréatique", "Chirurgie colorectale et proctologie", "Réanimation chirurgicale", "Endoscopie digestive (observation)", "Oncologie digestive (RCP)"],
 annees=[
  SOCLE_CHIR + ["Abdomen aigu : appendicite, occlusions, péritonites, hernies étranglées", "Réanimation et nutrition du patient chirurgical", "Complications postopératoires"],
  ["Lithiase biliaire et complications", "Hernies et éventrations, cœliochirurgie de base", "Traumatismes abdominaux", "Kyste hydatique du foie", "Proctologie chirurgicale"],
  ["Cancers de l'œsophage et de l'estomac", "Cancers colorectaux et chirurgie rectale", "Pancréatite aiguë et ses complications chirurgicales", "Chirurgie des voies biliaires (sténoses, kystes)"],
  ["Chirurgie hépatique et pancréatique (résections)", "Chirurgie bariatrique (orientation)", "Réhabilitation améliorée après chirurgie", "Chirurgie des métastases hépatiques"],
  ["Synthèse ; autonomie opératoire sur la chirurgie digestive courante", "Organisation de la garde", "Encadrement et morbi-mortalité"],
 ],
 sf=[("Appendicectomie", 1, 2), ("Laparotomie, stomies, résection-anastomose intestinale", 1, 3), ("Cholécystectomie cœlioscopique", 2, 4), ("Cure de hernie et d'éventration", 1, 3), ("Résection du dôme saillant / périkystectomie (kyste hydatique)", 2, 4), ("Colectomie et résection rectale", 3, 5), ("Gastrectomie", 3, 5), ("Duodénopancréatectomie (aide)", 4, 9)],
 urg=[("Péritonite aiguë généralisée", "A", ["peritonite"]), ("Occlusion intestinale", "A", ["occlusion"]), ("Hernie étranglée", "A", ["hernie"]), ("Traumatisme abdominal", "A", ["traumatisme abdominal"]), ("Hémorragie digestive (indication chirurgicale)", "A", ["hemorragie digestive"]), ("Angiocholite et cholécystite aiguë", "B", ["angiocholite", "cholecystite"]), ("Pancréatite aiguë grave (complications chirurgicales)", "B", ["pancreatite"]), ("Complications du kyste hydatique du foie", "B", ["kyste hydatique"]), ("Ischémie mésentérique aiguë", "B", ["ischemie mesenterique"]), ("Fistule anastomotique et péritonite postopératoire", "C", ["fistule anastomotique"]), ("Perforation œsophagienne", "C", ["perforation oesophagienne"])],
 recos=["Arrêté 1398 du 21/11/2024 (programme du DEMS) — annexe non acquise", "WSES — urgences abdominales", "TNCD / SNFGE (France) — thésaurus de cancérologie digestive", "ESMO / NCCN — cancers digestifs", "ERAS Society — réhabilitation améliorée", "OMS — prévention de l'infection du site opératoire (catalogue)"],
 pratique="dossier de chirurgie digestive (indication, technique, complication) et/ou évaluation gestuelle")
