# Тема урока: цикл for

# task 1 Python is awesome
for i in range(10):
    print('Python is awesome!')

# task 2 Повторяй за мной 1
line, n = input(), int(input())
for i in range(n):
    print(line)

# task 3 Последовательность символов
for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')

# task 4 Звездный прямоугольник
n = int(input())
for i in range(n):
    print('*' * 19)

# task 5 Повторяй за мной 2
line = input()
for i in range(10):
    print(i, line)

# task 6 Квадрат числа
n = int(input())
for i in range(n + 1):
    print(f'Квадрат числа {i} равен {i * i}')

# task 7 Звездный треугольник
n = int(input())
for i in range(n, 0, -1):
    print('*' * i)

# task 8 Популяция
m, p, n = int(input()), int(input()), int(input())
pop = m
for i in range(n):
    print(i + 1, pop)
    pop += pop * p / 100
