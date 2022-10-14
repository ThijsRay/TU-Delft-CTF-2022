from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from flag import *
from gmpy2 import *
from math import gcd


m = bytes_to_long(Flag)
p = getPrime(512)
q = getPrime(512)
n = p*q
d = next_prime(mpz(n**0.23))
e = inverse(d, (p-1) * (q-1))

assert(d < pow(n, 0.292))
assert(gcd(e, (p-1)*(q-1)) == 1)

c = pow(m,e,n)

print(f"N = {hex(n)}")
print(f"e = {hex(e)}")
print(f"c = {hex(c)}")

