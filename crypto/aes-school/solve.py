from pwn import *
import os

HOST = "localhost"

p = remote(HOST, 32000)

def encrypt(pt: bytes):
    p.sendlineafter(b">", b"1")
    p.sendlineafter(b":", pt.hex().encode())
    p.recvuntil(b": ")    
    return bytes.fromhex(p.recvline().decode().strip())

target = b"gimme the flag!!"
msg1 = b" "*8 + target[:8]
msg2 = target[8:]

ct1 = encrypt(msg1)
ct2 = encrypt(msg2)

soln = ct1[:16] + ct2[:16]

p.sendlineafter(b">", b"2")
p.sendlineafter(b": ", soln.hex().encode())
p.interactive()

