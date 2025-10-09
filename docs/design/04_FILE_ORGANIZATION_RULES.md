# File Organization Rules
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Final

---

## Overview

The knowledge_map system automatically organizes files by moving them to appropriate locations based on their content-derived tags. Organization happens daily at 2 AM with no user approval required. All moves are logged for transparency and audit trail.

**Key Principles:**
- Fully automatic organization (no user prompts)
- Content-based tagging determines destination
- Screenshots stay in place (virtual organization only)
- Desktop cleanup happens daily
- Change logs track all moves
- Naming conflicts are resolved automatically

---

## Folder Structure

### Master Organization Hierarchy

```
~/Documents/
├── _AUTOMATION/           # Automation scripts, tools, workflows
├── _PROJECTS/             # Active projects
│   ├── [project-name]/
│   └── _ARCHIVE/          # Completed projects
├── AI_ML/                 # AI/ML learning, research, notes
│   ├── Oxford/            # Oxford AI Programme materials
│   ├── Research/          # Papers, articles, studies
│   └── Tools/             # AI tools, prompts, experiments
├── Career/                # Career development, job search
│   ├── Resume/
│   ├── Interviews/
│   └── LinkedIn/
├── Product_Management/    # PM frameworks, docs, templates
├── Learning/              # General educational content
│   ├── Courses/
│   ├── Books/
│   └── Tutorials/
├── Business/              # Business strategy, finance, marketing
├── Personal/              # Personal files, not work-related
├── Reference/             # Long-term reference materials
├── Temp/                  # Temporary files (auto-cleanup after 30 days)
└── _CHANGE_LOGS/          # Organization audit trail

~/Desktop/
├── [daily files]          # Cleaned nightly → moved to proper locations
└── _CHANGE_LOG.json       # What moved from Desktop

~/Downloads/
├── [daily downloads]      # Cleaned nightly → moved to proper locations
└── _CHANGE_LOG.json       # What moved from Downloads

~/Pictures/Screenshots/
├── [all screenshots]      # NEVER MOVED (organized virtually)
└── _SCREENSHOT_INDEX.json # Virtual organization metadata
```

---

## Organization Rules

### Tag → Destination Mapping

#### Primary Tag Rules (Highest Priority)

| Primary Tag(s) | Destination | Example Files |
|----------------|-------------|---------------|
| `[oxford]` | `~/Documents/AI_ML/Oxford/` | Assignments, lecture notes, readings |
| `[ai-ethics]`, `[machine-learning]`, `[deep-learning]` | `~/Documents/AI_ML/Research/` | Papers, articles, studies |
| `[ai-tools]`, `[prompts]` | `~/Documents/AI_ML/Tools/` | ChatGPT prompts, AI experiments |
| `[career]`, `[resume]` | `~/Documents/Career/` | Resume drafts, cover letters |
| `[interview]`, `[job-search]` | `~/Documents/Career/Interviews/` | Interview prep, questions |
| `[product-management]`, `[pm-frameworks]` | `~/Documents/Product_Management/` | PRDs, roadmaps, frameworks |
| `[automation]`, `[scripts]` | `~/Documents/_AUTOMATION/` | Python scripts, workflows |
| `[project-*]` | `~/Documents/_PROJECTS/[project-name]/` | Project-specific files |
| `[learning]`, `[course]`, `[tutorial]` | `~/Documents/Learning/` | Educational materials |
| `[business]`, `[strategy]`, `[marketing]` | `~/Documents/Business/` | Business plans, marketing docs |
| `[personal]` | `~/Documents/Personal/` | Non-work personal files |
| `[reference]`, `[documentation]` | `~/Documents/Reference/` | Long-term reference docs |
| `[temp]`, `[draft]`, `[wip]` | `~/Documents/Temp/` | Temporary/work-in-progress |

#### Secondary Tag Rules (Refinement)

Secondary tags refine destination within primary folder:

| Secondary Tag | Action | Example |
|---------------|--------|---------|
| `[archive]` | Move to `_ARCHIVE/` subfolder | Old project files |
| `[important]` | Stay at top level (no subfolder) | Critical documents |
| `[infographic]`, `[cheatsheet]` | Move to `Reference/` subfolder | Quick reference materials |
| `[template]` | Move to `Templates/` subfolder | Reusable templates |

#### File Type Rules (Default Behavior)

| File Type | No Primary Tag? | Default Destination |
|-----------|-----------------|---------------------|
| `.pdf`, `.docx`, `.txt`, `.md` | Generic documents | `~/Documents/Reference/` |
| `.py`, `.sh`, `.js` | Scripts/code | `~/Documents/_AUTOMATION/` |
| `.png`, `.jpg`, `.gif` (screenshots) | Screenshots | STAY IN PLACE |
| `.png`, `.jpg`, `.gif` (non-screenshots) | Images | `~/Pictures/` |
| `.zip`, `.dmg`, `.pkg` | Installers/archives | `~/Downloads/Archive/` |
| `.csv`, `.xlsx`, `.numbers` | Spreadsheets | `~/Documents/Data/` |
| `.key`, `.pptx` | Presentations | `~/Documents/Presentations/` |

---

## Special Cases

### 1. Screenshots
**Rule:** Screenshots NEVER move physically. They are organized virtually in the knowledge graph only.

**Rationale:**
- macOS saves screenshots to a single default location
- Moving them breaks system expectations
- Virtual organization (tags + relationships) provides findability

**Implementation:**
- Screenshots detected by filename pattern (`Screenshot YYYY-MM-DD at HH.MM.SS.png`)
- OCR extracts content → tags applied
- Indexed in `_SCREENSHOT_INDEX.json` with virtual folder structure
- Graph shows as nodes with connections, but `file_path` never changes

**Example:**
```json
{
  "id": "screenshot_123",
  "file_path": "~/Pictures/Screenshots/Screenshot 2025-10-09 at 14.32.15.png",
  "virtual_path": "AI_ML/Ethics/AI-frameworks",
  "primary_tags": ["ai-ethics", "infographic"],
  "ocr_content": "AI Ethics Framework: 5 Principles..."
}
```

### 2. Desktop Cleanup
**Rule:** Desktop is cleaned EVERY night at 2 AM (daily batch).

**Behavior:**
- All files on Desktop are scanned and tagged
- Files moved to appropriate destinations based on tags
- Change log created: `~/Desktop/_CHANGE_LOG.json`
- Desktop should be empty every morning (except folders user manually created)

**Exclusions (Never Move):**
- Folders created by user
- System files (`.DS_Store`, etc.)
- Files in "Do Not Organize" list (user-configurable)

### 3. Downloads Folder
**Rule:** Downloads cleaned EVERY night at 2 AM (daily batch).

**Behavior:**
- Similar to Desktop cleanup
- Downloaded files often have generic names → content analysis critical
- Installers (`.dmg`, `.pkg`) → `~/Downloads/Archive/` (not moved to Documents)
- Compressed files (`.zip`, `.tar.gz`) → unzipped if needed, then organized

### 4. Temporary Files
**Rule:** Files tagged `[temp]` or moved to `~/Documents/Temp/` are auto-deleted after 30 days.

**Warning Log:**
- Before deletion, system logs files to be deleted
- User can review and rescue if needed

### 5. Apple Notes
**Rule:** Apple Notes are NOT physically moved (they live in Apple's database).

**Behavior:**
- Notes extracted and represented as virtual nodes in graph
- Tags applied based on content
- Virtual organization only (like screenshots)

### 6. Project Files
**Rule:** Files tagged with `[project-*]` get special handling.

**Behavior:**
- Project name extracted from tag: `[project-amazon-interview]` → `amazon-interview`
- Destination: `~/Documents/_PROJECTS/amazon-interview/`
- Project folder created if doesn't exist
- Multiple project tags → file copied to each project (not moved)

---

## Naming Conventions

### Folder Names
- Use `CamelCase` or `snake_case` (no spaces)
- Prefix special folders with `_` (e.g., `_AUTOMATION`, `_ARCHIVE`)
- Descriptive, not generic (e.g., `AI_ML` not `Stuff`)

### File Names
- System NEVER renames files (preserves original names)
- If user prefers renamed files: Future feature (not Phase 1)

### Change Log Names
- Format: `_CHANGE_LOG.json` (consistent across all locations)
- Location: Same directory where files were moved FROM

---

## Conflict Resolution

### Duplicate Filenames
**Problem:** File `document.pdf` already exists in destination.

**Resolution Strategy:**
1. **Check content hash:** If identical content → skip move, log as duplicate
2. **If different content:**
   - Rename new file: `document_YYYY-MM-DD.pdf` (add date)
   - Move renamed file
   - Log conflict resolution

**Example Log Entry:**
```json
{
  "date": "2025-10-09",
  "original_name": "document.pdf",
  "renamed_to": "document_2025-10-09.pdf",
  "reason": "filename_conflict",
  "source": "~/Desktop/document.pdf",
  "destination": "~/Documents/Career/document_2025-10-09.pdf"
}
```

### Conflicting Tags
**Problem:** File has tags pointing to multiple destinations.

**Resolution Strategy:**
1. **Primary tag priority:** Use first primary tag (most relevant)
2. **If equal weight:** Use most specific tag (e.g., `[oxford]` > `[learning]`)
3. **Log ambiguity:** Flag for user review in next manual check

**Example:**
- Tags: `[oxford]`, `[career]`
- Priority: `[oxford]` (more specific)
- Destination: `~/Documents/AI_ML/Oxford/`
- Log: "Also tagged [career], consider cross-reference"

### Ambiguous Content
**Problem:** Content analysis yields no clear tags.

**Resolution Strategy:**
1. **Default destination:** `~/Documents/Reference/Unsorted/`
2. **Flag for review:** Add `[needs-review]` secondary tag
3. **Learn from corrections:** When user manually tags, system learns

---

## Execution Schedule

### Daily Batch (2 AM)
**What runs:**
1. Scan all monitored locations (Desktop, Downloads, iCloud)
2. Process new/modified files (OCR, tagging, relationship detection)
3. Move files to destinations based on tags
4. Update knowledge graph
5. Write change logs
6. Clean up temp files (older than 30 days)

**Duration:** Target <5 minutes for 1,000 files

**User Experience:** Wake up to organized Desktop/Downloads + change log

### Weekly Tasks (Sunday 2 AM)
- Archive old change logs (move to `~/Documents/_CHANGE_LOGS/Archive/`)
- Export Calendar .ics file (Phase 2)
- Compact database indexes
- Generate weekly analytics report

### Monthly Tasks (1st of month, 2 AM)
- Delete expired temp files (>30 days old)
- Archive completed projects (if tagged `[archive]`)
- Optimize graph database
- Backup all change logs to iCloud

---

## Change Log Format

### Log Structure
**Location:** `[source-directory]/_CHANGE_LOG.json`

**Format:**
```json
{
  "log_created": "2025-10-09T02:00:00Z",
  "location": "~/Desktop/",
  "moves": [
    {
      "date": "2025-10-09T02:15:32Z",
      "file": "AI Ethics Paper.pdf",
      "source": "~/Desktop/AI Ethics Paper.pdf",
      "destination": "~/Documents/AI_ML/Research/AI Ethics Paper.pdf",
      "primary_tags": ["ai-ethics", "research"],
      "secondary_tags": ["academic"],
      "reason": "content-based-tagging",
      "confidence": 0.92
    },
    {
      "date": "2025-10-09T02:15:45Z",
      "file": "resume_draft_v3.docx",
      "source": "~/Desktop/resume_draft_v3.docx",
      "destination": "~/Documents/Career/Resume/resume_draft_v3.docx",
      "primary_tags": ["career", "resume"],
      "secondary_tags": ["draft"],
      "reason": "content-based-tagging",
      "confidence": 0.98
    }
  ],
  "summary": {
    "total_files_moved": 25,
    "total_files_scanned": 30,
    "files_skipped": 5,
    "errors": 0
  }
}
```

### Log Retention
- **Active logs:** Last 7 days in source directory
- **Archive:** Older logs moved to `~/Documents/_CHANGE_LOGS/Archive/YYYY-MM/`
- **Retention:** Keep 1 year, then compress to yearly summary

---

## Example Scenarios

### Scenario 1: Morning Desktop Cleanup
**Before (Evening):**
```
~/Desktop/
├── AI Ethics Paper.pdf
├── Screenshot 2025-10-08 at 14.32.15.png
├── oxford_assignment_draft.docx
├── resume_v3.docx
└── random_notes.txt
```

**After (Morning):**
```
~/Desktop/
└── _CHANGE_LOG.json

Files moved:
- AI Ethics Paper.pdf → ~/Documents/AI_ML/Research/
- oxford_assignment_draft.docx → ~/Documents/AI_ML/Oxford/
- resume_v3.docx → ~/Documents/Career/Resume/
- random_notes.txt → ~/Documents/Reference/Unsorted/

Screenshot stayed:
- Screenshot 2025-10-08 at 14.32.15.png (virtual tag: [ai-tools])
```

### Scenario 2: Project File Organization
**File:** `amazon_pm_interview_prep.pdf` on Desktop

**Tags detected:** `[interview]`, `[amazon]`, `[product-management]`

**Decision:**
1. Primary tag: `[interview]` → Destination base: `~/Documents/Career/Interviews/`
2. Secondary tag: `[amazon]` → Create subfolder: `~/Documents/Career/Interviews/Amazon/`
3. Final path: `~/Documents/Career/Interviews/Amazon/amazon_pm_interview_prep.pdf`

**Log entry:**
```json
{
  "file": "amazon_pm_interview_prep.pdf",
  "source": "~/Desktop/amazon_pm_interview_prep.pdf",
  "destination": "~/Documents/Career/Interviews/Amazon/amazon_pm_interview_prep.pdf",
  "primary_tags": ["interview", "amazon", "product-management"],
  "reason": "content-based-tagging",
  "subfolder_created": true
}
```

### Scenario 3: Screenshot with Educational Content
**File:** `Screenshot 2025-10-09 at 10.15.22.png` (infographic about AI prompt engineering)

**OCR Content:** "10 Prompt Engineering Techniques: 1. Chain of Thought..."

**Tags detected:** `[ai-tools]`, `[prompts]`, `[infographic]`, `[learning]`

**Decision:**
- Physical location: STAYS at `~/Pictures/Screenshots/Screenshot 2025-10-09 at 10.15.22.png`
- Virtual organization: Tagged in graph as `AI_ML/Tools/Prompts`
- Searchable by: "prompt engineering", "AI tools", or visual browsing

**Graph entry:**
```json
{
  "id": "screenshot_20251009_101522",
  "file_path": "~/Pictures/Screenshots/Screenshot 2025-10-09 at 10.15.22.png",
  "virtual_path": "AI_ML/Tools/Prompts",
  "primary_tags": ["ai-tools", "prompts", "infographic"],
  "ocr_content": "10 Prompt Engineering Techniques: 1. Chain of Thought...",
  "relationships": [
    {"target": "ai_tools_project", "type": "related-content"}
  ]
}
```

### Scenario 4: Duplicate Filename Conflict
**File:** `notes.txt` on Desktop

**Destination:** `~/Documents/Reference/notes.txt` (already exists)

**Resolution:**
1. Hash check: Content is different
2. Rename: `notes_2025-10-09.txt`
3. Move: `~/Documents/Reference/notes_2025-10-09.txt`
4. Log conflict

**Log entry:**
```json
{
  "file": "notes.txt",
  "renamed_to": "notes_2025-10-09.txt",
  "source": "~/Desktop/notes.txt",
  "destination": "~/Documents/Reference/notes_2025-10-09.txt",
  "reason": "filename_conflict",
  "conflict_resolution": "rename_with_date"
}
```

### Scenario 5: Temporary File Auto-Cleanup
**File:** `temp_calculations.xlsx` moved to `~/Documents/Temp/` on 2025-09-01

**After 30 days (2025-10-01):**
1. System flags for deletion
2. Warning log created: "temp_calculations.xlsx will be deleted on 2025-10-08 (7-day grace period)"
3. User can review and move if needed
4. After grace period: File deleted, logged in deletion log

---

## Configuration Options (User Control)

### Configurable Settings
**File:** `~/.knowledge_map/config.json`

```json
{
  "organization": {
    "auto_organize": true,
    "desktop_cleanup": true,
    "downloads_cleanup": true,
    "schedule": "02:00",
    "temp_file_retention_days": 30,
    "do_not_organize": [
      "~/Desktop/Important/",
      "~/Documents/DoNotTouch/"
    ]
  },
  "conflict_resolution": {
    "duplicate_strategy": "rename_with_date",
    "ambiguous_destination": "Reference/Unsorted"
  },
  "change_logs": {
    "retention_days": 365,
    "archive_monthly": true
  }
}
```

### User Overrides
- User can manually move files → system updates graph, no re-organization
- User can create `.knowledge_map_ignore` file in folder → that folder never scanned
- User can edit change log before archiving (if needed for audit trail)

---

## Performance Considerations

### Optimization Strategies
1. **Incremental scanning:** Only new/modified files (use file modification dates)
2. **Batch moves:** Group moves by destination to reduce I/O
3. **Parallel processing:** OCR + tagging can run in parallel for multiple files
4. **Indexing:** Maintain index of file hashes to avoid re-processing

### Target Performance
- **1,000 files:** <5 minutes (full scan + organization)
- **10,000 files:** <30 minutes (initial scan), <5 minutes (daily incremental)
- **Single file move:** <100ms

---

## Error Handling

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Permission denied | Insufficient file access | Request Full Disk Access, log error |
| Disk full | Not enough space for move | Alert user, skip move, log |
| File in use | App has file open | Retry after 1 minute, skip if fails |
| Network drive disconnected | OneDrive/iCloud offline | Skip, retry next cycle |
| Invalid filename | Special characters | Sanitize filename, log warning |

### Error Logging
**Location:** `~/.knowledge_map/error.log`

**Format:**
```
[2025-10-09T02:15:32Z] ERROR: Permission denied for ~/Desktop/locked_file.pdf
[2025-10-09T02:15:45Z] WARNING: Disk space low, skipping large file move
```

---

## Future Enhancements (Post-MVP)

1. **User-defined rules:** Custom tag → destination mappings
2. **Machine learning:** System learns from user corrections over time
3. **Smart suggestions:** "This file might belong in [folder]?"
4. **Undo feature:** One-click revert of last organization batch
5. **File renaming:** Optional intelligent file renaming based on content
6. **Cloud sync:** Sync change logs across devices

---

**Status:** ✅ Complete

**Next Steps:**
1. Implement file mover module (see 05_PROCESSING_PIPELINE.md)
2. Test conflict resolution logic
3. Create change log writer

---

**Document Control:**
- Author: Claude Code
- Version: 1.0
- Last Updated: 2025-10-09
