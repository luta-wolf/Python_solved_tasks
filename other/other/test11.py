import itertools

def check_mission(heroes, mission):
  mis = []
  for i in mission:
    available_herose = []
    for j in heroes:
      if i in j[1]:
        available_herose.append(j[0])
    if len(available_herose):
      mis.append(tuple(available_herose))
    else:
      return tuple([])

  print('------\n', mis)
  combinations = list(itertools.product(*mis))
  print('------\n',combinations, len(combinations))
  for combination in combinations:
    if len(set(combination)) == len(mission):
      return(combination)
  return tuple([])

# def check_mission(heroes: tuple, mission: tuple):
#     hers = sorted(heroes, key=lambda x: len(x[1]))
#     result = []
#     abilities = list(mission)

#     for h in hers:
#         for a in abilities:
#             if a in h[1] and h[0] not in result:
#                 abilities.remove(a)
#                 result.append(h[0])

#     return(tuple(result) if len(result) == len(mission) else ())

heroes = (("Илья М.", (1, 2, 3)),)
mission = (1,)

heroes2 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)
mission2 = (1, 2)

heroes3 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))
mission3 = (1, 1, 2)

heroes4 = (("Добрыня Н.", (2, 3)), ("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )))
mission4 = (1, 1, 2)

heroes5 = (("Добрыня Н.", (2, 3)), ("Илья М.", (2,)), ("Алёша П.", (1, )))
mission5 = (1, 1, 2)

heroes6 = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)
mission6 = (1, 5)

heroes7 = (("Добрыня Н.", (1, 2, 3, 4)), ("Илья М.", (1, 2, 4)), ("Алёша П.", (1, 2, 4)), ("Змей Г.", (1, 2, 4)))
mission7 = (1, 2, 3, 4)

heroes8 = (("Добрыня Н.", (1, 2, 3, 4)), ("Илья М.", (1, 2)), ("Алёша П.", (2, 4)), ("Змей Г.", (1, 4)))
mission8 = (1, 2, 3, 4)

# test Ok
print(check_mission(heroes, mission))
print(check_mission(heroes2, mission2))
print(check_mission(heroes3, mission3))
print(check_mission(heroes4, mission4))
print(check_mission(heroes5, mission5))
print(check_mission(heroes6, mission6))
print(check_mission(heroes7, mission7))
print(check_mission(heroes8, mission8))

b = [(1,2), (2,3), (1,3)]
a = list(itertools.product(*b))
# a = list(itertools.product(range(2), repeat=2))
print(a)

digits = range(10)
k = 0
combinations = itertools.product(digits, repeat=4)
print(list(digits))
for i in combinations:
  if len(set(i)) == 4:
    print(i)
    k += 1
print(k)


import string, itertools
letters = list(string.ascii_lowercase[:8])
print(letters)
num = -1
digits = range(1, 9)
for (letter, digit) in itertools.product(letters, digits):
	num += 1
	if num % 8 == 0:
		print()
	print(letter+str(digit), end=' ')
