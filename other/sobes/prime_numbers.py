d = {1: 'one', 2: 'two'}
d[1] = 'three'
print(d)

from datetime import datetime
import time

time2 = datetime.now()
time1 = time.time()

lst = [el for el in range(1, 1000001)]

for el in lst:
    flag = 1
    for i in range(2, int(el**0.5) + 1):
        if el % i == 0 :
            flag = 0

    if flag:
        print(el)

a = time.time() - time1
print(datetime.now() - time2)
print(time.time() - time1)

from datetime import datetime
import time

time2 = datetime.now()
time1 = time.time()

lst = [el for el in range(1, 1000001)]

for el in lst:
    flag = 1
    j = 1
    for i in range(2, int(el**0.5) + 1, j):
        j += 1
        if el % i == 0 :
            flag = 0

    if flag:
        print(el)

print(datetime.now() - time2)
print(time.time() - time1)
print(a)
