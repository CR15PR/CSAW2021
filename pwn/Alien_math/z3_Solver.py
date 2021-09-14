#!/usr/bin/python3
#
# Not my function! written by a1ex.t / EvilBunnyWrote
# Borrowed from: https://ctftime.org/writeup/30222
#
##################

from z3 import *

def fn(a, b):
    return (12 * (b - ord('0')) - 4 + 48 * (a - ord('0')) - (b - ord('0'))) % 10

def second():
    solver = z3.Solver()

    chars = z3.BitVecs(''.join((f'd{d:02} ' for d in range(len(expected)-1))), 32)
    for ch in chars:
        solver.add(ch > 47, ch <= 57)

    an = chars[0]
    for i in range(len(chars)- 1):
        v1 = chars[i + 1] - ord('0')

        an = ((v1 + fn(an, i + an)) % 10) + ord('0')
        solver.add(an == expected[i+1])

    solver.add(chars[0] == ord('7'))
    assert solver.check() == z3.sat
    rv = ''
    for i in range(len(chars)):
        rv += chr(solver.model()[chars[i]].as_long())
    print(rv)
    return rv

print('finding the second challenge answer...')
enter2 = second().encode() #  b'7856445899213065428791'
