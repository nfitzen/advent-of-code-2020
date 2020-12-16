#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

with open('input.txt') as f:
    data = f.readlines()

data = sorted(map(int,data))

data.insert(0, 0)
data.append(max(data)+3)

deltas = []

for i, v in enumerate(data[1:], start=1):
    delta = v - data[i-1]
    if delta > 3:
        print('wtf')
    deltas.append(delta)

print(deltas.count(1))

print(deltas.count(3))

print(deltas.count(1) * deltas.count(3))
