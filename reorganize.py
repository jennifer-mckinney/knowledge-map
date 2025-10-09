#!/usr/bin/env python3
import os
import shutil

base_dir = "/Users/jennifermckinney/Downloads/_ORGANIZED"
archived_dir = f"{base_dir}/Archived_Projects"
projects_dir = f"{base_dir}/Projects_By_Topic"

# Create topic structure
topics = [
    "Oxford/Oxford_AI_Programme",
    "AI_Ethics_Governance/Compliance_Course",
    "Career_Development/Amazon_Prep", 
    "Company_Projects/Nordstrom",
    "Research_Papers/Deepfake_Analysis",
    "AI_Tools_Demos/Audit_ROI",
    "AI_Projects/Agentic_AI_Suite",
    "Data_Analysis/Labor_Market",
    "Web_Development/Dashboards",
    "Design_Assets/Exported_Graphics",
    "Software/Applications",
    "Misc_Projects/Supply_Chain"
]

for topic in topics:
    os.makedirs(f"{projects_dir}/{topic}", exist_ok=True)

# Move files by category
moves = {
    "Oxford/Oxford_AI_Programme": [
        "Oxford_AI_Programme_files_April2025 copy",
        "Module 6 Downloads-20250531", 
        "Course_Assignments"
    ],
    "AI_Ethics_Governance/Compliance_Course": [
        "AI-Ethics-Regulation-and-Compliance-June-2025-2025-Aug-01_21-34-01-450",
        "AIGP",
        "module3-dashboard"
    ],
    "Career_Development/Amazon_Prep": [
        "amazon_prep",
        "Principal_TPM_Amazon.rtf"
    ],
    "Company_Projects/Nordstrom": [
        "Nordstrom_Capstone", 
        "signature-you-nordstrom-demo"
    ],
    "Research_Papers/Deepfake_Analysis": [
        "Deepfake_Research",
        "deepfake-dashboard"
    ],
    "AI_Tools_Demos/Audit_ROI": [
        "ai_audit_demo",
        "AI_ROI_Workflow_Outline",
        "terms-policy-reviewer.zip"
    ],
    "AI_Projects/Agentic_AI_Suite": [
        "Agentic_AI_Cast_Cards",
        "Agentic_AI_Cast_Cards.zip",
        "Agentic_AI_Core_Team",
        "Agentic_AI_Final_Visuals_and_Cards 2"
    ],
    "Data_Analysis/Labor_Market": [
        "feb2019_z5c6combined_csv",
        "labor_chat history.rtf"
    ],
    "Web_Development/Dashboards": [
        "HTML_Dashboards",
        "jobs-report-interactive-landing.html"
    ],
    "Software/Applications": [
        "Install Pronto.app"
    ],
    "Misc_Projects/Supply_Chain": [
        "Supply Chain"
    ]
}

# Move exported-assets to Design_Assets
for item in os.listdir(archived_dir):
    if item.startswith("exported-assets"):
        try:
            shutil.move(f"{archived_dir}/{item}", f"{projects_dir}/Design_Assets/Exported_Graphics/")
            print(f"✅ Moved {item}")
        except:
            pass

# Move other items
for topic, items in moves.items():
    for item in items:
        src = f"{archived_dir}/{item}"
        dest = f"{projects_dir}/{topic}/{item}"
        if os.path.exists(src):
            try:
                shutil.move(src, dest)
                print(f"✅ Moved {item} to {topic}")
            except Exception as e:
                print(f"❌ Error moving {item}: {e}")

print("🎉 Reorganization complete!")
