# def check_mission(heroes, mission) -> tuple:
# 	lst_man = []
# 	lst_power = []
# 	for man, superpowers in heroes:
# 		for i in superpowers:
# 			lst_power.append(i)
# 			if i in mission:
# 				lst_man.append(man)
# 		for i in mission:
# 			if i not in set(lst_power):
# 				return ()
# 	return tuple(set(lst_man))



# heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))
# mission = (1, 1, 2)

# heroes2 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)
# mission2 = (1, 5)

# heroes3 = (("Илья М.", (1, 2, 3)),)
# mission3 = (1,)

# print(check_mission(heroes, mission))
# print(check_mission(heroes2, mission2))
# print(check_mission(heroes3, mission3))

# x = range(0, 5)
# for i in enumerate(enumerate(x)):
#   print(i)

# def zipp(map):
# 	str = map * 2
# 	return str
# print(zipp("123"))

def a(x):
	if not x:
		print("in NOT X")
		def x(y):
			print("in X")
			print(y)
	print("before", x)
	x(1)
	print("after")
a(lambda x: print(-x))
print('-' * 5)
a(None)

