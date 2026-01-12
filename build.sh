#!/bin/bash
# Build script for the FOAM FAccT paper
# Usage: ./build.sh [clean]

set -e

PAPER_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PAPER_DIR"

# Clean option
if [ "$1" == "clean" ]; then
    echo "Cleaning build artifacts..."
    rm -f main.aux main.bbl main.blg main.log main.out main.pdf main.toc main.lof main.lot
    rm -f sections/*.aux
    rm -f *.synctex.gz
    echo "Done."
    exit 0
fi

echo "=========================================="
echo "Building FOAM Paper (FAccT 2026)"
echo "=========================================="

# Check for pdflatex
if ! command -v pdflatex &> /dev/null; then
    echo "ERROR: pdflatex not found. Install texlive:"
    echo "  sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended"
    exit 1
fi

# First pass - generates .aux files
echo "[1/4] Running pdflatex (first pass)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 || true

# BibTeX pass - processes citations
echo "[2/4] Running bibtex..."
bibtex main > /dev/null 2>&1 || true

# Second pass - incorporates bibliography
echo "[3/4] Running pdflatex (second pass)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 || true

# Third pass - resolves references
echo "[4/4] Running pdflatex (final pass)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 || true

# Check if PDF was created
if [ -f "main.pdf" ]; then
    echo "=========================================="
    echo "SUCCESS: main.pdf created"
    echo "Size: $(du -h main.pdf | cut -f1)"
    echo "=========================================="
else
    echo "=========================================="
    echo "ERROR: PDF not created. Check main.log for errors:"
    echo "  grep -A5 '!' main.log"
    echo "=========================================="
    exit 1
fi
