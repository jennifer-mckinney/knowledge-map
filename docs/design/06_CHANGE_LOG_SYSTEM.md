# Change Log System
# Personal Knowledge Graph System

**Project:** knowledge_map v2.0
**Document:** Change Log System Design
**Version:** 1.0
**Date:** 2025-10-09
**Status:** Draft

---

## Overview

The Change Log System maintains an audit trail of all file operations (moves, renames, deletions) performed by the automated file organizer. Each master location maintains its own change log to ensure users can always track where files went and why.

**Purpose:**
- Track all file movements and modifications
- Enable users to locate files that were moved
- Provide audit trail for organization decisions
- Support undo/rollback operations
- Archive historical changes for long-term reference

---

## 1. Change Log Structure

### JSON Format

Each change log is stored as a JSON file with the following structure:

```json
{
  "metadata": {
    "location": "iCloud Drive",
    "log_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/.knowledge_map/change_log.json",
    "created": "2025-10-01T00:00:00Z",
    "last_updated": "2025-10-09T14:30:00Z",
    "total_entries": 150,
    "version": "1.0"
  },
  "entries": [
    {
      "id": "cm_20251009_143012_abc123",
      "timestamp": "2025-10-09T14:30:12Z",
      "operation": "move",
      "file": {
        "name": "AI_Ethics_Framework.png",
        "type": "screenshot",
        "size_bytes": 245678,
        "hash": "sha256:abc123def456..."
      },
      "old_path": "/Users/username/Desktop/AI_Ethics_Framework.png",
      "new_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Screenshots/AI/AI_Ethics_Framework.png",
      "reason": "Automated organization based on content analysis",
      "tags": ["ai-ethics", "screenshot", "reference", "oxford"],
      "confidence": 0.92,
      "manual_override": false
    }
  ]
}
```

### Field Descriptions

**Metadata:**
- `location`: Human-readable master location name
- `log_path`: Absolute path to this change log file
- `created`: ISO 8601 timestamp of log creation
- `last_updated`: ISO 8601 timestamp of last entry
- `total_entries`: Count of all logged operations
- `version`: Change log schema version

**Entry Fields:**
- `id`: Unique identifier for this change (`cm_YYYYMMDD_HHMMSS_random`)
- `timestamp`: ISO 8601 timestamp when operation occurred
- `operation`: Type of operation performed
- `file`: File metadata (name, type, size, hash)
- `old_path`: Original absolute file path
- `new_path`: Destination absolute file path
- `reason`: Human-readable explanation of why action taken
- `tags`: Tags assigned to file that influenced decision
- `confidence`: Algorithm confidence score (0.0-1.0)
- `manual_override`: Boolean indicating if user manually approved/corrected

---

## 2. Operations Logged

### Move Operations

Logged when a file is moved from one location to another.

```json
{
  "id": "cm_20251009_020045_def789",
  "timestamp": "2025-10-09T02:00:45Z",
  "operation": "move",
  "file": {
    "name": "Product_Strategy_Draft.docx",
    "type": "document",
    "size_bytes": 125440,
    "hash": "sha256:def789abc123..."
  },
  "old_path": "/Users/username/Downloads/Product_Strategy_Draft.docx",
  "new_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/Product_Strategy_Draft.docx",
  "reason": "Document tagged [product-management, work] moved to appropriate work folder",
  "tags": ["product-management", "work", "document", "strategy"],
  "confidence": 0.87,
  "manual_override": false
}
```

### Rename Operations

Logged when a file is renamed without moving locations.

```json
{
  "id": "cm_20251009_020112_ghi456",
  "timestamp": "2025-10-09T02:01:12Z",
  "operation": "rename",
  "file": {
    "name": "Screenshot 2025-10-08 at 3.45.23 PM.png",
    "type": "screenshot",
    "size_bytes": 89012,
    "hash": "sha256:ghi456jkl789..."
  },
  "old_path": "/Users/username/Desktop/Screenshot 2025-10-08 at 3.45.23 PM.png",
  "new_path": "/Users/username/Desktop/Oxford_AI_Programme_Schedule.png",
  "reason": "Renamed based on OCR content: 'Oxford AI Programme Schedule Q4 2025'",
  "tags": ["oxford", "screenshot", "schedule", "ai-programme"],
  "confidence": 0.95,
  "manual_override": false
}
```

### Delete Operations

Logged when a file is marked for deletion or moved to trash.

```json
{
  "id": "cm_20251009_020145_jkl789",
  "timestamp": "2025-10-09T02:01:45Z",
  "operation": "delete",
  "file": {
    "name": "temp_download_copy.tmp",
    "type": "temporary",
    "size_bytes": 512,
    "hash": "sha256:jkl789mno012..."
  },
  "old_path": "/Users/username/Downloads/temp_download_copy.tmp",
  "new_path": "/Users/username/.Trash/temp_download_copy.tmp",
  "reason": "Temporary file older than 7 days, no meaningful content",
  "tags": ["temporary", "system-file"],
  "confidence": 0.99,
  "manual_override": false
}
```

### Organization Skip Operations

Logged when a file was analyzed but NOT moved.

```json
{
  "id": "cm_20251009_020230_mno012",
  "timestamp": "2025-10-09T02:02:30Z",
  "operation": "skip",
  "file": {
    "name": "InProgress_Thesis.docx",
    "type": "document",
    "size_bytes": 892456,
    "hash": "sha256:mno012pqr345..."
  },
  "old_path": "/Users/username/Desktop/InProgress_Thesis.docx",
  "new_path": null,
  "reason": "File in 'do not move' folder or confidence below threshold (0.65 < 0.70)",
  "tags": ["oxford", "thesis", "document", "in-progress"],
  "confidence": 0.65,
  "manual_override": false
}
```

---

## 3. Log Locations

### Master Location Mapping

Each master location has its own change log stored in a hidden `.knowledge_map` directory:

```
iCloud Drive
└── .knowledge_map/
    └── change_log.json

Desktop
└── .knowledge_map/
    └── change_log.json

Downloads
└── .knowledge_map/
    └── change_log.json
```

### Absolute Paths

```json
{
  "master_locations": {
    "icloud": {
      "name": "iCloud Drive",
      "root": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/",
      "log_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/.knowledge_map/change_log.json"
    },
    "desktop": {
      "name": "Desktop",
      "root": "/Users/username/Desktop/",
      "log_path": "/Users/username/Desktop/.knowledge_map/change_log.json"
    },
    "downloads": {
      "name": "Downloads",
      "root": "/Users/username/Downloads/",
      "log_path": "/Users/username/Downloads/.knowledge_map/change_log.json"
    }
  }
}
```

### Cross-Location References

When a file moves from one master location to another, BOTH logs record the operation:

**Source Location Log (Desktop):**
```json
{
  "id": "cm_20251009_020300_pqr345",
  "operation": "move_out",
  "old_path": "/Users/username/Desktop/report.pdf",
  "new_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Documents/report.pdf",
  "reason": "Moved to iCloud Drive for permanent storage",
  "destination_log": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/.knowledge_map/change_log.json"
}
```

**Destination Location Log (iCloud):**
```json
{
  "id": "cm_20251009_020300_pqr345",
  "operation": "move_in",
  "old_path": "/Users/username/Desktop/report.pdf",
  "new_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Documents/report.pdf",
  "reason": "Moved from Desktop for permanent storage",
  "source_log": "/Users/username/Desktop/.knowledge_map/change_log.json"
}
```

---

## 4. Archive Strategy

### When to Archive

Change logs are archived after **1 month** to prevent active logs from becoming too large.

**Trigger Conditions:**
- Age: Entries older than 30 days
- Size: Active log exceeds 5MB
- Count: Active log exceeds 10,000 entries

### Archive Location

All archived logs are stored in iCloud Drive for long-term retention:

```
/Users/username/Library/Mobile Documents/com~apple~CloudDocs/.knowledge_map/archives/
├── icloud_change_log_2025-09.json
├── desktop_change_log_2025-09.json
├── downloads_change_log_2025-09.json
├── icloud_change_log_2025-08.json
└── ...
```

### Archive Process

1. **Identify entries to archive:**
   - All entries with `timestamp` older than 30 days from current date

2. **Create archive file:**
   ```
   {location}_change_log_{YYYY-MM}.json
   ```

3. **Move old entries to archive:**
   - Copy entries to archive file
   - Remove from active log
   - Update active log metadata

4. **Update active log:**
   ```json
   {
     "metadata": {
       "last_archived": "2025-10-09T02:00:00Z",
       "archive_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/.knowledge_map/archives/desktop_change_log_2025-09.json",
       "archived_entries": 1250
     }
   }
   ```

### Archive File Format

Same structure as active logs, with additional metadata:

```json
{
  "metadata": {
    "location": "Desktop",
    "archive_period": "2025-09",
    "entries_start_date": "2025-09-01T00:00:00Z",
    "entries_end_date": "2025-09-30T23:59:59Z",
    "total_entries": 1250,
    "archived_on": "2025-10-09T02:00:00Z",
    "version": "1.0"
  },
  "entries": [
    // All entries from September 2025
  ]
}
```

---

## 5. Lookup & Search Functionality

### Basic Lookup (by filename)

```bash
# Command-line interface
$ knowledge_map find-file "AI_Ethics_Framework.png"

Found in change log:
  Date: 2025-10-09 14:30:12
  Operation: move
  From: /Users/username/Desktop/AI_Ethics_Framework.png
  To: /Users/username/Library/Mobile Documents/.../Screenshots/AI/AI_Ethics_Framework.png
  Reason: Automated organization based on content analysis
  Tags: ai-ethics, screenshot, reference, oxford
```

### Advanced Search (by criteria)

```python
# API example
results = change_log_search(
    filename="*.png",
    operation="move",
    date_range=("2025-10-01", "2025-10-09"),
    tags=["ai-ethics"],
    confidence_min=0.8
)
```

### Search Indexes

For fast lookups, maintain indexes:

```json
{
  "indexes": {
    "by_filename": {
      "AI_Ethics_Framework.png": ["cm_20251009_143012_abc123"]
    },
    "by_old_path": {
      "/Users/username/Desktop/AI_Ethics_Framework.png": ["cm_20251009_143012_abc123"]
    },
    "by_tag": {
      "ai-ethics": ["cm_20251009_143012_abc123", "cm_20251009_020045_def789"]
    },
    "by_date": {
      "2025-10-09": ["cm_20251009_143012_abc123", "cm_20251009_020045_def789"]
    }
  }
}
```

### Search Across Archives

When searching, query both active logs AND archives:

1. Search active log first (fast, recent entries)
2. If not found, search archive indexes
3. Load relevant archive files only when needed
4. Combine results and sort by timestamp

---

## 6. Example Change Log Entries

### Complete Daily Batch Example

```json
{
  "metadata": {
    "location": "Desktop",
    "log_path": "/Users/username/Desktop/.knowledge_map/change_log.json",
    "created": "2025-10-01T00:00:00Z",
    "last_updated": "2025-10-09T02:05:00Z",
    "total_entries": 45,
    "version": "1.0"
  },
  "entries": [
    {
      "id": "cm_20251009_020015_aaa111",
      "timestamp": "2025-10-09T02:00:15Z",
      "operation": "move",
      "file": {
        "name": "meeting_notes_2025-10-08.txt",
        "type": "note",
        "size_bytes": 3456,
        "hash": "sha256:aaa111bbb222..."
      },
      "old_path": "/Users/username/Desktop/meeting_notes_2025-10-08.txt",
      "new_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Notes/Work/meeting_notes_2025-10-08.txt",
      "reason": "Note tagged [work, meeting] moved to work notes folder",
      "tags": ["work", "meeting", "note"],
      "confidence": 0.91,
      "manual_override": false
    },
    {
      "id": "cm_20251009_020023_bbb222",
      "timestamp": "2025-10-09T02:00:23Z",
      "operation": "move",
      "file": {
        "name": "Screenshot 2025-10-08 at 11.22.15 AM.png",
        "type": "screenshot",
        "size_bytes": 178923,
        "hash": "sha256:bbb222ccc333..."
      },
      "old_path": "/Users/username/Desktop/Screenshot 2025-10-08 at 11.22.15 AM.png",
      "new_path": "/Users/username/Library/Mobile Documents/com~apple~CloudDocs/Screenshots/Social/linkedin_post_ideas.png",
      "reason": "Screenshot contains social media content, moved to Social folder",
      "tags": ["screenshot", "social-media", "linkedin", "career"],
      "confidence": 0.88,
      "manual_override": false
    },
    {
      "id": "cm_20251009_020035_ccc333",
      "timestamp": "2025-10-09T02:00:35Z",
      "operation": "skip",
      "file": {
        "name": "Current_Project.xlsx",
        "type": "spreadsheet",
        "size_bytes": 456789,
        "hash": "sha256:ccc333ddd444..."
      },
      "old_path": "/Users/username/Desktop/Current_Project.xlsx",
      "new_path": null,
      "reason": "File actively being worked on (modified < 24 hours ago), skipping organization",
      "tags": ["work", "spreadsheet", "project"],
      "confidence": 0.75,
      "manual_override": false
    }
  ]
}
```

---

## 7. User Interface for Viewing Logs

### Web UI Components

#### Change Log Viewer (Main Interface)

```
┌─────────────────────────────────────────────────────────────┐
│  Change Log Viewer                          [Filter ▼] [⚙]  │
├─────────────────────────────────────────────────────────────┤
│  Location: [All Locations ▼]   Date: [Last 30 Days ▼]      │
│  Operation: [All ▼]            Tags: [All ▼]                │
│  Search: [________________]                         [Search] │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 📄 AI_Ethics_Framework.png                          │   │
│  │ Moved • 2025-10-09 14:30:12                         │   │
│  │                                                       │   │
│  │ From: ~/Desktop/AI_Ethics_Framework.png             │   │
│  │ To:   ~/iCloud/Screenshots/AI/AI_Ethics_Frame...    │   │
│  │                                                       │   │
│  │ Reason: Automated organization based on content     │   │
│  │ Tags: ai-ethics, screenshot, reference, oxford      │   │
│  │ Confidence: 92%                                      │   │
│  │                                                       │   │
│  │ [Open File] [Show in Graph] [Undo Move]             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 📝 meeting_notes_2025-10-08.txt                     │   │
│  │ Moved • 2025-10-09 02:00:15                         │   │
│  │ ...                                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 📊 Current_Project.xlsx                             │   │
│  │ Skipped • 2025-10-09 02:00:35                       │   │
│  │ ...                                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                               │
│  Showing 25 of 150 entries        [◀ Previous] [Next ▶]    │
└─────────────────────────────────────────────────────────────┘
```

#### File Lookup Tool

```
┌─────────────────────────────────────────────────────────────┐
│  Find File                                                   │
├─────────────────────────────────────────────────────────────┤
│  Filename: [AI_Ethics_Framework.png________] [Search]       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ✓ Found: AI_Ethics_Framework.png                           │
│                                                               │
│  Current Location:                                           │
│  /Users/username/Library/Mobile Documents/com~apple~Cloud   │
│  Docs/Screenshots/AI/AI_Ethics_Framework.png                │
│                                                               │
│  [Open in Finder] [Copy Path]                               │
│                                                               │
│  ─────────────────────────────────────────────────────────  │
│                                                               │
│  Move History:                                               │
│                                                               │
│  • 2025-10-09 14:30  Moved to Screenshots/AI/               │
│    From: ~/Desktop/                                          │
│    Reason: Automated organization                            │
│                                                               │
│  • 2025-10-08 15:45  Downloaded                              │
│    To: ~/Desktop/                                            │
│    Source: Safari download                                   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

#### Statistics Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│  Change Log Statistics - Last 30 Days                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Total Operations: 1,250                                     │
│                                                               │
│  Moves:   1,050 (84%)  ████████████████████▌                │
│  Renames:   125 (10%)  ██▌                                   │
│  Deletes:    50  (4%)  █                                     │
│  Skipped:    25  (2%)  ▌                                     │
│                                                               │
│  ─────────────────────────────────────────────────────────  │
│                                                               │
│  Top Destinations:                                           │
│  1. iCloud/Screenshots/  425 files                           │
│  2. iCloud/Documents/    315 files                           │
│  3. iCloud/Notes/        210 files                           │
│                                                               │
│  Average Confidence: 87%                                     │
│  Manual Overrides: 12 (1%)                                   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Command-Line Interface

```bash
# View recent changes
$ knowledge_map changelog --recent 10

# Find file by name
$ knowledge_map find "AI_Ethics_Framework.png"

# Search by tag
$ knowledge_map changelog --tag "ai-ethics" --date "2025-10"

# Undo last operation
$ knowledge_map undo cm_20251009_143012_abc123

# View statistics
$ knowledge_map changelog --stats

# Archive old entries
$ knowledge_map changelog --archive --date-before "2025-09-30"
```

---

## Implementation Notes

### Performance Considerations

1. **Indexing:** Maintain separate index files for fast lookups
2. **Lazy Loading:** Only load log entries when needed
3. **Batch Writes:** Append new entries in batches, not one-by-one
4. **Archive Compression:** Compress archived logs (gzip) to save space

### Error Handling

1. **Log Corruption:** Maintain backup of previous version before writes
2. **Missing Logs:** Recreate from knowledge graph database
3. **Cross-Location Sync:** Verify both logs updated for cross-location moves
4. **Archive Failures:** Retry with exponential backoff, alert user

### Integration Points

1. **File Organizer:** Calls `log_change()` after every operation
2. **Knowledge Graph:** Queries change log to update node paths
3. **Web UI:** Reads logs via API endpoints
4. **Backup System:** Includes change logs in system backups

---

## Summary

The Change Log System provides comprehensive audit trails for all file operations, enabling users to:
- Track where files went and why
- Search historical changes across all locations
- Undo unwanted moves
- Understand system decisions
- Archive old records efficiently

By maintaining separate logs per master location with cross-references for moves between locations, the system ensures users never lose track of their files while keeping logs performant and maintainable.

---

**Document Status:** ✅ READY FOR IMPLEMENTATION

**Next Steps:**
1. Implement change log data structures
2. Integrate with file organizer module
3. Build search/lookup API
4. Create web UI components
5. Test archive strategy
