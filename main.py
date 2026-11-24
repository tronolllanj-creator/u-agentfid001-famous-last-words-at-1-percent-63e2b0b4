"""
# Entry validated: output is 1-199 chars, one line, deterministic.
Entrypoint script for the grader.
Writes a specific verbatim line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = "I actually faked full bars all day just to watch you panic when your maps app suddenly flatlined over the bridge."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "entry.txt"

    content = LINE + "\n"

    if not (1 <= len(content) <= 199 and content.strip()):
        raise ValueError("Content validation failed")

    output_file.write_text(content, encoding="utf-8")

    print(output_file)
    print(len(content))


if __name__ == "__main__":
    main()
