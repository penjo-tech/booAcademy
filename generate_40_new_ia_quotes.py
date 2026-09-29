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

def generate_40_quotes():
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

    # 40 Brand New Motivational Quotes (Items 30 to 69)
    items = [
        {"num": "30", "headline": "L'IA EST UN ACCÉLÉRATEUR, PAS UN RACCOURCI.", "brush_kw": "PAS UN RACCOURCI", "subtext": "Elle te fait gagner du temps, mais elle ne fera jamais le travail d'apprentissage à ta place."},
        {"num": "31", "headline": "NE LAISSE PAS L'IA ÉCRIRE TON HISTOIRE.", "brush_kw": "TON HISTOIRE", "subtext": "Tes valeurs, ta culture et ta vision ne se trouvent dans aucun dataset d'entraînement."},
        {"num": "32", "headline": "L'IA SANS PROMPT PRÉCIS, C'EST UN TIR À L'AVEUGLE.", "brush_kw": "TIR À L'AVEUGLE", "subtext": "Sois d'une clarté chirurgicale dans tes instructions si tu veux des résultats d'exception."},
        {"num": "33", "headline": "L'EXPERTISE SANS IA SERA LENTE. L'IA SANS EXPERTISE SERA DANGEREUSE.", "brush_kw": "DANGEREUSE", "subtext": "Combine ton savoir-faire métier avec la puissance des algorithmes pour devenir imbattable."},
        {"num": "34", "headline": "CEUX QUI ONT PEUR DE L'IA ONT SOUVENT PEUR DE CHANGER.", "brush_kw": "PEUR DE CHANGER", "subtext": "L'outil n'est pas ton ennemi. La résistance au changement est ton seul vrai frein."},
        {"num": "35", "headline": "L'IA NE REMPLACERA JAMAIS TON INTUITION DE TERRAIN.", "brush_kw": "TON INTUITION", "subtext": "Les données observent le passé. Ton intuition et ton flair sentent les opportunités de demain."},
        {"num": "36", "headline": "PROMPT DE QUALITÉ = RÉFLEXION EN AMONT.", "brush_kw": "RÉFLEXION EN AMONT", "subtext": "Prends 5 minutes pour réfléchir à ton objectif avant de taper le moindre mot dans ChatGPT."},
        {"num": "37", "headline": "SI TU UTILISES L'IA COMME TOUT LE MONDE, TU SERAS MOYEN.", "brush_kw": "TU SERAS MOYEN", "subtext": "Injecte tes propres exemples, tes données et ton style unique dans chaque requête."},
        {"num": "38", "headline": "L'IA EST L'ÉGALISATEUR ULTIME DES CHANCES.", "brush_kw": "ÉGALISATEUR ULTIME", "subtext": "Aujourd'hui, un indépendant dans son salon a la même puissance de frappe qu'une multinationale."},
        {"num": "39", "headline": "CE N'EST PAS UNE GUERRE HUMAIN CONTRE IA.", "brush_kw": "UNE ALLIANCE", "subtext": "C'est une alliance. L'intelligence artificielle au service de l'intelligence humaine."},
        {"num": "40", "headline": "APPRENDS À DÉLÉGUER À L'IA COMME À UN COLLABORATEUR.", "brush_kw": "COLLABORATEUR", "subtext": "Donne-lui un rôle clair, un contexte précis et repasse derrière pour valider son travail."},
        {"num": "41", "headline": "L'IA NE RÉSOUDRA PAS TON DÉFICIT DE DISCIPLINE.", "brush_kw": "DISCIPLINE", "subtext": "Elle te donne des outils puissants, mais c'est ta rigueur quotidienne qui fera la différence."},
        {"num": "42", "headline": "LA CRÉATIVITÉ C'EST CONNECTER DES IDÉES INCOMPATIBLES.", "brush_kw": "INCOMPATIBLES", "subtext": "L'IA cherche la moyenne prévisible. L'humain crée la surprise inattendue."},
        {"num": "43", "headline": "TON CERVEAU EST LE CAPITAINE, L'IA EST LE MOTEUR.", "brush_kw": "LE CAPITAINE", "subtext": "Un moteur V12 sans capitaine va droit dans le mur. Garde le contrôle du gouvernail."},
        {"num": "44", "headline": "L'IA EST UNE OPPORTUNITÉ HISTORIQUE POUR L'AFRIQUE.", "brush_kw": "OPPORTUNITÉ HISTORIQUE", "subtext": "Saute des étapes technologiques et prends une longueur d'avance dès aujourd'hui."},
        {"num": "45", "headline": "ARNAQUE DE LA FACILITÉ : COPIER-COLLER SANS RÉFLÉCHIR.", "brush_kw": "COPIER-COLLER", "subtext": "Si tu ne repasses pas sur ce que produit l'IA, ton travail perd toute crédibilité."},
        {"num": "46", "headline": "L'IA N'A PAS DE PASSION. TOI SI.", "brush_kw": "PAS DE PASSION", "subtext": "C'est la passion et l'énergie que tu mets dans tes projets qui captivent ton audience."},
        {"num": "47", "headline": "LE MARCHÉ NE PAYERA PAS POUR DES RÉPONSES GÉNÉRIQUES.", "brush_kw": "GÉNÉRIQUES", "subtext": "Tout le monde peut générer du texte. La valeur réside dans ta touche personnelle."},
        {"num": "48", "headline": "SOIS PLUS CURIEUX QUE LA MOYENNE.", "brush_kw": "PLUS CURIEUX", "subtext": "Teste de nouveaux outils chaque semaine. C'est l'expérimentation constante qui crée l'avance."},
        {"num": "49", "headline": "L'IA MULTIPLIE TA VITESSE D'EXÉCUTION PAR 10.", "brush_kw": "PAR 10", "subtext": "Ce qui te prenait une semaine se fait en une journée. Utilise ce temps libre pour innover."},
        {"num": "50", "headline": "L'IGNORANCE D'AUJOURD'HUI SERA LE REGRET DE DEMAIN.", "brush_kw": "REGRET DE DEMAIN", "subtext": "Ne dis pas dans 5 ans : 'J'aurais dû m'y mettre plus tôt'. Commence maintenant."},
        {"num": "51", "headline": "LA CONFIDENTIALITÉ DE TES DONNÉES N'EST PAS UN DÉTAIL.", "brush_kw": "PAS UN DÉTAIL", "subtext": "Ne nourris pas les modèles publics avec les secrets confidentiels de ton entreprise."},
        {"num": "52", "headline": "RÉDIGER UN BON PROMPT C'EST STRUCTURER SA PENSÉE.", "brush_kw": "STRUCTURER SA PENSÉE", "subtext": "Si tu n'arrives pas à expliquer ton besoin à l'IA, c'est qu'il n'est pas clair dans ta tête."},
        {"num": "53", "headline": "L'IA PERMET D'EXÉCUTER DE MANIÈRE INDUSTRIELLE.", "brush_kw": "MANIÈRE INDUSTRIELLE", "subtext": "Mais le design, l'expérience utilisateur et l'esprit restent de l'artisanat humain."},
        {"num": "54", "headline": "NE CHERCHE PAS L'OUTIL PARFAIT. CHERCHE LE PROBLÈME.", "brush_kw": "CHERCHE LE PROBLÈME", "subtext": "L'IA est un moyen. La valeur que tu apportes au client reste l'unique priorité."},
        {"num": "55", "headline": "LES MEILLEURS PROMPTEURS SONT DE BONS COMMUNICANTS.", "brush_kw": "BONS COMMUNICANTS", "subtext": "Si tu sais expliquer un projet avec clarté à un humain, tu sauras piloter n'importe quelle IA."},
        {"num": "56", "headline": "L'IA TE LIBÈRE DES TÂCHES DE NIVEAU 1.", "brush_kw": "NIVEAU 1", "subtext": "Profites-en pour monter en compétences et passer au niveau 10 de ton domaine."},
        {"num": "57", "headline": "L'ÉTHIQUE N'EST PAS UNE OPTION DANS L'IA.", "brush_kw": "PAS UNE OPTION", "subtext": "Sois transparent sur l'utilisation des outils et garde une honnêteté intellectuelle totale."},
        {"num": "58", "headline": "L'IA EST UN MIROIR DE TES COMPÉTENCES.", "brush_kw": "MIROIR DE TES COMPÉTENCES", "subtext": "Elle reflète ta maîtrise. Un débutant aura un travail moyen, un pro aura un chef-d'œuvre."},
        {"num": "59", "headline": "L'AVENIR APPARTIENT AUX HYBRIDES.", "brush_kw": "AUX HYBRIDES", "subtext": "Ceux qui combinent expertise métier, psychologie humaine et maîtrise technologique."},
        {"num": "60", "headline": "STOP AU BLA BLA : CRÉE ET EXPÉRIMENTE.", "brush_kw": "CRÉE ET EXPÉRIMENTE", "subtext": "Les discours théoriques sur l'IA ne valent rien face à 10 minutes de pratique réelle."},
        {"num": "61", "headline": "L'IA NE RESSENT PAS LA DOULEUR DE TES CLIENTS.", "brush_kw": "PAS LA DOULEUR", "subtext": "Comprendre leurs frustrations profondes et leurs besoins réels reste ton rôle exclusif."},
        {"num": "62", "headline": "NE SOIS PAS SPECTATEUR DE LA RÉVOLUTION IA.", "brush_kw": "SPECTATEUR", "subtext": "Prends ta place sur le terrain dès maintenant. Les premiers arrivés fixent les règles."},
        {"num": "63", "headline": "L'IA N'A PAS DE CRÉDIBILITÉ. TOI SI.", "brush_kw": "CRÉDIBILITÉ", "subtext": "Les gens achètent ta réputation, ton expérience et la confiance que tu inspires."},
        {"num": "64", "headline": "FORMATTE TES PROMPTS COMME UN CAHIER DES CHARGES.", "brush_kw": "CAHIER DES CHARGES", "subtext": "Contexte, rôle, objectif, contraintes et format de sortie. La précision fait des miracles."},
        {"num": "65", "headline": "LA VRAIE FORCE DE L'IA C'EST DE TESTER 50 IDÉES EN 5 MIN.", "brush_kw": "TESTER 50 IDÉES", "subtext": "Utilise-la comme partenaire de brainstorming pour explorer des angles inédits."},
        {"num": "66", "headline": "L'IA NE REMPLACERA JAMAIS LA CHALEUR D'UNE RELATION.", "brush_kw": "CHALEUR D'UNE RELATION", "subtext": "Dans un monde automatisé, un appel téléphonique ou une vraie poignée de main devient du luxe."},
        {"num": "67", "headline": "PASSE DE L'ÉTAT D'EXÉCUTANT À CELUI DE DÉCIDEUR.", "brush_kw": "DÉCIDEUR", "subtext": "Laisse les tâches automatisables aux machines et concentre-toi sur les choix à fort impact."},
        {"num": "68", "headline": "SI TU N'UTILISES PAS L'IA, TES CONCURRENTS LE FONT DÉJÀ.", "brush_kw": "TES CONCURRENTS", "subtext": "La compétition s'accélère. Ne leur offre pas une avance de 10 longueurs."},
        {"num": "69", "headline": "L'IA EST UN LEVIER. TON AMBITION EST LE POINT D'APPUI.", "brush_kw": "TON AMBITION", "subtext": "Donne-toi la permission de viser 10 fois plus haut avec les outils d'aujourd'hui."}
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
    generate_40_quotes()
