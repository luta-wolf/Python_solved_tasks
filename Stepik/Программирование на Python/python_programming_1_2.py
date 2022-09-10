# 1) Операторы, переменные, типы данных, условия
# print("3 * 5 =", int(3 * 5))
# print(11111 * 1111111)
# print(40/8)
# print(40//8)
# print(42/8)
# print(42//8)
# print(42 % 8)
# print(42 / (4 + 2 * (-2)))
# print(2014 ** 14)
# a = -+42
# print(a)
# print(0.5 + 0.2)
# print(1/3)
# print(0.333 + 0.333 + 0.333)
# print(5e-1)
# print(2014.0 ** 14)
# print(7//3)
# # Типы числовые и строковые
# # int float bool
# # str
# print("-" * 25)
# print(9**19 - int(float(9**19)))
# print(type(7))
# print(type(7.0))
# 3
# def foo():
#     a = 2.0
# a = 2
# print(type(a))
# a = 'abacaba'
# print(type(a))
# a = foo()
# print(type(a))
# a = int(input("Input first digital "))
# b = int(input("Input second digital "))
# print(a, "*", b , "=", a * b)
# name = input("enter your name ")
# print("Hello, ", name)
# a = int(input("enter digital"))
# print(a * 2)

# x = int(input())
# hour = x // 60
# min = x % 60
# print(hour)
# print(min)
# X=int(input())
# print(f"{X//60}\n{X%60}")
# sleepTime = int(input())
# hour = int(input())
# minute = int(input())
# if (minute + sleepTime%60 < 60):
#     print(hour + sleepTime//60)
#     print(minute + sleepTime%60)
# else:
#     print(hour + 1 + sleepTime // 60)
#     print(minute + sleepTime % 60 - 60)

# sleep_time = int(input())
# hour = int(input())
# minute = int(input())
# time = hour * 60 + sleep_time + minute
# print(time//60)
# print(time%60)

# x or y , x and y , not x
# False (0)
# True  (1)

# a = int(input())
# print(a > 0)
# print(a >= 10 and a < 100)

# x1, x2, x3 = False, True, False
# print(not x1 or x2 and x3)
# x = 52
# y = 10
# print(y > x * x or y >= 2 * x and x < y)
# y > x * x or y >= 2 * x and x < y
# 10 > 25 or 10 >= 10 and 5 < 10

# a = True
# b = False
# print(a and b or not a and not b)
# x = int(input())
# if (x == 0):
#     print("zero")
# elif (x % 2 == 0):
#     print("even")
# else:
#     print("not even")

# a = int(input())
# b = int(input())
# if b != 0:
#     print(a / b)
# else:
#     print("division is not possible")

# a = int(input("enter the number "))
# while(1):
#     b = int(input("enter the number, not zero "))
#     if b != 0:
#         break
# print(a / b)

# min_hour = int(input())
# max_hour = int(input())
# anna_hour = int(input())
# if min_hour <= anna_hour <= max_hour:
#     print("Это нормально")
# elif anna_hour < min_hour:
#     print("Недосып")
# elif anna_hour > max_hour:
#     print("Пересып")

# year = int(input())
# if (1900 <= year <= 3000):
#     if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#         print("Високосный")
#     else:
#         print("Обычный")

# str = """super
# string"""
# str2 = '''new super
# string'''
# print(str, '\n', str2)
# print("239" > "30" and 239 > 30)

# a = 'string'
# b = "anothor string"
# print(a, b)
# print(a + b)
# print(a + '\n' + b)

# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(square)

# a = int(input())
# if (-15 < a <= 12 or 14 < a < 17 or a >= 19):
#     print("True")
# else:
#     print("False")

# a = float(input())
# b = float(input())
# operation = input()
# if (operation == "+"):
#     print(a + b)
# elif (operation == "-"):
#     print(a - b)
# elif (operation == "/"):
#     if b == 0 or b == 0.0:
#         print("Деление на 0!")
#     else:
#         print(a / b)
# elif (operation == "*"):
#     print(a * b)
# elif (operation == "mod"):
#     if b == 0 or b == 0.0:
#         print("Деление на 0!")
#     else:
#         print(a % b)
# elif (operation == "pow"):
#     print(a ** b)
# elif (operation == "div"):
#     if b == 0 or b == 0.0:
#         print("Деление на 0!")
#     else:
#         print(a // b)
# form = input()
# a = float(input())
# if form == "круг":
#     print(3.14 * a * a)
# elif form == "прямоугольник":
#     b = float(input())
#     print(a * b)
# elif form == "треугольник":
#     b = float(input())
#     c = float(input())
#     p = (a + b + c) / 2
#     square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print(square)

# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c and c <= b <= a and c <= a and c < b:
#     max = a
#     med = b
#     min = c
# elif b >= a and b >= c and c <= a <= b  and c <= a and c < b:
#     max = b
#     med = a
#     min = c
# elif c >= a and c >= b and a <= b <= c  and a <= c and a < b:
#     max = c
#     med = a
#     min = c
# print(max, '\n', min, "\n", med)

# a = int(input())
# b = int(input())
# c = int(input())
# if c <= b <= a:
#     max = a
#     med = b
#     min = c
# elif b <= c <= a:
#     max = a
#     med = c
#     min = b
# elif c <= a <= b:
#     max = b
#     med = a
#     min = c
# elif a <= c <= b:
#     max = b
#     med = c
#     min = a
# elif a <= b <= c:
#     max = c
#     med = b
#     min = a
# elif b <= a <= c:
#     max = c
#     med = a
#     min = b
# print(max, '\n', min, "\n", med)

# x=sorted([int(input()),int(input()),int(input())])
# print (x[2], x[0], x[1], sep="\n")

# a = int(input())
# b = int(input())
# c = int(input())
# list = []
# list.append(a)
# list.append(b)
# list.append(c)
# new_list = sorted(list)
# print(new_list[2], "\n", new_list[0], "\n", new_list[1])

# num = int(input())
# str1, str2 = 'программист', ''
# remainder1 = num % 10
# remainder2 = num % 100
# if (0 <= num <= 1000):
#     if 11 <= remainder2 <= 19 or 5 <= remainder1 <= 10 or remainder1 == 0:
#         str2 = 'ов'
#     elif remainder1 == 1:
#         str2 = ''
#     else:
#         str2 = 'а'
# print(num, str1 + str2)

# num = int(input())
# f = num % 10
# num = num // 10
# e = num % 10
# num = num // 10
# d = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# b = num % 10
# a = num // 10
# if a + b + c == d + e + f:
#     print('Счастливый')
# else:
#     print('Обычный')

# a, b, c, d, e, f = input()
# n= int(a)+int (b)+int(c)
# m= int(d)+int (e)+int(f)
# if n==m:
#     print ('Счастливый')
# else:
#     print ('Обычный')


# 2) Циклы. Строки. Списки
# a = 5
# while a > 0:
#     print(a, end=' ')
#     a -= 1

# a = 5
# while a <= 55:
#     print(a, end=' ')
#     a += 2

# i = 0
# k = 0
# while i <= 10:
#     k += 1
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i, k)


# i = 1
# while i <= 6:
#     print("*" * i)
#     i += 1

# stars = '*'
# while len(stars) <= 6:
#     print(stars)
#     stars += '*'

# i = 0
# k = 0
# while i < 5:
#     print('*')
#     k += 1
#     if i % 2 == 0:
#         print('**')
#         k += 2
#     if i > 2:
#         print('***')
#         k += 3
#     i = i + 1
# print(k)

# a = int(input())
# b = int(input())
# sum = 0
# while a <= b:
#     sum += a
#     a += 1
# print(sum)

# sum = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     sum += a
# print(sum)

# a = int(input())
# sum = 0
# while a != 0:
#     sum += a
#     a = int(input())
# print(sum)

# a = int(input())
# b = int(input())
# i = 1
# while True:
#     if i % a == 0 and i % b == 0:
#         break
#     i += 1
# print(i)

# a = int(input())
# b = int(input())
# i = 1
# while not (i % a == 0 and i % b == 0):
#     i += 1
# print(i)

# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if a == 0 and b == 0:
#         break
#     if a == 0 or b == 0:
#         continue
#     print(a * b)
#     i += 1

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)

# while True:
#     a = int(input())
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     print(a)

# for i in 2, 3, 5:
#     print(i * i)

# for i in range(10):
#     print(i * i)
#
# a = 'super string'
# for i in a:
#     print(i)
#
# for i in range(2, 15, 4):
#     print(i, i * i)

# a = '******'
# for i in range(6):
#     print(a)

# a = 6
# for i in range(a):
#     print('*' * a)

# n = 10
# for i in range(n):
#     for j in range(n):
#         print('*', end='')
#     print()

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if 1 <= a <= 10 and 1 <= b <= 10 and 1 <= c <= 10 and 1 <= d <= 10 and a <= b and c <= d:
#     for k in range(c, d + 1):
#         print("\t", k, end="\t")
#     print()
#     for i in range(a, b + 1):
#         print(i, end= "")
#         for j in range(c, d + 1):
#             print("\t", i * j, end='\t')
#         print()

# a = 3
# b = 7
# sum = 0
# for i in range(a, b + 1, 2):
#     sum += i
# print(sum)

# a, b = input().split()
# a = int(a)
# b = int(b)
# sum = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     sum += i
# print(sum)

# a, b = (int(i) for i in input().split())
# sum = 0
# if a % 2 == 0:
#     a += 1
# for i in range(a, b + 1, 2):
#     sum += i
# print(sum)

# a, b = int(input()), int(input())
# sum = 0
# k = 0
# for i in range(a, b + 1):
#     if i % 3 == 0:
#         sum += i
#         k += 1
# print(sum / k)

# genome = 'ATGG'
# for i in range(4):
#     print(genome[i])
# for c in genome:
#     print(c)

# genome = 'CACCTGGAC'
# count = 0
# for i in genome2:
#     if i == 'C':
#         count += 1
# print(count)

# genome2 ='GATTACA'
# print((genome.count('C')))

# s = 'aTGcc'
# p = 'CC'
# s.upper()
# s.lower()
# s.count(p)
# s.find(p)
# s.replace('c', 'C')

# s = 'dfvsDFvsf'
# s.upper()
# print(s) # выведет dfvsDFvsf
# s = s.upper()
# print(s) #  выведет DFVSDFVSF

# s = 'agTtcAGtc'
# print(s.upper().count('gt'.upper()))

# genome = input()
# count = 0
# genome = genome.upper()
# for i in genome:
#     if i == 'C' or i == 'G':
#         count += 1
# print(count / len(genome) * 100)

# genome = input().upper()
# count = genome.count('C') + genome.count('G')
# print(count / len(genome) * 100)

# dna = 'ATTCGGCGCT'
# print(dna[1])
# print(dna[1:4])
# print(dna[:4])
# print(dna[4:])
# print(dna[-4:])
# print(dna[1:-1])
# print(dna[1:-1:2])
# print(dna[::-1]) - # выводим в обратном порядке

# genome = 'CAGGTGGAC'
# genome2 = 'GATTACA'
# if genome == genome[::-1]:
#     print('YES')
# else:
#     print('NO')

# s = input()
# i = 0
# j = len(s) -1
# is_palindrom = True
# while i < j:
#     if s[i] != s[j]:
#         is_palindrom = False
#     i += 1
#     j -= 1
# if is_palindrom:
#     print('YES')
# else:
#     print('NO')

# s = 'abcdefghijk'
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])

# genome = input()
# genome = genome + ' '
# shifr = ''
# count = 1
# for i in range(0, len(genome) - 1):
#     if genome[i] == genome[i + 1]:
#         count += 1
#     if genome[i] != genome[i + 1]:
#         shifr = shifr + genome[i] + str(count)
#         count = 1
# print(shifr)

# students = ['ivasha', 'ne ivasha', 'super']
# for i in students:
#     print('Hello', i)

# students = ['ivasha', 'ne ivasha', 'super']
# students.append('olga')
# print(students)
# students += ['olga']
# print(students)
# students.insert(1, 'ne olga')
# print(students)
#
# c = [1, 2, 3]
# f = c
# f += ['a']
# print(c)

# students = ['ivan', 'masha', 'sasha']
# print(students)
# students.remove('sasha')
# print(students)
# del students[0]
# print(students)

# students = ['ivan', 'masha', 'sasha']
# if 'ivan' in students:
#     print('yes')
# if 'ann' not in students:
#     print('no')
# ind = students.index('sasha')
# print(ind)
# ind = students.index('ann')
# print(ind)

# students = ['sasha', 'ivan', 'masha']
# print(students)
# ordered_students = sorted(students)
# print(ordered_students)
# students.sort()
# print(students)
#
# print(dir(max))
# print(max(students))
# print(min(students))

# a = [1, 'A', 2]
# b = a
# a[0] = 42
# print(a)
# print(b)
# b[2] = 30
# print(a)
# print(b)

# a = [1, 2, 3]
# b = a
# print(b)
# a[1] = 10
# print(b)
# b[0] = 20
# print(a)
# a = [5, 6]
# print(b)

# a = [0] * 5
# print(a)
# a = [0 for i in range(5)]
# print(a)
# a = [i * i for i in range(5)]
# print(a)
# a = [int(i) for i in input().split()]
# print(a)

# a = [int(i) for i in input().split()]
# print(sum(a))
# a = map(int, input().split())
# print(sum(a))

# a = [int(i) for i in input().split()]
# a.insert(0, a[len(a) - 1])
# a.append(a[1])
# list1 = []
# if len(a) == 3:
#     print(a[0])
# else:
#     for i in range(1, len(a) - 1):
#         b = a[i - 1] + a[i + 1]
#         list1.append(b)
#     print(list1)

# a = [int(i) for i in input().split()]
# a.insert(0, a[len(a) - 1])
# a.append(a[1])
# if len(a) == 3:
#     print(a[0])
# else:
#     for i in range(1, len(a) - 1):
#         print(a[i - 1] + a[i + 1], end=' ')

# a = [int(i) for i in input().split()]
# a.sort()
# print(a)
# flag = 0
# for i in range(len(a) - 1):
#     if a[i] == a[i + 1]:
#         flag = 1
#     else:
#         flag = 0
#     if flag == 1:
#         print(a[i], end=' ')

# a = [int(i) for i in input().split()]
# a.sort()
# a.append(0)
# count = 0
# for i in range(len(a) - 1):
#     if count == 1:
#         print(a[i], end=' ')
#     if a[i] == a[i + 1]:
#         count += 1
#     else:
#         count = 0

# a, c = [str(i) for i in input().split()], []
# for i in a:
#     if i not in c and a.count(i) > 1:
#         c.append(i)
#         print(i, end=' ')

# a =[[1, 2, 3], [4, 5, 6],[7, 8, 9]]
# print(a[1])
# print(a[1][1])
# n = 3
# a = [[0] * n] * n
# print(a)
# a[0][0] = 5
# print(a)
# a = [[0] * n for i in range(n)]
# print(a)
# a = [[0 for j in range(n)] for i in range(n)]
# print(a)

# a = [5, 8, 4, 3, 5, 7]
# min_a = a[0]
# for i in a:
#     if min_a > i:
#         min_a = i
# print(min_a)

# Сапер
# n, m, k = (int(i) for i in input().split())    # строки, столбцы, кол-во мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):                             # перебираем кол-во мин
#     row, col = (int(i) - 1 for i in input().split()) # записываем строку и столбец одной мины при каждом проходе
#     a[row][col] = -1  # записываем мину по координатам столбца и строки
# # нам нужно заглянуть в каждую пустую ячейку, и находясь в ячейке пробежаться еще вокруг и поискать мины
# for i in range(n):                             # перебираем строки
#     for j in range(m):                         # перебираем столбцы
#         if a[i][j] == 0:                       # ячейка без мины
#             for di in range(-1, 2):            # перебираем соседние строки (просто цифры -1 0 1)
#                 for dj in range(-1, 2):        # перебираем соседние столбцы (просто цифры -1 0 1)
#                     ai = i + di                # координата по строке
#                     aj = j + dj                 # координата по столбцу
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: # проверка вхождения в диапазон и мины по соседству
#                         a[i][j] += 1
# # вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end='')
#         elif a[i][j] == 0:
#             print('.', end='')
#         else:
#             print(a[i][j], end='')
#     print()

# lst = []
# summa = 0
# while True:
#     num = int(input())
#     summa += num
#     lst.append(num * num)
#     if summa == 0:
#         break
# print(sum(lst))

# num = int(input())
# lst = []
# for i in range(1, num + 1):
#     dig = i
#     for j in range(1, i + 1):
#         lst.append(dig)
#         if len(lst) == num:
#             break
#     if len(lst) == num:
#         break
# print(*lst)

# num = int(input())
# lst = []
# for i in range(1, num + 1):
#     dig = i
#     for j in range(1, i + 1):
#         lst.append(dig)
# print(*lst[:num])

# matrix = [int(i) for i in input().split()]
# num = int(input())
# lst = []
# for i in range(len(matrix)):
#     if matrix[i] == num:
#         lst.append(i)
# if len(lst) == 0:
#     print('Отсутствует')
# else:
#     print(*lst)

# matrix, num  = [int(i) for i in input().split()], int(input())
# if matrix.count(num) == 0:
#     print('Отсутствует')
# else:
#     for i in range(len(matrix)):
#         if matrix[i] == num:
#             print(i, end=' ')

# a = [[1,2,3,4,5,6,7,8,9,10],
#      [11,12,13,14,15,16,17,18,19,20],
#      [21,22,23,24,25,26,27,28,29,30],
#      [31,32,33,34,35,36,37,38,39,40],
#      [41,42,43,44,45,46,47,48,49,50],
#      [51,52,53,54,55,56,57,58,59,60],
#      [61,62,63,64,65,66,67,68,69,70]]
# print(a[0][0], ' ', a[-7][-10], '---', a[0][9], a[-7][-1])
# print('|\t\t\t|')
# print('|\t\t\t|')
# print(a[6][0], a[-1][-10], '---', a[6][9], a[-1][-1])
# m = 10
# n = 7
# b = []
# print(a[-1][0],a[-6][0],a[0][-1],a[0][-9])
# print(a[5][9],a[0][9],a[6][8],a[6][0])
# for i in range(n):
#     for j in range(m):
#         x_sum = a[i - 1][j] + a[i - n + 1][j] + \
#                 a[i][j - 1] + a[i][j - m + 1]
#         b.append(x_sum)
# print(b)
# for i in range(n):
#     print(*b[:10])
#     b = b[10:]

# # Считываем матрицу, ее длину и ширину
# b = []
# a = []
# width = 0
# while True:
#     arg = input().split()
#     if arg[0] == 'end':
#         break
#     for i in arg:
#         b.append(int(i))
#     a.append(b)
#     length = len(b)
#     b = []
#     width += 1
# # Заполняем матрицу суммой соседних элементов
# for i in range(width):
#     for j in range(length):
#         x_sum = a[i - 1][j] + a[i - width + 1][j] + \
#                 a[i][j - 1] + a[i][j - length + 1]
#         b.append(x_sum)
# # Распечатываем матрицу (без скобок)
# for i in range(width):
#     print(*b[:length])
#     b = b[length:]

# # Считываем матрицу
# b = []
# a = []
# while True:
#     arg = input().split()
#     if arg == ['end']:
#         break
#     a.append([int(i) for i in arg])
# length, width = len(a[0]), len(a)
# # Заполняем матрицу суммой соседних элементов
# for i in range(width):
#     for j in range(length):
#         x_sum = a[i - 1][j] + a[i - width + 1][j] + \
#                 a[i][j - 1] + a[i][j - length + 1]
#         b.append(x_sum)
# # Распечатываем матрицу (без скобок [])
# for i in range(width):
#     print(*b[:length])
#     b = b[length:]
# ---------------------------------------------------------------------------------------------------
# arg = int(input())
# a = [[0 for i in range(arg)] for j in range(arg)]
# num = [i + 1 for i in range(arg*arg)]
#
# for i in range(arg):
#     a[0][i] = i + 1

# for i in range(arg - 1):
#     for j in range(arg - 1):

# for i in a:
#     print(*i)
# print(num)
# ---------------------------------------------------------------------------------------------------
# arg = int(input())
# a = [[0 for i in range(arg)] for j in range(arg)]
# num = [i + 1 for i in range(arg*arg)]
# b = [0 for i in range(arg * arg)]
# print(b)
#
# n = arg -1
# for i in range(n):
#     a[0][i] = i + 1
# # for i in range(n):
#     a[i][arg - 1] = i + 1 + n
# # for i in range(n):
#     a[arg - 1][- i - 1] = i + 1 + n * 2
# # for i in range(n):
#     a[-i -1][0] = i + 1 + n * 3
#
#
# for i in a:
#     print(*i)
# print(num)
# for i in range(arg):
#     print(*b[:arg])
#     b = b[arg:]
# ---------------------------------------------------------------------------------------------------

# str = 'a3b4c2e10b1'
# str = str + ' '
# numbers = '0123456789'
# str_num = ''
# a = ''
# for i in range(len(str)):
#     if str[i] not in numbers:
#         a = str[i]
#         # print(a)
#     else:
#         str_num += str[i]
#         if str_num != '' and str[i + 1] not in numbers:
#             num = int(str_num)
#             # print(num)
#             str_num = ''
#             print(a * num, end='')

# ------------------------------------------------------------------
# первый способ
arg = int(input())
b = [[0 for i in range(arg)] for j in range(arg)]
n, lens, st = 0, arg, -1
while n < arg*arg-1:
    st += 1
    lens -= 1
    for i in range(st, lens):  # to ->
        n += 1
        b[st][i] = n
    for j in range(st, lens):  # to down \|
        n += 1
        b[j][lens] = n
    for i in range(st, lens):  # to <-
        n += 1
        b[lens][lens - i + st] = n
    for j in range(st, lens):  # to up ^
        n += 1
        b[lens-j + st][st] = n
if arg%2:
    b[arg//2][arg//2] = arg*arg
for i in b:
        print(*i)
# второй способ
arg = int(input())
b = [[0 for i in range(arg)] for j in range(arg)]
lens = arg
st = -1
n = -(lens - st) * 3
while n < arg * arg - 1:
    n += (lens - st) * 3
    lens -= 1
    st += 1
    for i in range(st, lens):  # to ->
        n += 1
        b[st][i] = n
        b[i][lens] = n + (lens - st)
        b[lens][lens - i + st] = n + (lens - st) * 2
        b[lens - i + st][st] = n + (lens - st) * 3
if arg % 2:
    b[arg // 2][arg // 2] = arg * arg
for i in b:
    print(*i)
# ------------------------------------------------------------------