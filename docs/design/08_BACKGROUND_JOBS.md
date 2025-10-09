# Background Jobs & Scheduling
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Final

---

## Overview

The Personal Knowledge Graph System runs automated background jobs to keep the knowledge graph synchronized, organized, and up-to-date. Jobs are scheduled at optimal times to minimize disruption and ensure fresh data.

**Design Principles:**
- Run during low-usage hours (overnight/weekends)
- Complete quickly (<5 minutes for daily jobs)
- Handle errors gracefully without breaking workflow
- Log all operations for transparency and debugging
- Support manual triggers for on-demand processing

---

## Daily Jobs (2:00 AM)

### Execution Order

Jobs run sequentially in this order to handle dependencies:

#### 1. File Discovery & Scanning (2:00-2:01 AM)
**What:** Scan all monitored locations for new/modified files
- iCloud Documents
- iCloud Desktop
- Local Downloads
- OneDrive (all synced paths)

**Output:** List of files requiring processing

**Duration:** ~30-60 seconds for 10,000 files

#### 2. Screenshot OCR Processing (2:01-2:03 AM)
**What:** Extract text from all unprocessed screenshots
- Detect screenshots (filename patterns, metadata)
- Run OCR (Apple Vision API or Tesseract)
- Extract visible text content
- Classify type (infographic, quote, chart, code)

**Priority:** CRITICAL - Screenshots are highest user value

**Duration:** ~2 seconds per screenshot (~2 minutes for 60 screenshots)

#### 3. Content Extraction (2:03-2:04 AM)
**What:** Extract content from documents
- PDFs → text extraction
- DOCX/Pages → document text
- TXT/MD → direct read
- Extract metadata (author, dates, titles)

**Duration:** ~30-60 seconds

#### 4. Dynamic Tagging (2:04-2:05 AM)
**What:** Auto-tag all new/modified content
- NLP topic modeling (spaCy + scikit-learn)
- Entity extraction (people, organizations, places)
- Document classification
- Keyword extraction
- Tag assignment (primary + secondary)

**AI Option:** Claude API for advanced tagging (opt-in)

**Duration:** ~1 minute for 100 files

#### 5. Relationship Detection (2:05-2:06 AM)
**What:** Create/update relationships between nodes
- Content similarity analysis
- Temporal relationships (same day/week)
- Shared tags/keywords
- Cross-domain connections

**Duration:** ~30 seconds

#### 6. File Organization (2:06-2:07 AM)
**What:** Move files to appropriate locations based on tags
- Determine destination folder from tag rules
- Move files (not copy)
- Update graph with new paths
- Handle conflicts (duplicate names)

**Skip:** Files in "do not move" folders

**Duration:** ~100ms per file (~1 minute for 500 files)

#### 7. Change Log Generation (2:07 AM)
**What:** Record all file moves and changes
- Create JSON log entry per location
- Record: date, file, old path, new path, reason, tags
- Store in original location for user reference

**Duration:** <10 seconds

#### 8. Rogue File Detection (2:07 AM)
**What:** Identify files in unexpected locations
- Desktop files not yet organized
- Downloads older than 7 days
- Untagged files
- Files outside monitored locations

**Output:** Alert list for user review

**Duration:** <10 seconds

**Total Daily Job Time:** ~5-7 minutes

---

## Weekly Jobs (Sunday 11:00 PM)

### Execution Order

#### 1. Apple Notes Sync (11:00-11:02 PM)
**What:** Extract all notes from Apple Notes database
- Read SQLite database (`~/Library/Group Containers/group.com.apple.notes/`)
- Extract: title, content, dates, folders, attachments
- Create/update note nodes in graph
- Detect relationships with files/events

**Frequency:** Weekly (notes change less frequently)

**Duration:** ~2 minutes for 500 notes

#### 2. Calendar Sync (11:02-11:03 PM)
**What:** Import calendar events (Phase 2)
- Export .ics file from Calendar.app
- Parse events, dates, attendees, notes
- Create event nodes in graph
- Link to related files (temporal + keyword matching)

**Purpose:** Time tracking, activity correlation

**Duration:** ~1 minute for 1,000 events

#### 3. Photo Library Sync (11:03-11:05 PM) - Phase 2
**What:** Index Photos Library (non-screenshots)
- Scan Photos.photoslibrary
- Extract metadata (dates, locations, albums, faces)
- OCR text in photos
- Create photo nodes in graph

**Exclude:** Screenshots (handled daily)

**Duration:** ~2 minutes for incremental sync

#### 4. Analytics Computation (11:05-11:06 PM)
**What:** Pre-compute analytics for dashboard
- Knowledge clusters
- Gap analysis (isolated nodes)
- Cross-domain opportunities
- Time vs. output correlation
- Tag frequency distributions
- Relationship patterns

**Purpose:** Fast dashboard loading

**Duration:** ~1 minute

**Total Weekly Job Time:** ~6 minutes

---

## Monthly Jobs (1st of Month, 3:00 AM)

### Execution Order

#### 1. Archive Old Change Logs (3:00 AM)
**What:** Move logs older than 30 days to archive
- Source: Change log JSONs at each location
- Destination: `~/Library/Mobile Documents/.../iCloud_Knowledge_Map_Archive/change_logs/YYYY-MM/`
- Compress: Gzip archived logs
- Retain: Last 30 days in original locations

**Purpose:** Keep system tidy, preserve history

**Duration:** <30 seconds

#### 2. Monthly Insights Report (3:00-3:01 AM)
**What:** Generate comprehensive monthly report
- Files added/organized this month
- Top tags and topics
- Knowledge gaps identified
- Cross-domain opportunities discovered
- Time allocation summary
- Productivity metrics (time vs. output)

**Output:** Markdown report + JSON data

**Destination:** `~/Library/Mobile Documents/.../Reports/YYYY-MM.md`

**Duration:** ~1 minute

#### 3. Stale File Detection (3:01-3:02 AM)
**What:** Identify potentially obsolete files
- Files not accessed in 6+ months
- Draft files never finalized
- Duplicate content
- Low-value tags (auto-suggestion for archive)

**Output:** Review list (not auto-deleted)

**Duration:** ~1 minute

#### 4. Database Optimization (3:02-3:03 AM)
**What:** Optimize graph database
- SQLite VACUUM (compact database)
- Rebuild indexes
- Remove orphaned relationships (target files deleted)
- Verify data integrity

**Purpose:** Maintain performance

**Duration:** ~1 minute

**Total Monthly Job Time:** ~3-4 minutes

---

## Job Scheduling

### Recommended: launchd (macOS Native)

**Why launchd:**
- Native macOS solution (no dependencies)
- Reliable, always runs
- System-level scheduling
- Handles missed jobs (if Mac was asleep)
- Low resource usage

**Configuration:**

Create plist files in `~/Library/LaunchAgents/`:

**Daily Job:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge_map.daily</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/path/to/knowledge_map/jobs/daily_job.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/path/to/logs/daily.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/logs/daily_error.log</string>
</dict>
</plist>
```

**Weekly Job:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge_map.weekly</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/path/to/knowledge_map/jobs/weekly_job.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>0</integer> <!-- 0 = Sunday -->
        <key>Hour</key>
        <integer>23</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/path/to/logs/weekly.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/logs/weekly_error.log</string>
</dict>
</plist>
```

**Monthly Job:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge_map.monthly</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/path/to/knowledge_map/jobs/monthly_job.py</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Day</key>
        <integer>1</integer> <!-- 1st of month -->
        <key>Hour</key>
        <integer>3</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/path/to/logs/monthly.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/logs/monthly_error.log</string>
</dict>
</plist>
```

**Load Jobs:**
```bash
launchctl load ~/Library/LaunchAgents/com.knowledge_map.daily.plist
launchctl load ~/Library/LaunchAgents/com.knowledge_map.weekly.plist
launchctl load ~/Library/LaunchAgents/com.knowledge_map.monthly.plist
```

**Unload Jobs:**
```bash
launchctl unload ~/Library/LaunchAgents/com.knowledge_map.daily.plist
launchctl unload ~/Library/LaunchAgents/com.knowledge_map.weekly.plist
launchctl unload ~/Library/LaunchAgents/com.knowledge_map.monthly.plist
```

### Alternative: Python APScheduler

**Why APScheduler:**
- Pure Python (no system configuration)
- Easier to debug
- More flexible (dynamic scheduling)

**Configuration:**

```python
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

scheduler = BlockingScheduler()

# Daily job at 2:00 AM
scheduler.add_job(
    run_daily_jobs,
    CronTrigger(hour=2, minute=0),
    id='daily_job',
    name='Daily knowledge graph update'
)

# Weekly job on Sunday at 11:00 PM
scheduler.add_job(
    run_weekly_jobs,
    CronTrigger(day_of_week='sun', hour=23, minute=0),
    id='weekly_job',
    name='Weekly sync jobs'
)

# Monthly job on 1st at 3:00 AM
scheduler.add_job(
    run_monthly_jobs,
    CronTrigger(day=1, hour=3, minute=0),
    id='monthly_job',
    name='Monthly maintenance'
)

scheduler.start()
```

**Run as Service:**
- Create launchd plist to run scheduler.py
- Scheduler stays running, triggers jobs at specified times

### Alternative: Cron (Unix Standard)

**Why Cron:**
- Simple, well-known
- Available on all Unix systems

**Configuration:**

```bash
# Edit crontab
crontab -e

# Daily job at 2:00 AM
0 2 * * * /usr/local/bin/python3 /path/to/knowledge_map/jobs/daily_job.py >> /path/to/logs/daily.log 2>&1

# Weekly job on Sunday at 11:00 PM
0 23 * * 0 /usr/local/bin/python3 /path/to/knowledge_map/jobs/weekly_job.py >> /path/to/logs/weekly.log 2>&1

# Monthly job on 1st at 3:00 AM
0 3 1 * * /usr/local/bin/python3 /path/to/knowledge_map/jobs/monthly_job.py >> /path/to/logs/monthly.log 2>&1
```

**Recommendation:** Use **launchd** (native, reliable, handles sleep/wake)

---

## Error Handling

### Principles

1. **Fail gracefully** - Don't crash entire job if one file fails
2. **Log everything** - Capture errors with context
3. **Retry logic** - Attempt 3 times before giving up
4. **Alert user** - Notify of critical failures
5. **Continue processing** - Skip failed items, process rest

### Error Types & Responses

#### File Access Errors
**Examples:** Permission denied, file not found, file locked

**Response:**
- Log error with file path and reason
- Skip file, continue processing others
- Add to retry queue (attempt next run)
- Alert if >10% of files fail

#### OCR Failures
**Examples:** Corrupted image, unsupported format, OCR timeout

**Response:**
- Log failed screenshot path
- Tag as `[ocr-failed]` for manual review
- Continue with other screenshots
- Retry with alternative OCR engine

#### API Failures (Claude/OpenAI)
**Examples:** API timeout, rate limit, authentication error

**Response:**
- Fall back to local NLP (spaCy)
- Log API failure
- Continue with local processing
- Retry API on next run

#### Database Errors
**Examples:** Corruption, lock timeout, disk full

**Response:**
- Attempt database repair (VACUUM, REINDEX)
- Fall back to read-only mode
- Alert user (CRITICAL)
- Create backup before any repair

#### System Resource Errors
**Examples:** Out of memory, disk full, CPU overload

**Response:**
- Pause processing
- Log resource state
- Retry with smaller batches
- Alert user to check system

### Error Notification

**Critical Errors (Immediate Alert):**
- Database corruption
- Disk full
- >50% of files fail processing
- System crash/restart

**Warning Errors (Daily Summary):**
- <10% file failures
- OCR failures
- API rate limits
- Permission issues

**Info Errors (Logged Only):**
- Individual file skipped
- Duplicate detection
- Already processed

**Alert Methods:**
- macOS notification (critical only)
- Email summary (daily digest)
- Dashboard warning banner
- Log file entry

### Example Error Handler

```python
import logging
from functools import wraps

def handle_errors(max_retries=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except FileNotFoundError as e:
                    logging.error(f"File not found: {e}")
                    break  # Don't retry
                except PermissionError as e:
                    logging.error(f"Permission denied: {e}")
                    break  # Don't retry
                except Exception as e:
                    retries += 1
                    logging.warning(f"Attempt {retries}/{max_retries} failed: {e}")
                    if retries >= max_retries:
                        logging.error(f"Max retries exceeded for {func.__name__}")
                        raise
            return None
        return wrapper
    return decorator

@handle_errors(max_retries=3)
def process_file(file_path):
    # Processing logic
    pass
```

---

## Logging

### Log Locations

```
~/Library/Mobile Documents/.../iCloud_Knowledge_Map_Logs/
├── jobs/
│   ├── daily_YYYY-MM-DD.log          # Daily job execution
│   ├── weekly_YYYY-MM-DD.log         # Weekly job execution
│   ├── monthly_YYYY-MM.log           # Monthly job execution
│   └── errors_YYYY-MM-DD.log         # All errors
├── processing/
│   ├── ocr_YYYY-MM-DD.log            # OCR operations
│   ├── tagging_YYYY-MM-DD.log        # Auto-tagging
│   └── organization_YYYY-MM-DD.log   # File moves
└── system/
    ├── performance_YYYY-MM-DD.log    # Timing/resource usage
    └── api_YYYY-MM-DD.log            # API calls (if enabled)
```

### Log Format

```
YYYY-MM-DD HH:MM:SS [LEVEL] [MODULE] Message
Context: Additional details
```

**Example:**
```
2025-10-09 02:01:34 [INFO] [scanner] Starting daily file scan
2025-10-09 02:01:35 [INFO] [scanner] Found 157 new files, 23 modified
2025-10-09 02:01:56 [INFO] [ocr] Processing 12 screenshots
2025-10-09 02:01:58 [WARNING] [ocr] Failed to process screenshot_2025-10-08.png
Context: Unsupported image format (WebP)
2025-10-09 02:02:15 [INFO] [ocr] Completed: 11 success, 1 failed
2025-10-09 02:03:42 [INFO] [organizer] Moved 45 files
2025-10-09 02:03:43 [INFO] [daily_job] Daily job completed in 4m 9s
```

### Log Levels

- **DEBUG:** Verbose details (disabled by default)
- **INFO:** Normal operation events
- **WARNING:** Recoverable issues
- **ERROR:** Failures requiring attention
- **CRITICAL:** System-level failures

### Log Rotation

**Daily Logs:**
- Retain: 30 days
- Archive: Compress logs >30 days to gzip
- Location: `iCloud_Knowledge_Map_Archive/logs/YYYY-MM/`

**Monthly Logs:**
- Retain: 12 months
- Archive: Compress after 1 year

**Error Logs:**
- Retain: 90 days (longer for debugging)
- Never auto-delete critical errors

**Rotation Script (runs monthly):**
```python
import gzip
import shutil
from datetime import datetime, timedelta

def rotate_logs():
    log_dir = Path("~/Library/Mobile Documents/.../iCloud_Knowledge_Map_Logs/")
    archive_dir = Path("~/Library/Mobile Documents/.../iCloud_Knowledge_Map_Archive/logs/")
    cutoff_date = datetime.now() - timedelta(days=30)

    for log_file in log_dir.rglob("*.log"):
        if log_file.stat().st_mtime < cutoff_date.timestamp():
            # Compress
            archive_path = archive_dir / log_file.parent.name / f"{log_file.stem}.log.gz"
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            with open(log_file, 'rb') as f_in:
                with gzip.open(archive_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            log_file.unlink()
```

---

## Manual Triggers

### Purpose

Allow users to run jobs on-demand:
- After bulk file import
- Before important search
- Testing/debugging
- Immediate organization

### CLI Commands

**Run Daily Job:**
```bash
python3 /path/to/knowledge_map/jobs/daily_job.py --manual
```

**Run Specific Task:**
```bash
python3 /path/to/knowledge_map/jobs/daily_job.py --task=ocr
python3 /path/to/knowledge_map/jobs/daily_job.py --task=organize
python3 /path/to/knowledge_map/jobs/daily_job.py --task=tag
```

**Run Weekly Job:**
```bash
python3 /path/to/knowledge_map/jobs/weekly_job.py --manual
```

**Run Monthly Job:**
```bash
python3 /path/to/knowledge_map/jobs/monthly_job.py --manual
```

**Process Specific Folder:**
```bash
python3 /path/to/knowledge_map/jobs/process_folder.py --path=/path/to/folder
```

**Force Full Rescan:**
```bash
python3 /path/to/knowledge_map/jobs/daily_job.py --full-rescan
```

### Web UI Triggers

**Dashboard Actions:**
- "Run Scan Now" button
- "Organize Files" button
- "Process Screenshots" button
- "Sync Notes" button

**Implementation:**
```python
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/api/jobs/trigger', methods=['POST'])
def trigger_job():
    job_type = request.json.get('job_type')
    allowed_jobs = ['daily', 'weekly', 'monthly', 'ocr', 'organize']

    if job_type not in allowed_jobs:
        return jsonify({'error': 'Invalid job type'}), 400

    # Run job in background
    subprocess.Popen([
        'python3',
        f'/path/to/knowledge_map/jobs/{job_type}_job.py',
        '--manual'
    ])

    return jsonify({'status': 'Job started', 'job': job_type})
```

### Safety Guards

**Prevent Concurrent Runs:**
```python
import fcntl

def acquire_lock(lock_file):
    lock = open(lock_file, 'w')
    try:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        return lock
    except IOError:
        return None

# Usage
lock = acquire_lock('/tmp/knowledge_map_daily.lock')
if not lock:
    print("Job already running, exiting")
    sys.exit(0)

try:
    run_daily_jobs()
finally:
    lock.close()
```

---

## Example Job Configurations

### Daily Job Script

```python
#!/usr/bin/env python3
"""
Daily Knowledge Graph Update Job
Runs at 2:00 AM daily
"""

import logging
import sys
from datetime import datetime
from pathlib import Path

# Setup logging
log_file = Path.home() / "Library/Mobile Documents/.../iCloud_Knowledge_Map_Logs/jobs" / f"daily_{datetime.now().strftime('%Y-%m-%d')}.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('daily_job')

def run_daily_jobs():
    """Execute all daily jobs in sequence"""
    start_time = datetime.now()
    logger.info("=" * 60)
    logger.info("Starting daily knowledge graph update")
    logger.info("=" * 60)

    try:
        # 1. File Discovery
        logger.info("Step 1: File discovery and scanning")
        from knowledge_map.scanner import FileScanner
        scanner = FileScanner()
        new_files, modified_files = scanner.scan_all_locations()
        logger.info(f"Found {len(new_files)} new files, {len(modified_files)} modified")

        # 2. Screenshot OCR
        logger.info("Step 2: Screenshot OCR processing")
        from knowledge_map.ocr import ScreenshotProcessor
        ocr = ScreenshotProcessor()
        screenshots = [f for f in new_files if ocr.is_screenshot(f)]
        ocr_results = ocr.process_batch(screenshots)
        logger.info(f"Processed {len(screenshots)} screenshots")

        # 3. Content Extraction
        logger.info("Step 3: Content extraction")
        from knowledge_map.extractors import ContentExtractor
        extractor = ContentExtractor()
        for file in new_files + modified_files:
            extractor.extract(file)
        logger.info(f"Extracted content from {len(new_files) + len(modified_files)} files")

        # 4. Dynamic Tagging
        logger.info("Step 4: Dynamic tagging")
        from knowledge_map.tagger import AutoTagger
        tagger = AutoTagger()
        for file in new_files + modified_files:
            tags = tagger.tag_file(file)
            logger.debug(f"Tagged {file.name}: {tags}")
        logger.info(f"Tagged {len(new_files) + len(modified_files)} files")

        # 5. Relationship Detection
        logger.info("Step 5: Relationship detection")
        from knowledge_map.relationships import RelationshipEngine
        rel_engine = RelationshipEngine()
        rel_engine.detect_relationships(new_files + modified_files)
        logger.info("Relationships updated")

        # 6. File Organization
        logger.info("Step 6: File organization")
        from knowledge_map.organizer import FileOrganizer
        organizer = FileOrganizer()
        moved_files = organizer.organize_files(new_files)
        logger.info(f"Organized {len(moved_files)} files")

        # 7. Change Log
        logger.info("Step 7: Change log generation")
        from knowledge_map.changelog import ChangeLogger
        changelog = ChangeLogger()
        changelog.log_moves(moved_files)
        logger.info("Change logs updated")

        # 8. Rogue File Detection
        logger.info("Step 8: Rogue file detection")
        from knowledge_map.scanner import RogueFileDetector
        detector = RogueFileDetector()
        rogue_files = detector.detect()
        logger.info(f"Found {len(rogue_files)} rogue files")

        # Summary
        duration = (datetime.now() - start_time).total_seconds()
        logger.info("=" * 60)
        logger.info(f"Daily job completed in {duration:.1f}s")
        logger.info(f"Processed: {len(new_files)} new, {len(modified_files)} modified")
        logger.info(f"OCR: {len(screenshots)} screenshots")
        logger.info(f"Organized: {len(moved_files)} files")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"Daily job failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    run_daily_jobs()
```

### Weekly Job Script

```python
#!/usr/bin/env python3
"""
Weekly Knowledge Graph Sync Job
Runs Sunday at 11:00 PM
"""

import logging
import sys
from datetime import datetime
from pathlib import Path

# Setup logging
log_file = Path.home() / "Library/Mobile Documents/.../iCloud_Knowledge_Map_Logs/jobs" / f"weekly_{datetime.now().strftime('%Y-%m-%d')}.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('weekly_job')

def run_weekly_jobs():
    """Execute all weekly jobs in sequence"""
    start_time = datetime.now()
    logger.info("=" * 60)
    logger.info("Starting weekly sync jobs")
    logger.info("=" * 60)

    try:
        # 1. Apple Notes Sync
        logger.info("Step 1: Apple Notes sync")
        from knowledge_map.integrations.apple_notes import AppleNotesSync
        notes_sync = AppleNotesSync()
        note_count = notes_sync.sync_all_notes()
        logger.info(f"Synced {note_count} notes")

        # 2. Calendar Sync
        logger.info("Step 2: Calendar sync")
        from knowledge_map.integrations.calendar import CalendarSync
        cal_sync = CalendarSync()
        event_count = cal_sync.sync_calendar()
        logger.info(f"Synced {event_count} calendar events")

        # 3. Photo Library Sync (Phase 2)
        logger.info("Step 3: Photo Library sync")
        from knowledge_map.integrations.photos import PhotoSync
        photo_sync = PhotoSync()
        photo_count = photo_sync.sync_photos()
        logger.info(f"Synced {photo_count} photos")

        # 4. Analytics Computation
        logger.info("Step 4: Analytics computation")
        from knowledge_map.analytics import AnalyticsEngine
        analytics = AnalyticsEngine()
        analytics.compute_all()
        logger.info("Analytics updated")

        # Summary
        duration = (datetime.now() - start_time).total_seconds()
        logger.info("=" * 60)
        logger.info(f"Weekly job completed in {duration:.1f}s")
        logger.info(f"Notes: {note_count}, Events: {event_count}, Photos: {photo_count}")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"Weekly job failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    run_weekly_jobs()
```

### Monthly Job Script

```python
#!/usr/bin/env python3
"""
Monthly Knowledge Graph Maintenance Job
Runs 1st of month at 3:00 AM
"""

import logging
import sys
from datetime import datetime
from pathlib import Path

# Setup logging
log_file = Path.home() / "Library/Mobile Documents/.../iCloud_Knowledge_Map_Logs/jobs" / f"monthly_{datetime.now().strftime('%Y-%m')}.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('monthly_job')

def run_monthly_jobs():
    """Execute all monthly maintenance jobs"""
    start_time = datetime.now()
    logger.info("=" * 60)
    logger.info("Starting monthly maintenance")
    logger.info("=" * 60)

    try:
        # 1. Archive Old Change Logs
        logger.info("Step 1: Archive old change logs")
        from knowledge_map.maintenance import LogArchiver
        archiver = LogArchiver()
        archived_count = archiver.archive_old_logs(days=30)
        logger.info(f"Archived {archived_count} log files")

        # 2. Monthly Insights Report
        logger.info("Step 2: Generate monthly insights report")
        from knowledge_map.reports import MonthlyReport
        report = MonthlyReport()
        report_path = report.generate()
        logger.info(f"Report saved to: {report_path}")

        # 3. Stale File Detection
        logger.info("Step 3: Detect stale files")
        from knowledge_map.maintenance import StaleFileDetector
        detector = StaleFileDetector()
        stale_files = detector.detect(months=6)
        logger.info(f"Found {len(stale_files)} stale files")

        # 4. Database Optimization
        logger.info("Step 4: Database optimization")
        from knowledge_map.database import DatabaseOptimizer
        optimizer = DatabaseOptimizer()
        optimizer.optimize()
        logger.info("Database optimized")

        # Summary
        duration = (datetime.now() - start_time).total_seconds()
        logger.info("=" * 60)
        logger.info(f"Monthly job completed in {duration:.1f}s")
        logger.info(f"Archived: {archived_count} logs")
        logger.info(f"Stale files: {len(stale_files)}")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"Monthly job failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    run_monthly_jobs()
```

---

## Status Monitoring

### Job Status Dashboard

**Web UI Display:**
- Last run time
- Next scheduled run
- Duration (last run)
- Status (success/failed/running)
- Error count (last 24 hours)

**Example API Endpoint:**
```python
@app.route('/api/jobs/status', methods=['GET'])
def job_status():
    return jsonify({
        'daily': {
            'last_run': '2025-10-09 02:00:00',
            'next_run': '2025-10-10 02:00:00',
            'duration': 247,  # seconds
            'status': 'success',
            'errors': 2
        },
        'weekly': {
            'last_run': '2025-10-06 23:00:00',
            'next_run': '2025-10-13 23:00:00',
            'duration': 342,
            'status': 'success',
            'errors': 0
        },
        'monthly': {
            'last_run': '2025-10-01 03:00:00',
            'next_run': '2025-11-01 03:00:00',
            'duration': 189,
            'status': 'success',
            'errors': 0
        }
    })
```

### Health Checks

**System Health Indicators:**
- Disk space available (warn if <10GB)
- Database size (warn if >1GB)
- Log directory size
- Last successful job run (warn if >48 hours)
- Error rate (warn if >5% failures)

---

**Status:** ✅ Complete
