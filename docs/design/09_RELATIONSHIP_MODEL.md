# Relationship Model Design Document
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Draft

---

## Overview

The knowledge graph connects nodes (files, notes, events) through **weighted, typed relationships** that capture HOW and WHY artifacts are connected. Each relationship includes:
- **Weight:** 0.0-1.0 indicating strength/relevance
- **Type:** Category of relationship (content, temporal, hierarchical, etc.)
- **WHY:** Array of reasons explaining the connection
- **Metadata:** Creation date, modification date, user confirmations

---

## Relationship Types

### 1. Content Similarity (Type: `content_similarity`)

**What it means:** Documents share similar topics, keywords, or concepts.

**Weight calculation:**
```python
# Cosine similarity of TF-IDF vectors
from sklearn.metrics.pairwise import cosine_similarity

def calculate_content_weight(doc1_vector, doc2_vector):
    similarity = cosine_similarity([doc1_vector], [doc2_vector])[0][0]
    # similarity ranges 0.0-1.0, use directly as weight
    return round(similarity, 3)

# Example:
# "Machine Learning Ethics.pdf" ↔ "AI Bias Research.md"
# Weight: 0.852 (high content overlap)
```

**WHY field examples:**
```json
{
  "type": "content_similarity",
  "weight": 0.852,
  "why": [
    "shared_tags: ['machine-learning', 'ethics', 'ai']",
    "shared_entities: ['neural networks', 'bias detection', 'fairness metrics']",
    "semantic_similarity: 0.852"
  ]
}
```

**Detection method:**
1. Extract tags and entities from both documents
2. Compute TF-IDF vectors for full text
3. Calculate cosine similarity
4. Create relationship if similarity > 0.5

---

### 2. Temporal (Type: `temporal`)

**What it means:** Documents worked on during the same time period.

**Weight calculation:**
```python
from datetime import datetime, timedelta

def calculate_temporal_weight(date1, date2):
    """
    Same day: 1.0
    Same week: 0.8
    Same month: 0.5
    Same quarter: 0.3
    Beyond: 0.0
    """
    delta = abs((date1 - date2).days)

    if delta == 0:
        return 1.0
    elif delta <= 7:
        return 0.8
    elif delta <= 30:
        return 0.5
    elif delta <= 90:
        return 0.3
    else:
        return 0.0

# Example:
# "Lecture Notes 2025-10-08.md" ↔ "Essay Draft 2025-10-09.md"
# Weight: 1.0 (same day, likely part of same work session)
```

**WHY field examples:**
```json
{
  "type": "temporal",
  "weight": 1.0,
  "why": [
    "worked_same_day: 2025-10-08",
    "session_overlap: true",
    "time_gap_hours: 2"
  ]
}
```

**Detection method:**
1. Daily scan identifies files modified on same date
2. Compare modification timestamps from filesystem
3. Group files by work sessions (same-day clusters)
4. Create temporal relationships within clusters

---

### 3. Hierarchical (Type: `hierarchical`)

**What it means:** Parent-child, part-of, derived-from relationships.

**Weight calculation:**
```python
def calculate_hierarchical_weight(relationship_subtype):
    """
    Direct parent/child: 1.0
    Derived from: 0.9
    Part of collection: 0.7
    Related chapter: 0.6
    """
    weights = {
        "parent_child": 1.0,
        "derived_from": 0.9,
        "part_of": 0.7,
        "related_chapter": 0.6
    }
    return weights.get(relationship_subtype, 0.5)

# Example:
# "Oxford Thesis/" (folder) ↔ "Chapter 1 Draft.md" (file)
# Weight: 1.0 (direct parent-child)
```

**WHY field examples:**
```json
{
  "type": "hierarchical",
  "weight": 1.0,
  "why": [
    "folder_structure: parent_child",
    "path: /Oxford Thesis/Chapter 1 Draft.md",
    "hierarchy_level: 1"
  ]
}
```

**Detection method:**
1. Parse file paths to detect folder hierarchies
2. Detect "Chapter X" patterns in filenames
3. Identify "v2", "draft", "final" version chains
4. Track file renames/moves in change log

---

### 4. Cross-Domain (Type: `cross_domain`)

**What it means:** **High-value bridges** connecting disparate knowledge areas.

**Weight calculation:**
```python
def calculate_cross_domain_weight(doc1_tags, doc2_tags):
    """
    High-value if documents from different domains
    share specific overlapping concepts.
    """
    domain1 = get_primary_domain(doc1_tags)
    domain2 = get_primary_domain(doc2_tags)

    if domain1 == domain2:
        return 0.0  # Not cross-domain

    # Check for shared secondary tags (bridging concepts)
    shared = set(doc1_tags) & set(doc2_tags)
    shared_count = len(shared)

    if shared_count >= 3:
        return 0.9  # Strong bridge
    elif shared_count == 2:
        return 0.7  # Moderate bridge
    elif shared_count == 1:
        return 0.5  # Weak bridge
    else:
        return 0.0

# Example:
# "Machine Learning Paper.pdf" [ai, ethics] ↔
# "Business Ethics Case Study.md" [business, ethics]
# Weight: 0.7 (ethics bridges AI and business domains)
```

**WHY field examples:**
```json
{
  "type": "cross_domain",
  "weight": 0.7,
  "why": [
    "bridge_concept: ethics",
    "domain1: artificial-intelligence",
    "domain2: business-strategy",
    "opportunity: Apply ML ethics frameworks to business decision-making"
  ]
}
```

**Business value:**
- **Opportunity detection:** Find ways to apply knowledge from one domain to another
- **Gap identification:** Missing bridges suggest unexplored connections
- **Innovation potential:** High-weight cross-domain links = unique insights

**Detection method:**
1. Classify documents into primary domains using tags
2. Find documents with tags from multiple domains
3. Identify shared secondary concepts (bridge tags)
4. Create cross-domain relationships with high weights
5. Flag these relationships in analytics dashboard as "opportunities"

---

### 5. Manual (Type: `manual`)

**What it means:** User explicitly connected these documents.

**Weight calculation:**
```python
def calculate_manual_weight(user_input):
    """
    User-defined: use their specified weight
    User clicked "connect": default 0.8
    User added note: 0.9
    """
    if user_input.get("weight"):
        return user_input["weight"]
    elif user_input.get("note"):
        return 0.9
    else:
        return 0.8  # Default for simple click
```

**WHY field examples:**
```json
{
  "type": "manual",
  "weight": 0.9,
  "why": [
    "user_created: 2025-10-09",
    "user_note: This paper influenced my thesis methodology",
    "user_confirmed: true"
  ]
}
```

**Detection method:**
- UI provides "Connect" button on each node
- User selects target node and optionally adds note
- Relationship created with highest trust (user knows best)

---

### 6. Reference (Type: `reference`)

**What it means:** One document explicitly cites/mentions another.

**Weight calculation:**
```python
def calculate_reference_weight(citation_type):
    """
    Direct quote: 1.0
    Footnote citation: 0.9
    Bibliography entry: 0.8
    Filename mentioned: 0.6
    """
    weights = {
        "direct_quote": 1.0,
        "footnote": 0.9,
        "bibliography": 0.8,
        "filename_mention": 0.6
    }
    return weights.get(citation_type, 0.7)

# Example:
# "Thesis Chapter 2.md" contains: "See Figure 1 in research_data.xlsx"
# Weight: 0.6 (filename mention)
```

**WHY field examples:**
```json
{
  "type": "reference",
  "weight": 0.9,
  "why": [
    "citation_found: line 45",
    "citation_text: 'According to Smith (2024)...'",
    "reference_type: footnote"
  ]
}
```

**Detection method:**
1. Parse document text for filename patterns
2. Detect citation formats (footnotes, bibliography)
3. Find markdown links `[text](file.md)`
4. Extract URLs and file references

---

## WHY Field Structure

Every relationship MUST include a `why` array explaining the connection:

```json
{
  "source_id": "file_123",
  "target_id": "file_456",
  "type": "content_similarity",
  "weight": 0.823,
  "created_date": "2025-10-09",
  "modified_date": "2025-10-09",
  "user_confirmed": false,
  "why": [
    "shared_tags: ['machine-learning', 'ethics']",
    "shared_entities: ['bias detection', 'fairness']",
    "semantic_similarity: 0.823",
    "detection_method: tfidf_cosine"
  ],
  "metadata": {
    "auto_generated": true,
    "confidence": 0.85,
    "last_verified": "2025-10-09"
  }
}
```

**Why this matters:**
- **Transparency:** Users understand WHY connections exist
- **Debugging:** Easy to identify false positives
- **Learning:** System improves by analyzing which WHY patterns users confirm/reject

---

## Weight Decay and Reinforcement

### Decay Function (Temporal relationships)

```python
from datetime import datetime, timedelta

def apply_temporal_decay(relationship, current_date):
    """
    Temporal relationships weaken over time if not reinforced.
    Decay rate: -0.1 per 30 days
    """
    if relationship["type"] != "temporal":
        return relationship["weight"]

    created_date = datetime.fromisoformat(relationship["created_date"])
    days_elapsed = (current_date - created_date).days

    decay_rate = 0.1 / 30  # 0.1 per month
    decay_amount = decay_rate * days_elapsed

    new_weight = max(0.0, relationship["weight"] - decay_amount)
    return round(new_weight, 3)

# Example:
# Temporal relationship created 60 days ago with weight 0.8
# Decay: 0.8 - (0.1 / 30 * 60) = 0.8 - 0.2 = 0.6
```

### Reinforcement Function

```python
def reinforce_relationship(relationship, reinforcement_event):
    """
    Relationships strengthen when:
    - User views both files in same session
    - User confirms relationship
    - Files modified on same day again
    - New shared tags added

    Reinforcement: +0.1 per event, max 1.0
    """
    current_weight = relationship["weight"]
    boost = 0.1

    new_weight = min(1.0, current_weight + boost)

    # Log reinforcement in WHY field
    relationship["why"].append(
        f"reinforced: {reinforcement_event['type']} on {reinforcement_event['date']}"
    )

    relationship["modified_date"] = reinforcement_event["date"]
    relationship["weight"] = round(new_weight, 3)

    return relationship

# Example:
# User views "Paper A" and "Paper B" in same session
# Content similarity weight: 0.7 → 0.8
```

---

## Relationship Lifecycle

```
1. DETECTION
   ↓
   [Daily scan detects potential relationship]
   ↓
2. CREATION
   ↓
   [Relationship created with initial weight + WHY]
   ↓
3. USER REVIEW (optional)
   ↓
   [User confirms/rejects/ignores]
   ↓
4. REINFORCEMENT
   ↓
   [Weight increases with usage]
   ↓
5. DECAY (temporal only)
   ↓
   [Weight decreases if not used]
   ↓
6. PRUNING
   ↓
   [Relationships with weight < 0.3 archived]
```

---

## Pruning Strategy

**Monthly job** (see `08_BACKGROUND_JOBS.md`):
- Archive relationships with weight < 0.3
- Keep manual relationships regardless of weight
- Keep cross-domain relationships (high value)
- Log pruned relationships for potential restoration

```python
def prune_weak_relationships(db, threshold=0.3):
    """
    Archive relationships below threshold.
    Exception: manual, cross_domain always kept.
    """
    query = """
        UPDATE relationships
        SET archived = 1, archived_date = ?
        WHERE weight < ?
        AND type NOT IN ('manual', 'cross_domain')
        AND archived = 0
    """
    db.execute(query, (datetime.now().isoformat(), threshold))
    db.commit()
```

---

## Example: Multi-Type Relationships

Two documents can have MULTIPLE relationships:

```json
[
  {
    "source_id": "ethics_paper.pdf",
    "target_id": "thesis_chapter2.md",
    "type": "content_similarity",
    "weight": 0.85,
    "why": ["shared_tags: ['ethics', 'ai']"]
  },
  {
    "source_id": "ethics_paper.pdf",
    "target_id": "thesis_chapter2.md",
    "type": "reference",
    "weight": 1.0,
    "why": ["citation_found: line 127", "citation_text: 'According to Chen (2024)...'"]
  },
  {
    "source_id": "ethics_paper.pdf",
    "target_id": "thesis_chapter2.md",
    "type": "temporal",
    "weight": 0.8,
    "why": ["worked_same_week: 2025-10-05 to 2025-10-11"]
  }
]
```

**Aggregate weight for graph visualization:**
```python
def calculate_aggregate_weight(relationships):
    """Use highest weight among all relationship types."""
    return max(rel["weight"] for rel in relationships)
```

---

## SQL Schema (from 05_GRAPH_DATABASE_SCHEMA.md)

```sql
CREATE TABLE IF NOT EXISTS relationships (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL,
    target_id TEXT NOT NULL,
    type TEXT NOT NULL,
    weight REAL NOT NULL CHECK(weight >= 0.0 AND weight <= 1.0),
    created_date TEXT NOT NULL,
    modified_date TEXT NOT NULL,
    user_confirmed BOOLEAN DEFAULT 0,
    archived BOOLEAN DEFAULT 0,
    archived_date TEXT,
    why_json TEXT,  -- JSON array of reasons
    metadata_json TEXT,  -- JSON object
    FOREIGN KEY (source_id) REFERENCES nodes(id) ON DELETE CASCADE,
    FOREIGN KEY (target_id) REFERENCES nodes(id) ON DELETE CASCADE
);

CREATE INDEX idx_relationships_source ON relationships(source_id);
CREATE INDEX idx_relationships_target ON relationships(target_id);
CREATE INDEX idx_relationships_type ON relationships(type);
CREATE INDEX idx_relationships_weight ON relationships(weight DESC);
```

---

**Status:** ✅ Complete
