#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

import re

requiredKeys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

with open('input.txt') as f:
    data = f.read()

data = data.split('\n\n')

keyValues = [s.split() for s in data]

dicts = []

exp1 = re.compile(r'(\d+)(cm|in)')
exp2 = re.compile(r'#[\da-f]{6}')
exp3 = re.compile(r'\d{9}')
ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.

validation = {
    'byr': lambda v: len(v) == 4 and 1920 <= int(v) <= 2002,
    'iyr': lambda v: len(v) == 4 and 2010 <= int(v) <= 2020,
    'eyr': lambda v: len(v) == 4 and 2020 <= int(v) <= 2030,
    'hgt': lambda v: (150 <= int(exp1.match(v).groups()[0]) <= 193 if (exp1.match(v).groups()[1] if exp1.match(v) else None) == 'cm' else False) != (59 <= int(exp1.match(v).groups()[0]) <= 76 if (exp1.match(v).groups()[1] if exp1.match(v) else None) == 'in' else False),
    'hcl': lambda v: bool(exp2.fullmatch(v)),
    'ecl': lambda v: v in ecls,
    'pid': lambda v: bool(exp3.fullmatch(v))
}

for entry in keyValues:
    tempDict = {}
    for kv in entry:
        tempDict[kv[:3]] = kv[4:]
    print(tempDict)
    dicts.append(tempDict)

validPasses = 0

for d in dicts:
    if set(d.keys()).issuperset(requiredKeys):
        for k in validation:
            if not validation[k](d[k]):
                print(k, validation[k](d[k]))
                break
        else:
            validPasses += 1

print(validPasses)
