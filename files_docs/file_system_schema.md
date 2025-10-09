# Jennifer McKinney's File System Schema

## Path Mappings

| Standard Mac Path | Your Actual Path | Storage Type |
|------------------|------------------|--------------|
| ~/Documents | ~/Library/Mobile Documents/com~apple~CloudDocs/Documents | iCloud |
| ~/Desktop | Not used (avoid - crashes) | N/A |
| ~/Downloads | ~/Downloads (local) | Local |
| ~/Downloads/_ORGANIZED | ~/Downloads/_ORGANIZED/Projects_By_Topic | Local |

## Key Directories

```
Your System:
├── ~/Library/Mobile Documents/com~apple~CloudDocs/Documents/ (iCloud)
│   ├── _AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace/
│   ├── 01_Career_Professional/
│   ├── 02_Education_Coursework/
│   ├── 03_AI_Research/
│   ├── 04_Reports_Analysis/
│   ├── 05_Technical_Development/
│   ├── 06_Administrative/
│   └── knowledge_graph_*.html files
├── ~/Downloads/_ORGANIZED/Projects_By_Topic/ (Local)
│   ├── Oxford/Oxford_AI_Programme/
│   ├── Career_Development/Amazon_Prep/
│   └── Research_Papers/Deepfake_Analysis/
└── ~/OneDrive/ (Cloud - visible but not primary)

## Quick Reference
- Documents = iCloud, NOT local
- Desktop = DO NOT USE (causes crashes)
- Downloads = Local, with _ORGANIZED structure
- Primary work = iCloud Documents for sync across devices
```
