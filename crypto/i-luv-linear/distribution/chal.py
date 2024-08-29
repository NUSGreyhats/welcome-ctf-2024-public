import random
flag = input().encode()
assert len(flag)==32

def enc(pt):
    random.seed(0)
    ct = int(pt.hex(),16)
    for _ in range(100):
        ct ^= ct>>random.randint(1,32)
    return bytes.fromhex(hex(ct)[2:])

assert enc(flag)==b'n\xb2t"l(cWp\x8c\x83\xb3\xc5\xee\x98T\x0e\xceI&\x83\xe9ZZ7uvFf\x88\xdcz'
print(f"{flag = }")
