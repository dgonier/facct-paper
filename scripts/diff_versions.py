#!/usr/bin/env python3
"""
Diff and manage paper versions for FAccT submission.

Usage:
    # List all versions
    python diff_versions.py --list

    # Add new version from Google Doc export
    python diff_versions.py --add path/to/new_export.md

    # Diff two versions (shows what changed)
    python diff_versions.py --diff v1 v2

    # Generate detailed change report
    python diff_versions.py --report v1 v2

    # Show sections that changed between versions
    python diff_versions.py --sections v1 v2
"""

import argparse
import difflib
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

VERSIONS_DIR = Path(__file__).parent.parent / "versions"
SECTIONS_DIR = Path(__file__).parent.parent / "sections"


def list_versions():
    """List all saved versions."""
    versions = sorted(VERSIONS_DIR.glob("v*_*.md"))
    if not versions:
        print("No versions found.")
        return []

    print("Available versions:")
    print("-" * 60)
    for v in versions:
        # Extract version info from filename
        name = v.stem
        parts = name.split("_", 2)
        version = parts[0]
        date = parts[1] if len(parts) > 1 else "unknown"
        label = parts[2] if len(parts) > 2 else ""

        size = v.stat().st_size
        print(f"  {version:5} | {date:10} | {label:20} | {size:,} bytes")

    return versions


def add_version(source_path: Path, label: str = None):
    """Add a new version from a markdown file."""
    if not source_path.exists():
        print(f"Error: Source file not found: {source_path}")
        sys.exit(1)

    # Find next version number
    existing = sorted(VERSIONS_DIR.glob("v*_*.md"))
    if existing:
        last_version = existing[-1].stem.split("_")[0]
        version_num = int(last_version[1:]) + 1
    else:
        version_num = 1

    # Create new filename
    date_str = datetime.now().strftime("%Y-%m-%d")
    label = label or "update"
    new_name = f"v{version_num}_{date_str}_{label}.md"
    dest_path = VERSIONS_DIR / new_name

    shutil.copy(source_path, dest_path)
    print(f"Added new version: {new_name}")

    # Show what changed from previous version
    if existing:
        print("\nChanges from previous version:")
        diff_versions(existing[-1].stem.split("_")[0], f"v{version_num}")

    return dest_path


def get_version_path(version_id: str) -> Path:
    """Get the path for a version identifier (e.g., 'v1' or 'v2')."""
    matches = list(VERSIONS_DIR.glob(f"{version_id}_*.md"))
    if not matches:
        print(f"Error: Version {version_id} not found")
        sys.exit(1)
    return matches[0]


def diff_versions(v1_id: str, v2_id: str, context_lines: int = 3):
    """Show diff between two versions."""
    v1_path = get_version_path(v1_id)
    v2_path = get_version_path(v2_id)

    with open(v1_path) as f:
        v1_lines = f.readlines()
    with open(v2_path) as f:
        v2_lines = f.readlines()

    diff = difflib.unified_diff(
        v1_lines, v2_lines,
        fromfile=v1_path.name,
        tofile=v2_path.name,
        lineterm='',
        n=context_lines
    )

    diff_output = list(diff)
    if not diff_output:
        print("No differences found.")
        return

    # Color output if terminal supports it
    for line in diff_output:
        if line.startswith('+') and not line.startswith('+++'):
            print(f"\033[92m{line}\033[0m", end='')  # Green
        elif line.startswith('-') and not line.startswith('---'):
            print(f"\033[91m{line}\033[0m", end='')  # Red
        elif line.startswith('@@'):
            print(f"\033[96m{line}\033[0m", end='')  # Cyan
        else:
            print(line, end='')


def extract_sections(content: str) -> dict:
    """Extract sections from markdown content."""
    sections = {}
    current_section = "preamble"
    current_content = []

    for line in content.split('\n'):
        # Check for section headers (## or ###)
        if re.match(r'^#{1,3}\s+\**\d*\.?\d*\s*', line):
            if current_content:
                sections[current_section] = '\n'.join(current_content)
            current_section = line.strip()
            current_content = [line]
        else:
            current_content.append(line)

    if current_content:
        sections[current_section] = '\n'.join(current_content)

    return sections


def section_diff(v1_id: str, v2_id: str):
    """Show which sections changed between versions."""
    v1_path = get_version_path(v1_id)
    v2_path = get_version_path(v2_id)

    with open(v1_path) as f:
        v1_sections = extract_sections(f.read())
    with open(v2_path) as f:
        v2_sections = extract_sections(f.read())

    all_sections = set(v1_sections.keys()) | set(v2_sections.keys())

    print(f"Section changes: {v1_id} -> {v2_id}")
    print("-" * 60)

    for section in sorted(all_sections):
        v1_content = v1_sections.get(section, "")
        v2_content = v2_sections.get(section, "")

        if section not in v1_sections:
            print(f"  [NEW]     {section[:50]}")
        elif section not in v2_sections:
            print(f"  [REMOVED] {section[:50]}")
        elif v1_content != v2_content:
            # Calculate change magnitude
            v1_words = len(v1_content.split())
            v2_words = len(v2_content.split())
            diff_pct = abs(v2_words - v1_words) / max(v1_words, 1) * 100
            print(f"  [CHANGED] {section[:40]} ({diff_pct:+.0f}% words)")
        else:
            print(f"  [same]    {section[:50]}")


def generate_report(v1_id: str, v2_id: str):
    """Generate a detailed change report for updating LaTeX."""
    v1_path = get_version_path(v1_id)
    v2_path = get_version_path(v2_id)

    with open(v1_path) as f:
        v1_content = f.read()
    with open(v2_path) as f:
        v2_content = f.read()

    v1_sections = extract_sections(v1_content)
    v2_sections = extract_sections(v2_content)

    print("=" * 70)
    print(f"CHANGE REPORT: {v1_id} -> {v2_id}")
    print("=" * 70)
    print()

    # Map sections to LaTeX files
    section_to_latex = {
        "introduction": "01_introduction.tex",
        "accountability": "02_related_work.tex",
        "related work": "02_related_work.tex",
        "foam approach": "03_foam_approach.tex",
        "case study": "04_case_study.tex",
        "empirical": "05_evaluation.tex",
        "evaluation": "05_evaluation.tex",
        "implications": "06_implications.tex",
        "limitations": "07_limitations.tex",
        "conclusion": "08_conclusion.tex",
    }

    changed_latex_files = set()

    for section in v2_sections:
        v1_content = v1_sections.get(section, "")
        v2_content = v2_sections.get(section, "")

        if v1_content != v2_content:
            # Find matching LaTeX file
            section_lower = section.lower()
            for key, latex_file in section_to_latex.items():
                if key in section_lower:
                    changed_latex_files.add(latex_file)
                    break

    print("LaTeX files that need updating:")
    for f in sorted(changed_latex_files):
        print(f"  - sections/{f}")

    print("\nDetailed changes by section:")
    print("-" * 70)

    for section in sorted(set(v1_sections.keys()) | set(v2_sections.keys())):
        v1_text = v1_sections.get(section, "")
        v2_text = v2_sections.get(section, "")

        if v1_text != v2_text:
            print(f"\n### {section}")
            # Show condensed diff
            v1_lines = v1_text.split('\n')
            v2_lines = v2_text.split('\n')

            differ = difflib.Differ()
            diff = list(differ.compare(v1_lines[:50], v2_lines[:50]))  # Limit for readability

            for line in diff:
                if line.startswith('+ '):
                    print(f"\033[92m{line[:100]}\033[0m")
                elif line.startswith('- '):
                    print(f"\033[91m{line[:100]}\033[0m")


def main():
    parser = argparse.ArgumentParser(description="Manage paper versions for FAccT")
    parser.add_argument("--list", "-l", action="store_true", help="List all versions")
    parser.add_argument("--add", "-a", type=Path, help="Add new version from file")
    parser.add_argument("--label", type=str, default=None, help="Label for new version")
    parser.add_argument("--diff", "-d", nargs=2, metavar=("V1", "V2"), help="Diff two versions")
    parser.add_argument("--sections", "-s", nargs=2, metavar=("V1", "V2"), help="Show section changes")
    parser.add_argument("--report", "-r", nargs=2, metavar=("V1", "V2"), help="Generate change report")

    args = parser.parse_args()

    VERSIONS_DIR.mkdir(exist_ok=True)

    if args.list:
        list_versions()
    elif args.add:
        add_version(args.add, args.label)
    elif args.diff:
        diff_versions(args.diff[0], args.diff[1])
    elif args.sections:
        section_diff(args.sections[0], args.sections[1])
    elif args.report:
        generate_report(args.report[0], args.report[1])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
