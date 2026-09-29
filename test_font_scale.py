from PIL import Image, ImageDraw, ImageFont

font_bold = 'C:/Windows/Fonts/GOTHICB.TTF'
font_reg = 'C:/Windows/Fonts/GOTHIC.TTF'

quotes = [
    "L'IA ne remplacera pas les humains.\nMais les humains qui utilisent l'IA\nremplaceront ceux qui l'ignorent.",
    "L'IA n'est pas intelligente, elle est rapide.\nSans la créativité et le jugement humain,\nelle ne produit que du bruit.",
    "L'IA ne résoudra pas un problème mal posé.\nSi votre stratégie est floue, l'IA accélérera\nsimplement votre échec."
]

for i, q in enumerate(quotes):
    lines = [l for l in q.split('\n') if l.strip()]
    for sz in [60, 68, 76]:
        f = ImageFont.truetype(font_reg, sz)
        widths = [f.getbbox(l)[2] - f.getbbox(l)[0] for l in lines]
        h = len(lines) * (sz * 1.35)
        print(f"Quote {i+1} @ {sz}px -> max_w: {max(widths):.0f}px, total_h: {h:.0f}px")
