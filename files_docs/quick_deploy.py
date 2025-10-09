#!/usr/bin/env python3

import os
from pathlib import Path

# Your iCloud Documents path
base = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents"
workspace = base / "_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace"

# Create all directories
dirs = [
    workspace / "Technical_Designs/Architecture_Diagrams",
    workspace / "Technical_Designs/System_Documentation", 
    workspace / "Technical_Designs/API_Specifications",
    workspace / "Technical_Designs/Implementation_Guides",
    workspace / "Project_Artifacts/Requirements_Documents",
    workspace / "Project_Artifacts/Design_Reviews",
    workspace / "Project_Artifacts/Technical_Proposals",
    workspace / "Project_Artifacts/Solution_Blueprints",
    workspace / "Knowledge_Management/Best_Practices",
    workspace / "Knowledge_Management/Lessons_Learned",
    workspace / "Knowledge_Management/Reference_Materials",
    workspace / "Knowledge_Management/Process_Documentation",
    workspace / "Active_Development/Current_Projects",
    workspace / "Active_Development/Prototypes",
    workspace / "Active_Development/Code_Samples",
    workspace / "Active_Development/Testing_Documentation"
]

for d in dirs:
    d.mkdir(parents=True, exist_ok=True)
    print(f"✓ {d.name}")

print(f"\n✅ Created in: {base}/_AUTOMATION/knowledge_map/Project_Workspaces")
print("Open Finder → iCloud Drive → Documents → Look for _AUTOMATION folder")
