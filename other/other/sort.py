import time
# Сортировка пузырьком
lst = [4, 2, 6, 8, 1, 3, 7, 5]
def bable_sort(lst):
	for i in range(len(lst) - 1):
		for j in range(len(lst) - i - 1):
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst [j]
	return lst

a = time.time()
print(bable_sort(lst), time.time() - a)
print('-' * 20)

# Сортировка вставками
def insertion_sort(alist):
	for i in range(1, len(alist)):
		temp = alist[i]
		j = i - 1
		while (j >= 0 and temp < alist[j]):
			alist[j + 1] = alist[j]
			j = j - 1
		alist[j + 1] = temp
	return alist

a = time.time()
print(insertion_sort(lst), time.time() - a)
print('-' * 20)

# Сортировка выбором
def selection_sort(alist):
	for i in range(0, len(alist) - 1):
		smallest = i
		for j in range(i + 1, len(alist)):
			if alist[j] < alist[smallest]:
				smallest = j
		alist[i], alist[smallest] = alist[smallest], alist[i]
	return alist

a = time.time()
print(selection_sort(lst), time.time() - a)
print('-' * 20)
