"""Write the quiet-dread code review entry to /output/entry.txt.

One line, 104 characters (limit 140) -- no trailing newline."""

from pathlib import Path

ENTRY = "LGTM. The code works, the tests pass, and none of us will remember why any of this exists in six months."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
