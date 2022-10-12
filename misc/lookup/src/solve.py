from multiprocessing import Pool
from requests import get
import string


possible = string.ascii_letters+string.digits

def req(x):
    s = f'https://drive.google.com/file/d/1wbQE3UBemjvWO3dh5KhtBfYB05ZQ1L{x}'
    code = get(s).status_code

    if (code == 200):
        print(s)

v = []

for i in possible:
    for j in possible: v.append(i+j)

with Pool(50) as P:
    P.map(req, v)
