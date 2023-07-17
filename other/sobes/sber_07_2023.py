lst = [el for el in range(1, 1001)]

for el in lst:
    flag = 1
    for i in range(2, el):
        if el % i == 0 :
            flag = 0
    if flag:
        print(el)
