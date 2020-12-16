#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

from string import ascii_lowercase as alpha

with open('input.txt') as f:
    data = f.read()[:-1]

groups = data.split('\n\n')

splitGroups = [s.split('\n') for s in groups]

counts = []

for g in splitGroups:
    conv = set(g[0])
    for line in g[1:]:
        conv &= set(line)
    counts.append(len(conv))
    print(conv)


print(sum(counts))
