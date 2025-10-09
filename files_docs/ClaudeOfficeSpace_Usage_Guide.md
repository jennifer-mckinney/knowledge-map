# ClaudeOfficeSpace Usage Guide

## Your Workspace is Ready

Location: `~/Library/Mobile Documents/com~apple~CloudDocs/Documents/_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace`

## How to Use Each Folder

### Technical_Designs/
- **Architecture_Diagrams**: Save .drawio, .svg, .png architecture files
- **System_Documentation**: System design docs, technical specs
- **API_Specifications**: OpenAPI specs, API documentation
- **Implementation_Guides**: Step-by-step implementation docs

### Project_Artifacts/
- **Requirements_Documents**: PRDs, BRDs, requirements specs
- **Design_Reviews**: Review meeting notes, feedback docs
- **Technical_Proposals**: RFPs, technical proposals
- **Solution_Blueprints**: Solution architecture documents

### Knowledge_Management/
- **Best_Practices**: Proven methodologies, standards docs
- **Lessons_Learned**: Retrospectives, post-mortems
- **Reference_Materials**: Quick reference guides, cheat sheets
- **Process_Documentation**: Workflow docs, procedures

### Active_Development/
- **Current_Projects**: Active work files
- **Prototypes**: POCs, experimental code
- **Code_Samples**: Reusable code snippets
- **Testing_Documentation**: Test plans, test results

## Quick Actions

### Add a file via Terminal:
```bash
cp ~/Downloads/myfile.pdf ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace/Technical_Designs/
```

### Add a file via Finder:
1. Open Finder
2. Click iCloud Drive → Documents → _AUTOMATION → knowledge_map → Project_Workspaces → ClaudeOfficeSpace
3. Drag files to appropriate category folder

### Create a new document directly:
```bash
echo "# Project Name" > ~/Library/Mobile\ Documents/com~apple~CloudDocs/Documents/_AUTOMATION/knowledge_map/Project_Workspaces/ClaudeOfficeSpace/Active_Development/Current_Projects/new_project.md
```

## File Naming Conventions

- Use underscores for spaces: `project_requirements_v1.pdf`
- Include dates: `design_review_20250115.md`
- Version numbers: `api_spec_v2.yaml`
- Status prefixes: `DRAFT_proposal.docx`, `FINAL_architecture.pdf`

## Integration with Your Existing Files

Your knowledge graph HTML files and numbered folders (01_Career_Professional, etc.) remain in the main Documents folder. ClaudeOfficeSpace provides dedicated workspace for active technical work that can reference or link to these existing resources.

## Next Steps

1. Move any current technical documentation into appropriate folders
2. Set up your preferred editor to save directly to these locations
3. Create README files in each category for your specific use cases

The workspace syncs automatically via iCloud to all your devices.
