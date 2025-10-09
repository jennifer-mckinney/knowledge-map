#!/usr/bin/env python3
"""
Populate Project_Workspaces with initial content files
"""

from pathlib import Path
from datetime import datetime

base = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Documents"
workspace = base / "_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace"

# Technical_Designs content
(workspace / "Technical_Designs/Architecture_Diagrams" / "system_overview.md").write_text("""# System Architecture Overview
Created: """ + datetime.now().strftime('%Y-%m-%d') + """

## Components
- Frontend: React-based UI
- API Gateway: Request routing and authentication  
- Microservices: Domain-specific business logic
- Data Layer: PostgreSQL + MongoDB
- Cache: Redis

## Integration Points
- REST APIs with OAuth 2.0
- Webhook endpoints for real-time events
- Message queue with Kafka

## Deployment
- Kubernetes on AWS EKS
- Terraform infrastructure as code
""")

(workspace / "Technical_Designs/API_Specifications" / "api_design_template.md").write_text("""# API Specification Template

## Endpoint: /api/v1/resource

### GET /api/v1/resource
- Description: Retrieve resource list
- Authentication: Bearer token required
- Response: 200 OK with JSON array

### POST /api/v1/resource  
- Description: Create new resource
- Request Body: JSON object
- Response: 201 Created with resource ID

### Error Codes
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Internal Server Error
""")

# Project_Artifacts content
(workspace / "Project_Artifacts/Requirements_Documents" / "project_template.md").write_text("""# Project Requirements Template

## Executive Summary
Project objectives and key deliverables.

## Functional Requirements
- User authentication and authorization
- Data processing pipeline
- Real-time analytics dashboard
- API integration capabilities

## Non-Functional Requirements  
- 99.95% uptime SLA
- Sub-2 second response time
- Support 10x growth scaling
- GDPR/CCPA compliance

## Acceptance Criteria
- All functional tests pass
- Performance benchmarks met
- Security audit complete
""")

(workspace / "Project_Artifacts/Technical_Proposals" / "proposal_outline.md").write_text("""# Technical Proposal Outline

## Problem Statement
Current challenges and pain points.

## Proposed Solution
Technical approach and architecture.

## Implementation Plan
- Phase 1: Foundation (4 weeks)
- Phase 2: Core Features (8 weeks)  
- Phase 3: Integration (4 weeks)
- Phase 4: Testing & Launch (4 weeks)

## Resource Requirements
- Engineering: 4 developers, 1 architect
- Infrastructure: AWS services
- Timeline: 20 weeks total

## Success Metrics
- Performance improvements
- Cost reduction
- User satisfaction
""")

# Knowledge_Management content
(workspace / "Knowledge_Management/Best_Practices" / "coding_standards.md").write_text("""# Coding Standards & Best Practices

## Python
- Use type hints for function signatures
- Follow PEP 8 style guide
- Write docstrings for all public methods
- Use pathlib for file operations

## Git Workflow  
- Feature branches from main
- Descriptive commit messages
- PR reviews required before merge
- Squash commits on merge

## Documentation
- README in every repository
- Inline code comments for complex logic
- API documentation with examples
- Architecture decision records

## Testing
- Minimum 80% code coverage
- Unit tests for all functions
- Integration tests for APIs
- Performance benchmarks
""")

(workspace / "Knowledge_Management/Lessons_Learned" / "project_retrospective.md").write_text("""# Project Retrospective Template

## What Worked Well
- Python-based file operations reliable
- Clear directory structure aided organization
- Automation reduced manual effort

## What Didn't Work
- Bash scripts with special characters failed
- Relative paths caused confusion
- Desktop storage caused system crashes

## Key Learnings
- Always use absolute paths
- Test with 3 files first
- Provide copy-paste Terminal solutions
- Documents in iCloud, not local

## Action Items
- Document non-standard paths
- Create reusable script templates
- Build error handling into all operations
""")

# Active_Development content
(workspace / "Active_Development/Prototypes" / "automation_prototype.py").write_text("""#!/usr/bin/env python3
'''
File Organization Automation Prototype
'''

from pathlib import Path
import shutil
from datetime import datetime

class FileOrganizer:
    def __init__(self):
        self.home = Path.home()
        self.downloads = self.home / "Downloads"
        self.organized = self.downloads / "_ORGANIZED"
        
    def categorize_file(self, file_path):
        '''Categorize file based on extension and keywords'''
        ext = file_path.suffix.lower()
        name = file_path.stem.lower()
        
        if ext in ['.pdf', '.doc', '.docx']:
            if 'resume' in name or 'cv' in name:
                return 'Career_Development'
            elif 'requirement' in name:
                return 'Project_Artifacts'
            else:
                return 'Documents'
        elif ext in ['.py', '.js', '.html']:
            return 'Code_Samples'
        else:
            return 'Misc'
    
    def organize_downloads(self):
        '''Sort downloads into organized folders'''
        for file in self.downloads.iterdir():
            if file.is_file():
                category = self.categorize_file(file)
                dest = self.organized / category
                dest.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file), str(dest / file.name))
                print(f"Moved {file.name} to {category}")

if __name__ == "__main__":
    organizer = FileOrganizer()
    # organizer.organize_downloads()  # Uncomment to run
    print("Prototype ready for testing")
""")

(workspace / "Active_Development/Code_Samples" / "terminal_snippets.sh").write_text("""# Useful Terminal Commands

# Navigate to workspace
cd ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace/

# Find all markdown files
find . -name "*.md" -type f

# Count files in each directory
for dir in */; do echo "$dir: $(find "$dir" -type f | wc -l) files"; done

# Create timestamped backup
tar -czf "backup_$(date +%Y%m%d).tar.gz" .

# Search for keyword in all files
grep -r "keyword" .

# List files modified today
find . -type f -mtime -1 -ls
""")

# Create workspace index
(workspace / "INDEX.md").write_text("""# ClaudeOfficeSpace Index

## Quick Navigation

### Technical_Designs/
- [System Architecture Overview](Technical_Designs/Architecture_Diagrams/system_overview.md)
- [API Design Template](Technical_Designs/API_Specifications/api_design_template.md)

### Project_Artifacts/
- [Project Requirements Template](Project_Artifacts/Requirements_Documents/project_template.md)
- [Technical Proposal Outline](Project_Artifacts/Technical_Proposals/proposal_outline.md)

### Knowledge_Management/
- [Coding Standards](Knowledge_Management/Best_Practices/coding_standards.md)
- [Project Retrospective](Knowledge_Management/Lessons_Learned/project_retrospective.md)

### Active_Development/
- [Automation Prototype](Active_Development/Prototypes/automation_prototype.py)
- [Terminal Snippets](Active_Development/Code_Samples/terminal_snippets.sh)

---
Updated: """ + datetime.now().strftime('%Y-%m-%d %H:%M') + """
Total Files: 9
""")

print("✅ Created 9 content files in Project_Workspaces")
print("\nFiles created:")
print("  Technical_Designs: 2 files")
print("  Project_Artifacts: 2 files")  
print("  Knowledge_Management: 2 files")
print("  Active_Development: 2 files")
print("  Root: 1 index file")
print("\n📍 Location: ~/Library/Mobile Documents/com~apple~CloudDocs/Documents/_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace/")
