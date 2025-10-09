# Product Requirements Document (PRD)
# Personal Knowledge Graph System

**Project:** knowledge_map v2.0 - Personal Knowledge Graph System
**Owner:** Jennifer McKinney
**Date Created:** 2025-10-09
**Status:** Draft - Design Phase
**Version:** 1.0

---

## Executive Summary

A comprehensive Personal Knowledge Graph System that automatically discovers, organizes, tags, and connects all digital artifacts across your ecosystem (files, notes, screenshots, calendar events) to reveal patterns, identify knowledge gaps, surface unrealized opportunities, and enable intelligent search and analysis.

**Core Value Proposition:**
Transform scattered digital artifacts into a connected knowledge graph that shows you:
- What you know
- How knowledge connects
- Where you spend time
- What gaps exist
- What opportunities are unrealized
- What you're truly good at

---

## Problem Statement

### Current Pain Points

**1. Scattered Information**
- Files across multiple locations (iCloud, OneDrive, local drives)
- Screenshots impossible to find ("which influencer was that?")
- Notes in Apple Notes disconnected from related files
- Calendar events not linked to work artifacts

**2. Manual Organization Overhead**
- Hard to keep desktop/folders tidy
- Time-consuming to tag and organize files
- No automated relationship detection
- File organization falls behind

**3. Lost Knowledge**
- Screenshots of educational content (AI tips, infographics) disappear
- Can't search by content (only by filename)
- No visibility into what you've learned
- Forgotten work that could be repurposed

**4. No Strategic Insights**
- Can't see knowledge gaps
- Don't know where time is spent vs. output created
- Missing cross-domain opportunities (e.g., AI + Career content)
- Can't identify your unique strengths/differentiators

**5. Business Value Untapped**
- Unique skill combinations invisible
- Content buried that could be repurposed
- Don't know what makes you different in market
- Can't quantify expertise areas

---

## Success Criteria

### Must Have (Phase 1 - MVP)

**Functional Requirements:**
1. ✅ Automatic file discovery across all locations (iCloud, OneDrive, Desktop, Downloads)
2. ✅ Screenshot OCR and content extraction (daily batch)
3. ✅ Dynamic content-based tagging (AI/NLP, minimal hard-coding)
4. ✅ Automated file organization (move files to proper locations)
5. ✅ Knowledge graph database (nodes + edges + relationships)
6. ✅ Change logs at each location (track file moves)
7. ✅ Apple Notes content extraction and integration
8. ✅ Search interface (find files by content, tags, relationships)
9. ✅ Visual graph interface (interactive, zoomable, based on current UI style)
10. ✅ Time tracking (basic: dates worked, not duration)

**Non-Functional Requirements:**
1. ✅ Privacy-first: All processing happens locally (no cloud AI unless user opts in)
2. ✅ Performance: Daily scan completes in <5 minutes
3. ✅ Reliability: Change logs prevent lost files
4. ✅ Maintainability: Minimal hard-coding, self-learning system
5. ✅ User Experience: Tidy file system, automated organization

**Success Metrics:**
- 100% of files discovered and tagged within 24 hours
- Screenshot search: Find any screenshot by content in <5 seconds
- File organization: Desktop clutter reduced by 90%
- Graph completeness: All files have ≥1 relationship
- User time saved: 80% reduction in manual file organization

### Should Have (Phase 2 - Enhanced)

1. Calendar integration (weekly sync)
2. Photos Library integration (non-screenshots)
3. Cross-source relationship detection (files ↔ events ↔ photos)
4. Advanced analytics dashboard (gaps, patterns, opportunities)
5. Business value insights ("What makes you unique?")
6. Advanced time tracking (duration spent in documents)

### Could Have (Phase 3 - Advanced)

1. Email integration
2. App usage tracking
3. External storage (USB drives when connected)
4. Collaborative graph (shared folders with others)
5. Export/publishing (turn graph into portfolio/website)
6. Mobile app (iOS companion)

### Won't Have (Out of Scope)

1. Real-time file watching (daily batch is sufficient)
2. Cloud-based processing (everything stays local)
3. Social media integration
4. Blockchain/crypto features
5. Multi-user/team features (single user system)

---

## User Personas & Use Cases

### Primary Persona: Jennifer McKinney

**Background:**
- Professional: Product Manager with AI/ML focus
- Education: Oxford AI Programme student
- Work Style: Scattered learning (screenshots, notes, docs across devices)
- Pain: Can't find educational screenshots, knowledge disconnected
- Goal: Understand strengths, find opportunities, leverage unique skill combo

**Key Use Cases:**

**Use Case 1: Find That Screenshot**
```
Scenario: "I saw an infographic about AI ethics frameworks 2 weeks ago.
          Where is it?"

Current State: Search through 200+ screenshots by date, give up

Desired State:
1. Search: "AI ethics framework"
2. System finds screenshot via OCR content
3. Shows related files (Oxford notes, research papers)
4. Found in <5 seconds
```

**Use Case 2: Tidy Desktop Automatically**
```
Scenario: Desktop has 30 files after a busy week

Current State: Manually sort files into folders (20 minutes)

Desired State:
1. System runs daily (2 AM)
2. Auto-tags all files by content
3. Moves to proper folders based on tags
4. Morning: Desktop has 0 files, change log shows what moved
```

**Use Case 3: Discover Knowledge Gaps**
```
Scenario: "Where should I focus learning/content creation?"

Current State: No visibility into knowledge landscape

Desired State:
1. Open analytics dashboard
2. See: "85 files on AI, 62 on Career, only 3 connect both"
3. Insight: "Create more AI + Career content"
4. Opportunity: "AI Product Leadership is your differentiator"
```

**Use Case 4: Understand Time vs. Output**
```
Scenario: "Am I productive or just busy?"

Current State: Feel busy, not sure if output matches

Desired State:
1. Calendar shows: 15 hours in "AI Ethics meetings" this month
2. Graph shows: 2 files tagged [ai-ethics] created
3. Gap detected: High time input, low artifact output
4. Action: Create more documentation/notes
```

**Use Case 5: Leverage Apple Notes**
```
Scenario: "I have tons of notes on my phone - connect them to my work"

Current State: Notes on iPhone, files on Mac, no connection

Desired State:
1. Apple Notes synced to graph daily
2. Note: "Meeting with Sarah about Oxford project"
3. Auto-linked to: Calendar event, Oxford files, related screenshots
4. Search "Sarah" shows everything connected
```

---

## System Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│              DATA SOURCES (Input)                        │
├─────────────────────────────────────────────────────────┤
│ • iCloud Drive (Documents, Desktop)                     │
│ • OneDrive (synced files)                               │
│ • Local (Downloads, Desktop)                            │
│ • Apple Notes (iPhone + Desktop sync)                   │
│ • Screenshots (across all locations)                    │
│ • Calendar (weekly export - Phase 2)                    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│           PROCESSING PIPELINE                            │
├─────────────────────────────────────────────────────────┤
│ 1. File Discovery (daily scan)                          │
│ 2. Content Extraction (OCR, text, metadata)             │
│ 3. Dynamic Tagging (AI/NLP analysis)                    │
│ 4. Relationship Detection (similarity, temporal, etc.)  │
│ 5. File Organization (move to proper folders)           │
│ 6. Change Logging (track all moves)                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│          KNOWLEDGE GRAPH DATABASE                        │
├─────────────────────────────────────────────────────────┤
│ • Nodes (files, notes, events, screenshots)             │
│ • Edges (relationships with weights, dates, WHY)        │
│ • Tags (primary, secondary, auto-keywords)              │
│ • Metadata (time tracking, change history)              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              USER INTERFACES                             │
├─────────────────────────────────────────────────────────┤
│ • Graph Visualization (interactive, current UI style)   │
│ • Search Interface (content, tags, relationships)       │
│ • Analytics Dashboard (gaps, patterns, opportunities)   │
│ • File Browser (organized view)                         │
│ • Change Log Viewer (audit trail)                       │
└─────────────────────────────────────────────────────────┘
```

### Core Components

**1. File System Watcher**
- Scans all monitored locations daily (2 AM)
- Detects new/modified files
- Queues for processing

**2. Content Extractor**
- PDF → Text extraction
- Images → OCR (Tesseract or Apple Vision)
- Word/Pages → Document text
- Apple Notes → Note content
- Metadata → Dates, size, type

**3. Auto-Tagger (Dynamic)**
- NLP topic modeling (local, privacy-preserving)
- Entity extraction (people, places, organizations)
- Document type classification
- Context awareness (recent calendar, nearby files)
- Learning from user corrections (improves over time)

**4. Relationship Engine**
- Content similarity analysis
- Temporal relationships (same day/week/month)
- Hierarchical (folder structure)
- Cross-domain bridges (AI + Career, etc.)
- Manual user links

**5. File Organizer**
- Determines destination folder from tags
- Moves files (not copies)
- Updates graph with new paths
- Creates change log entries

**6. Change Logger**
- JSON log per master location
- Records: date, file, old path, new path, reason, tags
- Old location keeps record (for user lookup)

**7. Graph Database**
- Nodes: All artifacts
- Edges: Relationships with weights, dates, WHY
- Tags: Primary (1-3), secondary (unlimited), keywords (auto)
- Required fields: date_created, type

**8. Analytics Engine**
- Pattern detection (work habits, strengths)
- Gap analysis (isolated clusters, missing connections)
- Opportunity finder (cross-domain bridges)
- Business value insights (unique combinations)
- Time vs. output correlation

**9. Web UI**
- Knowledge graph view (D3.js, current visual style)
- Search bar (content, tags, filenames)
- Filters (by type, date, location, tags)
- Analytics dashboard (insights, charts)
- Change log viewer

---

## Data Requirements

### Master Keys (Required for ALL Nodes)

Every file/note/event MUST have:
```javascript
{
  id: "unique_id",
  date_created: "YYYY-MM-DD",
  type: "[document|image|screenshot|note|event|etc.]",
  file_path: "/full/path/to/file",
  file_name: "filename.ext",
  primary_tags: ["tag1", "tag2", "tag3"],  // 1-3 required
  secondary_tags: [],                       // unlimited, optional
  keywords: [],                             // auto-extracted
  relationships: []                         // edges to other nodes
}
```

### Relationship Schema

```javascript
{
  source: "node_id_1",
  target: "node_id_2",
  weight: 0.8,                    // 0.0 to 1.0
  created_date: "YYYY-MM-DD",     // When relationship formed
  why: ["temporal-same-day", "shared-tags"],  // Reasons
  type: "content-similarity",     // Category
  metadata: {}                    // Additional context
}
```

### Tag Categories

**1. Type Tags (1 required)**
- [document], [image], [screenshot], [video], [note], [spreadsheet], etc.

**2. Primary Tags (1-3 required)**
- Main topics: [ai-ethics], [oxford], [career], [product-management]
- Projects: [amazon-interview], [thesis-research]
- Themes: [learning], [work], [personal]

**3. Secondary Tags (unlimited, optional)**
- Descriptors: [infographic], [quote], [tutorial], [reference], [draft]
- Quality: [important], [archive], [needs-review]
- Source: [social-media], [website], [textbook]

**4. Auto-Keywords (unlimited, automatic)**
- Extracted from content via NLP
- Searchable but not displayed as primary tags

---

## Technical Constraints

### Platform
- **OS:** macOS (primary development target)
- **Deployment:** Local installation on user's Mac
- **Storage:** Local disk (iCloud sync handled by macOS)
- **Processing:** All local (privacy-first)

### Technology Stack (Recommendations)

**Backend:**
- Language: Python 3.9+
- NLP: spaCy, scikit-learn (local processing)
- OCR: Tesseract or Apple Vision Framework
- Database: JSON files or SQLite (lightweight, portable)
- File watching: watchdog library (Python)

**Frontend:**
- Framework: HTML/CSS/JavaScript (static files)
- Visualization: D3.js (current graph style)
- UI: Minimal framework (vanilla JS or lightweight library)
- Hosting: Local web server (Python http.server or similar)

**Optional (User Choice):**
- AI API: OpenAI or Claude API for advanced tagging (opt-in, costs ~$0.01/file)

### Performance Requirements

- Daily scan: Complete in <5 minutes for 10,000 files
- Search: Return results in <1 second
- Graph render: Load 1,000 nodes in <3 seconds
- File move: <100ms per file
- OCR: Process screenshot in <2 seconds

### Storage Requirements

- Graph database: ~10MB per 1,000 files
- Change logs: ~1MB per 10,000 moves
- Indexes: ~5MB per 10,000 files
- Total: Minimal (~50MB for typical user)

---

## Dependencies & Integrations

### macOS Dependencies
- File system access (standard)
- Spotlight metadata (kMDItem* attributes)
- Apple Notes database (~/Library/Group Containers/group.com.apple.notes/)
- Photos Library (optional, Phase 2)
- Calendar (manual export .ics, Phase 2)

### Python Libraries
- pathlib (file operations)
- watchdog (file monitoring)
- pytesseract (OCR)
- spaCy (NLP)
- scikit-learn (ML)
- sqlite3 (database - built-in)
- json (data storage - built-in)

### External APIs (Optional)
- OpenAI GPT-4 (advanced tagging)
- Claude API (advanced tagging)
- None required for core functionality

---

## Security & Privacy

### Privacy Requirements
1. **No cloud upload** unless user explicitly opts in
2. **Local processing** for all content analysis
3. **No telemetry** - no usage data sent anywhere
4. **Encrypted storage** for sensitive metadata (future)
5. **User control** over all data

### Data Access
- Read-only access to user files (scanning)
- Write access for file organization (moving files)
- No modification of file contents
- No external network access (except optional AI API)

### Permissions Required
- Full Disk Access (macOS System Preferences)
- Access to iCloud Drive
- Access to Apple Notes database
- Access to Photos Library (Phase 2)

---

## User Experience Requirements

### Design Principles
1. **Minimal user intervention** - System should "just work"
2. **Tidy by default** - Automated organization keeps system clean
3. **Transparent** - Show what's happening (change logs, audit trail)
4. **Forgiving** - Easy to undo moves, find relocated files
5. **Visual learner friendly** - Graphs, charts, visual representations

### UI Requirements
1. **Match current style** - Use existing knowledge_map visual design
2. **Color scheme** - Keep current colors (user likes them)
3. **Interactive graph** - Zoomable, clickable, filterable
4. **Search-first** - Prominent search bar
5. **Mobile-friendly** - Responsive design (future)

### UX Flows

**Daily Morning Routine:**
1. Wake up, open system
2. See: "25 files organized overnight"
3. Click change log → See what moved where
4. Desktop is clean, everything findable

**Search for Screenshot:**
1. Type: "AI ethics framework"
2. Results appear instantly
3. Click result → Opens file + shows related items
4. Graph highlights connections

**Discover Insights:**
1. Open analytics dashboard
2. See: Knowledge clusters, gaps, time allocation
3. Click opportunity → Drill into specific area
4. Take action based on insights

---

## Risks & Mitigation

### Technical Risks

**Risk 1: File moves break user workflows**
- Mitigation: Change logs show old → new paths
- Mitigation: Search still finds files regardless of location
- Mitigation: User can configure "do not move" folders

**Risk 2: OCR accuracy issues**
- Mitigation: Use high-quality OCR engine (Apple Vision preferred)
- Mitigation: Manual tag correction improves system
- Mitigation: Keyword search as fallback

**Risk 3: Performance with large file sets (100k+ files)**
- Mitigation: Incremental scanning (only new/modified files)
- Mitigation: Database indexing
- Mitigation: Lazy loading in UI

**Risk 4: Apple Notes database structure changes**
- Mitigation: Use stable libraries (e.g., osxphotos approach)
- Mitigation: Fallback to manual export
- Mitigation: Version detection and adaptation

### User Experience Risks

**Risk 5: User disagrees with auto-organization**
- Mitigation: Learning system adapts to corrections
- Mitigation: Undo functionality
- Mitigation: Configurable rules

**Risk 6: Too many tags, overwhelming**
- Mitigation: Show only primary tags by default
- Mitigation: Progressive disclosure (expand for more)
- Mitigation: Tag hierarchies

---

## Timeline & Milestones

### ⚡ AGGRESSIVE 2-WEEK TIMELINE

### Week 1 (Days 1-7) - Core System
- File system scanner (iCloud, OneDrive, Desktop, Downloads)
- Screenshot OCR (HIGH PRIORITY)
- Dynamic tagging engine (Claude API + local NLP)
- File organization + change logging
- Knowledge graph database
- Apple Notes integration
- Calendar integration (weekly sync)
- Email integration
- Web UI (search + graph visualization)
- Basic analytics (gaps, patterns, opportunities)

**Milestone:** Fully functional core system with search

### Week 2 (Days 8-14) - Advanced Features
- Photo Library integration
- Advanced analytics (business intelligence, predictions, trends, ROI)
- Advanced time tracking (duration in documents)
- Mobile app (iOS companion)
- Polish, testing, refinement

**Milestone:** Complete system with all features

---

## Open Questions - ✅ RESOLVED

1. **AI API Usage:** ✅ Use Claude API for dynamic tagging/NLP
2. **File Organization:** ✅ Fully automatic (no approval needed)
3. **Change Log Retention:** ✅ Archive after 1 month to iCloud location
4. **Screenshots Destination:** ✅ Leave in place, organize virtually in graph
5. **Apple Notes:** ✅ Include ALL notes

---

## Success Measurement

### Quantitative Metrics
- Files discovered: Target 100% within 24 hours
- Search accuracy: >95% relevant results
- Search speed: <1 second average
- Organization rate: >90% of files auto-organized correctly
- User time saved: 80% reduction in manual organization (20 min → 4 min/week)

### Qualitative Metrics
- User satisfaction: "I can find anything instantly"
- System trust: "I trust the auto-organization"
- Insight value: "I discovered opportunities I didn't know existed"
- Productivity: "I spend less time organizing, more time creating"

### Business Impact
- Unique positioning discovered: "I know what makes me different"
- Content repurposed: "I'm leveraging existing knowledge"
- Opportunities identified: "I see gaps to fill"
- Time optimization: "I know where to focus my energy"

---

## Appendix

### Reference Documents
- file_system_schema.md (existing paths)
- UPDATED_AUTOMATION_INSTRUCTIONS.md (existing setup)
- BUG_AUDIT_REPORT.md (existing codebase issues)

### Related Projects
- Current knowledge_map HTML files (visualization reference)
- generic_downloads_organizer.py (organization patterns)
- generic_documents_organizer.py (categorization logic)

---

**Status:** ✅ READY FOR REVIEW

**Next Steps:**
1. Review and approve PRD
2. Create remaining design documents (02-12)
3. Begin Phase 1 implementation
4. Commit to Git repository

---

**Document Control:**
- Author: Jennifer McKinney + Claude Code
- Reviewers: Jennifer McKinney
- Approval Required: Yes
- Version History: v1.0 (2025-10-09) - Initial draft
