import re, time, string
from collections import Counter

def funk_yield(path):
	with open(path) as f:
		one_line = '1'
		while one_line:
			one_line = f.readline()
			yield one_line

def method_split_count(path, word):
	with open(path) as f:
		text = f.read()
	ss = text.lower().split()
	ss = ' '.join(ss).split(',')
	ss = ' '.join(ss).split('"')
	ss = ' '.join(ss).split('?')
	ss = ' '.join(ss).split('.')
	ss = ' '.join(ss).split(')')
	ss = ' '.join(ss).split('(')
	ss = ' '.join(ss).split(':')
	ss = ' '.join(ss).split(';')
	ss = ' '.join(ss).split()
	return ss.count(word)

def method_string_count(path, word):
	with open(path) as f:
		text = f.read()
	ss = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
	return ss.count(word)

def method_re_count(path, word):
	with open(path) as f:
		text = f.read()
	# return Counter(re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower())).get(word)
	print(len(re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower())))
	return re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower()).count(word)


def method_gen(path, word):
	count = 0
	for line in funk_yield(path):
		ss = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
		count += count_of_word(ss, word)
	return count

def method_gen2(path, word):
	count = 0
	for line in funk_yield(path):
		line = line.lower()
		ss = re.findall(r'[A-Za-zА-Яа-я]+', line)
		count += count_of_word(ss, word)
	return count

def method_gen3(path, word):
	count = 0
	for line in funk_yield(path):
		ss = line.lower().split()
		ss = ' '.join(ss).split(',')
		ss = ' '.join(ss).split('"')
		ss = ' '.join(ss).split('?')
		ss = ' '.join(ss).split('.')
		ss = ' '.join(ss).split(')')
		ss = ' '.join(ss).split('(')
		ss = ' '.join(ss).split(':')
		ss = ' '.join(ss).split(';')
		ss = ' '.join(ss).split()
		count += count_of_word(ss, word)
	return count

def method_string(path, word):
	file = open(path, encoding='utf-8')
	count = 0
	for line in file.readlines():
		ss = line.lower().translate(str.maketrans('', '', string.punctuation)).split()
		count += count_of_word(ss, word)
	file.close()
	return count

def method_re(path, word):
	file = open(path, encoding='utf-8')
	count = 0
	for line in file.readlines():
		line = line.lower()
		ss = re.findall(r'[A-Za-zА-Яа-я]+', line)
		count += count_of_word(ss, word)
	file.close()
	return count

def method_split(path, word):
	file = open(path, encoding='utf-8')
	count = 0
	# new_list = []
	for line in file.readlines():
		ss = line.lower().split()
		ss = ' '.join(ss).split(',')
		ss = ' '.join(ss).split('"')
		ss = ' '.join(ss).split('?')
		ss = ' '.join(ss).split('.')
		ss = ' '.join(ss).split(')')
		ss = ' '.join(ss).split('(')
		ss = ' '.join(ss).split(':')
		ss = ' '.join(ss).split(';')
		ss = ' '.join(ss).split()
		count += count_of_word(ss, word)
		# new_list.extend(ss)
	# count = Counter(new_list).get(word)
	file.close()
	return count

def count_of_word(words, value):
	count = 0
	for word in words:
		if word == value:
			count += 1
	return count

# Здесь записываем искомое слово и путь к файлу
word = 'сказал'
path = 'war_and_peace.txt'

time_start = time.time()
a = method_string(path, word.lower())
time_1 = time.time() - time_start

time_start = time.time()
b = method_re(path, word.lower())
time_2 = time.time() - time_start

time_start = time.time()
c = method_split(path, word.lower())
time_3 = time.time() - time_start

time_start = time.time()
d = method_gen(path, word.lower())
time_4 = time.time() - time_start

time_start = time.time()
e = method_gen2(path, word.lower())
time_5 = time.time() - time_start

time_start = time.time()
f = method_gen3(path, word.lower())
time_6 = time.time() - time_start

time_start = time.time()
g = method_re_count(path, word.lower())
time_g = time.time() - time_start

time_start = time.time()
g2 = method_split_count(path, word.lower())
time_g2 = time.time() - time_start

time_start = time.time()
g3 = method_string_count(path, word.lower())
time_g3 = time.time() - time_start

print(f'Ищем слово - \'{word}\'. \n\
	Метод string, {"слов":>12} {a}, время {time_1:.4f} секунд. \n\
	Метод string + yield, слов {d:>2}, время {time_4:.4f} секунд. \n\
	Метод string + count, слов {g3:>2}, время {time_g3:.4f} секунд.\n\n\
	Метод re, {"слов":>16} {e}, время {time_5:.4f} секунд.\n\
	Метод re + yield, {"слов":>8} {b}, время {time_2:.4f} секунд.\n\
	Метод re + count, {"слов":>8} {g}, время {time_g:.4f} секунд.\n\n\
	Метод split, {"слов":>13} {c}, время {time_3:.4f} секунд.\n\
	Метод split + yield, {"слов":>5} {f}, время {time_6:.4f} секунд.\n\
	Метод split + count, {"слов":>5} {g2}, время {time_g2:.4f} секунд.')

# seconds = time.time()
# file = open('war_and_peace.txt', encoding='utf-8')
# s = 0
# for line in file.readlines():
	# ss = line.lower().translate(str.maketrans('', '', string.punctuation)).split()

	# line = line.lower()
	# ss = re.findall(r'[A-Za-zА-Яа-я]+', line)

	# ss = line.lower().split()
	# ss = ' '.join(ss).split(',')
	# ss = ' '.join(ss).split('"')
	# ss = ' '.join(ss).split('?')
	# ss = ' '.join(ss).split('.')
	# ss = ' '.join(ss).split(')')
	# ss = ' '.join(ss).split('(')
	# ss = ' '.join(ss).split(':')
	# ss = ' '.join(ss).split(';')
	# ss = ' '.join(ss).split()

	# for k in ss:
	# 	if k == 'князь':
	# 		s += 1

# file.close()
# print(s)
# print(time.time() - seconds)
