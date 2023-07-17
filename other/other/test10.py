# a = 12345
# b = (a // 100) % 10

# print(int(b))

# a = int(input())
# max_n = a
# for i in range(9):
# 	a = int(input())
# 	if a > max_n:
# 		max_n = a

# print('-' * 104)
# print(max_n)

# print('-' * 10)
# lst = [x for x in range(10)]
# print(lst)
# print(lst[5])
# print('-' * 10)

d = {0:1, 1:2, 2:3}
for u in d:
	print(u)
print(sum(d))

# lst = [1,2,3,7]
# print(contains(lst))
# a = (x for x in [1, 2])
# print(a)

# class printer():
# 	def __init__(self):
# 		print('printer is on')

# 	def work(self):
# 		print(' '.join('printer goes brrrrrrrr'.split()[::-1]))

# 	def __del__(self):
# 		print('printer is off')

# printer.work(1)
# a = printer()
# a.work()

# l = ['Jim', 'Joahnna', 'Max', 'Susanna']
# l.sort
# print(l)

# x = {x for x in range(3)}
# print(type(x))

# class mama(object):
# 	def says(self):
# 		print(1)

# class sis(object):
# 	def says(self, ):
# 		super().says()
# 		print(2)

# s = sis()
# super(s.__class__, s).says()

l = ['', '1', '2', '', '3', False, None]
x = list(filter(None, l))
print(x)

d = dict()
for x, y in enumerate(range(5, 0, -1)):
	d[x] = y
for k in d:
	print(k, end=', ')
print()
x, y, *z = 1,2,3,4,5
print(x,y,z)
