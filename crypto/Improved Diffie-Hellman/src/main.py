from secrets import randbits
from cryptography.fernet import Fernet
from os import environ
from base64 import b64encode

p = 0xfd67a3b76136aaeb345f4175f38e65cad628e6535e7fc40f5e7952e7799d1b23
g = 0x2

class Party:
    def __init__(self) -> None:
        self.private = randbits(128)
        self.public = pow(g, self.private, p)

    def calculate_key(self, other_public, nonce):
        self.key = (pow(other_public, self.private, p) ^ nonce)
        print("key is", self.key)
        self.key = b64encode(self.key.to_bytes(32, 'little'))
        self.f = Fernet(self.key)

    def encrypt(self, plaintext):
        return self.f.encrypt(plaintext)

    def decrypt(self, ciphertext):
        return self.f.decrypt(ciphertext)

print("Alice and Bob are trying send some sensitive information via you.")
print("Because they are not sure if you can be trusted, they have decided to")
print("encrypt the information before sending it.")
print()
print("They decide to use an Improved Diffie-Hellman key exchange\u2122.")
print("It contains a nonce for extra randomness and security.")
print()

try:
    alice = Party()
    bob = Party()

    print(f"Alice's public key is {alice.public}")
    print(f"Bob's public key is {bob.public}")

    bobs_nonce = randbits(32 * 8)
    print(f"Bob requests you to send his nonce to Alice: {bobs_nonce}")

    bobs_copy = int(input("Bob requests Alice's public key: "))

    alices_copy = int(input("Alice requests Bob's public key: "))
    alices_nonce = int(input("Alice requests the Bob's nonce from you: "))

    print("Alice and Bob are calculating their shared key...")
    alice.calculate_key(alices_copy, alices_nonce)
    bob.calculate_key(bobs_copy, bobs_nonce)

    print('Just to be sure, Alice and Bob verify via a different channel that their key matches.')
    if alice.key != bob.key:
        print("The keys do not match! Someone has manipulated the key exchange! Exiting...")
        exit(0)
    else:
        print("The keys match! Secure communication channel has been established. Nobody should be able to listen in")

    a = alice.encrypt(b"Hey Bob, can you send me the flag?")
    print(f"Alice sends to Bob: {a}")
    bob.decrypt(a)
    b = bob.encrypt(b"Sure! The flag is " + environ['FLAG'].encode('utf-8'))
    print(f"Bob replies to Alice: {b}")
    print("Alice and Bob closed their communication channel")
except Exception as e:
    print(f"An error occured: {e}. Exiting...")
    exit(1)
