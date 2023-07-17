print(f'---{int(2.5**6)}---')

lst = [x for x in range(1,11)]
product = 1
for i in lst:
	if i % 2 == 0:
		product *= i

print(product)

lst = [x for x in range(-10,11)]
print(lst)
product = 1
for i in lst:
	if i % 2 != 0:
		product *= i

print(product)

lst = [x for x in range(1, 7)]
print(lst)
product = 1
for i in lst:
		product *= i

print(product)


money = 100_000
for i in range(12):
	print(i)
	money *= 1.02

print(int(money))
