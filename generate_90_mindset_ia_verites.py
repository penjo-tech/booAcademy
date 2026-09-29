import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def draw_painter_brush_underline(draw_obj, start_x, end_x, y_pos, color=(255, 195, 0, 255), thickness=20, tilt=-5):
    """
    Draws an artistic painter brush stroke underline shifted below text with high color saturation.
    """
    y_start = y_pos + 16
    x1 = start_x - 18
    x2 = end_x + 20
    y1 = y_start
    y2 = y_start + tilt
    
    # Main slanted brush body (Vivid saturated gold)
    points = [
        (x1, y1),
        (x2, y2),
        (x2 + 6, y2 + thickness),
        (x1 - 4, y1 + thickness + 2)
    ]
    draw_obj.polygon(points, fill=color)
    
    # High-saturation electric yellow inner core
    inner_color = (255, 235, 10, 255)
    inner_points = [
        (x1 + 10, y1 + 2),
        (x2 - 12, y2 + 1),
        (x2 - 6, y2 + thickness - 5),
        (x1 + 14, y1 + thickness - 4)
    ]
    draw_obj.polygon(inner_points, fill=inner_color)

    # Painted bristle tips at both ends
    draw_obj.ellipse([x2 + 8, y2 + 1, x2 + 24, y2 + thickness - 2], fill=color)
    draw_obj.ellipse([x2 + 14, y2 + 3, x2 + 28, y2 + thickness - 6], fill=color)
    
    draw_obj.ellipse([x1 - 24, y1 + 2, x1 - 8, y1 + thickness - 1], fill=color)
    draw_obj.ellipse([x1 - 30, y1 + 5, x1 - 16, y1 + thickness - 4], fill=color)

def generate_90_mindset_ia_verites():
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy\3"
    os.makedirs(target_dir, exist_ok=True)

    width, height = 1200, 1200
    
    font_path_reg = "C:/Windows/Fonts/GOTHIC.TTF"
    font_path_bold = "C:/Windows/Fonts/GOTHICB.TTF"

    # Logo light setup
    logo_light_path = r"C:\Users\hp omen\Desktop\PERSONNAL BRANDING\My Logo\logo-light.png"
    logo_light = None
    if os.path.exists(logo_light_path):
        raw_logo = Image.open(logo_light_path).convert("RGBA")
        bbox = raw_logo.getbbox()
        if bbox:
            raw_logo = raw_logo.crop(bbox)
        lw, lh = raw_logo.size
        max_lw, max_lh = 220, 75
        ratio = min(max_lw / lw, max_lh / lh)
        logo_light = raw_logo.resize((int(lw * ratio), int(lh * ratio)), Image.Resampling.LANCZOS)

    # 90 Brutal Truths on IA Learning & Mindset (Items 31 to 120)
    items = [
        # Groupe 1: L'illusion du Prompting & Accumulation d'outils (31 - 45)
        {
            "num": "31",
            "headline": "COLLECTIONNER DES OUTILS IA EST DE LA PROCRASTINATION.",
            "brush_kw": "PROCRASTINATION",
            "subtext": "Tester 50 nouveaux logiciels chaque semaine ne remplacera jamais la création d'un vrai projet."
        },
        {
            "num": "32",
            "headline": "LE PROMPT MAGIQUE N'EXISTE ABSOLUMENT PAS.",
            "brush_kw": "N'EXISTE ABSOLUMENT PAS",
            "subtext": "Ce qui compte, c'est la clarté de tes idées et la précision avec laquelle tu exprimes ton besoin."
        },
        {
            "num": "33",
            "headline": "SANS CULTURE GÉNÉRALE, TES PROMPTS SERONT MÉDIOCRES.",
            "brush_kw": "MÉDIOCRES",
            "subtext": "L'IA ne peut puiser que là où tu la diriges. Si ta culture est pauvre, le résultat sera basique."
        },
        {
            "num": "34",
            "headline": "L'IA PRODUIT DU MOYEN PAR DÉFAUT.",
            "brush_kw": "DU MOYEN PAR DÉFAUT",
            "subtext": "Pour obtenir de l'excellence, tu dois injecter ton expertise et affiner sans relâche."
        },
        {
            "num": "35",
            "headline": "NE CONFONDS PAS VITESSE ET QUALITÉ RÉELLE.",
            "brush_kw": "QUALITÉ RÉELLE",
            "subtext": "Générer du texte en 3 secondes est facile. Créer un impact durable demande toujours de la réflexion."
        },
        {
            "num": "36",
            "headline": "UTILISER L'IA SANS COMPRENDRE LES BASES EST DANGEREUX.",
            "brush_kw": "EST DANGEREUX",
            "subtext": "Si tu ne peux pas vérifier le résultat de l'IA, tu seras victime de ses erreurs sans t'en rendre compte."
        },
        {
            "num": "37",
            "headline": "L'IA N'A AUCUN GOÛT ESTHÉTIQUE NATIVE.",
            "brush_kw": "AUCUN GOÛT",
            "subtext": "C'est la sensibilité et l'œil humain qui transforment un contenu banal en chef-d'œuvre visuel."
        },
        {
            "num": "38",
            "headline": "TROP D'AUTOMATISATION TUE LA RELATION CLIENT.",
            "brush_kw": "TUE LA RELATION",
            "subtext": "Les gens achètent de l'humain et de la confiance. Ne robotise pas ce qui fait ton authenticité."
        },
        {
            "num": "39",
            "headline": "LAFLEMME N'EST PAS UN STRATÉGIE IA.",
            "brush_kw": "STRATÉGIE IA",
            "subtext": "Utiliser l'IA pour tout déléguer sans vérifier détruira ta crédibilité plus vite que l'incompétence."
        },
        {
            "num": "40",
            "headline": "UN MAUVAIS DESIGNER AVEC L'IA RESTE MÉDIOCRE.",
            "brush_kw": "RESTE MÉDIOCRE",
            "subtext": "L'outil accélère tes compétences existantes, mais il ne comble pas l'absence totale de talent."
        },
        {
            "num": "41",
            "headline": "SAUTER SUR TOUTES LES NOUVEAUTÉS T'ÉPUISE.",
            "brush_kw": "T'ÉPUISE",
            "subtext": "Maîtrise parfaitement 2 ou 3 outils fondamentaux au lieu d'en effleurer 20 sans profondeur."
        },
        {
            "num": "42",
            "headline": "L'IA EST UN MIROIR DE TA PROPRE RIGUEUR.",
            "brush_kw": "TA PROPRE RIGUEUR",
            "subtext": "Si tes consignes sont vagues, ses réponses seront floues. La précision s'impose de ton côté."
        },
        {
            "num": "43",
            "headline": "LE CONTENU GÉNÉRÉ SANS ÉDITION SE RECONNAÎT CROIS-MOI.",
            "brush_kw": "SE RECONNAÎT",
            "subtext": "Le public repère immédiatement les phrases sans âme. Réécris et réapproprie-toi toujours le texte."
        },
        {
            "num": "44",
            "headline": "TU N'ES PAS UN EXPERT PARCE QUE TU UTILISES CHATGPT.",
            "brush_kw": "PAS UN EXPERT",
            "subtext": "Savoir poser une question à une IA ne fait pas de toi un spécialiste du domaine."
        },
        {
            "num": "45",
            "headline": "LA TECHNIQUE CHANGE MAIS LA LOGIQUE RESTE.",
            "brush_kw": "LA LOGIQUE RESTE",
            "subtext": "Ne t'attache pas à l'interface d'un logiciel. Apprends la méthode sous-jacente pour durer."
        },

        # Groupe 2: Exécution vs Théorie & Apprentissage concret (46 - 60)
        {
            "num": "46",
            "headline": "10 MINUTES DE PRATIQUE VALENT 2 HEURES DE THÉORIE.",
            "brush_kw": "VALENT 2 HEURES",
            "subtext": "Arrête de lire des articles sur l'IA. Ouvre l'outil et résous un problème réel dès maintenant."
        },
        {
            "num": "47",
            "headline": "CONSTRUIS DES PROJETS RÉELS POUR APPRENDRE.",
            "brush_kw": "PROJETS RÉELS",
            "subtext": "C'est en confrontant l'IA à tes vrais besoins professionnels que tu développeras une maîtrise."
        },
        {
            "num": "48",
            "headline": "L'ÉCHEC EN PROMPTING EST UNE INFORMATION PRÉCIEUSE.",
            "brush_kw": "INFORMATION PRÉCIEUSE",
            "subtext": "Quand l'IA répond à côté, comprends pourquoi. C'est ainsi que tu affines ta logique de guidage."
        },
        {
            "num": "49",
            "headline": "APPRENDRE L'IA EST UN MARATHON PAS UN SPRINT.",
            "brush_kw": "UN MARATHON",
            "subtext": "La régularité quotidienne surpasse les sessions intensives d'un week-end suivies de rien."
        },
        {
            "num": "50",
            "headline": "LA CURIOSITÉ EST TA MEILLEURE COMPÉTENCE TECHNIQUE.",
            "brush_kw": "CURIOSITÉ",
            "subtext": "Ceux qui testent sans peur et posent des questions atypiques apprennent 10 fois plus vite."
        },
        {
            "num": "51",
            "headline": "NE CHERCHE PAS À TOUT COMPRENDRE D'UN COUP.",
            "brush_kw": "TOUT COMPRENDRE",
            "subtext": "Avance par étapes successives. Résous une difficulté après l'autre pour bâtir ton niveau."
        },
        {
            "num": "52",
            "headline": "LE MEILLEUR APPRENTISSAGE EST CELUI QUI FAIT MAL.",
            "brush_kw": "FAIT MAL",
            "subtext": "Sortir de sa zone de confort technique est la seule preuve que tu es en train de progresser."
        },
        {
            "num": "53",
            "headline": "DOCUMENTER TES MEILLEURS PROMPTS EST VITAL.",
            "brush_kw": "EST VITAL",
            "subtext": "Crée ta propre bibliothèque d'instructions validées pour ne pas réinventer la roue chaque jour."
        },
        {
            "num": "54",
            "headline": "PARTAGE TES DÉCOUVERTES POUR MIEUX LES FIXER.",
            "brush_kw": "PARTAGE TES DÉCOUVERTES",
            "subtext": "Expliquer ce que tu as appris sur l'IA à un tiers est le meilleur moyen de valider tes acquis."
        },
        {
            "num": "55",
            "headline": "L'EXPÉRIMENTATION EST LE SEUL DIPLÔME QUI COMPTE.",
            "brush_kw": "SEUL DIPLÔME",
            "subtext": "Les certifications théoriques s'effacent devant celui qui sait résoudre un cas concret immédiatement."
        },
        {
            "num": "56",
            "headline": "SI TU NE PRATIQUES PAS CETTE SEMAINE TU OUBLIERAS.",
            "brush_kw": "TU OUBLIERAS",
            "subtext": "L'apprentissage des réflexes IA est volatile. Seule l'action répétée transforme l'essai."
        },
        {
            "num": "57",
            "headline": "DÉMANTÈLE TES ANCIENNES ROUTINES DE TRAVAIL.",
            "brush_kw": "ANCIENNES ROUTINES",
            "subtext": "Revois entièrement ta façon d'organiser tes tâches pour y intégrer intelligemment l'IA."
        },
        {
            "num": "58",
            "headline": "LAVRAIE PUISSANCE RESIDE DANS LES WORKFLOWS.",
            "brush_kw": "LES WORKFLOWS",
            "subtext": "Connecter plusieurs outils IA entre eux vaut bien plus qu'utiliser un seul modèle de façon isolée."
        },
        {
            "num": "59",
            "headline": "NE SOIS PAS UN SIMPLE SPECTATEUR DU PROGRÈS.",
            "brush_kw": "SIMPLE SPECTATEUR",
            "subtext": "Regarder les autres innover ne t'apportera rien. Mets les mains dans le cambouis."
        },
        {
            "num": "60",
            "headline": "L'IA REQUIS UNE DISCIPLINE DE FER AU QUOTIDIEN.",
            "brush_kw": "DISCIPLINE DE FER",
            "subtext": "Consacre 20 minutes chaque matin à tester une idée. Les résultats cumulés seront gigantesques."
        },

        # Groupe 3: Mindset, Discipline & Habitudes (61 - 75)
        {
            "num": "61",
            "headline": "CHANGER DE MINDSET PREND DU TEMPS SOIS PATIENT.",
            "brush_kw": "SOIS PATIENT",
            "subtext": "Accepte de te sentir malhabile au début. C'est le passage obligé vers la maîtrise future."
        },
        {
            "num": "62",
            "headline": "NE CONFONDS PAS IA ET MAGIE SANS EFFORT.",
            "brush_kw": "MAGIE SANS EFFORT",
            "subtext": "L'IA est un levier mécanique. Sans l'énergie et l'orientation humaine, le levier ne bouge pas."
        },
        {
            "num": "63",
            "headline": "LA RÉSISTANCE AU CHANGEMENT EST TON PIRE ENNEMI.",
            "brush_kw": "TA PIRE ENNEMI",
            "subtext": "Dire 'on a toujours fait comme ça' est le meilleur moyen de devenir obsolète en 2 ans."
        },
        {
            "num": "64",
            "headline": "DEVELOPPE UNE MENTALITÉ D'ÉTERNEL DÉBUTANT.",
            "brush_kw": "ÉTERNEL DÉBUTANT",
            "subtext": "Face aux mutations de l'IA, garder un esprit ouvert et humble garantit ta capacité à pivoter."
        },
        {
            "num": "65",
            "headline": "L'IA NE RASSASIERA JAMAIS UN ESPRIT SANS VISION.",
            "brush_kw": "SANS VISION",
            "subtext": "Si tu ne sais pas où tu vas, aucun algorithme ne saura te tracer une trajectoire gagnante."
        },
        {
            "num": "66",
            "headline": "SOIS UN CRÉATEUR PAS UN SIMPLE CONSOMMATEUR.",
            "brush_kw": "UN CRÉATEUR",
            "subtext": "Utilise l'IA pour bâtir des solutions, pas seulement pour consommer des résumés confortables."
        },
        {
            "num": "67",
            "headline": "TON ATTITUDE DÉCIDE DE TON SUCCÈS AVEC L'IA.",
            "brush_kw": "TON ATTITUDE",
            "subtext": "Ceux qui voient l'IA comme une opportunité écrasent ceux qui la perçoivent comme une menace."
        },
        {
            "num": "68",
            "headline": "LA PERSEVÉRANCE BATTRA TOUJOURS LE TALENT BRUT.",
            "brush_kw": "LA PERSEVÉRANCE",
            "subtext": "Tester 100 fois pour trouver le bon calibrage exige un mental d'acier que peu possèdent."
        },
        {
            "num": "69",
            "headline": "NE LAISSE PAS LAPASSEMENT TECHNIQUE T'EFFRAYER.",
            "brush_kw": "T'EFFRAYER",
            "subtext": "Nul besoin de comprendre le code profond pour tirer une valeur immense de ces technologies."
        },
        {
            "num": "70",
            "headline": "L'HUMILITÉ INTELLECTUELLE EST OBLIGATOIRE EN IA.",
            "brush_kw": "OBLIGATOIRE",
            "subtext": "Ce qui marchait hier peut être dépassé aujourd'hui. Sois prêt à réapprendre sans cesse."
        },
        {
            "num": "71",
            "headline": "CONCENTRATION MAXIMALE SUR LA VALEUR CRÉÉE.",
            "brush_kw": "VALEUR CRÉÉE",
            "subtext": "Peu importe l'outil utilisé, seule compte l'utilité réelle du résultat pour tes utilisateurs."
        },
        {
            "num": "72",
            "headline": "APPRENDRE L'IA EXIGE D'ÉTEINDRE LES DISTRACTIONS.",
            "brush_kw": "ÉTEINDRE LES DISTRACTIONS",
            "subtext": "Isole-toi et bloque des plages de travail profond pour maîtriser les cas complexes."
        },
        {
            "num": "73",
            "headline": "NE CHERCHE PAS L'APPROBATION DES SCEPTIQUES.",
            "brush_kw": "DES SCEPTIQUES",
            "subtext": "Pendant qu'ils débattent de la fin du monde, construis et prends une avance irratrapable."
        },
        {
            "num": "74",
            "headline": "TON NIVEAU D'EXIGENCE DÉTERMINE LE RENDU.",
            "brush_kw": "NIVEAU D'EXIGENCE",
            "subtext": "Si tu te contentes du premier jet de l'IA, ton travail paraîtra ordinaire et sans relief."
        },
        {
            "num": "75",
            "headline": "LAFLEXIBILITÉ MENTALE EST LE SURPOUVOIR DU SIÈCLE.",
            "brush_kw": "SURPOUVOIR",
            "subtext": "Savoir pivoter en quelques jours face aux nouveaux modèles est la clé absolue de survie."
        },

        # Groupe 4: Pensée Critique, Qualité & Valeur Humaine (76 - 90)
        {
            "num": "76",
            "headline": "LA RIGUEUR DE VÉRIFICATION SEPARE LES PROS.",
            "brush_kw": "SEPARE LES PROS",
            "subtext": "L'IA hallucine parfois avec aplomb. Verifier chaque donnée est ton obligation professionnelle."
        },
        {
            "num": "77",
            "headline": "L'ESPRIT CRITIQUE EST LE SEUL REMPART CONTRE L'IA.",
            "brush_kw": "SEUL REMPART",
            "subtext": "Ne prends jamais une affirmation d'IA pour parole d'évangile. Questionne et valide toujours."
        },
        {
            "num": "78",
            "headline": "INJECTE TON VÉCU DANS CHAQUE CONTENU IA.",
            "brush_kw": "TON VÉCU",
            "subtext": "Tes anecdotes personnelles et tes échecs passés sont ce que l'IA ne pourra jamais simuler."
        },
        {
            "num": "79",
            "headline": "L'IA NE RESSENT NI ÉMOTION NI EMPATHIE.",
            "brush_kw": "NI ÉMOTION",
            "subtext": "Comprendre les peines et les désirs profonds de tes clients reste ton rôle exclusif."
        },
        {
            "num": "80",
            "headline": "LE CONTEXTE EST ROI DANS L'APPRENTISSAGE IA.",
            "brush_kw": "EST ROI",
            "subtext": "Plus tu fournis un cadre précis et documenté, plus les résultats de l'IA deviennent brillants."
        },
        {
            "num": "81",
            "headline": "SANS STRATÉGIE IA N'EST QU'UN GADGET AMUSANT.",
            "brush_kw": "GADGET AMUSANT",
            "subtext": "Aligner l'IA sur des objectifs business clairs transforme une curiosité en machine à produire."
        },
        {
            "num": "82",
            "headline": "SACHE DIRE NON AUX PROPOSITIONS FADE DE L'IA.",
            "brush_kw": "SAYE DIRE NON",
            "subtext": "Rejeter les suggestions sans relief et imposer ton style est la marque des vrais créateurs."
        },
        {
            "num": "83",
            "headline": "L'ORIGINALITÉ VIENT DE TES ASSOCIATIONS D'IDÉES.",
            "brush_kw": "ASSOCIATIONS D'IDÉES",
            "subtext": "Croiser deux domaines distants grâce à l'IA génère les innovations les plus marquantes."
        },
        {
            "num": "84",
            "headline": "L'ÉTHIQUE DANS L'UTILISATION IA EST INDISPENSABLE.",
            "brush_kw": "INDISPENSABLE",
            "subtext": "Garde une transparence totale sur tes processus pour construire une relation de confiance."
        },
        {
            "num": "85",
            "headline": "LAQUALITÉ BATTE TOUJOURS LA QUANTITÉ ENCOMBRANTE.",
            "brush_kw": "BATTE TOUJOURS",
            "subtext": "Publier un contenu mémorable retravaillé vaut mieux que 10 articles génériques générés au kilomètre."
        },
        {
            "num": "86",
            "headline": "L'IA NE REMPLACERA JAMAIS TARESPONSABILITÉ.",
            "brush_kw": "RESPONSABILITÉ",
            "subtext": "En cas d'erreur ou d'échec, c'est ton nom qui est engagé, pas celui de l'algorithme."
        },
        {
            "num": "87",
            "headline": "LAFUSION HUMAIN ET IA EST LA FORMULE GAGNANTE.",
            "brush_kw": "FORMULE GAGNANTE",
            "subtext": "Combine la vitesse de la machine avec la sensibilité humaine pour obtenir un résultat imbattable."
        },
        {
            "num": "88",
            "headline": "NE DEVIENS PAS ESCLAVE DE TES PROPRES AUTOMATISMES.",
            "brush_kw": "PAS ESCLAVE",
            "subtext": "Garde du temps pour réfléchir à main levée, sans écran ni sollicitation d'algorithme."
        },
        {
            "num": "89",
            "headline": "L'ART DU QUESTIONNEMENT EST TON PLUS GRAND ATOUT.",
            "brush_kw": "PLUS GRAND ATOUT",
            "subtext": "Celui qui sait poser la meilleure question obtient toujours la réponse la plus puissante."
        },
        {
            "num": "90",
            "headline": "TA PERSONNALITÉ EST LE FILTRE D'EXCELLENCE.",
            "brush_kw": "FILTRE D'EXCELLENCE",
            "subtext": "C'est ta voix unique, ton humour et ton ton qui rendent une production IA captivante."
        },

        # Groupe 5: Peur du Changement, Dépassement & Compétitivité (91 - 105)
        {
            "num": "91",
            "headline": "IGNORER L'IA AUJOURD'HUI EST UN SUICIDE PRO.",
            "brush_kw": "SUICIDE PRO",
            "subtext": "Fermer les yeux sur cette révolution ne l'empêchera pas de transformer ton marché."
        },
        {
            "num": "92",
            "headline": "LA PEUR N'A JAMAIS ARRÊTÉ LE PROGRÈS TECHNIQUE.",
            "brush_kw": "ARRÊTÉ LE PROGRÈS",
            "subtext": "Transforme ton inquiétude en énergie d'apprentissage pour prendre le contrôle immédiatement."
        },
        {
            "num": "93",
            "headline": "LE MARCHÉ NE PARDONNE PAS LA LENTEUR D'ADAPTATION.",
            "brush_kw": "LENTEUR D'ADAPTATION",
            "subtext": "Ceux qui adoptent l'IA réduisent leurs coûts et délais pendant que tu hésites encore."
        },
        {
            "num": "94",
            "headline": "TES CONCURRENTS UTILISENT DÉJÀ L'IA EN SECRET.",
            "brush_kw": "UTILISENT DÉJÀ",
            "subtext": "Ne crois pas qu'ils dorment. Ils optimisent leurs offres pendant que tu te poses des questions."
        },
        {
            "num": "95",
            "headline": "APPRENDRE L'IA SEULEMENT QUAND IL LE FAUDRA EST TROP TARD.",
            "brush_kw": "EST TROP TARD",
            "subtext": "L'anticipation est le seul moyen de garder une position de force sur son marché."
        },
        {
            "num": "96",
            "headline": "TU N'AS PAS BESOIN D'UN DIPLÔME POUR RÉUSSIR EN IA.",
            "brush_kw": "PAS BESOIN",
            "subtext": "Le domaine est si jeune que la valeur se mesure uniquement aux résultats concrets produits."
        },
        {
            "num": "97",
            "headline": "L'ÂGE N'EST PAS UNE EXCUSE POUR NE PAS T'Y METTRE.",
            "brush_kw": "PAS UNE EXCUSE",
            "subtext": "L'interface est en langage naturel. Si tu sais écrire et réfléchir, tu peux réussir."
        },
        {
            "num": "98",
            "headline": "SOIS PRÊT À DÉSAPPRENDRE CE QUE TU SAIS DEPUIS 10 ANS.",
            "brush_kw": "DÉSAPPRENDRE",
            "subtext": "La valeur n'est plus dans l'exécution manuelle mais dans la capacité à orchestrer."
        },
        {
            "num": "99",
            "headline": "L'IA REVALORISE LES ESPRITSSYNTHÉTIQUES ET CLAIRS.",
            "brush_kw": "ESPRITS SYNTHÉTIQUES",
            "subtext": "Savoir structurer une pensée complexe devient la compétence reine dans un monde d'IA."
        },
        {
            "num": "100",
            "headline": "LE STATU QUO EST LE PLUS GRAND DANGER DE TA CARRIÈRE.",
            "brush_kw": "PLUS GRAND DANGER",
            "subtext": "Rester immobile en période de rupture technologique équivaut à reculer à grande vitesse."
        },
        {
            "num": "101",
            "headline": "N'AIE PAS PEUR DE REMPLACER TES PROPRES MÉTHODES.",
            "brush_kw": "TES PROPRES MÉTHODES",
            "subtext": "Auto-disrupte tes processus avant qu'un concurrent ne vienne le faire à ta place."
        },
        {
            "num": "102",
            "headline": "L'IA OFFRIRA DES OPPORTUNITÉS INÉDITES AUX AUDACIEUX.",
            "brush_kw": "AUX AUDACIEUX",
            "subtext": "Ceux qui osent tester des formats nouveaux créeront les standards de demain."
        },
        {
            "num": "103",
            "headline": "TRAVAILLE PLUS INTELLIGEMMENT PAS SEULEMENT PLUS DUR.",
            "brush_kw": "PLUS INTELLIGEMMENT",
            "subtext": "L'IA te permet de démultiplier ton impact sans augmenter tes heures de travail."
        },
        {
            "num": "104",
            "headline": "TON EXPERTISE MÉTIER EST TA MEILLEURE ARME.",
            "brush_kw": "MEILLEURE ARME",
            "subtext": "Combinée à l'IA, ta connaissance intime de ton domaine te rendra imbattable."
        },
        {
            "num": "105",
            "headline": "ARRÊTE DE RÊVER ET COMMENCE À PROMPTER ET CRÉER.",
            "brush_kw": "COMMENCE À PROMPTER",
            "subtext": "Les idées ne valent rien. Seule l'exécution assistée par IA crée une différence mesurable."
        },

        # Groupe 6: Vision Long Terme & Maîtrise Ultime (106 - 120)
        {
            "num": "106",
            "headline": "DANS 3 ANS L'IA SERA AUSSI BANALE QUE L'ELECTRICITÉ.",
            "brush_kw": "AUSSI BANALE",
            "subtext": "Ne perds pas de temps à t'émerveiller. Intègre-la d'ores et déjà comme un outil standard."
        },
        {
            "num": "107",
            "headline": "L'AUTONOMIE EN APPRENTISSAGE EST TON MEILLEUR ATOUT.",
            "brush_kw": "MEILLEUR ATOUT",
            "subtext": "N'attends pas qu'on te forme. Cherche, teste, échoue et apprends par toi-même tous les jours."
        },
        {
            "num": "108",
            "headline": "DEVAGUES DE NOUVEAUX OUTILS ARRIVERONT SANS CESSE.",
            "brush_kw": "ARRIVERONT SANS CESSE",
            "subtext": "Ne cherche pas la stabilité. Développe ton agilité pour t'adapter à chaque nouvelle vague."
        },
        {
            "num": "109",
            "headline": "LA SIMPLICITÉ DES RÉSULTATS CACHE UN GRAND EFFORT.",
            "brush_kw": "GRAND EFFORT",
            "subtext": "Derrière un contenu fluide produit avec l'IA se trouvent des heures de calibrage rigoureux."
        },
        {
            "num": "110",
            "headline": "L'IA REVOLUTIONNE L'APPRENTISSAGE SUR MESURE.",
            "brush_kw": "APPRENTISSAGE SUR MESURE",
            "subtext": "Tu as désormais le meilleur tuteur mondial disponible 24/7 dans ta poche. Utilise-le !"
        },
        {
            "num": "111",
            "headline": "EXIGE L'EXCELLENCE DE TES INTERACTIONS IA.",
            "brush_kw": "EXIGE L'EXCELLENCE",
            "subtext": "Ne te contente jamais d'un résultat moyen. Repousse les limites de l'outil à chaque fois."
        },
        {
            "num": "112",
            "headline": "LE VRAI LEADERSHIP EN IA EST D'INSPIRER LES AUTRES.",
            "brush_kw": "INSPIRER LES AUTRES",
            "subtext": "Montre la voie, partage tes cas d'usage et aide ton entourage à monter en compétences."
        },
        {
            "num": "113",
            "headline": "L'APPRENTISSAGE CONTINU N'EST PLUS UNE OPTION.",
            "brush_kw": "PLUS UNE OPTION",
            "subtext": "Dans le monde de l'IA, arrêter d'apprendre pendant 6 mois équivaut à perdre 5 ans."
        },
        {
            "num": "114",
            "headline": "FAIS DE L'IA TON ASSISTANT PAS TON REMPLAÇANT.",
            "brush_kw": "TON ASSISTANT",
            "subtext": "Garde les commandes stratégiques et laisse la machine gérer la charge de travail brute."
        },
        {
            "num": "115",
            "headline": "LA CLARTÉ STRATÉGIQUE EST LA CLÉ DU SUCCÈS.",
            "brush_kw": "CLÉ DU SUCCÈS",
            "subtext": "Savoir exactement ce que tu cherches à accomplir rend l'utilisation de l'IA redoutable."
        },
        {
            "num": "116",
            "headline": "NE CRAINS PAS L'AVENIR CRÉE-LE AVEC L'IA.",
            "brush_kw": "CRÉE-LE AVEC L'IA",
            "subtext": "Prends les devants et façonne le futur de ton activité en intégrant l'IA dès aujourd'hui."
        },
        {
            "num": "117",
            "headline": "L'AUDACE DE TESTER FAIT TOUTE LA DIFFÉRENCE.",
            "brush_kw": "AUDACE DE TESTER",
            "subtext": "Les meilleures méthodes IA sont découvertes par ceux qui sortent des sentiers battus."
        },
        {
            "num": "118",
            "headline": "TON SYSTEME DE PENSÉE EST TON SEUL PLAFOND.",
            "brush_kw": "SEUL PLAFOND",
            "subtext": "L'IA n'a pas de limites de puissance. Seule ta propre imagination restreint le résultat."
        },
        {
            "num": "119",
            "headline": "CONSTRUIS UNEAVANTAGE INCOMPARABLE AVEC L'IA.",
            "brush_kw": "AVANTAGE INCOMPARABLE",
            "subtext": "Combines tes forces uniques avec la vitesse IA pour bâtir une barrière à la concurrence."
        },
        {
            "num": "120",
            "headline": "L'AVENIR APPARTIENT À CEUX QUI AGISSENT MAINTENANT.",
            "brush_kw": "AGISSENT MAINTENANT",
            "subtext": "Le meilleur moment pour maîtriser l'IA était il y a un an. Le deuxième meilleur moment est aujourd'hui."
        }
    ]

    font_size_head = 64
    font_head = ImageFont.truetype(font_path_bold, font_size_head)
    font_sub = ImageFont.truetype(font_path_reg, 40)

    count = 0
    for item in items:
        img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
        draw = ImageDraw.Draw(img)

        headline = item["headline"]
        brush_kw = item["brush_kw"]
        subtext = item["subtext"]

        lines_head = textwrap.wrap(headline, width=19)
        lines_sub = textwrap.wrap(subtext, width=27)

        lh_head = int(font_size_head * 1.32)
        lh_sub = int(40 * 1.35)

        h_head = len(lines_head) * lh_head
        h_sub = len(lines_sub) * lh_sub
        spacing = 50

        total_h = h_head + spacing + h_sub
        start_y = 580 - (total_h // 2)

        # Render Headline + Painter Brush stroke under keyword
        curr_y = start_y
        for l in lines_head:
            bbox = font_head.getbbox(l)
            w_l = bbox[2] - bbox[0]
            start_x_l = (width - w_l) // 2
            
            if brush_kw in l:
                idx = l.index(brush_kw)
                prefix = l[:idx]
                prefix_w = font_head.getbbox(prefix)[2] - font_head.getbbox(prefix)[0] if prefix else 0
                kw_w = font_head.getbbox(brush_kw)[2] - font_head.getbbox(brush_kw)[0]
                
                kw_start_x = start_x_l + prefix_w
                kw_end_x = kw_start_x + kw_w
                
                draw_painter_brush_underline(draw, kw_start_x, kw_end_x, curr_y + font_size_head + 2, color=(255, 195, 0, 255), thickness=20, tilt=-5)

            draw.text((start_x_l, curr_y), l, fill=(255, 255, 255, 255), font=font_head)
            curr_y += lh_head

        curr_y += spacing

        # Render Subtext
        for l in lines_sub:
            bbox = font_sub.getbbox(l)
            w_l = bbox[2] - bbox[0]
            draw.text(((width - w_l) // 2, curr_y), l, fill=(215, 215, 215, 255), font=font_sub)
            curr_y += lh_sub

        # Logo in Bottom Right Footer
        if logo_light:
            lw_l, lh_l = logo_light.size
            img.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

        out_name = f"motivation_ia_verite_{item['num']}.png"
        out_path = os.path.join(target_dir, out_name)
        img.save(out_path, "PNG")
        count += 1
        if count % 10 == 0:
            print(f"Generated {count}/90 images... (latest: {out_name})")

    print(f"DONE! Successfully generated all {count} images in {target_dir}")

if __name__ == "__main__":
    generate_90_mindset_ia_verites()
