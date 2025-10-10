# Personal Knowledge Graph System v2.0

Transform scattered digital artifacts into an intelligent, connected knowledge graph that reveals patterns, identifies gaps, and surfaces unrealized opportunities.

[![Status](https://img.shields.io/badge/status-in%20development-yellow)]() [![Version](https://img.shields.io/badge/version-2.0-blue)]() [![License](https://img.shields.io/badge/license-MIT-green)]()

---

## 🎯 Vision

Stop manually organizing files. Start discovering insights.

This system automatically discovers, organizes, tags, and connects all your digital artifacts (files, notes, screenshots, Notion pages, calendar events) into an interactive knowledge graph that helps you understand your work patterns, knowledge distribution, and career opportunities.

---

## ✨ Planned Features

### Phase 1 - Foundation (Week 1)
- ✅ **Interactive Knowledge Graph** - D3.js force-directed visualization with zoom, pan, drag
- ✅ **Multiple Layout Modes** - Organic, Circular, Grid, Hierarchical views
- ✅ **Dynamic Filtering** - Click clusters to filter, hover for details
- ✅ **Light/Dark Theme** - Smooth theme switching with localStorage persistence
- 🚧 **Intelligent File Discovery** - Auto-scan iCloud, OneDrive, local storage, Apple Notes
- 🚧 **Screenshot OCR** - Find any screenshot by content using Apple Vision or Tesseract
- 🚧 **AI-Powered Tagging** - Claude API with local NLP fallback, learns from corrections
- 🚧 **Automated Organization** - Daily cleanup, change logs, desktop tidying
- 🚧 **SQLite + FTS5 Storage** - Fast full-text search with graph relationships

### Phase 2 - Integration & Intelligence (Week 2)
- 📋 **Notion Integration** - Sync workspaces, pages, databases with full metadata
- 📋 **Email Integration** - Link emails to files, calendar, projects
- 📋 **Analytics Dashboard** - Pattern detection, gap analysis, time-vs-output metrics
- 📋 **Donut Chart Stats** - Interactive file type breakdown with storage metrics
- 📋 **Dynamic Insights Panel** - AI-generated storytelling that matters
- 📋 **Advanced Time Tracking** - Duration tracking with document access logs

### Phase 3 - Advanced Features (Future)
- 📋 **Mobile Companion** - iOS app for on-the-go access
- 📋 **Browser History Integration** - Track research trails
- 📋 **Hierarchical Drill-Down** - Multi-level topic exploration
- 📋 **Custom Metadata Fields** - User-defined properties per node

**Legend:** ✅ Complete | 🚧 In Progress | 📋 Planned

---

## 📊 Project Progress

### Overall Status

```
████████████░░░░░░░░░░░░░░░░░░░░  40% Complete

Phase 1: Foundation      ████████░░░░░░░░  45%
Phase 2: Integration     ░░░░░░░░░░░░░░░░   0%
Phase 3: Advanced        ░░░░░░░░░░░░░░░░   0%
```

### Completion Breakdown

| Component | Status | Progress | Details |
|-----------|--------|----------|---------|
| **📋 Design Docs** | ✅ Complete | ████████████████ 100% | All 14 documents finalized |
| **🎨 Frontend Prototype** | 🚧 In Progress | ████████░░░░░░░░ 50% | Sections 1-3 complete |
| **⚙️ Backend System** | 📋 Planned | ░░░░░░░░░░░░░░░░ 0% | In design phase |
| **🔗 Integrations** | 📋 Planned | ░░░░░░░░░░░░░░░░ 0% | Notion API documented |
| **📊 Analytics** | 📋 Planned | ░░░░░░░░░░░░░░░░ 0% | Queries designed |
| **📱 Mobile App** | 📋 Planned | ░░░░░░░░░░░░░░░░ 0% | Phase 3 |

### Milestones & Business Value

| Milestone | Business Outcome | Status | Impact |
|-----------|------------------|--------|--------|
| **🎯 M1: See Your Knowledge** | Visualize 1000+ scattered files as connected insights | ✅ **Done** | Stop forgetting what you know |
| **🔍 M2: Find Anything Instantly** | OCR + full-text search across all files | 📋 Next | Save 2+ hours/week searching |
| **🤖 M3: Automatic Organization** | Files tagged & sorted while you sleep | 📋 Week 2 | Never manually organize again |
| **💡 M4: Discover Opportunities** | AI identifies skill gaps & career paths | 📋 Week 2 | Turn scattered work into strategy |
| **📊 M5: Quantify Your Expertise** | Data-driven portfolio generation | 📋 Week 2 | Prove your value with metrics |
| **🔗 M6: Connect Everything** | Link Notion + Email + Calendar + Files | 📋 Phase 3 | One source of truth |
| **📱 M7: Access Anywhere** | Mobile app for insights on-the-go | 📋 Future | Your knowledge in your pocket |

### Frontend Sections Progress

| Section | Feature | Status | Unlocks |
|---------|---------|--------|---------|
| **Section 1** | Base + Theme | ✅ Complete | Professional dark/light modes |
| **Section 2** | Navigation | ✅ Complete | Switch between view modes |
| **Section 3** | Graph Canvas | ✅ Complete | See & explore your knowledge network |
| **Section 4** | Interactions | 📋 Next Up | Deep-dive into connections |
| **Section 5** | Visual Clustering | 📋 Planned | Spot patterns at a glance |
| **Section 6** | Smart Insights | 📋 Planned | AI tells you what matters |
| **Section 7** | Layout Modes | 📋 Planned | Different lenses on your work |

---

## 📊 Current Status

### Frontend Prototype (D3.js + HTML/CSS)

**Section 1: Base + Theme System** ✅
- CSS variables for light/dark themes
- Theme toggle with localStorage persistence
- Smooth transitions (0.25s ease-in-out)

**Section 2: Navigation Bar** ✅
- Fixed top navigation with layout links
- Active state tracking
- Theme toggle integration

**Section 3: Graph Canvas** ✅
- D3.js v7 force-directed graph
- Drag individual nodes
- Zoom & pan (0.2x - 3x scale)
- Node tooltips (type, cluster, files, modified)
- Link tooltips (type, strength, from/to)
- Legend bar with file counts
- Horizontal scrolling support
- Active cluster filtering
- Stats bubble (📊) - Files, Projects, Topics, Storage
- Soft color palette (#6366f1, #4ecdc4, #45b7d1, #96ceb4, #85c1e9)

**Next Steps:**
- Section 4: Enhanced graph interactions
- Section 5: Convex hulls (cluster background blobs)
- Section 6: Donut chart + dynamic insights
- Section 7: Layout mode switching

### Backend (Python + Flask)

🚧 **In Design Phase** - See [System Architecture](docs/design/12_SYSTEM_ARCHITECTURE.md)

---

## 📁 Project Structure

```
knowledge_map/
├── frontend/
│   ├── prototype_section1.html  # Base + Theme
│   ├── prototype_section2.html  # Navigation
│   └── prototype_section3.html  # Graph Canvas ✨
├── docs/
│   └── design/
│       ├── 01_PRODUCT_REQUIREMENTS.md
│       ├── 02_DATA_SOURCE_MAPPING.md
│       ├── 03_AUTO_TAGGING_SYSTEM.md
│       ├── 04_FILE_ORGANIZATION_RULES.md
│       ├── 05_GRAPH_DATABASE_SCHEMA.md
│       ├── 06_CHANGE_LOG_SYSTEM.md
│       ├── 07_TIME_TRACKING.md
│       ├── 08_BACKGROUND_JOBS.md
│       ├── 09_RELATIONSHIP_MODEL.md
│       ├── 10_ANALYTICS_QUERIES.md
│       ├── 11_UI_DESIGN.md
│       ├── 12_SYSTEM_ARCHITECTURE.md
│       ├── 13_UI_SPECIFICATIONS.md
│       └── 14_TESTING_PLAN.md
├── CHANGELOG.md
└── README.md (you are here)
```

---

## 📚 Documentation

### Design Documents

Comprehensive design documentation with decisions, rationale, and implementation details:

**Foundation**
- [01 - Product Requirements](docs/design/01_PRODUCT_REQUIREMENTS.md) - Complete PRD with all decisions resolved
- [02 - Data Source Mapping](docs/design/02_DATA_SOURCE_MAPPING.md) - iCloud, OneDrive, Apple Notes, Notion API, Calendar, Email
- [03 - Auto-Tagging System](docs/design/03_AUTO_TAGGING_SYSTEM.md) - Claude API + local NLP, learning from corrections
- [04 - File Organization Rules](docs/design/04_FILE_ORGANIZATION_RULES.md) - Automated moves with change logging

**Data & Storage**
- [05 - Graph Database Schema](docs/design/05_GRAPH_DATABASE_SCHEMA.md) - SQLite + FTS5 with relationship weights
- [06 - Change Log System](docs/design/06_CHANGE_LOG_SYSTEM.md) - Audit trail with monthly archival
- [07 - Time Tracking](docs/design/07_TIME_TRACKING.md) - Phase 1: dates, Phase 2: duration
- [09 - Relationship Model](docs/design/09_RELATIONSHIP_MODEL.md) - 6 relationship types with weight calculations (0.0-1.0)

**System & Operations**
- [08 - Background Jobs](docs/design/08_BACKGROUND_JOBS.md) - Daily/weekly/monthly automation with launchd
- [10 - Analytics Queries](docs/design/10_ANALYTICS_QUERIES.md) - SQL queries for insights, gaps, time-vs-output
- [12 - System Architecture](docs/design/12_SYSTEM_ARCHITECTURE.md) - 5-layer architecture (Ingestion → Analytics → Presentation)
- [14 - Testing Plan](docs/design/14_TESTING_PLAN.md) - 320+ unit tests, 60+ integration tests, self-check strategy

**User Interface**
- [11 - UI Design](docs/design/11_UI_DESIGN.md) - Visual design philosophy and interaction patterns
- [13 - UI Specifications](docs/design/13_UI_SPECIFICATIONS.md) - Exact measurements, colors, typography for Figma/Canva

### Development Log

See [CHANGELOG.md](CHANGELOG.md) for detailed history of all changes, features, and fixes.

---

## 🏗️ Design Philosophy

### Data-First Approach
We prioritize getting data organized and accessible before building complex UI features. Clean data structure → powerful insights.

### Lego Blocks Development
Build one section at a time, test thoroughly, then move to the next. Each component must meet requirements before adding complexity.

### Knowledge Management Standards
Following industry standards (Notion, Obsidian, Roam) for taxonomy:
- **Labels/Clusters** - Cross-cutting themes (Education, Professional, Technical, Research)
- **Node Types** - topic, project, document, folder
- **Relationships** - Inferred from containment and semantic links
- **Flexible Metadata** - Designed to support custom and dynamic fields (no hardcoded properties)

### Privacy-First
- Local-first processing
- Optional Claude API (can use local NLP fallback)
- No telemetry - your data stays yours
- Self-hosted deployment

---

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.9+
python --version

# D3.js (loaded via CDN in frontend)
# No installation needed for prototypes
```

### Quick Start (Prototype)

```bash
# Clone the repository
git clone https://github.com/jennifer-mckinney/knowledge-map.git
cd knowledge-map

# Open the latest prototype in your browser
open frontend/prototype_section3.html
```

### Backend Setup (Coming Soon)

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment
export CLAUDE_API_KEY="your-key"  # Optional

# Run initial scan
python src/scan_files.py

# Start Flask server
python src/app.py
```

---

## 🎨 Technology Stack

**Frontend**
- D3.js v7 - Force-directed graph visualization
- Vanilla HTML/CSS/JavaScript - No framework overhead
- CSS Variables - Dynamic theming

**Backend (Planned)**
- Python 3.9+ - Core processing
- Flask - REST API
- SQLite + FTS5 - Storage with full-text search
- Claude API - AI tagging (optional)
- Tesseract/Apple Vision - OCR for screenshots

**Automation**
- launchd (macOS) - Scheduled background jobs
- Python scripts - Daily/weekly/monthly tasks

---

## 🤝 Contributing

This is a personal project, but suggestions and feedback are welcome! Open an issue to discuss ideas.

---

## 📄 License

MIT License - see LICENSE file for details

---

## 👤 Author

**Jennifer McKinney**
- GitHub: [@jennifer-mckinney](https://github.com/jennifer-mckinney)
- Project: [knowledge-map](https://github.com/jennifer-mckinney/knowledge-map)
