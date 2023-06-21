# Экзамен

# task 1 Начало столетия
n = int(input())
n3 = (n // 10**1) % 10
n4 = (n // 10**0) % 10
if n4 == n3 == 0:
    print('YES')
else:
    print('NO')

# task 2 Шахматная доска
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

# task 3 Girls only
age, sex = int(input()), input()
if 10 <= age <= 15 and sex == 'f':
    print('YES')
else:
    print('NO')

# task 4 Римские цифры
n = int(input())
i, v , x, res = 'I', 'V', 'X', ''
if  n < 1 or n > 10:
    print('ошибка')
if n < 4:
    print('I' * n)
elif n == 4:
    print('I' + 'V')
elif n == 5:
    print('V')
elif n < 9:
    print('V' + 'I' * (n-5))
elif n == 9:
    print('I' + 'X')
elif n == 10:
    print('X')

# task 5 YES or NO вот в чем вопрос
n = int(input())
if n % 2 != 0 or n % 2 == 0 and 6 <= n <= 20:
    print('YES')
elif n % 2 == 0 and 2 <= n <= 5 or n % 2 == 0 and n > 20:
    print('NO')

# task 6 Ход слона 🌶️
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2)**2 == (y1 -y2)**2:
    print('YES')
else:
    print('NO')

# task 7 Ход коня
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2)**2 == 4 and (y1 - y2)**2 == 1 or (y1 - y2)**2 == 4 and (x1 - x2)**2 == 1:
    print('YES')
else:
    print('NO')


# task 8 Ход ферзя
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2)**2 == (y1 -y2)**2 or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
