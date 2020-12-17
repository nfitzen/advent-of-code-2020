#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

from cmath import rect
from math import radians

with open('input.txt') as f:
    data = f.readlines()

inst = [(s[0], int(s[1:])) for s in data]

movInstruct = {
    'N': lambda s, v, a=0: s + v*1j,
    'S': lambda s, v, a=0: s - v*1j,
    'E': lambda s, v, a=0: s + v,
    'W': lambda s, v, a=0: s - v,
    'F': lambda s, v, a=0: s + rect(v, radians(a)*1j)
}

rotInstruct = {
    'L': lambda a, v: (a + v) % 360,
    'R': lambda a, v: (a - v) % 360
}

pos = 0+0j
a = 0


for i, v in inst:
    if i in movInstruct:
        pos = movInstruct[i](pos, v, a)
    elif i in rotInstruct:
        a = rotInstruct[i](a, v)
    else:
        print('wut')

print(abs(pos.real)+abs(pos.imag))
