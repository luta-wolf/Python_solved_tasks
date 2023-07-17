# lst = [1000, 5, 13, 203, 400, 60, 0]
# lst2 = [993, 123, 90, 345, 13, 3, 1, 0]
# num_max = 0
# for i in lst2:
# 	if i % 10 == 3 and i > num_max:
# 		num_max = i
# print(num_max)


# v = int(input("Введите количество строк: "))
# s = int(input("Введите количество символов в строке: "))

# for i in range(v):
#     for j in range(s):
#         if i % 2 == 0:
#             print("*", end="")
#         else:
#             print("-", end="")
#     print()


# n = int(input("Введите количество людей, которым рассказывают слух в день: "))

# people = 1 # изначально слух знает 1 человек
# t = 1

# for i in range(7):
# 	t *= n
# 	people += t # умножаем на количество людей, которым рассказывают слух в день
# 	print(people)
# 	# n -= 1 # уменьшаем количество людей, которым еще не рассказали слух

# print("Через 7 дней историю будет знать:", people, "человек")


# string = input()
# string = string.lower()[:30]
# print(string.count('нео'))

# n = int(input())
# lst = []
# num = int(input())
# lst.append(num)
# num_max = num
# num_min = num
# for i in range(n - 1):
# 	num = int(input())
# 	lst.append(num)
# 	if num > num_max:
# 		num_max = num
# 	if num < num_min:
# 		num_min = num
# for i in range(len(lst)):
# 	if lst[i] == num_min:
# 		lst[i] = num_max

# print(lst)

class Client:
	def __init__(self, name, town, age):
		self.name = name
		self.town = town
		self.age = age

	def print_info(self):
		string = f'Имя: {self.name}\nГород: {self.town}\nВозраст: {self.age} '
		if self.age % 10 == 1:
			s = 'год'
		elif self.age % 10 == 2 or self.age % 10 == 3 or self.age % 10 == 4:
			s = 'года'
		else:
			s = 'лет'
		print(string + s)
ll = Client('Дмитрий', 'Москва', 23)
ll.print_info()
l1 = Client('Денис', 'Волгоград', 25)
l1.print_info()
l2 = Client('Алина', 'Москва', 42)
l2.print_info()
l3 = Client('Максим', 'Краснодар', 31)
l3.print_info()

print(1*2*3*4)
