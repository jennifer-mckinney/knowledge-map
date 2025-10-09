# UI Specifications Document
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Purpose:** Complete design specifications for Figma/Canva implementation

---

## Design System

### Typography

**Font Family:**
```
Primary: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif
Monospace: "SF Mono", Monaco, Consolas, monospace
```

**Type Scale:**
```
Display Large:    32px / 600 weight / 1.2 line-height
Display Medium:   24px / 600 weight / 1.3 line-height
Heading 1:        18px / 600 weight / 1.4 line-height
Heading 2:        16px / 600 weight / 1.4 line-height
Heading 3:        14px / 600 weight / 1.4 line-height
Body Large:       16px / 400 weight / 1.6 line-height
Body Regular:     14px / 400 weight / 1.6 line-height
Body Small:       13px / 400 weight / 1.5 line-height
Caption:          12px / 500 weight / 1.4 line-height
Label:            11px / 600 weight / 1.3 line-height
Label Small:      10px / 600 weight / 1.2 line-height
```

**Letter Spacing:**
```
Labels (uppercase): +0.5px
Body text: 0px
Headlines: -0.2px
```

---

### Color Palette

#### Light Theme (Default)

**Surfaces:**
```
Background:       #FAFAFA
Surface:          rgba(255, 255, 255, 0.98)
Surface Elevated: #FFFFFF
Border:           #E1E8ED
Border Subtle:    #F0F0F0
Divider:          #E8E8E8
```

**Text:**
```
Primary:          #14171A
Secondary:        #657786
Tertiary:         #8899A6
Disabled:         #AAB8C2
Inverse:          #FFFFFF
```

**Accent:**
```
Primary:          #4A90A4
Primary Hover:    #3A7A94
Primary Active:   #2C5A70
Primary Light:    rgba(74, 144, 164, 0.15)
Primary Ghost:    rgba(74, 144, 164, 0.08)
```

**Status:**
```
Success:          #22C55E
Success Light:    rgba(34, 197, 94, 0.15)
Warning:          #F59E0B
Warning Light:    rgba(245, 158, 11, 0.15)
Error:            #EF4444
Error Light:      rgba(239, 68, 68, 0.15)
Info:             #3B82F6
Info Light:       rgba(59, 130, 246, 0.15)
```

**Cluster Colors (Graph Nodes):**
```
System:           #6366F1  (Indigo)
Education:        #4ECDC4  (Turquoise)
Professional:     #45B7D1  (Sky Blue)
Technical:        #96CEB4  (Sage Green)
Research:         #85C1E9  (Light Blue)
Analysis:         #F59E0B  (Amber)
Admin:            #A78BFA  (Purple)
Archive:          #94A3B8  (Gray)
```

#### Dark Theme

**Surfaces:**
```
Background:       #14171A
Surface:          rgba(32, 35, 39, 0.98)
Surface Elevated: #202327
Border:           #3D4043
Border Subtle:    #2A2D31
Divider:          #38393D
```

**Text:**
```
Primary:          #F7F9FA
Secondary:        #8899A6
Tertiary:         #6B7785
Disabled:         #4A5561
Inverse:          #14171A
```

**Accent:**
```
Primary:          #6EB3C7
Primary Hover:    #8EC4D6
Primary Active:   #A8D4E1
Primary Light:    rgba(110, 179, 199, 0.2)
Primary Ghost:    rgba(110, 179, 199, 0.1)
```

**Cluster Colors (Dark Mode - Adjusted):**
```
System:           #7C7FF2  (Lighter Indigo)
Education:        #5EDDD4  (Brighter Turquoise)
Professional:     #55C7E1  (Brighter Sky Blue)
Technical:        #A6DEC4  (Lighter Sage)
Research:         #95D1F9  (Brighter Blue)
Analysis:         #FFA726  (Brighter Amber)
Admin:            #B79CFA  (Lighter Purple)
Archive:          #A4B3C8  (Lighter Gray)
```

---

### Spacing System

**Base Unit:** 4px

**Spacing Scale:**
```
xs:     4px   (0.25rem)
sm:     8px   (0.5rem)
md:     12px  (0.75rem)
lg:     16px  (1rem)
xl:     20px  (1.25rem)
2xl:    24px  (1.5rem)
3xl:    32px  (2rem)
4xl:    40px  (2.5rem)
5xl:    48px  (3rem)
6xl:    64px  (4rem)
```

**Component Spacing:**
```
Between elements in group:     8px
Between groups:                16px
Section padding:               20px
Panel padding:                 16px
Card padding:                  12px
Button padding:                8px 16px
Input padding:                 10px 12px
```

---

### Border Radius

```
None:      0px
Small:     4px   (chips, tags, small buttons)
Medium:    6px   (buttons, inputs, cards)
Large:     8px   (panels, modals)
XL:        12px  (large panels, drawers)
Round:     50%   (circular elements, avatars)
```

---

### Shadows

**Light Theme:**
```
sm:     0 1px 2px rgba(0, 0, 0, 0.05)
md:     0 2px 8px rgba(0, 0, 0, 0.1)
lg:     0 4px 20px rgba(0, 0, 0, 0.15)
xl:     0 10px 40px rgba(0, 0, 0, 0.2)
focus:  0 0 0 3px rgba(74, 144, 164, 0.1)
```

**Dark Theme:**
```
sm:     0 1px 2px rgba(0, 0, 0, 0.3)
md:     0 2px 8px rgba(0, 0, 0, 0.4)
lg:     0 4px 20px rgba(0, 0, 0, 0.5)
xl:     0 10px 40px rgba(0, 0, 0, 0.6)
focus:  0 0 0 3px rgba(110, 179, 199, 0.2)
```

---

## Page Layouts

### 1. Main Graph View (`/`)

**Viewport:** 1440px × 900px (reference size)

**Layout Structure:**
```
┌─────────────────────────────────────────────────────────────┐
│ NAV BAR (50px height)                                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                                                             │
│                     GRAPH CANVAS                            │
│                  (calc(100vh - 90px))                       │
│                                                             │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ LEGEND BAR (40px height)                                    │
└─────────────────────────────────────────────────────────────┘
```

**Floating Elements:**
- Insights Panel: Bottom left, 20px from edge
- Tooltips: Follow mouse cursor

---

### Navigation Bar Specifications

**Dimensions:**
```
Height:            50px
Padding:           0 30px
Background:        var(--surface)
Border bottom:     1px solid var(--border)
Backdrop filter:   blur(10px)
Position:          Fixed, top: 0, z-index: 1000
```

**Layout Grid:**
```
┌─────────────────────────────────────────────────────────────┐
│  [Brand]           [Nav Links]                [Theme]       │
│  30px              Center-aligned              30px         │
└─────────────────────────────────────────────────────────────┘
```

**Brand (Left Section):**
```
Text: "Knowledge Map"
Font: 16px / 600 weight
Color: var(--text-primary)
Left padding: 0px
```

**Nav Links (Center Section):**
```
Container:
  Display: flex
  Gap: 30px
  Justify: center
  Align: center

Each Link:
  Font: 14px / 500 weight
  Color: var(--text-secondary)
  Padding: 8px 12px
  Border radius: 6px
  Transition: all 0.2s ease

Hover State:
  Color: var(--accent-primary)
  Background: var(--primary-ghost)

Active State:
  Color: var(--accent-primary)
  Background: var(--primary-light)
```

**Theme Toggle (Right Section):**
```
Button:
  Width: 36px
  Height: 36px
  Background: none
  Border: none
  Border radius: 6px
  Font size: 20px
  Cursor: pointer
  Transition: background 0.2s ease

Hover:
  Background: var(--primary-ghost)

Icon:
  🌙 (moon) for light mode
  ☀️ (sun) for dark mode
```

---

### Legend Bar Specifications

**Dimensions:**
```
Height:            40px
Padding:           0 20px
Background:        var(--surface)
Border top:        1px solid var(--border)
Position:          Fixed, bottom: 0, z-index: 1000
Display:           flex
Align:             center
Gap:               20px
Overflow-x:        auto (horizontal scroll if needed)
```

**Legend Item:**
```
Container:
  Display: flex
  Align: center
  Gap: 8px
  Padding: 4px 8px
  Border radius: 6px
  Cursor: pointer
  Transition: opacity 0.2s ease
  White-space: nowrap

Color Circle:
  Width: 12px
  Height: 12px
  Border radius: 50%
  Background: [cluster color]
  Border: 1px solid rgba(255, 255, 255, 0.8) (light theme)
  Border: 1px solid rgba(0, 0, 0, 0.3) (dark theme)

Label:
  Font: 11px / 500 weight
  Color: var(--text-primary)

Hover:
  Opacity: 0.7

Active (filtered):
  Opacity: 0.5
  Background: var(--primary-ghost)
```

---

### Insights Panel Specifications

**Dimensions:**
```
Width:             280px
Max-width:         90vw (mobile)
Background:        var(--surface)
Border:            1px solid var(--border)
Border radius:     12px
Padding:           16px
Box shadow:        0 4px 20px rgba(0, 0, 0, 0.1)
Position:          Fixed
Bottom:            80px (above legend)
Left:              20px
Z-index:           1000
```

**Animation:**
```
Animation: fadeIn 0.5s ease 0.5s both

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Header:**
```
Display:           flex
Align:             center
Gap:               8px
Margin bottom:     12px
Padding bottom:    10px
Border bottom:     1px solid var(--border)

Icon:
  Font size: 18px

Title:
  Font: 13px / 600 weight
  Color: var(--text-primary)
  Text transform: uppercase
  Letter spacing: 0.5px
```

**Content:**
```
Font: 13px / 400 weight
Line height: 1.6
Color: var(--text-secondary)
```

**Insight Item:**
```
Margin: 8px 0
Padding: 8px
Background: var(--primary-ghost)
Border radius: 6px
Border left: 3px solid var(--accent-primary)
```

**Highlight Text:**
```
Color: var(--accent-primary)
Font weight: 600
```

---

### Graph Canvas Specifications

**Dimensions:**
```
Width:             100vw
Height:            calc(100vh - 90px)  /* Viewport minus nav (50px) and legend (40px) */
Background:        var(--background)
Position:          relative
```

**SVG Container:**
```
Width:             100%
Height:            100%
Background:        var(--background)
Cursor:            grab (default)
Cursor:            grabbing (when dragging)
```

**Graph Nodes (Circles):**
```
Radius:            8px - 40px (based on file count)
Fill:              [cluster color] or white (for folder types)
Stroke:            [cluster color]
Stroke width:      2px (default)
Stroke width:      3px (hover)
Stroke width:      4px (highlighted)
Cursor:            pointer
Transition:        all 0.2s ease

Hover Effect:
  Stroke width: 3px
  Filter: brightness(1.1)

Highlighted State:
  Stroke width: 4px
  Stroke: #2C5AA0
  Filter: drop-shadow(0 0 6px rgba(44, 90, 160, 0.4))

Dimmed State:
  Opacity: 0.3
```

**Graph Edges (Lines):**
```
Stroke:            var(--text-secondary)
Stroke opacity:    0.3 (default)
Stroke width:      1px (default)
Transition:        all 0.2s ease
Pointer events:    stroke

Hover:
  Stroke: var(--accent-primary)
  Stroke opacity: 0.9
  Stroke width: 3px

Highlighted:
  Stroke: var(--accent-primary)
  Stroke opacity: 0.8
  Stroke width: 2.5px
```

**Node Labels:**
```
Font: 10px / 500 weight
Fill: var(--text-primary)
Text anchor: middle
Pointer events: none
Opacity: 0.9

Category Labels (larger nodes):
  Font: 12px / 600 weight

Dimmed:
  Opacity: 0.2
```

**Cluster Backgrounds (Convex Hulls):**
```
Fill: [cluster color]
Opacity: 0.15 (light theme)
Opacity: 0.12 (dark theme)
Transition: opacity 0.3s ease

Hover:
  Opacity: 0.25
```

---

### Tooltip Specifications

**Node Tooltip:**
```
Dimensions:
  Padding: 12px 16px
  Max-width: 280px
  Background: rgba(20, 23, 26, 0.95) (light theme)
  Background: rgba(248, 249, 250, 0.95) (dark theme)
  Color: #FFFFFF (light theme)
  Color: #14171A (dark theme)
  Border radius: 8px
  Font: 13px / 400 weight
  Line height: 1.4
  Box shadow: 0 4px 12px rgba(0, 0, 0, 0.3)
  Position: absolute
  Z-index: 2100
  Pointer events: none

Animation:
  Opacity: 0 (hidden)
  Opacity: 1 (visible)
  Transition: opacity 0.2s ease
```

**Tooltip Header:**
```
Font: 14px / 600 weight
Margin bottom: 8px
Padding bottom: 6px
Border bottom: 1px solid rgba(255, 255, 255, 0.2) (light theme)
Border bottom: 1px solid rgba(20, 23, 26, 0.2) (dark theme)
```

**Tooltip Row:**
```
Display: flex
Justify content: space-between
Margin: 4px 0
Font: 12px

Label:
  Color: rgba(255, 255, 255, 0.7) (light theme)
  Color: rgba(20, 23, 26, 0.7) (dark theme)

Value:
  Font weight: 500
```

---

## Component Library

### Button Specifications

**Primary Button:**
```
Dimensions:
  Height: 36px
  Padding: 8px 16px
  Border radius: 6px
  Font: 14px / 500 weight

Colors:
  Background: var(--accent-primary)
  Color: #FFFFFF
  Border: none

Hover:
  Background: var(--accent-hover)
  Transform: translateY(-1px)
  Box shadow: 0 2px 8px rgba(74, 144, 164, 0.3)

Active:
  Background: var(--accent-active)
  Transform: translateY(0)

Disabled:
  Background: var(--disabled)
  Cursor: not-allowed
  Opacity: 0.6
```

**Secondary Button:**
```
Same dimensions as primary

Colors:
  Background: var(--surface)
  Color: var(--accent-primary)
  Border: 1px solid var(--border)

Hover:
  Background: var(--primary-ghost)
  Border color: var(--accent-primary)
```

**Ghost Button:**
```
Same dimensions as primary

Colors:
  Background: transparent
  Color: var(--accent-primary)
  Border: none

Hover:
  Background: var(--primary-ghost)
```

**Icon Button:**
```
Dimensions:
  Width: 36px
  Height: 36px
  Padding: 8px
  Border radius: 6px

Colors:
  Background: transparent
  Color: var(--text-secondary)

Hover:
  Background: var(--primary-ghost)
  Color: var(--accent-primary)
```

---

### Input/Search Field

```
Dimensions:
  Height: 40px
  Padding: 10px 12px
  Border: 1px solid var(--border)
  Border radius: 6px
  Font: 14px / 400 weight
  Width: 100%

Colors:
  Background: var(--surface)
  Color: var(--text-primary)
  Placeholder: var(--text-tertiary)

Focus:
  Border color: var(--accent-primary)
  Box shadow: 0 0 0 3px var(--primary-ghost)
  Outline: none

Disabled:
  Background: var(--surface)
  Color: var(--disabled)
  Cursor: not-allowed
```

---

### Card Component

```
Dimensions:
  Padding: 16px
  Border: 1px solid var(--border)
  Border radius: 8px
  Background: var(--surface)
  Box shadow: 0 1px 2px rgba(0, 0, 0, 0.05)

Hover (if interactive):
  Box shadow: 0 4px 12px rgba(0, 0, 0, 0.1)
  Transform: translateY(-2px)
  Transition: all 0.2s ease
```

---

### Tag/Chip Component

```
Dimensions:
  Height: 24px
  Padding: 4px 12px
  Border radius: 12px (pill shape)
  Font: 12px / 500 weight
  Display: inline-flex
  Align: center
  Gap: 6px

Primary Tag:
  Background: var(--accent-primary)
  Color: #FFFFFF

Secondary Tag:
  Background: var(--primary-light)
  Color: var(--accent-primary)

Removable Tag (with X):
  Add close icon: ×
  Icon size: 14px
  Icon hover: opacity 0.7
```

---

## Page: Automation Control (`/automation.html`)

**Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│ NAV BAR (same as main)                                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────┐  ┌──────────────────────────────┐   │
│  │  AUTOMATION      │  │  METRICS PANEL               │   │
│  │  CONTROLS        │  │                              │   │
│  │                  │  │  Files Processed: 0          │   │
│  │  [Daily]         │  │  Error Rate: 0%              │   │
│  │  [Weekly]        │  │  Time Saved: 0m              │   │
│  │  [Monthly]       │  │  Accuracy: 95%               │   │
│  │  [Test]          │  │                              │   │
│  │                  │  └──────────────────────────────┘   │
│  └──────────────────┘                                      │
│                                                             │
│  ┌───────────────────────────────────────────────────┐     │
│  │  REPORT GENERATION                                │     │
│  │                                                   │     │
│  │  [Generate Report]  [Export Data]                │     │
│  └───────────────────────────────────────────────────┘     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Automation Control Panel:**
```
Width: 320px
Padding: 20px
Background: var(--surface)
Border: 1px solid var(--border)
Border radius: 12px
Box shadow: 0 2px 8px rgba(0, 0, 0, 0.1)

Grid Layout (2×2):
  Display: grid
  Grid template columns: repeat(2, 1fr)
  Gap: 12px

Button:
  Height: 80px
  Display: flex
  Flex direction: column
  Align: center
  Justify: center
  Gap: 8px
  Background: var(--surface)
  Border: 1px solid var(--border)
  Border radius: 8px
  Cursor: pointer
  Transition: all 0.2s ease

  Icon: 24px
  Label: 13px / 500 weight

Hover:
  Background: var(--primary-ghost)
  Border color: var(--accent-primary)
  Transform: translateY(-2px)

Active (running):
  Background: var(--accent-primary)
  Color: #FFFFFF
  Border color: var(--accent-primary)
```

**Metrics Panel:**
```
Width: 400px
Padding: 20px
Background: var(--surface)
Border: 1px solid var(--border)
Border radius: 12px

Grid (2×2):
  Display: grid
  Grid template columns: repeat(2, 1fr)
  Gap: 12px

Metric Card:
  Padding: 12px
  Background: var(--surface-elevated)
  Border: 1px solid var(--border)
  Border radius: 6px

  Value:
    Font: 24px / 600 weight
    Color: var(--text-primary)

  Label:
    Font: 11px / 600 weight
    Color: var(--text-secondary)
    Text transform: uppercase
    Letter spacing: 0.5px
    Margin top: 4px
```

---

## Responsive Breakpoints

```
Mobile:        320px - 767px
Tablet:        768px - 1023px
Desktop:       1024px - 1439px
Large Desktop: 1440px+
```

**Mobile Adjustments:**
- Nav links collapse to hamburger menu
- Insights panel becomes bottom sheet
- Legend items stack/scroll horizontally
- Graph occupies full viewport (minus bottom bar)
- Touch targets minimum 44×44px

**Tablet Adjustments:**
- Nav links remain visible but closer spacing
- Insights panel width: 240px
- Side-by-side layouts stack vertically

---

## Interaction States & Animations

**Transitions:**
```
Standard: 0.2s ease
Slow: 0.3s ease
Fast: 0.1s ease
```

**Common Transitions:**
```
Button hover: all 0.2s ease
Color change: color 0.2s ease, background-color 0.2s ease
Transform: transform 0.2s ease
Opacity: opacity 0.2s ease
```

**Loading States:**
```
Spinner:
  Width: 40px
  Height: 40px
  Border: 3px solid var(--border)
  Border-top-color: var(--accent-primary)
  Border radius: 50%
  Animation: spin 1s linear infinite

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

---

## Accessibility Requirements

**Color Contrast:**
- Text on background: Minimum 4.5:1 (WCAG AA)
- Large text (18px+): Minimum 3:1
- Interactive elements: Minimum 3:1

**Focus Indicators:**
```
All interactive elements:
  Outline: 2px solid var(--accent-primary)
  Outline offset: 2px

Or:
  Box shadow: 0 0 0 3px var(--primary-ghost)
```

**Touch Targets:**
- Minimum size: 44×44px (mobile)
- Spacing: 8px minimum between targets

**Screen Reader:**
- All images have alt text
- Buttons have aria-labels
- Focus order follows visual order
- Semantic HTML (nav, main, aside, etc.)

---

## Export Assets Checklist

**For Figma/Canva:**
- [ ] Color palette as style library
- [ ] Typography scale as text styles
- [ ] Component library (buttons, inputs, cards)
- [ ] Icon set (24×24px, 20×20px, 16×16px sizes)
- [ ] Spacing grid (4px base unit)
- [ ] Shadow styles
- [ ] Border radius styles
- [ ] Each page as separate frame
- [ ] Light + dark theme variants

**File Format:**
- SVG for icons (scalable)
- PNG @2x for raster assets
- Design tokens as JSON (if supported)

---

**Status:** ✅ Complete - Ready for Figma/Canva Implementation
