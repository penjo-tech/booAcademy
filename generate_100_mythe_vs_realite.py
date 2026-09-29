import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def draw_painter_brush_underline(draw_obj, start_x, end_x, y_pos, color=(255, 195, 0, 255), thickness=18, tilt=-5):
    """
    Draws an artistic painter brush stroke underline shifted below text with high color saturation.
    """
    y_start = y_pos + 14
    x1 = start_x - 16
    x2 = end_x + 18
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
    draw_obj.ellipse([x2 + 8, y2 + 1, x2 + 22, y2 + thickness - 2], fill=color)
    draw_obj.ellipse([x2 + 14, y2 + 3, x2 + 26, y2 + thickness - 6], fill=color)
    
    draw_obj.ellipse([x1 - 22, y1 + 2, x1 - 8, y1 + thickness - 1], fill=color)
    draw_obj.ellipse([x1 - 28, y1 + 5, x1 - 16, y1 + thickness - 4], fill=color)

def generate_100_mythe_vs_realite():
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy\5"
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

    # 100 MYTHE vs RÉALITÉ Contents
    items = [
        # 1-20: Intelligence Artificielle & Outils
        {
            "num": "01",
            "mythe": "MYTHE : L'IA sait tout et ne se trompe jamais.",
            "brush_kw": "NE SE TROMPE JAMAIS",
            "realite": "RÉALITÉ : L'IA prédit des mots probables, pas la vérité. Sans vérification humaine, les hallucinations sont inévitables."
        },
        {
            "num": "02",
            "mythe": "MYTHE : Il faut être ingénieur pour utiliser l'IA.",
            "brush_kw": "ÊTRE INGÉNIEUR",
            "realite": "RÉALITÉ : La vraie compétence clé est la clarté d'esprit, la logique et la capacité à poser les bonnes questions."
        },
        {
            "num": "03",
            "mythe": "MYTHE : ChatGPT va remplacer tous les rédacteurs.",
            "brush_kw": "TOUS LES RÉDACTEURS",
            "realite": "RÉALITÉ : Il remplace la rédaction médiocre. Le style, la sensibilité et l'expérience humaine restent irremplaçables."
        },
        {
            "num": "04",
            "mythe": "MYTHE : Plus le prompt est long, meilleure est la réponse.",
            "brush_kw": "MEILLEURE EST LA RÉPONSE",
            "realite": "RÉALITÉ : La concision et la structure priment sur la longueur. Un prompt flou reste inutile, peu importe sa taille."
        },
        {
            "num": "05",
            "mythe": "MYTHE : L'IA possède une conscience propre.",
            "brush_kw": "CONSCIENCE PROPRE",
            "realite": "RÉALITÉ : C'est un outil statistique ultra-performant. Elle simule la réflexion sans jamais rien comprendre."
        },
        {
            "num": "06",
            "mythe": "MYTHE : Copier du code IA fait de toi un développeur.",
            "brush_kw": "DE TOI UN DÉVELOPPEUR",
            "realite": "RÉALITÉ : Si tu ne comprends pas ce qu'elle génère, tu seras incapable de déboguer au moindre problème."
        },
        {
            "num": "07",
            "mythe": "MYTHE : L'IA crée du contenu parfait au 1er essai.",
            "brush_kw": "PARFAIT AU 1ER ESSAI",
            "realite": "RÉALITÉ : L'IA produit le premier jet. Le travail d'affinage et d'édition humaine fait 80% de la qualité finale."
        },
        {
            "num": "08",
            "mythe": "MYTHE : Utiliser l'IA au travail est de la triche.",
            "brush_kw": "DE LA TRICHE",
            "realite": "RÉALITÉ : C'est comme utiliser une calculatrice en comptabilité. C'est un levier d'efficacité obligatoire."
        },
        {
            "num": "09",
            "mythe": "MYTHE : Les LLM comprennent le sens de tes phrases.",
            "brush_kw": "COMPRENNENT LE SENS",
            "realite": "RÉALITÉ : Ils manipulent des représentations mathématiques et des vecteurs, pas des concepts philosophiques."
        },
        {
            "num": "10",
            "mythe": "MYTHE : L'IA est réservée aux géants de la Tech.",
            "brush_kw": "GÉANTS DE LA TECH",
            "realite": "RÉALITÉ : Aujourd'hui, un indépendant ou une PME peut automatiser ses tâches avec des outils très accessibles."
        },
        {
            "num": "11",
            "mythe": "MYTHE : L'IA va supprimer tous les emplois.",
            "brush_kw": "SUPPRIMER TOUS LES EMPLOIS",
            "realite": "RÉALITÉ : Elle va redéfinir les rôles. Ceux qui maîtrisent l'IA remplaceront ceux qui refusent d'évoluer."
        },
        {
            "num": "12",
            "mythe": "MYTHE : Midjourney va tuer tous les designers.",
            "brush_kw": "TUER TOUS LES DESIGNERS",
            "realite": "RÉALITÉ : Il tue l'exécution lente. La direction artistique, la cohérence de marque et le goût restent humains."
        },
        {
            "num": "13",
            "mythe": "MYTHE : ChatGPT résout les bugs de structure.",
            "brush_kw": "BUGS DE STRUCTURE",
            "realite": "RÉALITÉ : Sans données structurées et sans stratégie claire, l'IA ne fait qu'accélérer le désordre existant."
        },
        {
            "num": "14",
            "mythe": "MYTHE : Le prompt magique enrichit instantanément.",
            "brush_kw": "ENRICHIT INSTANTANÉMENT",
            "realite": "RÉALITÉ : C'est une illusion marketing. La vraie valeur réside dans la résolution de vrais problèmes business."
        },
        {
            "num": "15",
            "mythe": "MYTHE : L'IA rend le cerveau humain paresseux.",
            "brush_kw": "CERVEAU HUMAIN PARESSEUX",
            "realite": "RÉALITÉ : Elle libère du temps de cerveau disponible en éliminant les tâches réitératives et chronophages."
        },
        {
            "num": "16",
            "mythe": "MYTHE : Les réponses de l'IA sont 100% neutres.",
            "brush_kw": "100% NEUTRES",
            "realite": "RÉALITÉ : L'IA reflète les biais, préjugés et tendances présents dans ses données d'entraînement."
        },
        {
            "num": "17",
            "mythe": "MYTHE : L'IA remplace une vraie stratégie marketing.",
            "brush_kw": "STRATÉGIE MARKETING",
            "realite": "RÉALITÉ : Elle génère des idées et du contenu, mais la vision globale et la connaissance client restent humaines."
        },
        {
            "num": "18",
            "mythe": "MYTHE : Plus besoin d'apprendre les langues.",
            "brush_kw": "D'APPRENDRE LES LANGUES",
            "realite": "RÉALITÉ : La traduction automatique aide à dépanner, mais la relation et l'immersion culturelle exigent une vraie maîtrise."
        },
        {
            "num": "19",
            "mythe": "MYTHE : L'IA automatise tout en un jour.",
            "brush_kw": "AUTOMATISE TOUT EN UN JOUR",
            "realite": "RÉALITÉ : L'automatisation se fait processus par processus, avec des ajustements et des contrôles constants."
        },
        {
            "num": "20",
            "mythe": "MYTHE : Tester l'IA 10 minutes suffit à juger.",
            "brush_kw": "SUFFIT À JUGER",
            "realite": "RÉALITÉ : L'écosystème évolue chaque semaine. L'apprentissage est une pratique continue et expérimentale."
        },

        # 21-40: Productivité & Organisation
        {
            "num": "21",
            "mythe": "MYTHE : Travailler 12h garantit le succès.",
            "brush_kw": "GARANTIT LE SUCCÈS",
            "realite": "RÉALITÉ : La fatigue détruit la clarté. Travailler intelligemment avec de bons systèmes bat la surcharge."
        },
        {
            "num": "22",
            "mythe": "MYTHE : Le multitâche fait gagner du temps.",
            "brush_kw": "FAIT GAGNER DU TEMPS",
            "realite": "RÉALITÉ : Le cerveau ne fait que switcher. Le multitâche réduit la concentration et augmente les erreurs."
        },
        {
            "num": "23",
            "mythe": "MYTHE : Être débordé signifie être productif.",
            "brush_kw": "SIGNIFIE ÊTRE PRODUCTIF",
            "realite": "RÉALITÉ : Brasser du vent et répondre à des mails n'est pas produire de la valeur. Priorise le travail profond."
        },
        {
            "num": "24",
            "mythe": "MYTHE : Une to-do list géante garde le contrôle.",
            "brush_kw": "GARDE LE CONTRÔLE",
            "realite": "RÉALITÉ : Elle crée de l'anxiété. Seules 2 à 3 priorités majeures par jour doivent captiver ton attention."
        },
        {
            "num": "25",
            "mythe": "MYTHE : Travailler sous pression est meilleur.",
            "brush_kw": "EST MEILLEUR",
            "realite": "RÉALITÉ : La pression produit du stress. La préparation et la régularité produisent l'excellence."
        },
        {
            "num": "26",
            "mythe": "MYTHE : La volonté suffit pour être discipliné.",
            "brush_kw": "SUFFIT POUR ÊTRE DISCIPLINÉ",
            "realite": "RÉALITÉ : La volonté s'épuise vite. Seuls les systèmes et les routines solides durent dans le temps."
        },
        {
            "num": "27",
            "mythe": "MYTHE : Une nouvelle app règle tes retards.",
            "brush_kw": "RÈGLE TES RETARDS",
            "realite": "RÉALITÉ : Un mauvais système sur Notion ou Trello reste un mauvais système, juste numérisé."
        },
        {
            "num": "28",
            "mythe": "MYTHE : Les réunions font avancer les projets.",
            "brush_kw": "FONT AVANCER LES PROJETS",
            "realite": "RÉALITÉ : 80% des réunions pourraient être remplacées par une note synthétique ou un message asynchrone."
        },
        {
            "num": "29",
            "mythe": "MYTHE : Se lever à 5h est le secret absolu.",
            "brush_kw": "LE SECRET ABSOLU",
            "realite": "RÉALITÉ : Le secret est la régularité et le respect de son rythme biologique, pas l'heure du réveil."
        },
        {
            "num": "30",
            "mythe": "MYTHE : Dire oui à tout booste la carrière.",
            "brush_kw": "BOOSTE LA CARRIÈRE",
            "realite": "RÉALITÉ : Savoir dire non préserve ton énergie et te permet d'exceller sur ce qui compte vraiment."
        },
        {
            "num": "31",
            "mythe": "MYTHE : Automatiser fait gagner du temps net.",
            "brush_kw": "GAGNER DU TEMPS NET",
            "realite": "RÉALITÉ : Créer l'automatisation prend du temps. Elle ne devient rentable que si la tâche est récurrente."
        },
        {
            "num": "32",
            "mythe": "MYTHE : La perfection est le seul standard.",
            "brush_kw": "LE SEUL STANDARD",
            "realite": "RÉALITÉ : Le perfectionnisme est une forme de procrastination. Fait vaut toujours mieux que parfait."
        },
        {
            "num": "33",
            "mythe": "MYTHE : Travailler vite égale travail bâclé.",
            "brush_kw": "TRAVAIL BÂCLÉ",
            "realite": "RÉALITÉ : La vitesse maîtrisée vient de la clarté et de l'automatisation des gestes répétés."
        },
        {
            "num": "34",
            "mythe": "MYTHE : Vérifier ses mails au réveil avance.",
            "brush_kw": "AU RÉVEIL AVANCE",
            "realite": "RÉALITÉ : Tu commences ta journée en réagissant aux priorités des autres plutôt qu'aux tiennes."
        },
        {
            "num": "35",
            "mythe": "MYTHE : Les pauses font perdre le rythme.",
            "brush_kw": "PERDRE LE RYTHME",
            "realite": "RÉALITÉ : Les pauses stratégiques restaurent l'attention et évitent les erreurs d'inattention coûteuses."
        },
        {
            "num": "36",
            "mythe": "MYTHE : Tout retenir de tête prouve l'esprit.",
            "brush_kw": "PROUVE L'ESPRIT",
            "realite": "RÉALITÉ : Le cerveau est fait pour créer des idées, pas les stocker. Utilise un second cerveau numérique."
        },
        {
            "num": "37",
            "mythe": "MYTHE : Le silence total est indispensable.",
            "brush_kw": "TOTAL EST INDISPENSABLE",
            "realite": "RÉALITÉ : La capacité de focalisation dépend de l'état d'esprit et de la méthode, pas uniquement du décor."
        },
        {
            "num": "38",
            "mythe": "MYTHE : La motivation précède l'action.",
            "brush_kw": "PRÉCÈDE L'ACTION",
            "realite": "RÉALITÉ : C'est l'action qui génère la motivation. Commence 5 minutes et l'élan viendra naturellement."
        },
        {
            "num": "39",
            "mythe": "MYTHE : Un bureau vide rend ultra créatif.",
            "brush_kw": "REND ULTRA CRÉATIF",
            "realite": "RÉALITÉ : L'organisation doit servir le travailleur, pas devenir une obsession rigide qui freine l'action."
        },
        {
            "num": "40",
            "mythe": "MYTHE : Finir épuisé prouve l'effort fourni.",
            "brush_kw": "PROUVE L'EFFORT FORNI",
            "realite": "RÉALITÉ : L'épuisement prouve souvent un manque d'efficience. Une bonne journée laisse de l'énergie."
        },

        # 41-60: Excel & Bureautique
        {
            "num": "41",
            "mythe": "MYTHE : Excel est un outil dépassé.",
            "brush_kw": "UN OUTIL DÉPASSÉ",
            "realite": "RÉALITÉ : Excel reste le moteur invisible des entreprises. Le maîtriser donne un avantage immense."
        },
        {
            "num": "42",
            "mythe": "MYTHE : Le copier-coller manuel est normal.",
            "brush_kw": "MANUEL EST NORMAL",
            "realite": "RÉALITÉ : Power Query et VBA permettent d'automatiser 100% de la collecte et du nettoyage de données."
        },
        {
            "num": "43",
            "mythe": "MYTHE : SOMME et MOYENNE suffisent largement.",
            "brush_kw": "SUFFISENT LARGEMENT",
            "realite": "RÉALITÉ : Les TCD, RECHERCHEX et fonctions logiques font passer ton niveau de débutant à expert."
        },
        {
            "num": "44",
            "mythe": "MYTHE : Plus il y a de couleurs, plus c'est beau.",
            "brush_kw": "PLUS C'EST BEAU",
            "realite": "RÉALITÉ : La surcharge visuelle masque l'information. Un bon tableau est lisible, épuré et structuré."
        },
        {
            "num": "45",
            "mythe": "MYTHE : Nettoyer des données prend des heures.",
            "brush_kw": "PREND DES HEURES",
            "realite": "RÉALITÉ : Formules texte, Power Query et filtres nettoient des milliers de lignes en quelques secondes."
        },
        {
            "num": "46",
            "mythe": "MYTHE : Les macros VBA sont réservées aux devs.",
            "brush_kw": "RÉSERVÉES AUX DEVS",
            "realite": "RÉALITÉ : L'enregistreur de macro et quelques bases simples permettent à quiconque de gagner des heures."
        },
        {
            "num": "47",
            "mythe": "MYTHE : Power BI est réservé aux Data Scientists.",
            "brush_kw": "DATA SCIENTISTS",
            "realite": "RÉALITÉ : C'est un outil accessible pour tout manager voulant transformer ses tableaux Excel en dashboards."
        },
        {
            "num": "48",
            "mythe": "MYTHE : Word sert juste à saisir du texte.",
            "brush_kw": "SAISIR DU TEXTE",
            "realite": "RÉALITÉ : L'utilisation des styles, sommaires et publipostages transforme Word en usine à documents pro."
        },
        {
            "num": "49",
            "mythe": "MYTHE : PowerPoint sert à lire ses diapositives.",
            "brush_kw": "LIRE SES DIAPOSITIVES",
            "realite": "RÉALITÉ : Les slides sont un support visuel. Tu es le présentateur, pas la liseuse de tes puces."
        },
        {
            "num": "50",
            "mythe": "MYTHE : 50 lignes par slide enrichit le propos.",
            "brush_kw": "ENRICHIT LE PROPOS",
            "realite": "RÉALITÉ : Personne ne lit des slides surchargées. Une idée clé par slide capte et retient l'attention."
        },
        {
            "num": "51",
            "mythe": "MYTHE : Le Cloud sert juste de sauvegarde.",
            "brush_kw": "JUSTE DE SAUVEGARDE",
            "realite": "RÉALITÉ : Le Cloud permet la collaboration en temps réel et élimine les fichiers 'final_v2_definitif.xlsx'."
        },
        {
            "num": "52",
            "mythe": "MYTHE : Garder ses fichiers sur le bureau est top.",
            "brush_kw": "SUR LE BUREAU EST TOP",
            "realite": "RÉALITÉ : C'est le meilleur moyen de perdre ses documents et de perdre du temps lors des recherches."
        },
        {
            "num": "53",
            "mythe": "MYTHE : Les raccourcis clavier sont accessoires.",
            "brush_kw": "SONT ACCESSOIRES",
            "realite": "RÉALITÉ : Mis bout à bout, maîtriser les raccourcis fait gagner jusqu'à 100 heures de travail par an."
        },
        {
            "num": "54",
            "mythe": "MYTHE : Les bugs Excel arrivent sans raison.",
            "brush_kw": "ARRIVENT SANS RAISON",
            "realite": "RÉALITÉ : 99% des erreurs viennent d'une mauvaise manipulation ou d'un manque de contrôle des données."
        },
        {
            "num": "55",
            "mythe": "MYTHE : Un graphique complexe fait sérieux.",
            "brush_kw": "COMPLEXE FAIT SÉRIEUX",
            "realite": "RÉALITÉ : La clarté est le comble du chic. Si le graphique demande 5 min d'explications, il est raté."
        },
        {
            "num": "56",
            "mythe": "MYTHE : Utiliser des templates manque de style.",
            "brush_kw": "MANQUE DE STYLE",
            "realite": "RÉALITÉ : Réinventer la roue à chaque doc est du gâchis. Les templates pros assurent vitesse et qualité."
        },
        {
            "num": "57",
            "mythe": "MYTHE : La sécurité IT ne concerne que l'IT.",
            "brush_kw": "NE CONCERNE QUE L'IT",
            "realite": "RÉALITÉ : L'humain est le premier vecteur de faille. La vigilance individuelle est la meilleure protection."
        },
        {
            "num": "58",
            "mythe": "MYTHE : Imprimer est requis pour relire.",
            "brush_kw": "REQUIS POUR RELIRE",
            "realite": "RÉALITÉ : Les outils d'annotation numérique et de suivi de modification sont plus rapides et écologiques."
        },
        {
            "num": "59",
            "mythe": "MYTHE : Les formules géantes impressionnent.",
            "brush_kw": "GÉANTES IMPRESSIONNENT",
            "realite": "RÉALITÉ : La simplicité et la robustesse prévalent. Une formule trop complexe devient inmaintenable."
        },
        {
            "num": "60",
            "mythe": "MYTHE : La bureautique s'apprend une fois.",
            "brush_kw": "S'APPREND UNE FOIS",
            "realite": "RÉALITÉ : Les logiciels évoluent continuellement. Mettre à jour ses compétences est un impératif pro."
        },

        # 61-80: Carrière & Futur du travail
        {
            "num": "61",
            "mythe": "MYTHE : Un grand diplôme garantit la carrière.",
            "brush_kw": "GARANTIT LA CARRIÈRE",
            "realite": "RÉALITÉ : Le marché valorise les compétences concrètes et la capacité à résoudre de vrais problèmes."
        },
        {
            "num": "62",
            "mythe": "MYTHE : Travailler dur dans son coin suffit.",
            "brush_kw": "DANS SON COIN SUFFIT",
            "realite": "RÉALITÉ : La visibilité de tes résultats et ta capacité à communiquer comptent autant que ton travail."
        },
        {
            "num": "63",
            "mythe": "MYTHE : Changer de secteur après 30 ans est tard.",
            "brush_kw": "APRÈS 30 ANS EST TARD",
            "realite": "RÉALITÉ : Les compétences transversales (logique, communication, gestion) s'appliquent partout."
        },
        {
            "num": "64",
            "mythe": "MYTHE : La technique est l'unique atout.",
            "brush_kw": "L'UNIQUE ATOUT",
            "realite": "RÉALITÉ : Les soft skills (empathie, écoute, négociation) font la différence aux postes de direction."
        },
        {
            "num": "65",
            "mythe": "MYTHE : Les jeunes maîtrisent tout le digital.",
            "brush_kw": "TOUT LE DIGITAL",
            "realite": "RÉALITÉ : Utiliser TikTok ne signifie pas savoir structurer des données ou piloter une IA."
        },
        {
            "num": "66",
            "mythe": "MYTHE : Le télétravail casse la cohésion.",
            "brush_kw": "CASSE LA COHÉSION",
            "realite": "RÉALITÉ : C'est le manque de communication et de confiance des managers qui détruit la cohésion."
        },
        {
            "num": "67",
            "mythe": "MYTHE : Attends que l'entreprise te forme.",
            "brush_kw": "QUE L'ENTREPRISE TE FORME",
            "realite": "RÉALITÉ : Ton employabilité est sous ta responsabilité. Investis sur toi-même sans attendre."
        },
        {
            "num": "68",
            "mythe": "MYTHE : L'empathie est inutile en affaires.",
            "brush_kw": "INUTILE EN AFFAIRES",
            "realite": "RÉALITÉ : C'est le moteur du leadership, de la gestion de conflit et du travail d'équipe efficace."
        },
        {
            "num": "69",
            "mythe": "MYTHE : Automatiser son poste rend inutile.",
            "brush_kw": "REND INUTILE",
            "realite": "RÉALITÉ : Automatiser son poste permet d'aborder des projets stratégiques à plus haute valeur ajoutée."
        },
        {
            "num": "70",
            "mythe": "MYTHE : Le manager doit avoir réponse à tout.",
            "brush_kw": "RÉPONSE À TOUT",
            "realite": "RÉALITÉ : Les meilleurs managers savent poser les bonnes questions et s'entourer de collaborateurs experts."
        },
        {
            "num": "71",
            "mythe": "MYTHE : Repartir de zéro est un échec.",
            "brush_kw": "EST UN ÉCHEC",
            "realite": "RÉALITÉ : C'est une preuve de courage et d'adaptabilité face aux mutations du marché du travail."
        },
        {
            "num": "72",
            "mythe": "MYTHE : Le réseau se fait en soirée réseau.",
            "brush_kw": "EN SOIRÉE RÉSEAU",
            "realite": "RÉALITÉ : Le réseau se construit au quotidien en aidant les autres et en partageant de la valeur."
        },
        {
            "num": "73",
            "mythe": "MYTHE : Les introvertis ne peuvent pas diriger.",
            "brush_kw": "NE PEUVENT PAS DIRIGER",
            "realite": "RÉALITÉ : La capacité d'écoute et la réflexion profonde font des introvertis des leaders d'exception."
        },
        {
            "num": "74",
            "mythe": "MYTHE : Demander de l'aide montre la faiblesse.",
            "brush_kw": "MONTRE LA FAIBLESSE",
            "realite": "RÉALITÉ : C'est le signe d'une volonté d'avancer vite et d'éviter les erreurs coûteuses."
        },
        {
            "num": "75",
            "mythe": "MYTHE : Un bon CV détaille toute sa vie.",
            "brush_kw": "DÉTAILLE TOUTE SA VIE",
            "realite": "RÉALITÉ : Un bon CV est un document marketing ciblé spécifiquement sur les besoins futurs du recruteur."
        },
        {
            "num": "76",
            "mythe": "MYTHE : L'imposteur disparaît avec l'âge.",
            "brush_kw": "DISPARAÎT AVEC L'ÂGE",
            "realite": "RÉALITÉ : Il revient à chaque palier. Apprends à avancer malgré lui plutôt qu'à l'attendre disparaître."
        },
        {
            "num": "77",
            "mythe": "MYTHE : Le salaire ne dépend que des années.",
            "brush_kw": "QUE DES ANNÉES",
            "realite": "RÉALITÉ : Le salaire dépend de la rareté de tes compétences et de l'impact direct que tu génères."
        },
        {
            "num": "78",
            "mythe": "MYTHE : Ne jamais se tromper est l'objectif.",
            "brush_kw": "EST L'OBJECTIF",
            "realite": "RÉALITÉ : Ne jamais se tromper signifie ne rien tenter de nouveau. L'échec est une étape d'apprentissage."
        },
        {
            "num": "79",
            "mythe": "MYTHE : Se spécialiser dans une niche est risqué.",
            "brush_kw": "NICHE EST RISQUÉ",
            "realite": "RÉALITÉ : Être un généraliste flou rend invisible. L'expertise ciblée attire les meilleures opportunités."
        },
        {
            "num": "80",
            "mythe": "MYTHE : La retraite est le seul vrai repos.",
            "brush_kw": "LE SEUL VRAI REPOS",
            "realite": "RÉALITÉ : L'équilibre de vie se construit chaque jour, pas après 40 ans de sacrifice continu."
        },

        # 81-100: Mindset & Apprentissage
        {
            "num": "81",
            "mythe": "MYTHE : Le talent est inné et génétique.",
            "brush_kw": "INNÉ ET GÉNÉTIQUE",
            "realite": "RÉALITÉ : Le talent est le produit de milliers d'heures de pratique et de constance délibérée."
        },
        {
            "num": "82",
            "mythe": "MYTHE : Apprendre une compétence prend des années.",
            "brush_kw": "PREND DES ANNÉES",
            "realite": "RÉALITÉ : 20h de pratique concentrée suffisent pour acquérir des bases solides et opérationnelles."
        },
        {
            "num": "83",
            "mythe": "MYTHE : L'échec est le contraire du succès.",
            "brush_kw": "LE CONTRAIRE DU SUCCÈS",
            "realite": "RÉALITÉ : L'échec fait partie intégrante du chemin vers le succès. C'est du feedback précieux."
        },
        {
            "num": "84",
            "mythe": "MYTHE : Les idées viennent d'éclats soudains.",
            "brush_kw": "D'ÉCLATS SOUDAINS",
            "realite": "RÉALITÉ : Les meilleures idées sont la combinaison intelligente de concepts déjà existants."
        },
        {
            "num": "85",
            "mythe": "MYTHE : Lire 50 livres rend plus intelligent.",
            "brush_kw": "REND PLUS INTELLIGENT",
            "realite": "RÉALITÉ : C'est l'application concrète d'un seul livre qui transforme ta vie, pas la vitesse de lecture."
        },
        {
            "num": "86",
            "mythe": "MYTHE : Il faut un plan fixe sur 10 ans.",
            "brush_kw": "FIXE SUR 10 ANS",
            "realite": "RÉALITÉ : Le monde change vite. Il faut une direction claire et une grande agilité à court terme."
        },
        {
            "num": "87",
            "mythe": "MYTHE : La critique est une attaque perso.",
            "brush_kw": "UNE ATTAQUE PERSO",
            "realite": "RÉALITÉ : Une critique constructive est un raccourci gratuit pour améliorer ton travail."
        },
        {
            "num": "88",
            "mythe": "MYTHE : La zone de confort est sans danger.",
            "brush_kw": "EST SANS DANGER",
            "realite": "RÉALITÉ : La zone de confort rétrécit avec le temps. L'apprentissage permanent garantit la sécurité."
        },
        {
            "num": "89",
            "mythe": "MYTHE : L'inspiration doit venir avant.",
            "brush_kw": "DOIT VENIR AVANT",
            "realite": "RÉALITÉ : L'inspiration survient pendant l'action. Se mettre au travail la déclenche."
        },
        {
            "num": "90",
            "mythe": "MYTHE : Avoir des idées suffit pour réussir.",
            "brush_kw": "SUFFIT POUR RÉUSSIR",
            "realite": "RÉALITÉ : L'exécution disciplinée est ce qui transforme une idée originale en résultat concret."
        },
        {
            "num": "91",
            "mythe": "MYTHE : Les winners ne doutent jamais.",
            "brush_kw": "NE DOUTENT JAMAIS",
            "realite": "RÉALITÉ : Ils doutent comme tout le monde, mais ils agissent quand même malgré le doute."
        },
        {
            "num": "92",
            "mythe": "MYTHE : Te comparer aux autres te fait avancer.",
            "brush_kw": "TE FAIT AVANCER",
            "realite": "RÉALITÉ : Tu compares tes coulisses au spectacle des autres. Compare-toi uniquement à toi d'hier."
        },
        {
            "num": "93",
            "mythe": "MYTHE : La créativité est juste artistique.",
            "brush_kw": "JUSTE ARTISTIQUE",
            "realite": "RÉALITÉ : Résoudre un problème complexe ou optimiser un processus demande une immense créativité."
        },
        {
            "num": "94",
            "mythe": "MYTHE : Se former est une dépense d'argent.",
            "brush_kw": "DÉPENSE D'ARGENT",
            "realite": "RÉALITÉ : C'est un investissement qui offre le meilleur rendement sur le long terme."
        },
        {
            "num": "95",
            "mythe": "MYTHE : Travailler dur apporte tout.",
            "brush_kw": "APPORTE TOUT",
            "realite": "RÉALITÉ : Travailler dur sur la mauvaise chose ne mène nulle part. La direction prime sur l'effort."
        },
        {
            "num": "96",
            "mythe": "MYTHE : La chance explique tout le succès.",
            "brush_kw": "EXPLIQUE TOUT LE SUCCÈS",
            "realite": "RÉALITÉ : Les opportunités se créent en se montrant, en publiant et en produisant de la valeur."
        },
        {
            "num": "97",
            "mythe": "MYTHE : Cache tes projets jusqu'à la fin.",
            "brush_kw": "JUSQU'À LA FIN",
            "realite": "RÉALITÉ : Tester rapidement auprès des utilisateurs donne du feedback vital avant d'investir trop."
        },
        {
            "num": "98",
            "mythe": "MYTHE : Le changement est une menace.",
            "brush_kw": "EST UNE MENACE",
            "realite": "RÉALITÉ : Le changement est la seule constante. L'embrasser offre un avantage concurrentiel majeur."
        },
        {
            "num": "99",
            "mythe": "MYTHE : La discipline bride la liberté.",
            "brush_kw": "BRIDE LA LIBERTÉ",
            "realite": "RÉALITÉ : La discipline crée la vraie liberté : liberté financière, temporelle et d'esprit."
        },
        {
            "num": "100",
            "mythe": "MYTHE : C'est trop tard pour commencer.",
            "brush_kw": "TROP TARD POUR COMMENCER",
            "realite": "RÉALITÉ : Le meilleur moment pour commencer était hier. Le deuxième meilleur moment est aujourd'hui. Fonce."
        }
    ]

    font_head = ImageFont.truetype(font_path_bold, 50)
    font_sub = ImageFont.truetype(font_path_reg, 38)
    font_tag = ImageFont.truetype(font_path_bold, 28)

    count = 0
    for item in items:
        # Dark canvas background (Template Noir)
        img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
        draw = ImageDraw.Draw(img)

        # 1. Header Tag "MYTHE vs RÉALITÉ"
        tag_text = "MYTHE vs RÉALITÉ"
        bbox_tag = font_tag.getbbox(tag_text)
        w_tag = bbox_tag[2] - bbox_tag[0]
        draw.text(((width - w_tag) // 2, 140), tag_text, fill=(255, 195, 0, 255), font=font_tag)
        draw.line([(width//2 - 90, 180), (width//2 + 90, 180)], fill=(255, 195, 0, 255), width=3)

        # 2. Text Wrapping
        lines_mythe = textwrap.wrap(item["mythe"], width=22)
        lines_realite = textwrap.wrap(item["realite"], width=25)

        lh_mythe = 68
        lh_realite = 52
        spacing = 50

        h_mythe = len(lines_mythe) * lh_mythe
        h_realite = len(lines_realite) * lh_realite

        total_h = h_mythe + spacing + h_realite
        start_y = 590 - (total_h // 2)

        # 3. Render MYTHE text + Brush underline on brush_kw
        curr_y = start_y
        brush_kw = item["brush_kw"]
        for l in lines_mythe:
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
                
                draw_painter_brush_underline(draw, kw_start_x, kw_end_x, curr_y + 50, color=(255, 195, 0, 255), thickness=18, tilt=-5)

            draw.text((start_x_l, curr_y), l, fill=(255, 255, 255, 255), font=font_head)
            curr_y += lh_mythe

        curr_y += spacing

        # 4. Render RÉALITÉ text
        for l in lines_realite:
            bbox = font_sub.getbbox(l)
            w_l = bbox[2] - bbox[0]
            draw.text(((width - w_l) // 2, curr_y), l, fill=(215, 215, 215, 255), font=font_sub)
            curr_y += lh_realite

        # 5. Logo Light in Bottom Right Footer
        if logo_light:
            lw_l, lh_l = logo_light.size
            img.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

        out_name = f"mythe_vs_realite_{item['num']}.png"
        out_path = os.path.join(target_dir, out_name)
        img.save(out_path, "PNG")
        count += 1
        if count % 10 == 0:
            print(f"Generated {count}/100 images... (latest: {out_name})")

    print(f"DONE! Successfully generated all {count} images in {target_dir}")

if __name__ == "__main__":
    generate_100_mythe_vs_realite()
