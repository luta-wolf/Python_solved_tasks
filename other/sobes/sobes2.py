# def some_func(some_args: list = []):
# 	some_args.append(1)
# 	return some_args

# print(some_func())
# print(some_func())
# print(some_func())
# print(some_func())


# def some_func2(some_args: list = []):
# 	some_args.append(1)
# 	return some_args

# print(some_func2())
# print(some_func2())
# print(some_func2())
# print(some_func2())

# def funk(*args):
# 	print('\nType of data = ', type(args))
# 	sum = 0
# 	for n in args:
# 		sum += n
# 	print(sum)

# funk(1, 2, 3, 4, 5)
# funk(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# def funk2(**kwargs):
# 	print('\nType of data = ', type(kwargs))
# 	sum = 0
# 	for k, v  in kwargs.items():
# 		print(f'{k}   {v}')

# funk2(a = 1, b =  2, c =  3, d = 4, e = 5)


# def some_func(some_args: list = []):
# 	some_args.append(2)
# 	return some_args

# print(some_func())
# print(some_func())
# print(some_func())
# print(some_func())


# tup = ('a', 'b')
# print(tup, type(tup))
# b = []
# tup2 = ('a', b)
# b.append(1)
# print(tup, type(tup))
# c = {tup2: 11}
# print(c, type(c))


# a = [1, 2, 9, 10]
# for x in [8, 7, 6, 5, 4, 3]:
#     a.insert(2, x)

# print(a)


# def decorator(func):
# 	def wrapper(*args, **kwargs):
# 		result = func(*args, **kwargs)
# 		return result
# 	return wrapper

# @decorator()
# def some():
# 	print('funk')

# some()

# def some_2():
# 	pass

# some_2_with_dec = decorator(some_2)


#decarator
def header(func):

	def inner(*args, **kwargs):
		print('<h1>')
		func(*args, **kwargs)
		print('</h1>')
	return inner

def table(func):

	def inner(*args, **kwargs):
		print('<table>')
		func(*args, **kwargs)
		print('</table>')
	return inner

@header
@table  # say = header(table(say))
def say(name, surname, age):
	print('hello', name, surname, age)


# say = table(header(say))
# say('Vasia', 'Ivavov', 30)
# print('-' * 20)
# say = header(table(say))
say('Vasia', 'Ivavov', 30)
print('-' * 20)


def decor(func):
	def inner(*args, **kwargs):
		print('start')
		func(*args, **kwargs)
		print('finish')
	return inner

@decor
def say(name, surname):
	print(f'Hello {name} {surname}')

say('Vasia', 1)
print('-' * 20)

# абстрактные классы
from abc import ABC, abstractclassmethod, abstractmethod

class A(ABC):
	@abstractclassmethod
	def some(self):
		print('абстракция')
	@abstractclassmethod
	def some2(self):
		print('абстракция2')


class B(A):
	a = 1
	def some(self):
		print('а-------')
	def some2(self):
		print('-------я')

A.some()

obj = B()
obj.some()
obj.some2()


class Basic(ABC):
    @abstractmethod
    def hello(self):
        print("Hello from Basic class")


class Advanced(Basic):
    def hello(self):
        super().hello()
        print("Enriched functionality")


a = Advanced()
a.hello()
print('-' * 20)
'''
# Что такое async и await?
- Python не многопоточный язык

Какие модули в Python есть для тетирования?Какие отличия, плюсы и минусы?
- Тесты нужны всегда
- Unittest -(встроенный, он не pip8 френдли) тестирует мелкий функционал. 
Класс, функцию, какой-то минимальный блок. Плюсы: встроен
- Pytest (более широкий функциона, куча батареек, работа с текстурами) Плюсы: Гибкий, наличие кучи плагинов

Что такое moсk? Зачем нужен?
- Иногда нам нужно избежать каких то вызовов. mock это такой объект, 
который подменяет реальный объект и мы можем задать ожидаемое поведение.

Какие есть типы асинхронного выполнения?

Что такое ORM? С какими работал?
- Объектно-реалиационное отображение. У нас есть код на питоне, у нас есть база данных, а 
ORM это прослойка в виде библиотеки, которая связывает наши объекты и классы с таблицами и 
стоками в базе данных
- Django ORM
- SQLAlhemy - здоровенный фрейморк

Чем отличаются импотыр от абслютных?

Best practic     
- SOLID 
single responsibility - Принцип единственной ответственности 
Для каждого класса должно быть определено единственное назначение. 
Все ресурсы, необходимые для его осуществления, должны быть инкапсулированы 
в этот класс и подчинены только этой задаче.
 
open–closed - Принцип открытости/закрытости  «программные сущности … 
должны быть открыты для расширения, но закрыты для модификации».
Liskov substitution - Принцип подстановки Лисков
«функции, которые используют базовый тип, должны иметь возможность 
использовать подтипы базового типа не зная об этом». 
interface segregation - Принцип разделения интерфейса 
«много интерфейсов, специально предназначенных для клиентов, лучше, 
чем один интерфейс общего назначения»
dependency inversion - Принцип инверсии зависимостей 
«Зависимость на Абстракциях. Нет зависимости на что-то конкретное».
- KISS - «Keep it simple, stupid» — «Делай проще, тупица» 
нужно держать свои функции максимально простыми и тупыми, 
чтобы они выполняли то, что нужно
- DRY - Don’t repeat yourself «не повторяйся» - 
не повторяй свой код, выноси его в функцию
- YAGNI «You aren't gonna need it»; с англ. «Вам это не понадобится» - 
 у тебя в коде должен быть функционл, который нужен тебе сейчас 
 (отказ добавления функциональности, в которой нет непосредственной надобности.)
 
Conflict management - вопрос на разрешение любой конфликтной ситуции
SDLC - управление проектами в команде
Adjale 
Scram - больше всего работтают в этим
CanBan


Базы данных
Какие NoSQL базы данных ты знаешь? С какими работал? Кейсы использования? Плюсы и минусы?
Redis - In-Memory резидентная (находящаяся в памяти). Используется как для баз данныхб так 
и для реализации кэшей и брокеров сообщений.Для высоконагруженных систем.
Mongo DB - документоориентированная бд, инфа хранится в json формате. Высокая доступность,
масштабируемость и безопасность, кросспоатформенность и быстрое разворачивание в облаке
Данные хранятся в виде коллекций и документов 
Какие SQL базы данных ты знаешь? С какими работал? Кейсы использования? Плюсы и минусы?
PK,  FK
Типы связей? Как реализуется многие ко многим?
Зачем нужны индексы?
Зачем нужны тригеры?
Что такое транзакция?
ASID
Уровни изолированной транзакции?
'''