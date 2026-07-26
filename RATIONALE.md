# Chilling-potato — Design Rationale

A warm-grounded dark Neovim colorscheme. Colors are defined in the
perceptually uniform [HSLuv](https://www.hsluv.org/) color space.
The palette satisfies a set of explicit design constraints.
It's what I would call mathematically elegant!

HSLuv is the foundation that makes it possible.
It transforms sRGB into a space where equal
coordinate changes produce equal perceived differences.


## Palette

| Role | Hex | HSLuv (H°/S%/L%) |
|------|-----|-------------------|
| bg | `#1d1b1a` | 30/5/10 |
| fg | `#d2cbc6` | 42/10/82 |
| comment | `#656871` | 255/8/44 |
| keyword | `#9599bc` | 262/32/64 |
| operator | `#7787a2` | 248/28/56 |
| func | `#8cb4c1` | 216/40/71 |
| field | `#839e9c` | 188/28/63 |
| string | `#85a781` | 124/32/65 |
| type | `#cca386` | 42/38/70 |
| number | `#bc8373` | 26/36/60 |
| parameter | `#bc8373` | 26/36/60 |
| attribute | `#c38a88` | 14/32/63 |
| constant | `#c294a5` | 346/30/66 |
| error | `#c17f84` | 8/34/60 |
| warn | `#ba9077` | 38/38/63 |
| info | `#7f989b` | 202/28/61 |
| ok | `#839c86` | 132/22/62 |

## Design constraints

A good colorscheme for reading code should satisfy these properties.
All constraint numbers are measurable in HSLuv against the palette above.

### Constraint 1 — Adjacency separation

Tokens that frequently appear next to each other in code must be separated
by at least 30° in hue. Rare adjacencies may be closer.

Rationale: when your eye scans `def foo()`, the keyword `def` and the
function name `foo` sit adjacent. If they share a similar hue, your visual
system must work harder to discriminate them.
I actually don't have any scientific paper to back this up but you can trust me because I spend a lot of time in front of my computer. AKA trust me bro metrics.


### Constraint 2 — Luminance hierarchy

Visual weight must match code scanning patterns: you first look for *what*
(types, functions), then *how* (keywords), then the *data* (strings, numbers).
So the definition is always the brightest. At a glance, you know what you're
looking at.

```
fg             L=82  highest  primary text
func           L=71           "what does it do?"
type           L=70           "what am I working with?"
constant       L=66           important values
string         L=65           data content
keyword        L=64           structural words
field          L=63           member access
attribute      L=63           annotations
number         L=60           literal values
error          L=60           diagnostics
operator       L=56  lowest   syntax glue
comment        L=44           intentionally dim
bg             L=10           background
```

### Constraint 3 — Contrast floor

Foreground must achieve WCAG (Web Content Accessibility Guidelines) AAA contrast (≥7:1) against background.

All syntax accents must achieve at least AA (≥4.5:1).
Comments are exempt! People don't write any, and we don't read them anyway.


Rationale: high contrast is necessary for legibility, but pure white
(#FFFFFF at L=100) on pure black creates halation, which is a complex way to say it hurts my eyes.
The warm cream foreground at L=82 achieves AAA (10.7:1) without glare.

### Constraint 4 — Saturation ceiling

No accent color may exceed 40% saturation in HSLuv.

Honestly... why not. I don't have a good way to justify this.
The palette uses 22–40% saturation, mean 27.6%.

### Constraint 5 — Temperature cycle

The palette must alternate warm → cool → warm across the color wheel
to prevent visual system adaptation to a single color temperature.
(POV: you've used Vim's `:colorscheme Blue` once)

Rationale: monochrome themes (all-blue, all-warm) cause cone fatigue
because one set of retinal cells works constantly while others idle.

The palette's warm background (30°) → cool structural accents
(124–262°) → warm highlights (8–42°) creates a cycle that engages
all three cone types.

## Constraint verification

Every constraint is verified against the palette above. The following
table checks Constraint 1 for each token pair:

| Pair | Freq | HSLuv gap | Satisfies ≥30°? |
|------|------|-----------|------------------|
| keyword ↔ func | 10 | 46° | ✓ |
| func ↔ parameter | 7 | 170° | ✓ |
| attribute ↔ func | 4 | 158° | ✓ |
| keyword ↔ type | 6 | 140° | ✓ |
| number ↔ operator | 5 | 138° | ✓ |
| keyword ↔ constant | 4 | 84° | ✓ |
| type ↔ number | 5 | 16° | ~ (same category) |
| keyword ↔ operator | 5 | 14° | ~ (same category) |

The two pairs below 30° are intentional: types and numbers are both
"values" and benefit from visual grouping; keywords and operators are
both "structure." Every high-frequency pair (≥5) that crosses semantic
categories has a gap ≥ 46°.

Constraint 3 is verified by WCAG contrast computation (see script below):

| Role | Contrast | WCAG |
|------|----------|------|
| fg | **10.7:1** | AAA |
| func | 7.7:1 | AAA |
| type | 7.5:1 | AAA |
| constant | 6.6:1 | AA |
| string | 6.4:1 | AA |
| keyword | 6.2:1 | AA |
| field | 6.0:1 | AA |
| number | 5.4:1 | AA |
| error | 5.4:1 | AA |
| operator | 4.7:1 | AA |
| comment | 3.1:1 | exempt |

Constraint 4: saturation range is 5–40%, mean 27.6%. All accents are
at or below 40%, well within the safe zone where chromatic aberration
becomes negligible.

