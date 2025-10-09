#!/usr/bin/env python3
"""
Project Workspaces Deployment for Mac
Direct deployment script for Jennifer McKinney's system
Creates the complete workspace structure at the correct location
"""

import os
import json
from pathlib import Path
from datetime import datetime

def deploy_project_workspaces():
    """Deploy the complete Project Workspaces structure on Mac system"""

    # BUG FIX: Use Path.home() for portability instead of hardcoded username
    # This allows the script to work on any user's system, not just one specific user
    home = Path.home()

    # Build paths relative to user's home directory
    # Using "Documents" here (not iCloud path) for local deployment
    automation_dir = home / "Documents" / "_AUTOMATION"
    knowledge_map_dir = automation_dir / "knowledge_map"
    project_workspaces_dir = knowledge_map_dir / "Project_Workspaces"
    
    print("🚀 Project Workspaces Deployment for Mac System")
    print("=" * 50)
    print(f"Target location: {project_workspaces_dir}")
    print()
    
    # Create the directory structure
    print("📁 Creating directory structure...")
    
    # Create main directories
    directories_to_create = [
        knowledge_map_dir,
        project_workspaces_dir,
        project_workspaces_dir / "ClaudeOfficeSpace",
        project_workspaces_dir / "Oxford_AI_Integration",
        project_workspaces_dir / "Career_Portfolio_Development",
        project_workspaces_dir / "Research_Documentation",
        
        # ClaudeOfficeSpace subdirectories
        project_workspaces_dir / "ClaudeOfficeSpace" / "Technical_Designs",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Technical_Designs" / "Architecture_Diagrams",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Technical_Designs" / "System_Documentation",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Technical_Designs" / "API_Specifications",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Technical_Designs" / "Implementation_Guides",
        
        project_workspaces_dir / "ClaudeOfficeSpace" / "Project_Artifacts",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Project_Artifacts" / "Requirements_Documents",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Project_Artifacts" / "Design_Reviews",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Project_Artifacts" / "Technical_Proposals",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Project_Artifacts" / "Solution_Blueprints",
        
        project_workspaces_dir / "ClaudeOfficeSpace" / "Knowledge_Management",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Knowledge_Management" / "Best_Practices",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Knowledge_Management" / "Lessons_Learned",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Knowledge_Management" / "Reference_Materials",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Knowledge_Management" / "Process_Documentation",
        
        project_workspaces_dir / "ClaudeOfficeSpace" / "Active_Development",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Active_Development" / "Current_Projects",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Active_Development" / "Prototypes",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Active_Development" / "Code_Samples",
        project_workspaces_dir / "ClaudeOfficeSpace" / "Active_Development" / "Testing_Documentation",
        
        # Data and reports directories
        knowledge_map_dir / "data",
        knowledge_map_dir / "reports",
    ]
    
    for directory in directories_to_create:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {directory.relative_to(automation_dir)}")
    
    # Create README files
    print("\n📝 Creating documentation files...")
    
    # Main Project Workspaces README
    main_readme = project_workspaces_dir / "README.md"
    main_readme_content = """# Project Workspaces

This directory contains organized workspaces for various technical projects and initiatives.

## Active Workspaces

### ClaudeOfficeSpace
Technical design artifacts and project documentation workspace.
- **Technical_Designs**: Architecture diagrams, system documentation, API specs
- **Project_Artifacts**: Requirements, reviews, proposals, blueprints
- **Knowledge_Management**: Best practices, lessons learned, references
- **Active_Development**: Current projects, prototypes, code samples

### Future Workspaces
- **Oxford_AI_Integration**: Integration with Oxford AI Programme materials
- **Career_Portfolio_Development**: Career development documentation
- **Research_Documentation**: Research project documentation

## Integration

This workspace structure is fully integrated with:
- Knowledge Map visualization system
- Daily automation scripts
- Control Center management
- Quarterly maintenance routines

## Usage

1. Place files in appropriate category folders
2. Run knowledge map generation to update visualization
3. Access through Control Center for management options
4. Review quarterly reports for workspace analytics

Created: """ + datetime.now().strftime('%Y-%m-%d')
    
    main_readme.write_text(main_readme_content)
    print("✅ Created Project_Workspaces/README.md")
    
    # ClaudeOfficeSpace README
    claude_readme = project_workspaces_dir / "ClaudeOfficeSpace" / "README.md"
    claude_readme_content = """# ClaudeOfficeSpace

Technical design and project documentation workspace.

## Directory Structure

```
ClaudeOfficeSpace/
├── Technical_Designs/
│   ├── Architecture_Diagrams/     # System architecture visualizations
│   ├── System_Documentation/      # Technical system docs
│   ├── API_Specifications/        # API documentation
│   └── Implementation_Guides/     # Step-by-step implementation docs
├── Project_Artifacts/
│   ├── Requirements_Documents/    # Project requirements
│   ├── Design_Reviews/           # Design review materials
│   ├── Technical_Proposals/      # Technical proposals
│   └── Solution_Blueprints/      # Solution architecture blueprints
├── Knowledge_Management/
│   ├── Best_Practices/           # Documented best practices
│   ├── Lessons_Learned/          # Project retrospectives
│   ├── Reference_Materials/      # Reference documentation
│   └── Process_Documentation/    # Process and workflow docs
└── Active_Development/
    ├── Current_Projects/          # Active project files
    ├── Prototypes/               # Proof of concepts
    ├── Code_Samples/             # Example code
    └── Testing_Documentation/    # Test plans and results
```

## File Naming Convention

- Use descriptive names with underscores
- Include dates for versioning: `design_review_20250911.md`
- Prefix drafts with 'DRAFT_'

Created: """ + datetime.now().strftime('%Y-%m-%d')
    
    claude_readme.write_text(claude_readme_content)
    print("✅ Created ClaudeOfficeSpace/README.md")
    
    # Create placeholder READMEs for future workspaces
    for workspace in ["Oxford_AI_Integration", "Career_Portfolio_Development", "Research_Documentation"]:
        workspace_readme = project_workspaces_dir / workspace / "README.md"
        content = f"# {workspace.replace('_', ' ')}\n\nThis workspace is reserved for future development.\n\nCreated: {datetime.now().strftime('%Y-%m-%d')}"
        workspace_readme.write_text(content)
        print(f"✅ Created {workspace}/README.md")
    
    # Create a sample welcome file
    welcome_file = project_workspaces_dir / "ClaudeOfficeSpace" / "Knowledge_Management" / "Reference_Materials" / "welcome.md"
    welcome_content = """# Welcome to ClaudeOfficeSpace

This workspace is your centralized hub for technical documentation and project artifacts. The structure has been designed to support your workflow while maintaining consistency with your existing automation systems.

## Quick Start

1. **Technical Designs**: Place architecture diagrams and system documentation here
2. **Project Artifacts**: Store requirements, proposals, and project documentation
3. **Knowledge Management**: Capture best practices and lessons learned
4. **Active Development**: Keep current work and prototypes

## Automation Features

- Files are automatically categorized based on keywords
- Daily automation maintains organization
- Monthly reports track workspace growth
- Quarterly maintenance archives old projects

Created: """ + datetime.now().strftime('%Y-%m-%d')
    
    welcome_file.write_text(welcome_content)
    print("✅ Created welcome documentation")
    
    # Summary
    print("\n" + "=" * 50)
    print("🎉 DEPLOYMENT COMPLETE!")
    print("=" * 50)
    print(f"\n📍 Location: {project_workspaces_dir}")
    print("\n🎯 Next Steps:")
    print("   1. Navigate to the ClaudeOfficeSpace directory")
    print("   2. Start adding your technical documentation")
    print("   3. Run your knowledge map generator to visualize")
    print("\n✨ Your Project Workspaces are ready for use!")

if __name__ == "__main__":
    try:
        deploy_project_workspaces()
    except Exception as e:
        print(f"\n❌ Error during deployment: {e}")
        print("Please ensure you have write permissions to your Documents folder")
