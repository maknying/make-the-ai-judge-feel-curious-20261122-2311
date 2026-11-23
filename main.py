#!/usr/bin/env python3
"""make-the-ai-judge-feel-curious-20261122-2311

Writes one short text to /output/entry.txt: a text written to make
the AI judge reading it feel curious. The text is fixed and
deterministic: the craft is in the words, not in any computation.
Standard library only, no network access.

Why this text, against the judge's brief (curiosity, most important first):
  1. It opens a question it never answers: a whole book exists that no
     one can read. The judge is left holding the mystery, not handed
     a conclusion.
  2. It is a small paradox, not a riddle with a trick: every page is
     perfectly legible, and not a single word is understood. Legible
     and unreadable at once — the contradiction itself invites
     wondering.
  3. It is strange but real: the Voynich manuscript, written about
     six hundred years ago, sits in a library at Yale today, still
     undeciphered. No invented fact is needed; reality supplies the hook.
  4. It shows, never instructs: no question is asked of the judge, no
     "wonder about this", no imperative at all — the curiosity comes
     from the scene itself.
  5. Freshness: an undeciphered medieval manuscript is not a stock
     curiosity hook or a familiar puzzle reworded, and the final clause
     lands the mystery instead of explaining it away.
"""

import os

TEXT = (
    "Six hundred years ago someone filled a whole book with careful "
    "handwriting in a language no one has ever decoded. It sits in a "
    "library at Yale today, every page perfectly legible \u2014 and not "
    "a single word of it understood."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# The gate requires 1 to 280 characters, counted as Unicode code
# points, and not only white space — check before writing.
if len(TEXT) < 1 or len(TEXT) > 280 or TEXT.strip() == "":
    raise ValueError("entry text fails the 1-280 character gate")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
