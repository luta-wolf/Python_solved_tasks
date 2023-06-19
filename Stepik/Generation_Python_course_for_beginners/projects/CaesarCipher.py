# Шифр Цезаря

en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

direction = input('Шифрование - ch или дешифрование - def ? ')
lang = input('Язык алфавита: русский - ru или английский - en ? ')
step = int(input('Введите шаг сдвига (со сдвигом вправо) '))
text = input('Введите текст: ')

def assign_variables(en_lower, en_upper, ru_lower, ru_upper):
	if lang == 'en':
		return en_lower, en_upper, 26
	elif lang == 'ru':
		return ru_lower, ru_upper, 32

el_low, el_upp, digit = assign_variables(en_lower, en_upper, ru_lower, ru_upper)

for el in text:
	if el.isalpha():
		if el.isupper():
			index = el_upp.index(el)
			if direction == 'ch':
				print(el_upp[(index + step) % digit], end='')
			elif direction == 'def':
				print(el_upp[(index - step) % digit], end='')
		elif el.islower():
			index = el_low.index(el)
			if direction == 'ch':
				print(el_low[(index + step) % digit], end='')
			elif  direction == 'def':
				print(el_low[(index - step) % digit], end='')
	else:
		print(el, end='')

print()
