# Тема урока: работа с целыми числами

# task 1 Три последовательных числа
num = int(input())
print(num)
print(num + 1)
print(num + 2)

# task 2 Сумма трёх чисел
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 + num2 + num3)

# task 3 Куб
num = int(input())
print('Объем =', num * num * num)
print('Площадь полной поверхности =', 6 * num * num)

# task 4 Значение функции
a = int(input())
b = int(input())
f = 3 * (a + b)**3 + 275 * b**2 - 127 * a - 41
print(f)

# task 5 Следующее и предыдущее
num = int(input())
print('Следующее за числом', num, 'число:', num + 1)
print('Для числа', num, 'предыдущее число:', num - 1)

# task 6 Стоимость покупки
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(3 * (a + b + c + d))

# task 7 Арифметические операции
a = int(input())
b = int(input())
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)

# task 8 Арифметическая прогрессия
a = int(input())
d = int(input())
n = int(input())
print(a + d * (n - 1))

# task 7 Разделяй и властвуй
x = int(input())
print(x, x*2, x*3, x*4, x*5, sep='---')
