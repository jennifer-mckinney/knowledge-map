# Downloads Organization Project Instructions

## Project Overview
Maintain organized Downloads folder with automated sorting into topic-based categories under `_ORGANIZED/Projects_By_Topic/`.

## Current Structure
```
Downloads/
├── _ORGANIZED/
│   ├── Projects_By_Topic/
│   │   ├── Oxford/Oxford_AI_Programme/
│   │   ├── AI_Ethics_Governance/Compliance_Course/
│   │   ├── Career_Development/Amazon_Prep/
│   │   ├── Company_Projects/Nordstrom/
│   │   ├── Research_Papers/Deepfake_Analysis/
│   │   ├── AI_Tools_Demos/Audit_ROI/
│   │   ├── AI_Projects/Agentic_AI_Suite/
│   │   ├── Data_Analysis/Labor_Market/
│   │   ├── Web_Development/Dashboards/
│   │   ├── Design_Assets/Exported_Graphics/
│   │   ├── Software/Applications/
│   │   └── Misc_Projects/Supply_Chain/
│   ├── Documents/
│   ├── Images_Media/
│   ├── Archives_Zips/
│   └── [other organized folders]
└── [new downloads]
```

## Maintenance Tasks

### Weekly (5 minutes)
- Move new downloads to appropriate topic folders
- Quick scan for misplaced files
- Delete obvious temp files

### Monthly (15 minutes)
- Review and consolidate duplicate files
- Archive completed projects
- Create new topic folders if needed
- Update this instruction file

### Quarterly (30 minutes)
- Deep organization review
- Archive old projects (>6 months inactive)
- Optimize folder structure
- Run duplicate detection

## Adding New Projects

### Create New Topic Category:
1. Assess if fits existing categories
2. Create folder: `Projects_By_Topic/[Category]/[Project_Name]/`
3. Move related files
4. Update this document

### File Naming Convention:
- Use descriptive names
- Avoid special characters
- Include dates for versions: `Project_v1_2025-09-10`
- Group related files in subfolders

## Automation Opportunities

### Daily Auto-Sort Script:
```python
# Sort by file type and common patterns
file_patterns = {
    'resume': 'Career_Development/',
    'oxford': 'Oxford/Oxford_AI_Programme/',
    'deepfake': 'Research_Papers/Deepfake_Analysis/',
    'nordstrom': 'Company_Projects/Nordstrom/'
}
```

### Archive Rules:
- Files >1 year old → Archive folder
- Completed projects → Project archive
- Temp files >30 days → Delete

## Topic Category Guidelines

### Oxford/Oxford_AI_Programme
- Course materials, assignments, transcripts
- Module downloads and submissions
- Study guides and certificates

### Career_Development/Amazon_Prep
- Resume versions and cover letters
- Interview prep materials
- Company research documents

### Research_Papers/Deepfake_Analysis
- Academic papers and analysis
- Data visualizations and dashboards
- Research methodologies

### AI_Projects/Agentic_AI_Suite
- AI tool demos and prototypes
- Project documentation
- Implementation files

### Company_Projects/[Company_Name]
- Client-specific work
- Project deliverables
- Company research

## Quality Standards
- No loose files in main Downloads
- Clear folder hierarchy (max 3 levels deep)
- Descriptive folder names
- Regular cleanup of duplicates
- Consistent naming conventions

## Emergency Recovery
- Backup organized structure monthly
- Keep reorganization scripts updated
- Document major changes
- Test scripts on small batches first

## Contact/Support
- Reference: Downloads_Organization_Retro.md
- Scripts: reorganize.py (tested working version)
- Automation: Reference existing automation setup
