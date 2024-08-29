HOST = "challs.nusgreyhats.org"
# HOST = "localhost"
# Update port as needed
PORT = 32832

# Put the solution script here
from pwn import *
p = remote(HOST, PORT)
p.sendlineafter(b"Enter", b"2038-01-01T02:12:27")
p.interactive()