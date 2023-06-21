# Тема урока: строки


s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')

# task 3 В столбик 1
s = input()
for i in range(0, len(s), 2):
    print(s[i])

# task 4 В столбик 2
s = input()
n = len(s)
for i in range(n -1, -1, -1):
    print(s[i])

# task 5 ФИО
i, f, o = (input() for _ in range(3))
print(f[0] + i[0] + o[0])

# task 6 Цифра 1
s, summ = input(), 0
for i in s:
    summ += int(i)
print(summ)

# task 7 Цифра 2
s = input()
for i in s:
    if i in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')

# task 8 Цифра 2Сколько раз?
s, c_plus, c_star = input(), 0, 0
for i in s:
    if i == '*':
        c_star += 1
    if i == '+':
        c_plus += 1
print(f'Символ + встречается {c_plus} раз')
print(f'Символ * встречается {c_star} раз')

# task 9 Одинаковые соседи
s, count = input(), 0
for i in range(len(s)-1):
    if s[i] == s[i + 1]:
        count += 1
print(count)

# task 10 Гласные и согласные
s, c_gl, c_sgl = input(), 0, 0
for i in s:
    if i.lower() in 'аяуюоеёэиы':
        c_gl += 1
    if i.upper() in 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        c_sgl += 1
print(f'Количество гласных букв равно {c_gl}')
print(f'Количество согласных букв равно {c_sgl}')

s, c_gl, c_sgl = input().lower(), 0, 0
for i in s:
    if i in 'аяуюоеёэиы':
        c_gl += 1
    if i in 'бвгджзйклмнпрстфхцчшщ':
        c_sgl += 1
print(f'Количество гласных букв равно {c_gl}')
print(f'Количество согласных букв равно {c_sgl}')

# task 11 Decimal to Binary
n = int(input())
print(bin(n)[2:])

n = int(input())
b = ''
while n > 0:
    b = str(n % 2) + b
    n //= 2
print(b)
