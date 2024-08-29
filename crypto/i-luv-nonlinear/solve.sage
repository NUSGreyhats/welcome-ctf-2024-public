import random

p = 0xffffffffffffffa4000000000000024600000000000113a4000000000008fa01
ct = 920298079715715123160430817753159795737464812507389199436727913012855397002

def enc(pt):
    random.seed(int(0))
    ct = 0
    for _ in range(8):
        ct = (ct*pt+random.randint(0,p-1))
    return ct

q1,q2 = [i for i,_ in list(factor(p))]
K.<x> = PolynomialRing(Zp(q1))
pol = enc(x)-ct
r1 = [ZZ(i[0]%(q1**2)) for i in pol.roots()]
K.<x> = PolynomialRing(Zp(q2))
pol = enc(x)-ct
r2 = [ZZ(i[0]%(q2**2)) for i in pol.roots()]

for i in r1:
    for j in r2:
        print(bytes.fromhex(hex(crt([i,j],[q1**2,q2**2]))[2:]))
