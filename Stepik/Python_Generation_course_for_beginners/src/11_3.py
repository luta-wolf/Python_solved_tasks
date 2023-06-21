# Тема урока: методы добавления и удаления элементов

# task 1 Все сразу 1 🌶️
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
print('YES' if 5 and 17 in numbers else'NO')
del numbers[0]
del numbers[-1]
print(numbers)

# task 2 Список строк
n = int(input())
lst = []
for _ in range(n):
    s = input()
    lst.append(s)
print(lst)

# task 3 Алфавит
template = ' abcdefghijklmnopqrstuvwxyz'
lst = []
for i in range(1, 27):
    lst.append(template[i] * i)
print(lst)

# task 4 Список кубов
n = int(input())
lst = []
for i in range(n):
    num = int(input())
    lst.append(num**3)
print(lst)

# task 5 Список делителей
n = int(input())
lst = []
for i in range(1, n + 1):
    if n % i == 0:
        lst.append(i)
print(lst)

# task 5 Суммы двух
# 1
n, lst, a, b = int(input()), [], 1, 1
for i in range(n):
    num = int(input())
    a, b = num, a
    lst.append(a + b)
del lst[0]
print(lst)
# 2
seq = []
for _ in range(int(input())):
    seq.append(int(input()))
res = []
for i in range(len(seq) - 1):
    res.append(seq[i] + seq[i+1])
print(res)

# task 6 Удалите нечетные индексы
# 1
n, lst = int(input()), []
for i in range(n):
    lst.append(int(input()))
    if i % 2 != 0:
        del lst[-1]
print(lst)
# 2
n, lst = int(input()), []
for i in range(n):
    lst.append(int(input()))
del lst[1::2]
print(lst)

# task 7 k-ая буква слова 🌶️🌶️
n, lst = int(input()), []
for _ in range(n):
    lst.append(input())
k = int(input())
for i in lst:
    if k <= len(i):
        print(i[k - 1], end='')

# task 8 Символы всех строк
n, lst = int(input()), []
for i in range(n):
    lst.extend(input())
print(lst)


