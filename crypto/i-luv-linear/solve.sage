import random

def enc(ct):
    random.seed(int(0))
    for _ in range(100):
        ct ^^= ct>>random.randint(1,32)
    return ct

def tovec(x,n):
    return vector(GF(2),[(x>>i)&1 for i in range(n)])

def toint(v,n):
    return sum(2^e for i,e in zip(v,range(n)) if i)

ct = b'n\xb2t"l(cWp\x8c\x83\xb3\xc5\xee\x98T\x0e\xceI&\x83\xe9ZZ7uvFf\x88\xdcz'
ct = int(ct.hex(),16)
n = 32*8
M = Matrix([tovec(enc(2^i),n) for i in range(n)])^-1
pt = tovec(ct,n)*M
print(bytes.fromhex(toint(pt,n).hex()))
