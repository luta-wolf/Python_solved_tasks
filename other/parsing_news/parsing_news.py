import requests
import json

headers = {
	'content-type': 'application/json',
	'x-access-token': '1920e49f7904b7153214097f6791fbf3a036ded7'
}
params = {
	'offset': 4,
	'bound_limit': 12,
	'limit': 12,
	'full': 'true'
}

url = 'https://api.vedomosti.ru/v2/lists/ecology-releases-top'

resp = requests.get(url, params=params, headers=headers)

news = []
# print(resp.json())

data = resp.json()['list']['documents']
i = 0
for dat in data:
	aa = dat['bound_documents']
	header = 1
	href = 1
	text = 1
	date = 1
	news.append(aa)
	# news.append({'title': header, 'url': href,
	# 			'description': text, 'date': date})

a = 'subtitle'
print(len(news))





# print(data)
print(len(data))

h = open('json3.txt', 'w')
h.write(str(data))
h.close()
