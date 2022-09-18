# def min2(a, b):
#     if a <= b:
#         return a
#     else:
#         return b
#
#
# print(min2(55, -55))


# def f(n):
#     return n * 10 + 5
#
#
# print(f(f(f(10))))
#
#
# # Функция принимает произвольное число агруметнов
# def mymin(*a):
#     m = a[0]
#     for x in a:
#         if m > x:
#             m = x
#     return m
#
#
# print(mymin(55, 13, 25, 101))
# print(mymin([55, 130, 25, 101]))


# # значения параметров по умолчанию
# def my_range(start, stop, step=1):
#     res = []
#     if step > 0:
#         x = start
#         while x < stop:
#             res += [x]
#             x += step
#     elif step < 0:
#         x = start
#         while x > stop:
#             res += [x]
#             x += step
#     return res
#
#
# print(my_range(2, 5))
# print(my_range(2, 15, 3))
# print(my_range(15, 2, -3))
#
# print(divmod(100, 3))

# def append_zero(xs):
#     xs.append(0)
#
# a = []
# append_zero(a)
# print(a)

# def print_value():
#     print(a)
#     b = 10
#     print(b)
#
# a = 5
# print_value()
#
# def f(x):
#     if x <= -2:
#         m = 1 - (x + 2)**2
#     elif -2 < x <= 2:
#         m = -x / 2
#     elif 2 < x:
#         m = (x - 2)**2 + 1
#     return m
#
# print(f(4.5))
# print(f(-4.5))
# print(f(1))


# def modify_list(l):
#     a = []
#     for i in l[:]:
#         if i % 2 == 0:
#             a.append(i // 2)
#     l.clear()
#     l.extend(a)
#
# def modify_list(l):
#     l[:] = [i // 2 for i in l if i % 2 == 0]


# def modify_list(l):
#     a = []
#     for i in l:
#         if i % 2 == 0:
#             a.append(i)
#     l.clear()
#     l.extend(a)
#     for i in range(len(l)):
#         l[i] = l[i]//2


# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)  # [1, 2, 3]
# modify_list(lst)
# print(lst)  # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)
# lst = [0, 0, 0, 0]
# modify_list(lst)
# print(lst)
# lst = [0, 5, 0, 98]
# modify_list(lst)
# print(lst)
# lst = [0, 7, 112, 0, 5, 0, 98, 0]
# modify_list(lst)
# print(lst)
# lst = [1, 1, 2, 24, 3, 1, 122]
# modify_list(lst)
# print(lst)

# a = set() # создание пустого множества
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
# print('orange' in basket)
# print('python' in basket)

# Словарь (dictionaty), Отображение (map), ассоциативный
# Позволяет хранить пары <ключ, значение>
# ключи не изменяемы
# dict, {}
# d = {'a': 239, 10: 100}
# print(d['a'])
# print(d[10])
# print(d.get(10), d.get(9))
# # Перебор элеметов словаря
#
# d = {'C': 14, 'A': 12, 'T': 9, 'G': 18}
# for key in d:
#     print(key, end=' ')
# print()
# for key in d.keys():
#     print(key, end=' ')
# print()
# for key in d.values():
#     print(key, end=' ')
# print()
# for key, value in d.items():
#     print(key, value,  end='; ')
# ---------------------------------------------------------
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif not key in d:
#         if not d:
#             d[key * 2] = [value]
#         else:
#             if key * 2 in d:
#                 d[key * 2] += [value]
#             else:
#                 d[key * 2] = [value]
#
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}
# ---------------------------------------------------------

# str = input().lower().split()
# str.sort()
# str.append(0)
# for i in range(len(str) - 1):
#     if str[i] != str[i + 1]:
#         print(str[i], str.count(str[i]))
#
# str = input().lower().split()
# for i in set(str):
#     print(i, str.count(i))

# ---------------------------------------------------------
# n = int(input())
# dict = {}
# for i in range(n):
#     num = int(input())
#     if num not in dict:
#         dict[num] = f(num)
#     print(dict[num])
# ---------------------------------------------------------
# a = [int(i) for i in input().split()]
# sum_a = 0
# for i in a:
#     sum_a += i
# print(sum_a)
# ---------------------------------------------------------
# Чтение из файла
import os.path

# inf = open('file.txt', 'r') # open('file.txt')
# s1 = inf.readline()
# s2 = inf.readline()
# inf.close()
#
# или
# with open('file.txt') as inf:
#     s1 = inf.readline()
#     s2 = inf.readline()
#
# s = inf.readline().strip()
# '\t abc \n'.strip() -> 'abc'
# import  os
# os.path.join('.', 'dirname', 'filename.txt') # для отбражения корректного пути к файлу
# './dirname/filename.txt'

# как прочесть все сроки из файла
# with open('main.py') as inf:
#     for line in inf:
#         # line = line.strip()
#         print(line)
# # Запись в файл
# ouf = open('file.txt', 'w')
# ouf.write('some text\n')
# ouf.write(str(25))
# ouf.close()
#
# или
#
# with open('text.txt', 'w') as ouf:
#     ouf.write('some text\n')
#     ouf.write(str(25))
# ---------------------------------------------------------
# inf = open('dataset_3363_2.txt', 'r')
# str = inf.readline().strip()
# inf.close()
#
# str = 'a3b4c2e10b1'
# str = str + ' '
# numbers = '0123456789'
# str_num = ''
# a = ''
# out_str = ''
# for i in range(len(str)):
#     if str[i] not in numbers:
#         a = str[i]
#     else:
#         str_num += str[i]
#         if str_num != '' and str[i + 1] not in numbers:
#             num = int(str_num)
#             str_num = ''
#             out_str += a * num
#             print(a * num, end='')
# print()
# print(out_str)
# ouf = open('file.txt', 'w')
# ouf.write(out_str)
# ouf.close()
# ---------------------------------------------------------
#  №1
# file = open('dataset_3363_3.txt')
# line = file.read().strip().lower().split()
# file.close()
# line.sort()
# d = {}
# maxx = 0
# for i in range(len(line)):
#     d[line[i]] = line.count(line[i])
#     if d[line[i]] > maxx:
#         maxx = d[line[i]]
# ouf = open('file.txt', 'w')
# for key, value in d.items():
#     if value == maxx:
#         ouf.write(key + ' ' + str(value))
#         print(key, value)

#  №2
# all = open('dataset.txt', 'r')
# s = all.read().lower().strip().split()
# y = 0
# m =''
# for i in s:
#     z = s.count(i)
#     if z >= y:
#         y = z
#         m = i
# print(m, y)
# ---------------------------------------------------------
# file = open('dataset_3363_4.txt')
# l, one, two, three, count = [], 0, 0, 0, 0
# for line in file:
#     l.append(line.strip().split(';'))
# ouf = open('file.txt', 'w')
# for i in l:
#     count += 1
#     one += int(i[1])
#     two += int(i[2])
#     three += int(i[3])
#     summ = int(i[1]) + int(i[2]) + int(i[3])
#     print(summ / 3)
#     ouf.write(str(summ / 3) + '\n')
# print(one/count, two/count, three/count)
# ouf.write(str(one/count) + ' ' + str(two/count) + ' ' + str(three/count))
# ---------------------------------------------------------
# Модули
# Запуск внешних процессов модуль subprocess
# запускает программу в соответствии с аргументами(args).
# дожидается выполнения и возвращает код возврата.
# Пример
# import subprocess
# subprocess.call(["python", "-h"])

# import sys
# print(len(sys.argv))
# ---------------------------------------------------------
# import math
# r = float(input())
# l = 2 * math.pi * r
# print(l)
#
# from math import pi
# print(float(input()) * 2 * pi)
# ---------------------------------------------------------
# import sys
# for i in range(1, len(sys.argv)):
#     print(sys.argv[i], end=' ')
# print('\n')

# from sys import argv
#
# print(*argv[1:])
# ---------------------------------------------------------
# n = int(input())
# d, l, victory, draw, defeat = {}, [], 3, 1, 0
# for i in range(n):
#     data = input().split(';')
#     l.append(data)
#     if data[0] not in d:
#         d[data[0]] = [0, 0, 0, 0, 0]
#     if data[2] not in d:
#         d[data[2]] = [0, 0, 0, 0, 0]
#     d[data[0]][0] += 1
#     d[data[2]][0] += 1
#     if int(data[1]) > int(data[3]):
#         d[data[0]][1] += 1
#         d[data[2]][3] += 1
#         d[data[0]][4] += victory
#     elif int(data[1]) < int(data[3]):
#         d[data[0]][3] += 1
#         d[data[2]][1] += 1
#         d[data[2]][4] += victory
#     else:
#         d[data[0]][2] += 1
#         d[data[2]][2] += 1
#         d[data[0]][4] += draw
#         d[data[2]][4] += draw
# for i in d:
#     print(i + ":", d[i][0], d[i][1], d[i][2], d[i][3], d[i][4])
# ---------------------------------------------------------
# a, k, s1, s2 = input(), input(), input(), input()
# d , d1 = {}, {}
# for i in range(len(a)):
#     d[a[i]] = k[i]
#     d1[k[i]] = a[i]
# for c in s1:
#     print(d[c], end='')
# print()
# for c in s2:
#     print(d1[c], end='')
# ---------------------------------------------------------
# n1 = int(input())
# l1 = []
# for i in range(n1):
#     l1.append(input().lower())
# n2 = int(input())
# l2 = []
# for i in range(n2):
#     l = set(input().lower().split())
#     for word in l:
#         if word not in l1:
#             l2.append(word)
# for i in set(l2):
#     print(i)
# ---------------------------------------------------------
# вариант 1
# n = int(input())
# d = {'север': [], 'юг': [], 'восток': [], 'запад': []}
# for i in range(n):
#     a = input().split()
#     if a[0] == 'север':
#         d['север'] += [int(a[1])]
#     if a[0] == 'юг':
#         d['юг'] += [-int(a[1])]
#     if a[0] == 'восток':
#         d['восток'] += [int(a[1])]
#     if a[0] == 'запад':
#         d['запад'] += [-int(a[1])]
# print(sum(d['восток']) + sum(d['запад']), sum(d['север']) + sum(d['юг']))

# вариант 2
# n = int(input())
# d = {'север': [], 'юг': [], 'восток': [], 'запад': []}
# for i in range(n):
#     key, value = input().split()
#     d[key] += [int(value)]
# print(sum(d['восток']) - sum(d['запад']), sum(d['север']) - sum(d['юг']))
# ---------------------------------------------------------
# file = open('dataset_3380_5.txt')
# l= []
# d = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': []}
# for line in file:
#     l.append(line.strip().split())
# for i in l:
#     d[i[0]] += [int(i[2])]
# ouf = open('file.txt', 'w')
# for i in d:
#     print(i, sum(d[i])/len(d[i]))
#     ouf.write(str(i) + ' ' +  str(sum(d[i])/len(d[i])) + '\n')

# file = open('dataset_3380_5.txt')
# d = {i: [] for i in range(1, 12)}
# # print(d1)
# # d = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': []}
# # print(d)
# for line in file:
#     i = line.split()
#     d[int(i[0])] += [int(i[2])]
# ouf = open('file.txt', 'w')
# for i in d:
#     print(i, sum(d[i]) / len(d[i]))
#     ouf.write(str(i) + ' ' + str(sum(d[i]) / len(d[i])) + '\n')
# ---------------------------------------------------------


# import requests
# r = requests.get('http://example.com') # простой GET запрос
# print(r.text)                          # вывод ответа от сервера
#
# url = 'http://example.com'
# par = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(url, params=par)    #  передача параметров в запрос
# print(r.url) # Сформированный url-адрес с учетом параметров GET  запроса
#
# url = 'http://httpbin.org/cookies'
# cookies = {'cookies_are': 'working'}
# r = requests.get(url, cookies=cookies) # отправка сформированных cookies на сервер
# print(r.text)
#
# print(r.cookies['example_cookie_name'])
# ---------------------------------------------------------
# N1
# import  requests
# inf = open('dataset_3378_2.txt')
# url = inf.readline().strip()
# print(url)
# file = requests.get(url).text
# print(file)
# count = 0
# for i in file:
#     if i == '\n':
#         count += 1
# print(count)
# ouf = open('file.txt', 'w')
# ouf.write(str(count))
# N2
# import requests
#
# with open('dataset_3378_2.txt') as inf:
#     r = requests.get(inf.readline().strip())
#     print(len(r.text.splitlines()))
# ---------------------------------------------------------
import  requests
inf = open('dataset_3378_3.txt')
url = inf.readline().strip()
print(url)
file = requests.get(url).text
print(file)
inf = open('https://stepic.org/media/attachments/course67/3.6.3/213837.txt')
url = inf.readline().strip()
print(url)
file = requests.get(url).text
print(file)

