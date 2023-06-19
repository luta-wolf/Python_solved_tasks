# Генератор безопасных паролей

import random

def data_entry(digits, lowercase_letters, uppercase_letters, punctuation):
	chars = ''

	print('Введите следующие данные: ')
	amount = int(input('Количество паролей для генерации: '))
	len_pswd = int(input('Длину одного пароля: '))
	let_digit = input('Включать ли цифры 0123456789 ? (y/n) ').strip()
	if let_digit == 'y' or let_digit == 'yes':
		print('Цифры включены.')
		chars += digits
	let_upp = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? (y/n) ').strip()
	if let_upp == 'y' or let_upp == 'yes':
		print('Прописные буквы включены.')
		chars += uppercase_letters
	let_low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? (y/n) ').strip()
	if let_low == 'y' or let_low == 'yes':
		print('Цифры включены.')
		chars += lowercase_letters
	let_punc = input('Включать ли символы !#$%&*+-=?@^_ ? (y/n) ').strip()
	if let_punc == 'y' or let_punc == 'yes':
		print('Цифры включены.')
		chars += punctuation
	let_excp = input('Исключать ли неоднозначные символы il1Lo0O ? (y/n) ').strip()
	if let_excp == 'y' or let_excp == 'yes':
		print('Исключения учтены.\n')
		for i in chars:
			if i in 'il1Lo0O':
				n = chars.index(i)
				chars = chars[:n] + chars[n + 1:]
	return chars, amount, len_pswd

def generate_password(len_pswd, chars):
	return ''.join(random.sample(chars, len_pswd))


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars, amount, len_pswd = (data_entry(digits, lowercase_letters, uppercase_letters, punctuation))
print('Ваши пароли:')
for i in range(amount):
	print(generate_password(len_pswd, chars))
