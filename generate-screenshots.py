from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "public/images/portfolio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H = 800, 600

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def make_gradient(draw, c1, c2, y_start, y_end):
    c1 = hex_to_rgb(c1)
    c2 = hex_to_rgb(c2)
    for y in range(y_start, y_end):
        ratio = (y - y_start) / max(1, y_end - y_start)
        r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
        g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
        b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

def create_screenshot(cfg):
    img = Image.new("RGB", (W, H), hex_to_rgb("#0a0a0a"))
    draw = ImageDraw.Draw(img)

    # Background gradient
    make_gradient(draw, cfg["bg1"], cfg["bg2"], 32, H)

    # Browser bar
    draw.rectangle([0, 0, W, 32], fill=hex_to_rgb("#1a1a1a"))
    draw.ellipse([12, 10, 22, 20], fill=hex_to_rgb("#ff5f56"))
    draw.ellipse([30, 10, 40, 20], fill=hex_to_rgb("#ffbd2e"))
    draw.ellipse([48, 10, 58, 20], fill=hex_to_rgb("#27c93f"))
    draw.rounded_rectangle([72, 8, W-12, 24], radius=8, fill=hex_to_rgb("#0f0f0f"), outline=hex_to_rgb("#2a2a2a"))

    # Nav
    draw.rectangle([0, 32, W, 92], fill=hex_to_rgb(cfg["nav_bg"]))
    # Logo
    draw.rounded_rectangle([24, 44, 80, 80], radius=6, fill=hex_to_rgb(cfg["accent"]))
    draw.text((44, 52), "S", fill=hex_to_rgb("#0a0a0a"), font=cfg["font_large"])
    # Nav links
    links = ["Start", "O nas", "Oferta", "Kontakt"]
    x = 460
    for link in links:
        draw.text((x, 54), link, fill=hex_to_rgb(cfg["text_dim"]), font=cfg["font_small"])
        x += 80

    # Hero section
    hero_y = 140
    draw.text((W//2, hero_y), cfg["title"], fill=hex_to_rgb(cfg["text"]), font=cfg["font_title"], anchor="mm")
    draw.text((W//2, hero_y+50), cfg["subtitle"], fill=hex_to_rgb(cfg["text_dim"]), font=cfg["font_small"], anchor="mm")
    # CTA button
    btn_w, btn_h = 180, 40
    bx, by = (W-btn_w)//2, hero_y+90
    draw.rounded_rectangle([bx, by, bx+btn_w, by+btn_h], radius=20, fill=hex_to_rgb(cfg["accent"]))
    draw.text((W//2, by+btn_h//2), cfg["cta"], fill=hex_to_rgb("#0a0a0a"), font=cfg["font_small"], anchor="mm")

    # Content cards
    card_y = 340
    cards = cfg.get("cards", [])
    gap = 20
    card_w = (W - 80 - (len(cards)-1)*gap) // len(cards)
    for i, card in enumerate(cards):
        cx = 40 + i * (card_w + gap)
        draw.rounded_rectangle([cx, card_y, cx+card_w, card_y+140], radius=12, fill=hex_to_rgb(cfg["card_bg"]))
        # Card image placeholder
        draw.rounded_rectangle([cx+10, card_y+10, cx+card_w-10, card_y+70], radius=8, fill=hex_to_rgb(cfg["card_img"]))
        # Card title
        draw.text((cx+10, card_y+82), card["title"], fill=hex_to_rgb(cfg["text"]), font=cfg["font_small"])
        # Card desc lines
        draw.rounded_rectangle([cx+10, card_y+108, cx+card_w//2, card_y+118], radius=3, fill=hex_to_rgb(cfg["text_dim2"]))
        draw.rounded_rectangle([cx+10, card_y+126, cx+card_w//1.5, card_y+136], radius=3, fill=hex_to_rgb(cfg["text_dim2"]))

    # Footer
    draw.rectangle([0, H-50, W, H], fill=hex_to_rgb(cfg["nav_bg"]))
    draw.text((W//2, H-25), "© 2025  |  Wszelkie prawa zastrzeżone", fill=hex_to_rgb(cfg["text_dim"]), font=cfg["font_tiny"], anchor="mm")

    out = os.path.join(OUTPUT_DIR, cfg["filename"])
    img.save(out, "PNG")
    print(f"[OK] {cfg['filename']}")

# Load fonts
def load_font(size):
    paths = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

font_title = load_font(26)
font_large = load_font(20)
font_small = load_font(13)
font_tiny = load_font(11)

configs = [
    {
        "filename": "salon-glow.png",
        "title": "Salon Kosmetyczny Glow",
        "subtitle": "Profesjonalne zabiegi pielęgnacyjne",
        "cta": "Umów wizytę",
        "bg1": "#1a0a0a", "bg2": "#2d1515",
        "nav_bg": "#0f0a0a", "accent": "#e8b4b8",
        "text": "#f5e6e8", "text_dim": "#c4a5a8", "text_dim2": "#5a3a3e",
        "card_bg": "#1a1010", "card_img": "#3d2025",
        "cards": [{"title": "Zabiegi"}, {"title": "Cennik"}, {"title": "Galeria"}],
    },
    {
        "filename": "sklep-budowlany.png",
        "title": "Dach-Mur",
        "subtitle": "Materiały budowlane - dostawa w 24h",
        "cta": "Zobacz ofertę",
        "bg1": "#1a1205", "bg2": "#2d2310",
        "nav_bg": "#0f0c05", "accent": "#f0c040",
        "text": "#f5efe0", "text_dim": "#c4b898", "text_dim2": "#5a4a20",
        "card_bg": "#1a1608", "card_img": "#3d3515",
        "cards": [{"title": "Cegły"}, {"title": "Dachówki"}, {"title": "Farby"}],
    },
    {
        "filename": "kancelaria.png",
        "title": "Kancelaria Kowalski",
        "subtitle": "Prawo cywilne · Rodzinne · Gospodarcze",
        "cta": "Bezpłatna konsultacja",
        "bg1": "#0a0a1a", "bg2": "#15152d",
        "nav_bg": "#0a0a0f", "accent": "#8ab4f8",
        "text": "#e8ecf5", "text_dim": "#a5b4c4", "text_dim2": "#2a3a5a",
        "card_bg": "#10101a", "card_img": "#1a2a4a",
        "cards": [{"title": "Prawo cywilne"}, {"title": "Rozwody"}, {"title": "Firmy"}],
    },
    {
        "filename": "pizzeria.png",
        "title": "Pizzeria La Mamma",
        "subtitle": "Autentyczna włoska kuchnia od 2005",
        "cta": "Zamów online",
        "bg1": "#1a0a05", "bg2": "#2d1a10",
        "nav_bg": "#0f0805", "accent": "#ff8c42",
        "text": "#f5e8e0", "text_dim": "#c4a898", "text_dim2": "#5a3a20",
        "card_bg": "#1a1008", "card_img": "#3d2515",
        "cards": [{"title": "Pizza"}, {"title": "Makarony"}, {"title": "Sałatki"}],
    },
    {
        "filename": "transport.png",
        "title": "Speed-Trans",
        "subtitle": "Transport krajowy i międzynarodowy",
        "cta": "Wycena transportu",
        "bg1": "#051a0a", "bg2": "#102d1a",
        "nav_bg": "#050f0a", "accent": "#4ade80",
        "text": "#e0f5e8", "text_dim": "#98c4a8", "text_dim2": "#205a3a",
        "card_bg": "#081a10", "card_img": "#153d25",
        "cards": [{"title": "Krajowy"}, {"title": "Europa"}, {"title": "Magazyn"}],
    },
    {
        "filename": "fotografia.png",
        "title": "Studio Focus",
        "subtitle": "Fotografia ślubna · Biznesowa · Eventowa",
        "cta": "Zobacz portfolio",
        "bg1": "#12051a", "bg2": "#23102d",
        "nav_bg": "#0a050f", "accent": "#c084fc",
        "text": "#f0e8f5", "text_dim": "#b8a0c8", "text_dim2": "#4a205a",
        "card_bg": "#120818", "card_img": "#2a153d",
        "cards": [{"title": "Śluby"}, {"title": "Biznes"}, {"title": "Eventy"}],
    },
]

for c in configs:
    c["font_title"] = font_title
    c["font_large"] = font_large
    c["font_small"] = font_small
    c["font_tiny"] = font_tiny

for cfg in configs:
    create_screenshot(cfg)

print(f"\n✅ Zapisano w {OUTPUT_DIR}/")
