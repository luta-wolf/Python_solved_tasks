# Угадайка чисел

# Version 1

# import random

# # Функция проверки корректности введенных данных
# def is_valid(s):
# 	if s.isdigit() and 1 <= int(s) <= 100:
# 		return True
# 	else:
# 		return False

# # Заголовок программы
# num = random.randrange(1, 101)
# print(num)
# print('Добро пожаловать в числовую угадайку')

# # Основной цикл программы
# while True:
# 	s = input('Введие число: ')
# 	if is_valid(s):
# 		n = int(s)
# # Сравнение введенного числа с загаданным
# 		if n < num:
# 			print('Ваше число меньше загаданного, попробуйте еще разок')
# 		elif n > num:
# 			print('Ваше число больше загаданного, попробуйте еще разок')
# 		else:
# 			print('Вы угадали, поздравляем!')
# 			break
# 	else:
# 		print('А может быть все-таки введем целое число от 1 до 100?')
# print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


# Version 2
import random
# # Заголовок программы
print('Добро пожаловать в числовую угадайку')

# Функция проверки корректности введенных данных
def is_valid(n, max_n):
	return n.isdigit() and 1 <= int(n) <= max_n

# Функция создания числа
def create_number(max_n):
	return random.randrange(1, max_n + 1)

# Основной цикл программы
def input_num(max_n):
	while True:
		s = input('Введите число: ')
		if is_valid(s, max_n):
			return int(s)
		else:
			print(f'А может быть все-таки введем целое число от 1 до {max_n}?')

# Сравнение введенного числа с загаданным
def compare_num():
	max_n = int(input('Введите максимальное число для случайного выбора: '))
	num = create_number(max_n)
	total = 0
	while True:
		n = input_num(max_n)
		if n < num:
			print('Ваше число меньше загаданного, попробуйте еще разок')
			total += 1
		elif n > num:
			print('Ваше число больше загаданного, попробуйте еще разок')
			total += 1
		else:
			print(f'Вы угадали за {total} попыток, поздравляем!')
			break
	print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

compare_num()
