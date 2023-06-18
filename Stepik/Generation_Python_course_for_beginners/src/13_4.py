# Тема урока: функции с возвратом значения

# task 1 Конвертер километров
# объявление функции
def convert_to_miles(km):
    return km * 0.6214

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))

# task 2 Количество дней
# объявление функции
def get_days(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9,11]:
        return 30
    else:
        return 31

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))

# task 3 Делители 1
# объявление функции
def get_factors(num):
    lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            lst.append(i)
    return lst

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))


# task 4 Делители 2
# объявление функции
def number_of_factors(num):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    return cnt

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))


# task 5 Найти всех
# объявление функции
def find_all(target, symbol):
    lst = []
    for i in range(len(target)):
        if target[i] == symbol:
            lst.append(i)
    return lst

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))

# task 6 Merge lists 1
# объявление функции
def merge(list1, list2):
    lst = list1 + list2
    lst.sort()
    return lst

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))

# task 7 Merge lists 2
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]

    return result


lst = [el for el in range(int(input()))]
for i in range(len(lst)):
    lst[i] = [int(el) for el in input().split()]
total = []
for i in range(len(lst)):
    total = quick_merge(total, lst[i])
print(*total)
