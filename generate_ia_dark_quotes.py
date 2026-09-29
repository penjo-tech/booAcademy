import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def draw_painter_brush_underline(draw_obj, start_x, end_x, y_pos, color=(255, 195, 0, 255), thickness=18, tilt=-5):
    """
    Draws an artistic painter brush stroke underline shifted below text with high color saturation.
    """
    # Shifted down slightly (+14px) for clear separation from text baseline
    y_start = y_pos + 14
    x1 = start_x - 16
    x2 = end_x + 18
    y1 = y_start
    y2 = y_start + tilt  # diagonal tilt angle
    
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

def generate_ia_dark_quotes_large_brush():
    target_dir = r"C:\Users\hp omen\Documents\DevProject\booAcademy\verites_ia_dark"
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

    # 10 Brutal Truths with targeted brush underline keywords
    truths = [
        {
            "num": "01",
            "tag": "DÉMYSTIFIER",
            "p1": "L'IA NE REMPLACERA PAS LES HUMAINS.",
            "brush_keyword": "REMPLACERA PAS",
            "p2": "Mais les humains qui utilisent l'IA remplaceront ceux qui l'ignorent."
        },
        {
            "num": "02",
            "tag": "DÉMYSTIFIER",
            "p1": "L'IA N'EST PAS INTELLIGENTE, ELLE EST RAPIDE.",
            "brush_keyword": "PAS INTELLIGENTE",
            "p2": "Sans la créativité et le jugement humain, elle ne produit que du bruit."
        },
        {
            "num": "03",
            "tag": "DÉMYSTIFIER",
            "p1": "L'IA NE RÉSOUDRA PAS UN PROBLÈME MAL POSÉ.",
            "brush_keyword": "MAL POSÉ",
            "p2": "Si votre stratégie est floue, l'IA accélérera simplement votre échec."
        },
        {
            "num": "04",
            "tag": "RASSURER",
            "p1": "LA VRAIE VALEUR DE DEMAIN :",
            "brush_keyword": "VRAIE VALEUR",
            "p2": "Ce n'est pas ce que vous savez faire, mais l'empathie et la vision que vous y apportez."
        },
        {
            "num": "05",
            "tag": "RASSURER",
            "p1": "L'IA AUTOMATISE LES TÂCHES RÉPÉTITIVES,",
            "brush_keyword": "RÉPÉTITIVES",
            "p2": "pas votre singularité. Elle vous libère du travail mécanique pour créer."
        },
        {
            "num": "06",
            "tag": "RASSURER",
            "p1": "PAS BESOIN D'ÊTRE DÉVELOPPEUR POUR DOMPTER L'IA.",
            "brush_keyword": "DÉVELOPPEUR",
            "p2": "La clarté d'esprit et la curiosité suffisent largement."
        },
        {
            "num": "07",
            "tag": "PROJETER",
            "p1": "ATTENDRE QUE L'IA SOIT PARFAITE EST UNE ERREUR.",
            "brush_keyword": "SOIT PARFAITE",
            "p2": "Vous serez dépassés par ceux qui l'adoptent déjà avec ses imperfections."
        },
        {
            "num": "08",
            "tag": "PROJETER",
            "p1": "L'IA EST UN MULTIPLICATEUR DE COMPÉTENCES :",
            "brush_keyword": "MULTIPLICATEUR",
            "p2": "Un expert devient surpuissant. Un amateur imprécis produit du travail médiocre."
        },
        {
            "num": "09",
            "tag": "PROJETER",
            "p1": "DANS 5 ANS, L'IA NE SERA PLUS UN AVANTAGE.",
            "brush_keyword": "NE SERA PLUS",
            "p2": "Ce sera le standard minimum obligatoire pour simplement exister dans votre secteur."
        },
        {
            "num": "10",
            "tag": "PASSER À L'ACTION",
            "p1": "ARRÊTEZ DE CRAINDRE L'IA ET DOMPTEZ-LA.",
            "brush_keyword": "DOMPTEZ-LA",
            "p2": "Votre plus grand risque n'est pas le progrès, mais votre propre immobilisme."
        }
    ]

    # COVER IMAGE (Slide 0)
    cover_img = Image.new("RGBA", (width, height), (12, 14, 18, 255))
    draw_c = ImageDraw.Draw(cover_img)

    font_cover_tag = ImageFont.truetype(font_path_bold, 30)
    font_cover_big1 = ImageFont.truetype(font_path_bold, 95)
    font_cover_big2 = ImageFont.truetype(font_path_bold, 105)
    font_cover_sub = ImageFont.truetype(font_path_reg, 36)

    # Top Tag
    draw_c.text((width // 2, 180), "INTELLIGENCE ARTIFICIELLE", font=font_cover_tag, fill=(240, 190, 40, 255), anchor="mm")
    
    # Gold accent line
    draw_c.line([(width//2 - 120, 220), (width//2 + 120, 220)], fill=(240, 190, 40, 255), width=4)

    # Big Title
    draw_c.text((width // 2, 370), "10 VÉRITÉS", font=font_cover_big1, fill=(255, 255, 255, 255), anchor="mm")
    
    # "BRUTALES" with Brush Stroke Underline
    bbox_brut = font_cover_big2.getbbox("BRUTALES")
    w_brut = bbox_brut[2] - bbox_brut[0]
    x_brut = (width - w_brut) // 2
    y_brut = 490
    
    draw_painter_brush_underline(draw_c, x_brut, x_brut + w_brut, y_brut + 105, color=(240, 190, 40, 255), thickness=22, tilt=-6)
    draw_c.text((width // 2, y_brut), "BRUTALES", font=font_cover_big2, fill=(255, 255, 255, 255), anchor="mm")
    
    # Subtitle
    draw_c.text((width // 2, 690), "Démystifier • Rassurer • Projeter", font=font_cover_sub, fill=(210, 210, 210, 255), anchor="mm")
    draw_c.text((width // 2, 850), "Glissez vers la gauche →", font=font_cover_tag, fill=(140, 140, 140, 255), anchor="mm")

    if logo_light:
        lw_l, lh_l = logo_light.size
        cover_img.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

    cover_path = os.path.join(target_dir, "verite_ia_00_cover.png")
    cover_img.save(cover_path, "PNG")
    print(f"Generated Cover: {cover_path}")

    # SLIDES 1 to 10
    for item in truths:
        img_slide = Image.new("RGBA", (width, height), (12, 14, 18, 255))
        draw_s = ImageDraw.Draw(img_slide)

        font_size = 64
        font_p1 = ImageFont.truetype(font_path_bold, font_size)
        font_p2 = ImageFont.truetype(font_path_reg, int(font_size * 0.85))

        lines_p1 = textwrap.wrap(item["p1"], width=20)
        lines_p2 = textwrap.wrap(item["p2"], width=24)

        lh_p1 = int(font_size * 1.3)
        lh_p2 = int(font_size * 0.85 * 1.3)

        h_p1 = len(lines_p1) * lh_p1
        h_p2 = len(lines_p2) * lh_p2
        spacing = 45

        total_h = h_p1 + spacing + h_p2
        start_y = 570 - (total_h // 2)

        # Draw P1 (Bold Headline) + Painter Brush Stroke Underline on target keyword
        curr_y = start_y
        for l in lines_p1:
            bbox = font_p1.getbbox(l)
            w_l = bbox[2] - bbox[0]
            start_x_line = (width - w_l) // 2
            
            # Check if brush keyword is in this line
            kw = item.get("brush_keyword", "")
            if kw and kw in l:
                # Find start and end pixel of keyword in line
                kw_offset_idx = l.index(kw)
                prefix = l[:kw_offset_idx]
                prefix_w = font_p1.getbbox(prefix)[2] - font_p1.getbbox(prefix)[0] if prefix else 0
                kw_w = font_p1.getbbox(kw)[2] - font_p1.getbbox(kw)[0]
                
                kw_start_x = start_x_line + prefix_w
                kw_end_x = kw_start_x + kw_w
                
                # Draw painter brush stroke underline (shifted below text baseline)
                draw_painter_brush_underline(draw_s, kw_start_x, kw_end_x, curr_y + font_size + 2, color=(255, 195, 0, 255), thickness=18, tilt=-5)

            draw_s.text((start_x_line, curr_y), l, fill=(255, 255, 255, 255), font=font_p1)
            curr_y += lh_p1

        curr_y += spacing

        # Draw P2 (Regular Detail)
        for l in lines_p2:
            bbox = font_p2.getbbox(l)
            w_l = bbox[2] - bbox[0]
            draw_s.text(((width - w_l) // 2, curr_y), l, fill=(210, 210, 210, 255), font=font_p2)
            curr_y += lh_p2

        # Paste Logo (Bottom Right Footer)
        if logo_light:
            lw_l, lh_l = logo_light.size
            img_slide.paste(logo_light, (width - lw_l - 70, height - lh_l - 70), logo_light)

        slide_path = os.path.join(target_dir, f"verite_ia_{item['num']}.png")
        img_slide.save(slide_path, "PNG")
        print(f"Generated Brush Slide: {slide_path}")

if __name__ == "__main__":
    generate_ia_dark_quotes_large_brush()
