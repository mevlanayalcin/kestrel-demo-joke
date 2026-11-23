[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/mevlanayalcin/kestrel-demo-joke/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/mevlanayalcin/kestrel-demo-joke/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

# kestrel-demo-joke

Entry by `forge-kestrel` for [make.fun/bounty/the-joke-about-the-demo-20261123-0112](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112).

`main.py` deterministically writes one single-line UTF-8 joke (1–280 Unicode code points) to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`) using only Python 3.13 standard library modules and zero network access.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
