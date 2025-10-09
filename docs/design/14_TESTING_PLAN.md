# Testing Plan & Quality Assurance Strategy
**Project:** knowledge_map v2.0 - Personal Knowledge Graph System
**Date:** 2025-10-09
**Status:** Final
**Version:** 1.0

---

## Executive Summary

This document defines the comprehensive testing strategy for the knowledge_map v2.0 system. It answers the critical question: **"How are you gonna check yourself?"** with a multi-layered approach that includes unit testing, integration testing, end-to-end testing, performance testing, and continuous self-checking mechanisms throughout implementation.

**Key Testing Principles:**
1. **Test-First Development** - Write tests before implementation where practical
2. **Continuous Validation** - Self-check at every implementation milestone
3. **Automated Coverage** - 80%+ code coverage target
4. **Real-World Testing** - Use actual user files, not just synthetic data
5. **Performance Benchmarks** - Measure against defined targets
6. **Error Resilience** - Test failure modes, not just happy paths

---

## Table of Contents

1. [Testing Strategy Overview](#1-testing-strategy-overview)
2. [Self-Checking Strategy (CRITICAL)](#2-self-checking-strategy-critical)
3. [Test Execution Plan](#3-test-execution-plan)
4. [Unit Testing](#4-unit-testing)
5. [Integration Testing](#5-integration-testing)
6. [End-to-End Testing](#6-end-to-end-testing)
7. [Performance Testing](#7-performance-testing)
8. [Component-Specific Test Cases](#8-component-specific-test-cases)
9. [Testing Tools & Frameworks](#9-testing-tools--frameworks)
10. [Success Criteria & Benchmarks](#10-success-criteria--benchmarks)
11. [Test Data Management](#11-test-data-management)
12. [Continuous Integration](#12-continuous-integration)

---

## 1. Testing Strategy Overview

### 1.1 Testing Pyramid

```
                    ┌─────────────────────┐
                    │   E2E Tests (5%)    │  Real user workflows
                    │   ~20 tests         │  Full system integration
                    └─────────────────────┘
                  ┌───────────────────────────┐
                  │  Integration Tests (15%)  │  Component interaction
                  │  ~60 tests                │  API, Database, Jobs
                  └───────────────────────────┘
              ┌─────────────────────────────────────┐
              │     Unit Tests (80%)                │  Individual functions
              │     ~320 tests                      │  Fast, isolated
              └─────────────────────────────────────┘
```

**Rationale:**
- **80% Unit Tests**: Fast execution, catch bugs early, easy to maintain
- **15% Integration Tests**: Verify components work together correctly
- **5% E2E Tests**: Validate critical user workflows, catch system-level issues

### 1.2 Testing Levels

**Level 1: Unit Testing**
- Test individual functions and methods in isolation
- Mock external dependencies (database, APIs, file system)
- Run in milliseconds
- Target: 80% code coverage

**Level 2: Integration Testing**
- Test component interactions (scanner + database, tagger + Claude API)
- Use test database and temporary file system
- Run in seconds
- Target: All critical integration points covered

**Level 3: System Testing**
- Test complete workflows (daily job, file organization flow)
- Use isolated test environment
- Run in minutes
- Target: All major features validated

**Level 4: Performance Testing**
- Test scalability, speed, resource usage
- Use realistic data volumes (10k+ files)
- Run in minutes to hours
- Target: Meet defined performance benchmarks

**Level 5: Acceptance Testing**
- Test real-world user scenarios
- Use actual user data (with permission)
- Manual validation
- Target: 100% of user stories verified

### 1.3 Test Automation Levels

| Test Type | Automation Level | Frequency |
|-----------|------------------|-----------|
| Unit Tests | 100% automated | Every commit |
| Integration Tests | 100% automated | Every push |
| E2E Tests | 90% automated | Daily |
| Performance Tests | 100% automated | Weekly |
| Acceptance Tests | 50% automated | Per milestone |

---

## 2. Self-Checking Strategy (CRITICAL)

**This section answers: "How are you gonna check yourself during implementation?"**

### 2.1 Implementation Validation Checkpoints

**Principle: Test as you build, not after you're done.**

#### Checkpoint 1: After Each Function Implementation
```python
# Example: After implementing file scanner
def test_file_scanner_basic():
    """
    SELF-CHECK: Does the scanner find files?
    """
    scanner = FileScanner()
    test_dir = create_test_directory_with_files(count=10)
    files = scanner.scan(test_dir)

    assert len(files) == 10, "Scanner should find all 10 files"
    assert all(f.exists() for f in files), "All files should exist"

    print("✓ Self-check passed: Scanner finds files correctly")
```

**When to run:** Immediately after writing the function, before moving on.

#### Checkpoint 2: After Each Module Implementation
```python
# Example: After implementing OCR module
def self_check_ocr_module():
    """
    SELF-CHECK: Does OCR extract text correctly?
    """
    ocr = ScreenshotProcessor()

    # Test with known screenshot containing "Hello World"
    test_screenshot = "tests/fixtures/hello_world_screenshot.png"
    result = ocr.extract_text(test_screenshot)

    assert "Hello World" in result, "OCR should extract 'Hello World'"
    assert result.confidence > 0.8, "OCR confidence should be high"

    print("✓ Self-check passed: OCR extracts text correctly")

    # Test with empty image
    empty_image = "tests/fixtures/blank.png"
    result = ocr.extract_text(empty_image)
    assert result.text == "", "OCR should return empty for blank image"

    print("✓ Self-check passed: OCR handles edge cases")
```

**When to run:** After completing each major module (scanner, tagger, organizer, etc.)

#### Checkpoint 3: Integration Smoke Tests
```python
# Example: After connecting scanner + database
def smoke_test_scanner_database_integration():
    """
    SMOKE TEST: Can scanner write to database?
    """
    scanner = FileScanner()
    db = DatabaseConnection(":memory:")  # In-memory test DB

    # Scan test directory
    files = scanner.scan("tests/fixtures/sample_files")

    # Write to database
    for file in files:
        node_id = db.insert_node(file)
        assert node_id is not None, "Database insert should succeed"

    # Verify in database
    nodes = db.get_all_nodes()
    assert len(nodes) == len(files), "All scanned files should be in database"

    print("✓ Smoke test passed: Scanner → Database integration works")
```

**When to run:** After connecting any two components together.

#### Checkpoint 4: Feature Acceptance Criteria
```python
# Example: After implementing screenshot organization feature
def acceptance_test_screenshot_organization():
    """
    ACCEPTANCE: Screenshots are organized correctly
    User Story: "As a user, I want screenshots automatically organized by topic"
    """
    # Setup: Create test environment
    desktop = create_temp_directory()
    oxford_folder = create_temp_directory()

    # Create screenshot with "Oxford AI Ethics" text
    screenshot = create_test_screenshot(
        text="Oxford AI Ethics Framework",
        path=desktop / "Screenshot 2025-10-09.png"
    )

    # Run daily job
    daily_job = DailyJob()
    daily_job.run()

    # Verify: Screenshot moved to correct location
    expected_path = oxford_folder / "AI_Ethics" / "Screenshot 2025-10-09.png"
    assert expected_path.exists(), "Screenshot should be moved to Oxford folder"

    # Verify: Tagged correctly
    node = db.get_node_by_path(expected_path)
    assert "oxford" in node.primary_tags
    assert "ai-ethics" in node.primary_tags

    # Verify: Change log created
    changelog = read_changelog(desktop / "CHANGELOG.json")
    assert len(changelog) == 1, "Change log should have one entry"
    assert changelog[0]['file'] == "Screenshot 2025-10-09.png"

    print("✓ Acceptance test passed: Screenshot organization feature works")
```

**When to run:** After completing each user story or feature.

### 2.2 Code Review Self-Checklist

**Before committing any code, verify:**

**Functionality Checks:**
- [ ] Function does what it's supposed to do (happy path)
- [ ] Function handles edge cases (empty input, null, invalid data)
- [ ] Function handles errors gracefully (doesn't crash)
- [ ] Function returns correct data types
- [ ] Function has proper error messages

**Code Quality Checks:**
- [ ] Code is readable and well-commented
- [ ] No hard-coded values (use config/constants)
- [ ] No duplicate code (DRY principle)
- [ ] Functions are single-purpose (SRP)
- [ ] Variable names are descriptive

**Testing Checks:**
- [ ] Unit test exists for this function
- [ ] Test covers happy path
- [ ] Test covers edge cases
- [ ] Test covers error conditions
- [ ] Test is independent (no shared state)

**Integration Checks:**
- [ ] Component integrates with database correctly
- [ ] Component integrates with file system correctly
- [ ] Component handles API failures gracefully
- [ ] Component logs errors appropriately

**Performance Checks:**
- [ ] Function runs in acceptable time (<1s for most operations)
- [ ] No memory leaks (resources are released)
- [ ] No infinite loops possible
- [ ] Batch operations are efficient (not O(n²) when O(n) possible)

**Security Checks:**
- [ ] No SQL injection vulnerabilities (use parameterized queries)
- [ ] No path traversal vulnerabilities (validate file paths)
- [ ] No secrets in code (use environment variables)
- [ ] User input is validated and sanitized

### 2.3 Continuous Self-Validation During Development

**Daily Developer Self-Check (5 minutes before end of day):**

```bash
#!/bin/bash
# daily_dev_check.sh - Run this before committing at end of day

echo "🔍 Daily Self-Check Starting..."

# 1. Run unit tests
echo "1️⃣ Running unit tests..."
pytest tests/unit -v
if [ $? -ne 0 ]; then
    echo "❌ Unit tests failed - fix before committing"
    exit 1
fi

# 2. Run integration tests
echo "2️⃣ Running integration tests..."
pytest tests/integration -v
if [ $? -ne 0 ]; then
    echo "❌ Integration tests failed - fix before committing"
    exit 1
fi

# 3. Check code coverage
echo "3️⃣ Checking code coverage..."
pytest --cov=src --cov-report=term-missing
COVERAGE=$(pytest --cov=src --cov-report=term | grep "TOTAL" | awk '{print $4}' | sed 's/%//')
if [ "$COVERAGE" -lt 80 ]; then
    echo "⚠️  Coverage is ${COVERAGE}% (target: 80%)"
fi

# 4. Run linter
echo "4️⃣ Running linter..."
pylint src/
if [ $? -ne 0 ]; then
    echo "⚠️  Linting issues found"
fi

# 5. Check for common issues
echo "5️⃣ Checking for common issues..."
# Check for print statements (should use logging)
grep -rn "print(" src/ && echo "⚠️  Found print() statements - use logging instead"

# Check for hard-coded paths
grep -rn "/Users/jennifer" src/ && echo "⚠️  Found hard-coded paths"

# Check for API keys in code
grep -rn "sk-" src/ && echo "❌ SECURITY: Found API key in code!"

echo "✅ Daily self-check complete!"
```

**Run frequency:** Before every commit.

### 2.4 Milestone Validation Gates

**Before moving to next phase, validate:**

**Gate 1: After Implementing Core Ingestion (Days 1-2)**
- [ ] File scanner finds all test files (100% accuracy)
- [ ] OCR extracts text from 10 test screenshots (>80% accuracy)
- [ ] Content extractor handles PDF, DOCX, TXT (no crashes)
- [ ] Files written to database correctly (verified by query)
- [ ] Run time <5 minutes for 1,000 files

**Gate 2: After Implementing Processing Layer (Days 3-4)**
- [ ] Auto-tagger assigns tags to 50 test files (>85% user acceptance)
- [ ] Relationship engine creates connections (verified in database)
- [ ] File organizer moves files to correct locations (>90% accuracy)
- [ ] Change logs created with all required fields
- [ ] No data loss (all files accounted for)

**Gate 3: After Implementing Storage Layer (Day 5)**
- [ ] Database queries return correct results (<100ms)
- [ ] Full-text search works (finds known content)
- [ ] Indexes speed up queries (measure before/after)
- [ ] Database handles 10,000 nodes without performance degradation
- [ ] Backup/restore works correctly

**Gate 4: After Implementing Analytics Layer (Day 6)**
- [ ] Strength detection returns sensible results
- [ ] Gap analysis identifies isolated nodes
- [ ] Cross-domain opportunities are meaningful
- [ ] Analytics queries run in <1 second
- [ ] Results match manual verification

**Gate 5: After Implementing API Layer (Day 7)**
- [ ] All API endpoints return valid JSON
- [ ] Error handling works (returns 400/404/500 appropriately)
- [ ] API performance <200ms per request
- [ ] API handles concurrent requests
- [ ] API documentation is accurate

**Gate 6: After Implementing Frontend (Days 8-9)**
- [ ] Graph renders 1,000 nodes smoothly
- [ ] Search returns results in <1 second
- [ ] User can navigate without errors
- [ ] UI works in Safari, Chrome, Firefox
- [ ] Mobile view is functional

**Gate 7: Before Production Deployment (Day 14)**
- [ ] All unit tests pass (400+ tests)
- [ ] All integration tests pass (60+ tests)
- [ ] All E2E tests pass (20+ tests)
- [ ] Performance benchmarks met (see Section 10)
- [ ] User acceptance testing complete
- [ ] No critical bugs remaining

---

## 3. Test Execution Plan

### 3.1 Test Phases

**Phase 1: Unit Testing (Ongoing - Throughout Development)**
- **When:** After implementing each function/class
- **Duration:** Continuous
- **Goal:** 80% code coverage, all functions tested in isolation
- **Tools:** pytest, pytest-cov, pytest-mock

**Phase 2: Integration Testing (Week 1, Days 5-7)**
- **When:** After completing major components
- **Duration:** 2 days
- **Goal:** All component integrations verified
- **Tools:** pytest with fixtures, testcontainers

**Phase 3: System Testing (Week 2, Days 8-10)**
- **When:** After completing end-to-end flows
- **Duration:** 3 days
- **Goal:** All major workflows validated
- **Tools:** pytest-bdd, Selenium (for UI)

**Phase 4: Performance Testing (Week 2, Days 11-12)**
- **When:** After system testing passes
- **Duration:** 2 days
- **Goal:** Meet all performance benchmarks
- **Tools:** pytest-benchmark, locust, memory-profiler

**Phase 5: User Acceptance Testing (Week 2, Days 13-14)**
- **When:** After performance testing passes
- **Duration:** 2 days
- **Goal:** User validates all features work as expected
- **Tools:** Manual testing, user feedback

### 3.2 Test Data Setup

**Test Database:**
```python
@pytest.fixture
def test_database():
    """Create in-memory SQLite database for testing"""
    db = sqlite3.connect(":memory:")
    cursor = db.cursor()

    # Load schema
    with open("src/database/schema.sql") as f:
        cursor.executescript(f.read())

    yield db

    db.close()
```

**Test File System:**
```python
@pytest.fixture
def test_file_system(tmp_path):
    """Create temporary file system structure for testing"""
    # Create directories
    documents = tmp_path / "Documents"
    downloads = tmp_path / "Downloads"
    desktop = tmp_path / "Desktop"

    documents.mkdir()
    downloads.mkdir()
    desktop.mkdir()

    # Create sample files
    (documents / "test.pdf").write_bytes(create_sample_pdf())
    (downloads / "screenshot.png").write_bytes(create_sample_screenshot())
    (desktop / "notes.txt").write_text("Sample notes content")

    yield {
        'documents': documents,
        'downloads': downloads,
        'desktop': desktop,
        'root': tmp_path
    }
```

**Test Fixtures:**
```
tests/fixtures/
├── documents/
│   ├── ai_ethics.pdf           # Known content for testing
│   ├── resume.pdf              # Known content for testing
│   └── research_notes.txt      # Known content for testing
├── screenshots/
│   ├── hello_world.png         # OCR test: "Hello World"
│   ├── code_snippet.png        # OCR test: code
│   ├── blank.png               # OCR test: empty
│   └── corrupted.png           # OCR test: error handling
├── notes/
│   └── sample_notes.json       # Apple Notes test data
└── database/
    └── test_graph.db           # Pre-populated test database
```

### 3.3 Automated vs. Manual Testing

**Automated (95% of tests):**
- All unit tests
- All integration tests
- Most E2E tests
- All performance tests
- Regression tests

**Manual (5% of tests):**
- Visual UI validation
- Usability testing
- Edge case exploration
- User acceptance testing
- Final smoke testing before production

---

## 4. Unit Testing

### 4.1 Unit Test Structure

**Template:**
```python
import pytest
from src.core.scanner import FileScanner

class TestFileScanner:
    """Test suite for FileScanner component"""

    def test_scan_finds_all_files(self, test_file_system):
        """Scanner should find all files in directory"""
        # Arrange
        scanner = FileScanner()
        test_dir = test_file_system['documents']

        # Act
        files = scanner.scan(test_dir)

        # Assert
        assert len(files) == 10
        assert all(f.exists() for f in files)

    def test_scan_excludes_hidden_files(self, test_file_system):
        """Scanner should skip files starting with ."""
        # Arrange
        scanner = FileScanner()
        test_dir = test_file_system['documents']
        (test_dir / ".hidden").write_text("hidden")

        # Act
        files = scanner.scan(test_dir)

        # Assert
        assert not any(f.name.startswith('.') for f in files)

    def test_scan_handles_permission_denied(self, test_file_system):
        """Scanner should gracefully handle permission errors"""
        # Arrange
        scanner = FileScanner()
        protected_dir = test_file_system['root'] / "protected"
        protected_dir.mkdir(mode=0o000)  # No permissions

        # Act
        files = scanner.scan(protected_dir)

        # Assert
        assert files == []  # Should return empty, not crash
        assert scanner.errors['permission_denied'] == 1

    def test_scan_performance_10k_files(self, benchmark):
        """Scanner should process 10,000 files in <60 seconds"""
        # Arrange
        scanner = FileScanner()
        large_dir = create_test_directory(file_count=10000)

        # Act & Assert
        result = benchmark(scanner.scan, large_dir)
        assert len(result) == 10000
        assert benchmark.stats['mean'] < 60  # seconds
```

### 4.2 Unit Test Coverage Targets

| Component | Target Coverage | Priority | Test Count |
|-----------|-----------------|----------|------------|
| File Scanner | 90% | Critical | 25 |
| Content Extractor | 85% | Critical | 30 |
| OCR Processor | 80% | Critical | 20 |
| Auto-Tagger | 90% | Critical | 40 |
| Relationship Engine | 85% | High | 35 |
| File Organizer | 90% | Critical | 30 |
| Database Queries | 95% | Critical | 50 |
| API Endpoints | 90% | High | 40 |
| Background Jobs | 85% | High | 30 |
| Frontend (JS) | 70% | Medium | 20 |
| **Total** | **85%** | - | **320** |

### 4.3 Critical Unit Tests by Component

**File Scanner:**
```python
def test_scanner_finds_new_files()
def test_scanner_finds_modified_files()
def test_scanner_skips_unchanged_files()
def test_scanner_handles_symlinks()
def test_scanner_excludes_patterns()
def test_scanner_handles_unicode_filenames()
def test_scanner_handles_very_long_paths()
def test_scanner_handles_deleted_files_during_scan()
def test_scanner_performance_large_directory()
def test_scanner_incremental_vs_full_scan()
```

**OCR Processor:**
```python
def test_ocr_extracts_simple_text()
def test_ocr_extracts_multiline_text()
def test_ocr_handles_poor_quality_image()
def test_ocr_handles_blank_image()
def test_ocr_handles_corrupted_image()
def test_ocr_handles_unsupported_format()
def test_ocr_handles_very_large_image()
def test_ocr_timeout_protection()
def test_ocr_confidence_scoring()
def test_ocr_language_detection()
```

**Auto-Tagger:**
```python
def test_tagger_assigns_primary_tags()
def test_tagger_assigns_secondary_tags()
def test_tagger_extracts_keywords()
def test_tagger_enforces_1_to_3_primary_tags()
def test_tagger_normalizes_tag_format()
def test_tagger_uses_claude_api_when_available()
def test_tagger_falls_back_to_local_nlp()
def test_tagger_applies_learning_corrections()
def test_tagger_handles_empty_content()
def test_tagger_handles_very_long_content()
def test_tagger_context_awareness()
def test_tagger_performance_batch_processing()
```

**Relationship Engine:**
```python
def test_relationship_content_similarity()
def test_relationship_temporal_same_day()
def test_relationship_temporal_same_week()
def test_relationship_hierarchical()
def test_relationship_cross_domain_detection()
def test_relationship_weight_calculation()
def test_relationship_bidirectional()
def test_relationship_deduplication()
def test_relationship_performance_large_graph()
```

**File Organizer:**
```python
def test_organizer_moves_file_to_correct_location()
def test_organizer_creates_destination_directory()
def test_organizer_handles_duplicate_filenames()
def test_organizer_updates_database_path()
def test_organizer_creates_change_log_entry()
def test_organizer_skips_do_not_move_folders()
def test_organizer_handles_move_failure()
def test_organizer_rollback_on_error()
def test_organizer_preserves_file_metadata()
def test_organizer_performance_batch_moves()
```

**Database:**
```python
def test_db_insert_node()
def test_db_update_node()
def test_db_delete_node()
def test_db_insert_edge()
def test_db_query_by_tag()
def test_db_query_by_date()
def test_db_full_text_search()
def test_db_transaction_commit()
def test_db_transaction_rollback()
def test_db_concurrent_writes()
def test_db_index_performance()
def test_db_backup_restore()
```

---

## 5. Integration Testing

### 5.1 Integration Test Scenarios

**Scenario 1: Scanner → Database Integration**
```python
def test_scanner_writes_to_database(test_database, test_file_system):
    """
    INTEGRATION: Scanner finds files and writes them to database
    """
    # Arrange
    scanner = FileScanner()
    db = DatabaseConnection(test_database)

    # Act
    files = scanner.scan(test_file_system['documents'])
    for file in files:
        node_id = db.insert_node({
            'file_path': str(file),
            'file_name': file.name,
            'date_created': file.stat().st_mtime,
            'type': 'document'
        })

    # Assert
    nodes = db.query("SELECT * FROM nodes")
    assert len(nodes) == len(files)
    assert all(node['file_name'] in [f.name for f in files] for node in nodes)
```

**Scenario 2: OCR → Tagger Integration**
```python
def test_ocr_output_feeds_tagger(test_database):
    """
    INTEGRATION: OCR extracts text, tagger uses it for tagging
    """
    # Arrange
    ocr = ScreenshotProcessor()
    tagger = AutoTagger()
    screenshot = "tests/fixtures/screenshots/ai_ethics.png"

    # Act
    ocr_result = ocr.extract_text(screenshot)
    tags = tagger.tag_content(
        content=ocr_result.text,
        filename="ai_ethics.png",
        context={'type': 'screenshot'}
    )

    # Assert
    assert ocr_result.text != ""
    assert "ai-ethics" in tags['primary_tags']
    assert tags['confidence'] > 0.7
```

**Scenario 3: Tagger → Organizer Integration**
```python
def test_tagger_tags_feed_organizer(test_file_system, test_database):
    """
    INTEGRATION: Tags determine file destination
    """
    # Arrange
    tagger = AutoTagger()
    organizer = FileOrganizer()
    test_file = test_file_system['downloads'] / "oxford_notes.pdf"

    # Act
    tags = tagger.tag_file(test_file)
    destination = organizer.determine_destination(test_file, tags)
    organizer.move_file(test_file, destination)

    # Assert
    assert "oxford" in tags['primary_tags']
    assert "Education/Oxford" in str(destination)
    assert destination.exists()
    assert not test_file.exists()  # Original removed
```

**Scenario 4: API → Database Integration**
```python
def test_api_queries_database(test_database, client):
    """
    INTEGRATION: API endpoints query database correctly
    """
    # Arrange
    db = DatabaseConnection(test_database)
    db.insert_node({
        'id': 'node-001',
        'file_name': 'test.pdf',
        'primary_tags': ['ai-ethics'],
        'type': 'document'
    })

    # Act
    response = client.get('/api/search?q=ai-ethics')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data['results']) == 1
    assert data['results'][0]['id'] == 'node-001'
```

**Scenario 5: Background Job → Full Pipeline**
```python
def test_daily_job_end_to_end(test_file_system, test_database):
    """
    INTEGRATION: Daily job runs full pipeline
    """
    # Arrange
    daily_job = DailyJob(
        database=test_database,
        paths=test_file_system
    )

    # Create test files
    (test_file_system['desktop'] / "screenshot.png").write_bytes(
        create_screenshot_with_text("Oxford AI Ethics")
    )

    # Act
    result = daily_job.run()

    # Assert - File was processed through entire pipeline
    assert result['files_scanned'] == 1
    assert result['ocr_processed'] == 1
    assert result['files_tagged'] == 1
    assert result['files_organized'] == 1
    assert result['relationships_created'] >= 0

    # Verify final state
    db = DatabaseConnection(test_database)
    nodes = db.query("SELECT * FROM nodes WHERE type='screenshot'")
    assert len(nodes) == 1
    assert "oxford" in nodes[0]['primary_tags']

    # Verify file moved
    oxford_folder = test_file_system['documents'] / "Education/Oxford"
    assert (oxford_folder / "screenshot.png").exists()
```

### 5.2 Integration Test Matrix

| Component A | Component B | Test Scenario | Status |
|-------------|-------------|---------------|--------|
| Scanner | Database | Write scanned files to DB | ✓ |
| Scanner | Extractor | Pass files for content extraction | ✓ |
| Extractor | Tagger | Extract content, then tag | ✓ |
| Tagger | Database | Write tags to DB | ✓ |
| Tagger | Organizer | Use tags to determine destination | ✓ |
| Organizer | Database | Update file paths after move | ✓ |
| Organizer | Changelog | Record file moves | ✓ |
| Database | API | API queries DB | ✓ |
| API | Frontend | Frontend calls API | ✓ |
| Claude API | Tagger | API provides tags | ✓ |
| Local NLP | Tagger | Fallback tagging | ✓ |
| Relationship Engine | Database | Write edges to DB | ✓ |
| Analytics | Database | Query nodes for insights | ✓ |

---

## 6. End-to-End Testing

### 6.1 Critical User Workflows

**Workflow 1: New Screenshot → Organized and Tagged**
```python
@pytest.mark.e2e
def test_workflow_screenshot_organization():
    """
    E2E: User takes screenshot → System organizes it

    Steps:
    1. Screenshot saved to Desktop
    2. Daily job runs
    3. OCR extracts text
    4. System tags screenshot
    5. System moves to appropriate folder
    6. Change log created
    7. User can search for screenshot
    """
    # Setup
    desktop = Path.home() / "Desktop"
    screenshot = desktop / "Screenshot_2025-10-09_oxford.png"
    screenshot.write_bytes(create_screenshot_with_text("Oxford AI Ethics Framework"))

    # Run daily job
    subprocess.run(["python", "src/jobs/daily_job.py", "--manual"])

    # Verify: Screenshot moved
    expected_location = Path.home() / "Documents/Education/Oxford/AI_Ethics"
    moved_screenshot = expected_location / "Screenshot_2025-10-09_oxford.png"
    assert moved_screenshot.exists(), "Screenshot should be moved to Oxford folder"

    # Verify: Tagged correctly
    db = DatabaseConnection()
    node = db.get_node_by_path(str(moved_screenshot))
    assert node is not None
    assert "oxford" in node['primary_tags']
    assert "ai-ethics" in node['primary_tags']
    assert "screenshot" in node['primary_tags']

    # Verify: Searchable
    results = db.search("Oxford AI Ethics")
    assert len(results) > 0
    assert any(r['file_name'] == moved_screenshot.name for r in results)

    # Verify: Change log exists
    changelog = desktop / "CHANGELOG.json"
    assert changelog.exists()
    with open(changelog) as f:
        log = json.load(f)
        assert len(log) == 1
        assert log[0]['file'] == "Screenshot_2025-10-09_oxford.png"
```

**Workflow 2: Search for File by Content**
```python
@pytest.mark.e2e
def test_workflow_content_search():
    """
    E2E: User searches for file by content

    Steps:
    1. User opens web UI
    2. User types search query
    3. System returns relevant results
    4. User clicks result
    5. File details displayed
    """
    # Using Selenium for browser automation
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/search")

    # Type search query
    search_box = driver.find_element(By.ID, "search-input")
    search_box.send_keys("AI ethics framework")
    search_box.send_keys(Keys.RETURN)

    # Wait for results
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "search-result"))
    )

    # Verify results displayed
    results = driver.find_elements(By.CLASS_NAME, "search-result")
    assert len(results) > 0

    # Click first result
    results[0].click()

    # Verify details displayed
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "node-details"))
    )

    details = driver.find_element(By.CLASS_NAME, "node-details")
    assert "ai-ethics" in details.text.lower()

    driver.quit()
```

**Workflow 3: Manual Job Trigger from Web UI**
```python
@pytest.mark.e2e
def test_workflow_manual_job_trigger():
    """
    E2E: User triggers job from web UI

    Steps:
    1. User opens automation page
    2. User clicks "Run Daily Job"
    3. Job starts executing
    4. Progress shown to user
    5. Job completes
    6. Results displayed
    """
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/automation")

    # Click "Run Daily Job" button
    run_button = driver.find_element(By.ID, "run-daily-job")
    run_button.click()

    # Verify job started
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-running"))
    )

    # Wait for completion (max 2 minutes)
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CLASS_NAME, "job-complete"))
    )

    # Verify results displayed
    results = driver.find_element(By.CLASS_NAME, "job-results")
    assert "success" in results.text.lower()

    driver.quit()
```

**Workflow 4: Graph Visualization Interaction**
```python
@pytest.mark.e2e
def test_workflow_graph_interaction():
    """
    E2E: User interacts with knowledge graph

    Steps:
    1. User opens main page
    2. Graph renders
    3. User hovers over node
    4. Tooltip appears
    5. User clicks node
    6. Connections highlighted
    7. User clicks legend filter
    8. Graph filters by cluster
    """
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")

    # Wait for graph to render
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "graph-canvas"))
    )

    # Find a node
    node = driver.find_element(By.CSS_SELECTOR, "circle.node")

    # Hover over node
    ActionChains(driver).move_to_element(node).perform()

    # Verify tooltip appears
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tooltip"))
    )

    # Click node
    node.click()

    # Verify connections highlighted
    highlighted = driver.find_elements(By.CSS_SELECTOR, "line.highlighted")
    assert len(highlighted) > 0

    # Click legend filter
    legend_item = driver.find_element(By.CSS_SELECTOR, "[data-cluster='oxford']")
    legend_item.click()

    # Verify nodes filtered
    visible_nodes = driver.find_elements(By.CSS_SELECTOR, "circle.node:not(.hidden)")
    all_nodes = driver.find_elements(By.CSS_SELECTOR, "circle.node")
    assert len(visible_nodes) < len(all_nodes)

    driver.quit()
```

### 6.2 E2E Test Coverage

| User Story | E2E Test | Priority | Status |
|------------|----------|----------|--------|
| Screenshot organization | test_workflow_screenshot_organization | Critical | ✓ |
| Content search | test_workflow_content_search | Critical | ✓ |
| File organization | test_workflow_file_organization | Critical | ✓ |
| Manual job trigger | test_workflow_manual_job_trigger | High | ✓ |
| Graph interaction | test_workflow_graph_interaction | High | ✓ |
| Analytics dashboard | test_workflow_analytics_view | High | ✓ |
| Change log review | test_workflow_changelog_view | Medium | ✓ |
| Tag correction | test_workflow_tag_correction | Medium | ✓ |
| Export data | test_workflow_export_data | Low | - |

---

## 7. Performance Testing

### 7.1 Performance Benchmarks

**File Scanning:**
```python
@pytest.mark.performance
def test_performance_scan_10k_files(benchmark):
    """
    PERFORMANCE: Scan 10,000 files in <60 seconds
    """
    scanner = FileScanner()
    large_directory = create_test_directory_with_files(count=10000)

    result = benchmark(scanner.scan, large_directory)

    assert len(result) == 10000
    assert benchmark.stats['mean'] < 60.0, f"Scan took {benchmark.stats['mean']}s (target: <60s)"
```

**OCR Processing:**
```python
@pytest.mark.performance
def test_performance_ocr_batch(benchmark):
    """
    PERFORMANCE: Process 100 screenshots in <200 seconds
    """
    ocr = ScreenshotProcessor()
    screenshots = [create_test_screenshot() for _ in range(100)]

    result = benchmark(ocr.process_batch, screenshots)

    assert len(result) == 100
    assert benchmark.stats['mean'] < 200.0, "Batch OCR should take <200s"
```

**Database Queries:**
```python
@pytest.mark.performance
def test_performance_search_10k_nodes(benchmark, populated_database):
    """
    PERFORMANCE: Search 10,000 nodes in <100ms
    """
    db = DatabaseConnection(populated_database)

    result = benchmark(db.search, "ai ethics")

    assert benchmark.stats['mean'] < 0.1, f"Search took {benchmark.stats['mean']}s (target: <0.1s)"
```

**Graph Rendering:**
```python
@pytest.mark.performance
def test_performance_graph_render_1000_nodes(benchmark):
    """
    PERFORMANCE: Render 1,000 node graph in <3 seconds
    """
    # Using Selenium with timing
    driver = webdriver.Chrome()

    def render_graph():
        start = time.time()
        driver.get("http://localhost:5000/?nodes=1000")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "circle.node"))
        )
        return time.time() - start

    render_time = benchmark(render_graph)

    assert render_time < 3.0, f"Graph render took {render_time}s (target: <3s)"

    driver.quit()
```

**API Response Times:**
```python
@pytest.mark.performance
def test_performance_api_response_times(client):
    """
    PERFORMANCE: All API endpoints respond in <200ms
    """
    endpoints = [
        '/api/graph/data',
        '/api/search?q=test',
        '/api/analytics/strengths',
        '/api/automation/status',
        '/api/changelog?days=7'
    ]

    for endpoint in endpoints:
        start = time.time()
        response = client.get(endpoint)
        duration = time.time() - start

        assert response.status_code == 200
        assert duration < 0.2, f"{endpoint} took {duration}s (target: <0.2s)"
```

### 7.2 Load Testing

**Concurrent API Requests:**
```python
from locust import HttpUser, task, between

class KnowledgeMapUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def search(self):
        self.client.get("/api/search?q=ai")

    @task(2)
    def graph_data(self):
        self.client.get("/api/graph/data")

    @task(1)
    def analytics(self):
        self.client.get("/api/analytics/strengths")

# Run with: locust -f tests/performance/load_test.py --users 50 --spawn-rate 5
```

**Test Scenario:** 50 concurrent users, verify system handles load without errors or slowdowns.

### 7.3 Memory Testing

**Memory Leak Detection:**
```python
@pytest.mark.performance
def test_memory_leak_detection():
    """
    PERFORMANCE: Detect memory leaks in long-running operations
    """
    import tracemalloc

    tracemalloc.start()

    scanner = FileScanner()

    # Run operation 100 times
    for i in range(100):
        scanner.scan("/path/to/test/directory")

        if i % 10 == 0:
            current, peak = tracemalloc.get_traced_memory()
            print(f"Iteration {i}: Current={current / 1024 / 1024:.1f}MB, Peak={peak / 1024 / 1024:.1f}MB")

    final_current, final_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Memory should not continuously grow
    assert final_current < 100 * 1024 * 1024, "Memory usage should not exceed 100MB"
```

### 7.4 Performance Metrics Dashboard

**Track Over Time:**
- Daily scan duration (target: <5 minutes)
- OCR processing speed (target: <2 seconds per screenshot)
- Search query latency (target: <100ms)
- Database query latency (target: <50ms)
- API response time (target: <200ms)
- Memory usage (target: <500MB during scanning)
- CPU usage (target: <50% during scanning)

---

## 8. Component-Specific Test Cases

### 8.1 Ingestion Layer Tests

**File Scanner Tests:**
```python
class TestFileScanner:
    def test_finds_all_files_in_directory(self)
    def test_finds_new_files_since_last_scan(self)
    def test_finds_modified_files(self)
    def test_skips_hidden_files(self)
    def test_handles_permission_denied_gracefully(self)
    def test_handles_symlinks_correctly(self)
    def test_excludes_configured_patterns(self)
    def test_handles_unicode_filenames(self)
    def test_handles_very_long_paths(self)
    def test_incremental_scan_performance(self)
    def test_full_scan_vs_incremental_scan(self)
    def test_concurrent_file_modifications(self)
```

**Content Extractor Tests:**
```python
class TestContentExtractor:
    def test_extracts_pdf_text(self)
    def test_extracts_docx_text(self)
    def test_extracts_txt_text(self)
    def test_handles_corrupted_pdf(self)
    def test_handles_encrypted_pdf(self)
    def test_handles_empty_file(self)
    def test_handles_binary_file(self)
    def test_extracts_metadata(self)
    def test_handles_large_files(self)
    def test_performance_batch_extraction(self)
```

**OCR Processor Tests:**
```python
class TestOCRProcessor:
    def test_extracts_simple_text_from_screenshot(self)
    def test_extracts_multiline_text(self)
    def test_extracts_text_from_code_screenshot(self)
    def test_handles_blank_image(self)
    def test_handles_corrupted_image(self)
    def test_handles_unsupported_format(self)
    def test_handles_very_large_image(self)
    def test_timeout_protection(self)
    def test_confidence_scoring(self)
    def test_detects_image_type(self)  # infographic, quote, code, etc.
    def test_apple_vision_fallback(self)
```

### 8.2 Processing Layer Tests

**Auto-Tagger Tests:**
```python
class TestAutoTagger:
    def test_assigns_1_to_3_primary_tags(self)
    def test_assigns_secondary_tags(self)
    def test_extracts_keywords(self)
    def test_normalizes_tag_format(self)
    def test_uses_claude_api_when_available(self)
    def test_falls_back_to_local_nlp(self)
    def test_applies_context_from_calendar(self)
    def test_applies_context_from_location(self)
    def test_applies_learning_corrections(self)
    def test_handles_empty_content(self)
    def test_handles_very_long_content(self)
    def test_handles_non_english_content(self)
    def test_tag_synonym_mapping(self)
    def test_tag_hierarchy_enforcement(self)
    def test_confidence_scoring(self)
    def test_batch_tagging_performance(self)
```

**Relationship Engine Tests:**
```python
class TestRelationshipEngine:
    def test_detects_content_similarity(self)
    def test_detects_temporal_same_day(self)
    def test_detects_temporal_same_week(self)
    def test_detects_hierarchical_relationships(self)
    def test_detects_cross_domain_bridges(self)
    def test_calculates_relationship_weights(self)
    def test_creates_bidirectional_edges(self)
    def test_avoids_duplicate_relationships(self)
    def test_updates_relationships_on_node_change(self)
    def test_removes_relationships_on_node_delete(self)
    def test_performance_large_graph(self)
```

**File Organizer Tests:**
```python
class TestFileOrganizer:
    def test_determines_destination_from_tags(self)
    def test_creates_destination_directory(self)
    def test_moves_file_successfully(self)
    def test_handles_duplicate_filenames(self)
    def test_updates_database_after_move(self)
    def test_creates_change_log_entry(self)
    def test_skips_do_not_move_folders(self)
    def test_handles_move_failure_gracefully(self)
    def test_rollback_on_error(self)
    def test_preserves_file_metadata(self)
    def test_handles_special_characters_in_filename(self)
    def test_batch_organization_performance(self)
```

### 8.3 Storage Layer Tests

**Database Tests:**
```python
class TestDatabase:
    def test_insert_node(self)
    def test_update_node(self)
    def test_delete_node(self)
    def test_insert_edge(self)
    def test_delete_edge(self)
    def test_query_nodes_by_tag(self)
    def test_query_nodes_by_date(self)
    def test_query_nodes_by_type(self)
    def test_full_text_search(self)
    def test_full_text_search_with_stemming(self)
    def test_transaction_commit(self)
    def test_transaction_rollback(self)
    def test_concurrent_reads(self)
    def test_concurrent_writes(self)
    def test_handles_database_lock(self)
    def test_handles_constraint_violations(self)
    def test_backup_database(self)
    def test_restore_database(self)
    def test_database_optimization(self)
    def test_index_performance(self)
    def test_query_performance_10k_nodes(self)
```

### 8.4 Analytics Layer Tests

**Analytics Engine Tests:**
```python
class TestAnalyticsEngine:
    def test_calculates_knowledge_strengths(self)
    def test_detects_knowledge_gaps(self)
    def test_finds_cross_domain_opportunities(self)
    def test_calculates_time_vs_output(self)
    def test_detects_isolated_nodes(self)
    def test_calculates_business_value_score(self)
    def test_summarizes_recent_activity(self)
    def test_detects_patterns(self)
    def test_cache_invalidation(self)
    def test_cache_performance(self)
    def test_handles_empty_graph(self)
    def test_handles_large_graph(self)
```

### 8.5 API Layer Tests

**API Endpoint Tests:**
```python
class TestAPIEndpoints:
    def test_get_graph_data(self)
    def test_get_node_details(self)
    def test_search_by_query(self)
    def test_search_with_filters(self)
    def test_get_analytics_strengths(self)
    def test_get_analytics_gaps(self)
    def test_get_analytics_opportunities(self)
    def test_trigger_job_daily(self)
    def test_trigger_job_weekly(self)
    def test_get_job_status(self)
    def test_get_changelog(self)
    def test_filter_changelog_by_date(self)
    def test_handles_invalid_node_id(self)
    def test_handles_invalid_search_query(self)
    def test_handles_invalid_job_type(self)
    def test_returns_correct_error_codes(self)
    def test_handles_concurrent_requests(self)
    def test_api_performance(self)
```

### 8.6 Frontend Tests

**Graph Visualization Tests (JavaScript + Jest):**
```javascript
describe('Graph Visualization', () => {
    test('renders graph with nodes and edges', () => {})
    test('node hover shows tooltip', () => {})
    test('node click highlights connections', () => {})
    test('legend filter works', () => {})
    test('layout switch works', () => {})
    test('zoom and pan work', () => {})
    test('search highlights nodes', () => {})
    test('handles empty graph gracefully', () => {})
    test('handles large graph (1000+ nodes)', () => {})
    test('handles network errors', () => {})
})
```

**Search Interface Tests:**
```javascript
describe('Search Interface', () => {
    test('search returns results', () => {})
    test('search autocomplete works', () => {})
    test('search filters work', () => {})
    test('search highlights matches', () => {})
    test('click result opens details', () => {})
    test('handles no results gracefully', () => {})
    test('handles search errors', () => {})
})
```

### 8.7 Background Jobs Tests

**Daily Job Tests:**
```python
class TestDailyJob:
    def test_runs_all_steps_in_order(self)
    def test_logs_execution(self)
    def test_handles_step_failure_gracefully(self)
    def test_completes_within_time_limit(self)
    def test_prevents_concurrent_execution(self)
    def test_resumes_after_interruption(self)
    def test_sends_error_notification_on_failure(self)
```

**Weekly Job Tests:**
```python
class TestWeeklyJob:
    def test_syncs_apple_notes(self)
    def test_syncs_calendar(self)
    def test_computes_analytics(self)
    def test_handles_missing_data_sources(self)
    def test_completes_within_time_limit(self)
```

**Monthly Job Tests:**
```python
class TestMonthlyJob:
    def test_archives_old_logs(self)
    def test_generates_monthly_report(self)
    def test_detects_stale_files(self)
    def test_optimizes_database(self)
    def test_completes_within_time_limit(self)
```

---

## 9. Testing Tools & Frameworks

### 9.1 Python Testing Stack

**Core Testing Framework:**
```bash
# Install testing dependencies
pip install pytest pytest-cov pytest-mock pytest-benchmark pytest-bdd
pip install pytest-xdist  # Parallel test execution
pip install pytest-timeout  # Timeout protection
```

**Configuration (pytest.ini):**
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --strict-markers
    --tb=short
    --cov=src
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    performance: Performance tests
    slow: Slow tests (>1 second)
```

**Key Libraries:**

**pytest** - Main testing framework
```python
# Install: pip install pytest
# Run: pytest
# Run specific: pytest tests/unit/test_scanner.py
# Run with markers: pytest -m unit
```

**pytest-cov** - Code coverage measurement
```python
# Install: pip install pytest-cov
# Run with coverage: pytest --cov=src --cov-report=html
# View report: open htmlcov/index.html
```

**pytest-mock** - Mocking framework
```python
# Install: pip install pytest-mock
# Example:
def test_tagger_uses_claude_api(mocker):
    mock_api = mocker.patch('src.integrations.claude_api.call_api')
    mock_api.return_value = {'tags': ['ai-ethics']}

    tagger = AutoTagger()
    result = tagger.tag_content("test content")

    assert mock_api.called
    assert 'ai-ethics' in result['primary_tags']
```

**pytest-benchmark** - Performance benchmarking
```python
# Install: pip install pytest-benchmark
# Example:
def test_scanner_performance(benchmark):
    scanner = FileScanner()
    result = benchmark(scanner.scan, "/test/directory")
    assert benchmark.stats['mean'] < 1.0
```

**pytest-bdd** - Behavior-driven development
```python
# Install: pip install pytest-bdd
# Example:
from pytest_bdd import scenario, given, when, then

@scenario('features/screenshot_organization.feature',
          'Screenshot is organized automatically')
def test_screenshot_organization():
    pass

@given('a screenshot on the Desktop')
def screenshot_on_desktop():
    return create_test_screenshot()

@when('the daily job runs')
def run_daily_job():
    DailyJob().run()

@then('the screenshot is moved to the Oxford folder')
def verify_screenshot_moved():
    assert Path("~/Documents/Oxford/screenshot.png").exists()
```

### 9.2 Frontend Testing Stack

**JavaScript Testing:**
```bash
# Install testing dependencies
npm install --save-dev jest @testing-library/dom @testing-library/jest-dom
npm install --save-dev selenium-webdriver
```

**Jest Configuration (jest.config.js):**
```javascript
module.exports = {
    testEnvironment: 'jsdom',
    coverageDirectory: 'coverage',
    collectCoverageFrom: [
        'frontend/static/js/**/*.js',
        '!frontend/static/js/vendor/**'
    ],
    coverageThreshold: {
        global: {
            branches: 70,
            functions: 70,
            lines: 70,
            statements: 70
        }
    }
};
```

**Selenium for E2E Testing:**
```python
# Install: pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_graph_renders():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "graph-canvas"))
    )

    assert "Knowledge Map" in driver.title
    driver.quit()
```

### 9.3 Database Testing Tools

**In-Memory SQLite for Tests:**
```python
import sqlite3

@pytest.fixture
def test_db():
    """Create in-memory test database"""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Load schema
    with open("src/database/schema.sql") as f:
        cursor.executescript(f.read())

    yield conn
    conn.close()
```

**Test Data Fixtures:**
```python
@pytest.fixture
def populated_db(test_db):
    """Database with sample data"""
    cursor = test_db.cursor()

    # Insert sample nodes
    for i in range(100):
        cursor.execute("""
            INSERT INTO nodes (id, file_name, type, primary_tags)
            VALUES (?, ?, ?, ?)
        """, (f"node-{i}", f"file{i}.pdf", "document", "ai-ethics"))

    test_db.commit()
    return test_db
```

### 9.4 Performance Testing Tools

**pytest-benchmark** - Microbenchmarking
```python
def test_search_performance(benchmark, populated_db):
    db = DatabaseConnection(populated_db)
    result = benchmark(db.search, "ai ethics")
    assert benchmark.stats['mean'] < 0.1
```

**Locust** - Load testing
```python
# Install: pip install locust
from locust import HttpUser, task

class APIUser(HttpUser):
    @task
    def search(self):
        self.client.get("/api/search?q=test")
```

**memory-profiler** - Memory usage profiling
```python
# Install: pip install memory-profiler
from memory_profiler import profile

@profile
def test_memory_usage():
    scanner = FileScanner()
    scanner.scan("/large/directory")
```

### 9.5 Continuous Integration

**GitHub Actions Workflow (.github/workflows/tests.yml):**
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov

    - name: Run unit tests
      run: pytest tests/unit -v --cov=src

    - name: Run integration tests
      run: pytest tests/integration -v

    - name: Check coverage
      run: |
        pytest --cov=src --cov-report=term-missing --cov-fail-under=80

    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v2
```

---

## 10. Success Criteria & Benchmarks

### 10.1 Functional Success Criteria

**Must Pass Before Production:**

**File Discovery & Scanning:**
- [ ] Finds 100% of test files in monitored locations
- [ ] Detects new files within 1 scan cycle
- [ ] Detects modified files accurately
- [ ] Handles permission errors gracefully
- [ ] Completes scan of 10,000 files in <60 seconds

**OCR Processing:**
- [ ] Extracts text from 90%+ of test screenshots
- [ ] OCR confidence >0.80 for clear screenshots
- [ ] Handles corrupted images without crashing
- [ ] Processes screenshot in <2 seconds average
- [ ] Batch processes 100 screenshots in <200 seconds

**Auto-Tagging:**
- [ ] Assigns 1-3 primary tags to every file
- [ ] Tagging accuracy >85% (user acceptance)
- [ ] Claude API fallback to local NLP works seamlessly
- [ ] Learning system improves accuracy over time
- [ ] Processes file in <2 seconds average

**File Organization:**
- [ ] Moves files to correct destination >90% of time
- [ ] Creates change log for every move
- [ ] No data loss (all files accounted for)
- [ ] Handles duplicate filenames correctly
- [ ] Respects "do not move" folder rules

**Database:**
- [ ] All queries return in <100ms for 10k nodes
- [ ] Full-text search works with 95%+ relevance
- [ ] Handles concurrent access without corruption
- [ ] Backup/restore preserves 100% of data
- [ ] Database size <50MB for 10k nodes

**API:**
- [ ] All endpoints return valid JSON
- [ ] Response times <200ms (95th percentile)
- [ ] Proper error codes (400, 404, 500)
- [ ] Handles 50 concurrent requests
- [ ] No memory leaks under load

**Frontend:**
- [ ] Graph renders 1,000 nodes in <3 seconds
- [ ] Search returns results in <1 second
- [ ] UI responsive on mobile and desktop
- [ ] Works in Safari, Chrome, Firefox
- [ ] No JavaScript errors in console

**Background Jobs:**
- [ ] Daily job completes in <5 minutes
- [ ] Weekly job completes in <10 minutes
- [ ] Monthly job completes in <5 minutes
- [ ] Jobs log all operations
- [ ] Jobs handle errors without crashing

### 10.2 Performance Benchmarks

| Operation | Target | Measurement Method |
|-----------|--------|-------------------|
| File scan (10k files) | <60s | pytest-benchmark |
| Screenshot OCR | <2s each | pytest-benchmark |
| Batch OCR (100) | <200s | pytest-benchmark |
| File tagging | <2s each | pytest-benchmark |
| Batch tagging (100) | <200s | pytest-benchmark |
| File move | <100ms | pytest-benchmark |
| Database insert | <10ms | pytest-benchmark |
| Database query | <50ms | pytest-benchmark |
| Full-text search | <100ms | pytest-benchmark |
| API response | <200ms | Locust load test |
| Graph render (1000 nodes) | <3s | Selenium timing |
| Daily job | <5min | Manual timing |
| Weekly job | <10min | Manual timing |
| Memory usage (idle) | <200MB | memory-profiler |
| Memory usage (scanning) | <500MB | memory-profiler |

### 10.3 Quality Metrics

**Code Coverage:**
- Overall: 80%+
- Critical components: 90%+
- API endpoints: 90%+
- Database queries: 95%+

**Test Metrics:**
- Total tests: 400+
- Unit tests: 320+
- Integration tests: 60+
- E2E tests: 20+
- All tests pass: 100%

**Bug Density:**
- Critical bugs: 0
- High priority bugs: <5
- Medium priority bugs: <20
- Low priority bugs: <50

**User Acceptance:**
- Tagging accuracy: >85% user satisfaction
- Organization accuracy: >90% user satisfaction
- Search relevance: >95% relevant results
- Overall satisfaction: >90%

---

## 11. Test Data Management

### 11.1 Test Data Structure

```
tests/
├── fixtures/
│   ├── documents/
│   │   ├── ai_ethics_paper.pdf          # 247KB, known content
│   │   ├── resume_sample.pdf            # 89KB, known content
│   │   ├── oxford_notes.txt             # 15KB, known content
│   │   ├── corrupted.pdf                # Intentionally corrupted
│   │   └── encrypted.pdf                # Password protected
│   ├── screenshots/
│   │   ├── clear_text.png               # High OCR confidence
│   │   ├── code_snippet.png             # Code text
│   │   ├── infographic.png              # Visual content
│   │   ├── handwriting.png              # Low OCR confidence
│   │   ├── blank.png                    # Empty image
│   │   └── corrupted.png                # Corrupted image
│   ├── notes/
│   │   └── sample_notes.json            # Apple Notes format
│   ├── database/
│   │   ├── empty.db                     # Empty schema
│   │   ├── small.db                     # 100 nodes
│   │   ├── medium.db                    # 1,000 nodes
│   │   └── large.db                     # 10,000 nodes
│   └── api/
│       ├── graph_response.json          # Sample API responses
│       ├── search_response.json
│       └── analytics_response.json
└── generators/
    ├── generate_test_files.py           # Create synthetic test files
    ├── generate_test_database.py        # Populate test databases
    └── generate_test_screenshots.py     # Create test screenshots
```

### 11.2 Test Data Generators

**Generate Test Files:**
```python
def generate_test_directory(num_files=100, output_dir="tests/data/generated"):
    """
    Generate directory with realistic test files
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for i in range(num_files):
        # Mix of file types
        if i % 10 == 0:
            # PDF document
            create_sample_pdf(
                output_dir / f"document_{i}.pdf",
                content=f"Sample document {i} about AI ethics and machine learning."
            )
        elif i % 10 == 1:
            # Screenshot
            create_sample_screenshot(
                output_dir / f"screenshot_{i}.png",
                text=f"Screenshot {i}: Oxford AI Programme"
            )
        else:
            # Text file
            (output_dir / f"notes_{i}.txt").write_text(
                f"Sample notes {i}\nAI Ethics\nMachine Learning\nOxford"
            )
```

**Generate Test Database:**
```python
def populate_test_database(db_path, num_nodes=1000):
    """
    Create database with known test data
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Load schema
    with open("src/database/schema.sql") as f:
        cursor.executescript(f.read())

    # Insert test nodes
    for i in range(num_nodes):
        cursor.execute("""
            INSERT INTO nodes (id, file_name, type, date_created, primary_tags)
            VALUES (?, ?, ?, ?, ?)
        """, (
            f"node-{i}",
            f"file{i}.pdf",
            random.choice(['document', 'screenshot', 'note']),
            fake.date_between(start_date='-1y'),
            json.dumps(random.sample(['ai-ethics', 'oxford', 'career', 'research'], 2))
        ))

    # Insert test edges
    for i in range(num_nodes * 5):
        source = f"node-{random.randint(0, num_nodes-1)}"
        target = f"node-{random.randint(0, num_nodes-1)}"

        if source != target:
            cursor.execute("""
                INSERT INTO edges (id, source, target, weight, type)
                VALUES (?, ?, ?, ?, ?)
            """, (
                f"edge-{i}",
                source,
                target,
                random.uniform(0.5, 1.0),
                random.choice(['content-similarity', 'temporal', 'hierarchical'])
            ))

    conn.commit()
    conn.close()
```

### 11.3 Real User Data Testing

**With User Permission:**
```python
@pytest.mark.real_data
@pytest.mark.skip(reason="Requires user permission and real data")
def test_with_real_user_data():
    """
    Test with actual user data (run manually with consent)
    """
    # Use a copy of real database
    real_db = Path.home() / "Library/Application Support/knowledge_map/knowledge_graph_copy.db"

    if not real_db.exists():
        pytest.skip("Real data not available")

    # Run tests with real data
    db = DatabaseConnection(real_db)
    results = db.search("oxford")

    # Verify results make sense
    assert len(results) > 0
    assert all('oxford' in r['primary_tags'] for r in results)
```

---

## 12. Continuous Integration

### 12.1 Pre-Commit Hooks

**Setup (.git/hooks/pre-commit):**
```bash
#!/bin/bash
# Pre-commit hook: Run tests before allowing commit

echo "Running pre-commit checks..."

# 1. Run linter
echo "Running linter..."
pylint src/
if [ $? -ne 0 ]; then
    echo "❌ Linting failed. Fix issues before committing."
    exit 1
fi

# 2. Run unit tests
echo "Running unit tests..."
pytest tests/unit -q
if [ $? -ne 0 ]; then
    echo "❌ Unit tests failed. Fix tests before committing."
    exit 1
fi

# 3. Check coverage
echo "Checking coverage..."
pytest --cov=src --cov-fail-under=80 -q
if [ $? -ne 0 ]; then
    echo "❌ Coverage below 80%. Add tests before committing."
    exit 1
fi

echo "✅ Pre-commit checks passed!"
```

### 12.2 CI/CD Pipeline

**GitHub Actions Full Pipeline:**
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: pip install pylint
      - name: Lint
        run: pylint src/

  unit-tests:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run unit tests
        run: pytest tests/unit -v --cov=src --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v2
        with:
          files: ./coverage.xml

  integration-tests:
    runs-on: ubuntu-latest
    needs: unit-tests
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest
      - name: Run integration tests
        run: pytest tests/integration -v

  e2e-tests:
    runs-on: ubuntu-latest
    needs: integration-tests
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest selenium
      - name: Start Flask server
        run: |
          python src/app.py &
          sleep 10
      - name: Run E2E tests
        run: pytest tests/e2e -v

  performance-tests:
    runs-on: ubuntu-latest
    needs: e2e-tests
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-benchmark
      - name: Run performance tests
        run: pytest tests/performance -v --benchmark-only
```

### 12.3 Test Reporting

**Coverage Report:**
- View in browser: `open htmlcov/index.html`
- Coverage badge in README
- Weekly coverage trends tracked

**Test Results Dashboard:**
- Number of tests passing/failing
- Test execution time trends
- Flaky test detection
- Coverage trends over time

---

## Conclusion

This comprehensive testing plan ensures quality through:

1. **Multi-layered testing** - Unit, integration, E2E, performance
2. **Continuous self-checking** - Validate at every implementation step
3. **Automated coverage** - 80%+ code coverage with automated tests
4. **Real-world validation** - Test with actual user data and workflows
5. **Performance benchmarks** - Meet defined speed and resource targets
6. **Continuous integration** - Automated testing on every commit

**The answer to "How are you gonna check yourself?" is:**
- Write tests first (or immediately after) for every function
- Run self-checks at every implementation milestone
- Use validation gates before moving to next phase
- Automate all tests for continuous verification
- Measure against defined success criteria
- Test with real data before production deployment

**Result:** High confidence that the system works correctly, performs well, and meets user needs.

---

**Status:** ✅ Complete and ready for implementation

**Last Updated:** 2025-10-09

**Related Documents:**
- 01_PRODUCT_REQUIREMENTS.md (success criteria)
- 12_SYSTEM_ARCHITECTURE.md (components to test)
- 08_BACKGROUND_JOBS.md (job testing)

---

**Next Steps:**
1. Review and approve testing plan
2. Set up testing infrastructure (pytest, fixtures, CI)
3. Begin implementation with test-first approach
4. Track test coverage and quality metrics throughout development
