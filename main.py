"""Deterministic entry generator for the-joke-about-the-demo-20261123-0112."""

from __future__ import annotations

import os
from pathlib import Path

# Round 3 V3 Apex Champion (M8_stage_ceo_own, 95 Unicode code points, 10/10 glm-5.3-flash sweep).
ENTRY_TEXT = (
    "Our demo crashed on stage the second the CEO typed his own name—"
    "my coding agent hardcoded mine."
)


def validate_entry(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Entry text must not be empty or whitespace-only")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("Entry text must be a single line")
    if not (1 <= len(cleaned) <= 280):
        raise ValueError(f"Entry length out of bounds: {len(cleaned)}")
    cleaned.encode("utf-8")
    return cleaned


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = validate_entry(ENTRY_TEXT)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
