#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

import itertools

with open('9/input.txt') as f:
    data = f.readlines()

data = list(map(int, data))

for n in enumerate(data[25:], 25):
    if n[1] not in (a + b for a, b in itertools.combinations(data[n[0]-25:n[0]], 2)):
        invalid = n[1]
        break

print(invalid)

# I might have gotten my indices wrong

for i in range(2, len(data)-25):
    for j in range(len(data)-i):
        tmp = data[j:j+i]
        if sum(tmp) == invalid:
            print(min(tmp) + max(tmp))
