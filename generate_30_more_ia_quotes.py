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

def generate_30_more_quotes():
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy\1"
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

    # 30 Brand New Motivational Quotes (Items 70 to 99)
    items = [
        {"num": "70", "headline": "L'IA NE RANGERA PAS TES PRIORITÉS À TA PLACE.", "brush_kw": "TES PRIORITÉS", "subtext": "Savoir ce qui compte vraiment reste le rôle exclusif du leader."},
        {"num": "71", "headline": "CE N'EST PAS LA MACHINE QUI CRÉE LA CONFIANCE.", "brush_kw": "LA CONFIANCE", "subtext": "Tes clients achètent ta parole, ton intégrité et ton histoire."},
        {"num": "72", "headline": "UTILISER L'IA SANS STRATÉGIE C'EST BRÛLER DU TEMPS.", "brush_kw": "BRÛLER DU TEMPS", "subtext": "Définis clairement la destination avant d'appuyer sur l'accélérateur."},
        {"num": "73", "headline": "L'IA PRODUIT DE LA QUANTITÉ, TU APPORTES LA RARETÉ.", "brush_kw": "LA RARETÉ", "subtext": "Dans un monde saturé de contenu automatisé, ta voix unique devient précieuse."},
        {"num": "74", "headline": "NE CONFONDS PAS VITESSE D'EXÉCUTION ET PERTINENCE.", "brush_kw": "PERTINENCE", "subtext": "Faire une erreur en 2 secondes au lieu de 2 heures n'est pas une victoire."},
        {"num": "75", "headline": "L'IA N'A PAS LE SENS DU TIMING STRATÉGIQUE.", "brush_kw": "TIMING STRATÉGIQUE", "subtext": "Savoir quand parler, quand se taire et quand agir reste de la pure psychologie humaine."},
        {"num": "76", "headline": "SI TU NE COMPRENDS PAS LE FOND, L'IA TE TROMPERA.", "brush_kw": "LE FOND", "subtext": "Il faut connaître la théorie pour repérer les fausses informations générées avec assurance."},
        {"num": "77", "headline": "L'IA EST UN ACCÉLÉRATEUR POUR CEUX QUI OSENT.", "brush_kw": "POUR CEUX QUI OSENT", "subtext": "Ceux qui expérimentent aujourd'hui prennent les meilleures places de demain."},
        {"num": "78", "headline": "L'AUTOMATISATION SANS EMPATHIE DEVIENT FROIDE.", "brush_kw": "SANS EMPATHIE", "subtext": "Garde de l'émotion humaine dans chacune de tes interactions."},
        {"num": "79", "headline": "L'IA EST UN PINCEAU, TU ES LE PEINTRE.", "brush_kw": "TU ES LE PEINTRE", "subtext": "Ce n'est pas le pinceau qui fait le chef-d'œuvre, c'est la main qui le guide."},
        {"num": "80", "headline": "TESTER L'IA UNE FOIS NE SUFFIT PAS.", "brush_kw": "NE SUFFIT PAS", "subtext": "C'est une pratique quotidienne. La maîtrise vient avec la répétition."},
        {"num": "81", "headline": "L'IA N'A PAS DE VISION À 5 ANS.", "brush_kw": "DE VISION", "subtext": "Elle répond à l'instant T. Anticiper l'avenir reste ton super-pouvoir."},
        {"num": "82", "headline": "ARNAQUE DU MOMENT : TOUT VOULOIR DÉLÉGUER À L'IA.", "brush_kw": "TOUT DÉLÉGUER", "subtext": "Garde la maîtrise des compétences clés de ton cœur de métier."},
        {"num": "83", "headline": "LA VRAIE VALEUR EST DANS LA DÉCISION.", "brush_kw": "LA DÉCISION", "subtext": "L'IA te donne 10 options, c'est toi qui tranches et en assumeras la responsabilité."},
        {"num": "84", "headline": "NE SOIS PAS UN PASSAGER PASSIF DU CHANGEMENT.", "brush_kw": "PASSAGER PASSIF", "subtext": "Prends le volant. Apprends à maîtriser les outils avant qu'ils ne s'imposent à toi."},
        {"num": "85", "headline": "L'IA NE REMPLACERA PAS LE RELATIONNEL DE TERRAIN.", "brush_kw": "RELATIONNEL DE TERRAIN", "subtext": "Un déjeuner ou une poignée de main vaudra toujours plus qu'un prompt parfait."},
        {"num": "86", "headline": "L'INTELLIGENCE SANS ACTION NE VAUT RIEN.", "brush_kw": "SANS ACTION", "subtext": "L'IA donne des idées, mais seule l'exécution concrète génère des résultats."},
        {"num": "87", "headline": "L'IA EST L'ALLIÉE DES ESPRITS CURIEUX.", "brush_kw": "ESPRITS CURIEUX", "subtext": "Plus tu te poses de bonnes questions, plus l'IA devient un partenaire redoutable."},
        {"num": "88", "headline": "NE CHERCHE PAS À RIVALISER AVEC LE CALCUL.", "brush_kw": "RIVALISER", "subtext": "Joue sur ton terrain : la créativité, l'émotion, le leadership et l'esprit critique."},
        {"num": "89", "headline": "L'IA EST UN MULTIPLICATEUR D'IMPACT.", "brush_kw": "MULTIPLICATEUR D'IMPACT", "subtext": "Donne-toi les moyens d'impacter 10 fois plus de clients avec les mêmes efforts."},
        {"num": "90", "headline": "L'IGNORANCE COÛTE PLUS CHER QUE LA FORMATION.", "brush_kw": "L'IGNORANCE COÛTE", "subtext": "Investir du temps pour te former aujourd'hui te fera gagner des années demain."},
        {"num": "91", "headline": "L'IA TE DONNE DES AILES, GARDE LES PIEDS SUR TERRE.", "brush_kw": "LES PIEDS SUR TERRE", "subtext": "Vérifie toujours les faits et garde une rigueur professionnelle absolue."},
        {"num": "92", "headline": "L'AUDACE HUMAINE NE SE PROGRAMME PAS.", "brush_kw": "NE SE PROGRAMME PAS", "subtext": "Prendre un pari osé ou lancer un projet fou reste le privilège de l'humain."},
        {"num": "93", "headline": "L'IA REND L'EXCELLENCE PLUS ACCESSIBLE.", "brush_kw": "PLUS ACCESSIBLE", "subtext": "Profites-en pour élever tes standards et proposer du travail de haut niveau."},
        {"num": "94", "headline": "NE DEVIENS PAS DÉPENDANT DE L'OUTIL.", "brush_kw": "DÉPENDANT", "subtext": "L'IA doit soutenir ta pensée, pas se substituer à ton raisonnement."},
        {"num": "95", "headline": "LA VITESSE SANS CAP EST UN DANGER.", "brush_kw": "VITESSE SANS CAP", "subtext": "Assure-toi de savoir où tu vas avant d'accélérer la cadence."},
        {"num": "96", "headline": "L'IA SIMPLIFIE LA TECHNIQUE, VALORISE LA STRATÉGIE.", "brush_kw": "VALORISE LA STRATÉGIE", "subtext": "Plus la technique devient facile, plus le sens et la direction prennent de la valeur."},
        {"num": "97", "headline": "CEUX QUI RÉUSSISSENT EXPÉRIMENTENT SANS CESSE.", "brush_kw": "EXPÉRIMENTENT SANS CESSE", "subtext": "N'attends pas la méthode parfaite, teste par toi-même et adapte sur le terrain."},
        {"num": "98", "headline": "L'IA EST UN BOOST, PAS UN SUBSTITUT D'EFFORT.", "brush_kw": "PAS UN SUBSTITUT", "subtext": "Le travail et la persévérance restent les piliers de toute réussite durable."},
        {"num": "99", "headline": "LE FUTUR APPARTIENT À CEUX QUI SE FORMENT.", "brush_kw": "SE FORMENT", "subtext": "Fais le choix de l'apprentissage continu et deviens incontournable dans ton domaine."}
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

        # Render Subtext + check brush keyword
        for l in lines_sub:
            bbox = font_sub.getbbox(l)
            w_l = bbox[2] - bbox[0]
            start_x_l = (width - w_l) // 2
            
            if brush_kw in l:
                idx = l.index(brush_kw)
                prefix = l[:idx]
                prefix_w = font_sub.getbbox(prefix)[2] - font_sub.getbbox(prefix)[0] if prefix else 0
                kw_w = font_sub.getbbox(brush_kw)[2] - font_sub.getbbox(brush_kw)[0]
                
                kw_start_x = start_x_l + prefix_w
                kw_end_x = kw_start_x + kw_w
                
                draw_painter_brush_underline(draw, kw_start_x, kw_end_x, curr_y + 40 + 2, color=(255, 195, 0, 255), thickness=16, tilt=-5)

            draw.text((start_x_l, curr_y), l, fill=(215, 215, 215, 255), font=font_sub)
            curr_y += lh_sub

        # Logo in Bottom Right Footer
        if logo_light:
            lw_l, lh_l = logo_light.size
            img.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

        out_name = f"motivation_ia_verite_{item['num']}.png"
        out_path = os.path.join(target_dir, out_name)
        img.save(out_path, "PNG")
        print(f"Generated Motivation #{item['num']}: {out_path}")

if __name__ == "__main__":
    generate_30_more_quotes()
