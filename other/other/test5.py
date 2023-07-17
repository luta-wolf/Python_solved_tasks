num = int(input())
max_num = num
min_mum = num
for i in range(10):
	num = int(input())
	if num > max_num:
		max_num = num
	elif num < min_mum:
		min_mum = num

print('Max num = ', max_num)
print('Min num = ', min_mum)
