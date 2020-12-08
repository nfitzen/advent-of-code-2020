#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

# Since I'm physically incapable of beating star 1 right now,
# I'm just making whatever overengineered dumb thing I feel like.

with open('8/input.txt') as f:
    instructions = f.readlines()

class Console():
    def __init__(self):
        self.instructions = {'nop', 'acc', 'jmp'}
        self.accumulator = 0
        self.lastOp = 'nop'
        self.lastArg = '+0'
        self.position = 0
        self.lastPosition = 0
    def process(self, instructions: list) -> int:
        '''Returns the accumulator value at the end.'''
        visitedPos = set()

        while self.position < len(instructions):
            self.lastPosition = self.position
            ins = self.parse(instructions[self.position])
            if ins[0] == 'acc':
                self.acc(ins[1])
            elif ins[0] == 'jmp':
                self.jmp(ins[1])
            elif ins[0] == 'nop':
                self.nop(ins[1])
            self.position += 1

            if self.position in visitedPos:
                break
            visitedPos.add(self.position)
        return self.accumulator
    def parse(self, instruction: str) -> tuple:
        op = instruction[0:3]
        arg = int(instruction[4:])
        if op not in self.instructions:
            op = 'nop'
            arg = 0
        return (op, arg)
    def acc(self, arg: int):
        self.accumulator += arg
        return self.accumulator
    def jmp(self, arg: int) -> int:
        '''Returns last position'''
        self.lastPosition = self.position
        self.position += arg - 1
        return self.position
    def nop(self, arg: int):
        return arg

console = Console()

print(console.process(instructions))
