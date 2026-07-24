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


def readable_text(path: Path) -> str | None:
    if not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None


def public_files(files: list[Path]) -> list[Path]:
    return [
        path
        for path in files
        if ROOT / "data" not in path.parents
    ]


def validate_credentials(files: list[Path]) -> None:
    patterns = {
        "GitHub token": re.compile(
            r"\b(?:ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]+)\b"
        ),
        "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
        "SerpAPI key": re.compile(
            r"\bSERPAPI_(?:API_)?KEY\s*=\s*[A-Za-z0-9_-]{20,}"
        ),
        "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    }
    for path in public_files(files):
        text = readable_text(path)
        if text is None:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in patterns.items():
                if pattern.search(line):
                    error(
                        f"{path.relative_to(ROOT)}:{line_number}: "
                        f"possible {label}"
                    )


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


def validate_source_table(path: Path) -> None:
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not re.match(r"^\|\s*S\d+\s*\|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 6:
            error(
                f"{path.relative_to(ROOT)}:{line_number}: "
                f"{len(cells)} source columns; expected 6"
            )
            continue
        url = urllib.parse.urlparse(cells[2])
        if url.scheme in {"http", "https"} and url.path in {"", "/"}:
            error(
                f"{path.relative_to(ROOT)}:{line_number}: "
                "source URL points only to a domain homepage"
            )
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[3]):
            error(
                f"{path.relative_to(ROOT)}:{line_number}: "
                "Retrieved must be an ISO date"
            )


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
        source_text = sources_path.read_text(encoding="utf-8")
        source_header = "| ID | Source | URL | Retrieved | Supports | Notes |"
        if source_header not in source_text:
            error(
                f"{sources_path.relative_to(ROOT)}: "
                "source table does not match the template columns"
            )
        validate_source_table(sources_path)
        if calibration_path.exists():
            calibration_text = calibration_path.read_text(encoding="utf-8")
            bias_header = (
                "| Source | Condition bucket | Observed bias | Adjustment | "
                "Observations | Independent contributors | Counterexamples | "
                "Confidence |"
            )
            if bias_header not in calibration_text:
                error(
                    f"{calibration_path.relative_to(ROOT)}: "
                    "source-bias table does not match the template columns"
                )
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


def validate_public_privacy(files: list[Path]) -> None:
    identity_patterns = {
        "email address": re.compile(
            r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE
        ),
        "rider weight": re.compile(r"\b\d{2,3}\s*kg\b", re.IGNORECASE),
        "rider height": re.compile(r"\b1\d{2}\s*cm\b", re.IGNORECASE),
    }
    sensitive_content_patterns = {
        "exact accommodation": re.compile(r"\bexact accommodation\b", re.IGNORECASE),
        "seller phone": re.compile(r"\bseller phone\b", re.IGNORECASE),
        "rental booking": re.compile(r"\brental booking reference\b", re.IGNORECASE),
        "raw session": re.compile(r"\braw session row\b", re.IGNORECASE),
    }
    for path in public_files(files):
        text = readable_text(path)
        if text is None:
            continue
        relative = path.relative_to(ROOT)
        patterns = dict(identity_patterns)
        is_location_pack = (
            len(relative.parts) >= 4
            and relative.parts[0] == "locations"
            and "_template" not in relative.parts
        )
        is_scan_catalog = bool(relative.parts and relative.parts[0] == "scan")
        if is_location_pack or is_scan_catalog:
            patterns.update(sensitive_content_patterns)
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in patterns.items():
                if pattern.search(line):
                    error(
                        f"{path.relative_to(ROOT)}:{line_number}: "
                        f"possible private {label}"
                    )


def validate_local_csvs() -> None:
    data = ROOT / "data"
    archive = data / "archive"
    for path in sorted(data.rglob("*.csv")):
        if archive not in path.parents:
            validate_csv(path)


def main() -> int:
    files = tracked_files()
    validate_credentials(files)
    validate_markdown_links(files)
    for path in files:
        if path.suffix.lower() == ".csv":
            validate_csv(path)
    validate_location_packs()
    validate_public_privacy(files)
    validate_local_csvs()

    if ERRORS:
        for message in ERRORS:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1
    print("Extended validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
