import random
flag = input().encode()
assert len(flag)==32
assert flag[:5]==b"grey{" and flag[-1:]==b"}"
p = 0xffffffffffffffa4000000000000024600000000000113a4000000000008fa01

def enc(pt):
    random.seed(0)
    pt = int(pt.hex(),16)
    ct = 0
    for _ in range(8):
        ct = (ct*pt+random.randint(0,p-1))%p
    return ct#bytes.fromhex(hex(ct)[2:])

assert enc(flag) == 920298079715715123160430817753159795737464812507389199436727913012855397002
print(f"{flag = }")
