# Тема урока: частые сценарии
'''
сумматор - подсчитывает сумму
мультипликатор - подсчитывает произведение
'''

# task 1 Количество чисел
a, b = (int(input()) for _ in range(2))
counter = 0
for i in range(a, b + 1):
    if i * i * i % 10 == 4 or i * i * i % 10 == 9:
        counter += 1
print(counter)

# task 2 Сумма чисел
n = int(input())
total = 0
for i in range(n):
    a = int(input())
    total += a
print(total)

n = int(input())
lst = map(float, [input() for _ in range(n)])
print(int(sum(list(lst))))

# task 3 Асимптотическое приближение
from math import log

n = int(input())
total = 1
for i in range(2, n + 1):
    total += 1 / i
print(total - log(n))

# task 4 Сумма чисел 2
n, total = int(input()), 0
for i in range(1, n + 1):
    if i * i % 10 == 2 or i * i % 10 == 5 or i * i % 10 == 8:
        total += i
print(total)

n, total = int(input()), 0
for i in range(1, n + 1):
    if i * i % 10 in [2, 5, 8]:
        total += i
print(total)

# task 5 Факториал
n = int(input())
total = 1
for i in range(1, n + 1):
    total *= i
print(total)

from math import factorial
print(factorial(int(input())))

# task 6 Без нулей
res = 1
for i in range(10):
    n = int(input())
    if n != 0:
        res *= n
print(res)

# task 7 Сумма делителей
n = int(input())
res = 0
for i in range(1, n +1):
    if n % i == 0:
        res += i
print(res)

# task 8 Знакочередующаяся сумма
n, res = int(input()), 0
for i in range(1, n + 1):
    res += (-1)**(i+1) * i
print(res)

# task 9 Наибольшие числа 🌶️🌶️
n, max1, max2 = int(input()), -1, -1
for i in range(n):
    num = int(input())
    if max1 < num:
        max2 = max1
        max1 = num
    elif max2 < num:
        max2 = num
print(max1, max2, sep='\n')

# task 10 Only even numbers 🌶️
flag = True
for _ in range(10):
    n = int(input())
    if n % 2 != 0:
        flag = False
print('YES' if flag else 'NO')

# task 11 Последовательность Фибоначчи 🌶️
n = int(input())
n1, n2 = 0, 1
print(1, end=' ')
for i in range(2, n + 1):
    print(n1 + n2, end=' ')
    n1, n2 = n2, n1 + n2
