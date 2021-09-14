!#/usr/bin/env python3
#
# Not my script
# Borrowed from https://github.com/apoirrier/CTFs-writeups/blob/master/CSAWQual2021/pwn/AlienMath.md
#
import ctypes

goal = "7759406485255323229225"

def modify(x, y, i):
    b = ctypes.c_uint((x*0x30 + (x+i)*0xb - 4)).value % 10
    b += y
    return b % 10

print(7, end="")
current = 7
for i in range(21):
    g = int(goal[i+1])
    for next in range(10):
        if modify(current, next, i) == g:
            print(next, end="")
            current = g
            break
