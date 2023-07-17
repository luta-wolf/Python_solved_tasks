# n = 1000
# k = 0
# for i in range(n):
# 	for j in range(n):
# 		if i == j or i + j == n - 1:
# 			print(1, end= ' ')
# 			k += 1
# 		else:
# 			print(0, end = ' ')
# 	print()
# print(k)


# for i in range(10):
# 	for j in range(10):
# 		# if i * j % 2 == 1:
# 		if (i + j) % 2 == 1:
# 			print(1, end= ' ')
# 		else:
# 			print(0, end = ' ')
# 	print()


# class Ball:
# 	def __init__(self, canvas, color):
# 		self.canvas = canvas
# 		self.id = canvas
# 		self.x2 = x2
# 		self.y2 = y2



# year = 2
# for i in range(year):
# 	print(f'year {2000 + i} {"winter":>10}')
# 	print(f'year {2000 + i} sping')
# 	print(f'year {2000 + i} summer')
# 	print(f'year {2000 + i} autumn')

# class A():
# 	def test(self):
# 		print('A')

# class B(A):
# 	def test(self):
# 		print('B')

# class C(A):
# 	def test(self):
# 		 print('C')

# class D(B, C):
# 	def test_a(self):
# 		print('D')

# a = D()
# a.test()
# a.test_a()


# for i in range(2, 10, 2):
# 	print (i + 1, "Роза")

def my_dec(a):
	return 10

@my_dec
def my_func(a):
	a *= 80
	return a

print(my_func if type(my_func) == int else my_func(1))
print(type(my_func))

# @my_dec
# def may_f(strr):
# 	return strr + '01'

# # print(may_f('strr'))
# print(type(may_f))
