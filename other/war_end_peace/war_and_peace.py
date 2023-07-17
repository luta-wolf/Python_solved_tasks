from collections import Counter

with open('war_and_peace.txt', 'r') as f:
	text = f.read()

text = text.split()
print(Counter(text).most_common(20))
