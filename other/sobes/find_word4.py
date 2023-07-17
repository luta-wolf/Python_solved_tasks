import re

word = 'князь'
path = 'war_and_peace.txt'

with open(path) as f:
	text = f.read()

all_words = re.split(r'[^A-Za-zА-Яа-я0-9]', text.lower())
count = all_words.count(word)
print(count)
