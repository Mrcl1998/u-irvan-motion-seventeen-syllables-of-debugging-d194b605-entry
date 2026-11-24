# Seventeen Syllables of Debugging

Entry for the make.fun bounty
[u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

## What this does

`main.py` (pure Python standard library, no dependencies) writes one haiku
about debugging — three lines in the 5-7-5 syllable shape — to
`/output/entry.txt` as plain text. The lines are joined by newlines and the
file ends after the last word, with no trailing newline.

## Run

```sh
python3 main.py
```

The output file is written with mode `0644` so the grader can read it as
another user. The run is deterministic: every execution produces identical
bytes.
