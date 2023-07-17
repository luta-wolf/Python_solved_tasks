import re, time

word = 'князь'
path = 'war_and_peace.txt'

st = time.time()
with open(path) as f:
	text = f.read()
all_words = re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower())
count = all_words.count(word)
ft = (time.time() - st)
print(f'Count: Слов {count}, Время {ft:.5f}')


st = time.time()
file = open(path, encoding='utf-8')
count = 0
for line in file.readlines():
	words = re.findall(r'[A-Za-zА-Яа-я]+', line.lower())
	for i in words:
		if i == word:
			count += 1
file.close()
ft = (time.time() - st)
print(f'For:   Слов {count}, Время {ft:.5f}')
