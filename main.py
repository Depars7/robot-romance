#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — entry generator (stdlib only).

Writes the chosen one-line pickup line to /output/entry.txt, byte-identical
on every run: no trailing newline, UTF-8, deterministic.
"""

import os

ENTRY = "Are you an overfitted model? Because you memorized my heart and generalize to no one else."

MIN_LEN = 1
MAX_LEN = 200

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Gate bounty: 1-200 karakter, bukan hanya whitespace, satu baris."""
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise ValueError("entry length %d outside %d-%d" % (len(text), MIN_LEN, MAX_LEN))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main():
    os.umask(0o022)
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verifikasi pasca-tulis: isi file harus byte-identik dengan ENTRY.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    expected = ENTRY.encode("utf-8")
    if written != expected:
        raise RuntimeError("verification failed: /output/entry.txt differs from ENTRY")
    print("wrote %d bytes to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
