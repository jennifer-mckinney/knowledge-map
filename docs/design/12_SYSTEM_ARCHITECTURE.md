# System Architecture Document
**Project:** knowledge_map v2.0 - Personal Knowledge Graph System
**Date:** 2025-10-09
**Status:** Final
**Version:** 2.0

---

## Executive Summary

The Personal Knowledge Graph System v2.0 is a single-user, macOS-native application that automatically discovers, organizes, tags, and visualizes digital artifacts across your ecosystem. The system uses a 5-layer architecture with Python/Flask backend, D3.js frontend, SQLite database, and Claude API for AI-powered tagging.

**Key Characteristics:**
- **Deployment:** Local macOS installation (single user)
- **Privacy-first:** All processing happens locally, optional cloud AI
- **Automation-focused:** Daily background jobs keep system synchronized
- **Graph-centric:** Knowledge graph database with relationship modeling
- **Minimal maintenance:** Self-learning system with automated organization

---

## 1. Technology Stack

### Backend Technologies

**Core Framework:**
```
Python 3.9+
Flask 2.0+ (web framework)
Werkzeug (WSGI utility)
```

**Database:**
```
SQLite 3.35+ (embedded database)
- FTS5 for full-text search
- JSON1 extension for metadata
- ACID transactions
- Single-file portability
```

**AI/NLP:**
```
Primary: Anthropic Claude API (claude-3-5-sonnet-20241022)
Fallback: Local NLP stack
  - spaCy 3.0+ (NER, entity extraction)
  - scikit-learn 1.0+ (TF-IDF, topic modeling)
  - NLTK (text processing)
```

**Content Extraction:**
```
PyPDF2 / pdfplumber (PDF text extraction)
python-docx (Word documents)
pytesseract / Apple Vision (OCR)
Pillow (image processing)
beautifulsoup4 (HTML parsing)
```

**File System:**
```
watchdog (file system monitoring)
pathlib (path operations)
```

**Scheduling:**
```
APScheduler (Python job scheduling)
macOS LaunchAgents (production scheduling)
```

### Frontend Technologies

**Core:**
```
HTML5 / CSS3
Vanilla JavaScript (ES6+)
D3.js v7 (graph visualization)
```

**Styling:**
```
CSS Variables (theme system)
Flexbox / Grid layout
CSS animations / transitions
```

**Optional Enhancements:**
```
Chart.js (analytics charts)
highlight.js (code syntax highlighting)
```

### Development Tools

```
Git (version control)
pytest (unit testing)
black (code formatting)
pylint (linting)
VS Code / PyCharm (IDE)
```

---

## 2. File Structure

### Project Directory Layout

```
knowledge_map/
├── src/                          # Python source code
│   ├── __init__.py
│   ├── app.py                    # Flask application entry point
│   ├── config.py                 # Configuration management
│   │
│   ├── core/                     # Core business logic
│   │   ├── __init__.py
│   │   ├── scanner.py            # File system scanning
│   │   ├── extractor.py          # Content extraction (PDF, OCR, etc.)
│   │   ├── tagger.py             # AI tagging system
│   │   ├── organizer.py          # File organization engine
│   │   └── relationships.py      # Relationship detection
│   │
│   ├── database/                 # Database layer
│   │   ├── __init__.py
│   │   ├── schema.sql            # SQLite schema
│   │   ├── models.py             # Data models
│   │   └── queries.py            # SQL query helpers
│   │
│   ├── integrations/             # External integrations
│   │   ├── __init__.py
│   │   ├── apple_notes.py        # Apple Notes sync
│   │   ├── calendar.py           # Calendar sync
│   │   ├── photos.py             # Photos Library sync
│   │   └── claude_api.py         # Claude API client
│   │
│   ├── jobs/                     # Background jobs
│   │   ├── __init__.py
│   │   ├── daily.py              # Daily job (scanning, tagging)
│   │   ├── weekly.py             # Weekly job (notes, calendar)
│   │   └── monthly.py            # Monthly job (maintenance)
│   │
│   ├── api/                      # REST API endpoints
│   │   ├── __init__.py
│   │   ├── graph.py              # Graph data endpoints
│   │   ├── search.py             # Search endpoints
│   │   ├── analytics.py          # Analytics endpoints
│   │   ├── automation.py         # Automation control
│   │   └── changelog.py          # Change log endpoints
│   │
│   └── utils/                    # Utility functions
│       ├── __init__.py
│       ├── logger.py             # Logging configuration
│       ├── validators.py         # Input validation
│       └── helpers.py            # Common helpers
│
├── frontend/                     # Frontend files
│   ├── index.html                # Main graph view
│   ├── automation.html           # Automation control page
│   ├── search.html               # Search interface
│   ├── analytics.html            # Analytics dashboard
│   ├── changelog.html            # Change log viewer
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css          # Main styles
│   │   │   ├── theme-light.css   # Light theme
│   │   │   └── theme-dark.css    # Dark theme
│   │   │
│   │   ├── js/
│   │   │   ├── graph.js          # D3.js graph visualization
│   │   │   ├── search.js         # Search functionality
│   │   │   ├── analytics.js      # Analytics charts
│   │   │   ├── automation.js     # Automation controls
│   │   │   └── api.js            # API client
│   │   │
│   │   └── assets/
│   │       ├── icons/            # SVG icons
│   │       └── fonts/            # Custom fonts (if any)
│   │
│   └── components/               # Reusable UI components
│       ├── navbar.html
│       ├── insights-panel.html
│       └── legend.html
│
├── data/                         # Data storage
│   ├── knowledge_graph.db        # SQLite database
│   ├── config.json               # User configuration
│   ├── corrections.json          # Learning system data
│   │
│   ├── cache/                    # Temporary cache
│   │   ├── ocr/                  # OCR results cache
│   │   └── embeddings/           # Text embeddings cache
│   │
│   └── backups/                  # Database backups
│       └── knowledge_graph_YYYY-MM-DD.db
│
├── tests/                        # Unit tests
│   ├── __init__.py
│   ├── test_scanner.py
│   ├── test_tagger.py
│   ├── test_relationships.py
│   ├── test_api.py
│   └── fixtures/                 # Test fixtures
│
├── scripts/                      # Utility scripts
│   ├── setup.sh                  # Initial setup script
│   ├── install_launchd.sh        # Install LaunchAgent
│   ├── backup_db.py              # Manual backup script
│   └── migrate_data.py           # Data migration tools
│
├── logs/                         # Application logs
│   ├── app.log                   # Main application log
│   ├── jobs/                     # Job execution logs
│   └── errors/                   # Error logs
│
├── docs/                         # Documentation
│   ├── design/                   # Design documents (01-13)
│   ├── api/                      # API documentation
│   └── user_guide.md             # User manual
│
├── .env                          # Environment variables (secrets)
├── .env.example                  # Example env file
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup
├── pytest.ini                    # Pytest configuration
├── README.md                     # Project readme
└── LICENSE                       # License file
```

### Key Files Description

**src/app.py** - Flask application entry point
```python
# Initializes Flask app, registers blueprints, starts scheduler
# Usage: python src/app.py
```

**src/config.py** - Configuration management
```python
# Loads .env, manages user preferences, paths
# Handles dev vs. production settings
```

**data/knowledge_graph.db** - SQLite database
```
# Single-file database containing:
# - nodes (files, notes, events)
# - edges (relationships)
# - tags (normalized tags)
# - analytics_cache (pre-computed insights)
```

**.env** - Environment variables (not committed)
```bash
# Contains:
# - ANTHROPIC_API_KEY (Claude API key)
# - DATABASE_PATH (override default location)
# - LOG_LEVEL (DEBUG, INFO, WARNING, ERROR)
# - ENABLE_CLOUD_AI (true/false)
```

---

## 3. Five-Layer Architecture

### Overview

```
┌─────────────────────────────────────────────────────────┐
│                   5. PRESENTATION LAYER                 │
│              (Flask Routes + HTML/CSS/JS)               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                   4. ANALYTICS LAYER                     │
│           (Insights, Queries, Business Logic)           │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                   3. STORAGE LAYER                       │
│              (SQLite + File System)                      │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  2. PROCESSING LAYER                     │
│    (Tagging, Relationships, Organization)               │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                   1. INGESTION LAYER                     │
│      (File Scanning, OCR, Content Extraction)           │
└─────────────────────────────────────────────────────────┘
```

### Layer 1: Ingestion

**Purpose:** Discover and extract content from files

**Components:**
- `src/core/scanner.py` - File system scanning
- `src/core/extractor.py` - Content extraction

**Responsibilities:**
1. Monitor file system locations (iCloud, Downloads, etc.)
2. Detect new/modified files
3. Extract text content (PDF, DOCX, OCR)
4. Extract metadata (dates, size, type)
5. Generate content hashes (SHA-256)

**Data Flow:**
```
File System → Scanner → Extractor → Raw Content + Metadata → Processing Layer
```

**Performance:**
- Scan 10,000 files in <60 seconds
- OCR processing: <2 seconds per screenshot
- Incremental scanning (only new/modified files)

**Implementation Details:**
```python
# File scanner monitors these locations
MONITORED_PATHS = [
    Path.home() / 'Library/Mobile Documents/com~apple~CloudDocs/Documents',
    Path.home() / 'Downloads',
    Path.home() / 'Desktop'
]

# Content extraction by file type
EXTRACTORS = {
    '.pdf': extract_pdf_content,
    '.docx': extract_docx_content,
    '.txt': extract_text_content,
    '.png': extract_image_text,  # OCR
    '.jpg': extract_image_text   # OCR
}
```

### Layer 2: Processing

**Purpose:** Transform raw content into structured knowledge

**Components:**
- `src/core/tagger.py` - AI tagging
- `src/core/relationships.py` - Relationship detection
- `src/core/organizer.py` - File organization

**Responsibilities:**
1. Auto-tag files using Claude API or local NLP
2. Detect relationships between nodes (similarity, temporal, cross-domain)
3. Organize files into appropriate folders
4. Generate change logs

**Data Flow:**
```
Raw Content → Tagger → Tagged Content → Relationship Engine → Organizer → Storage Layer
```

**AI Tagging Pipeline:**
1. Extract content + context (calendar, location, related files)
2. Call Claude API with prompt (or fallback to local NLP)
3. Parse response → primary tags (1-3), secondary tags, keywords
4. Validate and normalize tags
5. Apply learning corrections

**Relationship Detection:**
- Content similarity (cosine similarity of TF-IDF vectors, threshold 0.70)
- Temporal (same day=1.0, week=0.8, month=0.5)
- Hierarchical (folder structure)
- Cross-domain (tags from different domains)
- Manual (user-created)

**Implementation Details:**
```python
# Tagging strategy
if ENABLE_CLOUD_AI and api_available():
    tags = tag_with_claude(content, context)
else:
    tags = tag_with_local_nlp(content, context)

# Relationship weights
SIMILARITY_THRESHOLD = 0.70
TEMPORAL_WEIGHTS = {
    'same_day': 1.0,
    'same_week': 0.8,
    'same_month': 0.5,
    'same_quarter': 0.3
}
```

### Layer 3: Storage

**Purpose:** Persist and index knowledge graph

**Components:**
- `src/database/models.py` - Data models
- `src/database/queries.py` - Query helpers
- SQLite database

**Responsibilities:**
1. Store nodes (files, notes, events)
2. Store edges (relationships with weights, reasons)
3. Store tags (normalized, indexed)
4. Full-text search indexing (FTS5)
5. Transaction management

**Database Schema:**
```sql
-- Core tables
CREATE TABLE nodes (
    id TEXT PRIMARY KEY,
    date_created TEXT NOT NULL,
    date_modified TEXT,
    type TEXT NOT NULL,
    file_path TEXT,
    file_name TEXT,
    file_size INTEGER,
    file_extension TEXT,
    content_hash TEXT,
    content_excerpt TEXT,
    metadata_json TEXT,
    time_tracking_json TEXT,
    change_history_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE edges (
    id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    target TEXT NOT NULL,
    weight REAL NOT NULL CHECK(weight >= 0.0 AND weight <= 1.0),
    created_date TEXT NOT NULL,
    last_updated TEXT,
    type TEXT NOT NULL,
    why_json TEXT NOT NULL,
    metadata_json TEXT,
    bidirectional INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source) REFERENCES nodes(id) ON DELETE CASCADE,
    FOREIGN KEY (target) REFERENCES nodes(id) ON DELETE CASCADE
);

CREATE TABLE tags (
    node_id TEXT NOT NULL,
    tag TEXT NOT NULL,
    tag_type TEXT NOT NULL,  -- 'primary', 'secondary', 'keyword'
    score REAL,
    PRIMARY KEY (node_id, tag, tag_type),
    FOREIGN KEY (node_id) REFERENCES nodes(id) ON DELETE CASCADE
);

CREATE TABLE analytics_cache (
    query_name TEXT PRIMARY KEY,
    result_json TEXT NOT NULL,
    computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_nodes_type ON nodes(type);
CREATE INDEX idx_nodes_date_created ON nodes(date_created);
CREATE INDEX idx_nodes_file_path ON nodes(file_path);
CREATE INDEX idx_tags_node_id ON tags(node_id);
CREATE INDEX idx_tags_tag ON tags(tag);
CREATE INDEX idx_edges_source ON edges(source);
CREATE INDEX idx_edges_target ON edges(target);
CREATE INDEX idx_edges_weight ON edges(weight);

-- Full-text search (FTS5)
CREATE VIRTUAL TABLE nodes_fts USING fts5(
    id,
    file_name,
    content_excerpt,
    content=nodes,
    content_rowid=rowid
);
```

**Backup Strategy:**
- Daily automatic backup (via monthly job)
- 30-day retention
- Stored in `data/backups/`

### Layer 4: Analytics

**Purpose:** Extract insights and answer user questions

**Components:**
- `src/api/analytics.py` - Analytics endpoints
- Pre-computed queries (weekly job)

**Responsibilities:**
1. Strength detection ("What am I good at?")
2. Cross-domain opportunities
3. Knowledge gaps identification
4. Time vs. output analysis
5. Business value scoring
6. Recent activity summaries

**Analytics Queries:**

**Knowledge Strengths:**
```sql
SELECT
    t.tag,
    COUNT(DISTINCT t.node_id) as artifact_count,
    AVG(e.weight) as avg_connection_strength,
    (COUNT(DISTINCT t.node_id) * AVG(e.weight)) as strength_score
FROM tags t
LEFT JOIN edges e ON t.node_id = e.source OR t.node_id = e.target
WHERE t.tag_type = 'primary'
GROUP BY t.tag
HAVING artifact_count >= 3
ORDER BY strength_score DESC
LIMIT 10;
```

**Knowledge Gaps:**
```sql
SELECT
    t.tag,
    COUNT(DISTINCT n.id) as isolated_docs,
    COUNT(DISTINCT e.id) as total_connections
FROM tags t
JOIN nodes n ON t.node_id = n.id
LEFT JOIN edges e ON n.id = e.source OR n.id = e.target
WHERE t.tag_type = 'primary'
GROUP BY t.tag
HAVING total_connections < 2
ORDER BY isolated_docs DESC;
```

**Cross-Domain Opportunities:**
```sql
SELECT
    t1.tag as domain1,
    t2.tag as domain2,
    COUNT(DISTINCT e.id) as bridge_count,
    AVG(e.weight) as avg_strength
FROM edges e
JOIN tags t1 ON e.source = t1.node_id
JOIN tags t2 ON e.target = t2.node_id
WHERE t1.tag != t2.tag
  AND t1.tag_type = 'primary'
  AND t2.tag_type = 'primary'
GROUP BY t1.tag, t2.tag
HAVING bridge_count >= 3
ORDER BY avg_strength DESC
LIMIT 10;
```

**Recent Activity:**
```sql
SELECT
    t.tag,
    COUNT(DISTINCT n.id) as active_files,
    SUM(LENGTH(n.content_excerpt)) as total_content
FROM nodes n
JOIN tags t ON n.id = t.node_id
WHERE n.date_modified >= date('now', '-7 days')
  AND t.tag_type = 'primary'
GROUP BY t.tag
ORDER BY active_files DESC;
```

**Caching:**
- Cache results for 1 hour
- Invalidate on data modification
- Store in `analytics_cache` table

### Layer 5: Presentation

**Purpose:** User interfaces and API endpoints

**Components:**
- Flask routes (REST API)
- HTML/CSS/JS frontend
- D3.js graph visualization

**Responsibilities:**
1. Serve web interface
2. Provide REST API for data access
3. Handle user interactions
4. Render graph visualization
5. Display analytics dashboards

**Pages:**
- `/` - Main graph view (D3.js force-directed visualization)
- `/automation` - Automation control panel
- `/search` - Search interface
- `/analytics` - Analytics dashboard
- `/changelog` - Change log viewer

---

## 4. REST API Endpoints

### Graph Endpoints

**GET /api/graph/data**
```json
Description: Get full graph data for visualization
Response: {
  "nodes": [
    {
      "id": "node-001",
      "name": "ai_ethics_framework.pdf",
      "type": "document",
      "cluster": "education",
      "size": 24,
      "files": 1,
      "primary_tags": ["ai-ethics", "oxford"],
      "lastModified": "2025-10-09"
    }
  ],
  "links": [
    {
      "source": "node-001",
      "target": "node-002",
      "strength": 0.85,
      "type": "content-similarity",
      "why": ["shared-tags: ai-ethics", "temporal-same-day"]
    }
  ],
  "generated": "2025-10-09T14:30:00Z",
  "total_files": 1234
}
Status: 200 OK
```

**GET /api/graph/node/:id**
```json
Description: Get details for specific node
Response: {
  "id": "node-001",
  "title": "ai_ethics_framework.pdf",
  "type": "document",
  "file_path": "/Documents/Oxford/AI/ai_ethics_framework.pdf",
  "primary_tags": ["ai-ethics", "oxford", "research"],
  "secondary_tags": ["reference", "important"],
  "keywords": ["fairness", "bias", "transparency"],
  "content_excerpt": "First 500 chars...",
  "connections": [
    {
      "node_id": "node-002",
      "weight": 0.85,
      "type": "content-similarity"
    }
  ],
  "metadata": {
    "size": 1048576,
    "created": "2025-10-01",
    "modified": "2025-10-09"
  }
}
Status: 200 OK, 404 Not Found
```

**GET /api/graph/cluster/:cluster**
```json
Description: Get all nodes in a cluster
Query Params: ?cluster=education
Response: {
  "cluster": "education",
  "nodes": [...],
  "count": 239,
  "avg_connections": 4.2,
  "top_tags": ["oxford", "ai-ethics", "research"]
}
Status: 200 OK
```

### Search Endpoints

**GET /api/search**
```json
Description: Full-text search across all content
Query Params:
  ?q=ai ethics
  &type=document (optional)
  &tag=oxford (optional)
  &limit=50
Response: {
  "query": "ai ethics",
  "results": [
    {
      "id": "node-001",
      "title": "ai_ethics_framework.pdf",
      "snippet": "...AI <b>ethics</b> frameworks address fairness...",
      "tags": ["ai-ethics", "oxford"],
      "type": "document",
      "score": 0.95
    }
  ],
  "count": 42,
  "time_ms": 34
}
Status: 200 OK
```

**GET /api/search/suggest**
```json
Description: Search suggestions/autocomplete
Query Params: ?q=ai
Response: {
  "suggestions": [
    {"tag": "ai-ethics", "count": 24},
    {"tag": "ai-ml", "count": 18},
    {"tag": "ai-research", "count": 12}
  ]
}
Status: 200 OK
```

### Analytics Endpoints

**GET /api/analytics/strengths**
```json
Description: Knowledge strength analysis
Response: {
  "strengths": [
    {
      "tag": "machine-learning",
      "artifact_count": 24,
      "avg_connection_strength": 0.78,
      "strength_score": 27.3
    },
    {
      "tag": "product-management",
      "artifact_count": 18,
      "avg_connection_strength": 0.82,
      "strength_score": 22.1
    }
  ]
}
Status: 200 OK
```

**GET /api/analytics/gaps**
```json
Description: Knowledge gap detection
Response: {
  "gaps": [
    {
      "tag": "finance",
      "isolated_docs": 7,
      "total_connections": 1
    },
    {
      "tag": "marketing",
      "isolated_docs": 5,
      "total_connections": 0
    }
  ]
}
Status: 200 OK
```

**GET /api/analytics/opportunities**
```json
Description: Cross-domain opportunities
Response: {
  "opportunities": [
    {
      "domains": ["machine-learning", "business-strategy"],
      "bridge_count": 5,
      "avg_strength": 0.87,
      "business_value": "high"
    },
    {
      "domains": ["ai-ethics", "product-management"],
      "bridge_count": 8,
      "avg_strength": 0.79,
      "business_value": "high"
    }
  ]
}
Status: 200 OK
```

**GET /api/analytics/recent**
```json
Description: Recent activity summary (last 7 days)
Response: {
  "recent": [
    {
      "tag": "oxford-thesis",
      "active_files": 8,
      "total_words": 15200,
      "days_active": 5
    },
    {
      "tag": "career",
      "active_files": 3,
      "total_words": 4500,
      "days_active": 2
    }
  ]
}
Status: 200 OK
```

**GET /api/analytics/time-vs-output**
```json
Description: Time allocation vs content output correlation
Response: {
  "analysis": [
    {
      "tag": "oxford",
      "calendar_hours": 15,
      "artifacts_created": 12,
      "productivity_ratio": 0.80
    },
    {
      "tag": "career",
      "calendar_hours": 8,
      "artifacts_created": 3,
      "productivity_ratio": 0.38
    }
  ]
}
Status: 200 OK
```

### Automation Endpoints

**POST /api/automation/trigger**
```json
Description: Manually trigger a background job
Request: {
  "job_type": "daily" | "weekly" | "monthly" | "ocr" | "organize"
}
Response: {
  "status": "started",
  "job_id": "job-12345",
  "estimated_duration": 300
}
Status: 202 Accepted, 400 Bad Request
```

**GET /api/automation/status**
```json
Description: Get status of all background jobs
Response: {
  "daily": {
    "last_run": "2025-10-09T02:00:00Z",
    "next_run": "2025-10-10T02:00:00Z",
    "status": "success",
    "duration": 247,
    "files_processed": 157,
    "errors": 2
  },
  "weekly": {
    "last_run": "2025-10-06T23:00:00Z",
    "next_run": "2025-10-13T23:00:00Z",
    "status": "success",
    "duration": 342,
    "notes_synced": 45,
    "errors": 0
  },
  "monthly": {
    "last_run": "2025-10-01T03:00:00Z",
    "next_run": "2025-11-01T03:00:00Z",
    "status": "success",
    "duration": 189,
    "logs_archived": 24,
    "errors": 0
  }
}
Status: 200 OK
```

**GET /api/automation/logs/:job_type**
```json
Description: Get execution logs for a job
Query Params: ?limit=100&offset=0
Response: {
  "job_type": "daily",
  "logs": [
    {
      "timestamp": "2025-10-09T02:00:34Z",
      "level": "INFO",
      "message": "Processing 157 new files"
    },
    {
      "timestamp": "2025-10-09T02:01:56Z",
      "level": "WARNING",
      "message": "OCR failed for screenshot_2025-10-08.png"
    }
  ],
  "total": 247
}
Status: 200 OK
```

**GET /api/automation/metrics**
```json
Description: Get automation performance metrics
Response: {
  "files_processed_today": 157,
  "error_rate_24h": 0.03,
  "time_saved_estimate": 1200,
  "tagging_accuracy": 0.94,
  "avg_job_duration": 245
}
Status: 200 OK
```

### Changelog Endpoints

**GET /api/changelog**
```json
Description: Get recent file moves/changes
Query Params:
  ?location=desktop (optional)
  &days=7 (optional)
  &limit=100
Response: {
  "changes": [
    {
      "date": "2025-10-09T02:06:12Z",
      "file": "screenshot.png",
      "old_path": "/Desktop/screenshot.png",
      "new_path": "/Documents/Oxford/screenshot.png",
      "reason": "Tagged as oxford",
      "tags": ["oxford", "screenshot"],
      "action": "moved"
    },
    {
      "date": "2025-10-09T02:05:45Z",
      "file": "resume.pdf",
      "old_path": "/Downloads/resume.pdf",
      "new_path": "/Documents/Career/resume.pdf",
      "reason": "Tagged as career",
      "tags": ["career", "resume"],
      "action": "moved"
    }
  ],
  "count": 25,
  "locations": ["desktop", "downloads"]
}
Status: 200 OK
```

**POST /api/changelog/undo**
```json
Description: Undo a file move
Request: {
  "change_id": "change-12345",
  "file_path": "/Documents/Oxford/screenshot.png"
}
Response: {
  "status": "success",
  "restored_path": "/Desktop/screenshot.png"
}
Status: 200 OK, 404 Not Found, 409 Conflict
```

---

## 5. Frontend Pages

### Main Graph View (`/`)

**Purpose:** Interactive knowledge graph visualization

**Features:**
- Force-directed graph (D3.js)
- Layout modes: Organic, Circular, Grid, Hierarchical
- Node hover tooltips
- Click to highlight connections
- Zoom/pan navigation
- Dynamic insights panel
- Cluster legend with filters
- Theme toggle (light/dark)

**Components:**
- Navigation bar (top)
- Graph canvas (main area)
- Insights panel (bottom left)
- Legend bar (bottom)

**User Interactions:**
1. Drag nodes to reposition
2. Hover for file details
3. Click node to highlight connections
4. Click legend item to filter by cluster
5. Click layout link to change visualization
6. Toggle theme (moon/sun icon)

**Layout Modes:**

*Organic (Default):*
```javascript
// Force-directed natural clustering
simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).distance(100))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(width/2, height/2))
    .force("collision", d3.forceCollide().radius(d => d.size * 2));
```

*Circular:*
```javascript
// Nodes arranged in circle
nodes.forEach((d, i) => {
    const angle = (i / nodes.length) * 2 * Math.PI;
    d.fx = centerX + radius * Math.cos(angle);
    d.fy = centerY + radius * Math.sin(angle);
});
```

*Grid:*
```javascript
// Systematic grid layout
const cols = Math.ceil(Math.sqrt(nodes.length));
nodes.forEach((d, i) => {
    d.fx = (i % cols) * cellWidth + margin;
    d.fy = Math.floor(i / cols) * cellHeight + margin;
});
```

*Hierarchical:*
```javascript
// Radial cluster grouping
clusters.forEach((clusterNodes, clusterName) => {
    const clusterAngle = clusterIndex * (2 * Math.PI / clusterCount);
    const clusterX = centerX + clusterRadius * Math.cos(clusterAngle);
    const clusterY = centerY + clusterRadius * Math.sin(clusterAngle);

    clusterNodes.forEach((node, i) => {
        const nodeAngle = (i / clusterNodes.length) * 2 * Math.PI;
        node.fx = clusterX + nodeRadius * Math.cos(nodeAngle);
        node.fy = clusterY + nodeRadius * Math.sin(nodeAngle);
    });
});
```

### Automation Control (`/automation`)

**Purpose:** Manage background jobs and view metrics

**Features:**
- Manual job triggers (Daily, Weekly, Monthly, Test)
- Job status dashboard (last run, next run, duration)
- Metrics panel (files processed, error rate, time saved)
- Real-time log viewer
- Report generation
- Export data

**Controls:**
- Run Daily Job - triggers immediate scan/organization
- Run Weekly Job - triggers notes/calendar sync
- Run Monthly Job - triggers maintenance
- Run Test - dry run without file moves

**Metrics Display:**
- Files Processed Today
- Error Rate (last 24 hours)
- Time Saved (vs. manual organization)
- Tagging Accuracy

**Example UI:**
```
┌──────────────────────────────────────────────────────────┐
│ Automation Control Panel                                 │
├──────────────────────────────────────────────────────────┤
│                                                           │
│ Job Status                                               │
│ ┌──────────────────────────────────────────────────┐    │
│ │ Daily Job          [Run Now]                     │    │
│ │ Last Run: Oct 9, 2025 2:00 AM                    │    │
│ │ Next Run: Oct 10, 2025 2:00 AM                   │    │
│ │ Duration: 4m 7s | Status: Success | Errors: 2    │    │
│ └──────────────────────────────────────────────────┘    │
│                                                           │
│ Performance Metrics                                      │
│ ┌──────────────────────────────────────────────────┐    │
│ │ Files Processed Today: 157                       │    │
│ │ Error Rate (24h): 1.3%                           │    │
│ │ Time Saved: 20 minutes                           │    │
│ │ Tagging Accuracy: 94%                            │    │
│ └──────────────────────────────────────────────────┘    │
│                                                           │
│ Recent Activity Log                                      │
│ ┌──────────────────────────────────────────────────┐    │
│ │ 02:00:34 [INFO] Processing 157 new files         │    │
│ │ 02:01:56 [WARN] OCR failed for screenshot.png    │    │
│ │ 02:03:42 [INFO] Moved 45 files                   │    │
│ └──────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────┘
```

### Search Interface (`/search`)

**Purpose:** Find files by content, tags, or filename

**Features:**
- Search bar with autocomplete
- Filter by type, date, tags
- Full-text search (FTS5)
- Results with snippets
- Click to open file or view in graph
- Save searches
- Advanced query syntax

**Search Syntax:**
```
ai ethics                    → Full-text search
tag:oxford                   → Filter by tag
type:document                → Filter by type
date:2025-10                → Filter by date
oxford AND thesis            → Boolean AND
oxford OR research           → Boolean OR
"exact phrase"               → Exact match
tag:oxford type:screenshot   → Combined filters
```

**Example UI:**
```
┌──────────────────────────────────────────────────────────┐
│ Search Knowledge Graph                                   │
│ ┌────────────────────────────────────────────────────┐  │
│ │ ai ethics                                     [🔍] │  │
│ └────────────────────────────────────────────────────┘  │
│                                                           │
│ Filters: [Type: All ▼] [Tags: All ▼] [Date: All ▼]     │
│                                                           │
│ 42 results (34ms)                                        │
│                                                           │
│ ┌────────────────────────────────────────────────────┐  │
│ │ ai_ethics_framework.pdf                            │  │
│ │ ...AI ethics frameworks address fairness...        │  │
│ │ Tags: ai-ethics, oxford, research                  │  │
│ │ Modified: Oct 9, 2025                              │  │
│ └────────────────────────────────────────────────────┘  │
│                                                           │
│ ┌────────────────────────────────────────────────────┐  │
│ │ Screenshot_2025-10-05.png                          │  │
│ │ ...10 Essential AI Ethics Frameworks...            │  │
│ │ Tags: ai-ethics, screenshot                        │  │
│ │ Modified: Oct 5, 2025                              │  │
│ └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

### Analytics Dashboard (`/analytics`)

**Purpose:** Visualize knowledge insights and patterns

**Features:**
- Strength bubbles (what you're good at)
- Cross-domain network (opportunities)
- Knowledge gaps bar chart
- Time vs. output scatter plot
- Recent activity timeline
- Business value quadrant

**Interactive Charts:**
- Click data point to view related files
- Hover for detailed tooltips
- Filter by date range
- Export as CSV/JSON

**Example Views:**

*Knowledge Strengths (Bubble Chart):*
```
Bubble size = artifact count
Color = domain category
Position = connection strength
```

*Cross-Domain Network:*
```
Nodes = domains (tags)
Edges = shared files/connections
Thickness = bridge strength
```

*Knowledge Gaps (Bar Chart):*
```
X-axis = tags
Y-axis = isolated document count
Color = urgency level
```

*Time vs Output (Scatter Plot):*
```
X-axis = calendar hours spent
Y-axis = artifacts created
Color = domain
Trend line = productivity correlation
```

### Changelog Viewer (`/changelog`)

**Purpose:** Audit trail of file moves and changes

**Features:**
- Chronological list of changes
- Filter by location, date, action
- Search by filename
- Undo functionality (restore to old path)
- Archive old logs
- Export report

**Display Format:**
```
┌──────────────────────────────────────────────────────────┐
│ Change Log                                               │
│                                                           │
│ Filter: [Location: All ▼] [Date: Last 7 days ▼]         │
│                                                           │
│ ┌────────────────────────────────────────────────────┐  │
│ │ Oct 9, 2025 2:06:12 AM                             │  │
│ │ screenshot_ethics.png                              │  │
│ │ Moved: /Desktop → /Documents/Oxford/AI_Ethics/     │  │
│ │ Reason: Tagged as [oxford, ai-ethics, screenshot]  │  │
│ │ [Undo] [View in Graph]                             │  │
│ └────────────────────────────────────────────────────┘  │
│                                                           │
│ ┌────────────────────────────────────────────────────┐  │
│ │ Oct 9, 2025 2:05:45 AM                             │  │
│ │ resume_2025.pdf                                    │  │
│ │ Moved: /Downloads → /Documents/Career/             │  │
│ │ Reason: Tagged as [career, resume]                 │  │
│ │ [Undo] [View in Graph]                             │  │
│ └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

## 6. Flask Application Structure

### Application Initialization

**src/app.py**
```python
from flask import Flask, send_from_directory
from src.config import Config
from src.api import graph_bp, search_bp, analytics_bp, automation_bp, changelog_bp
from src.utils.logger import setup_logging

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__,
                static_folder='../frontend/static',
                template_folder='../frontend')
    app.config.from_object(config_class)

    # Setup logging
    setup_logging(app.config['LOG_LEVEL'])

    # Register blueprints
    app.register_blueprint(graph_bp, url_prefix='/api/graph')
    app.register_blueprint(search_bp, url_prefix='/api/search')
    app.register_blueprint(analytics_bp, url_prefix='/api/analytics')
    app.register_blueprint(automation_bp, url_prefix='/api/automation')
    app.register_blueprint(changelog_bp, url_prefix='/api/changelog')

    # Serve frontend pages
    @app.route('/')
    def index():
        return send_from_directory('../frontend', 'index.html')

    @app.route('/automation')
    def automation():
        return send_from_directory('../frontend', 'automation.html')

    @app.route('/search')
    def search():
        return send_from_directory('../frontend', 'search.html')

    @app.route('/analytics')
    def analytics():
        return send_from_directory('../frontend', 'analytics.html')

    @app.route('/changelog')
    def changelog():
        return send_from_directory('../frontend', 'changelog.html')

    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500

    # Request/response middleware
    @app.before_request
    def log_request():
        """Log all API requests"""
        from flask import request
        import logging
        logger = logging.getLogger('api')
        logger.info(f"{request.method} {request.path}")

    @app.after_request
    def add_cors_headers(response):
        """Add CORS headers for local development"""
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5000'
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=False)
```

### Configuration Management

**src/config.py**
```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Database
    DATABASE_PATH = Path(os.environ.get('DATABASE_PATH',
                         '~/Library/Application Support/knowledge_map/knowledge_graph.db')).expanduser()

    # API Keys
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    ENABLE_CLOUD_AI = os.environ.get('ENABLE_CLOUD_AI', 'true').lower() == 'true'

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    LOG_DIR = Path('~/Library/Logs/knowledge_map').expanduser()

    # Monitored Locations
    MONITORED_PATHS = [
        Path.home() / 'Library/Mobile Documents/com~apple~CloudDocs/Documents',
        Path.home() / 'Downloads',
        Path.home() / 'Desktop'
    ]

    # Job Schedules
    DAILY_JOB_TIME = '02:00'
    WEEKLY_JOB_TIME = 'Sunday 23:00'
    MONTHLY_JOB_TIME = '1st 03:00'

    # Performance
    BATCH_SIZE = 50
    MAX_WORKERS = 10
    API_TIMEOUT = 30
    CACHE_TTL = 3600  # 1 hour

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LOG_LEVEL = 'INFO'
```

### Blueprint Structure

**src/api/graph.py**
```python
from flask import Blueprint, jsonify, request
from src.database.queries import get_graph_data, get_node_by_id, get_cluster_nodes

graph_bp = Blueprint('graph', __name__)

@graph_bp.route('/data')
def graph_data():
    """Get full graph data for visualization"""
    try:
        data = get_graph_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@graph_bp.route('/node/<node_id>')
def node_details(node_id):
    """Get node details"""
    try:
        node = get_node_by_id(node_id)
        if not node:
            return jsonify({'error': 'Node not found'}), 404
        return jsonify(node)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@graph_bp.route('/cluster/<cluster>')
def cluster_data(cluster):
    """Get all nodes in a cluster"""
    try:
        nodes = get_cluster_nodes(cluster)
        return jsonify({
            'cluster': cluster,
            'nodes': nodes,
            'count': len(nodes)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

**src/api/search.py**
```python
from flask import Blueprint, jsonify, request
from src.database.queries import full_text_search, get_search_suggestions

search_bp = Blueprint('search', __name__)

@search_bp.route('')
def search():
    """Full-text search"""
    query = request.args.get('q', '')
    type_filter = request.args.get('type')
    tag_filter = request.args.get('tag')
    limit = int(request.args.get('limit', 50))

    if not query:
        return jsonify({'error': 'Query parameter required'}), 400

    try:
        results = full_text_search(query, type_filter, tag_filter, limit)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@search_bp.route('/suggest')
def suggest():
    """Search suggestions"""
    prefix = request.args.get('q', '')

    try:
        suggestions = get_search_suggestions(prefix)
        return jsonify({'suggestions': suggestions})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

---

## 7. Deployment

### Local Development Setup

**Prerequisites:**
```bash
macOS 12+ (Monterey or later)
Python 3.9+
pip 21+
Git
```

**Installation Steps:**

1. Clone repository
```bash
cd ~/Documents/_AUTOMATION/Claude_Projects
git clone [repo-url] knowledge_map
cd knowledge_map
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment
```bash
cp .env.example .env
# Edit .env and add ANTHROPIC_API_KEY
nano .env
```

5. Initialize database
```bash
python scripts/setup_database.py
```

6. Run application
```bash
python src/app.py
```

7. Open browser
```
http://localhost:5000
```

**Development Workflow:**
```bash
# Activate virtual environment
source venv/bin/activate

# Run tests
pytest

# Format code
black src/

# Lint code
pylint src/

# Start Flask app
python src/app.py
```

### Production Deployment (macOS LaunchAgent)

**Purpose:** Run Flask app as persistent background service

**LaunchAgent Plist (Flask Server):**

File: `~/Library/LaunchAgents/com.knowledge_map.server.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge_map.server</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/venv/bin/python3</string>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/src/app.py</string>
    </array>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/server.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/server_error.log</string>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin</string>
        <key>PYTHONUNBUFFERED</key>
        <string>1</string>
    </dict>

    <key>WorkingDirectory</key>
    <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map</string>
</dict>
</plist>
```

**Background Jobs (Separate LaunchAgents):**

**Daily Job Plist:**
File: `~/Library/LaunchAgents/com.knowledge_map.daily.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge_map.daily</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/venv/bin/python3</string>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/src/jobs/daily.py</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/jobs/daily.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/jobs/daily_error.log</string>

    <key>WorkingDirectory</key>
    <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map</string>
</dict>
</plist>
```

**Weekly Job Plist:**
File: `~/Library/LaunchAgents/com.knowledge_map.weekly.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge_map.weekly</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/venv/bin/python3</string>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/src/jobs/weekly.py</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>0</integer>
        <key>Hour</key>
        <integer>23</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/jobs/weekly.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/jobs/weekly_error.log</string>

    <key>WorkingDirectory</key>
    <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map</string>
</dict>
</plist>
```

**Monthly Job Plist:**
File: `~/Library/LaunchAgents/com.knowledge_map.monthly.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge_map.monthly</string>

    <key>ProgramArguments</key>
    <array>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/venv/bin/python3</string>
        <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map/src/jobs/monthly.py</string>
    </array>

    <key>StartCalendarInterval</key>
    <dict>
        <key>Day</key>
        <integer>1</integer>
        <key>Hour</key>
        <integer>3</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>

    <key>StandardOutPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/jobs/monthly.log</string>

    <key>StandardErrorPath</key>
    <string>/Users/jennifermckinney/Library/Logs/knowledge_map/jobs/monthly_error.log</string>

    <key>WorkingDirectory</key>
    <string>/Users/jennifermckinney/Documents/_AUTOMATION/Claude_Projects/knowledge_map</string>
</dict>
</plist>
```

**Installation Script:**

File: `scripts/install_launchd.sh`
```bash
#!/bin/bash

# Knowledge Map LaunchAgent Installation Script

LAUNCHAGENTS_DIR=~/Library/LaunchAgents
LOG_DIR=~/Library/Logs/knowledge_map

# Create directories
mkdir -p "$LAUNCHAGENTS_DIR"
mkdir -p "$LOG_DIR/jobs"

# Copy plist files
echo "Installing LaunchAgents..."
cp scripts/com.knowledge_map.server.plist "$LAUNCHAGENTS_DIR/"
cp scripts/com.knowledge_map.daily.plist "$LAUNCHAGENTS_DIR/"
cp scripts/com.knowledge_map.weekly.plist "$LAUNCHAGENTS_DIR/"
cp scripts/com.knowledge_map.monthly.plist "$LAUNCHAGENTS_DIR/"

# Load services
echo "Loading services..."
launchctl load "$LAUNCHAGENTS_DIR/com.knowledge_map.server.plist"
launchctl load "$LAUNCHAGENTS_DIR/com.knowledge_map.daily.plist"
launchctl load "$LAUNCHAGENTS_DIR/com.knowledge_map.weekly.plist"
launchctl load "$LAUNCHAGENTS_DIR/com.knowledge_map.monthly.plist"

# Verify
echo "Verifying installation..."
launchctl list | grep knowledge_map

echo "Installation complete!"
echo "Flask server should be running at http://localhost:5000"
echo "Check logs at: $LOG_DIR"
```

**Management Commands:**
```bash
# Load all services
launchctl load ~/Library/LaunchAgents/com.knowledge_map.*.plist

# Unload all services
launchctl unload ~/Library/LaunchAgents/com.knowledge_map.*.plist

# Check status
launchctl list | grep knowledge_map

# View logs
tail -f ~/Library/Logs/knowledge_map/server.log
tail -f ~/Library/Logs/knowledge_map/jobs/daily.log

# Restart Flask server
launchctl stop com.knowledge_map.server
launchctl start com.knowledge_map.server

# Trigger manual job
launchctl start com.knowledge_map.daily
```

---

## 8. Performance Targets

### System Performance

| Metric | Target | Strategy |
|--------|--------|----------|
| Daily scan (10k files) | <5 minutes | Incremental scanning, parallel processing |
| Search query | <100ms | FTS5 indexing, query result caching |
| Graph render (1000 nodes) | <3 seconds | Canvas rendering, lazy loading |
| OCR per screenshot | <2 seconds | Apple Vision API, batch processing |
| API response time | <200ms | Database indexes, connection pooling |
| Database query | <50ms | Optimized indexes, prepared statements |

### Resource Usage

```
Memory: <200 MB (idle), <500 MB (scanning)
CPU: <5% (idle), <50% (scanning)
Disk: ~50 MB (database for 10k files)
Network: None (except optional Claude API)
```

### Scalability Targets

```
Files: 10,000 - 100,000
Nodes: 10,000 - 50,000
Edges: 50,000 - 500,000
Tags: 100 - 1,000 unique
Daily processing: 100 - 500 new files
Concurrent users: 1 (single-user system)
```

### Performance Optimizations

**Database:**
- Indexed queries on common columns
- FTS5 for fast full-text search
- Connection pooling (max 5 connections)
- Query result caching (1 hour TTL)
- Prepared statements for repeated queries

**File Scanning:**
- Incremental scanning (only new/modified via mtime)
- Content hash comparison (skip unchanged via SHA-256)
- Parallel content extraction (ThreadPoolExecutor, 10 workers)
- Batch processing (50 files per batch)

**Frontend:**
- D3.js force simulation optimization (alpha decay)
- Canvas rendering for large graphs (>1000 nodes)
- Lazy loading of node details
- Debounced search input (300ms)
- Virtualized lists for large result sets

**API:**
- Response compression (gzip)
- ETag caching
- Pagination for large datasets
- Rate limiting (100 req/min per IP)

---

## 9. Data Flow Examples

### Example 1: New Screenshot Flow

**Scenario:** User takes a screenshot during Oxford AI Programme lecture

```
1. USER takes screenshot → saves to Desktop
   File: Screenshot_2025-10-09_14-32.png

2. DAILY JOB (2:00 AM next day)
   ↓
   Scanner detects new file: Screenshot_2025-10-09_14-32.png
   - Check mtime: modified since last scan
   - Calculate hash: sha256:abc123...
   ↓
   Extractor runs OCR → "10 AI Ethics Frameworks..."
   - Apple Vision API processes image
   - Extracts text with 92% confidence
   - Duration: 1.8 seconds
   ↓
   Tagger calls Claude API
   - Context: Recent calendar event "Oxford AI Programme"
   - Content: "10 AI Ethics Frameworks, fairness, transparency..."
   - Location: Desktop (pending organization)
   ↓
   Claude returns tags:
   {
     "primary_tags": ["ai-ethics", "oxford", "screenshot"],
     "secondary_tags": ["infographic", "learning", "framework"],
     "keywords": ["fairness", "transparency", "accountability"],
     "reasoning": "Educational screenshot from Oxford AI Programme"
   }
   ↓
   Relationship Engine
   - Finds similar nodes (ai_ethics_framework.pdf)
   - Calculates cosine similarity: 0.85
   - Creates edge (weight=0.85, type=content-similarity)
   - Finds temporal match: oxford_notes.md (same day)
   - Creates edge (weight=1.0, type=temporal)
   ↓
   Organizer
   - Destination: /Documents/Education/Oxford/AI_Ethics/
   - Move file (not copy)
   - Update node with new path
   ↓
   Change Logger
   - Create entry in Desktop/CHANGELOG.json:
   {
     "date": "2025-10-10T02:06:12Z",
     "file": "Screenshot_2025-10-09_14-32.png",
     "old_path": "/Desktop/Screenshot_2025-10-09_14-32.png",
     "new_path": "/Documents/Education/Oxford/AI_Ethics/Screenshot_2025-10-09_14-32.png",
     "reason": "Tagged as oxford, ai-ethics",
     "tags": ["ai-ethics", "oxford", "screenshot"]
   }
   ↓
   Database
   - INSERT INTO nodes (id, type, file_path, ...)
   - INSERT INTO tags (node_id, tag, tag_type)
   - INSERT INTO edges (source, target, weight, ...)
   - Update FTS5 index
   - Transaction commit
   ↓
   Duration: 3.2 seconds total

3. USER opens web interface (8:00 AM)
   ↓
   Graph visualization loads
   - New node appears in Education cluster
   - Connected to ai_ethics_framework.pdf (thick edge)
   - Connected to oxford_notes.md (dashed edge)
   ↓
   USER searches "ai ethics frameworks"
   - Screenshot appears in results
   - Click → opens file location
   - Shows connections in graph
```

### Example 2: Search Flow

**Scenario:** User searches for "ai ethics" content

```
1. USER types "ai eth" in search bar
   ↓
2. FRONTEND
   - Debounce input (300ms delay)
   - After 300ms, call /api/search/suggest?q=ai%20eth
   ↓
3. API ENDPOINT /api/search/suggest
   ↓
4. DATABASE QUERY (Autocomplete)
   SELECT tag, COUNT(*) as count
   FROM tags
   WHERE tag LIKE 'ai-eth%'
   GROUP BY tag
   ORDER BY count DESC
   LIMIT 5;
   ↓
5. RESPONSE
   {
     "suggestions": [
       {"tag": "ai-ethics", "count": 24},
       {"tag": "ai-ethics-framework", "count": 5}
     ]
   }
   ↓
6. USER sees dropdown suggestions, selects "ai-ethics"
   ↓
7. USER presses Enter → full search
   ↓
8. FRONTEND calls /api/search?q=ai%20ethics&limit=50
   ↓
9. API ENDPOINT /api/search
   ↓
10. DATABASE QUERY (FTS5)
    SELECT
        n.id,
        n.file_name,
        n.type,
        snippet(nodes_fts, 1, '<b>', '</b>', '...', 64) as snippet,
        bm25(nodes_fts) as score
    FROM nodes n
    JOIN nodes_fts ON n.id = nodes_fts.id
    WHERE nodes_fts MATCH 'ai ethics'
    ORDER BY score
    LIMIT 50;
    ↓
    Duration: 34ms
    ↓
11. RESPONSE
    {
      "query": "ai ethics",
      "results": [
        {
          "id": "node-001",
          "title": "ai_ethics_framework.pdf",
          "snippet": "...AI <b>ethics</b> frameworks address fairness...",
          "tags": ["ai-ethics", "oxford"],
          "type": "document",
          "score": 2.4
        },
        {
          "id": "node-002",
          "title": "Screenshot_2025-10-09.png",
          "snippet": "...10 Essential <b>AI</b> <b>Ethics</b> Frameworks...",
          "tags": ["ai-ethics", "screenshot"],
          "type": "screenshot",
          "score": 2.1
        }
      ],
      "count": 42,
      "time_ms": 34
    }
    ↓
12. FRONTEND renders results
    - Display 42 results
    - Show highlighted snippets
    - Display search time (34ms)
    ↓
13. USER clicks first result
    - Opens file in default application
    - Graph view highlights node and connections
```

### Example 3: Analytics Computation Flow

**Scenario:** Weekly job pre-computes analytics for dashboard

```
1. WEEKLY JOB (Sunday 11:00 PM)
   ↓
2. Analytics Engine starts
   ↓
3. QUERY: Knowledge Strengths
   - Count artifacts per tag
   - Calculate avg connection strength
   - Compute strength score = count × avg_strength
   ↓
   SELECT
       t.tag,
       COUNT(DISTINCT t.node_id) as artifact_count,
       AVG(e.weight) as avg_connection_strength,
       (COUNT(DISTINCT t.node_id) * AVG(e.weight)) as strength_score
   FROM tags t
   LEFT JOIN edges e ON t.node_id = e.source OR t.node_id = e.target
   WHERE t.tag_type = 'primary'
   GROUP BY t.tag
   HAVING artifact_count >= 3
   ORDER BY strength_score DESC
   LIMIT 10;
   ↓
   Results:
   [
     {"tag": "ai-ethics", "artifact_count": 24, "strength_score": 27.3},
     {"tag": "oxford", "artifact_count": 22, "strength_score": 24.8}
   ]
   ↓
   Store in analytics_cache:
   INSERT INTO analytics_cache (query_name, result_json, computed_at)
   VALUES ('knowledge_strengths', '[...]', CURRENT_TIMESTAMP);
   ↓
4. QUERY: Cross-Domain Opportunities
   - Find relationships where source_domain != target_domain
   - Group by domain pairs
   - Calculate bridge counts and strengths
   ↓
   SELECT
       t1.tag as domain1,
       t2.tag as domain2,
       COUNT(DISTINCT e.id) as bridge_count,
       AVG(e.weight) as avg_strength
   FROM edges e
   JOIN tags t1 ON e.source = t1.node_id
   JOIN tags t2 ON e.target = t2.node_id
   WHERE t1.tag != t2.tag
     AND t1.tag_type = 'primary'
     AND t2.tag_type = 'primary'
   GROUP BY t1.tag, t2.tag
   HAVING bridge_count >= 3
   ORDER BY avg_strength DESC
   LIMIT 10;
   ↓
   Store in analytics_cache
   ↓
5. QUERY: Knowledge Gaps
   - Find nodes with <2 connections
   - Group by primary tag
   - Identify isolated clusters
   ↓
   SELECT
       t.tag,
       COUNT(DISTINCT n.id) as isolated_docs,
       COUNT(DISTINCT e.id) as total_connections
   FROM tags t
   JOIN nodes n ON t.node_id = n.id
   LEFT JOIN edges e ON n.id = e.source OR n.id = e.target
   WHERE t.tag_type = 'primary'
   GROUP BY t.tag
   HAVING total_connections < 2
   ORDER BY isolated_docs DESC;
   ↓
   Store in analytics_cache
   ↓
6. Total Duration: ~45 seconds for all queries

7. USER opens /analytics (Monday morning)
   ↓
8. FRONTEND calls /api/analytics/strengths
   ↓
9. API reads from analytics_cache (instant!)
   ↓
10. FRONTEND renders charts (D3.js, Chart.js)
    - Strength bubbles
    - Cross-domain network
    - Knowledge gaps bar chart
    - All data pre-computed, loads in <1 second
```

---

## 10. Error Handling Strategies

### Principle: Fail Gracefully

**Never crash the entire system due to a single file error**

### File Access Errors

**Error Types:**
- Permission denied
- File not found
- File locked by another process
- Disk read error

**Handling:**
```python
def process_file(file_path):
    """Process a single file with error handling"""
    try:
        content = extract_content(file_path)
        tags = tag_content(content)
        store_node(file_path, content, tags)
        return True

    except PermissionError:
        logger.warning(f"Permission denied: {file_path}")
        return None  # Skip this file, continue with others

    except FileNotFoundError:
        logger.error(f"File disappeared during scan: {file_path}")
        return None  # File was deleted, skip

    except IOError as e:
        logger.error(f"IO error reading {file_path}: {e}")
        return None  # Disk error, skip file

    except Exception as e:
        logger.error(f"Unexpected error processing {file_path}: {e}", exc_info=True)
        return None  # Catch-all, don't crash
```

**User Notification:**
- Log to file (all errors)
- Daily summary email (if >10% files fail)
- Dashboard warning banner (immediate for critical errors)
- Retry queue (attempt again next run)

### OCR Failures

**Error Types:**
- Corrupted image
- Unsupported format
- OCR timeout
- Low confidence result (<50%)

**Handling:**
```python
def extract_screenshot_text(image_path, timeout=5):
    """Extract text from screenshot with fallback"""
    try:
        # Attempt primary OCR (Apple Vision)
        text, confidence = run_apple_vision(image_path, timeout=timeout)

        if confidence < 0.5:
            logger.warning(f"Low OCR confidence ({confidence}): {image_path}")
            # Still use result, but flag for review

        return text, confidence

    except TimeoutError:
        logger.error(f"OCR timeout (>{timeout}s): {image_path}")
        # Fallback to Tesseract
        try:
            text = run_tesseract(image_path, timeout=timeout)
            return text, 0.6  # Assume moderate confidence
        except:
            return "", 0.0  # Empty content, tag by filename only

    except UnsupportedFormatError:
        logger.error(f"Unsupported image format: {image_path}")
        return "", 0.0

    except Exception as e:
        logger.error(f"OCR failed: {image_path}: {e}")
        return "", 0.0
```

**Fallback Strategy:**
1. Apple Vision API (primary)
2. Tesseract OCR (secondary)
3. Filename pattern matching (tertiary)
4. Location context tagging (last resort)
5. Mark as `[ocr-failed]` for manual review

### API Failures (Claude)

**Error Types:**
- Rate limit exceeded (429)
- API timeout
- Authentication error (401)
- Invalid response format
- Network error

**Handling:**
```python
import anthropic

def tag_with_claude(content, context, max_retries=3):
    """Call Claude API with retry and fallback"""

    for attempt in range(max_retries):
        try:
            response = anthropic_client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                messages=[{"role": "user", "content": build_prompt(content, context)}]
            )
            return parse_claude_response(response)

        except anthropic.RateLimitError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                logger.warning(f"Rate limit hit, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                logger.warning("Rate limit exceeded, using local NLP")
                return tag_with_local_nlp(content, context)

        except anthropic.APITimeoutError:
            logger.warning(f"API timeout (attempt {attempt + 1})")
            if attempt == max_retries - 1:
                return tag_with_local_nlp(content, context)

        except anthropic.AuthenticationError:
            logger.error("Claude API authentication failed")
            return tag_with_local_nlp(content, context)

        except anthropic.APIError as e:
            logger.error(f"Claude API error: {e}")
            return tag_with_local_nlp(content, context)

        except Exception as e:
            logger.error(f"Unexpected API error: {e}")
            return tag_with_local_nlp(content, context)

    # All retries failed
    return tag_with_local_nlp(content, context)
```

**Fallback Chain:**
```
Claude API → (retry 3x with backoff) → Local NLP (spaCy + TF-IDF) → Rule-based → Filename heuristics
```

### Database Errors

**Error Types:**
- Database locked (SQLITE_BUSY)
- Disk full
- Corruption (SQLITE_CORRUPT)
- Constraint violations

**Handling:**
```python
import sqlite3
import time

def insert_node_with_retry(node_data, max_retries=5):
    """Insert node with retry logic for locked database"""

    for attempt in range(max_retries):
        try:
            conn = get_db_connection()
            conn.execute("BEGIN IMMEDIATE")  # Prevent locks

            conn.execute(
                "INSERT INTO nodes (id, type, file_path, ...) VALUES (?, ?, ?, ...)",
                node_data
            )

            conn.commit()
            return True

        except sqlite3.OperationalError as e:
            if "database is locked" in str(e).lower():
                if attempt < max_retries - 1:
                    wait_time = 0.1 * (2 ** attempt)  # Exponential backoff
                    logger.debug(f"Database locked, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Database locked after {max_retries} attempts")
                    return False
            else:
                logger.error(f"Database operational error: {e}")
                return False

        except sqlite3.IntegrityError as e:
            logger.warning(f"Constraint violation (likely duplicate): {e}")
            return False  # Already exists, not an error

        except sqlite3.DatabaseError as e:
            if "corrupt" in str(e).lower():
                logger.critical(f"DATABASE CORRUPTION DETECTED: {e}")
                # Attempt restore from backup
                restore_from_backup()
            else:
                logger.error(f"Database error: {e}")
            return False

        except Exception as e:
            logger.error(f"Unexpected database error: {e}", exc_info=True)
            return False

    return False
```

**Critical Errors (Alert User):**
- Database corruption → Restore from backup immediately
- Disk full → Notify user to free space
- >50% of files fail → System check required
- Backup restoration needed → User confirmation

### Network Errors

**Error Types:**
- No internet connection (when using Claude API)
- DNS resolution failure
- Connection timeout
- SSL certificate errors

**Handling:**
```python
import requests

def check_api_available(timeout=2):
    """Test if Claude API is reachable"""
    try:
        response = requests.head(
            "https://api.anthropic.com",
            timeout=timeout
        )
        return response.status_code < 500
    except requests.RequestException:
        return False

# In daily job
if ENABLE_CLOUD_AI:
    if check_api_available():
        use_claude = True
        logger.info("Claude API available")
    else:
        use_claude = False
        logger.info("Claude API unavailable, using local NLP")
else:
    use_claude = False
    logger.info("Cloud AI disabled by user, using local NLP")
```

### Logging Strategy

**Log Levels:**
```
DEBUG: Verbose details (disabled in production)
  Example: "Processing file: /path/to/file.pdf"

INFO: Normal operations (default level)
  Example: "Daily job completed: 157 files processed"

WARNING: Recoverable issues (system continues)
  Example: "OCR failed for screenshot.png, using filename"

ERROR: Failures requiring attention (but not critical)
  Example: "10% of files failed processing"

CRITICAL: System-level failures (immediate action)
  Example: "Database corruption detected"
```

**Log Locations:**
```
~/Library/Logs/knowledge_map/
├── app.log              # Main application (INFO+)
├── api.log              # API requests/responses
├── jobs/
│   ├── daily.log        # Daily job execution
│   ├── weekly.log       # Weekly job execution
│   └── monthly.log      # Monthly job execution
├── errors.log           # All ERROR and CRITICAL
└── debug.log            # DEBUG level (development only)
```

**Log Format:**
```
2025-10-09 02:01:34 [INFO] [scanner] Starting daily file scan
2025-10-09 02:01:35 [INFO] [scanner] Found 157 new files, 23 modified
2025-10-09 02:01:56 [WARNING] [ocr] Failed to process screenshot_2025-10-08.png
Context: Unsupported image format (WebP)
2025-10-09 02:02:15 [INFO] [ocr] Completed: 11 success, 1 failed
2025-10-09 02:03:42 [INFO] [organizer] Moved 45 files
2025-10-09 02:03:43 [INFO] [daily_job] Daily job completed in 4m 9s
```

**Log Rotation:**
```python
import logging
from logging.handlers import RotatingFileHandler

# Rotate when file reaches 10MB, keep 5 backups
handler = RotatingFileHandler(
    'app.log',
    maxBytes=10*1024*1024,
    backupCount=5
)

# Compress old logs
# Monthly job compresses logs >30 days to .gz
# Retain error logs for 90 days
# Never auto-delete CRITICAL errors
```

---

## 11. Security Considerations

### Data Privacy

**Principle: Privacy-First Architecture**

1. **Local Processing by Default**
   - All content extraction happens locally
   - Local NLP fallback available (spaCy, scikit-learn)
   - No telemetry or usage tracking
   - No data sent to external servers (except opt-in Claude API)

2. **Optional Cloud AI**
   - User must explicitly enable Claude API in config
   - Clear disclosure in UI: "Enable AI tagging (sends content to Claude API)"
   - Can disable at any time via config or UI toggle
   - Fallback to local processing if disabled

3. **API Key Storage**
   ```bash
   # Store in .env file (not committed to git)
   ANTHROPIC_API_KEY=sk-ant-api03-...

   # File permissions: 600 (read/write owner only)
   chmod 600 .env

   # Load at runtime
   from dotenv import load_dotenv
   load_dotenv()
   ```

4. **Content Transmission**
   - Only send necessary context to API (first 2000 chars)
   - Truncate long documents
   - Never send:
     - Full file paths (only filenames)
     - User personal info
     - Sensitive metadata (permissions, owner)
   - Example prompt:
   ```python
   def build_api_prompt(content, context):
       """Build prompt with minimal sensitive data"""
       return f"""
       Analyze this content and generate tags.

       Filename: {Path(file_path).name}  # Name only, not full path
       Type: {file_type}
       Content (truncated): {content[:2000]}  # First 2000 chars

       [Instructions...]
       """
   ```

### Authentication & Authorization

**Current: Single-User, No Auth**
- Runs locally on user's machine (127.0.0.1)
- Flask binds to localhost only
- Not accessible from network
- No login required

**Security Measures:**
```python
# Flask app.py
if __name__ == '__main__':
    app.run(
        host='127.0.0.1',  # Localhost only
        port=5000,
        debug=False,  # No debug in production
        use_reloader=False
    )
```

**Future: Multi-User (Out of Scope v2.0)**
- JWT authentication
- User session management
- Role-based access control (RBAC)
- Password hashing (bcrypt)

### Input Validation

**API Endpoints:**
```python
from src.utils.validators import validate_node_id, validate_search_query, sanitize_path

@graph_bp.route('/node/<node_id>')
def node_details(node_id):
    # Validate input format
    if not validate_node_id(node_id):
        return jsonify({'error': 'Invalid node ID'}), 400

    # node_id format: UUID v4
    # Regex: ^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$

    # Use parameterized queries (prevents SQL injection)
    node = get_node_by_id(node_id)
    return jsonify(node)
```

**Validators (src/utils/validators.py):**
```python
import re
from pathlib import Path

def validate_node_id(node_id):
    """Validate UUID v4 format"""
    pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    return bool(re.match(pattern, node_id, re.IGNORECASE))

def validate_search_query(query):
    """Validate search query"""
    if not query or len(query) > 1000:
        return False
    # Allow alphanumeric, spaces, hyphens, quotes
    pattern = r'^[a-zA-Z0-9\s\-"\']+$'
    return bool(re.match(pattern, query))

def sanitize_path(user_input, allowed_roots):
    """Prevent directory traversal attacks"""
    try:
        path = Path(user_input).resolve()

        # Ensure path is within allowed directories
        if not any(path.is_relative_to(root) for root in allowed_roots):
            raise ValueError(f"Path outside allowed directories: {path}")

        # Prevent ../ traversal
        if '..' in path.parts:
            raise ValueError("Path contains '..' traversal")

        return path
    except Exception as e:
        raise ValueError(f"Invalid path: {e}")
```

### SQL Injection Prevention

**Always use parameterized queries:**
```python
# GOOD - Parameterized query (safe)
def get_node_by_id(node_id):
    cursor.execute(
        "SELECT * FROM nodes WHERE id = ?",
        (node_id,)  # Tuple of parameters
    )
    return cursor.fetchone()

# GOOD - Named parameters (safe)
def search_nodes(query, type_filter):
    cursor.execute(
        "SELECT * FROM nodes WHERE type = :type AND content MATCH :query",
        {"type": type_filter, "query": query}
    )
    return cursor.fetchall()

# BAD - String formatting (vulnerable to SQL injection)
def get_node_by_id(node_id):
    cursor.execute(f"SELECT * FROM nodes WHERE id = '{node_id}'")  # NEVER DO THIS
    return cursor.fetchone()
```

### XSS Prevention

**Sanitize user-generated content:**

**Frontend (JavaScript):**
```javascript
// Escape HTML to prevent XSS
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Display user content (safe)
function displayNodeTitle(node) {
    // Use textContent (not innerHTML)
    document.getElementById('title').textContent = node.title;
}

// Build HTML safely
function renderSearchResults(results) {
    const resultsHTML = results.map(result => `
        <div class="result">
            <h3>${escapeHtml(result.title)}</h3>
            <p>${result.snippet}</p>
        </div>
    `).join('');

    document.getElementById('results').innerHTML = resultsHTML;
}
```

**Backend (Python):**
```python
from markupsafe import escape

@app.route('/api/node/<node_id>')
def node_details(node_id):
    node = get_node_by_id(node_id)

    # Escape user content before returning
    node['title'] = escape(node['title'])
    node['content_excerpt'] = escape(node['content_excerpt'])

    return jsonify(node)
```

### File System Security

**Permissions:**
```bash
# Database file (only owner can read/write)
chmod 600 ~/Library/Application\ Support/knowledge_map/knowledge_graph.db

# Log directory (owner read/write, group read)
chmod 750 ~/Library/Logs/knowledge_map

# Configuration file (only owner can read/write)
chmod 600 .env

# Application files (standard permissions)
chmod 644 src/**/*.py
chmod 755 src/app.py scripts/*.sh
```

**Sandboxing (Future Enhancement):**
- macOS App Sandbox (restricts file system access)
- Limited file system access (only monitored directories)
- No network access (except optional API)
- No camera/microphone access

**File Access Restrictions:**
```python
# Only access files within monitored directories
ALLOWED_ROOTS = [
    Path.home() / 'Library/Mobile Documents/com~apple~CloudDocs/Documents',
    Path.home() / 'Downloads',
    Path.home() / 'Desktop'
]

def safe_read_file(file_path):
    """Read file with path validation"""
    path = sanitize_path(file_path, ALLOWED_ROOTS)

    # Check file exists and is readable
    if not path.is_file():
        raise FileNotFoundError(f"Not a file: {path}")

    if not os.access(path, os.R_OK):
        raise PermissionError(f"Cannot read: {path}")

    with open(path, 'r') as f:
        return f.read()
```

### API Key Security

**Best Practices:**
1. Never commit `.env` to git (add to `.gitignore`)
2. Use environment variables (not hardcoded)
3. Rotate keys periodically (quarterly)
4. Monitor API usage for anomalies
5. Use API key with minimal permissions

**Key Rotation:**
```bash
# Generate new Claude API key at https://console.anthropic.com

# Update .env with new key
nano .env
# Change: ANTHROPIC_API_KEY=sk-ant-api03-NEW-KEY

# Restart Flask app
launchctl stop com.knowledge_map.server
launchctl start com.knowledge_map.server

# Verify new key works
curl http://localhost:5000/api/automation/status
```

**API Usage Monitoring:**
```python
# Log all API calls
@app.before_request
def log_api_request():
    if request.path.startswith('/api/'):
        logger.info(f"API {request.method} {request.path} from {request.remote_addr}")

# Track API key usage
def track_claude_api_usage(tokens_used, cost_usd):
    """Track Claude API usage for monitoring"""
    with open('data/api_usage.json', 'a') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'tokens': tokens_used,
            'cost': cost_usd
        }, f)

    # Alert if daily budget exceeded
    if daily_cost() > 5.0:  # $5/day limit
        send_alert("API budget exceeded")
```

### Backup Security

**Encrypted Backups (Future Enhancement):**
```python
import gzip
from cryptography.fernet import Fernet

def backup_database_encrypted(db_path, backup_path, encryption_key):
    """Create encrypted, compressed backup"""

    # Read database
    with open(db_path, 'rb') as f_in:
        data = f_in.read()

    # Compress
    compressed = gzip.compress(data)

    # Encrypt
    fernet = Fernet(encryption_key)
    encrypted = fernet.encrypt(compressed)

    # Save
    with open(backup_path, 'wb') as f_out:
        f_out.write(encrypted)

    logger.info(f"Encrypted backup created: {backup_path}")

def restore_from_encrypted_backup(backup_path, db_path, encryption_key):
    """Restore from encrypted backup"""

    # Read encrypted backup
    with open(backup_path, 'rb') as f_in:
        encrypted = f_in.read()

    # Decrypt
    fernet = Fernet(encryption_key)
    compressed = fernet.decrypt(encrypted)

    # Decompress
    data = gzip.decompress(compressed)

    # Write database
    with open(db_path, 'wb') as f_out:
        f_out.write(data)

    logger.info(f"Database restored from: {backup_path}")
```

**Backup Permissions:**
```bash
# Backup directory (only owner can access)
chmod 700 ~/Library/Application\ Support/knowledge_map/backups

# Individual backups (only owner can read/write)
chmod 600 ~/Library/Application\ Support/knowledge_map/backups/*.db
```

---

## Appendix A: Database Schema Reference

See `05_GRAPH_DATABASE_SCHEMA.md` for complete schema documentation.

**Quick Reference:**

```sql
-- Core tables
nodes (id, date_created, type, file_path, primary_tags, metadata_json)
edges (id, source, target, weight, type, why_json)
tags (node_id, tag, tag_type)
analytics_cache (query_name, result_json, computed_at)

-- Key indexes
idx_nodes_type, idx_nodes_date_created, idx_nodes_file_path
idx_edges_source, idx_edges_target, idx_edges_weight
idx_tags_node_id, idx_tags_tag

-- Full-text search
nodes_fts (FTS5 virtual table)
```

---

## Appendix B: Configuration Reference

**Environment Variables (.env):**
```bash
# Required
ANTHROPIC_API_KEY=sk-ant-api03-...

# Optional
DATABASE_PATH=/custom/path/knowledge_graph.db
LOG_LEVEL=INFO|DEBUG|WARNING|ERROR
ENABLE_CLOUD_AI=true|false
FLASK_PORT=5000
FLASK_HOST=127.0.0.1
SECRET_KEY=your-secret-key-here

# Performance
BATCH_SIZE=50
MAX_WORKERS=10
CACHE_TTL=3600
```

**User Configuration (data/config.json):**
```json
{
  "version": "2.0",
  "monitored_locations": [
    "/Users/jennifer/Library/Mobile Documents/com~apple~CloudDocs/Documents",
    "/Users/jennifer/Downloads",
    "/Users/jennifer/Desktop"
  ],
  "do_not_move_folders": [
    "/Users/jennifer/Documents/Archive",
    "/Users/jennifer/Documents/InProgress"
  ],
  "tag_corrections": {
    "machine-learning": ["ml", "machine learning", "ML"],
    "product-management": ["pm", "product mgmt"]
  },
  "daily_job_time": "02:00",
  "weekly_job_time": "Sunday 23:00",
  "monthly_job_time": "1st 03:00",
  "theme": "light",
  "enable_notifications": true,
  "ocr_engine": "apple_vision",
  "api_timeout": 30,
  "max_file_size_mb": 100
}
```

---

## Appendix C: Troubleshooting

**Common Issues:**

**1. Flask won't start**
```bash
# Check port 5000 not in use
lsof -i :5000

# Verify Python version
python --version  # Should be 3.9+

# Check logs
tail -f ~/Library/Logs/knowledge_map/server.log

# Kill existing process
pkill -f "knowledge_map/src/app.py"

# Restart
python src/app.py
```

**2. Daily job not running**
```bash
# Verify LaunchAgent loaded
launchctl list | grep knowledge_map

# Check job logs
tail -f ~/Library/Logs/knowledge_map/jobs/daily.log

# Test manually
python src/jobs/daily.py --manual

# Reload LaunchAgent
launchctl unload ~/Library/LaunchAgents/com.knowledge_map.daily.plist
launchctl load ~/Library/LaunchAgents/com.knowledge_map.daily.plist
```

**3. Claude API not working**
```bash
# Verify API key set
echo $ANTHROPIC_API_KEY

# Check .env file
cat .env | grep ANTHROPIC_API_KEY

# Test API connection
curl -H "x-api-key: $ANTHROPIC_API_KEY" \
     -H "anthropic-version: 2023-06-01" \
     https://api.anthropic.com/v1/messages

# Check internet connection
ping api.anthropic.com

# System falls back to local NLP automatically
```

**4. Graph not rendering**
```bash
# Check browser console for errors (F12 → Console)

# Verify API returns data
curl http://localhost:5000/api/graph/data

# Clear browser cache
# Chrome: Cmd+Shift+Delete → Clear cache

# Check D3.js loaded
# Browser console: typeof d3  # Should not be "undefined"
```

**5. Files not being organized**
```bash
# Check file permissions
ls -la /path/to/file

# Verify not in "do not move" folders
cat data/config.json | grep do_not_move_folders

# Check daily job logs for errors
tail -f ~/Library/Logs/knowledge_map/jobs/daily.log

# Run manual test (dry run)
python src/jobs/daily.py --test --verbose
```

**6. Database locked errors**
```bash
# Check for multiple processes accessing DB
lsof | grep knowledge_graph.db

# Kill all processes
pkill -f knowledge_map

# Restart services
launchctl load ~/Library/LaunchAgents/com.knowledge_map.*.plist
```

**7. High CPU/memory usage**
```bash
# Check running jobs
launchctl list | grep knowledge_map

# Monitor resource usage
top -pid $(pgrep -f knowledge_map)

# Stop jobs temporarily
launchctl stop com.knowledge_map.daily

# Reduce batch size in config
# Edit data/config.json: "batch_size": 25
```

---

## Document Control

**Status:** Complete and ready for implementation

**Last Updated:** 2025-10-09

**Version:** 2.0

**Related Documents:**
- 01_PRODUCT_REQUIREMENTS.md - Product requirements and use cases
- 03_AUTO_TAGGING_SYSTEM.md - AI tagging implementation details
- 05_GRAPH_DATABASE_SCHEMA.md - Complete database schema
- 08_BACKGROUND_JOBS.md - Job scheduling and execution
- 11_UI_DESIGN.md - User interface specifications
- 13_UI_SPECIFICATIONS.md - Detailed UI component specs

**Revision History:**
- v1.0 (2025-10-09): Initial draft
- v2.0 (2025-10-09): Complete comprehensive version with all sections

**Next Steps:**
1. Review and approve architecture
2. Begin implementation (Phase 1)
3. Create development environment
4. Build core components (Layers 1-3)
5. Implement REST API (Layer 5)
6. Develop frontend interfaces
7. Deploy LaunchAgents
8. User acceptance testing

---

**END OF DOCUMENT**
