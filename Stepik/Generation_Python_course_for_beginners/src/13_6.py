# Тема урока: функции с возвратом значения

# task 1 Середина отрезка
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    pass

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# task 2 Площадь и длина
from math import pi

# объявление функции
def get_circle(radius):
    length = 2 * pi * r
    area = pi * r ** 2

    return length, area


# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)

# task 3 Корни уравнения 🌶️🌶️
# объявление функции
def solve(a, b, c):
    d = b**2 - 4 * a * c
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    if x1 >= x2:
        return x2, x1
    else:
        return x1, x2

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
