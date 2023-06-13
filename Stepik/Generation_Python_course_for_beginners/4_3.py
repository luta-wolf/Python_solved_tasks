# Тема урока: условный оператор

# task 1 Гонка спидстеров
zum, flash = int(input()), int(input())
if flash > zum:
    print('YES')
elif flash < zum:
    print('NO')
else:
    print("Don't know")

# task 2 Вид треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

# task 3 Среднее число
a, b, c = int(input()), int(input()), int(input())
midle = a
if a < b < c or c < b < a:
    midle = b
if b < a < c or c < a < b:
    midle = a
if a < c < b or b < c < a:
    midle = c
print(midle)

# task 4 Количество дней
n = int(input())
if n == 4 or n == 6 or n == 9 or n == 11:
    print(30)
elif n == 2:
    print(28)
else:
    print(31)

# task 5 Церемония взвешивания
n = int(input())
if n < 60:
    print('Легкий вес')
elif n < 64:
    print('Первый полусредний вес')
elif n < 69:
    print('Полусредний вес')

# task 6 Самописный калькулятор 🌶️
a, b, s = int(input()), int(input()), input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/' and b != 0:
    print(a / b)
elif s == '/' and b == 0:
    print('На ноль делить нельзя!')
else:
    print('Неверная операция')

# task 7 Цветовой микшер 🌶️
col1, col2 = input(), input()
if col1 != 'красный' and col1 != 'синий' and col1 != 'желтый' or col2 != 'красный' and col2 != 'синий' and col2 != 'желтый':
    print('ошибка цвета')
elif col1 == col2 == 'красный':
    print('красный')
elif col1 == col2 == 'синий':
    print('синий')
elif col1 == col2 == 'желтый':
    print('желтый')
elif col1 == 'красный' and col2 == 'синий' or col2 == 'красный' and col1 == 'синий':
    print('фиолетовый')
elif col1 == 'красный' and col2 == 'желтый' or col2 == 'красный' and col1 == 'желтый':
    print('оранжевый')
elif col1 == 'синий' and col2 == 'желтый' or col2 == 'синий' and col1 == 'желтый':
    print('зеленый')

# task 8 Цвета колеса рулетки 🌶️
n = int(input())
if 0 <= n <= 36:
    if n == 0:
        print('зеленый')
    elif 1 <= n <= 10 and n % 2 != 0 or 11 <= n <= 18 and n % 2 == 0 or 19 <= n <= 28 and n % 2 != 0 or 29 <= n <= 36 and n % 2 == 0:
        print('красный')
    else:
        print('черный')

else:
    print('ошибка ввода')

# task 9 Пересечение отрезков 🌶️🌶️
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2  or b2 < a1:
    print('пустое множество')
elif b1 == a2:
    print(b1)
elif a1 == b2:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif a2 == a1 and b1 == b2:
    print(a1, b1)
