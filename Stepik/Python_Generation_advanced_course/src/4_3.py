# task 1 Список по образцу 1
# 1
n = int(input())
lst = []
for i in range(n):
    lst.append([int(i) for i in range(1, n + 1)])
for el in lst:
    print(el)

# 2
n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')

# task 2 Список по образцу 2
# 1
n = int(input())
for i in range(1, n + 1):
    print([el for el in range(1 , i + 1)])

# 2
n = int(input())
result = []

for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))

print(*result, sep='\n')

# task 3 Треугольник Паскаля 1 🌶️
# обучающее видео https://www.youtube.com/watch?v=jTxY1Cgs3Mw&ab_channel=Amulya%27sAcademy
def pascal(n):
    lst = []
    for i in range(n + 1):
        tmp_lst = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp_lst.append(1)
            else:
                tmp_lst.append(lst[i - 1][j] + lst[i - 1][j - 1])
        lst.append(tmp_lst)
    return lst[n]

n = int(input())
print(pascal(n))

# task 4 Треугольник Паскаля 2
# 1
def pascal(n):
    lst = []
    for i in range(n):
        tmp_lst = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp_lst.append(1)
            else:
                tmp_lst.append(lst[i - 1][j - 1] + lst[i - 1][j])
        lst.append(tmp_lst)
    return lst

n = int(input())
pascal = pascal(n)
for el in pascal:
    print(*el)

# 2
#-------------------ФУНКЦИЯ-------------------
def pascal(n):
    lst = []
    for i in range(n):
        tmp_lst = []
        for j in range(i + 1):
            if j == 0 or j == i:
                tmp_lst.append(1)
            else:
                tmp_lst.append(lst[i - 1][j - 1] + lst[i - 1][j])
        lst.append(tmp_lst)
    return lst

#--------------------ВЫЗОВ--------------------
[print(*row) for row in pascal(int(input()))]

# task 5 Упаковка дубликатов 🌶️
s = input().split()
s = ''.join(s) + ' '
lst = []
cnt = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        cnt += 1
    else:
        lst.append(list(s[i]) * cnt)
        cnt = 1

print(lst)

# task 6 Разбиение на чанки 🌶️
# 1
def chunked(s, n):
    s = ''.join(s)
    lst, tmp, cnt = [], [], 0
    for i in range(len(s)):
        cnt += 1
        tmp.append(s[i])
        if cnt % n == 0:
            lst.append(tmp)
            tmp = []
    cnt = 0
    for el in lst:
        cnt += len(el)
    if cnt != len(s):
        lst.append(tmp)
    return lst

s, n = input().split(), int(input())
print(chunked(s, n))

# 2
def chunked(s, n):
    lst = []
    for i in range(0, len(s), n):
        lst.append(s[i:i + n])
    return lst

s, n = input().split(), int(input())
print(chunked(s, n))

# task 7 Подсписки списка 🌶️🌶️
