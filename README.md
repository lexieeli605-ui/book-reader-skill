# Book Reader Skill for QoderWork

A QoderWork skill that turns any book or article into a structured reading report with auto-roleplay dialogue — no prompt copy-paste needed.

## Features

- **Multi-format input**: PDF, EPUB, DOCX, TXT, Markdown, HTML, and web URLs
- **Concept extraction**: Distills core ideas, key arguments, and unique insights
- **Character & perspective analysis**: Identifies key figures, relationships, beliefs, and decision patterns (for fiction and non-fiction alike)
- **Auto-roleplay dialogue**: After generating a report, simply ask questions — the AI automatically adopts the appropriate book character's or author's perspective, language style, and knowledge boundaries
- **3 dialogue modes**:
  - *Character roleplay* — biographies and novels (e.g., speak as Zeng Guofan, Steve Jobs)
  - *Author perspective* — non-fiction and thought books (e.g., think like the author of *Factfulness*)
  - *Philosophical framework* — philosophy and allegory (e.g., answer using the wisdom of *Siddhartha*)
- **5 HTML themes**: apple-modern, classical-chinese, warm-memoir, literary-novel, dark-dramatic — auto-selected based on book content
- **Single-file HTML output**: Clean, responsive report with smooth animations, zero external dependencies

## Installation

### Option 1: Install via .skill file

Download the `book-reader.skill` file from [Releases](../../releases) and click "Save skill" in QoderWork.

### Option 2: Manual install

Copy the skill directory to your QoderWork skills folder:

```bash
cp -r . ~/.qoderwork/skills/book-reader/
```

Then install the Python dependencies:

```bash
pip install pdfplumber ebooklib beautifulsoup4 python-docx lxml
```

## Usage

### Generate a reading report

In QoderWork, simply say:

> "帮我读一下这本书，生成阅读报告"

Provide a book file (PDF, EPUB, etc.) or a URL. The skill will:

1. Parse the content and extract metadata
2. Auto-select the best HTML theme for the book's genre
3. Generate a concept summary with key ideas
4. Identify core characters/perspectives with relationship maps
5. Create dialogue topics with language markers (self-reference, verbal tics, topic keywords)
6. Save context for auto-roleplay (`.book_context.json`)
7. Output a polished HTML reading report

### Talk to the book

After the report is generated, just ask questions directly:

> "一个读书人去带兵打仗，最大的困难是什么？"

The AI automatically detects which book was just read and responds in character — no prompt needed. It matches your question to the most relevant character, applies their language style and knowledge boundaries, and stays in character throughout the conversation.

## Output

The generated HTML report includes:

- **Hero section** with book cover, title, author, and one-liner summary
- **Core Ideas** section with numbered insight cards
- **Characters** section with expandable cards showing traits, beliefs, and relationships
- **Dialogue** section with topic cards and guiding questions

See [`examples/`](examples/) for sample outputs.

## Project Structure

```
book-reader/
├── SKILL.md                    # Skill definition and workflow
├── html-design-reference.md    # 5-theme HTML/CSS template reference
├── scripts/
│   └── parse_input.py          # Universal document parser
└── examples/
    └── steve-jobs-report.html  # Sample output (apple-modern theme)
```

## Requirements

- Python 3.8+
- Dependencies: `pdfplumber`, `ebooklib`, `beautifulsoup4`, `python-docx`, `lxml`

## License

MIT
