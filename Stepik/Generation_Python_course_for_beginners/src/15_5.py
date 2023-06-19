# Шифр Цезаря

en_lower = 'abcdefghijklmnopqrstuvwxyz'
en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

el_low, el_upp, digit = en_lower, en_upper, 26
text = input()
text2 = text.replace(',', '').replace('.', '').replace('"', '').replace('!', '')
lst = [len(el) for el in text2.split()]
cnt = 0
for el in text:
	if el == ' ':
		cnt += 1
	step = lst[cnt]
	if el.isalpha():
		if el.isupper():
			index = el_upp.index(el)
			print(el_upp[(index + step) % digit], end='')
		elif el.islower():
			index = el_low.index(el)
			print(el_low[(index + step) % digit], end='')

	else:
		print(el, end='')
print()
