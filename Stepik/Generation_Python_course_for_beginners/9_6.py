# Тема урока: представление строк в памяти компьютера, ASCII и Unicode
'''
ASCII (American Standard Code for Information Interchange – американский стандартный код обмена информацией).
UTF (Unicode transformation format) - Формат преобразования Юникод.
'''
# task 1 Символы в диапазоне
a, b = (int(input()) for _ in range(2))
for i in range(a, b + 1):
    print(chr(i), end=" ")

# task 2 Простой шифр
s = input()
for i in s:
    print(ord(i), end=" ")

# task 3 Шифр Цезаря 🌶️
#1
n, s = int(input()), input()
template = 'abcdefghijklmnopqrstuvwxyz'
for i in s:
    temp = ord(i) - n
    if temp < 97:
        temp = -(97 - temp)
        print(template[temp:temp + 1], end="")
    else:
        print(chr(temp), end="")
#2
n, s = int(input()), input()
for i in s:
    temp = ord(i) - n
    if temp < 97:
        temp += 26
    print(chr(temp), end = '')

#3
n, s = int(input()), input()
a = 'abcdefghijklmnopqrstuvwxyz'
for c in s:
    print(a[a.find(c) - n], end='')
