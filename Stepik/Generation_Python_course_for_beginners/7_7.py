# Тема урока: ревью кода

'''
Ревью кода – проверка исходного кода программы с целью обнаружения и исправления ошибок и неточностей, которые остались незамеченными при начальной разработке.
В процессе ревью кода могут быть исправлены:

- фактические ошибки;
- производительность кода;
- читабельность кода и ошибки форматирования кода.
Целью ревью кода является улучшение качества программного кода и совершенствование навыков программиста.
'''
# task 1 Ревью кода-1 🌶️🌶️
# до ревью
count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')

# после ревью
count = 0
res = 1					# ошибка 1: p = 0
for i in range(10):		# ошибка №2: range(1, 10)
    x = int(input())
    if x >= 0:			# ошибка № 3: х > 0
        res *= x
        count += 1
if count > 0:
    print(count)		# ошибка № 3: print(x)
    print(res)
else:
    print('NO')

# task 2 Ревью кода-2 🌶️🌶️
# до ревью
mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)

# после ревью
mx = -10**6	- 1			# неверно задана переменная (сравнивать будет с минимальным)
s = 0
for i in range(10):		# неверно задан диапозон (было 11)
    x = int(input())
    if x < 0:
        count += 1
        s += x			# # неверно задана формула (было равенство "=")
        if x > mx:		# смещен блок кода, чтобы условие работало только для x < 0
            mx = x
if count > 0:			# не был задано условие для вывода при отсутствии отрицательных чисел
    print(s)
    print(mx)
else:
    print('NO')

# task 3 Ревью кода-3
# до ревью
s = 1
for i in range(1, 7):
    n = input()
    if i % 2 == 0:
        s = s + n
print(s)
# после ревью
s = 0					# неверно задана переменная
for _ in range(7):		# неверно задан диапозон
    n = int(input())	# приведение типов
    if n % 2 == 0:		# обработка числа
        s += n
print(s)

# task 4 Ревью кода-4 🌶️🌶️
# до ревью
n = int(input())
max_digit = n % 10
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit < max_digit:
            digit = max_digit
    n = n % 10
if max_digit == 0:
    print('NO')
else:
    print(max_digit)
# после ревью
n = int(input())
max_digit = -1 #
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit: #
            max_digit = digit #
    n = n // 10 #
if max_digit == -1: #
    print('NO')
else:
    print(max_digit)

# task 5 Ревью кода-5 🌶️
# до ревью
n = int(input())
while n > 0:
    n %= 10
print(n)
# после ревью
n, digit = int(input()), -1
while n > 0:
    digit = n % 10
    n //= 10
print(digit)

n = int(input())
while n > 9:
    n //= 10
print(n)

# task 6 Ревью кода-6
# до ревью
n = input()
product = n % 10
while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)
# после ревью
n = int(input()) #
product = 1 #
while n > 0: #
    digit = n % 10
    product *= digit
    n //= 10
print(product)
