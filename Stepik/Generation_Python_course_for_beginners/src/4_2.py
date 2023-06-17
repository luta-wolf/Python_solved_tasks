# Тема урока: логические операторы
'''
Таблица истинности для оператора and. В ней перечислены выражения, соединённые оператором and,
показаны все возможные комбинации истинности и ложности и приведены результирующие значения выражений.

a		b		a and b
False	False	False
False	True	False
True	False	False
True	True	True

Таблица истинности для оператора or.

a		b		a or b
False	False	False
False	True	True
True	False	True
True	True	True

Таблица истинности для оператора not:

a		not a
False	True
True	False

Приоритет выполнения следующий:

в первую очередь выполняется логическое отрицание not;
далее выполняется логическое умножение and;
далее выполняется логическое сложение or.
Для явного указания порядка выполнения условных операторов используют скобки.
'''

# task 1 Принадлежность 1
num = int(input())
if -1 < num < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# task 2 Принадлежность 2
num = int(input())
if num <= -3 or num >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')

# task 3 Принадлежность 3
num = int(input())
if -30 < num <= -2 or 7 < num <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

# task 4 Красивое число 🌶️
num = int(input())
if 999 < num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')

# task 5 Неравенство треугольника
a, b, c = int(input()), int(input()), int(input())
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')

# task 6 Високосный год
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

# task 7 Ход ладьи
a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if a1 == b1 or a2 == b2:
    print('YES')
else:
    print('NO')

# task 8 Ход короля 🌶️
a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if -1 <= a1 - b1 <= 1 and -1 <= a2 - b2 <= 1:
    print('YES')
else:
    print('NO')
