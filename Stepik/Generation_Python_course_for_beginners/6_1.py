# Тема урока: числовые типы данных

# task 1 Площадь треугольника
a, b = float(input()), float(input())
print(a * b / 2 )

# task 2 Две старушки
s, v1, v2 = float(input()), float(input()), float(input())
print(s / (v1 + v2))

# task 3 Обратное число
n = float(input())
if n == 0:
    print('Обратного числа не существует')
else:
    print(1 / n)

# task 4 451 градус по Фаренгейту
f = float(input())
print((f - 32) * 5 / 9)

# task 5 Dog age
age = float(input())
if 0 < age <= 2:
    print(age * 10.5)
else:
    print(21 + (age - 2) * 4)

# task 6 Первая цифра после точки
n = float(input())
print(int(n * 10) % 10)

# task 7 Дробная часть
n = float(input())
print(n - int(n))

# task 8 Наибольшее и наименьшее
n1, n2, n3, n4, n5 = int(input()), int(input()), int(input()), int(input()), int(input())
print('Наименьшее число =', min(n1, n2, n3, n4, n5))
print('Наибольшее число =', max(n1, n2, n3, n4, n5))

# task 9 Сортировка трёх 🌶️
n1, n2, n3 = int(input()), int(input()), int(input()),
print(max(n1, n2, n3))
print(n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3))
print(min(n1, n2, n3))

# task 10 Интересное число
n = int(input())
d1 = (n // 10**2) % 10
d2 = (n // 10**1) % 10
d3 = (n // 10**0) % 10
if max(d1, d2, d3) - min(d1, d2, d3) == d1 + d2 + d3 - max(d1, d2, d3) - min(d1, d2, d3):
    print('Число интересное')
else:
    print('Число неинтересное')

# task 11 Абсолютная сумма
a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

lst = map(float, [input() for _ in range(5)])
print(sum(map(abs, lst)))

# task 11 Манхэттенское расстояние
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))

p1, p2, q1, q2 = [int(input()) for i in range(4)]
print(abs(p1 - q1) + abs(p2 - q2))
