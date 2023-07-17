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



def sum_nums(*args):
	print(type(args))
	s = 0
	for i in args:
		s += i
	print(s)

sum_nums(1, 2, 3)
sum_nums(1, 2, 3, 4, 5, 6)

def sum_name(**kwargs):
	print("\n Type of aguments", type(kwargs))
	for key, value in kwargs.items():
		print(f'{key}, {value}')

sum_name(name="Anna", surname = "Green", age = 30)


vv = 10
print(id(vv))


