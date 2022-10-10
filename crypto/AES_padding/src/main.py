# simple padding oracle attack
from os import urandom
from Cryptodome.Cipher import AES
FLAG = open('flag.txt', 'r').read()
secret = urandom(16)

print("""
###################################################################################
   ___  ____     __  ____   __ __  ____  ______   ___   ____   ____  ______    ___ 
  /  _]|    \   /  ]|    \ |  |  ||    \|      | /   \ |    \ |    ||      |  /  _]
 /  [_ |  _  | /  / |  D  )|  |  ||  o  )      ||     ||  _  | |  | |      | /  [_ 
|    _]|  |  |/  /  |    / |  ~  ||   _/|_|  |_||  O  ||  |  | |  | |_|  |_||    _]
|   [_ |  |  /   \_ |    \ |___, ||  |    |  |  |     ||  |  | |  |   |  |  |   [_ 
|     ||  |  \     ||  .  \|     ||  |    |  |  |     ||  |  | |  |   |  |  |     |
|_____||__|__|\____||__|\_||____/ |__|    |__|   \___/ |__|__||____|  |__|  |_____|                                                                                 
###################################################################################
""")
print("""Welcome to the AWS Encryptonite service!
For only 1000$ per month, we will encrypt your data for you!
But because we're so nice and generous, we'll give you a free trial!
Just send us your data and we'll encrypt it for you!

Because of our secret padding scheme (TM), your data is more secure than ever before.
""")
while True:
    try:
        print("Enter your message: ", end="")
        msg = input() + FLAG
        msg = msg + (16 - len(msg) % 16) * chr(16 - len(msg) % 16)
        msg = bytes(msg, encoding="ascii")
        cipher = AES.new(secret, AES.MODE_ECB)
        print("Here's your encrypted message: " + cipher.encrypt(msg).hex())
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print("Oops, something went wrong!\nWe'll report this to Jeff Bezos!")

        