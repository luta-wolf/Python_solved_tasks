# Экзамен

# task 1 Звездный прямоугольник
print('*' * 17)
print('*' + ' ' * 15 + '*', sep='')
print('*' + ' ' * 15 + '*', sep='')
print('*' * 17)

# task 2 Сумма квадратов VS квадрат суммы
a = int(input())
b = int(input())
print('Квадрат суммы', a, 'и', b, 'равен', (a + b)**2)
print('Сумма квадратов', a, 'и', b, 'равна', a**2 + b**2)

# task 3 Большое число
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b + c**d)

# task 4 Размножение n-ок
a = int(input())
print(a + a + a*10 + a + a*10 + a*100)
