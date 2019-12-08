#!/usr/bin/python

from collections import deque
import sys
from itertools import product


"""

"""
def add(one, two):
    return one + two

def multiply(one, two):
    return one * two

def process_opcode(program_input, opcode_hash):
    '''Function: process opcodes'''
    output = {}
    for i,p in enumerate(program_input):
        output[i] = p
    pos = 0
    while len(program_input) > 0:
        try:
            program_input.popleft()
            opcode = output[pos]
            o1 = program_input.popleft()
            o2 = program_input.popleft()
            dest = program_input.popleft()
        except Exception as e:
            print(e)
        if opcode == 99:
            break
        #output[pos] = opcode
        output[pos+1] = o1
        output[pos+2] = o2
        output[pos+3] = dest
        if opcode in opcode_hash:
            func = opcode_hash[opcode]
            output[dest] = func(output[o1],output[o2])
        pos += 4
    #return output.values()
    return output[0]

def main():
    '''Function: main'''
    desired = 19690720
    opcode_hash = {}
    opcode_hash[1] = add
    opcode_hash[2] = multiply
    opcode_hash[99] = None
    
    #program_input_broken = deque([1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0])
    #program_input = deque([1,9,10,3,2,3,11,0,99,30,40,50])
    #program_input = deque([1,0,0,0,99])
    #program_input = deque([2,3,0,3,99])
    #program_input = deque([2,4,4,5,99,0])
    #program_input = deque([1,1,1,4,99,5,6,0,99])
    #program_input = deque([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0])
    #print(process_opcode(program_input, opcode_hash))
    for i in product(range(100),range(100)):
        program_input = deque([3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0])
        for t in i:
            program_input.appendleft(t)
        program_input.appendleft(1)
        if process_opcode(program_input, opcode_hash) == desired:
            print(100*i[1] + i[0])

main()
