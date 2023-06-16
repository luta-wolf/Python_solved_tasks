# Тема урока: строки - Методы и функции

# task 1 Заглавные буквы
s = input()
print('YES' if s == s.title() else 'NO')

# task 2 sWAP cASE
s = input()
print(s.swapcase())

# task 3 Хороший оттенок
s = input()
print('YES' if 'хорош' in s.lower() else'NO')

# task 4 Нижний регистр
s, count = input(), 0
for i in s:
    if i == i.lower() and i.isalpha():
        count += 1
print(count)

s, count = input(), 0
for i in s:
    if i != i.upper():
        count += 1
print(count)
