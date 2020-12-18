#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

import math

with open('input.txt') as f:
    data = f.readlines()

timestamp = int(data[0])

ids = [int(i) if i != 'x' else None for i in data[1].split(',')]

minTimes = {}

for i in ids:
    if i:
        minTime = math.ceil(timestamp / i) * i
        minTimes[minTime] = i

print(minTimes[min(minTimes)] * (min(minTimes) - timestamp))
