#!/usr/bin/env python3
"""Offline structural validation for surf-guide."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [
        ROOT / item.decode("utf-8")
        for item in result.stdout.split(b"\0")
        if item
    ]


def validate_markdown_links(files: list[Path]) -> None:
    link_re = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in link_re.finditer(line):
                target = match.group(1).strip().strip("<>")
                if not target or target.startswith("#"):
                    continue
                parsed = urllib.parse.urlparse(target)
                if parsed.scheme or target.startswith("//"):
                    continue
                path_part = urllib.parse.unquote(target.split("#", 1)[0])
                if not path_part:
                    continue
                resolved = (
                    ROOT / path_part.lstrip("/")
                    if path_part.startswith("/")
                    else path.parent / path_part
                )
                if not resolved.exists():
                    rel = path.relative_to(ROOT)
                    error(f"{rel}:{line_number}: broken local link: {target}")


def validate_csv(path: Path) -> None:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    if not rows:
        error(f"{path.relative_to(ROOT)}: empty CSV")
        return
    width = len(rows[0])
    for row_number, row in enumerate(rows[1:], start=2):
        if len(row) != width:
            error(
                f"{path.relative_to(ROOT)}:{row_number}: "
                f"{len(row)} columns; expected {width}"
            )


def source_ids(path: Path) -> set[int]:
    ids: set[int] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"\|\s*S(\d+)\s*\|", line)
        if match:
            ids.add(int(match.group(1)))
    return ids


def referenced_source_ids(value: str) -> set[int]:
    ids = {int(value) for value in re.findall(r"\bS(\d+)\b", value)}
    for start, end in re.findall(r"\bS(\d+)\s*[–-]\s*S?(\d+)\b", value):
        lower, upper = sorted((int(start), int(end)))
        ids.update(range(lower, upper + 1))
    return ids


def validate_location_packs() -> None:
    required_fields = (
        "Slug:",
        "Approximate coordinates:",
        "Orientation:",
        "Wave type / bottom:",
        "Exposure class:",
        "Supported swell:",
        "Supported wind:",
        "Tide:",
        "Sections and skill:",
        "Hazards:",
        "Access:",
        "Crowd/localism:",
        "Confidence:",
        "Evidence label:",
        "Sources:",
    )
    for readme in sorted(ROOT.glob("locations/*/*/README.md")):
        if "_template" in readme.parts:
            continue
        sources_path = readme.with_name("sources.md")
        calibration_path = readme.with_name("calibration.md")
        if not sources_path.exists():
            error(f"{readme.relative_to(ROOT)}: missing sources.md")
            continue
        if not calibration_path.exists():
            error(f"{readme.relative_to(ROOT)}: missing calibration.md")
        available_ids = source_ids(sources_path)
        if not available_ids:
            error(f"{sources_path.relative_to(ROOT)}: no source IDs")

        text = readme.read_text(encoding="utf-8")
        headings = list(re.finditer(r"^### (.+)$", text, re.MULTILINE))
        if not headings:
            error(f"{readme.relative_to(ROOT)}: no spot headings")
            continue
        used_ids: set[int] = set()
        for index, heading in enumerate(headings):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
            block = text[heading.end() : end]
            spot = heading.group(1)
            for field in required_fields:
                if f"- {field}" not in block:
                    error(
                        f"{readme.relative_to(ROOT)}: "
                        f"{spot!r} missing field {field}"
                    )
            source_line = next(
                (line for line in block.splitlines() if line.startswith("- Sources:")),
                "",
            )
            referenced = referenced_source_ids(source_line)
            used_ids.update(referenced)
            missing = referenced - available_ids
            if missing:
                labels = ", ".join(f"S{item}" for item in sorted(missing))
                error(
                    f"{readme.relative_to(ROOT)}: "
                    f"{spot!r} references missing {labels}"
                )
        unused = available_ids - used_ids
        if unused:
            labels = ", ".join(f"S{item}" for item in sorted(unused))
            error(f"{sources_path.relative_to(ROOT)}: unused source IDs: {labels}")


def validate_public_privacy() -> None:
    patterns = {
        "email address": re.compile(
            r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE
        ),
        "rider weight": re.compile(r"\b\d{2,3}\s*kg\b", re.IGNORECASE),
        "rider height": re.compile(r"\b1\d{2}\s*cm\b", re.IGNORECASE),
        "exact accommodation": re.compile(r"\bexact accommodation\b", re.IGNORECASE),
        "seller phone": re.compile(r"\bseller phone\b", re.IGNORECASE),
        "rental booking": re.compile(r"\brental booking reference\b", re.IGNORECASE),
        "raw session": re.compile(r"\braw session row\b", re.IGNORECASE),
    }
    paths = list(ROOT.glob("locations/*/*/*.md")) + list((ROOT / "scan").glob("*.md"))
    for path in paths:
        if "_template" in path.parts:
            continue
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for label, pattern in patterns.items():
                if pattern.search(line):
                    error(
                        f"{path.relative_to(ROOT)}:{line_number}: "
                        f"possible private {label}"
                    )


def validate_local_private_data() -> None:
    data = ROOT / "data"
    if not (data / "active-location.md").exists():
        return

    legacy_patterns = {
        "removed trip tree": re.compile(r"`?trips/sagres-2026"),
        "renamed forecast method": re.compile(r"method/forecast-api-mechanics\.md"),
        "renamed flight method": re.compile(r"method/flight-api\.md"),
        "bare legacy forecast file": re.compile(r"(?<!method/)forecast-sources\.md"),
        "legacy beach file": re.compile(r"sagres-2026-beaches\.md"),
        "legacy board history": re.compile(r"surfboards\.txt"),
        "removed Beachcams path": re.compile(r"~/Documents/Surf/Beachcams"),
    }
    archive = data / "archive"
    for path in data.rglob("*.md"):
        if archive in path.parents:
            continue
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for label, pattern in legacy_patterns.items():
                if pattern.search(line):
                    error(
                        f"{path.relative_to(ROOT)}:{line_number}: "
                        f"{label}: {pattern.pattern}"
                    )

    for path in data.rglob("*.csv"):
        if archive not in path.parents:
            validate_csv(path)


def main() -> int:
    files = tracked_files()
    validate_markdown_links(files)
    for path in files:
        if path.suffix.lower() == ".csv":
            validate_csv(path)
    validate_location_packs()
    validate_public_privacy()
    validate_local_private_data()

    if ERRORS:
        for message in ERRORS:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1
    print("Extended validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
