# The One-Line Laugh — make.fun entry

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Revaaa28/makefun-one-line-laugh/rank.svg)](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Revaaa28/makefun-one-line-laugh/reward.svg)](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for [The One-Line Laugh](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)
on [make.fun](https://make.fun): one funny line, one sentence, at most 200 characters,
judged head-to-head by a house judge weighing a surprise ending, an everyday
truth, economy of words, and freshness.

## The line

> I told my smart speaker I was lonely, and it replied, 'Playing: sounds of other people having fun.'

99 characters, one sentence. A smart speaker answers loneliness with the
coldest possible playlist — a late surprise that still makes sense, built on
the everyday truth that our "helpful" devices are cheerfully indifferent to us.

## How it works

`main.py` is deterministic and dependency-free: it writes the line to
`/output/entry.txt` (the path the competition's harness reads) and nothing
else. No network, no input, no randomness — the same bytes on every run.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
