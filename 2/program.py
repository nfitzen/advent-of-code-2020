#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

import re

with open('input.txt') as f:
    lines = f.readlines()

    count = 0

    for line in lines:
        s = re.match('(\d+)-(\d+) (.): (.+)', line).groups()

        firstNum = int(s[0])
        secondNum = int(s[1])
        char = s[2]
        password = s[3]

        if (password[firstNum-1] == char) != (password[secondNum-1] == char):
            count += 1
            print('reee')



print(count)
