#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

with open('10/input.txt') as f:
    data = f.readlines()

data = sorted(map(int,data))

data.insert(0, 0)
data.append(max(data)+3)

# print(data)

reverse = data[::-1]

partials = {0: 1, 1: 1, 2: 1}

# Jesus Christ this is insanely terrible code.

for i, v in enumerate(reverse[3:], start=3):
    j = 3
    delta = reverse[i-3] - v
    if delta > 3:
        j = 2
        delta = reverse[i-2] - v
    if delta == 3:
        if j == 3: # Look, I just wanted to go to bed.
            tmp = partials[i-3] + partials[i-2] + partials[i-1]
        else:
            tmp = partials[i-2] + partials[i-1]
        partials[i] = tmp
        continue
    elif delta == 2:
        tmp = partials[i-2] + partials[i-1]
        partials[i] = tmp
    if delta > 3:
        partials[i] = partials[i-1]

print(partials[len(data)-1])
