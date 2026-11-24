"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username, one word and nothing
else, to /output/entry.txt.
"""

from pathlib import Path

USERNAME = "lightxa"


def main() -> None:
    # Gate in RULES.txt: UTF-8 text of 1 to 30 characters, not only
    # whitespace, a single word with no spaces or padding.
    if not 1 <= len(USERNAME) <= 30:
        raise ValueError("username must be 1 to 30 characters")
    if USERNAME != USERNAME.strip() or any(ch.isspace() for ch in USERNAME):
        raise ValueError("username must be a single word with no padding")

    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
