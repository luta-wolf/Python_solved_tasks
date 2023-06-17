# Тема урока: цикл for

# task 1 Последовательность чисел 1
m, n = (int(input()) for _ in range(2))
for i in range(m, n + 1):
    print(i)

# task 2 Последовательность чисел 2 🌶️
m, n = (int(input()) for _ in range(2))
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

# task 3 Последовательность чисел 3 🌶️
m, n = (int(input()) for _ in range(2))
for i in range(m, n - 1, -1):
    if i % 2 != 0:
        print(i)

# task 4 Последовательность чисел 4
m, n = (int(input()) for _ in range(2))
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)

# task 5 Таблица умножения
n = int(input())
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
