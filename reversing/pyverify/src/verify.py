from random import shuffle, seed

solution = [54, 242, 105, 236, 54, 55, 204, 159, 170, 116, 158, 254, 248, 170, 133, 8, 133, 116, 248, 225, 170, 141, 245, 170, 18, 8, 170, 193, 116, 169, 158, 53]

seed(42)
LUT = list(range(256))
shuffle(LUT)

def sub(first):
    return [LUT[a] for a in first]

def add(block, i):
    return [(a + i) % 256 for a in block]

password = input("Enter flag: ")
# check length
if len(password) != 32:
    print("Invalid length")
    exit(1)

# split up into blocks of 16
password = [bytes(password[i:i+16], encoding="ascii") for i in range(0, len(password), 16)]
password = [[a for a in block] for block in password]

for i in range(2**128): # super duper secure
    # perform lookup table
    password = [sub(block) for block in password]
    # add each block by i
    password = [add(block, i) for block in password]

#flatten 
password = [a for block in password for a in block]
if password == solution:
    print("Correct!")
else:
    print("Incorrect!")