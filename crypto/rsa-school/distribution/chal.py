from Crypto.Util.number import isPrime,GCD # pip install pycryptodome
import random
import sys
from hashlib import sha256

MAGIC1 = "ff20b341f8bd54837ba6a7d68a01bfb6922c9ab3f86f7a24cd4376277f77fa00"
MAGIC2 = "66200057048904561310773450754513118682872987215243475408580973598511850449092621163958665485940959549116143328863633485610674754281932357951581747279569555286557989465547173185431765053999599204779436658547634756129524189103394473610686233103699165808690574337593176117530396663309220705224502578368073507606"
t = open(sys.argv[0],"r").read().replace(MAGIC1,"").replace(MAGIC2,"")
random.seed(t) # please dont modify this file!
assert sha256(t.encode()).hexdigest()==MAGIC1 # please dont modify this file!

def newPrime(nbits):
    t = 4
    while not isPrime(t):
        t = random.randint(2**(nbits-1),2**nbits-1)
    return t

p = newPrime(512)
q = newPrime(512)
e = 65537
N = p*q

print("Let's see if you know RSA!")
print("-"*16+"[parameters]---"+"-"*16)
print(f"{p = }")
print(f"{q = }")
print(f"{e = }")
print("")
print("-"*16+"[setup]---"+"-"*16)
c = random.randint(2**1023,2**1024-1)-int(MAGIC2)
print("Here is the ciphertext, which is computed by c=m^e mod N where m is the message")
print(f"{c = }")
print("")
print("-"*16+"[step 1]---"+"-"*16)
print("To recover m, we first compute the private key d.")
print("d must satisfy the following equation: e*d = 1 mod [(p-1)(q-1)]")
print("Hint: look up modular inverse")
d = int(input(f"d = "))
assert (e*d)%((p-1)*(q-1)//GCD(p-1,q-1))==1

print("-"*16+"[step 2]---"+"-"*16)
print("Now, compute m=c^d mod (pq)")
print("Hint: look up modular exponentiation")
m = int(input(f"m = "))
assert pow(m,e,p*q) == c

print("-"*16+"[flag]---"+"-"*16)
print("Now convert m to a string and submit it as a flag!")
print("Hint: pycryptodome long_to_bytes")

print("-"*16+"[why does it work]---"+"-"*16)
print("Notice that x^(p-1) mod p = 1 and x^(q-1) mod q = 1 for any x (coprime to N)")
print("Hence x^[k*(p-1)(q-1)+1]=x mod (pq) for any k")
print("Hence (x^e)^d=x mod N for any x where N=pq")

