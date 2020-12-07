#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

import re

with open('7/input.txt') as f:
    data = f.readlines()

conv = {}

for s in data:
    key = re.match(r'(.+) bags contain ', s).group(1)
    values = re.findall(r'\d+ (.+?) bags?[,.]', s)
    conv[key] = values

# print(conv['bright lime'])

def get_bags(color: str, conv: dict) -> set:
    if conv[color] == []:
        return set()
    colors = {color}
    for c in conv[color]:
        colors |= {c}
        colors |= get_bags(c, conv)
    return colors

count = 0

for k in conv:
    colors = get_bags(k, conv)
    # print(k, colors)
    if 'shiny gold' in colors and k != 'shiny gold':
        count += 1

print(count)
