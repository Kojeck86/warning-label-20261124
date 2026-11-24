"""Entry for make.fun bounty u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

Writes one single-line safety warning label for human beings to
/output/entry.txt. Standard library only; deterministic: the same line
every run.

The label: a real printed-label WARNING about the universal human habit
of saying "just one more episode" at midnight — and the turn lands in
the last few words, when the exhausted, furious person is ready to do
it all again tonight. 118 characters, one line, inside the 1-160 gate.
"""

import os

LINE = (
    "WARNING: Says 'just one more episode' at midnight, then wakes up "
    "exhausted, furious, and ready to do it again tonight."
)


def main():
    # Gate: 1-160 characters, one line, no trailing newline.
    if not 1 <= len(LINE) <= 160:
        raise ValueError("entry line must be 1-160 characters, got %d" % len(LINE))
    if "\n" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
