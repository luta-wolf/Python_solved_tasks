# Тема урока: цикл while

# task 1 До КОНЦА 1
line = input()
while line != 'КОНЕЦ':
    print(line)
    line = input()

# task 2 До КОНЦА 2
line = input()
while not (line == 'КОНЕЦ' or line == 'конец'):
    print(line)
    line = input()

# task 3 Количество членов
line, words = input(), ('стоп', 'хватит', 'достаточно')
res = 0
while line not in words:
    res += 1
    line = input()
print(res)

# task 4 Пока делимся
n = int(input())
while n % 7 == 0:
    print(n)
    n = int(input())

# task 5 Сумма чисел
n, res = int(input()), 0
while n >= 0:
    res += n
    n = int(input())
print(res)

# task 6 Количество пятерок
n, res = int(input()), 0
while n >= 1 and n <= 5:
    if n == 5:
        res += 1
    n = int(input())
print(res)

# task 7 Количество пятерок
n, res = int(input()), 0
while n >= 1 and n <= 5:
    if n == 5:
        res += 1
    n = int(input())
print(res)

# task 7 Ведьмаку заплатите чеканной монетой
n, count = int(input()), 0
tmp = n // 25
count += tmp
n = n - tmp * 25
tmp = n // 10
count += tmp
n = n - tmp * 10
tmp = n // 5
count += tmp
n = n - tmp * 5
count += n
print(count)
