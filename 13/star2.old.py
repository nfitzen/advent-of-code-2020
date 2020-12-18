#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

import math
import itertools

with open('input.txt') as f:
    data = f.readlines()

firstId = int(data[1].split(',')[0])

ids = {(i, int(v)) for i, v in enumerate(data[1].split(',')) if v != 'x'}

check = 100000000000000 // firstId

print(check)

t = 100000000000000
while True:
    for i, v in ids:
        if (t + i) % v != 0:
            break
    else:
        break
    t += firstId

print(t)
