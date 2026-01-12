# FOAM Paper - FAccT 2026 Submission

## Directory Structure

```
facct/
├── main.tex                 # Main LaTeX document
├── references.bib           # Bibliography
├── FACCT_2026_GUIDELINES.md # Submission requirements
├── sections/                # LaTeX section files
│   ├── 01_introduction.tex
│   ├── 02_related_work.tex
│   ├── 03_foam_approach.tex
│   ├── 04_case_study.tex
│   ├── 05_evaluation.tex
│   ├── 06_implications.tex
│   ├── 07_limitations.tex
│   └── 08_conclusion.tex
├── versions/                # Markdown versions from Google Docs
│   └── v1_2025-01-12_baseline.md
├── figures/                 # Figures directory
└── scripts/                 # Utility scripts
    └── diff_versions.py
```

## Workflow: Google Doc → LaTeX Updates

### 1. Export New Version from Google Docs

Export as Markdown (.md) from Google Docs.

### 2. Add to Version Tracking

```bash
cd paper/facct
python scripts/diff_versions.py --add path/to/new_export.md --label "google-doc-update"
```

### 3. See What Changed

```bash
# List all versions
python scripts/diff_versions.py --list

# See section-level changes
python scripts/diff_versions.py --sections v1 v2

# Generate detailed change report
python scripts/diff_versions.py --report v1 v2

# Full diff
python scripts/diff_versions.py --diff v1 v2
```

### 4. Update LaTeX Files

The report shows which `sections/*.tex` files need updating:

```
LaTeX files that need updating:
  - sections/03_foam_approach.tex
  - sections/05_evaluation.tex
```

Edit those files to incorporate the changes.

### 5. Build PDF

```bash
# Using latexmk (recommended)
latexmk -pdf main.tex

# Or manually
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

## Key Dates (FAccT 2026)

| Deadline | Date |
|----------|------|
| Abstract | January 8, 2026 |
| Paper | January 13, 2026 |
| Rebuttal | February 24, 2026 |
| Camera-ready | May 11, 2026 |
| Conference | June 25-28, 2026 |

## Requirements

- **14 pages max** (excluding references)
- **Anonymized** for review
- ACM TAPS format

## Current Version

The LaTeX files are based on `v1_2025-01-12_baseline.md`.
Each section file has a comment indicating which version it was updated from.
