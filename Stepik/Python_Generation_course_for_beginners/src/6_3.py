# Тема урока: модуль math

from math import *

# task 1 Евклидово расстояние
x1, y1, x2, y2 = [float(input()) for _ in range(4)]
print(sqrt((x1 - x2)**2 + (y1 - y2)**2))

# task 2 Площадь и длина
r = float(input())
print(pi * r**2)
print(pi * r * 2)

# task 3 Средние значения
a, b = (float(input()) for _ in range(2))
print((a + b) / 2)				# Cреднее арифметическое
print(sqrt(a * b))				# Среднее геометрическое
print(2 * a * b / (a + b))		# Cреднее гармоническое
print(sqrt((a**2 + b**2) / 2))	# Среднее квадратичное

# task 4 Тригонометрическое выражение
x = float(input())
r = x * pi / 180
print(sin(r) + cos(r) + tan(r)**2)

# task 5 Пол и потолок
x = float(input())
print(floor(x) + ceil(x))

# task 6 Квадратное уравнение 🌶️🌶️
a, b, c = (float(input()) for i in range(3))
d = b**2 - 4 * a * c
if d > 0:
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
elif d == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')

# task 7 Правильный многоугольник
n, a = int(input()), float(input())
print(n * a **2 / (4 * tan(pi / n)))
