#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

import itertools

with open('input.txt') as f:
    text = f.readlines()
    ints = [int(s) for s in text]

    perms = itertools.permutations(ints,3)

    for p in perms:
        if sum(p) == 2020:
            print(p)
            quit()
