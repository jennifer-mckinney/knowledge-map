# UI Design Document
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Draft

**Reference:** Based on knowledge_map_OBSERVABLE_EXACT.html with user refinements

---

## Overview

The Knowledge Map UI is a **minimal, graph-first interface** with dynamic insights. Key design decisions:

- **No bulky control panels** - Clean, unobstructed graph view
- **Navigation via links** - Layout modes as top nav links instead of dropdowns
- **Dynamic insights** - Automatically generated contextual information on page load
- **Light + Dark themes** - Full theme support with seamless switching
- **Color-coded clusters** - Existing color scheme preserved

---

## Layout Structure (Simplified)

```
┌─────────────────────────────────────────────────────────────────────┐
│ Knowledge Map    [Organic] [Circular] [Grid] [Hierarchical]  [🌙]  │ ← Minimal nav bar
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│                                                                       │
│                      ●───────●                                       │
│                     ╱│       │╲                                      │
│                    ● │ GRAPH │ ●                                     │
│                     ╲│       │╱                                      │
│                      ●───────●                                       │
│                                                                       │
│                                                                       │
│                                                                       │
│  ┌─────────────────────────────────┐                                │
│  │ 💡 DYNAMIC INSIGHTS             │                                │
│  │                                  │                                │ ← Auto-generated insights
│  │ Your Education cluster has 239  │                                │    (bottom left)
│  │ files with strong connections   │                                │
│  │ to Research (0.8 strength)      │                                │
│  └─────────────────────────────────┘                                │
│                                                                       │
├─────────────────────────────────────────────────────────────────────┤
│ [System (20)] [Education (239)] [Professional (13)] [Technical (8)]│ ← Legend (bottom)
└─────────────────────────────────────────────────────────────────────┘
```

---

## Color System

### Light Theme (Default)
```css
/* Surfaces */
--background: #fafafa;
--surface: rgba(255, 255, 255, 0.98);
--border: #e1e8ed;

/* Text */
--text-primary: #14171a;
--text-secondary: #657786;

/* Accents */
--accent-primary: #4a90a4;
--accent-hover: #3a7a94;

/* Cluster colors (preserved from current design) */
--cluster-system: #6366f1;         /* Indigo */
--cluster-education: #4ecdc4;      /* Turquoise */
--cluster-professional: #45b7d1;   /* Sky blue */
--cluster-technical: #96ceb4;      /* Sage green */
--cluster-research: #85c1e9;       /* Light blue */
--cluster-analysis: #f59e0b;       /* Amber */
--cluster-admin: #a78bfa;          /* Purple */
--cluster-archive: #94a3b8;        /* Gray */
```

### Dark Theme
```css
/* Surfaces */
--background: #14171a;
--surface: rgba(32, 35, 39, 0.98);
--border: #3d4043;

/* Text */
--text-primary: #f7f9fa;
--text-secondary: #8899a6;

/* Accents */
--accent-primary: #6eb3c7;
--accent-hover: #8ec4d6;

/* Cluster colors (adjusted for dark background) */
--cluster-system: #7c7ff2;         /* Lighter indigo */
--cluster-education: #5eddd4;      /* Brighter turquoise */
--cluster-professional: #55c7e1;   /* Brighter sky blue */
--cluster-technical: #a6dec4;      /* Lighter sage */
--cluster-research: #95d1f9;       /* Brighter blue */
--cluster-analysis: #ffa726;       /* Brighter amber */
--cluster-admin: #b79cfa;          /* Lighter purple */
--cluster-archive: #a4b3c8;        /* Lighter gray */
```

---

## Component: Navigation Bar (Top)

**Position:** Fixed top, full width, minimal height (50px)

**Structure:**
```html
<nav class="top-nav">
    <div class="nav-left">
        <span class="brand">Knowledge Map</span>
    </div>

    <div class="nav-center">
        <a href="#" class="nav-link active" data-layout="organic">Organic</a>
        <a href="#" class="nav-link" data-layout="circular">Circular</a>
        <a href="#" class="nav-link" data-layout="grid">Grid</a>
        <a href="#" class="nav-link" data-layout="hierarchical">Hierarchical</a>
    </div>

    <div class="nav-right">
        <button class="theme-toggle" onclick="toggleTheme()">
            <span class="theme-icon">🌙</span>
        </button>
    </div>
</nav>
```

**Styling (Light):**
```css
.top-nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 50px;
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 30px;
    z-index: 1000;
    backdrop-filter: blur(10px);
}

.brand {
    font-weight: 600;
    font-size: 16px;
    color: var(--text-primary);
}

.nav-center {
    display: flex;
    gap: 30px;
}

.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    padding: 8px 12px;
    border-radius: 6px;
    transition: all 0.2s ease;
}

.nav-link:hover {
    color: var(--accent-primary);
    background: rgba(74, 144, 164, 0.1);
}

.nav-link.active {
    color: var(--accent-primary);
    background: rgba(74, 144, 164, 0.15);
}

.theme-toggle {
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
    padding: 6px 10px;
    border-radius: 6px;
    transition: background 0.2s ease;
}

.theme-toggle:hover {
    background: rgba(74, 144, 164, 0.1);
}
```

**Interactions:**
- Click layout link → change graph layout
- Active link has accent background
- Theme toggle button switches between 🌙 (dark) and ☀️ (light)

---

## Component: Dynamic Insights Panel (Bottom Left)

**Position:** Fixed, bottom left corner, above legend

**Purpose:** Auto-generates interesting insights about the graph on page load

**Structure:**
```html
<div class="insights-panel">
    <div class="insights-header">
        <span class="insights-icon">💡</span>
        <span class="insights-title">Insights</span>
    </div>
    <div class="insights-content" id="insightsContent">
        <!-- Dynamically generated content -->
    </div>
</div>
```

**Styling:**
```css
.insights-panel {
    position: fixed;
    bottom: 80px;  /* Above legend */
    left: 20px;
    width: 280px;
    max-width: 90vw;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    animation: fadeIn 0.5s ease 0.5s both;  /* Fade in after 0.5s delay */
}

.insights-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
}

.insights-icon {
    font-size: 18px;
}

.insights-title {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-primary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.insights-content {
    font-size: 13px;
    line-height: 1.6;
    color: var(--text-secondary);
}

.insight-item {
    margin: 8px 0;
    padding: 8px;
    background: rgba(74, 144, 164, 0.08);
    border-radius: 6px;
    border-left: 3px solid var(--accent-primary);
}

.insight-highlight {
    color: var(--accent-primary);
    font-weight: 600;
}

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

**Dynamic Content Generation:**
```javascript
function generateInsights() {
    const insights = [];

    // Insight 1: Largest cluster
    const clusterSizes = d3.rollup(
        fileData.nodes,
        v => v.reduce((sum, d) => sum + d.files, 0),
        d => d.cluster
    );
    const largestCluster = Array.from(clusterSizes.entries())
        .sort((a, b) => b[1] - a[1])[0];

    insights.push(`
        <div class="insight-item">
            Your <span class="insight-highlight">${clusters[largestCluster[0]].name}</span>
            cluster contains <span class="insight-highlight">${largestCluster[1]} files</span>
            — your largest knowledge area.
        </div>
    `);

    // Insight 2: Strongest connection
    const strongestLink = fileData.links
        .sort((a, b) => b.strength - a.strength)[0];
    const sourceNode = fileData.nodes.find(n => n.id === strongestLink.source.id);
    const targetNode = fileData.nodes.find(n => n.id === strongestLink.target.id);

    insights.push(`
        <div class="insight-item">
            Strongest connection: <span class="insight-highlight">${sourceNode.name}</span>
            ↔ <span class="insight-highlight">${targetNode.name}</span>
            (${Math.round(strongestLink.strength * 100)}% strength)
        </div>
    `);

    // Insight 3: Recent activity
    const recentNodes = fileData.nodes
        .filter(d => d.lastModified)
        .sort((a, b) => new Date(b.lastModified) - new Date(a.lastModified))
        .slice(0, 3);

    insights.push(`
        <div class="insight-item">
            Most recent work in:
            <span class="insight-highlight">${recentNodes.map(n => n.category).join(', ')}</span>
        </div>
    `);

    // Insight 4: Isolated nodes (opportunity)
    const connectedNodes = new Set();
    fileData.links.forEach(l => {
        connectedNodes.add(l.source.id);
        connectedNodes.add(l.target.id);
    });
    const isolatedCount = fileData.nodes.filter(n => !connectedNodes.has(n.id)).length;

    if (isolatedCount > 0) {
        insights.push(`
            <div class="insight-item">
                💡 <span class="insight-highlight">${isolatedCount} nodes</span> have no connections
                — potential for new relationships.
            </div>
        `);
    }

    // Render insights
    document.getElementById('insightsContent').innerHTML = insights.join('');
}

// Call on page load (after graph initializes)
setTimeout(generateInsights, 1000);
```

**Insight Types (Rotate/Vary):**
1. **Cluster dominance:** "Education cluster has 239 files — your primary focus area"
2. **Strong connections:** "Oxford_AI ↔ AI_Research (90% connection strength)"
3. **Recent activity:** "Most active this week: Professional, Technical"
4. **Isolated nodes:** "12 files have no connections — opportunity to link"
5. **Cross-domain:** "Technical and Research clusters overlap strongly"
6. **Time-based:** "45 files modified in last 7 days"

---

## Component: Legend (Bottom)

**Position:** Fixed bottom, full width (with margins)

**Unchanged from existing design** - Keep as-is:
```html
<div class="legend">
    <div class="legend-item" onclick="filterCluster('system')">
        <div class="legend-color" style="background: #6366f1"></div>
        <span>System (20)</span>
    </div>
    <!-- Repeat for each cluster -->
</div>
```

**Styling adjustments for dark theme:**
```css
/* Dark theme overrides */
body.dark-theme .legend {
    background: var(--surface);
    border-top: 1px solid var(--border);
}

body.dark-theme .legend-item {
    color: var(--text-primary);
}
```

---

## Theme Toggle System

**JavaScript Implementation:**
```javascript
// Theme state (persist in localStorage)
let currentTheme = localStorage.getItem('theme') || 'light';

function initTheme() {
    if (currentTheme === 'dark') {
        document.body.classList.add('dark-theme');
        document.querySelector('.theme-icon').textContent = '☀️';
    }
}

function toggleTheme() {
    currentTheme = currentTheme === 'light' ? 'dark' : 'light';

    if (currentTheme === 'dark') {
        document.body.classList.add('dark-theme');
        document.querySelector('.theme-icon').textContent = '☀️';
    } else {
        document.body.classList.remove('dark-theme');
        document.querySelector('.theme-icon').textContent = '🌙';
    }

    // Save preference
    localStorage.setItem('theme', currentTheme);

    // Smooth transition
    document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
}

// Initialize on load
document.addEventListener('DOMContentLoaded', initTheme);
```

**CSS Variables (Theme Switching):**
```css
/* Light theme (default) */
:root {
    --background: #fafafa;
    --surface: rgba(255, 255, 255, 0.98);
    --border: #e1e8ed;
    --text-primary: #14171a;
    --text-secondary: #657786;
    --accent-primary: #4a90a4;
    --accent-hover: #3a7a94;
}

/* Dark theme */
body.dark-theme {
    --background: #14171a;
    --surface: rgba(32, 35, 39, 0.98);
    --border: #3d4043;
    --text-primary: #f7f9fa;
    --text-secondary: #8899a6;
    --accent-primary: #6eb3c7;
    --accent-hover: #8ec4d6;
}

/* Apply to all components automatically */
body {
    background: var(--background);
    color: var(--text-primary);
    transition: background-color 0.3s ease, color 0.3s ease;
}

svg {
    background: var(--background);
}

.node {
    /* Node colors remain the same, but adjust opacity for dark theme */
    opacity: 1;
}

body.dark-theme .node {
    opacity: 0.95;
}

.link {
    stroke: var(--text-secondary);
    stroke-opacity: 0.3;
}

body.dark-theme .link {
    stroke-opacity: 0.4;  /* Slightly more visible in dark mode */
}
```

---

## Graph Canvas (Main)

**Unchanged from existing implementation** - Full-screen force-directed graph

**Interactions:**
- Drag nodes to reposition
- Hover for tooltips
- Click to highlight connections
- Zoom/pan with mouse wheel/drag

**Dark theme adjustments:**
```css
body.dark-theme .tooltip {
    background: rgba(248, 249, 250, 0.95);  /* Light tooltip on dark bg */
    color: #14171a;
}

body.dark-theme .cluster-background {
    opacity: 0.12;  /* Slightly lower opacity in dark mode */
}

body.dark-theme .label {
    fill: var(--text-primary);
}
```

---

## Removed Components

**From original OBSERVABLE_EXACT.html, these are REMOVED:**

1. ❌ **Control Panel (left side)** - Large panel with automation buttons, metrics
2. ❌ **Stats Panel (right side)** - Total files, projects, categories display
3. ❌ **Quick Actions Panel (bottom right)** - Organize, archive, duplicates buttons
4. ❌ **Keyboard Shortcuts Hint (bottom left)** - Overlay showing shortcuts
5. ❌ **Report Modal** - Full-screen report generation modal
6. ❌ **Dropdowns for clustering** - "By Category", "By Project", "By Type"

**Why removed:**
- User wants minimal, clean interface
- Graph should be the primary focus
- Navigation handled by top links
- Insights panel replaces manual controls

---

## Layout Modes (Navigation Links)

**Organic:**
- Default force-directed layout
- Nodes move dynamically
- Natural clustering

**Circular:**
- Nodes arranged in circle
- Equal spacing
- Fixed positions

**Grid:**
- Nodes in grid pattern
- Systematic organization

**Hierarchical:**
- Nodes grouped by cluster
- Radial arrangement

**JavaScript (simplified):**
```javascript
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();

        // Update active state
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');

        // Get layout mode
        const layout = link.dataset.layout;
        applyLayout(layout);
    });
});

function applyLayout(mode) {
    if (mode === 'circular') {
        const radius = Math.min(width, height) / 3;
        const angleStep = (2 * Math.PI) / fileData.nodes.length;

        fileData.nodes.forEach((d, i) => {
            const angle = i * angleStep;
            d.fx = width/2 + radius * Math.cos(angle);
            d.fy = height/2 + radius * Math.sin(angle);
        });
    } else if (mode === 'grid') {
        const cols = Math.ceil(Math.sqrt(fileData.nodes.length));
        const cellW = (width - 200) / cols;
        const cellH = (height - 200) / cols;

        fileData.nodes.forEach((d, i) => {
            d.fx = 100 + (i % cols) * cellW;
            d.fy = 100 + Math.floor(i / cols) * cellH;
        });
    } else if (mode === 'hierarchical') {
        // Radial cluster layout
        const clusterGroups = d3.group(fileData.nodes, d => d.cluster);
        const clusterCount = clusterGroups.size;
        const angleStep = (2 * Math.PI) / clusterCount;
        let clusterIndex = 0;

        clusterGroups.forEach((nodes, cluster) => {
            const angle = clusterIndex * angleStep;
            const clusterRadius = Math.min(width, height) / 4;
            const centerX = width/2 + clusterRadius * Math.cos(angle);
            const centerY = height/2 + clusterRadius * Math.sin(angle);

            nodes.forEach((d, i) => {
                const nodeAngle = (2 * Math.PI * i) / nodes.length;
                const nodeRadius = 50 + d.size * 2;
                d.fx = centerX + nodeRadius * Math.cos(nodeAngle);
                d.fy = centerY + nodeRadius * Math.sin(nodeAngle);
            });

            clusterIndex++;
        });
    } else {
        // Organic - remove constraints
        fileData.nodes.forEach(d => {
            d.fx = null;
            d.fy = null;
        });
    }

    simulation.alpha(1).restart();
}
```

---

## Responsive Design

### Desktop (1024px+)
- Full layout as described
- Nav bar with all links visible
- Insights panel bottom left

### Tablet (768px - 1023px)
- Nav center links collapse to hamburger menu
- Insights panel becomes bottom drawer (swipe up)
- Legend scrolls horizontally

### Mobile (<768px)
- Minimal nav: Brand + hamburger + theme toggle
- Insights as bottom sheet
- Simplified graph (fewer labels, larger touch targets)

---

## Keyboard Shortcuts (Hidden, No UI)

```
⌘K / Ctrl+K    → Focus search (if added later)
⌘T / Ctrl+T    → Toggle theme
⌘0 / Ctrl+0    → Reset zoom
⌘1-4           → Switch layouts (Organic=1, Circular=2, Grid=3, Hierarchical=4)
ESC            → Clear selections
```

---

## Accessibility

**Keyboard Navigation:**
- Tab through nav links
- Enter to activate
- Arrow keys to pan graph (optional)

**Screen Reader:**
```html
<nav aria-label="Main navigation">
    <a href="#" aria-label="Organic layout mode" data-layout="organic">Organic</a>
</nav>

<div class="insights-panel" role="complementary" aria-label="Graph insights">
    ...
</div>
```

**Color Contrast:**
- Light theme: All text > 4.5:1 contrast
- Dark theme: All text > 4.5:1 contrast
- Cluster colors adjusted for both themes

---

## Implementation Summary

### Key Changes from OBSERVABLE_EXACT.html:

1. ✅ **Removed:** Bulky control panel (left side)
2. ✅ **Added:** Minimal top navigation bar with layout links
3. ✅ **Added:** Dark theme support (full CSS variables)
4. ✅ **Added:** Dynamic insights panel (auto-generated on load)
5. ✅ **Simplified:** Clean, graph-first interface
6. ✅ **Preserved:** Existing color scheme, D3.js graph, legend

### Files to Update:

1. **HTML structure:** Add top nav, insights panel, theme toggle
2. **CSS:** Convert all colors to CSS variables, add dark theme classes
3. **JavaScript:** Add theme toggle, insights generation, nav link handlers

---

**Status:** ✅ Complete (User-refined design)
