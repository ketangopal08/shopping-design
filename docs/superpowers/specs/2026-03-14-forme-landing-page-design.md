# Formé — Landing Page Design Spec

**Date:** 2026-03-14
**Project:** Formé E-commerce Landing Page
**Status:** Approved

---

## Overview

A single-page marketing/landing page for Formé, a minimalist 3D-printed daily-use objects shop. Clean white/grey layout, minimal sans-serif typography, and charcoal as the sole accent color. The design follows the structure: Nav → Hero → Categories → Featured Products → Articles → Testimonials → Newsletter → Footer.

---

## Brand

| Property | Value |
|---|---|
| Shop name | Formé |
| Tagline | "Designed for daily life" |
| Accent color | Charcoal `#2D2D2D` |
| Background | White `#FFFFFF` |
| Section alt bg | Light grey `#FAFAFA` (hero, products, testimonials) |
| Section alt bg 2 | Soft grey `#F5F5F5` (newsletter, category tiles) |
| Body text | Dark `#1A1A1A` |
| Muted text | Grey `#888888` |
| Soft text | `#444444` (testimonial quote body, slightly softer than body) |
| Border/divider | `#EEEEEE` |
| Footer bg | `#1A1A1A` (intentionally darker than `#2D2D2D` to create depth) |

### Accent Color Application
`#2D2D2D` is used on:
- Primary CTA buttons (filled background)
- Subscribe button
- Active nav link underline
- Price text on product cards
- Footer link hover state

### Typography

| Element | Size | Weight | Transform |
|---|---|---|---|
| Logo | 16px | 700 | Uppercase, letter-spacing 3px |
| Hero headline | 52px | 700 | Normal |
| Section heading (h2) | 28px | 700 | Normal |
| Product name | 14px | 600 | Normal |
| Nav links | 13px | 400 | Normal |
| Body text | 13px | 400 | Normal |
| Article title | 14px | 600 | Normal |
| Tag / label | 10px | 600 | Uppercase, letter-spacing 2px |
| Price | 14px | 700 | Normal |
| Button label | 11px | 600 | Uppercase, letter-spacing 1.5px |
| Footer links | 12px | 400 | Normal |

Font: `Inter`, fallback `system-ui, -apple-system, sans-serif`. Load from Google Fonts with `font-display: swap`.

Default `line-height`: `1.5` for all body text, nav links, footer links, and product names unless otherwise specified.

---

## Tech Stack

- Plain HTML + CSS + minimal vanilla JS (no framework)
- Single `index.html` with an embedded `<style>` block
- No build step — open in browser directly
- Google Fonts CDN for Inter

### Required `<head>` block
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Formé — Designed for daily life</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

### Icons
- No external icon library. Use the following inline SVG snippets:
  - **Search**: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`
  - **Cart**: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 01-8 0"/></svg>`
  - **Instagram**: `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.5" fill="currentColor"/></svg>`
  - **Pinterest**: `<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.373 0 0 5.373 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738a.36.36 0 01.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.632-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0z"/></svg>`
  - **X (Twitter)**: `<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>`

- Placeholder `<img>` tags with explicit `width`, `height`, and descriptive `alt` attributes

---

## Layout Container

- Max content width: `1200px`, centered with `margin: 0 auto`
- Horizontal padding: `24px` on each side
- Full-bleed background colors extend edge-to-edge; content stays within the container

---

## Page Sections

### 1. Navigation

- Height: `64px`
- Sticky, `position: sticky; top: 0; z-index: 100`
- Background: white, `border-bottom: 1px solid #EEEEEE`
- Left: Logo — "FORMÉ" `16px / 700 / uppercase / letter-spacing 3px`
- Center: Links — Shop · About · Blog (`13px / 400`, hover: underline in `#2D2D2D`)
- Right: Search icon + Cart icon (`20px`, cursor pointer)
- No hamburger menu on mobile in this spec — nav links and search icon collapse to hidden at `< 768px`; only logo + cart icon shown

### 2. Hero

- Min-height: `90vh`
- Background: `#FAFAFA`
- Two-column flex layout (no gap, columns split `55% / 45%`)
- Left column (55%):
  - Tag: "New Collection" — `10px / 600 / uppercase / letter-spacing 2px / color #888`
  - Headline: "Designed<br>for daily life." — `52px / 700 / line-height 1.1`
  - Vertical gap: `24px` between tag → headline → button
  - CTA button: "SHOP NOW" — charcoal fill `#2D2D2D`, white text, `border-radius: 4px`, `padding: 12px 28px`
- Right column (45%):
  - `<img>` placeholder, aspect ratio `4:5` (portrait), `alt="Hero product — 3D printed desk object"`
  - Image fills the column height, `object-fit: cover`
- On mobile (`< 768px`): stack vertically, image above text, image becomes `16:9`

### 3. Browse by Category

- Background: white
- Section padding: `60px 0`
- Section heading: "Browse by category" — `28px / 700 / left-aligned`
- Heading bottom margin: `32px`
- 5 tiles using CSS Grid with `grid-template-columns: repeat(6, 1fr)`:
  - Row 1 (3 tiles): each tile `grid-column: span 2`
  - Row 2 (2 tiles, centered): first tile `grid-column: 2 / span 2`, second tile `grid-column: 4 / span 2`
  - `gap: 16px`
- Each tile: rounded card `border-radius: 12px`, background `#F5F5F5`, `padding: 20px`, `cursor: pointer`
  - Image placeholder: `aspect-ratio: 1`, `background: #E0E0E0`, `border-radius: 8px`, `alt="[Category name] — 3D printed objects"`
  - Label: category name `12px / 600 / center-aligned`, `margin-top: 10px`
  - Hover: `background: #EEEEEE`, smooth `transition: background 0.2s`
- All card/tile links use `href="#"` as placeholder
- Categories in order: Desk Organizers · Phone Stands · Cable Clips · Planters · Kitchen Tools

### 4. Featured Products

- Background: `#FAFAFA`
- Section padding: `60px 0`
- Section heading: "Featured products" — `28px / 700 / left-aligned`
- Subtext: "Trending this week" — `13px / 400 / color #888 / margin-top: 6px`
- Heading block bottom margin: `32px`
- 2×2 CSS Grid, `gap: 16px`
- Each product card: white background, `border-radius: 12px`, overflow hidden
  - Image: `aspect-ratio: 1`, `alt="[Product name]"`, `background: #F0F0F0`
  - Info row: product name (`14px / 600`) + price (`14px / 700 / #2D2D2D`), `padding: 12px 16px`
  - Hover: `box-shadow: 0 8px 24px rgba(0,0,0,0.08)`, `transform: translateY(-2px)`, `transition: 0.2s`
- Products:
  1. Minimal Desk Tray · $24.00
  2. Cable Clip Set · $12.00
  3. Phone Stand · $18.00
  4. Mini Planter · $16.00

### 5. Articles

- Background: white
- Section padding: `60px 0`
- Section heading: "Explore our articles" — `28px / 700 / left-aligned`
- Subtext: "Tips, ideas & updates" — `13px / 400 / color #888 / margin-top: 6px`
- Heading block bottom margin: `32px`
- 3-column CSS Grid, `gap: 20px`
- Each article card:
  - Image: `aspect-ratio: 4:3`, `border-radius: 10px`, `background: #E8E8E8`, `alt="Article: [title]"`
  - Tag: `10px / 600 / uppercase / letter-spacing 2px / color #888`, `margin-top: 10px`
  - Title: `14px / 600 / line-height 1.4`
  - "Read more →" link: `12px / #888`, hover: `color: #2D2D2D`
- Articles:
  1. Tag: Design · "How we design for daily use"
  2. Tag: Materials · "The filaments we use & why"
  3. Tag: Ideas · "Organise your desk in 5 steps"

### 6. Testimonials

- Background: `#FAFAFA`
- Section padding: `60px 0`
- Section heading: "What customers are saying" — `28px / 700 / left-aligned`
- Heading bottom margin: `32px`
- 2-column flex row, `gap: 16px`, `align-items: stretch`
- Each card: white background, `border-radius: 12px`, `padding: 24px`
  - Large opening quote mark: `"` — `48px / 700 / color #EEEEEE`
  - Quote text: `14px / 400 / line-height 1.6 / color #444`
  - Author row: `width: 36px height: 36px` circular avatar placeholder + name (`13px / 600`) + handle (`12px / color #888`)
  - Star rating: 5 filled stars rendered as `★★★★★` in `#2D2D2D`, `font-size: 12px`
- Testimonials:
  1. "Beautifully crafted. Exactly what my desk needed." — Sarah K. · @sarahk
  2. "Fast shipping, perfect quality. Will order again." — James R. · @james_r

### 7. Newsletter

- Background: `#F5F5F5`
- Section padding: `60px 0`
- Centered text layout, max-width `480px` centered
- Heading: "Subscribe & get 15% off" — `28px / 700 / center-aligned`
- Subtext: "Join the Formé community" — `14px / color #888 / center-aligned / margin-top: 8px / margin-bottom: 24px`
- Inline form: `display: flex`, `gap: 8px`
  - Email input: `flex: 1`, `border: 1px solid #DDDDDD`, `border-radius: 4px`, `padding: 12px 16px`, `font-size: 13px`
  - Submit button: "SUBSCRIBE" — charcoal fill, `border-radius: 4px`, `padding: 12px 24px`
- On submit: prevent default, replace form with success message: "You're in! Check your inbox." (`14px / color #2D2D2D`)
- Client-side validation: if email field is empty or not a valid email format (`/\S+@\S+\.\S+/`), add `border-color: red` to input and show inline error below the form: "Please enter a valid email." (`12px / color: red`). Error clears on next `input` event (i.e., as soon as the user starts typing again). No backend required.
- On mobile: form becomes `flex-direction: column`; button becomes `width: 100%`
- On mobile: CTA "SHOP NOW" button in Hero is `width: auto` (left-aligned, not full-width)

### 8. Footer

- Background: `#1A1A1A`
- Top row (`padding: 48px 0 32px`):
  - Left: FORMÉ logo in white, `16px / 700 / letter-spacing 3px`
  - Right: Two link columns
    - **Shop**: All Products · Categories · New In
    - **Info**: About · Blog · Contact
  - Links: `12px / color #888`, hover: `color: white`
- Social icons row (below logo): Instagram · Pinterest · X — rendered as simple SVG inline icons, `20px`, `color: #555`, hover: `color: white`
- Bottom bar: `border-top: 1px solid #2A2A2A`, `padding-top: 16px`
  - "© 2026 Formé · All rights reserved" — `11px / color #555`

---

## Responsive Behaviour

| Breakpoint | Behaviour |
|---|---|
| `>= 1200px` | Full layout as described |
| `768px – 1199px` | Category grid: `grid-template-columns: repeat(4, 1fr)`, tiles reflow as 2+2+1 (last tile centered via `grid-column: 2 / span 2`); product grid: 2×2 stays; articles: 2 columns; testimonials: 2 columns (unchanged); hero: 50/50 split |
| `< 768px` | Nav: logo + cart only (no links, no search icon); Hero: image stacks above text, headline `32px`; categories: `grid-template-columns: repeat(2, 1fr)`, all 5 tiles flow naturally (last tile left-aligned); products: 2 columns; articles: 1 column; testimonials: 1 column; newsletter form: stacked vertically, button `width: 100%` |

---

## Placeholder Image Strategy

| Location | Aspect Ratio | Alt text |
|---|---|---|
| Hero product | 4:5 | "Hero product — 3D printed desk object" |
| Category tile | 1:1 | "[Category name] — 3D printed objects" |
| Product card | 1:1 | "[Product name]" |
| Article card | 4:3 | "Article: [title]" |
| Testimonial avatar | 1:1 (36×36) | "[Name]'s avatar" |

Placeholders use `background: #E0E0E0` divs until real images are provided. All `<img>` tags use explicit `width` and `height` attributes to prevent layout shift.

---

## Accessibility & Interaction States

- All interactive elements (buttons, links, inputs) must have `:focus-visible { outline: 2px solid #2D2D2D; outline-offset: 2px; }` for keyboard accessibility
- All clickable tiles and cards must have `cursor: pointer`
- All links (nav, footer, article "Read more", category tiles) use `href="#"` as placeholder href

---

## Out of Scope

- No cart functionality or cart page
- No product detail pages
- No checkout flow
- No CMS, backend, or database
- No animations beyond CSS hover transitions
- No hamburger menu open/close state (mobile nav shows logo + cart only)
- No third-party analytics or tracking scripts
