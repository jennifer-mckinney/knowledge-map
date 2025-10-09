# Graph Database Schema
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Final

---

## 1. Node Schema

### Required Fields (ALL Nodes)

```json
{
  "id": "string (UUID v4)",
  "date_created": "YYYY-MM-DD (ISO 8601)",
  "type": "enum (see Node Types below)",
  "primary_tags": ["array", "1-3 tags", "required"]
}
```

### Full Node Structure

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "date_created": "2025-10-09",
  "date_modified": "2025-10-09",
  "type": "document",

  "file_path": "/Users/user/Documents/ai_ethics.pdf",
  "file_name": "ai_ethics.pdf",
  "file_size": 1048576,
  "file_extension": "pdf",

  "primary_tags": ["ai-ethics", "oxford", "research"],
  "secondary_tags": ["reference", "important"],
  "keywords": ["fairness", "bias", "transparency", "accountability"],

  "content_hash": "sha256:abc123...",
  "content_excerpt": "First 500 characters of extracted text...",

  "metadata": {
    "author": "string",
    "title": "string",
    "description": "string",
    "source": "string",
    "ocr_confidence": 0.95
  },

  "relationships": [
    "edge_id_1",
    "edge_id_2"
  ],

  "time_tracking": {
    "first_seen": "2025-10-09T14:30:00Z",
    "last_accessed": "2025-10-09T16:45:00Z",
    "duration_seconds": 0
  },

  "change_history": [
    {
      "date": "2025-10-09T14:30:00Z",
      "action": "created",
      "old_path": null,
      "new_path": "/Users/user/Documents/ai_ethics.pdf"
    }
  ]
}
```

### Node Types

```javascript
// Core types
"document"       // PDF, DOCX, TXT, Pages, etc.
"spreadsheet"    // Excel, Numbers, CSV
"presentation"   // PowerPoint, Keynote
"image"          // JPG, PNG, GIF (non-screenshot)
"screenshot"     // Screen captures
"video"          // MP4, MOV
"audio"          // MP3, M4A
"note"           // Apple Notes entries
"event"          // Calendar events
"email"          // Email messages
"folder"         // Directory nodes (optional)
"link"           // URLs/bookmarks
"code"           // Source code files
```

---

## 2. Edge Schema

### Required Fields (ALL Edges)

```json
{
  "id": "string (UUID v4)",
  "source": "node_id (UUID)",
  "target": "node_id (UUID)",
  "weight": "float (0.0-1.0)",
  "created_date": "YYYY-MM-DD",
  "type": "enum (see Relationship Types)",
  "why": ["array", "of reasons"]
}
```

### Full Edge Structure

```json
{
  "id": "660e8400-e29b-41d4-a716-446655440001",
  "source": "550e8400-e29b-41d4-a716-446655440000",
  "target": "770e8400-e29b-41d4-a716-446655440002",

  "weight": 0.85,
  "created_date": "2025-10-09",
  "last_updated": "2025-10-09",

  "type": "content-similarity",
  "why": [
    "shared-tags: ai-ethics, oxford",
    "temporal-same-week",
    "content-similarity: 0.85"
  ],

  "metadata": {
    "auto_generated": true,
    "confidence": 0.85,
    "method": "cosine-similarity",
    "user_confirmed": false
  },

  "bidirectional": true
}
```

---

## 3. Relationship Types

### Content Similarity (Auto-Generated)
- **Type:** `content-similarity`
- **Weight Calculation:** Cosine similarity of TF-IDF vectors
- **Threshold:** ≥0.70 to create edge
- **Why Examples:**
  - `"content-similarity: 0.85"`
  - `"shared-tags: 3"`
  - `"shared-keywords: fairness, bias, ethics"`

```json
{
  "type": "content-similarity",
  "weight": 0.85,
  "why": ["cosine-similarity: 0.85", "shared-tags: ai-ethics, oxford"],
  "metadata": {
    "method": "tfidf-cosine",
    "threshold": 0.70
  }
}
```

### Temporal (Auto-Generated)
- **Type:** `temporal`
- **Weight Calculation:**
  - Same day: 1.0
  - Same week: 0.8
  - Same month: 0.5
  - Same quarter: 0.3
- **Why Examples:**
  - `"created-same-day: 2025-10-09"`
  - `"modified-same-week"`
  - `"accessed-together"`

```json
{
  "type": "temporal",
  "weight": 1.0,
  "why": ["created-same-day: 2025-10-09"],
  "metadata": {
    "date": "2025-10-09",
    "granularity": "day"
  }
}
```

### Hierarchical (Auto-Generated)
- **Type:** `hierarchical`
- **Weight:** Always 1.0
- **Why Examples:**
  - `"parent-folder"`
  - `"child-of: /Documents/Oxford"`
  - `"sibling-file"`

```json
{
  "type": "hierarchical",
  "weight": 1.0,
  "why": ["parent-folder: /Documents/Oxford/AI"],
  "metadata": {
    "relationship": "parent-child",
    "depth": 2
  }
}
```

### Cross-Domain (Auto-Generated)
- **Type:** `cross-domain`
- **Weight Calculation:** Tag overlap × content similarity
- **Threshold:** Tags from different domains + similarity ≥0.60
- **Why Examples:**
  - `"bridges: ai-ethics + career"`
  - `"combines: oxford + product-management"`

```json
{
  "type": "cross-domain",
  "weight": 0.75,
  "why": ["bridges: ai-ethics + career", "unique-combination"],
  "metadata": {
    "domains": ["ai-ethics", "career"],
    "business_value": "high"
  }
}
```

### Manual (User-Created)
- **Type:** `manual`
- **Weight:** User-defined (default 1.0)
- **Why:** User-provided reason
- **Examples:**
  - `"user: related to Amazon interview prep"`
  - `"user: inspiration for blog post"`

```json
{
  "type": "manual",
  "weight": 1.0,
  "why": ["user: related to Amazon interview prep"],
  "metadata": {
    "created_by": "user",
    "note": "Reference for behavioral questions"
  }
}
```

### Reference (Auto-Generated)
- **Type:** `reference`
- **Weight:** Always 1.0
- **Why Examples:**
  - `"cited-in"`
  - `"attached-to-note"`
  - `"linked-in-document"`

```json
{
  "type": "reference",
  "weight": 1.0,
  "why": ["attached-to-note: Meeting Notes 2025-10-09"],
  "metadata": {
    "source_type": "note",
    "target_type": "document"
  }
}
```

---

## 4. Tag Structure

### Primary Tags (1-3 Required)
- **Purpose:** Main topics, high-level categorization
- **Format:** `lowercase-with-hyphens`
- **Examples:** `ai-ethics`, `oxford`, `career`, `product-management`
- **Display:** Always visible in UI
- **Storage:** Array of strings

```json
"primary_tags": ["ai-ethics", "oxford", "research"]
```

### Secondary Tags (Unlimited Optional)
- **Purpose:** Descriptors, quality markers, metadata
- **Format:** `lowercase-with-hyphens`
- **Examples:** `infographic`, `important`, `draft`, `reference`
- **Display:** Expandable in UI
- **Storage:** Array of strings

```json
"secondary_tags": ["infographic", "important", "needs-review"]
```

### Keywords (Auto-Generated)
- **Purpose:** Searchable content terms
- **Source:** NLP extraction from content
- **Format:** `lowercase`, no hyphens
- **Examples:** `fairness`, `bias`, `transparency`, `accountability`
- **Display:** Not shown by default, used for search
- **Storage:** Array of strings with optional scores

```json
"keywords": [
  "fairness",
  "bias",
  "transparency",
  "accountability"
]
```

### Tag Hierarchy (Suggested)
```
[ai-ethics]
├── [bias]
├── [fairness]
└── [transparency]

[oxford]
├── [thesis-research]
├── [coursework]
└── [readings]

[career]
├── [interview-prep]
├── [resume]
└── [portfolio]
```

---

## 5. Database Format

### Recommended: SQLite

**Rationale:**
- Fast indexed queries
- ACID transactions
- Built-in full-text search (FTS5)
- Portable single file
- No server required
- Python sqlite3 built-in

### Database Schema (SQL)

```sql
-- Nodes table
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

    metadata_json TEXT,  -- JSON blob
    time_tracking_json TEXT,
    change_history_json TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tags table (normalized)
CREATE TABLE tags (
    node_id TEXT NOT NULL,
    tag TEXT NOT NULL,
    tag_type TEXT NOT NULL,  -- 'primary', 'secondary', 'keyword'
    score REAL,  -- For keywords

    PRIMARY KEY (node_id, tag, tag_type),
    FOREIGN KEY (node_id) REFERENCES nodes(id) ON DELETE CASCADE
);

-- Edges table
CREATE TABLE edges (
    id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    target TEXT NOT NULL,

    weight REAL NOT NULL CHECK(weight >= 0.0 AND weight <= 1.0),
    created_date TEXT NOT NULL,
    last_updated TEXT,

    type TEXT NOT NULL,
    why_json TEXT NOT NULL,  -- JSON array
    metadata_json TEXT,
    bidirectional INTEGER DEFAULT 1,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (source) REFERENCES nodes(id) ON DELETE CASCADE,
    FOREIGN KEY (target) REFERENCES nodes(id) ON DELETE CASCADE
);

-- Indexes for fast queries
CREATE INDEX idx_nodes_type ON nodes(type);
CREATE INDEX idx_nodes_date_created ON nodes(date_created);
CREATE INDEX idx_nodes_file_path ON nodes(file_path);

CREATE INDEX idx_tags_node_id ON tags(node_id);
CREATE INDEX idx_tags_tag ON tags(tag);
CREATE INDEX idx_tags_tag_type ON tags(tag_type);

CREATE INDEX idx_edges_source ON edges(source);
CREATE INDEX idx_edges_target ON edges(target);
CREATE INDEX idx_edges_type ON edges(type);
CREATE INDEX idx_edges_weight ON edges(weight);

-- Full-text search (FTS5)
CREATE VIRTUAL TABLE nodes_fts USING fts5(
    id,
    file_name,
    content_excerpt,
    content=nodes,
    content_rowid=rowid
);

-- Triggers to keep FTS in sync
CREATE TRIGGER nodes_ai AFTER INSERT ON nodes BEGIN
    INSERT INTO nodes_fts(rowid, id, file_name, content_excerpt)
    VALUES (new.rowid, new.id, new.file_name, new.content_excerpt);
END;

CREATE TRIGGER nodes_ad AFTER DELETE ON nodes BEGIN
    DELETE FROM nodes_fts WHERE rowid = old.rowid;
END;

CREATE TRIGGER nodes_au AFTER UPDATE ON nodes BEGIN
    UPDATE nodes_fts SET
        file_name = new.file_name,
        content_excerpt = new.content_excerpt
    WHERE rowid = new.rowid;
END;
```

### Alternative: JSON Files (Not Recommended)

**Structure:**
```
knowledge_graph/
├── nodes/
│   ├── 550e8400-e29b-41d4-a716-446655440000.json
│   ├── 770e8400-e29b-41d4-a716-446655440002.json
│   └── ...
├── edges/
│   ├── 660e8400-e29b-41d4-a716-446655440001.json
│   └── ...
└── indexes/
    ├── by_tag.json
    ├── by_date.json
    └── by_type.json
```

**Drawbacks:**
- Slow for large graphs (>10k nodes)
- No atomic transactions
- Manual index maintenance
- No built-in search

---

## 6. Indexing Strategy

### SQLite Indexes (Recommended)

```sql
-- Primary indexes (created above)
CREATE INDEX idx_nodes_type ON nodes(type);
CREATE INDEX idx_nodes_date_created ON nodes(date_created);
CREATE INDEX idx_tags_tag ON tags(tag);
CREATE INDEX idx_edges_source ON edges(source);
CREATE INDEX idx_edges_target ON edges(target);

-- Composite indexes for common queries
CREATE INDEX idx_nodes_type_date ON nodes(type, date_created);
CREATE INDEX idx_tags_tag_type ON tags(tag, tag_type);
CREATE INDEX idx_edges_source_type ON edges(source, type);
CREATE INDEX idx_edges_type_weight ON edges(type, weight);

-- Covering index for search
CREATE INDEX idx_nodes_search ON nodes(type, date_created, file_name);
```

### Query Performance Targets

| Query Type | Target Time | Index Used |
|------------|-------------|------------|
| Search by tag | <50ms | `idx_tags_tag` |
| Search by content | <100ms | `nodes_fts` |
| Find node by ID | <10ms | Primary key |
| Get node edges | <50ms | `idx_edges_source` |
| Filter by type + date | <100ms | `idx_nodes_type_date` |
| Cross-domain search | <200ms | Multiple indexes |

### Cache Strategy
- **In-memory cache:** 1000 most-accessed nodes
- **Eviction:** LRU (Least Recently Used)
- **Invalidation:** On node update
- **Implementation:** Python `functools.lru_cache`

---

## 7. Example Graph Structure

### Sample Data: AI Ethics Research Project

```json
{
  "nodes": [
    {
      "id": "node-001",
      "date_created": "2025-10-01",
      "type": "document",
      "file_path": "/Users/user/Documents/Oxford/AI/ai_ethics_framework.pdf",
      "file_name": "ai_ethics_framework.pdf",
      "primary_tags": ["ai-ethics", "oxford", "research"],
      "secondary_tags": ["reference", "important"],
      "keywords": ["fairness", "bias", "transparency"],
      "content_excerpt": "This framework addresses key ethical considerations..."
    },
    {
      "id": "node-002",
      "date_created": "2025-10-01",
      "type": "screenshot",
      "file_path": "/Users/user/Desktop/Screenshot 2025-10-01 at 14.30.00.png",
      "file_name": "Screenshot 2025-10-01 at 14.30.00.png",
      "primary_tags": ["ai-ethics", "infographic"],
      "secondary_tags": ["social-media"],
      "keywords": ["bias", "mitigation", "strategies"],
      "metadata": {
        "ocr_confidence": 0.92,
        "source": "Twitter"
      }
    },
    {
      "id": "node-003",
      "date_created": "2025-10-01",
      "type": "note",
      "file_path": "apple-notes://note/12345",
      "file_name": "Meeting Notes: AI Ethics Discussion",
      "primary_tags": ["ai-ethics", "oxford", "meeting"],
      "secondary_tags": ["notes"],
      "keywords": ["fairness", "group", "discussion", "framework"]
    },
    {
      "id": "node-004",
      "date_created": "2025-10-02",
      "type": "document",
      "file_path": "/Users/user/Documents/Career/product_manager_resume.pdf",
      "file_name": "product_manager_resume.pdf",
      "primary_tags": ["career", "resume"],
      "secondary_tags": ["important"],
      "keywords": ["product", "management", "AI", "ethics"]
    },
    {
      "id": "node-005",
      "date_created": "2025-10-03",
      "type": "document",
      "file_path": "/Users/user/Documents/Career/ai_product_strategy.pdf",
      "file_name": "ai_product_strategy.pdf",
      "primary_tags": ["ai-ethics", "career", "product-management"],
      "secondary_tags": ["draft"],
      "keywords": ["strategy", "product", "ethics", "responsible-AI"]
    }
  ],

  "edges": [
    {
      "id": "edge-001",
      "source": "node-001",
      "target": "node-002",
      "weight": 0.85,
      "created_date": "2025-10-01",
      "type": "content-similarity",
      "why": [
        "shared-tags: ai-ethics",
        "temporal-same-day",
        "content-similarity: 0.85",
        "shared-keywords: bias"
      ]
    },
    {
      "id": "edge-002",
      "source": "node-001",
      "target": "node-003",
      "weight": 1.0,
      "created_date": "2025-10-01",
      "type": "temporal",
      "why": [
        "created-same-day: 2025-10-01",
        "shared-tags: ai-ethics, oxford"
      ]
    },
    {
      "id": "edge-003",
      "source": "node-001",
      "target": "node-005",
      "weight": 0.70,
      "created_date": "2025-10-03",
      "type": "content-similarity",
      "why": [
        "shared-tags: ai-ethics",
        "shared-keywords: ethics, fairness",
        "content-similarity: 0.70"
      ]
    },
    {
      "id": "edge-004",
      "source": "node-004",
      "target": "node-005",
      "weight": 0.75,
      "created_date": "2025-10-03",
      "type": "cross-domain",
      "why": [
        "bridges: career + ai-ethics",
        "shared-tags: career",
        "unique-combination: AI + Product Management"
      ],
      "metadata": {
        "business_value": "high",
        "domains": ["career", "ai-ethics", "product-management"]
      }
    },
    {
      "id": "edge-005",
      "source": "node-002",
      "target": "node-003",
      "weight": 0.65,
      "created_date": "2025-10-01",
      "type": "reference",
      "why": [
        "screenshot-referenced-in-note",
        "temporal-same-day"
      ]
    }
  ]
}
```

### Visual Representation

```
[ai_ethics_framework.pdf] ──(0.85)── [Screenshot: Bias Infographic]
    │ (node-001)                           │ (node-002)
    │                                       │
    │ (1.0, temporal)                      │ (0.65, reference)
    │                                       │
    └────────────────► [Meeting Notes] ◄───┘
                        │ (node-003)

[Resume.pdf] ────────(0.75, cross-domain)────► [AI Product Strategy.pdf]
 (node-004)            ⚡ High Business Value      (node-005)
                                                       │
                           (0.70, content-similarity) │
                                                       │
                    [ai_ethics_framework.pdf] ◄───────┘
                           (node-001)
```

### Graph Statistics

```json
{
  "nodes": {
    "total": 5,
    "by_type": {
      "document": 3,
      "screenshot": 1,
      "note": 1
    }
  },
  "edges": {
    "total": 5,
    "by_type": {
      "content-similarity": 2,
      "temporal": 1,
      "cross-domain": 1,
      "reference": 1
    },
    "avg_weight": 0.79
  },
  "tags": {
    "unique_primary": 6,
    "unique_secondary": 6,
    "unique_keywords": 12
  },
  "clusters": [
    {
      "name": "AI Ethics Research",
      "nodes": ["node-001", "node-002", "node-003"],
      "density": 0.67
    },
    {
      "name": "Career + AI Bridge",
      "nodes": ["node-004", "node-005", "node-001"],
      "density": 0.33,
      "business_value": "high"
    }
  ]
}
```

---

## Implementation Notes

### Database File Location
```
~/.knowledge_map/
├── knowledge_graph.db          # SQLite database
├── config.json                 # User configuration
└── backups/
    ├── knowledge_graph_2025-10-09.db
    └── ...
```

### Performance Considerations
- **Initial load:** Full scan creates ~10k nodes in ~30 seconds
- **Daily incremental:** ~100 new files in ~5 seconds
- **Search latency:** <100ms for 10k nodes
- **Graph render:** Load 1000 nodes in <3 seconds

### Backup Strategy
- **Frequency:** Daily automatic backup
- **Retention:** 30 days
- **Location:** `~/.knowledge_map/backups/`
- **Format:** SQLite database file (compressed)

### Migration Path
- JSON → SQLite migration script provided
- Preserves all node IDs and relationships
- Zero data loss

---

**Status:** ✅ Complete
**Next:** 06_TAGGING_SYSTEM_DESIGN.md
