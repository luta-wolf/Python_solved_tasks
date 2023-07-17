# fname = input('Введите имя файла: ')
# try:
# 	inf = open(fname, 'r')
# except FileNotFoundError:
# 	print(f"Невозможно открыть файл {fname}. Выходим...")
# 	# quit()
# text = inf.read()
# print(text)

# fname = input('Введите имя файла: ')

# file_opened = False
# while file_opened == False:
# 	try:
# 		inf = open(fname, 'r')
# 		file_opened = True
# 	except FileNotFoundError:
# 		print(f'Файл {fname} не найден. Попробуйте еще раз.')
# 		fname = input('Введите имя файла: ')
# text = inf.read()
# print(text)


age: int

while True:
	try:
		age = int(input('Введите свой возраст: '))
		break
	except ValueError:
		print("Ошибка, введена не цифра.\nПопробуй еще")

print('Ваш возраст', age)
