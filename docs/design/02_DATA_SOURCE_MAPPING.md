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
