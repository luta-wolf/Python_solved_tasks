letter_1 = "t"
letter_2 = "w"
print(letter_1 > letter_2)
print(ord("t"), ord("w"))
print(chr(116), chr(119))

m = 12
n = 19
k = 25

# максимальное число
print(max(m, n, k))

line_1 = "m"
line_2 = "n"
line_3 = "k"

# минимальная лексикографически строка
print(min(line_1, line_2, line_3))

# количество цифр в числе 2 в степени 2022
print(len(str(2 ** 2022)))


a = input('Как Вас зовут?\n')
print(f'Здравствуйте, {a}!')
b = input('Как дела?\n')
if b == 'хорошо':
	print('Я за вас рада!')
elif b == 'плохо':
	print('Всё наладится!')


