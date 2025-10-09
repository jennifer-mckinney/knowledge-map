# Changelog

All notable changes to the Knowledge Map v2.0 project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added - 2025-01-09

#### Frontend Prototype - Section 3 Refinements
- **Legend bar** - Added centered legend bar at bottom of page with colored dots representing each cluster
- **Legend filtering** - Click legend items to filter graph by cluster, click again to reset
- **Link tooltips** - Hover over connection lines to see relationship metadata:
  - Type (semantic, contains, related)
  - Strength value (0.0-1.0)
  - Source and target node names
- **Link type metadata** - Added `type` field to all link connections in sample data

#### Frontend Prototype - Section 3 Initial Build
- **Graph canvas with D3.js v7** - Force-directed graph visualization
- **Force simulation** - Exact settings from reference file:
  - Charge force: -150 (node repulsion)
  - Link strength: 0.5x connection strength
  - Collision radius: node size + 5px
- **Drag behavior** - Individual nodes can be dragged and repositioned
- **Node tooltips** - Hover nodes to see metadata (type, category, files, last modified)
- **Click highlighting** - Click nodes to highlight connected nodes and relationships
- **Soft color palette** - Exact colors from reference file:
  - System: #6366f1 (indigo)
  - Education: #4ecdc4 (teal)
  - Professional: #45b7d1 (blue)
  - Technical: #96ceb4 (mint green)
  - Research: #85c1e9 (light blue)
- **Zoom and pan** - SVG canvas supports zoom (0.2x - 3x) and pan
- **Theme integration** - Dark mode support with brighter cluster colors
- **Responsive design** - Canvas resizes with window

#### Frontend Prototype - Section 2
- **Navigation bar** - Fixed top navigation with layout mode links
- **Layout links** - Organic, Circular, Grid, Hierarchical (Organic functional, others pending)
- **Theme toggle button** - Moon/sun icon in top right
- **Active state tracking** - Visual feedback for selected layout mode
- **Smooth theme transitions** - Synchronized 0.25s ease-in-out transitions for all elements

#### Frontend Prototype - Section 1
- **Base HTML structure** - Clean semantic HTML5 structure
- **CSS variables system** - Centralized theming with light/dark mode support
- **Theme toggle** - Light/dark mode switching with localStorage persistence
- **Color system** - Complete color palette for both themes
- **Typography** - System font stack for native OS appearance

### Changed - 2025-01-09

#### Frontend Prototype - Section 3 Taxonomy Updates
- **Adopted Knowledge Management taxonomy** - Following industry standards (Notion, Obsidian, Roam)
- **Changed node types** - Renamed `type: "category"` to `type: "topic"` for clarity
- **Consistent terminology** - Using "cluster" for labels/domains, "type" for node kind, "hierarchy" for relationships
- **Flexible metadata** - Designed to support future custom and dynamic metadata fields
- **Stats label updated** - Changed "Categories" to "Topics" in stats bubble

#### Frontend Prototype - Section 3 Bug Fixes
- **Connection lines more visible** - Increased visibility with darker color (#666 hex) and higher opacity (0.5), kept 1px width
- **Thinner circle outlines** - Reduced stroke-width from 2px → 1px → 0.5px for minimal, clean appearance
- **Fixed purple bubble "snake" bug** - Initialize all nodes with fx/fy = null to prevent accidental fixed positioning during pan/zoom

#### Frontend Prototype - Section 3 Enhancements
- **File counts in legend** - Each cluster shows total file count in parentheses (e.g., "Education (239)")
- **Horizontal scrolling legend** - Legend dynamically grows with touch-friendly scrolling (max-width: 90vw)
- **Active state visual feedback** - Selected cluster shows light background and shadow ring around color dot
- **Stats bubble** - Click 📊 icon (bottom right) to expand/collapse metrics:
  - Total files across all nodes
  - Project count (nodes with type: "project")
  - Category count (nodes with type: "category")
  - Storage calculation (displayed as MB or GB)
- **Removed node labels** - Text labels removed from circles for cleaner visual (names shown in tooltips)
- **CSS transition override** - Disabled transitions on graph elements (`.node`, `.link`) to prevent interference with D3 animation

### Design Documentation Updates
- **Added Notion integration to Phase 2** - Official API integration for workspaces, pages, databases
  - Extract structured data (properties, tags, relations)
  - Map internal page links to relationship edges
  - Sync Notion metadata → dynamic graph fields
  - Critical for user's active documentation workflow

### Design Documentation
- Created 14 comprehensive design documents covering:
  - Product requirements and specifications
  - Data source mapping and ingestion
  - Auto-tagging system with Claude API
  - File organization rules and automation
  - Graph database schema (SQLite + FTS5)
  - Change log system design
  - Time tracking implementation
  - Background jobs architecture
  - Relationship model and analytics
  - System architecture
  - UI specifications (Figma/Canva ready)
  - Testing plan with self-checking strategy

## [0.1.0] - 2025-01-09

### Project Initialization
- Repository structure created
- Design-first approach established
- "Lego blocks" development methodology adopted
- Reference HTML files analyzed (`knowledge_map_FIXED.html`, `knowledge_map_OBSERVABLE_EXACT.html`)

---

**Note**: This project follows a "data first" approach, prioritizing file organization and knowledge graph data structure before UI implementation.
