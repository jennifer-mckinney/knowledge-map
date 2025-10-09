#!/bin/bash

# Reorganize Archived_Projects by topic
echo "🗂️  Reorganizing Archived_Projects by topic..."

BASE_DIR="/Users/jennifermckinney/Downloads/_ORGANIZED"
ARCHIVED_DIR="$BASE_DIR/Archived_Projects"
PROJECTS_DIR="$BASE_DIR/Projects_By_Topic"

# Create base Projects_By_Topic directory
mkdir -p "$PROJECTS_DIR"

# Oxford AI Programme
echo "📁 Creating Oxford/Oxford_AI_Programme"
mkdir -p "$PROJECTS_DIR/Oxford/Oxford_AI_Programme"
[ -d "$ARCHIVED_DIR/Oxford_AI_Programme_files_April2025 copy" ] && mv "$ARCHIVED_DIR/Oxford_AI_Programme_files_April2025 copy" "$PROJECTS_DIR/Oxford/Oxford_AI_Programme/"
[ -d "$ARCHIVED_DIR/Module 6 Downloads-20250531" ] && mv "$ARCHIVED_DIR/Module 6 Downloads-20250531" "$PROJECTS_DIR/Oxford/Oxford_AI_Programme/"
[ -d "$ARCHIVED_DIR/Course_Assignments" ] && mv "$ARCHIVED_DIR/Course_Assignments" "$PROJECTS_DIR/Oxford/Oxford_AI_Programme/"

# AI Ethics & Governance
echo "📁 Creating AI_Ethics_Governance/Compliance_Course"
mkdir -p "$PROJECTS_DIR/AI_Ethics_Governance/Compliance_Course"
[ -d "$ARCHIVED_DIR/AI-Ethics-Regulation-and-Compliance-June-2025-2025-Aug-01_21-34-01-450" ] && mv "$ARCHIVED_DIR/AI-Ethics-Regulation-and-Compliance-June-2025-2025-Aug-01_21-34-01-450" "$PROJECTS_DIR/AI_Ethics_Governance/Compliance_Course/"
[ -d "$ARCHIVED_DIR/AIGP" ] && mv "$ARCHIVED_DIR/AIGP" "$PROJECTS_DIR/AI_Ethics_Governance/Compliance_Course/"
[ -d "$ARCHIVED_DIR/module3-dashboard" ] && mv "$ARCHIVED_DIR/module3-dashboard" "$PROJECTS_DIR/AI_Ethics_Governance/Compliance_Course/"

# Career Development
echo "📁 Creating Career_Development/Amazon_Prep"
mkdir -p "$PROJECTS_DIR/Career_Development/Amazon_Prep"
[ -d "$ARCHIVED_DIR/amazon_prep" ] && mv "$ARCHIVED_DIR/amazon_prep" "$PROJECTS_DIR/Career_Development/Amazon_Prep/"
[ -d "$ARCHIVED_DIR/Principal_TPM_Amazon.rtf" ] && mv "$ARCHIVED_DIR/Principal_TPM_Amazon.rtf" "$PROJECTS_DIR/Career_Development/Amazon_Prep/"

# Nordstrom Projects
echo "📁 Creating Company_Projects/Nordstrom"
mkdir -p "$PROJECTS_DIR/Company_Projects/Nordstrom"
[ -d "$ARCHIVED_DIR/Nordstrom_Capstone" ] && mv "$ARCHIVED_DIR/Nordstrom_Capstone" "$PROJECTS_DIR/Company_Projects/Nordstrom/"
[ -d "$ARCHIVED_DIR/signature-you-nordstrom-demo" ] && mv "$ARCHIVED_DIR/signature-you-nordstrom-demo" "$PROJECTS_DIR/Company_Projects/Nordstrom/"

# Research & Papers
echo "📁 Creating Research_Papers/Deepfake_Analysis"
mkdir -p "$PROJECTS_DIR/Research_Papers/Deepfake_Analysis"
[ -d "$ARCHIVED_DIR/Deepfake_Research" ] && mv "$ARCHIVED_DIR/Deepfake_Research" "$PROJECTS_DIR/Research_Papers/Deepfake_Analysis/"
[ -d "$ARCHIVED_DIR/deepfake-dashboard" ] && mv "$ARCHIVED_DIR/deepfake-dashboard" "$PROJECTS_DIR/Research_Papers/Deepfake_Analysis/"

# AI Tools & Demos
echo "📁 Creating AI_Tools_Demos/Audit_ROI"
mkdir -p "$PROJECTS_DIR/AI_Tools_Demos/Audit_ROI"
[ -d "$ARCHIVED_DIR/ai_audit_demo" ] && mv "$ARCHIVED_DIR/ai_audit_demo" "$PROJECTS_DIR/AI_Tools_Demos/Audit_ROI/"
[ -d "$ARCHIVED_DIR/AI_ROI_Workflow_Outline" ] && mv "$ARCHIVED_DIR/AI_ROI_Workflow_Outline" "$PROJECTS_DIR/AI_Tools_Demos/Audit_ROI/"
[ -d "$ARCHIVED_DIR/terms-policy-reviewer.zip" ] && mv "$ARCHIVED_DIR/terms-policy-reviewer.zip" "$PROJECTS_DIR/AI_Tools_Demos/Audit_ROI/"

# Agentic AI Suite
echo "📁 Creating AI_Projects/Agentic_AI_Suite"
mkdir -p "$PROJECTS_DIR/AI_Projects/Agentic_AI_Suite"
[ -d "$ARCHIVED_DIR/Agentic_AI_Cast_Cards" ] && mv "$ARCHIVED_DIR/Agentic_AI_Cast_Cards" "$PROJECTS_DIR/AI_Projects/Agentic_AI_Suite/"
[ -f "$ARCHIVED_DIR/Agentic_AI_Cast_Cards.zip" ] && mv "$ARCHIVED_DIR/Agentic_AI_Cast_Cards.zip" "$PROJECTS_DIR/AI_Projects/Agentic_AI_Suite/"
[ -d "$ARCHIVED_DIR/Agentic_AI_Core_Team" ] && mv "$ARCHIVED_DIR/Agentic_AI_Core_Team" "$PROJECTS_DIR/AI_Projects/Agentic_AI_Suite/"
[ -d "$ARCHIVED_DIR/Agentic_AI_Final_Visuals_and_Cards 2" ] && mv "$ARCHIVED_DIR/Agentic_AI_Final_Visuals_and_Cards 2" "$PROJECTS_DIR/AI_Projects/Agentic_AI_Suite/"

# Data Analysis
echo "📁 Creating Data_Analysis/Labor_Market"
mkdir -p "$PROJECTS_DIR/Data_Analysis/Labor_Market"
[ -d "$ARCHIVED_DIR/feb2019_z5c6combined_csv" ] && mv "$ARCHIVED_DIR/feb2019_z5c6combined_csv" "$PROJECTS_DIR/Data_Analysis/Labor_Market/"
[ -d "$ARCHIVED_DIR/labor_chat history.rtf" ] && mv "$ARCHIVED_DIR/labor_chat history.rtf" "$PROJECTS_DIR/Data_Analysis/Labor_Market/"

# Web Development
echo "📁 Creating Web_Development/Dashboards"
mkdir -p "$PROJECTS_DIR/Web_Development/Dashboards"
[ -d "$ARCHIVED_DIR/HTML_Dashboards" ] && mv "$ARCHIVED_DIR/HTML_Dashboards" "$PROJECTS_DIR/Web_Development/Dashboards/"
[ -f "$ARCHIVED_DIR/jobs-report-interactive-landing.html" ] && mv "$ARCHIVED_DIR/jobs-report-interactive-landing.html" "$PROJECTS_DIR/Web_Development/Dashboards/"

# Design Assets
echo "📁 Creating Design_Assets/Exported_Graphics"
mkdir -p "$PROJECTS_DIR/Design_Assets/Exported_Graphics"
for item in "exported-assets" "exported-assets (1)" "exported-assets (2)" "exported-assets (2).zip" "exported-assets (2) 2" "exported-assets (3)" "exported-assets (3).zip" "exported-assets (4)" "exported-assets (4).zip"; do
    [ -e "$ARCHIVED_DIR/$item" ] && mv "$ARCHIVED_DIR/$item" "$PROJECTS_DIR/Design_Assets/Exported_Graphics/"
done

# Supply Chain
echo "📁 Creating Misc_Projects/Supply_Chain"
mkdir -p "$PROJECTS_DIR/Misc_Projects/Supply_Chain"
[ -d "$ARCHIVED_DIR/Supply Chain" ] && mv "$ARCHIVED_DIR/Supply Chain" "$PROJECTS_DIR/Misc_Projects/Supply_Chain/"

# Software
echo "📁 Creating Software/Applications"
mkdir -p "$PROJECTS_DIR/Software/Applications"
[ -d "$ARCHIVED_DIR/Install Pronto.app" ] && mv "$ARCHIVED_DIR/Install Pronto.app" "$PROJECTS_DIR/Software/Applications/"

echo ""
echo "🎉 Reorganization complete!"
echo "📊 New structure created in: $PROJECTS_DIR"

# Show remaining items
if [ "$(ls -A "$ARCHIVED_DIR" 2>/dev/null | grep -v '\.DS_Store' | wc -l)" -gt 0 ]; then
    echo ""
    echo "📋 Items remaining in Archived_Projects:"
    ls -la "$ARCHIVED_DIR" | grep -v '^\.' | grep -v '^total' | awk '{print "   • " $9}'
fi
