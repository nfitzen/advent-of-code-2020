#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

with open('3/input.txt') as f:
    data = f.readlines()

data = [s.rstrip() for s in data]

# print(data)

dx = 1
dy = 2

x, y = 0, 0
length = len(data[0])
# print(length)

count = 0

while y < len(data):

    if data[y][x % length] == '#':
        count += 1
        # print('ree')

    y += dy
    x += dx

print(count)
