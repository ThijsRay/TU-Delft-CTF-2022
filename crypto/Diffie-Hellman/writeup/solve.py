#!/usr/bin/python

# You can perform a man-in-the-middle attack here

from pwn import *
from secrets import randbits
from cryptography.fernet import Fernet
from os import environ
from base64 import b64encode

host = environ["HOST"]
port = environ["PORT"]

p = 0xfd67a3b76136aaeb345f4175f38e65cad628e6535e7fc40f5e7952e7799d1b23
g = 0x2

class Party:
    def __init__(self) -> None:
        self.private = randbits(128)
        self.public = pow(g, self.private, p)

    def calculate_key(self, other_public):
        self.key = pow(other_public, self.private, p)
        self.key = b64encode(self.key.to_bytes(32, 'little'))
        self.f = Fernet(self.key)

    def encrypt(self, plaintext):
        return self.f.encrypt(plaintext)

    def decrypt(self, ciphertext):
        return self.f.decrypt(ciphertext)

r = remote(host, port)

r.readuntil(b'public key is ')
alice_pk = int(r.readline()[:-1])

r.readuntil(b'public key is ')
bob_pk = int(r.readline()[:-1])

a2b = Party()
a2b.calculate_key(bob_pk)
b2a = Party()
b2a.calculate_key(alice_pk)

# Send fake public key to Bob
r.readuntil(b'public key: ')
r.sendline(str(a2b.public).encode('utf-8'))

# Send fake public key to Alice
r.readuntil(b'public key: ')
r.sendline(str(b2a.public).encode('utf-8'))

r.readuntil(b"sends to Bob: b'")
message = r.readline()[:-2]
print(b2a.decrypt(message))

r.readuntil(b"replies to Alice: b'")
message = r.readline()[:-2]
print(a2b.decrypt(message))
