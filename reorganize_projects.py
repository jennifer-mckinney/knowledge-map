#!/usr/bin/env python3
"""
Reorganize Archived_Projects folder by topic/theme
Groups related projects into logical folder structures
"""

import os
import shutil
from pathlib import Path

# Base paths
downloads_path = Path("/Users/jennifermckinney/Downloads")
organized_path = downloads_path / "_ORGANIZED"
archived_path = organized_path / "Archived_Projects"
new_base = organized_path / "Projects_By_Topic"

# Create new base directory
new_base.mkdir(exist_ok=True)

# Define reorganization mapping
reorganization_map = {
    # Oxford AI Programme
    "Oxford/Oxford_AI_Programme": [
        "Oxford_AI_Programme_files_April2025 copy",
        "Module 6 Downloads-20250531",
        "Course_Assignments"
    ],
    
    # AI Ethics & Governance
    "AI_Ethics_Governance/Compliance_Course": [
        "AI-Ethics-Regulation-and-Compliance-June-2025-2025-Aug-01_21-34-01-450",
        "AIGP",
        "module3-dashboard"
    ],
    
    # Career Development
    "Career_Development/Amazon_Prep": [
        "amazon_prep",
        "Principal_TPM_Amazon.rtf"
    ],
    
    # Nordstrom Projects
    "Company_Projects/Nordstrom": [
        "Nordstrom_Capstone",
        "signature-you-nordstrom-demo"
    ],
    
    # Research & Papers
    "Research_Papers/Deepfake_Analysis": [
        "Deepfake_Research",
        "deepfake-dashboard"
    ],
    
    # AI Tools & Demos
    "AI_Tools_Demos/Audit_ROI": [
        "ai_audit_demo",
        "AI_ROI_Workflow_Outline",
        "terms-policy-reviewer.zip"
    ],
    
    # Agentic AI Project Suite
    "AI_Projects/Agentic_AI_Suite": [
        "Agentic_AI_Cast_Cards",
        "Agentic_AI_Cast_Cards.zip",
        "Agentic_AI_Core_Team",
        "Agentic_AI_Final_Visuals_and_Cards 2"
    ],
    
    # Data Analysis
    "Data_Analysis/Labor_Market": [
        "feb2019_z5c6combined_csv",
        "labor_chat history.rtf"
    ],
    
    # Web Development
    "Web_Development/Dashboards": [
        "HTML_Dashboards",
        "jobs-report-interactive-landing.html"
    ],
    
    # Design Assets
    "Design_Assets/Exported_Graphics": [
        "exported-assets",
        "exported-assets (1)",
        "exported-assets (2)",
        "exported-assets (2).zip",
        "exported-assets (2) 2", 
        "exported-assets (3)",
        "exported-assets (3).zip",
        "exported-assets (4)",
        "exported-assets (4).zip"
    ],
    
    # Miscellaneous Projects
    "Misc_Projects/Supply_Chain": [
        "Supply Chain"
    ],
    
    # Software/Apps
    "Software/Applications": [
        "Install Pronto.app"
    ]
}

def move_items():
    """Move items from Archived_Projects to new topic-based structure"""
    
    print("🗂️  Reorganizing Archived_Projects by topic...")
    
    moved_count = 0
    
    for topic_path, items in reorganization_map.items():
        # Create topic directory
        topic_dir = new_base / topic_path
        topic_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n📁 Creating: {topic_path}")
        
        for item in items:
            source_path = archived_path / item
            dest_path = topic_dir / item
            
            if source_path.exists():
                try:
                    if source_path.is_dir():
                        shutil.move(str(source_path), str(dest_path))
                        print(f"   ✅ Moved folder: {item}")
                    else:
                        shutil.move(str(source_path), str(dest_path))
                        print(f"   ✅ Moved file: {item}")
                    moved_count += 1
                except Exception as e:
                    print(f"   ❌ Error moving {item}: {e}")
            else:
                print(f"   ⚠️  Not found: {item}")
    
    print(f"\n🎉 Reorganization complete! Moved {moved_count} items.")
    
    # Check for any remaining items
    remaining = list(archived_path.iterdir())
    remaining = [item for item in remaining if item.name not in ['.DS_Store']]
    
    if remaining:
        print(f"\n📋 Items remaining in Archived_Projects:")
        for item in remaining:
            print(f"   • {item.name}")
        print("\nThese items may need manual review or categorization.")

def print_new_structure():
    """Print the new organized structure"""
    print("\n📊 New Project Structure:")
    print("=" * 50)
    
    for topic_path in reorganization_map.keys():
        full_path = new_base / topic_path
        if full_path.exists():
            items = list(full_path.iterdir())
            items = [item for item in items if item.name != '.DS_Store']
            print(f"\n{topic_path}/ ({len(items)} items)")
            for item in items[:3]:  # Show first 3 items
                print(f"   • {item.name}")
            if len(items) > 3:
                print(f"   • ... and {len(items) - 3} more")

if __name__ == "__main__":
    # Check if source directory exists
    if not archived_path.exists():
        print(f"❌ Error: {archived_path} does not exist")
        exit(1)
    
    # Perform reorganization
    move_items()
    
    # Show new structure
    print_new_structure()
    
    print(f"\n🎯 All projects organized by topic in:")
    print(f"   {new_base}")
