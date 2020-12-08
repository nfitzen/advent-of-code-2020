#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2020 Nathaniel Fitzenrider <https://github.com/nfitzen>
#
# SPDX-License-Identifier: CC0-1.0

# Jesus Christ this was overengineered to Hell and back.

from typing import List, Tuple, Union

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
        self.status = 0
    def process(self, instructions: List[Union[Tuple[str, int], str]]) -> int:
        '''Returns the accumulator value at the end.'''
        self.status = 0
        if type(instructions[0]) == str:
            instructions = self.compile(instructions)
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
                self.status = 1
                break
            visitedPos.add(self.position)
        return (self.accumulator, self.status)
    def compile(self, instructions: list) -> List[Tuple[str, int]]:
        return [self.parse(i) if type(i) == str else i for i in instructions]
    def parse(self, instruction: str) -> Tuple[str, int]:
        if type(instruction) == tuple:
            return instruction
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

# It's not a universal solution; it only works for jmp.
# I just got lucky.

console = Console()

instructions = console.compile(instructions)

positions = {i[0] if i[1][0] == 'jmp' else None for i in enumerate(console.compile(instructions))}
positions -= {None}

for pos in positions:
    console.__init__()
    tmpInstruct = instructions.copy()
    tmpInstruct[pos] = ('nop', tmpInstruct[pos][1])
    acc, status = console.process(tmpInstruct)
    if status == 0:
        print(acc)
