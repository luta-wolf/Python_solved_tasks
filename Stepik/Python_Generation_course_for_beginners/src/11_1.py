# Тема урока: введение в списки

# task 1 Список чисел
n = int(input())
print(list(range(1, n + 1)))

# task 2 Список букв
# 1
n = int(input())
template = 'abcdefghijklmnopqrstuvwxyz'
print(list(template[:n]))
# 2
n, s = int(input()), ''
for i in range(97, 97 + n):
    s = s + chr(i)
print(list(s))
#3
n = int(input())
s = ''
for i in range(n):
    s += chr(97 + i)
print(list(s))
