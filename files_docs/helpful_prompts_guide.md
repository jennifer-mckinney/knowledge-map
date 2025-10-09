# Efficient Prompts for Working with Claude on File Organization

## Quick Context Setter
"My Documents folder is in iCloud at ~/Library/Mobile Documents/com~apple~CloudDocs/Documents. I don't use Desktop (it crashes). Downloads is local with _ORGANIZED structure."

## For File Operations
"Create a Python script using pathlib that I can run with python3 << 'EOF' syntax in Terminal. Target is iCloud Documents."

## For Troubleshooting
"Provide Terminal commands I can copy-paste directly. Use full paths, not shortcuts."

## For Documentation
"Create markdown files I can save to ClaudeOfficeSpace at [specific category]. Make them professional for leadership review."

## For Automation
"Update my existing automation using Python (not bash). Follow patterns from generic_downloads_organizer.py that worked."

## Project-Specific Prompts

### Knowledge Map Updates
"Update knowledge_map_generator.py to include Project_Workspaces. Use existing category patterns."

### File Sorting
"Create Python script to sort [location] files into Project_Workspaces categories. Test with 3 files first."

### Report Generation
"Generate report of Project_Workspaces contents with file counts per category."

## What NOT to Say
- "Save this to your Desktop" (Desktop crashes)
- "Your Documents folder" (it's in iCloud, not standard location)
- "Run this bash script" (Python works better)
- "Create a file" without specifying full path

## Helpful Context to Include
- "I have existing numbered folders (01_Career_Professional, etc.) in Documents"
- "My automation runs daily/weekly/monthly/quarterly"
- "Knowledge graph HTML files are in main Documents folder"
- "Downloads has Projects_By_Topic structure from previous organization"
