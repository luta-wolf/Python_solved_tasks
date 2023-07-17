def drawBox():
	print("**********")
	print("*        *")
	print("*        *")
	print("**********")

print(drawBox())

# def drawBox2(c):
# 	c = str(c)
# 	print(c*10)
# 	print(c, '      ', c )
# 	print(c, '      ', c )
# 	print(c*10)

# drawBox2(101)

# def drawBox2(c):
# 	c = str(c)
# 	prob = ' ' * len(c)
# 	print(c*10)
# 	print(c, prob * 7, c )
# 	print(c, prob * 7, c )
# 	print(c*10)

# drawBox2('**')

## Рисуем прямоугольник из звездочек, заполненный пробелами
# @param width – ширина прямоугольника
# @param height – высота прямоугольника
# @param outline – символ для рисования сторон прямоугольника
# # @param fill – символ для заливки прямоугольника
# default value - при объявлении
def drawBox(width, height, outline = '*', fill = ' '):
# Слишком маленькие прямоугольники не могут быть нарисованы при помощи этой функции
	if width < 2 or height < 2:
		print("Ошибка: ширина или высота прямоугольника слишком малы.")
		quit()
# Рисуем верхнюю линию прямоугольника
	print(outline * width)
# Рисуем стороны прямоугольника
	for i in range(height - 2):
		print(outline + fill * (width - 2) + outline)
# Рисуем нижнюю линию прямоугольника
	print(outline * width)


drawBox(20, 10, ':', ':')

# def inc():
# 	global x
# 	x += 1
# 	print(f"Количество вызовов функции равно {x}.")


# x = 0
# inc()
# inc()
# inc()

# def print_hello(name):
# 	print(f'Hello, {name}!')

# name = "world"
# print_hello(name)

# def gcd(num_1, num_2):
# 	lst_1 = []
# 	lst_2 = []
# 	lst_3 = []
# 	for i in range(1, num_1 + 1):
# 		if num_1 % i == 0:
# 			lst_1.append(i)
# 	for i in range(1, num_1 + 1):
# 		if num_2 % i == 0:
# 			lst_2.append(i)
# 	for i in lst_1:
# 		if i in lst_2:
# 			lst_3.append(i)
# 	print('result =', max(lst_3))

# result = gcd(12, 45)
# result = gcd(144, 96)

# def gcd2(num_1, num_2):
# 	if num_1 > num_2:
# 		temp = num_1
# 	else:
# 		temp = num_2
# 	for i in range(1, temp + 1):
# 		if num_1 % i == 0 and num_1 % i == 0:
# 			gcd = i
# 	print('result =', gcd)

# result = gcd(12, 45)
# result = gcd(144, 96)


# def number_length(num):
# 	if num < 0:
# 		num = num * -1
# 	length = str(num)
# 	count = 0
# 	for i in length:
# 		count += 1
# 	print('result =', count)


# result = number_length(12345)
# result = number_length(-100500)

# def month(num, shift):
# 	lst_ru = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# 	lst_en = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# 	if shift == 'ru':
# 		return lst_ru[num - 1]
# 	else:
# 		return lst_en[num - 1]

# result = print(month(12, "ru"))


# width – ширина прямоугольника
# height – высота прямоугольника
# outline – символ для рисования сторон прямоугольника
# fill – символ для заливки прямоугольника

