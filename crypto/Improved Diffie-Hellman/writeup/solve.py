#!/usr/bin/python

# Challenge is based on the blog post "The Most Backdoor-Looking Bug I've Ever Seen"
# by Filippo Valsorda (https://words.filippo.io/dispatches/telegram-ecdh/)

# In short: adding a nonce to Diffie-Hellman and allowing a third party to
# control it creates the possibility for an undetected MitM attack.
# The third part can obtain the shared key and participate in the conversation,
# and thus leak any sensitive information

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

    def calculate_key(self, key):
        self.key = b64encode(key.to_bytes(32, 'little'))
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

r.readuntil(b'nonce to Alice: ')
bob_nonce = int(r.readline()[:-1])

mitm = Party()

# Send fake public key to Bob
r.readuntil(b'public key: ')
r.sendline(str(mitm.public).encode('utf-8'))

# Send fake public key to Alicd
r.readuntil(b'public key: ')
r.sendline(str(mitm.public).encode('utf-8'))

# nonce_alice = A^t mod p  XOR  B^t mod p  XOR  nonce_bob
alice_nonce = pow(alice_pk, mitm.private, p) ^ pow(bob_pk, mitm.private, p) ^ bob_nonce
r.readuntil(b'nonce from you: ')
r.sendline(str(alice_nonce).encode('utf-8'))

# key_alice = T^a mod p  XOR  nonce_alice =
#   T^a mod p  XOR  (A^t mod p  XOR  B^t mod p  XOR  nonce_bob) =
#   B^t mod p  XOR  nonce_bob = key_bob
key = pow(bob_pk, mitm.private, p) ^ bob_nonce
mitm.calculate_key(key)

r.readuntil(b"sends to Bob: b'")
a2b = r.readline()[:-2]
print(mitm.decrypt(a2b))

r.readuntil(b"replies to Alice: b'")
b2a = r.readline()[:-2]
print(mitm.decrypt(b2a))
