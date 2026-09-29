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

def generate_user_quotes():
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

    # The 9 quotes specified by user
    items = [
        {
            "num": "21",
            "headline": "L'IA NE PRENDRA PAS TON POSTE.",
            "brush_kw": "TON POSTE",
            "subtext": "C'est celui qui sait s'en servir qui le prendra."
        },
        {
            "num": "22",
            "headline": "UNE IA SANS CONTEXTE, C'EST UN STAGIAIRE BRILLANT...",
            "brush_kw": "STAGIAIRE BRILLANT",
            "subtext": "... à qui tu n'as absolument rien expliqué."
        },
        {
            "num": "23",
            "headline": "LA QUALITÉ DE TA RÉPONSE DÉPEND DE TA QUESTION.",
            "brush_kw": "DE TA QUESTION",
            "subtext": "La clarté de tes consignes détermine la valeur du résultat."
        },
        {
            "num": "24",
            "headline": "L'IA N'INVENTE PAS TON EXPERTISE.",
            "brush_kw": "TON EXPERTISE",
            "subtext": "Elle la démultiplie et accélère ton impact au quotidien."
        },
        {
            "num": "25",
            "headline": "L'IA N'EST NI COMPLIQUÉE NI MAGIQUE.",
            "brush_kw": "NI MAGIQUE",
            "subtext": "Ceux qui la disent compliquée ne l'ont jamais ouverte. Ceux qui la disent magique ne l'ont jamais testée sérieusement."
        },
        {
            "num": "26",
            "headline": "2H DE TRAVAIL, 10 MIN DE PROMPT BIEN CONSTRUIT.",
            "brush_kw": "PROMPT BIEN CONSTRUIT",
            "subtext": "Tout le reste de la valeur produite, c'est ton jugement."
        },
        {
            "num": "27",
            "headline": "L'IA NE PENSE PAS À TA PLACE.",
            "brush_kw": "À TA PLACE",
            "subtext": "Elle t'oblige à structurer et penser beaucoup plus clairement."
        },
        {
            "num": "28",
            "headline": "L'AFRIQUE N'A PAS BESOIN D'ATTENDRE L'IA.",
            "brush_kw": "D'ATTENDRE L'IA",
            "subtext": "Elle a besoin de gens formés et prêts à l'utiliser dès aujourd'hui."
        },
        {
            "num": "29",
            "headline": "VÉRIFIER CE QUE L'IA TE SORT N'EST PAS DE LA MÉFIANCE.",
            "brush_kw": "PROFESSIONNALISME",
            "subtext": "C'est la preuve ultime de ton professionnalisme et de ta rigueur."
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

        # Render Subtext + check if brush_kw is in subtext
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
        print(f"Generated User Quote #{item['num']}: {out_path}")

if __name__ == "__main__":
    generate_user_quotes()
