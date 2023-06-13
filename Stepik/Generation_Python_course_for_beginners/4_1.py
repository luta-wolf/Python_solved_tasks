# Тема урока: условный оператор

# task 1 Пароль
str1, str2 = input(), input()
if str1 == str2:
    print('Пароль принят')
else:
    print('Пароль не принят')


print('Пароль принят' if input() == input() else 'Пароль не принят')

# task 2 Четное или нечетное?
num = int(input())
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# task 3 Соотношение
num = int(input())
d1 = (num // 10**3) % 10
d2 = (num // 10**2) % 10
d3 = (num // 10**1) % 10
d4 = (num // 10**0) % 10
if d1 + d4 == d2 - d3:
    print('ДА')
else:
    print('НЕТ')

# task 4 Роскомнадзор
age = int(input())
if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# task 5 Арифметическая прогрессия
a, b, c, = int(input()), int(input()), int(input())
if b - a == c - b:
    print('YES')
else:
    print('NO')

# task 6 Наименьшее из двух чисел
a, b = int(input()), int(input())
print(a if a < b else b)

# task 7 Наименьшее из четырёх чисел 🌶️
a, b, c, d = int(input()), int(input()), int(input()), int(input())
min_d = a
if b < min_d:
    min_d = b
if c < min_d:
    min_d = c
if d < min_d:
    min_d = d
print(min_d)

# task 8 Возрастная группа
age = int(input())
if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if age >= 60:
    print('старость')

# task 9 Только + 🌶️
a, b, c = int(input()), int(input()), int(input())
sum_d = 0
if a >= 0:
    sum_d += a
if b >= 0:
    sum_d += b
if c >= 0:
    sum_d += c
print(sum_d)
