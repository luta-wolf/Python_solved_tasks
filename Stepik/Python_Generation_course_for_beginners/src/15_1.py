# Тема урока: модуль random

import random

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)

print(num1)
print(num2)

import random

print('Бросаем кубики... ')
print('Значения граней:')
print(random.randint(1, 6))
print(random.randint(1, 6))

import random

numbers = list(range(2, 10, 2)) + [3]
print(numbers)

num = random.choice(numbers)
print(num)
