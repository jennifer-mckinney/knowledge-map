# Data Source Mapping
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Final

---

## Data Sources by Device/Location

### 🖥️ MacBook Pro (Primary)
- iCloud Desktop (synced, safe to monitor)
- Local Downloads folder
- Local file system

### 📱 iPhone 17
- iCloud Photos (synced)
- iCloud Notes (synced)
- Files sync via iCloud

### ☁️ iCloud Drive
- Documents (primary work location)
- Desktop (synced from MacBook)
- Photos Library
- Notes database

### ☁️ OneDrive
- All synced files and folders

### 💾 External Storage
- External drives (when connected - future)

### 🌐 Shared Folders
- Network locations (future)

---

## Phase 1 Sources (Week 1)

| Source | Path | Update Freq | Priority |
|--------|------|-------------|----------|
| iCloud Documents | `~/Library/Mobile Documents/.../Documents` | Daily | HIGH |
| iCloud Desktop | `~/Library/Mobile Documents/.../Desktop` | Daily | HIGH |
| Downloads | `~/Downloads` | Daily | HIGH |
| OneDrive | Synced paths | Daily | HIGH |
| **Screenshots** | All locations | **Daily** | **CRITICAL** |
| Apple Notes | `~/Library/Group Containers/group.com.apple.notes/` | Daily | HIGH |
| Calendar | Manual .ics export | Weekly | MEDIUM |
| Email | TBD | TBD | MEDIUM |

---

## Phase 2 Sources (After Phase 1 Complete)

| Source | API/Method | Update Freq | Priority | Notes |
|--------|------------|-------------|----------|-------|
| **Notion** | Official Notion API | Real-time/Daily | **HIGH** | Workspaces, pages, databases, properties |
| Browser History | SQLite/API | Daily | MEDIUM | Research trails, visited sites |
| Slack/Discord | API export | Weekly | LOW | Team communications |
| GitHub Repos | Git metadata | Weekly | MEDIUM | Project documentation |

### Notion Integration Details

**Why Notion is Critical:**
- User maintains active documentation in Notion (phone + laptop)
- Rich structured data (pages, databases, properties)
- Existing metadata (tags, relations, dates)
- Natural knowledge graph structure (internal page links)
- Official API with robust access

**What to Extract:**
```javascript
{
  type: "notion_page",
  notion_id: "page-uuid",
  title: "Page title",
  database: "parent_database_name",
  properties: {
    // User-defined properties from database
    tags: ["tag1", "tag2"],
    status: "In Progress",
    priority: "High",
    // ... any custom properties
  },
  content: "markdown_content",
  internal_links: ["page-uuid-1", "page-uuid-2"],
  created: "2025-01-09",
  last_edited: "2025-01-10",
  url: "notion.so/...",
  attachments: []
}
```

**Notion API Integration:**
- Authenticate via OAuth or Integration Token
- Pull workspace hierarchy (databases → pages)
- Extract page content as markdown
- Map database properties → dynamic metadata
- Track internal links → relationship edges
- Sync on schedule (real-time webhook or daily poll)

**Mapping to Knowledge Graph:**
- Notion Databases → `type: "topic"` nodes
- Notion Pages → `type: "document"` or `type: "project"` nodes
- Database properties → custom metadata fields
- Internal page links → `type: "semantic"` relationships
- Mentioned pages → `type: "related"` relationships

---

## Extraction Methods

### Files
- **Method:** Python pathlib direct access
- **Metadata:** name, size, dates, type, path
- **Content:** PDF (PyPDF2), DOCX (python-docx), TXT (direct read)

### Screenshots
- **Method:** OCR (Tesseract or Apple Vision)
- **Extract:** All visible text
- **Detection:** Chart/infographic/quote classification
- **Priority:** Educational AI/learning content

### Apple Notes
- **Method:** SQLite database read
- **Extract:** Title, content, dates, folders, attachments
- **Library:** Custom extractor or osxphotos approach

### Calendar
- **Method:** .ics file export (weekly)
- **Extract:** Events, dates, attendees, notes

### Email
- **Method:** TBD (Mail.app or export)
- **Extract:** Subject, sender, date, attachments

---

## Master Keys (All Nodes)

```javascript
{
  id: "unique_id",
  date_created: "YYYY-MM-DD",  // REQUIRED
  type: "[type]",               // REQUIRED
  file_path: "/path",
  primary_tags: [],             // 1-3 required
  secondary_tags: [],
  keywords: []
}
```

---

**Status:** ✅ Complete
