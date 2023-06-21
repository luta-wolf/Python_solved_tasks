# Экзамен

# task 1 Звездный треугольник 🌶️

# объявление функции
def draw_triangle():
	for i in range(1, 9):
		print(' ' * (8 - i) + '*' * ((i * 2 ) -1))

# основная программа
draw_triangle()  # вызов функции

# task 2 Калькулятор доставки
# объявление функции
def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))

# task 3 Биномиальный коэффициент 🌶️
from math import factorial
# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# считываем данные
n = 1
k = 1

# вызываем функцию
print(compute_binom(n, k))

# task 4 Число словами 🌶️
# объявление функции
def number_to_words(num):
    lst_1 = ['','один','два','три','четыре','пять','шесть','семь','восемь','девять']
    lst_11 = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    lst_10 = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if n < 10:
        return lst_1[num]
    if 11 <= num <= 19:
        return lst_11[num - 10]
    else:
        d1 = num // 10
        d2 = num % 10
        return lst_10[d1] + ' ' + lst_1[d2]

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))

# task 5 Искомый месяц
# объявление функции
def get_month(language, number):
    lst_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lst_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return lst_ru[number -1]
    else:
        return lst_en[number -1]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))

# task 6 Магические даты
# объявление функции
def is_magic(date):
    lst = date.split('.')
    return int(lst[0]) * int(lst[1]) == int(lst[2]) % 100

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))

# task 7 Панграммы
# 1
def is_pangram(text):
	text = text.upper().replace(' ', '')
	lst = [0 for _ in range(91)]
	for i in text:
		lst[ord(i)] = 1
	if sum(lst) == 26:
		return True
	else:
		return False

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))

# 2
def is_pangram(text):
    text = text.lower()
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in text:
            return False

    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
