# Вложенные циклы. Часть 2

# task 1 Численный треугольник 3
n, count = int(input()), 0
for i in range(1, n + 1):
    for j in range(n - i, n):
        count += 1
        print(count, end=' ')
    print()

n = int(input())
cur = 1
for i in range(n):
    for _ in range(i + 1):
        print(cur, end=" ")
        cur += 1
    print()

# task 2 Численный треугольник 4
n = int(input())
if n == 1:
    print(1)
for i in range(n):
    flag = 1
    count = 0
    for j in range(1, n*n):
        count += flag
        if count == 0:
            break
        print(count, end='')
        if j > i:
            flag = -1
    print()

num = int(input())
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end ='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()

# task 3 Делители-1 🌶️
a, b, digit, summ = int(input()), int(input()), 0, 0
for i in range(a, b + 1):
    s = 0
    for j in range(1, i + 1):
        if i % j == 0:
            s += j
    if s >= summ:
        summ = s
        digit = i
print(digit, summ)

# task 4 Делители-2
n, summ = int(input()), 0
for i in range(1, n + 1):
    s = 0
    for j in range(1, i + 1):
        if i % j == 0:
            s += 1
    print(str(i) + '+' * s)

# task 5 Цифровой корень
n = int(input())
for i in range(len(str(n)) + 1):
    summ = 0
    while n > 0:
        d = n % 10
        summ += d
        n //= 10
    n = summ
print(d)

# task 6 Сумма факториалов
from math import factorial
n, summ = int(input()), 0
for i in range(1, n + 1):
    summ += factorial(i)
print(summ)

# task 7 Простые числа
a, b, flag = int(input()), int(input()), 0
for i in range(a, b + 1):
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag += 1
    if flag <= 0 and i != 1:
        print(i)
