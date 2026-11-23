"""Write one short text for a make.fun bounty entry.

The text is a complete story about a journey, told in exactly one sentence.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on his last "
    "crossing he handed me the wheel at the whistle buoy and stood at the rail with his "
    "back to the town, so I brought us in by the smell of the cannery and he arrived a "
    "passenger."
)


def output_dir() -> Path:
    """Return the folder to write into, honouring MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(f"{len(TEXT)} characters -> {target / 'entry.txt'}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
