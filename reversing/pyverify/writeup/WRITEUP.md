# Pyverify

## Description
This challenge is a python script that verifies a flag. It uses some elements of AES without a key. It does a ton of iterations with both an substitution box and a simple addition.

## Solution
An important part of this solution is that unlike AES it doesn't do any ShiftRow or MixColumn. This makes it simple as each byte is practically being changed by itself without its surroundings.

A fun part about computers is their determinism. A function will always returns the same output for the same input. As long as information doesn't get lost and the input and output stay in the same range, you can usually keep doing the same function over and over and get the original input back.

Example:
```python
def add(x):
    return (x + 1) % 256 # mod 256 to constrain the space to 0-255

num = 0
for i in range(256):
    num = add(num)

print(num == 0) # True
```

In the case of the challenge both functions dont lose information and the input and output stay in the same range. So we can just do the same thing over and over and get the original input back. Luckily we know the beginning of the flag so we can just do the same thing over and over and count the iterations until we find the flag.

```python
password = solution
i = 2**128
while True:
    # perform lookup table
    password = [sub(block) for block in password]
    # shift each block by i
    password = [add(block, i) for block in password]
    i+=1
    if password[0][0] == ord('T'):
        print(i)
        break
# T...T©îo4..Æ±4.2..±O4þ.4Ë24A.à.¿
```

Wow, just like that we get the flag... but it looks bad. What happened?
Well 5185 is just the size to complete the cycle of the first byte. The other bytes may be in different cycles (Due to the random lookup table potentially having multiple cycles). So we solved all bytes in that cycle but not the other ones. Lets include some other known bytes:

```python
password = solution
i = 2**128
while True:
    # perform lookup table
    password = [sub(block) for block in password]
    # shift each block by i
    password = [add(block, i) for block in password]
    i+=1
    if password[0][:3] == bytes("TUD", encoding='ascii'):
        print(i)
        break
# TUD`TÌa³_l.ve_cycles_i¸_ìy_§lg.Y
```

We can see that even more cycles got resolved. Now on to the next bytes:

```python
password = solution
i = 2**128
while True:
    # perform lookup table
    password = [sub(block) for block in password]
    # shift each block by i
    password = [add(block, i) for block in password]
    i+=1
    if password[0][:3] == bytes("TUDCTF", encoding='ascii'):
        print(i)
        break
# TUDCTF{I_love_cycles_in_my_algo}
```

That's it! We solved the challenge. You can ofcourse try to reverse it by hand but imo this is also a fun way of solving it. And you will still need to know all the cycles since doing `2**128` operations is kinda unfeasible. The flag is `TUDCTF{I_love_cycles_in_my_algo}`