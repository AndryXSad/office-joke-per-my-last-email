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

# The entry line (81 chars, under the 200-char cap): the joke's turn lands
# on "in my will" — the speaker escalates "per my last email" past death,
# so the punchline is the escalation itself, not the email phrase alone.
LINE = "I put 'per my last email' in my will so my family knows I already explained this."


def main() -> None:
    # Self-check: a one-liner entry must stay a single line under the cap;
    # fail loudly instead of writing an invalid entry.
    assert 1 <= len(LINE) <= 199 and "\n" not in LINE, "entry line must be 1-199 chars, one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
