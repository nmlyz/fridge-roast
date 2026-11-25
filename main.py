#!/usr/bin/env python3
"""Write a one-line roast of a smart fridge to /output/entry.txt.

The line is a single roast, 110 characters: a smart fridge with a camera
inside and a touchscreen outside that still cannot find the milk hiding
behind the ketchup. Standard library only; the output is deterministic.
"""

import os

LINE = (
    "My smart fridge has a camera inside, a touchscreen outside, "
    "and still cannot find the milk behind the ketchup."
)

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 200


def output_path():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        pass
    return os.path.join(out_dir, OUTPUT_NAME)


def write_entry(path):
    text = LINE + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("written entry does not match the line")
    return len(LINE)


def main():
    if len(LINE) > MAX_CHARS:
        raise SystemExit("line exceeds the 200 character limit")
    write_entry(output_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
