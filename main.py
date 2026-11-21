"""Deliver the poem entry to the make.fun output directory.

The poem lives in entry.txt, right beside this script. Running
this program copies that file, byte for byte, to a file also
named entry.txt inside the output directory.
"""

import os
import shutil


def poem_source():
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, "entry.txt")


def main():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    shutil.copyfile(poem_source(), target)


if __name__ == "__main__":
    main()
