#!/usr/bin/python3

from z3 import *

nums = [7,7,5,9,4,0,6,4,8,5,2,5,5,3,2,3,2,2,9,2,2,5] # this is the number we need to compare to and match to proceed. But if this number is the input it goes through this transformation and gets mangled.

#once we figure out how to represent the transformation in the C code the z3 library can produce the required inputs based on the known output and constraints

def transformation(param1, param2):
    x = param1
    y = param2
    return ((x -48) * 48 + (y - 48) * 11 - 4) % 10


for i in range(len(nums)-1):
    x = i + 1
    y = transformation(nums[i], nums[i]+i)
    y = x - 48 + y
    nums[i+1] = y + (y/2) * -10 + '0'
