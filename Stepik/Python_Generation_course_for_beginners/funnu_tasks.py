# 1
# a, b, c = map(int, input())
# print(a, b ,c)

# 2
nums = [1, 2, 3, 4]
print(nums[10:])

# 3
data = {1}
data.add(1.0)
data.add(True)
print(len(data))
print('-' * 20)

# 4
def extend_list(value, lst = []):
	lst.append(value)
	return lst

lst1 = extend_list(10)
lst2 = extend_list(123, [])
lst3 = extend_list('a')
print(lst1, lst2, lst3)
print('-' * 20)

# 5
data = (['bee'], 'pygen')
try:
	data[0] += ['geek']
	print('good')
except:
	print(data[0])

# 6
def convert(n):
	s = ''
	for i in range(n + 1):
		s += str(i)
	return s

print(convert(0))
print(convert(5))
print(convert(12))


languages = ["Python", "C Programming", "Java", "JavaScript"]
smallest_string = min(languages)

print("The smallest string is:", smallest_string)

n = int(input())
lst = map(float, [input() for _ in range(n)])
print(int(sum(list(lst))))


