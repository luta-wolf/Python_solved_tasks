class SlideAverage:

	def __init__(self, array, num) -> None:
		self.array = array
		self.num = num

	def middle(self):
		if self.num == 0:
			self.num = -1
		return sum(self.array[-self.num:]) / self.num

	def addNum(self, n):
		return self.array.append(n)

win = 5
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

p1 = SlideAverage(array, win)
print(p1.middle())
print(array)
p1.addNum(11)
print(p1.middle())
print(array)

test1 = SlideAverage([1, 2, 3], 3)
if test1.middle() == 2:
	print('Test1 Ok')
else:
	print('Test1 Fail')

test2 = SlideAverage([1, 2, 3], 1)
if test2.middle() == 3:
	print('Test2 Ok')
else:
	print('Test2 Fail')

test3 = SlideAverage(array, 0)
if test3.middle() < 0:
    print('Test3 Ok')
else:
    print('Test3 Fail')


# print('Test Ok' if test1.middle() < 0 else 'Test Fail')
