from random import shuffle, seed

seed(42)
LUT = list(range(256))
shuffle(LUT)

def sub(first):
    return [LUT[a] for a in first]

def add(block, i):
    return [(a + i) % 256 for a in block]

# split up into blocks of 16
password = [[54, 242, 105, 236, 54, 55, 204, 159, 170, 116, 158, 254, 248, 170, 133, 8], [133, 116, 248, 225, 170, 141, 245, 170, 18, 8, 170, 193, 116, 169, 158, 53]]

i = 2**128
while True:
    # perform lookup table
    password = [sub(block) for block in password]
    # shift each block by i
    password = [add(block, i) for block in password]
    i+=1
    if password[0][0] == ord('T') and password[0][1] == ord('U') and password[0][2] == ord('D') and password[0][3] == ord('C') and password[0][4] == ord('T') and password[0][5] == ord('F') and password[0][6] == ord('{'):
        print(i)
        break

#flatten 
password = [a for block in password for a in block]
print(password)
# then put into cyberchef.
# in the end 22049280 was the correct number of iterations