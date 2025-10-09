# Analytics Queries Design Document
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Draft

---

## Overview

This document contains SQL queries and analytics logic for extracting insights from the knowledge graph. Each query answers a specific user question and includes:
- **Question:** What the user wants to know
- **SQL Query:** Complete executable SQL
- **Expected Output:** Sample results
- **Visualization:** How to display results in UI
- **Insight:** What this reveals about user's work

---

## Query 1: What Am I Good At? (Strength Detection)

### Question
"What topics do I have the most knowledge depth in?"

### SQL Query
```sql
-- Find tags with most connected high-quality artifacts
WITH tag_stats AS (
    SELECT
        t.tag,
        COUNT(DISTINCT nt.node_id) as artifact_count,
        AVG(n.word_count) as avg_depth,
        SUM(CASE WHEN n.word_count > 1000 THEN 1 ELSE 0 END) as substantial_docs,
        COUNT(DISTINCT r.target_id) as connection_count,
        MAX(n.date_modified) as recent_activity
    FROM tags t
    JOIN node_tags nt ON t.id = nt.tag_id
    JOIN nodes n ON nt.node_id = n.id
    LEFT JOIN relationships r ON n.id = r.source_id AND r.weight > 0.5
    WHERE nt.is_primary = 1
    GROUP BY t.tag
    HAVING artifact_count >= 3
)
SELECT
    tag,
    artifact_count,
    ROUND(avg_depth, 0) as avg_words,
    substantial_docs,
    connection_count,
    recent_activity,
    -- Strength score: weighted combination
    ROUND(
        (artifact_count * 0.3) +
        (substantial_docs * 0.4) +
        (connection_count * 0.3),
        2
    ) as strength_score
FROM tag_stats
ORDER BY strength_score DESC
LIMIT 20;
```

### Expected Output
```
tag                  | artifact_count | avg_words | substantial_docs | connection_count | recent_activity | strength_score
---------------------|----------------|-----------|------------------|------------------|-----------------|---------------
machine-learning     | 24             | 1850      | 18               | 45               | 2025-10-08      | 27.3
ethics               | 19             | 2200      | 15               | 38               | 2025-10-09      | 22.5
data-visualization   | 12             | 1200      | 8                | 22               | 2025-10-05      | 13.2
oxford-thesis        | 8              | 3500      | 8                | 15               | 2025-10-09      | 9.9
```

### Visualization
**Bubble chart:**
- X-axis: `artifact_count` (number of documents)
- Y-axis: `avg_words` (depth per document)
- Bubble size: `strength_score`
- Bubble color: Recency (bright = recent activity, dim = old)
- Label: `tag` name

### Insight
"You have **deep expertise** in machine learning (24 documents, 18 substantial) and ethics (19 documents). Recent activity in oxford-thesis shows this is your current focus area."

---

## Query 2: What Opportunities Am I Missing? (Cross-Domain Bridges)

### Question
"What knowledge from one domain could I apply to another?"

### SQL Query
```sql
-- Find cross-domain relationships with high weights
WITH domain_pairs AS (
    SELECT
        r.id as relationship_id,
        r.source_id,
        r.target_id,
        r.weight,
        r.why_json,
        -- Get primary tags (domains) for each node
        (SELECT t.tag FROM node_tags nt
         JOIN tags t ON nt.tag_id = t.id
         WHERE nt.node_id = r.source_id AND nt.is_primary = 1
         LIMIT 1) as source_domain,
        (SELECT t.tag FROM node_tags nt
         JOIN tags t ON nt.tag_id = t.id
         WHERE nt.node_id = r.target_id AND nt.is_primary = 1
         LIMIT 1) as target_domain,
        -- Get file names
        (SELECT title FROM nodes WHERE id = r.source_id) as source_file,
        (SELECT title FROM nodes WHERE id = r.target_id) as target_file
    FROM relationships r
    WHERE r.type = 'cross_domain'
    AND r.weight > 0.5
    AND r.archived = 0
)
SELECT
    source_domain,
    target_domain,
    COUNT(*) as bridge_count,
    MAX(weight) as strongest_connection,
    GROUP_CONCAT(source_file || ' ↔ ' || target_file, '; ') as examples
FROM domain_pairs
WHERE source_domain != target_domain
GROUP BY source_domain, target_domain
ORDER BY bridge_count DESC, strongest_connection DESC
LIMIT 10;
```

### Expected Output
```
source_domain        | target_domain        | bridge_count | strongest_connection | examples
---------------------|----------------------|--------------|----------------------|------------------------------------------
machine-learning     | business-strategy    | 5            | 0.87                 | ML Paper ↔ Business Ethics; AI Ethics ↔ Startup Strategy
data-visualization   | education            | 3            | 0.75                 | D3.js Tutorial ↔ Teaching Methods
ethics               | law                  | 2            | 0.69                 | AI Bias Paper ↔ Legal Framework
```

### Visualization
**Network diagram (subset of main graph):**
- Show only cross-domain relationships with weight > 0.5
- Color nodes by primary domain
- Edge thickness = weight
- Highlight clusters with 3+ bridges (hot opportunities)

**Insight card:**
```
💡 OPPORTUNITY DETECTED
You have ML expertise AND business strategy knowledge.
Bridge: "ethics" concept
Potential: Apply ML fairness frameworks to business decision-making.
5 existing connections suggest this is viable.
```

### Insight
"You have **5 connections** between ML and business strategy, bridged by ethics concepts. This suggests an opportunity to develop business applications of ML ethics frameworks."

---

## Query 3: Where Are My Knowledge Gaps? (Missing Connections)

### Question
"What areas have documents but no connections?"

### SQL Query
```sql
-- Find nodes with few relationships (potential orphans)
WITH node_connection_counts AS (
    SELECT
        n.id,
        n.title,
        n.type,
        n.date_created,
        n.word_count,
        -- Get primary tag
        (SELECT t.tag FROM node_tags nt
         JOIN tags t ON nt.tag_id = t.id
         WHERE nt.node_id = n.id AND nt.is_primary = 1
         LIMIT 1) as primary_tag,
        -- Count relationships
        (SELECT COUNT(*) FROM relationships r
         WHERE (r.source_id = n.id OR r.target_id = n.id)
         AND r.weight > 0.5
         AND r.archived = 0) as connection_count
    FROM nodes n
    WHERE n.archived = 0
)
SELECT
    primary_tag,
    COUNT(*) as isolated_docs,
    GROUP_CONCAT(title, '; ') as examples,
    AVG(word_count) as avg_size
FROM node_connection_counts
WHERE connection_count < 2
AND word_count > 500  -- Exclude trivial files
GROUP BY primary_tag
HAVING isolated_docs >= 2
ORDER BY isolated_docs DESC
LIMIT 10;
```

### Expected Output
```
primary_tag          | isolated_docs | examples                                    | avg_size
---------------------|---------------|---------------------------------------------|----------
finance              | 7             | Investment Notes; Budget 2025; Tax Docs     | 1200
health               | 5             | Workout Log; Nutrition Plan; Medical Records | 850
travel               | 3             | Italy Itinerary; Flight Confirmations       | 600
```

### Visualization
**Bar chart:**
- X-axis: `primary_tag`
- Y-axis: `isolated_docs` (number of orphaned documents)
- Color: Red (gaps = problems)
- Click bar → show list of specific files

**Insight card:**
```
⚠️ KNOWLEDGE GAP DETECTED
Topic: finance
7 documents with minimal connections
Suggestion: These files exist but aren't integrated into your broader knowledge.
Action: Review and connect to related work (business, planning, etc.)
```

### Insight
"You have **7 finance-related documents** that aren't connected to other work. Consider linking these to business strategy or personal planning documents."

---

## Query 4: Time vs. Output Analysis

### Question
"Am I spending time effectively? High effort → high output?"

### SQL Query
```sql
-- Compare days_worked vs. word_count/connections
SELECT
    n.id,
    n.title,
    -- Get primary tag
    (SELECT t.tag FROM node_tags nt
     JOIN tags t ON nt.tag_id = t.id
     WHERE nt.node_id = n.id AND nt.is_primary = 1
     LIMIT 1) as primary_tag,
    n.days_worked,
    n.span_days,
    n.word_count,
    -- Count relationships
    (SELECT COUNT(*) FROM relationships r
     WHERE r.source_id = n.id AND r.weight > 0.5) as connection_count,
    -- Efficiency score: output per day worked
    ROUND(CAST(n.word_count AS FLOAT) / NULLIF(n.days_worked, 0), 0) as words_per_day,
    -- Flag inefficiency
    CASE
        WHEN n.days_worked >= 5 AND n.word_count < 1000 THEN 'LOW_OUTPUT'
        WHEN n.days_worked >= 5 AND connection_count < 3 THEN 'ISOLATED'
        WHEN n.span_days > 60 AND n.days_worked < 5 THEN 'ABANDONED'
        ELSE 'NORMAL'
    END as flag
FROM nodes n
WHERE n.type IN ('file', 'note')
AND n.days_worked > 0
ORDER BY n.days_worked DESC
LIMIT 20;
```

### Expected Output
```
title                    | primary_tag      | days_worked | span_days | word_count | connection_count | words_per_day | flag
-------------------------|------------------|-------------|-----------|------------|------------------|---------------|----------
Oxford Thesis Chapter 1  | oxford-thesis    | 12          | 45        | 8500       | 15               | 708           | NORMAL
ML Ethics Paper          | machine-learning | 8           | 22        | 4200       | 22               | 525           | NORMAL
Business Plan Draft      | business         | 6           | 30        | 800        | 2                | 133           | LOW_OUTPUT
Startup Ideas            | entrepreneurship | 3           | 90        | 500        | 1                | 167           | ABANDONED
```

### Visualization
**Scatter plot:**
- X-axis: `days_worked`
- Y-axis: `word_count`
- Dot size: `connection_count`
- Dot color: `flag` (red = LOW_OUTPUT, yellow = ABANDONED, green = NORMAL)
- Diagonal reference line: expected words per day

**Insight card:**
```
⚠️ INEFFICIENCY ALERT
Document: "Business Plan Draft"
Time invested: 6 days
Output: 800 words (133 words/day)
Expected: ~1500 words for 6 days
Possible issue: Blockers, unclear direction, or gathering research?
```

### Insight
"**Business Plan Draft** took 6 days but produced only 800 words. This suggests blockers or unclear direction. Compare to ML Ethics Paper (8 days, 4200 words) which was more efficient."

---

## Query 5: Recent Activity Summary (What Am I Working On?)

### Question
"What have I been focused on in the last week?"

### SQL Query
```sql
-- Files accessed/modified in last 7 days
WITH recent_files AS (
    SELECT
        n.id,
        n.title,
        n.type,
        n.date_modified,
        n.date_accessed,
        n.word_count,
        -- Get primary tag
        (SELECT t.tag FROM node_tags nt
         JOIN tags t ON nt.tag_id = t.id
         WHERE nt.node_id = n.id AND nt.is_primary = 1
         LIMIT 1) as primary_tag
    FROM nodes n
    WHERE (julianday('now') - julianday(n.date_accessed)) <= 7
    OR (julianday('now') - julianday(n.date_modified)) <= 7
)
SELECT
    primary_tag,
    COUNT(*) as active_files,
    SUM(word_count) as total_words,
    MAX(date_modified) as last_modified
FROM recent_files
GROUP BY primary_tag
ORDER BY active_files DESC, last_modified DESC;
```

### Expected Output
```
primary_tag          | active_files | total_words | last_modified
---------------------|--------------|-------------|---------------
oxford-thesis        | 8            | 15200       | 2025-10-09
machine-learning     | 5            | 6800        | 2025-10-08
data-visualization   | 3            | 2400        | 2025-10-07
```

### Visualization
**Timeline view:**
- Today at top, 7 days ago at bottom
- Horizontal bars for each file accessed/modified
- Color by primary_tag
- Bar length = word_count

**Summary card:**
```
📅 LAST 7 DAYS
Primary focus: oxford-thesis (8 files, 15.2k words)
Secondary: machine-learning (5 files)
Most recent: Oxford Thesis Chapter 3 (modified 1 hour ago)
```

### Insight
"You've been heavily focused on **oxford-thesis** this week (8 active files). ML work has continued but at lower intensity."

---

## Query 6: Project Time Investment (Tag-Level Summary)

### Question
"How much total time have I invested in this project?"

### SQL Query
```sql
-- Sum time metrics for all files with specific tag
SELECT
    t.tag,
    COUNT(DISTINCT n.id) as total_files,
    SUM(n.days_worked) as total_days_worked,
    SUM(n.word_count) as total_words,
    MIN(n.date_created) as project_start,
    MAX(n.date_modified) as last_activity,
    -- Average days per file
    ROUND(AVG(n.days_worked), 1) as avg_days_per_file,
    -- Total span from earliest to latest
    (julianday(MAX(n.date_modified)) - julianday(MIN(n.date_created))) as project_span_days
FROM tags t
JOIN node_tags nt ON t.id = nt.tag_id
JOIN nodes n ON nt.node_id = n.id
WHERE t.tag = 'oxford-thesis'  -- Replace with user-selected tag
AND n.type IN ('file', 'note')
GROUP BY t.tag;
```

### Expected Output
```
tag           | total_files | total_days_worked | total_words | project_start | last_activity | avg_days_per_file | project_span_days
--------------|-------------|-------------------|-------------|---------------|---------------|-------------------|-------------------
oxford-thesis | 15          | 47                | 28500       | 2025-08-01    | 2025-10-09    | 3.1               | 69
```

### Visualization
**Project dashboard card:**
```
📊 OXFORD THESIS PROJECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Started:     August 1, 2025
Duration:    69 days (2.3 months)
Files:       15 documents
Work days:   47 days (68% of span)
Output:      28,500 words
Avg/file:    3.1 days, 1,900 words
Last active: 1 hour ago
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Status: 🟢 ACTIVE
```

### Insight
"**Oxford thesis** project started 69 days ago. You've actively worked 47 of those days (68% engagement rate), producing 28.5k words across 15 files. High engagement suggests strong momentum."

---

## Query 7: Business Value Identification

### Question
"Which knowledge could I monetize or apply professionally?"

### SQL Query
```sql
-- Find high-quality, well-connected documents in valuable domains
WITH business_domains AS (
    SELECT tag FROM tags
    WHERE tag IN (
        'business', 'entrepreneurship', 'consulting',
        'data-analysis', 'machine-learning', 'web-development',
        'writing', 'design', 'marketing'
    )
),
valuable_nodes AS (
    SELECT
        n.id,
        n.title,
        n.type,
        n.word_count,
        t.tag as domain,
        -- Quality score
        CASE
            WHEN n.word_count > 2000 THEN 3
            WHEN n.word_count > 1000 THEN 2
            ELSE 1
        END as quality_score,
        -- Connection count
        (SELECT COUNT(*) FROM relationships r
         WHERE r.source_id = n.id AND r.weight > 0.5) as connection_count,
        n.date_modified
    FROM nodes n
    JOIN node_tags nt ON n.id = nt.node_id
    JOIN tags t ON nt.tag_id = t.id
    WHERE t.tag IN (SELECT tag FROM business_domains)
    AND n.word_count > 800
)
SELECT
    domain,
    title,
    word_count,
    connection_count,
    quality_score,
    -- Business value score
    ROUND(
        (quality_score * 0.5) +
        (connection_count * 0.3) +
        (CASE WHEN word_count > 2000 THEN 2 ELSE 1 END * 0.2),
        2
    ) as business_value_score,
    date_modified
FROM valuable_nodes
ORDER BY business_value_score DESC
LIMIT 15;
```

### Expected Output
```
domain               | title                          | word_count | connection_count | quality_score | business_value_score | date_modified
---------------------|--------------------------------|------------|------------------|---------------|----------------------|---------------
machine-learning     | ML Ethics Framework Paper      | 4500       | 18               | 3             | 8.2                  | 2025-10-08
data-visualization   | D3.js Interactive Tutorial     | 2800       | 12               | 3             | 6.7                  | 2025-10-05
business             | SaaS Pricing Strategy Guide    | 2200       | 8                | 3             | 5.3                  | 2025-09-28
```

### Visualization
**Business value matrix:**
- Quadrant chart
- X-axis: `quality_score` (content depth)
- Y-axis: `connection_count` (knowledge integration)
- Dot size: `word_count`
- Color: `domain`
- Label: `title`

**High-value quadrant (top-right):**
- Deep content + well-connected = **monetization ready**
- Suggest: Blog post, course, consulting service, portfolio piece

### Insight
"**ML Ethics Framework Paper** scores highest for business value (8.2/10). It's substantial (4.5k words), well-connected (18 relationships), and in a marketable domain. Consider publishing as blog series or course content."

---

## Query 8: Idle Files (What Should I Clean Up?)

### Question
"What files am I not using anymore?"

### SQL Query
```sql
-- Files not accessed in 90+ days with low connection counts
SELECT
    n.id,
    n.title,
    n.type,
    n.date_created,
    n.date_accessed,
    (julianday('now') - julianday(n.date_accessed)) as days_since_access,
    n.word_count,
    (SELECT COUNT(*) FROM relationships r
     WHERE (r.source_id = n.id OR r.target_id = n.id)
     AND r.weight > 0.5) as connection_count,
    (SELECT t.tag FROM node_tags nt
     JOIN tags t ON nt.tag_id = t.id
     WHERE nt.node_id = n.id AND nt.is_primary = 1
     LIMIT 1) as primary_tag
FROM nodes n
WHERE (julianday('now') - julianday(n.date_accessed)) > 90
AND n.archived = 0
AND n.type = 'file'
ORDER BY days_since_access DESC
LIMIT 20;
```

### Expected Output
```
title                    | days_since_access | word_count | connection_count | primary_tag
-------------------------|-------------------|------------|------------------|-------------
Old Project Notes 2024   | 187               | 450        | 0                | misc
Untitled Document        | 156               | 120        | 1                | misc
Draft Ideas              | 134               | 280        | 0                | brainstorming
```

### Visualization
**List view with actions:**
```
🗑️ CLEANUP SUGGESTIONS

Old Project Notes 2024
Last accessed: 187 days ago (Apr 2025)
Size: 450 words | Connections: 0
Action: [Archive] [Delete] [Review]

Untitled Document
Last accessed: 156 days ago (May 2025)
Size: 120 words | Connections: 1
Action: [Archive] [Delete] [Review]
```

### Insight
"You have **20 files** not accessed in 90+ days with minimal connections. These are candidates for archival or deletion to reduce clutter."

---

## Implementation Notes

### Query Performance
All queries use indexes from `05_GRAPH_DATABASE_SCHEMA.md`:
- `idx_nodes_date_modified`
- `idx_relationships_weight`
- `idx_node_tags_node_id`

Expected performance: **<100ms** for all queries on 10k nodes.

### Caching Strategy
- Cache query results for 1 hour (analytics don't need real-time)
- Invalidate cache when nodes/relationships modified
- Store cached results in `analytics_cache` table

### Frontend Integration
Each query returns JSON that maps directly to UI components:
- Tables → DataGrid component
- Charts → D3.js/Chart.js
- Cards → Material-UI Card components

---

**Status:** ✅ Complete
