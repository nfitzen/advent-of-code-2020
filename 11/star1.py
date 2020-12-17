#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

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
            adj = []
            for k, l in itertools.product(range(-1, 2), repeat=2):
                if not (k == 0 and l == 0) and (i+k >= 0 and j+l >= 0):
                    try:
                        adj.append(state[i+k][j+l])
                    except:
                        pass
            numAdj = adj.count('#')
            if v == 'L' and numAdj == 0:
                newState[i][j] = '#'
            elif v == '#' and numAdj >= 4:
                newState[i][j] = 'L'
    return newState

old = None
new = deepcopy(data)

while old != new:
    old = deepcopy(new)
    new = update(old)
    # print('\n'.join(''.join(l) for l in new) + '\n')

print(sum(map(list.count, new, itertools.repeat('#'))))
