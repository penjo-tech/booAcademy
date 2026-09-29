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

def generate_90_bureautique_verites():
    # Target directory: folder 2
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy\2"
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

    # 90 Brand New Brutal Truths on Bureautique (Items 11 to 100)
    items = [
        # Group 1: Excel & Data Chaos (11 - 25)
        {
            "num": "11",
            "headline": "UN TABLEAU SANS COULEUR STRUCTURÉE EST ILLISIBLE.",
            "brush_kw": "STRUCTURÉE",
            "subtext": "La surcharge visuelle empêche vos décideurs de saisir les bonnes tendances au premier coup d'œil."
        },
        {
            "num": "12",
            "headline": "UTILISER EXCEL COMME BASE DE DONNÉES EST UNE ERREUR.",
            "brush_kw": "UNE ERREUR",
            "subtext": "Excel n'est pas une base relationnelle. Au-delà de 10 000 lignes, le système s'effondre."
        },
        {
            "num": "13",
            "headline": "LES CALCULS À LA CALCULATRICE DANS EXCEL SONT ABSURDES.",
            "brush_kw": "ABSURDES",
            "subtext": "Saisir des valeurs en dur au lieu de formules garantit une erreur au moindre changement."
        },
        {
            "num": "14",
            "headline": "LA RECHERCHEV EST DÉPASSÉE DEPUIS DES ANNÉES.",
            "brush_kw": "DÉPASSÉE",
            "subtext": "Passez à RECHERCHEX pour éviter d'effondrer vos tableaux au moindre ajout de colonne."
        },
        {
            "num": "15",
            "headline": "NE PAS PROTÉGER VOS FORMULES EST UNE INSOUCIANCE.",
            "brush_kw": "INSOUCIANCE",
            "subtext": "Un clic maladroit d'un collègue peut fausser vos résultats financiers en toute discrétion."
        },
        {
            "num": "16",
            "headline": "LES CELLULES FUSIONNÉES SONT LE CAUCHEMAR DU TRI.",
            "brush_kw": "CAUCHEMAR DU TRI",
            "subtext": "Fusionner des cellules empêche les filtres et détruit la structure logique de vos données."
        },
        {
            "num": "17",
            "headline": "UN TABLEAU CROISÉ DYNAMIQUE SE FAIT EN 3 CLICS.",
            "brush_kw": "EN 3 CLICS",
            "subtext": "Rédiger des résumés manuels pendant des heures est un pur gaspillage de votre énergie."
        },
        {
            "num": "18",
            "headline": "SAISIR LA MÊME DONNÉE DEUX FOIS EST UN ÉCHEC.",
            "brush_kw": "UN ÉCHEC",
            "subtext": "L'information doit être liée dynamiquement d'une feuille à l'autre, jamais dupliquée."
        },
        {
            "num": "19",
            "headline": "NE PAS VALIDER LES ENTRÉES DE DONNÉES CRÉE LE BORDEL.",
            "brush_kw": "CRÉE LE BORDEL",
            "subtext": "Sans listes déroulantes, vous aurez 10 orthographes différentes pour le même client."
        },
        {
            "num": "20",
            "headline": "LES GRAPHIQUES EN CAMEMBERT SONT SOUVENT INUTILES.",
            "brush_kw": "SOUVENT INUTILES",
            "subtext": "Privilégiez les histogrammes pour comparer avec clarté et précision plusieurs catégories."
        },
        {
            "num": "21",
            "headline": "MASQUER DES COLONNES AU LIEU DE GROUPER EST UN PIÈGE.",
            "brush_kw": "EST UN PIÈGE",
            "subtext": "Les colonnes masquées oubliées provoquent des erreurs de calcul dramatiques lors des exports."
        },
        {
            "num": "22",
            "headline": "UN EXCEL DE 100 MO EST UN SIGNAL D'ALERTE.",
            "brush_kw": "SIGNAL D'ALERTE",
            "subtext": "Votre fichier souffre de gaspillage de formats et de plages de calcul inutilisées."
        },
        {
            "num": "23",
            "headline": "IGNORER POWER QUERY C'EST CONDAMNER SON TEMPS.",
            "brush_kw": "CONDAMNER SON TEMPS",
            "subtext": "Nettoyer et transformer des données à la main chaque mois est totalement obsolète."
        },
        {
            "num": "24",
            "headline": "COMPTER DES CELLULES À LA MAIN EST EFFARANT.",
            "brush_kw": "EFFARANT",
            "subtext": "Utilisez NB.SI et SOMME.SI au lieu de fatiguer vos yeux inutilement sur votre écran."
        },
        {
            "num": "25",
            "headline": "MONTRER UN EXCEL SANS MISE EN PAGE C'EST PERDRE EN PRO.",
            "brush_kw": "PERDRE EN PRO",
            "subtext": "La clarté et l'esthétique d'un tableau reflètent directement la rigueur de votre travail."
        },

        # Group 2: Document Management & Files (26 - 40)
        {
            "num": "26",
            "headline": "LE BUREAU DE TON PC N'EST PAS UN DOSSIER DE RANGEMENT.",
            "brush_kw": "RANGEMENT",
            "subtext": "Accumuler 200 icônes sur son bureau ralentit votre ordinateur et brouille votre esprit."
        },
        {
            "num": "27",
            "headline": "LE NOMMAGE DOCUMENT1.DOCX EST UNE FAILLITE.",
            "brush_kw": "UNE FAILLITE",
            "subtext": "Chaque fichier doit porter une date, le nom du projet et un numéro de version explicite."
        },
        {
            "num": "28",
            "headline": "GARDER 50 VERSIONS DU MÊME FICHIER EST INVALIDE.",
            "brush_kw": "EST INVALIDE",
            "subtext": "Activez l'historique des versions sur SharePoint au lieu d'encombrer le serveur d'entreprise."
        },
        {
            "num": "29",
            "headline": "ENVOYER UN DOCX AU LIEU D'UN PDF EST UN AMATEURISME.",
            "brush_kw": "AMATEURISME",
            "subtext": "Votre mise en page risque d'être totalement déformée sur l'écran ou le mobile du client."
        },
        {
            "num": "30",
            "headline": "NE PAS SAUVEGARDER SUR LE CLOUD EST UN RISQUE MORTEL.",
            "brush_kw": "RISQUE MORTEL",
            "subtext": "Un disque dur qui crashe sans sauvegarde récente détruit des mois d'efforts irremplaçables."
        },
        {
            "num": "31",
            "headline": "PARTAGER UN FICHIER PAR EMAIL EST UNE HABITUDE DU PASSÉ.",
            "brush_kw": "HABITUDE DU PASSÉ",
            "subtext": "Partagez un lien d'accès sécurisé pour garder le contrôle absolu sur la version finale."
        },
        {
            "num": "32",
            "headline": "LES DOSSIERS IMBRIQUÉS SUR 10 NIVEAUX SONT INCOMPRÉHENSIBLES.",
            "brush_kw": "INCOMPRÉHENSIBLES",
            "subtext": "Personne ne retrouvera jamais vos documents enfouis sous une montagne de sous-dossiers."
        },
        {
            "num": "33",
            "headline": "IGNORER LA RECHERCHE AVANCÉE DE FICHIERS EST UN HANDICAP.",
            "brush_kw": "UN HANDICAP",
            "subtext": "Maîtrisez les filtres de recherche de votre OS pour dénicher n'importe quel fichier en 2 secondes."
        },
        {
            "num": "34",
            "headline": "CONSERVER DES FICHIERS OBSOLÈTES POLLUE LE SERVEUR.",
            "brush_kw": "POLLUE LE SERVEUR",
            "subtext": "Faites un archivage annuel strict pour ne conserver dans votre espace que l'actif."
        },
        {
            "num": "35",
            "headline": "MODIFIER LE MÊME DOCUMENT PAR EMAIL CRÉE LA CONFUSION.",
            "brush_kw": "CRÉE LA CONFUSION",
            "subtext": "Adoptez la co-édition en direct sur OneDrive ou Teams pour coordonner les contributions."
        },
        {
            "num": "36",
            "headline": "L'ABSENCE DE PROPRIÉTÉS ET TAGS SUR TES DOCS EST UN GÂCHIS.",
            "brush_kw": "UN GÂCHIS",
            "subtext": "Les métadonnées permettent d'indexer et trier vos projets complexes sans aucun effort."
        },
        {
            "num": "37",
            "headline": "IMPRIMER POUR RELIRE EST UNE HABITUDE COÛTEUSE.",
            "brush_kw": "HABITUDE COÛTEUSE",
            "subtext": "Utilisez le mode lecture, la lecture vocale ou le surlignage numérique pour réviser sans papier."
        },
        {
            "num": "38",
            "headline": "SCANNER DES DOCUMENTS SANS OCR EST INEXCUSABLE.",
            "brush_kw": "INEXCUSABLE",
            "subtext": "Un PDF scanné sous forme d'image rend impossible tout copier-coller ou recherche de mot-clé."
        },
        {
            "num": "39",
            "headline": "NE PAS PROTÉGER LES PDFS CONFIDENTIELS EST UNE FAUTE.",
            "brush_kw": "UNE FAUTE",
            "subtext": "Les données sensibles de vos clients doivent être systématiquement verrouillées."
        },
        {
            "num": "40",
            "headline": "GARDER DES FICHIERS LOURDS ENCOMBRE TON ORDINATEUR.",
            "brush_kw": "TON ORDINATEUR",
            "subtext": "Nettoyez votre dossier Téléchargements et vidangez votre corbeille de façon hebdomadaire."
        },

        # Group 3: Emails, Outlook & Meetings (41 - 55)
        {
            "num": "41",
            "headline": "LA BOÎTE MAIL N'EST PAS UNE TO-DO LIST.",
            "brush_kw": "PAS UNE TO-DO LIST",
            "subtext": "Mélanger messages entrants et tâches prioritaires garantit l'oubli et génère un stress inutile."
        },
        {
            "num": "42",
            "headline": "RÉPONDRE À TOUS PAR RÉFLEXE POLLUE LES BOÎTES.",
            "brush_kw": "POLLUE LES BOÎTES",
            "subtext": "N'incluez que les collaborateurs directement concernés par la décision ou l'information."
        },
        {
            "num": "43",
            "headline": "UN OBJET D'EMAIL FLOU GARANTIT UNE RÉPONSE TARDIVE.",
            "brush_kw": "RÉPONSE TARDIVE",
            "subtext": "Rédigez des objets précis mentionnant le nom du projet et l'action concrète attendue."
        },
        {
            "num": "44",
            "headline": "ÉCRIRE UN PAVÉ SANS STRUCTURE EST UN ÉCHEC.",
            "brush_kw": "UN ÉCHEC",
            "subtext": "Aérez vos messages avec des puces et mettez en gras les questions stratégiques."
        },
        {
            "num": "45",
            "headline": "LES NOTIFICATIONS D'EMAILS DÉTRUISENT VOTRE FOCUS.",
            "brush_kw": "DÉTRUISENT VOTRE FOCUS",
            "subtext": "Désactivez les pop-ups et traitez vos emails à des créneaux horaires fixes."
        },
        {
            "num": "46",
            "headline": "ENVOYER UN EMAIL POUR UN SIMPLE D'ACCORD EST INUTILE.",
            "brush_kw": "EST INUTILE",
            "subtext": "Utilisez les réactions rapides sur Teams ou votre messagerie instantanée d'équipe."
        },
        {
            "num": "47",
            "headline": "NE PAS METTRE DE MESSAGE D'ABSENCE EST MANQUER DE RESPECT.",
            "brush_kw": "MANQUER DE RESPECT",
            "subtext": "Prévenez vos interlocuteurs et donnez toujours les coordonnées d'un contact d'urgence."
        },
        {
            "num": "48",
            "headline": "CHERCHER UN ANCIEN EMAIL PENDANT 15 MIN EST UNE PERTE DE TEMPS.",
            "brush_kw": "PERTE DE TEMPS",
            "subtext": "Créez des règles d'archivage automatique et des dossiers thématiques clairs."
        },
        {
            "num": "49",
            "headline": "L'ABSENCE DE SIGNATURE PRO DÉCONCERTE VOS CONTACTS.",
            "brush_kw": "DÉCONCERTE VOS CONTACTS",
            "subtext": "Une signature sobre avec poste, téléphone et liens utiles crédibilise chaque envoi."
        },
        {
            "num": "50",
            "headline": "PROGRAMMER DES RÉUNIONS SANS ORDRE DU JOUR EST ANORMAL.",
            "brush_kw": "EST ANORMAL",
            "subtext": "Sans objectif clair dès l'invitation, 80% du temps de la réunion sera inévitablement gâché."
        },
        {
            "num": "51",
            "headline": "INVITER 15 PERSONNES À UNE SIMPLERÉUNION EST ABSURDE.",
            "brush_kw": "EST ABSURDE",
            "subtext": "Un court compte-rendu ou une note explicative remplace avantageusement une longue réunion."
        },
        {
            "num": "52",
            "headline": "NE PAS UTILISER LE CALENDRIER PRO EST UNE ERREUR.",
            "brush_kw": "UNE ERREUR",
            "subtext": "Bloquez des plages de travail individuel au même titre que vos réunions d'équipe."
        },
        {
            "num": "53",
            "headline": "CONFONDRE URGENCE ET IMPORTANCE NOIE VOTRE JOURNÉE.",
            "brush_kw": "NOIE VOTRE JOURNÉE",
            "subtext": "Tout ce qui atterrit dans votre boîte mail ne mérite pas une interruption immédiate."
        },
        {
            "num": "54",
            "headline": "LES RAPPELS EN RETARD SUR OUTLOOK NE SERVENT À RIEN.",
            "brush_kw": "NE SERVENT À RIEN",
            "subtext": "Programmez vos rappels 15 minutes ou 24 heures à l'avance pour anticiper réellement."
        },
        {
            "num": "55",
            "headline": "NE PAS NETTOYER SA BOÎTE SATURE LES SERVEURS.",
            "brush_kw": "SATURE LES SERVEURS",
            "subtext": "Archiver ou supprimer les pièces jointes volumineuses libère de l'espace et accélère Outlook."
        },

        # Group 4: Word & Document Processing (56 - 70)
        {
            "num": "56",
            "headline": "TAPER SUR ENTRÉE 10 FOIS POUR CHANGER DE PAGE EST INCORRECT.",
            "brush_kw": "EST INCORRECT",
            "subtext": "Utilisez le saut de page (Ctrl + Entrée) pour conserver une mise en page parfaite."
        },
        {
            "num": "57",
            "headline": "FRACTURER LA NUMÉROTATION MANUELLEMENT EST UN CAUCHEMAR.",
            "brush_kw": "UN CAUCHEMAR",
            "subtext": "Laissez Word gérer automatiquement les listes hiérarchisées et la numérotation."
        },
        {
            "num": "58",
            "headline": "NE PAS UTILISER LE SOMMAIRE AUTO EST DE LA FOLIE.",
            "brush_kw": "DE LA FOLIE",
            "subtext": "Créer une table des matières à la main prend des heures et introduit de nombreuses erreurs."
        },
        {
            "num": "59",
            "headline": "LES ESPACES MULTIPLES POUR ALIGNER DU TEXTE SONT INTERDITS.",
            "brush_kw": "SONT INTERDITS",
            "subtext": "Utilisez les tabulations et les retraits de paragraphe pour un alignement impeccable."
        },
        {
            "num": "60",
            "headline": "COPIER DU TEXTE DU WEB SANS PURGER LE FORMAT DÉTRUIT LE DOC.",
            "brush_kw": "DÉTRUIT LE DOC",
            "subtext": "Utilisez le collage en texte brut pour préserver l'harmonie typographique de votre rapport."
        },
        {
            "num": "61",
            "headline": "CHANGER LA POLICE PARTOUT À LA MAIN EST UNE PERTE DE TEMPS.",
            "brush_kw": "PERTE DE TEMPS",
            "subtext": "Modifiez directement le style 'Normal' pour appliquer le changement à l’ensemble du document."
        },
        {
            "num": "62",
            "headline": "UN DOCUMENT DE 50 PAGES SANS EN-TÊTE EST INCOMPLET.",
            "brush_kw": "EST INCOMPLET",
            "subtext": "Numérotez les pages et rappelez le titre de l'ouvrage ou du rapport en en-tête."
        },
        {
            "num": "63",
            "headline": "IGNORER LE VOLET DE NAVIGATION REND LA LECTURE DIFFICILE.",
            "brush_kw": "LECTURE DIFFICILE",
            "subtext": "Le volet de navigation permet de restructurer un long rapport d'un simple glisser-déposer."
        },
        {
            "num": "64",
            "headline": "LES TABLEAUX DANS WORD SONT SOUS-EXPLOITÉS.",
            "brush_kw": "SOUS-EXPLOITÉS",
            "subtext": "Ajustez les marges intérieures, soignez les bordures et répétez la ligne d'en-tête."
        },
        {
            "num": "65",
            "headline": "N'UTILISER QU'UNE POLICE PAR DÉFAUT MANQUE DE DYNAMISME.",
            "brush_kw": "MANQUE DE DYNAMISME",
            "subtext": "Associez une police percutante pour les titres et une font lisible pour le corps de texte."
        },
        {
            "num": "66",
            "headline": "LES IMAGES QUI SAUTENT DANS WORD VIENNENT D'UN MAUVAIS ANCRAGE.",
            "brush_kw": "MAUVAIS ANCRAGE",
            "subtext": "Configurez l'habillage en 'Carré' ou 'Aligné sur le texte' pour stabiliser vos visuels."
        },
        {
            "num": "67",
            "headline": "NE PAS ACTIVER LA CORRECTION DU TEXTE EST UN RISQUE.",
            "brush_kw": "EST UN RISQUE",
            "subtext": "Une faute d'orthographe évidente dans un devis entache immédiatement votre professionnalisme."
        },
        {
            "num": "68",
            "headline": "CONCEVOIR UN MODÈLE DE DOC À CHAQUE FOIS EST ABSURDE.",
            "brush_kw": "EST ABSURDE",
            "subtext": "Créez un modèle .dotx pré-configuré aux couleurs de votre entreprise."
        },
        {
            "num": "69",
            "headline": "LES RUPTURES DE SECTION SONT INDISPENSABLES.",
            "brush_kw": "INDISPENSABLES",
            "subtext": "Ne faites pas pivoter tout votre document Word pour une unique page en paysage."
        },
        {
            "num": "70",
            "headline": "NE PAS SUIVRE LES MODIFICATIONS CRÉE LE DÉSACCORD.",
            "brush_kw": "CRÉE LE DÉSACCORD",
            "subtext": "Activez le mode 'Suivi des modifications' lors des relectures partagées à plusieurs."
        },

        # Group 5: Presentations & PowerPoint (71 - 80)
        {
            "num": "71",
            "headline": "LIRE SES DIAPOSITIVES EN RÉUNION EST EMBARRASSANT.",
            "brush_kw": "EMBARRASSANT",
            "subtext": "Vos visuels servent de support dynamique, pas de prompteur pour votre discours."
        },
        {
            "num": "72",
            "headline": "SURCHARGER UNE DIAPO DE TEXTE TUE L'ATTENTION.",
            "brush_kw": "TUE L'ATTENTION",
            "subtext": "Appliquez la règle d'une seule idée forte par diapositive accompagnée de mots-clés."
        },
        {
            "num": "73",
            "headline": "UTILISER 10 POLICES DIFFÉRENTES DÉTRUIT LE DESIGN.",
            "brush_kw": "DÉTRUIT LE DESIGN",
            "subtext": "Limitez-vous à 2 typographies maximum pour conserver une identité visuelle cohérente."
        },
        {
            "num": "74",
            "headline": "LES ANIMATIONS FLASHY FONT AMATEUR.",
            "brush_kw": "FONT AMATEUR",
            "subtext": "Privilégiez des transitions subtiles et fluides comme le 'Fondu' ou le 'Morphing'."
        },
        {
            "num": "75",
            "headline": "IGNORER LE MASQUE DE DIAPOSITIVES FAIT PERDRE DU TEMPS.",
            "brush_kw": "FAIT PERDRE DU TEMPS",
            "subtext": "Modifiez le logo ou la palette en 1 seul clic sur l'ensemble de votre présentation."
        },
        {
            "num": "76",
            "headline": "DES IMAGES FLOUES DÉCREDIBILISENT LE PROJET.",
            "brush_kw": "DÉCREDIBILISENT LE PROJET",
            "subtext": "N'utilisez que des visuels haute définition issus de banques d'images professionnelles."
        },
        {
            "num": "77",
            "headline": "MONTRER DES TABLEAUX BRUTS SUR SLIDE EST UN ÉCHEC.",
            "brush_kw": "UN ÉCHEC",
            "subtext": "Extrayez uniquement le chiffre clé marquant ou présentez un graphique épuré."
        },
        {
            "num": "78",
            "headline": "NE PAS TESTER SA PRÉSENTATION CRÉE DES SURPRISES.",
            "brush_kw": "CRÉE DES SURPRISES",
            "subtext": "Les contrastes de couleurs et les polices varient selon les projecteurs et écrans."
        },
        {
            "num": "79",
            "headline": "ALIGNER LES ÉLÉMENTS À L'ŒIL EST IMPRÉCIS.",
            "brush_kw": "EST IMPRÉCIS",
            "subtext": "Servez-vous des repères dynamiques et des fonctions de distribution automatique."
        },
        {
            "num": "80",
            "headline": "PRÉSENTER SANS CHRONOMÉTRER EST DANGEREUX.",
            "brush_kw": "EST DANGEREUX",
            "subtext": "Répétez au préalable pour respecter scrupuleusement le temps imparti."
        },

        # Group 6: Automation, Mindset & Best Practices (81 - 100)
        {
            "num": "81",
            "headline": "REFUSER APPRENDRE DE NOUVEAUX OUTILS EST UN SUICIDE PRO.",
            "brush_kw": "SUICIDE PRO",
            "subtext": "Le monde du travail évolue vite : la rigidité vous condamne à l'obsolescence."
        },
        {
            "num": "82",
            "headline": "LE MULTITÂCHE EN BUREAUTIQUE N'EXISTE PAS.",
            "brush_kw": "N'EXISTE PAS",
            "subtext": "Passer continuellement d'une fenêtre à l'autre fait chuter votre efficacité globale de 20%."
        },
        {
            "num": "83",
            "headline": "CONSERVER DES PROCESSUS OBSOLÈTES EST NÉFASTE.",
            "brush_kw": "EST NÉFASTE",
            "subtext": "Interrogez régulièrement vos méthodes : 'Pourquoi faisons-nous cela ainsi ?'."
        },
        {
            "num": "84",
            "headline": "NE PAS SE FORMER C'EST ACCEPTER DE RAMER.",
            "brush_kw": "ACCEPTER DE RAMER",
            "subtext": "Consacrez 30 minutes chaque semaine à explorer une fonction cachée de vos logiciels."
        },
        {
            "num": "85",
            "headline": "LES MACROS EXCEL PEUVENT SAUVER VOTRE SEMAINE.",
            "brush_kw": "SAUVER VOTRE SEMAINE",
            "subtext": "Enregistrez vos manipulations récurrentes pour les exécuter automatiquement."
        },
        {
            "num": "86",
            "headline": "IGNORER POWER AUTOMATE C'EST RESTÉR AU PASSÉ.",
            "brush_kw": "RESTÉR AU PASSÉ",
            "subtext": "Interconnectez vos applications métier sans écrire une seule ligne de code."
        },
        {
            "num": "87",
            "headline": "IGNORER LES RACCOURCIS FREINE VOTRE RYTHME.",
            "brush_kw": "FREINE VOTRE RYTHME",
            "subtext": "Win+V, Win+E et Alt+Tab sont vos meilleurs alliés pour fluidifier votre navigation."
        },
        {
            "num": "88",
            "headline": "LES ERREURS RÉPÉTITIVES NÉCESSITENT UNE CHECK-LIST.",
            "brush_kw": "UNE CHECK-LIST",
            "subtext": "Ne reposez pas sur votre seule mémoire pour mener à bien des procédures complexes."
        },
        {
            "num": "89",
            "headline": "PARTAGER DES MOTS DE PASSE EN CLAIR EST UN CRIME.",
            "brush_kw": "EST UN CRIME",
            "subtext": "Adoptez un gestionnaire de mots de passe professionnel et crypté pour l'équipe."
        },
        {
            "num": "90",
            "headline": "NE PAS NETTOYER SES ACCÈS SYSTÈME EST UN RISQUE.",
            "brush_kw": "EST UN RISQUE",
            "subtext": "Revoyez périodiquement les autorisations accordées sur vos répertoires partagés."
        },
        {
            "num": "91",
            "headline": "TRAVAILLER SUR DEUX ÉCRANS N'EST PAS UN LUXE.",
            "brush_kw": "PAS UN LUXE",
            "subtext": "Disposer d'un double affichage augmente immédiatement votre rapidité de traitement."
        },
        {
            "num": "92",
            "headline": "NE PAS CUSTOMISER LA BARRE RAPIDE EST UN GÂCHIS.",
            "brush_kw": "EST UN GÂCHIS",
            "subtext": "Placez vos fonctionnalités quotidiennes au sommet de vos fenêtres pour y accéder en 1 clic."
        },
        {
            "num": "93",
            "headline": "L'ABSENCE DE CLARTÉ SUR VOS TÂCHES CRÉE DU STRESS.",
            "brush_kw": "CRÉE DU STRESS",
            "subtext": "Clarifiez vos priorités chaque soir afin d'attaquer la journée suivante en toute sérénité."
        },
        {
            "num": "94",
            "headline": "CONFONDRE ACTIVITÉ ET PRODUCTIVITÉ EST UNE ILLUSION.",
            "brush_kw": "UNE ILLUSION",
            "subtext": "Multiplier les clics et brasser de l'air ne signifie pas créer de la vraie valeur."
        },
        {
            "num": "95",
            "headline": "TRAVAILLER EN SILO DÉTRUIT LA SYNERGIE.",
            "brush_kw": "DÉTRUIT LA SYNERGIE",
            "subtext": "Partagez vos astuces et vos trames bureautiques pour faire progresser l'équipe."
        },
        {
            "num": "96",
            "headline": "CORRIGER DES ERREURS COÛTE PLUS CHER QUE SE FORMER.",
            "brush_kw": "QUE SE FORMER",
            "subtext": "Prévenir les mauvaises pratiques demande 10 fois moins d'efforts que réparer la casse."
        },
        {
            "num": "97",
            "headline": "TAPPER SANS REGARDER LE CLAVIER DOUBLE VOTRE VITESSE.",
            "brush_kw": "DOUBLE VOTRE VITESSE",
            "subtext": "La dactylographie moderne est un investissement personnel rentable à vie."
        },
        {
            "num": "98",
            "headline": "LE PRESSE-PAPIERS MULTIPLE WINDOWS GAGNE DU TEMPS.",
            "brush_kw": "GAGNE DU TEMPS",
            "subtext": "Le raccourci Win+V conserve un historique complet de vos éléments copiés."
        },
        {
            "num": "99",
            "headline": "LA BUREAUTIQUE EST L'ÉPINE DORSALE DES PROS.",
            "brush_kw": "ÉPINE DORSALE",
            "subtext": "Négliger la bureautique revient à fragiliser l'ensemble de la chaîne opérationnelle."
        },
        {
            "num": "100",
            "headline": "LA VRAIE MAÎTRISE LIBÈRE POUR CE QUI COMPTE.",
            "brush_kw": "POUR CE QUI COMPTE",
            "subtext": "Domptez vos outils quotidiens pour vous consacrer pleinement à votre vraie valeur."
        }
    ]

    font_size_head = 64
    font_head = ImageFont.truetype(font_path_bold, font_size_head)
    font_sub = ImageFont.truetype(font_path_reg, 40)

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

        out_name = f"motivation_bureautique_verite_{item['num']}.png"
        out_path = os.path.join(target_dir, out_name)
        img.save(out_path, "PNG")
        print(f"Generated Motivation #{item['num']}: {out_path}")

if __name__ == "__main__":
    generate_90_bureautique_verites()
