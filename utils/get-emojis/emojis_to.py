#!/usr/bin/env python3

import csv
from pprint import pprint
import sys

if len(sys.argv) < 2:
    raise ValueError("Path to emojis.csv missing")

emojis = {} # key: name, value: string containing emoji

with open(sys.argv[1], newline="") as c:
    reader = csv.reader(c)
    for index, row in enumerate(reader):
        if index == 0:
            continue
        emoji = row[4]
        name = row[5]
        emojis[name] = emoji

# Print the emojis dictionary to stdout here so that we can pipe into discordbot/emojis.py
pprint(emojis, indent=4)