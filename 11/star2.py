#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

# Remind me not to get a job that involves a lot of programming.

import itertools
from typing import List
from copy import deepcopy

with open('input.txt') as f:
    data = list(list(s.strip()) for s in f.readlines())

def update(state: List[List[str]]) -> List[List[str]]:
    '''Returns the updated seating state.'''
    newState = deepcopy(state)
    for i, row in enumerate(state):
        for j, v in enumerate(row):
            seen = 0
            for di in range(-1, 2): # di = delta i
                for dj in range(-1, 2):
                    k, l = i+di, j+dj
                    if not (di == dj == 0):
                        while (0 <= k <= len(state)) and (0 <= l <= len(row)):
                            try:
                                tmp = state[k][l]
                                if tmp == '#':
                                    seen += 1
                                    break
                                elif tmp != '.':
                                    break
                            except:
                                break
                            k, l = k+di, l+dj
            if v == 'L' and seen == 0:
                newState[i][j] = '#'
            elif v == '#' and seen >= 5:
                newState[i][j] = 'L'
    return newState

old = None
new = deepcopy(data)

while old != new:
    old = deepcopy(new)
    new = update(old)
    # print('\n'.join(''.join(l) for l in new) + '\n')

print(sum(map(list.count, new, itertools.repeat('#'))))
