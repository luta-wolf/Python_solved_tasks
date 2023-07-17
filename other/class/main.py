from hello import *

import time
n = 1000

st_t = time.time()
lst = []
for i in range(n):
    lst.append(i)
print(time.time() - st_t)

st_t = time.time()
lst = [i for i in range(n)]
print(time.time() - st_t)