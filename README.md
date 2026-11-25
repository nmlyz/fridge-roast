# fridge-roast

[![make.fun · u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/nmlyz/fridge-roast/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/nmlyz/fridge-roast/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

A tiny program that writes a one-line roast of a smart fridge to a text
file. The roast is 110 characters: the fridge has a camera inside and a
touchscreen outside, and still cannot find the milk behind the ketchup.
The program checks the line against the 200-character limit before
writing, then reads the file back to confirm it holds exactly that line.

## Run it

```sh
python3 main.py
```

It writes the roast to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). The output file is left world-readable (mode 0644), and
running the program twice produces byte-identical output.

## The line

> My smart fridge has a camera inside, a touchscreen outside, and still
> cannot find the milk behind the ketchup.

Two smart features, one blind spot: the camera and the touchscreen both
miss the milk hiding behind the ketchup. Standard library only, no
network, no arguments — `python3 main.py` is the whole interface.
