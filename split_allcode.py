#!/usr/bin/env python3
"""Rebuild the project folder from ALL_CODE.txt:  python3 split_allcode.py ALL_CODE.txt [output_dir]"""
import re, sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text()
dest = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "Astralis_rebuilt")
parts = re.split(r"^===== FILE: (.+?) =====\n", src, flags=re.M)
n = 0
for i in range(1, len(parts), 2):
    p = dest / parts[i]; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(parts[i + 1].strip("\n") + "\n"); n += 1
print(f"wrote {n} files to {dest}/  ->  cd {dest} && mvn package")
