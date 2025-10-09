# Personal Knowledge Graph System

Transform scattered digital artifacts into an intelligent, connected knowledge graph.

[![Status](https://img.shields.io/badge/status-in%20development-yellow)]() [![Version](https://img.shields.io/badge/version-2.0-blue)]() [![License](https://img.shields.io/badge/license-MIT-green)]()

---

## What This Does

Automatically discovers, organizes, tags, and connects all your digital artifacts (files, notes, screenshots, calendar events, emails) to reveal patterns, identify knowledge gaps, and surface unrealized opportunities.

**Stop manually organizing. Start discovering insights.**

---

## Key Features

- **Intelligent Discovery** - Auto-scan iCloud, OneDrive, local storage, Apple Notes
- **Screenshot OCR** - Find any screenshot by content, not filename
- **Dynamic AI Tagging** - Claude API-powered, learns from corrections
- **Automated Organization** - Daily cleanup, change logs, tidy desktop
- **Knowledge Graph** - Interactive D3.js visualization with weighted relationships
- **Analytics & Insights** - Pattern detection, gap analysis, business opportunities
- **Email Integration** - Link emails to files, calendar, projects
- **Mobile App** - iOS companion for on-the-go access
- **Advanced Time Tracking** - Duration spent in documents

---

## Installation

```bash
git clone https://github.com/jennifer-mckinney/knowledge-map.git
cd knowledge-map
pip install -r requirements.txt
export CLAUDE_API_KEY="your-key"
python src/scan_files.py
```

---

## Documentation

Full design docs in `/docs/design/`:
- [01_PRODUCT_REQUIREMENTS.md](docs/design/01_PRODUCT_REQUIREMENTS.md) - Complete PRD
- More docs coming...

---

## Timeline

**2-Week Build:**
- **Week 1:** Core system (files, screenshots, tagging, graph, UI, basic analytics)
- **Week 2:** Advanced features (photos, email, mobile app, advanced analytics)

---

## Privacy

- Local-first processing
- Optional Claude API (can use local NLP)
- No telemetry, your data stays yours

---

## License

MIT License

---

**Jennifer McKinney** | [GitHub](https://github.com/jennifer-mckinney)

*Status: Active Development | Last Updated: 2025-10-09*
