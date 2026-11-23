"""One Word From Grandma — the single word a grandma would text about AI.

Writes exactly one word (1-30 chars, UTF-8) to /output/entry.txt.
"""

import os

WORD = "nosy"

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
