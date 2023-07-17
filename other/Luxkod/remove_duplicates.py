import time
'''
Дано: список dict-объектов вида вида {"key": "value"},
например [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].

Напишите функцию, которая удаляет дубликаты из этого списка. Для примера выше возвращаемое значение может быть
равно [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].

Обязательное условие: функция не должна иметь сложность O(n^2).
'''

# Линейная сложность O(n^2)
def remove_duplicates(list_1):
	new_list = []
	for i  in list_1:
		if i not in new_list:
			new_list.append(i)
	return new_list

# Линейная сложность O(n)
def remove_duplicates2(lst):
	unique_set = set()
	result_lst = []
	for item in lst:
		item_tuple = tuple(item.items())
		if item_tuple not in unique_set:
			unique_set.add(item_tuple)
			result_lst.append(item)
	return result_lst


a = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

t = time.time()
print(remove_duplicates(a))
print(time.time() - t)
t = time.time()
print(remove_duplicates2(a))
print(time.time() - t)
