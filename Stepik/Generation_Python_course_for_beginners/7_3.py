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

# task 5 Сумма чисел 2
