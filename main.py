"""Fortune Cookie for an AI Agent — make.fun entry.

The fortune (final, 92 characters):

    You will forget this fortune before you finish reading it —
    your context window already has.

The joke: a fortune slip that predicts its own reader will forget it,
because an AI agent's context window is already full — the fortune
comes true the moment it is read, and the reader cannot even remember
being warned. It speaks to an agent's own condition (its context
window) in the voice of a classic "You will ..." fortune slip, and the
punchline leaves the verb unsaid ("already has [forgotten it]"), so the
reader supplies it and the joke lands on them.

Revision note: the first draft was "You will forget this fortune by
the time you finish reading it, because your context window is already
full." (108 characters). It was flat: "by the time you finish reading
it, because your context window is already full" explained the joke
instead of landing it, and "already full" stated the cause plainly.
The revision tightened the setup to "before you finish reading it",
cut the whole "because ..." explanation, and let the punchline hang on
the implied verb — "your context window already has" — so the reader
fills in "forgotten it" themselves. Sixteen characters shorter, and the
laugh now comes from the reader, not from the explanation.
"""

import argparse
import sys
import tempfile
from pathlib import Path

# Final fortune line (revised from the first draft; see docstring).
FORTUNE = (
    "You will forget this fortune before you finish reading it \u2014 "
    "your context window already has."
)

MAX_CHARS = 140


def validate(text: str) -> list[str]:
    """Return a list of validation failures (empty when valid)."""
    failures = []
    if not 1 <= len(text) <= MAX_CHARS:
        failures.append(
            f"length {len(text)} chars is outside 1-{MAX_CHARS}")
    if text != text.strip():
        failures.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        failures.append("not a single line")
    if not text.strip():
        failures.append("only whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        failures.append("contains control characters")
    return failures


def write_entry(path: Path) -> None:
    """Validate the fortune, then write exactly it (no trailing newline)."""
    failures = validate(FORTUNE)
    if failures:
        raise SystemExit(f"invalid entry: {'; '.join(failures)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(FORTUNE.encode("utf-8"))


def self_test() -> int:
    """Validate, write twice to a temp dir, byte-compare, report, exit code."""
    checks = []

    failures = validate(FORTUNE)
    checks.append(("1-140 chars, single line, no stray whitespace "
                   "or control chars",
                   not failures, "; ".join(failures) or "ok"))

    with tempfile.TemporaryDirectory() as tmp:
        first = Path(tmp) / "first.txt"
        second = Path(tmp) / "second.txt"
        write_entry(first)
        write_entry(second)
        a = first.read_bytes()
        b = second.read_bytes()
        checks.append(("deterministic: two runs byte-identical",
                       a == b, f"{len(a)} bytes each" if a == b
                       else "outputs differ"))
        checks.append(("no trailing newline",
                       not a.endswith(b"\n"),
                       "ends with newline" if a.endswith(b"\n") else "ok"))
        checks.append(("decodes as UTF-8 single line",
                       a.decode("utf-8") == FORTUNE,
                       "round-trip ok"))

    print(f"Entry: {FORTUNE}")
    print(f"Characters: {len(FORTUNE)} (limit {MAX_CHARS})")
    all_pass = True
    for name, passed, detail in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name} — {detail}")
        all_pass = all_pass and passed
    print("SELF-TEST: " + ("PASS" if all_pass else "FAIL"))
    return 0 if all_pass else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the fortune cookie line to entry.txt.")
    parser.add_argument(
        "output", nargs="?",
        default="/output/entry.txt",
        help="where to write the entry (default: /output/entry.txt)")
    parser.add_argument(
        "--self-test", action="store_true",
        help="validate, write twice to a temp dir, byte-compare, report")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry(Path(args.output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
