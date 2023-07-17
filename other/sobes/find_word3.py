import re, time, string

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
a = method_string(path, word)
time_1 = time.time() - time_start

time_start = time.time()
b = method_re(path, word)
time_2 = time.time() - time_start

time_start = time.time()
c = method_split(path, word)
time_3 = time.time() - time_start

st = time.time()
with open(path) as f:
	text = f.read()

all_words = re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower()).count(word)
ft = time.time() - st

print(f'Ищем слово ({word}). \n\
	Метод string, слов {a:>5}, время {time_1:.4f} секунд. \n\
	Метод re, слов {b:>9}, время {time_2:.4f} секунд.\n\
	re + count, слов {all_words:>7}, время {ft:.4f} секунд.\n\
	Метод split, слов {c:>6}, время {time_3:.4f} секунд.')

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
