a = [
	['В новом году мы уйдем'],
	['В новом году мы не уйдем'],
	['В новом году мы прийдем'],
	['Мы любим тебя'],
	['Мы любим не тебя']
]
b = []
с = []
for i in a:
	if not i[0].startswith('В новом году'):
		b.append(i)
		# continue
	# else:
	# 	с.append(i)
print('b = ', b)
print('c = ', с)
print('a = ', a)

# a = [
# 	['В новом году мы уйдем'],
# 	['В новом году мы не уйдем'],
# 	['В новом году мы прийдем'],
# 	['Мы любим тебя'],
# 	['Мы любим не тебя']
# ]
# i = 0
# len_a = len(a)
# while i < len_a:
# 	if a[i][0].startswith('В новом году'):
# 		a.pop(i)
# 		i -= 1
# 		len_a -= 1
# 	i += 1
# print(a)

# a = [
# 	['В новом году мы не уйдем'],
# 	['Мы любим тебя'],
# 	['В новом году мы прийдем'],
# 	['Мы любим не тебя'],
# 	['В новом году мы уйдем'],
# ]
# i = 0
# try:
# 	while True:
# 		if a[i][0].startswith('В новом году'):
# 			a.pop(i)
# 			i -= 1
# 		i += 1
# except IndexError:
# 	pass
# print(a)

# a = [
# 	['В новом году мы не уйдем'],
# 	['Мы любим тебя'],
# 	['В новом году мы прийдем'],
# 	['Мы любим не тебя'],
# 	['В новом году мы уйдем'],
# ]
# b = filter(lambda x: not x[0].startswith('В новом году'), a)
# print(list(b))



# import string

# i = 0
# for letter in string.letters:
#     print("The letter at index %i is %s" % (i, letter))
#     i = i + 1

# a = [1,2]
# b = [1,2]
# print (a is b)
# print (a == b)

# # string = '123456'
# # string[5] = '9'
# # print(string)

# def some_function(some_arg: list = []):
#     some_arg.append(1)
#     return some_arg

# print(some_function())
# print(some_function())
# print(some_function())
# print(some_function())

# s_list = [1, 2, 3]
# print(list(filter(lambda x: isinstance(x, int), s_list)))
# print('-' * 20)
# # тернарный оператор
# some = True
# result = 1 if some else 0
# print(result)

# import copy

# some_list = [1, [2], 3]
# print(some_list[1] is copy.copy(some_list)[1])
# print(some_list[1] is copy.deepcopy(some_list)[1])

# print(2 in [1, 2, 3])
# print(2 in {1, 2, 3})

# class A:
# 	def a(self):
# 		__some_val = 0

# 	@classmethod
# 	def b(cls):
# 		pass

# 	@staticmethod
# 	def c(self):
# 		pass

# a = A()

# a.a()
# A.b()
# A.c()
# a._some_val
# a._A__some_val

# def decorator(func):
# 	def wrapper(*args, **kwargs):
# 		result = func(*args, **kwargs)
# 		return result
# 	return wrapper

# @decorator
# def some():
# 	pass

# def some_2():
# 	pass

# some_2_with_dec = decorator(some_2)

# from abc import ABC, abstractmethod
# class A(ABC):
# 	@abstractmethod
# 	def some():
# 		pass

# A()

# a = 10*10 + (10 + 1) * (10 + 1) + (10 + 2) * (10 + 2) + (10 + 3) * (10 + 3) + (10 + 4) * (10 + 4)
# b = 5 * 100 + 2*10*1 + 1*1 + 2*10*2 + 2*2 + 2*10*3 + 3*3 +2*10*4 + 4*4
# c = 5 * 100 + 20 * (1 + 2 + 3 + 4) + 1 + 4 + 9 + 16
# d = 500 + 200 + 30
# e = 730 / 365

# def f():
# 	x = 15
# 	print(x)
# x = 12
# f()


# class A():
# 	def test(self):
# 		print("A")

# class B(A):
# 	def test(self):
# 		print("B")

# class C(A):
# 	def test(self):
# 		print("C")

# class D(B, C):
# 	def new_test(self):
# 		print("D")

# obj = D()
# obj.test()
# obj.new_test
# obj2 = A()
# obj2.test()

class A():
	def test(self):
		print("A")

class B(A):
	def test(self):
		print("B")

class C(A):
	def test(self):
		print("C")

class D(B, C):
	def new_test(self):
		print("D")

# obj = D()
# obj.test()

print('-' * 20)
print(D.mro())
print('-' * 20)


# a = [[]] * 3
# a[1].append(1)
# print(a)

# a = {}

# a["key"] = 'value'

# a[('tuple')] = 'value1'

# a[(1, 2)] = 'value2'

# print(a)


# def decor(func):
# 	mem = []
# 	def wraps(i):
# 		print(f'MEM: {mem}')
# 		print('до вызова')
# 		i *= 2
# 		print(func(i))
# 		mem.append(func(i))
# 		print('после вызова')
# 	return wraps

# @decor
# def calc(i: int):
# 	return i ** 2


# calc(10)
# calc(20)
# calc(30)
# calc(40)


# corpus = ['Мама мыла раму', 'Даша мыла яблоки', 'Даша очень любит маму']
# corpus_lem = []

# for cor in corpus:
# 	a = cor.lower()
# 	b = a.replace('мыла', 'мыть')
# 	c = b.replace('любит', 'любить')
# 	corpus_lem.append(c)

# print(corpus_lem)


from pymystem3 import Mystem

corpus = ['Мама мыла раму', 'Даша мыла яблоки', 'Даша очень любит маму']
corpus_lem = []
mystem = Mystem()

for cor in corpus:
	a = mystem.lemmatize(cor)[:-1]
	b = ''.join(a).replace('мыло', 'мыть')
	corpus_lem.append(b)

print(corpus_lem)

corpus_tokenized = [sentence.split() for sentence in corpus_lem]
line = []
words_indiced = {}
k = 0

for sentence in corpus_tokenized:
	for i in sentence:
		if not i in line:
			line.append(i)
			words_indiced[i] = k
			k += 1

# for i in enumerate(line):
# 	words_indiced[i[1]] = i[0]
print(words_indiced)


class A:
	a = 'hello'
	def print_a(self):
		print('a')

class B(A):
	def print_b(self):
		print('b')

class C(A):
	def print_c(self):
		print('c')

class D(B, C):
	pass

bob = D()
bob.print_a()
bob.print_b()
bob.print_c()
print(bob.a)

