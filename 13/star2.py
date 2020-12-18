#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

from math import lcm
import itertools

with open('input.txt') as f:
    data = f.readlines()

firstId = int(data[1].split(',')[0])

ids = {(i, int(v)) for i, v in enumerate(data[1].split(',')) if v != 'x'}

t, m = (firstId,) * 2

for i, v in ids:
    while (t+i) % v:
        t += m
    m = lcm(m, v)

print(t)
