#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

from string import ascii_lowercase as alpha

with open('6/input.txt') as f:
    data = f.read()

groups = data.split('\n\n')

counts = []

for g in groups:
    count = 0
    for l in alpha:
        if l in g:
            count += 1
    counts.append(count)

print(sum(counts))
