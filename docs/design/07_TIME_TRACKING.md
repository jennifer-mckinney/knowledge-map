# Time Tracking Design Document
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Draft

---

## Overview

Time tracking enables the system to correlate time investment with artifact creation, revealing productivity patterns, identifying high-effort/low-output areas, and surfacing opportunities to optimize focus. The system implements time tracking in two phases:

- **Phase 1 (MVP):** Basic time tracking (dates worked, work sessions, days worked)
- **Phase 2 (Enhanced):** Advanced time tracking (duration spent in documents, app-level monitoring)

---

## Phase 1: Basic Time Tracking

### What We Track

**File-Level Timestamps:**
- `date_created`: When file first appeared in system (REQUIRED for all nodes)
- `date_modified`: Last modification date (from filesystem metadata)
- `date_accessed`: Last accessed date (from filesystem metadata)
- `work_sessions`: Array of dates when file was actively worked on

**Data Structure:**
```javascript
{
  id: "file_123",
  date_created: "2025-09-15",
  date_modified: "2025-10-08",
  date_accessed: "2025-10-09",
  work_sessions: [
    { date: "2025-09-15", source: "created" },
    { date: "2025-09-20", source: "modified" },
    { date: "2025-10-08", source: "modified" }
  ],
  days_worked: 3,
  span_days: 24  // From creation to last modification
}
```

### Collection Methods

**1. Filesystem Metadata (Primary Method)**
- Read `kMDItemContentCreationDate`, `kMDItemContentModificationDate`, `kMDItemLastUsedDate`
- Available via macOS Spotlight metadata (mdls command)
- No additional instrumentation required
- Updated automatically by macOS

**2. Daily Scan Detection**
- Daily pipeline detects file changes
- Compare current modification date to stored value
- If different → add work session entry for that date
- Increments `days_worked` counter

**3. Change Log Integration**
- File moves logged with timestamp
- Provides activity history even when file metadata unchanged
- Shows when files were organized/reviewed

### Limitations (Phase 1)

- **No duration data**: Only knows files were worked on, not for how long
- **Coarse granularity**: Day-level only, not hour/minute
- **Access vs. Work**: File access doesn't guarantee meaningful work
- **External edits**: Files edited on other devices may have delayed sync

### Analytics Use Cases (Phase 1)

**1. Days Worked Analysis**
```
Query: Show all files with days_worked > 5
Insight: These are long-term projects requiring sustained attention
```

**2. Time Span Analysis**
```
Query: Show files with span_days > 30 and days_worked < 3
Insight: Long-running projects with minimal activity (abandoned?)
```

**3. Recent Activity**
```
Query: Show files with date_accessed in last 7 days
Insight: Current focus areas, active projects
```

**4. Creation vs. Modification Gap**
```
Query: Files created recently but not modified since
Insight: Potential drafts, abandoned ideas, or completed work
```

**5. Temporal Clustering**
```
Query: Group files by work_sessions dates
Insight: What was I working on during specific time periods?
```

---

## Phase 2: Advanced Time Tracking

### What We Track

**Duration Monitoring:**
- Time spent with file open/active
- Idle time vs. active editing time
- App-level focus tracking
- Cross-application work sessions (e.g., research → writing)

**Data Structure:**
```javascript
{
  id: "file_123",
  duration_tracking: {
    total_seconds: 14400,      // 4 hours total
    active_seconds: 10800,     // 3 hours active editing
    idle_seconds: 3600,        // 1 hour idle/open
    sessions: [
      {
        start: "2025-10-09T09:00:00Z",
        end: "2025-10-09T11:30:00Z",
        duration_seconds: 9000,
        active_seconds: 7200,
        app: "Pages",
        window_title: "AI Ethics Paper.pages"
      },
      {
        start: "2025-10-09T14:00:00Z",
        end: "2025-10-09T15:30:00Z",
        duration_seconds: 5400,
        active_seconds: 3600,
        app: "Pages",
        window_title: "AI Ethics Paper.pages"
      }
    ],
    first_tracked: "2025-09-15T08:30:00Z",
    last_tracked: "2025-10-09T15:30:00Z"
  }
}
```

### Collection Methods

**1. macOS Event Monitoring (Recommended Approach)**

**Option A: NSWorkspace API (Swift/Objective-C)**
- Monitor application activation events
- Track active window titles
- Detect file open/close events
- Low overhead, native integration

**Option B: Accessibility API**
- More detailed window focus tracking
- Requires accessibility permissions
- Can detect active document within apps

**Implementation:**
```python
# Python wrapper around Swift daemon
# Daemon runs in background, logs events to shared database

class TimeTrackingDaemon:
    def monitor_application_events(self):
        # NSWorkspace.shared.notificationCenter
        # Subscribe to: didActivateApplicationNotification
        # Subscribe to: didDeactivateApplicationNotification
        pass

    def monitor_file_events(self):
        # Track open files via lsof or fs_usage
        # Map file paths to applications
        pass

    def detect_idle_time(self):
        # CGEventSourceSecondsSinceLastEventType
        # If idle > 5 minutes, pause duration tracking
        pass
```

**2. Application Integration**

**Supported Apps (High Priority):**
- Pages/Word: Document editing
- Preview/PDF Expert: PDF reading
- VS Code: Code editing
- Safari/Chrome: Research (URL tracking)
- Notes.app: Note taking

**Integration Methods:**
- AppleScript automation for supported apps
- File handle monitoring (lsof)
- Window title tracking
- App-specific plugins (if available)

**3. Background Daemon Architecture**

**Daemon Process:**
```
knowledge_map_time_daemon
├── Runs as LaunchAgent (user-level)
├── Monitors application events
├── Writes to SQLite database
├── Low CPU/memory footprint (~5MB RAM)
└── Auto-restart on system reboot
```

**LaunchAgent Configuration:**
```xml
<!-- ~/Library/LaunchAgents/com.knowledge-map.time-tracker.plist -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.knowledge-map.time-tracker</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/time_tracking_daemon</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

**4. Idle Detection**

**Idle Threshold:** 5 minutes of no input
**Implementation:**
```python
import Quartz

def seconds_since_last_input():
    return Quartz.CGEventSourceSecondsSinceLastEventType(
        Quartz.kCGEventSourceStateHIDSystemState,
        Quartz.kCGAnyInputEventType
    )

# If idle > 300 seconds, pause active duration counting
```

### Privacy Considerations

**User Control:**
- Opt-in for duration tracking (disabled by default)
- Configure which apps to monitor
- Exclude specific files/folders
- Pause tracking on demand
- View all collected data
- Delete tracking history

**Data Storage:**
- All data stored locally (no cloud sync)
- Encrypted database option
- No screenshots or content capture
- Only metadata: app name, file path, duration

**Permissions Required:**
- Accessibility API access (System Preferences)
- Screen Recording permission (for window titles)
- Full Disk Access (for file monitoring)

### Analytics Use Cases (Phase 2)

**1. Time vs. Output Analysis**
```
Query: Files with duration_seconds > 3600 (1 hour+)
Compare: Output size/quality metrics
Insight: High time investment, low output → blockers/inefficiency
```

**2. Deep Work Sessions**
```
Query: Sessions with active_seconds > 1800 (30 min continuous)
Insight: Identify best times for focus work, flow states
```

**3. Context Switching**
```
Query: Count application switches per hour
Insight: High switching rate → distraction/multitasking issues
```

**4. Research vs. Writing Ratio**
```
Query: Time in Safari/Chrome vs. time in Pages/Word
Insight: Balance between research and creation
```

**5. Productivity Patterns**
```
Query: Average active_seconds by time of day
Insight: When are you most productive? Morning vs. afternoon?
```

**6. Project Time Investment**
```
Query: Sum duration_seconds for all files with tag [oxford]
Output: Total time invested in Oxford project
Insight: Correlate with grades, output quality
```

**7. Idle Time Analysis**
```
Query: Files with high idle_seconds ratio
Insight: Files left open but not actively worked → close unused files
```

---

**Status:** ✅ Complete
