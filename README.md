# SoloIT – Premium Freelance Website

Nowoczesna, statyczna strona internetowa zbudowana w [Astro](https://astro.build) z Tailwind CSS. 
Skoncentrowana na tworzeniu stron WWW (WordPress), automatyzacji procesów i serwisie IT z dojazdem na Śląsku.

🌐 **Live:** [https://soloit.pl](https://soloit.pl)

---

## 🚀 Technologie

- **Astro 6** – ultra-szybki generator stron statycznych
- **Tailwind CSS 4** – utility-first CSS
- **Decap CMS** – panel admina do zarządzania blogiem (`/admin/`)
- **TypeScript** – typowanie
- **Netlify** – hosting + CI/CD

---

## 📁 Struktura projektu

```
├── public/                  # Statyczne assety (favicon, logo, admin CMS)
├── src/
│   ├── components/          # Reużywalne komponenty Astro
│   ├── content/posts/       # Wpisy blogowe (Markdown)
│   ├── layouts/             # Layouty stron
│   ├── pages/               # Routing (Astro file-based)
│   └── styles/              # Globalne style + Tailwind
├── astro.config.mjs         # Konfiguracja Astro
├── netlify.toml             # Konfiguracja Netlify
└── content.config.ts        # Schema content collections
```

---

## 📝 Dodawanie wpisów na bloga

### Opcja 1: Decap CMS (najprostsza)
Wejdź na `https://soloit.pl/admin/`, zaloguj się i dodaj wpis przez panel graficzny.

### Opcja 2: Markdown w VS Code
Twórz pliki w `src/content/posts/nazwa-pliku.md`:

```md
---
title: "Tytuł wpisu"
description: "Opis SEO (max 200 znaków)"
pubDate: 2025-05-11
category: "Strony WWW"
tags: ["wordpress", "seo"]
featured: false
---

Tu piszesz treść w Markdownie.
```

---

## 🛠️ Lokalny development

```bash
# Instalacja zależności
npm install

# Serwer deweloperski (localhost:4321)
npm run dev

# Build produkcyjny
npm run build

# Preview buildu
npm run preview
```

---

## 📦 Deploy

Projekt automatycznie deployuje się na Netlify po każdym pushu do brancha `main` (GitHub → Netlify).

Ręczny deploy:
```bash
npm run build
# Wgraj zawartość folderu `dist/` na Netlify
```

---

## 📄 Licencja

Wszelkie prawa zastrzeżone © SoloIT.
