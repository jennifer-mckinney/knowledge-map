# Documents Organizer - User Instructions

## What This Does
Automatically organizes your Documents folder by content type and keywords into meaningful categories.

## Categories Created
- Financial/Tax_Documents (receipts, taxes, invoices)
- Financial/Banking (bank statements, loans)
- Medical/Health (doctor visits, prescriptions, insurance)
- Work/Career (resumes, job applications)
- Legal/Important (contracts, deeds, insurance)
- Education/Learning (courses, certificates)
- Personal/Family (family docs, photos)
- Projects/Creative (design work, writing)
- Reference/Manuals (guides, instructions)
- Archives/Old (files >2 years old)
- To_Review (unrecognized files)

## How to Use

### Step 1: Save Script
Save `generic_documents_organizer.py` to your Documents folder

### Step 2: Run
**On Mac/Linux:**
```bash
python3 generic_documents_organizer.py
```

**On Windows:**
```cmd
python generic_documents_organizer.py
```

### Step 3: Review Results
- Check `_ORGANIZED` folder in Documents
- Review files in `To_Review` folder manually
- Read generated report

## How It Categorizes
Files are sorted by keywords in the filename:
- "tax", "receipt", "invoice" → Financial/Tax_Documents
- "resume", "job", "work" → Work/Career
- "medical", "doctor", "health" → Medical/Health
- Files older than 2 years → Archives/Old

## Safety Features
- Tests with 3 files first
- Never deletes files
- Counts files before/after
- Creates detailed report
- Stops if errors occur

## After Running
Your Documents folder will have an `_ORGANIZED` folder with categorized documents, plus a report showing what was moved where.

## Customization
Edit the `categories` section to add your own keywords or folder names.
