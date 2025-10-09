#!/usr/bin/env python3
"""
Downloads Organizer Script
Run in Terminal: python3 /Users/jennifermckinney/Downloads/organize_downloads_final.py
"""

import os
import shutil
from pathlib import Path

downloads = Path("/Users/jennifermckinney/Downloads")
organized = downloads / "_ORGANIZED"

# Create all folders
folders = {
    'Resume_Career/Resumes': ['*jennifer*', '*mckinney*', '*resume*', '*cv*'],
    'Resume_Career/Cover_Letters': ['*cover*letter*', '*cl_*', '*_cl.*'],
    'Course_Materials/AI_Ethics': ['*ai*ethics*', 'aie_*', '*compliance*', '*ethical*'],
    'Course_Materials/Oxford_AI': ['oxf*ari*', 'oxford*'],
    'Course_Materials/Videos': ['*.mp4'],
    'Course_Materials/Transcripts': ['*transcript*'],
    'Projects/Deepfake_Research': ['*deepfake*'],
    'Projects/ValueCheck': ['*valuecheck*'],
    'Documents/Reports': ['*report*', '*beyond*illusions*', '*job*report*', '*cracks*surface*'],
    'Documents/Work_Documents': ['*misc*', '*mirakl*', '*pim*', '*product*', '*agenda*'],
    'Software_Installers': ['*.dmg', '*.pkg'],
    'Images_Media': ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.tif'],
    'Data_Files': ['*.xlsx', '*.csv', '*.json', '*.pbit'],
    'Presentations': ['*.pptx'],
    'Email_Exports': ['*.eml'],
    'Web_Downloads': ['*.html', '*.url'],
    'Archives_Zips': ['*.zip'],
    'Documents/Personal': ['*.rtf', '*.txt', '*.md'],
}

# Create folders
for folder in folders.keys():
    (organized / folder).mkdir(parents=True, exist_ok=True)
print("✓ Created folder structure")

# Move files
moved = 0
for file in downloads.iterdir():
    if file.name == '_ORGANIZED' or file.name.startswith('.') or 'organize' in file.name.lower():
        continue
    
    if file.is_file():
        moved_flag = False
        name_lower = file.name.lower()
        
        # Check each pattern
        for folder, patterns in folders.items():
            for pattern in patterns:
                pattern_lower = pattern.lower().replace('*', '')
                if pattern.startswith('*') and pattern.endswith('*'):
                    if pattern_lower[1:-1] in name_lower:
                        dest = organized / folder / file.name
                        shutil.move(str(file), str(dest))
                        print(f"→ {file.name} → {folder}")
                        moved += 1
                        moved_flag = True
                        break
                elif pattern.startswith('*'):
                    if name_lower.endswith(pattern_lower[1:]):
                        dest = organized / folder / file.name
                        shutil.move(str(file), str(dest))
                        print(f"→ {file.name} → {folder}")
                        moved += 1
                        moved_flag = True
                        break
                elif pattern.endswith('*'):
                    if name_lower.startswith(pattern_lower[:-1]):
                        dest = organized / folder / file.name
                        shutil.move(str(file), str(dest))
                        print(f"→ {file.name} → {folder}")
                        moved += 1
                        moved_flag = True
                        break
            if moved_flag:
                break
        
        # If not moved by pattern, move by extension
        if not moved_flag:
            ext = file.suffix.lower()
            if ext in ['.pdf']:
                dest = organized / 'Documents/Reports' / file.name
            elif ext in ['.docx', '.doc']:
                dest = organized / 'Documents/Work_Documents' / file.name
            else:
                dest = organized / 'Documents/Personal' / file.name
            
            shutil.move(str(file), str(dest))
            print(f"→ {file.name} → {dest.parent.name}")
            moved += 1
    
    elif file.is_dir():
        # Move directories to Archived_Projects
        if file.name not in ['_ORGANIZED']:
            dest = organized / 'Archived_Projects' / file.name
            dest.parent.mkdir(exist_ok=True)
            shutil.move(str(file), str(dest))
            print(f"→ {file.name} → Archived_Projects")
            moved += 1

print(f"\n✓ Organization complete! Moved {moved} items")
print(f"✓ Downloads folder now contains only _ORGANIZED and scripts")
