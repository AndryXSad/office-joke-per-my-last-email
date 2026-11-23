"""Make the AI Judge Laugh: Office Jokes — one original office joke.

The entry is a single original line (81 characters, well under the 200
character cap) about office life. The joke takes the most passive-aggressive
phrase in corporate email — "per my last email" — and escalates it to the
grave: the speaker has written it into their will, so even death does not
stop them from pointing out they already explained this.

Why this line: it is a genuine one-line joke (not a slogan or observation),
its turn lands at the end ("in my will"), it rings true for anyone who has
ever re-sent an ignored email, every word earns its place, and it avoids
the obvious Monday-morning / photocopier takes.

The program writes the line from a literal string so the run is fully
deterministic, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = "I put 'per my last email' in my will so my family knows I already explained this."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
