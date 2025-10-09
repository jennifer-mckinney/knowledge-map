# Auto-Tagging System Design
**Project:** knowledge_map v2.0
**Date:** 2025-10-09
**Status:** Draft

---

## Overview

The Auto-Tagging System is a dynamic, AI-powered content classification engine that automatically assigns meaningful tags to every file, note, and artifact in the knowledge graph. Unlike traditional keyword-based systems, it uses Claude API for intelligent semantic analysis combined with local NLP fallback to ensure privacy and reliability.

**Key Principles:**
- **Dynamic, not hard-coded**: Tags are generated from content analysis, not predefined rules
- **AI-first**: Claude API provides semantic understanding and context awareness
- **Privacy-preserving**: Local NLP fallback when user opts out of cloud AI
- **Learning system**: Improves accuracy from user corrections over time
- **Content + Context**: Analyzes both file content and surrounding context (time, location, related files)

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT: NEW FILE                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              CONTENT EXTRACTION                              │
│  • PDF → Text (PyPDF2)                                      │
│  • Images → OCR (Tesseract/Apple Vision)                   │
│  • Documents → Text (python-docx, textract)                │
│  • Screenshots → OCR + metadata                             │
│  • Notes → Title + body                                     │
│  • Metadata → Filename, dates, size, location              │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              CONTEXT GATHERING                               │
│  • Recent calendar events (past 7 days)                    │
│  • Location analysis (folder path, nearby files)           │
│  • Temporal context (creation date, day of week)           │
│  • Related files (same folder, same project)               │
│  • User correction history (learning data)                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              AI TAGGING (CLAUDE API)                         │
│  • Semantic content analysis                                │
│  • Entity extraction (people, places, orgs, topics)        │
│  • Intent classification (learning, work, reference)       │
│  • Document type detection                                  │
│  • Context-aware tag generation                             │
│  • Primary (1-3) + Secondary (unlimited) + Keywords        │
│                                                              │
│  IF API unavailable → Fallback to LOCAL NLP                │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              LOCAL NLP FALLBACK                              │
│  • spaCy NER (named entity recognition)                    │
│  • TF-IDF keyword extraction (scikit-learn)                │
│  • Topic modeling (LDA or LSA)                              │
│  • Rule-based classification (patterns, extensions)        │
│  • Filename heuristics                                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              TAG VALIDATION & REFINEMENT                     │
│  • Enforce 1-3 primary tags                                 │
│  • Normalize tag format (lowercase, hyphens)               │
│  • Remove duplicates                                         │
│  • Apply user preferences/corrections                       │
│  • Generate confidence scores                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              LEARNING SYSTEM UPDATE                          │
│  • Store tags + confidence + reasoning                      │
│  • Track user corrections                                    │
│  • Update correction history                                 │
│  • Adjust future tagging based on patterns                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              OUTPUT: TAGGED NODE                             │
│  {                                                           │
│    primary_tags: [1-3 tags],                                │
│    secondary_tags: [unlimited],                             │
│    keywords: [auto-extracted],                              │
│    confidence: 0.0-1.0,                                      │
│    method: "claude-api" | "local-nlp",                      │
│    reasoning: "why these tags"                              │
│  }                                                           │
└─────────────────────────────────────────────────────────────┘
```

---

## Claude API Integration

### When to Call Claude API

**Automatic Calls:**
1. New file discovered in daily scan
2. Existing file modified (content changed)
3. User requests re-tagging
4. OCR completes on screenshot
5. Apple Note synced/updated

**Skip API Calls:**
1. User opted out of cloud AI (use local NLP)
2. API quota exceeded (fallback to local)
3. File type has no extractable content (empty files)
4. File unchanged since last tag

### API Request Format

```json
{
  "model": "claude-3-5-sonnet-20241022",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Analyze this content and generate tags.\n\n**Filename:** screenshot_2025-10-05.png\n**Location:** /Desktop\n**Created:** 2025-10-05 14:32\n**Recent Calendar:** Meeting with Oxford AI Programme cohort\n**File Type:** Screenshot (image)\n\n**OCR Content:**\n\"10 Essential AI Ethics Frameworks\n1. Fairness\n2. Transparency\n3. Accountability...\"\n\n**Instructions:**\n- Provide 1-3 primary tags (main topics)\n- Provide secondary tags (descriptors, context)\n- Extract keywords\n- Format: lowercase, hyphens for multi-word\n- Explain reasoning\n\nReturn JSON:\n{\n  \"primary_tags\": [],\n  \"secondary_tags\": [],\n  \"keywords\": [],\n  \"reasoning\": \"\"\n}"
    }
  ]
}
```

### API Response Handling

```python
def parse_claude_response(response):
    """Extract tags from Claude API response"""
    try:
        # Parse JSON from response
        data = json.loads(response['content'][0]['text'])

        # Validate structure
        assert 1 <= len(data['primary_tags']) <= 3
        assert all(isinstance(tag, str) for tag in data['primary_tags'])

        # Normalize tags
        primary = [normalize_tag(t) for t in data['primary_tags']]
        secondary = [normalize_tag(t) for t in data.get('secondary_tags', [])]
        keywords = [normalize_tag(k) for k in data.get('keywords', [])]

        return {
            'primary_tags': primary,
            'secondary_tags': secondary,
            'keywords': keywords,
            'confidence': 0.9,  # High confidence from Claude
            'method': 'claude-api',
            'reasoning': data.get('reasoning', '')
        }
    except Exception as e:
        logging.warning(f"Claude API parsing failed: {e}")
        return None  # Trigger local NLP fallback
```

### API Error Handling

```python
def call_claude_api(content, context):
    """Call Claude API with retry logic"""
    try:
        # Attempt API call
        response = anthropic_client.messages.create(...)
        return parse_claude_response(response)

    except anthropic.RateLimitError:
        logging.warning("Rate limit hit, using local NLP")
        return None  # Fallback to local

    except anthropic.APIError as e:
        logging.error(f"API error: {e}")
        return None  # Fallback to local

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None  # Fallback to local
```

---

## Local NLP Fallback

When Claude API is unavailable, the system uses local NLP libraries for privacy-preserving tagging.

### Components

**1. spaCy NLP Pipeline**
```python
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """Extract named entities and topics"""
    doc = nlp(text)

    entities = {
        'people': [ent.text for ent in doc.ents if ent.label_ == 'PERSON'],
        'orgs': [ent.text for ent in doc.ents if ent.label_ == 'ORG'],
        'topics': [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'EVENT', 'WORK_OF_ART']],
        'dates': [ent.text for ent in doc.ents if ent.label_ == 'DATE']
    }

    return entities
```

**2. TF-IDF Keyword Extraction**
```python
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, corpus, top_n=10):
    """Extract important keywords using TF-IDF"""
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')

    # Add current text to corpus for comparison
    texts = corpus + [text]
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Get keywords for current document
    feature_names = vectorizer.get_feature_names_out()
    doc_vector = tfidf_matrix[-1].toarray()[0]

    # Sort by TF-IDF score
    top_indices = doc_vector.argsort()[-top_n:][::-1]
    keywords = [feature_names[i] for i in top_indices if doc_vector[i] > 0]

    return keywords
```

**3. Topic Modeling (LDA)**
```python
from sklearn.decomposition import LatentDirichletAllocation

def classify_topic(text, lda_model, vectorizer):
    """Classify document into topic categories"""
    # Transform text to document-term matrix
    doc_term_matrix = vectorizer.transform([text])

    # Get topic distribution
    topic_dist = lda_model.transform(doc_term_matrix)[0]

    # Map to predefined topic labels
    topic_labels = ['research', 'career', 'education', 'technical', 'personal']
    primary_topic = topic_labels[topic_dist.argmax()]

    return primary_topic
```

**4. Rule-Based Classification**
```python
def classify_by_rules(filename, file_path, content):
    """Apply heuristic rules for common patterns"""
    tags = []

    # File extension rules
    if filename.endswith('.pdf'):
        if 'oxford' in content.lower():
            tags.append('oxford')
        if 'resume' in filename.lower() or 'cv' in filename.lower():
            tags.append('career')

    # Screenshot detection
    if filename.startswith('Screenshot'):
        tags.append('screenshot')

    # Path-based rules
    if 'career' in file_path.lower():
        tags.append('career')
    if 'education' in file_path.lower():
        tags.append('education')

    # Content patterns
    if re.search(r'machine learning|neural network|deep learning', content, re.I):
        tags.append('ai-ml')

    return tags
```

### Local Tagging Pipeline

```python
def tag_with_local_nlp(file_info, content, context):
    """Full local NLP tagging pipeline"""

    # Extract entities
    entities = extract_entities(content)

    # Extract keywords
    keywords = extract_keywords(content, corpus=context.get('recent_files', []))

    # Classify topic
    primary_topic = classify_topic(content, lda_model, vectorizer)

    # Apply rules
    rule_tags = classify_by_rules(file_info['name'], file_info['path'], content)

    # Combine and rank
    all_tags = entities['topics'] + rule_tags + [primary_topic]
    tag_scores = rank_tags(all_tags, content)

    # Select top 1-3 for primary
    primary_tags = [tag for tag, score in tag_scores[:3] if score > 0.3]
    secondary_tags = [tag for tag, score in tag_scores[3:] if score > 0.2]

    return {
        'primary_tags': primary_tags,
        'secondary_tags': secondary_tags,
        'keywords': keywords[:20],
        'confidence': 0.6,  # Lower confidence for local NLP
        'method': 'local-nlp',
        'reasoning': f'Local NLP: topic={primary_topic}, entities={len(entities)}'
    }
```

---

## Content Extraction Methods

### PDF Documents

```python
import PyPDF2

def extract_pdf_content(file_path):
    """Extract text from PDF"""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages[:10]:  # First 10 pages for performance
                text += page.extract_text()
            return text.strip()
    except Exception as e:
        logging.error(f"PDF extraction failed: {e}")
        return ''
```

### Images & Screenshots (OCR)

```python
from PIL import Image
import pytesseract

def extract_image_text(file_path):
    """Extract text from image using OCR"""
    try:
        img = Image.open(file_path)

        # Preprocess for better OCR
        img = img.convert('L')  # Grayscale

        # Run OCR
        text = pytesseract.image_to_string(img, lang='eng')

        return text.strip()
    except Exception as e:
        logging.error(f"OCR failed: {e}")
        return ''
```

### Word Documents

```python
from docx import Document

def extract_docx_content(file_path):
    """Extract text from Word document"""
    try:
        doc = Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        logging.error(f"DOCX extraction failed: {e}")
        return ''
```

### Apple Notes

```python
import sqlite3

def extract_note_content(note_id, notes_db_path):
    """Extract content from Apple Notes database"""
    try:
        conn = sqlite3.connect(notes_db_path)
        cursor = conn.cursor()

        query = """
        SELECT
            ZICCLOUDSYNCINGOBJECT.ZTITLE1 as title,
            ZICCLOUDSYNCINGOBJECT.ZSNIPPET as snippet,
            datetime(ZICCLOUDSYNCINGOBJECT.ZCREATIONDATE + 978307200, 'unixepoch') as created
        FROM ZICCLOUDSYNCINGOBJECT
        WHERE Z_ENT = 9 AND ZTITLE1 IS NOT NULL
        AND ZICCLOUDSYNCINGOBJECT.Z_PK = ?
        """

        cursor.execute(query, (note_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return f"{row[0]}\n{row[1]}"
        return ''
    except Exception as e:
        logging.error(f"Note extraction failed: {e}")
        return ''
```

### Plain Text Files

```python
def extract_text_content(file_path):
    """Extract content from plain text files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Try with different encoding
        with open(file_path, 'r', encoding='latin-1') as f:
            return f.read()
    except Exception as e:
        logging.error(f"Text extraction failed: {e}")
        return ''
```

---

## Context Analysis

### Temporal Context

```python
def get_temporal_context(file_date):
    """Analyze temporal patterns for tagging"""
    context = {
        'day_of_week': file_date.strftime('%A'),
        'time_of_day': 'morning' if file_date.hour < 12 else 'afternoon' if file_date.hour < 18 else 'evening',
        'month': file_date.strftime('%B'),
        'year': file_date.year
    }

    # Check for work hours (likely professional content)
    if 9 <= file_date.hour <= 17 and file_date.weekday() < 5:
        context['likely_work'] = True

    return context
```

### Location Context

```python
def get_location_context(file_path):
    """Analyze file location for context"""
    path_parts = Path(file_path).parts

    context = {
        'root_location': 'icloud' if 'iCloud' in str(file_path) else 'local',
        'folder_hints': [],
        'parent_folder': Path(file_path).parent.name
    }

    # Extract hints from path
    for part in path_parts:
        if part.lower() in ['career', 'education', 'research', 'personal']:
            context['folder_hints'].append(part.lower())

    return context
```

### Recent Calendar Context

```python
def get_calendar_context(file_date):
    """Get recent calendar events for context"""
    # Query calendar events within 7 days
    recent_events = query_calendar_events(
        start_date=file_date - timedelta(days=7),
        end_date=file_date
    )

    context = {
        'recent_events': [e['title'] for e in recent_events],
        'recent_attendees': [a for e in recent_events for a in e['attendees']],
        'event_topics': extract_topics([e['title'] for e in recent_events])
    }

    return context
```

### Related Files Context

```python
def get_related_files_context(file_path):
    """Find related files in same location"""
    parent_dir = Path(file_path).parent

    # Get sibling files
    siblings = [f for f in parent_dir.glob('*') if f.is_file() and f != file_path]

    # Get their tags (if already processed)
    related_tags = []
    for sibling in siblings[:10]:  # Limit to 10 for performance
        node = get_node_by_path(str(sibling))
        if node:
            related_tags.extend(node.get('primary_tags', []))

    # Find common themes
    tag_counts = Counter(related_tags)
    common_tags = [tag for tag, count in tag_counts.most_common(5) if count > 1]

    return {
        'related_files': len(siblings),
        'common_tags': common_tags
    }
```

---

## Tag Generation Rules

### Primary Tags (1-3 Required)

**Selection Criteria:**
1. **Specificity**: Prefer specific over general (`ai-ethics` > `ai`)
2. **Relevance**: Directly related to main content
3. **Actionability**: Useful for search and organization
4. **Consistency**: Use existing tags when appropriate

**Format Rules:**
- Lowercase only
- Hyphens for multi-word (`product-management`, not `product_management`)
- No special characters
- Maximum 25 characters
- Singular form preferred (`document`, not `documents`)

**Examples:**
```json
{
  "file": "Oxford AI Ethics Framework.pdf",
  "primary_tags": ["ai-ethics", "oxford", "research"]
}

{
  "file": "Resume_Jennifer_McKinney_2025.pdf",
  "primary_tags": ["career", "resume"]
}

{
  "file": "Screenshot_AI_tips.png",
  "primary_tags": ["ai-ml", "learning", "screenshot"]
}
```

### Secondary Tags (Unlimited, Optional)

**Purpose:**
- Additional descriptors
- Quality indicators
- Source attribution
- Format/type information

**Categories:**
1. **Descriptors**: `infographic`, `quote`, `tutorial`, `reference`, `summary`
2. **Quality**: `important`, `draft`, `archive`, `needs-review`, `favorite`
3. **Source**: `social-media`, `website`, `textbook`, `conference`, `blog`
4. **Status**: `in-progress`, `completed`, `pending`, `reviewed`

**Examples:**
```json
{
  "primary_tags": ["ai-ethics", "research"],
  "secondary_tags": ["infographic", "important", "social-media"]
}
```

### Keywords (Unlimited, Automatic)

**Extraction Method:**
1. TF-IDF keyword extraction (top 20)
2. Named entities (people, places, organizations)
3. Technical terms
4. Frequently mentioned concepts

**Not Used For:**
- Primary organization (too granular)
- Display (too many)
- Manual selection by user

**Purpose:**
- Full-text search enhancement
- Relationship detection
- Analytics and insights

**Example:**
```json
{
  "keywords": [
    "machine-learning", "fairness", "transparency", "bias",
    "neural-networks", "accountability", "ethics", "framework",
    "privacy", "data-governance", "explainability", "regulation"
  ]
}
```

---

## Learning System

The system improves tagging accuracy over time by learning from user corrections.

### Correction Tracking

```python
class CorrectionHistory:
    """Track user corrections to improve tagging"""

    def __init__(self, db_path):
        self.db_path = db_path
        self.corrections = self.load_corrections()

    def record_correction(self, file_path, original_tags, corrected_tags, file_content):
        """Store user correction"""
        correction = {
            'timestamp': datetime.now().isoformat(),
            'file_path': file_path,
            'original': original_tags,
            'corrected': corrected_tags,
            'content_snippet': file_content[:500],  # First 500 chars
            'file_type': Path(file_path).suffix
        }

        self.corrections.append(correction)
        self.save_corrections()

    def get_similar_corrections(self, content, file_type):
        """Find similar past corrections"""
        similar = []

        for correction in self.corrections:
            if correction['file_type'] == file_type:
                # Calculate content similarity
                similarity = calculate_similarity(
                    content[:500],
                    correction['content_snippet']
                )

                if similarity > 0.7:
                    similar.append(correction)

        return similar
```

### Learning Application

```python
def apply_learning(tags, file_info, content, correction_history):
    """Apply learned corrections to new tags"""

    # Find similar past corrections
    similar = correction_history.get_similar_corrections(
        content,
        Path(file_info['path']).suffix
    )

    if not similar:
        return tags  # No learning to apply

    # Analyze correction patterns
    patterns = analyze_correction_patterns(similar)

    # Apply learned patterns
    for pattern in patterns:
        if pattern['trigger'] in content.lower():
            # User frequently changes X to Y in this context
            if pattern['original_tag'] in tags['primary_tags']:
                tags['primary_tags'].remove(pattern['original_tag'])
                tags['primary_tags'].append(pattern['corrected_tag'])

    return tags
```

### Confidence Adjustment

```python
def adjust_confidence(tags, correction_history):
    """Adjust confidence based on correction history"""

    # Start with base confidence
    confidence = tags['confidence']

    # Check if similar files were corrected before
    correction_rate = correction_history.get_correction_rate(
        tags['primary_tags']
    )

    # Lower confidence if these tags are frequently corrected
    if correction_rate > 0.3:  # 30% correction rate
        confidence *= 0.7

    # Higher confidence if tags match learned patterns
    if correction_history.matches_pattern(tags['primary_tags']):
        confidence *= 1.2

    tags['confidence'] = min(1.0, max(0.1, confidence))
    return tags
```

---

## Example Tagging Scenarios

### Scenario 1: Oxford AI Ethics Screenshot

**Input:**
```
File: Screenshot_2025-10-05_14-32-08.png
Path: /Users/jennifer/Desktop
Created: 2025-10-05 14:32
Size: 2.3 MB
```

**Content Extraction (OCR):**
```
"10 Essential AI Ethics Frameworks
1. Fairness - Ensure equal treatment
2. Transparency - Explainable decisions
3. Accountability - Clear responsibility
4. Privacy - Protect personal data
5. Security - Safeguard systems
..."
```

**Context:**
```
Recent Calendar: "Oxford AI Programme - Module 3" (2025-10-05 10:00-12:00)
Location: Desktop (pending organization)
Time: 14:32 (afternoon, weekday, work hours)
Related Files: Oxford_Module3_Notes.pdf, AI_Ethics_Reading.pdf
```

**Claude API Tags:**
```json
{
  "primary_tags": ["ai-ethics", "oxford", "screenshot"],
  "secondary_tags": ["infographic", "learning", "framework", "reference"],
  "keywords": [
    "fairness", "transparency", "accountability", "privacy",
    "security", "ethics", "framework", "ai-governance"
  ],
  "confidence": 0.95,
  "method": "claude-api",
  "reasoning": "Screenshot of AI ethics framework, clearly related to Oxford AI Programme based on calendar context and content. Educational reference material."
}
```

**Organization Decision:**
```
Destination: /iCloud/Documents/Education/Oxford_AI_Programme/Module_3_Ethics/
Reason: Primary tag 'oxford' + folder structure match
```

---

### Scenario 2: Career Document (Resume)

**Input:**
```
File: Resume_Jennifer_McKinney_2025_Product_Manager.pdf
Path: /Users/jennifer/Downloads
Created: 2025-10-03 09:15
Size: 156 KB
```

**Content Extraction:**
```
"JENNIFER MCKINNEY
Product Manager | AI/ML Specialist

EXPERIENCE
Senior Product Manager, Amazon (2020-2023)
- Led AI-powered recommendation system
- Managed cross-functional team of 12
...

EDUCATION
Oxford Artificial Intelligence Programme (2024-2025)
..."
```

**Context:**
```
Recent Calendar: "Amazon Interview Prep" (2025-10-02 15:00)
Location: Downloads (default download location)
Time: 09:15 (morning, weekday, work hours)
Related Files: Cover_Letter_Amazon.pdf, Amazon_JD.pdf
```

**Claude API Tags:**
```json
{
  "primary_tags": ["career", "resume"],
  "secondary_tags": ["product-management", "important", "current"],
  "keywords": [
    "amazon", "product-manager", "ai-ml", "oxford",
    "senior", "recommendation-system", "cross-functional"
  ],
  "confidence": 0.98,
  "method": "claude-api",
  "reasoning": "Resume document for product management role, clearly career-related. Recent Amazon interview calendar event suggests active job search."
}
```

**Organization Decision:**
```
Destination: /iCloud/Documents/Career_Professional/Job_Search_2025/Amazon/
Reason: Primary tag 'career' + context (Amazon interview) + filename
```

---

### Scenario 3: Research Note (Apple Notes)

**Input:**
```
Note: "Meeting Notes - Sarah (Oxford)"
Created: 2025-10-04 11:30
Location: Apple Notes / Work folder
```

**Content Extraction:**
```
"Meeting with Sarah from Oxford cohort

Discussed thesis ideas:
- AI bias in hiring systems
- Fairness metrics comparison
- Industry applications

Action items:
- Read Barocas paper on fairness
- Draft thesis outline by next week
- Schedule follow-up
"
```

**Context:**
```
Recent Calendar: "Coffee with Sarah - Thesis Discussion" (2025-10-04 11:00)
Location: Apple Notes (synced from iPhone)
Time: 11:30 (late morning, weekday)
Related Files: None found
```

**Claude API Tags:**
```json
{
  "primary_tags": ["oxford", "research", "meeting-notes"],
  "secondary_tags": ["thesis", "ai-ethics", "fairness", "action-items"],
  "keywords": [
    "sarah", "bias", "hiring", "fairness-metrics",
    "barocas", "thesis", "industry-applications"
  ],
  "confidence": 0.92,
  "method": "claude-api",
  "reasoning": "Meeting notes from Oxford cohort discussion about thesis research on AI fairness. Calendar event confirms meeting with Sarah. Research-oriented content."
}
```

**Organization Decision:**
```
Destination: Virtual organization only (Apple Notes stay in place)
Links: Connect to Oxford_AI_Programme folder, any files tagged 'thesis'
```

---

### Scenario 4: Technical Document (No Clear Context)

**Input:**
```
File: document.pdf
Path: /Users/jennifer/Desktop
Created: 2025-10-01 22:45
Size: 4.2 MB
```

**Content Extraction:**
```
"Neural Network Architectures
Convolutional Neural Networks (CNNs)
CNNs are designed for processing grid-like data...

Recurrent Neural Networks (RNNs)
RNNs handle sequential data...

Transformer Architecture
Self-attention mechanisms..."
```

**Context:**
```
Recent Calendar: None relevant
Location: Desktop (pending organization)
Time: 22:45 (late evening, weekday)
Related Files: None obvious
```

**Local NLP Tags (API unavailable):**
```json
{
  "primary_tags": ["ai-ml", "technical"],
  "secondary_tags": ["neural-networks", "reference", "deep-learning"],
  "keywords": [
    "cnn", "rnn", "transformer", "architecture",
    "self-attention", "convolutional", "recurrent", "sequential-data"
  ],
  "confidence": 0.65,
  "method": "local-nlp",
  "reasoning": "Local NLP detected technical AI/ML content about neural network architectures. No clear context from calendar or location. Generic filename suggests needs manual review."
}
```

**Organization Decision:**
```
Destination: /iCloud/Documents/Education/Technical_References/AI_ML/
Reason: Primary tag 'ai-ml' + technical content
Flag: Low confidence, suggest manual review
```

---

## Tag Normalization

```python
def normalize_tag(tag):
    """Standardize tag format"""
    # Convert to lowercase
    tag = tag.lower().strip()

    # Replace spaces/underscores with hyphens
    tag = re.sub(r'[\s_]+', '-', tag)

    # Remove special characters
    tag = re.sub(r'[^a-z0-9-]', '', tag)

    # Remove multiple consecutive hyphens
    tag = re.sub(r'-+', '-', tag)

    # Remove leading/trailing hyphens
    tag = tag.strip('-')

    # Apply synonym mapping
    synonym_map = {
        'machine-learning': 'ai-ml',
        'artificial-intelligence': 'ai',
        'pm': 'product-management'
    }
    tag = synonym_map.get(tag, tag)

    return tag
```

---

## Performance Considerations

### Batch Processing

```python
def batch_tag_files(file_list, batch_size=50):
    """Process files in batches for efficiency"""

    results = []

    for i in range(0, len(file_list), batch_size):
        batch = file_list[i:i+batch_size]

        # Extract content in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            contents = list(executor.map(extract_content, batch))

        # Tag files (sequential for API rate limits)
        for file_info, content in zip(batch, contents):
            tags = tag_file(file_info, content)
            results.append(tags)

        # Brief pause to avoid rate limits
        time.sleep(1)

    return results
```

### Caching

```python
class TagCache:
    """Cache tags to avoid re-processing unchanged files"""

    def get_cached_tags(self, file_path, file_hash):
        """Check if file tags are cached"""
        cache_key = f"{file_path}:{file_hash}"
        return self.cache.get(cache_key)

    def cache_tags(self, file_path, file_hash, tags):
        """Store tags in cache"""
        cache_key = f"{file_path}:{file_hash}"
        self.cache[cache_key] = {
            'tags': tags,
            'timestamp': datetime.now().isoformat()
        }
```

---

## Success Metrics

**Tagging Accuracy:**
- Target: >90% user acceptance without correction
- Measure: Correction rate from user feedback

**Performance:**
- Target: <2 seconds per file (including API call)
- Target: <5 minutes for daily scan of 100 new files

**API Usage:**
- Target: <$1/day in API costs (~100 files)
- Fallback: Local NLP when quota exceeded

**Learning Improvement:**
- Target: 10% reduction in correction rate per month
- Measure: Track correction frequency over time

---

**Status:** Ready for implementation
