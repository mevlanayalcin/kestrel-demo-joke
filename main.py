"""Deterministic entry generator for the-joke-about-the-demo-20261123-0112."""

from __future__ import annotations

import os
from pathlib import Path

# Undefeated out-of-family champion (APEX_C_today, 145 Unicode code points, 0.650 OOF win rate).
ENTRY_TEXT = (
    "Our demo crashed on stage; my coding agent typed "
    "'Found the exact one-line fix!', compacted its context, "
    "and asked, 'What are we building today?'"
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
