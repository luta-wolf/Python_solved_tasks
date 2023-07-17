# some_string = '12345'

# some_string[3] = 9

# print(some_string)

# def some_func(arg: list = []):
# 	arg.append(1)
# 	return arg

# print(some_func())
# print(some_func())
# print(some_func())

# что такоей args и kwargs ?
# args - это аргумент, который принимает в себя неограниченное количесво позиционных аргументов функции
# kwargs - тоже принимает неограниченное кол-во элементо, которые мы передаем с помощью ключевых слов
'''
*args для неименованных аргументов; Аргументы передаются как кортеж ()
**kwargs для именованных аргументов. Аргументы передаются как словарь {}
Мы используем *args и **kwargs в качестве аргумента, когда заранее не известно, сколько значений мы хотим передать функции.
- *args и **kwargs — специальный синтаксис, позволяющий передавать в функцию переменное количество аргументов. При этом, совсем не обязательно использовать имена аргументов args и kwargs;
- *args используется для неименованных аргументов, с которыми можно работать как со списком;
- **kwargs используется для именованных аргументов, с которыми можно работать как со словарём;
- если вы хотите использовать и *args, и **kwargs, то это делается так: func(fargs, *args, **kwargs), порядок следования аргументов важен;
'''
# Асинхронность — это возможность выполнения программой задач и процессов без ожидания их завершения.

def adder(*nums):
	print("\nData type of argument: ",type(nums))
	sum = 0
	for n in nums:
		sum += n
	print("Sum: ", sum)

adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)

print('-' * 20)

def intro(**data):
	print("\nData type of argument: ",type(data))

	for key, value in data.items():
		print("{} is {}".format(key, value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

print('-' * 20)

a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = [1, 2, 3]
print(a, b, c)
a, b, c = [True, 2, 'Hello']
print(a, b, c)
a, *b, c = [True, 2, 'Hello', 9, '54', 77]
print(a, b, c)
*a, b, c = [True, 2, 'Hello', 9, '54', 77]
print(a, b, c)
*a, b, c = 'Hello World'
print(a, b, c)

s = [4, 10]
print(list(range(1, 5)))
print(list(range(*s)))

print('-' * 20)

def f(a, b, c, d):
	print(a, b, c, d)

f(1, 2, 3, 4)
a = (True, 'Hello', 78, [1, 2, 3])
f(* a)

def f(*args):
	 print(args, type(args))

f(1, 2, 3, 4, 5, 6)
f(1, 2, 3 )
f()


def f(**kwargs):
	for k, v in kwargs.items():
		print(k, v)

f(a = 1, b = 2, c = 3, name=90)


def f(*args, **kwargs):
	print(args, kwargs)

f(45,2,6, "gfff", a = 1, b = 2, c = 3, name=90)


def outPrint(*args, sep='#', end='@'):
	print(args, sep, end)

outPrint(1, 2, 3, 4, 5, sep='90')
outPrint(1, 2, 3,  end=111)


a = [1, 2, 3, 4, 5]
print(a)
print(*a)

print('-' * 20)

a = 1
b = 2
a = a + b
print(a)

'''
Магичиские методы (dunder methods) __str__ , __repr__
оба метода отвечают за текстовое отображение нашего метода в системе
 __repr__ - как его будут видет разработчики
 __str__ - как будет отображен объект если к нему применить str() или print().
 т. е. как увидят этот объект пользователи
'''

# class Lion:
# 	def __init__(self, name):
# 		self.name = name

# 	def __repr__(self):
print('-' * 20)
a = 123
import math, time

n = 1233211233555252252252525214341414141143141411414141414144141441434252521141413411431243214123413413
b = time.time_ns()
# if a == a[::-1]:
# 	print('полиндом')
# 	print
# else:
# 	print('no')
bb = len(str(n))
print(f'{bb} time: {time.time_ns() - b}')


a = time.time_ns()
digits = int(math.log10(n))+1
# print(digits)
print(f'{digits} time: {time.time_ns() - a}')

c = time.time_ns()
s = 1
while n >= 10:
	n = n // 10
	s += 1
print(f'{s} time: {time.time_ns() - c}')

print('-' * 25)

a = [x ** 2 for x in range(5)]
print(a)
newlist = [x for x in range(10)]
print(newlist)

x = 5
a = lambda x:  x **2
print(a(5))
b = lambda x, y: x * y
print(b(3, 4))

double = lambda x: x*2
print(double(10))

def double2(x):
		return x * 2
print(double2(20))

print('-' * 25)

def defined_cube(y):
	return y*y*y


lambda_cube = lambda y: y*y*y
print(defined_cube(2))
print(lambda_cube(2))

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: x % 2 ==0, my_list))
print(new_list)

current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x : x**2, current_list))
print(new_list)
