#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

from cmath import exp, rect
from math import radians

with open('input.txt') as f:
    data = f.readlines()

inst = [(s[0], int(s[1:])) for s in data]

wp_movInstruct = {
    'N': lambda wp, v: wp + v*1j,
    'S': lambda wp, v: wp - v*1j,
    'E': lambda wp, v: wp + v,
    'W': lambda wp, v: wp - v
}

wp_rotInstruct = {
    'L': lambda wp, a: wp * exp(radians(a)*1j),
    'R': lambda wp, a: wp * exp(-radians(a)*1j)
}

movInstruct = {
    'F': lambda s, v, wp=10+1j: s + v*wp
}

pos = 0+0j
wp = 10+1j
a = 0

for i, v in inst:
    if i in wp_movInstruct:
        wp = wp_movInstruct[i](wp, v)
    elif i in wp_rotInstruct:
        wp = wp_rotInstruct[i](wp, v)
    elif i in movInstruct:
        pos = movInstruct[i](pos, v, wp)
    else:
        print('wut')


print(abs(pos.real)+abs(pos.imag))
