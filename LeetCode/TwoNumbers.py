def addTwoNumbers(l1, l2):

	test = l1[::]
	count = 0
	while(True):
		if test:
			test.pop()
			count += 1
		else:
			break
	num = 0
	for i in range(count):
		num += l1[i] * 10 ** i

	test = l2[::]
	count = 0
	while(True):
		if test:
			test.pop()
			count += 1
		else:
			break
	num2 = 0
	for i in range(count):
		num2 += l2[i] * 10 ** i

	num = num + num2
	num2 = num

	count = 1
	while(True):
		if num // 10 > 0:
			count += 1
		else:
			break
		num = num // 10

	l3 = []
	for i in range(count):
		l3.append(num2 % 10)
		num2 = num2 // 10

	return l3


l1 = [2,4,3]
l2 = [5,6,4]

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]


print(addTwoNumbers(l1, l2))
