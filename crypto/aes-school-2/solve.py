import os
from pwn import *

HOST = "localhost"

p = remote(HOST, 32001)

def encryptflag():
    p.sendlineafter(b">", b"1")
    p.recvuntil(b": ")    
    return bytes.fromhex(p.recvline().decode().strip())

def decrypt(pt: bytes):
    p.sendlineafter(b">", b"2")
    p.sendlineafter(b":", pt.hex().encode())
    return "received" in p.recvline().decode()

ct = bytearray(encryptflag())

CT = ct[:]

ans = bytearray([0 for i in range(32)])
                
for idx in range(2, 17):
    for j in range(1, idx):
        CT[-16-j] ^= (idx-1)^idx
    for i in range(256):
        CT[-16-idx] = i
        if (decrypt(CT)):
            ans[-idx] = ct[-16-idx]^idx^i
            break

CT = ct[:-16]

for idx in range(1, 17):
    for j in range(1, idx):
        CT[-16-j] ^= (idx-1)^idx
    for i in range(256):
        CT[-16-idx] = i
        if (decrypt(CT)):
            ans[-16-idx] = ct[-32-idx]^idx^i
            break


print(ans)
