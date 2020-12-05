#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

with open('5/input.txt') as f:
    data = f.readlines()

passes = {int(s.replace('F','0').replace('B','1').replace('R','1').replace('L','0'), 2) for s in data}

print(max(passes))
