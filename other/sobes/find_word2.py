import re, time
from collections import Counter

word = 'сказал'
path = 'war_and_peace.txt'


st = time.time()
with open(path) as f:
	text = f.read()
all_occurrences = text.count(word)
ft0 = (time.time() - st)


st = time.time()
with open(path) as f:
	text = f.read()
all_words = re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower())
count_words = len(all_words)
purified_count = all_words.count(word)
ft = (time.time() - st)


st = time.time()
with open(path) as f:
	text = f.read()
all_words = re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower())
count_words = len(all_words)
purified_counter = Counter(all_words).get(word)
ft2 = (time.time() - st)

print(f'Всего слов (с предлогами) {count_words}, ищем слово "{word}"\n\
		общих вхождений {all_occurrences}, {"время":>15} {ft0:.3f}  сек\n\
		точных совпадений count {purified_count}, {"время":>7} {ft:.3f}  сек\n\
		точных совпадений Counter {purified_counter}, время {ft2:.3f}  сек')

