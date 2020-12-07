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
    values = [(int(n), c) for n, c in re.findall(r'(\d+) (.+?) bags?[,.]', s)]
    conv[key] = values

# print(conv['bright lime'])

def get_count(color: str, conv: dict) -> int:
    if conv[color] == []:
        return 0
    count = 0
    for c in conv[color]:
        count += c[0]
        count += c[0] * get_count(c[1], conv)
    return count

print(get_count('shiny gold', conv))
