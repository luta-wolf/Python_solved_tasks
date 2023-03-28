n = 8
l = [(0, 0), (1, 1), (0, 2), (5, 0), (5, 2), (0, 4), (3, 0), (3, 4)]

max_s = 0
for i in range(n):
	rect = {}
	rect['first'] = (l[i])
	first_ugol = False
	second_ugol = False
	for j in range(i + 1, n):
		if l[i][0] == l[j][0] and not first_ugol:
			rect['second'] = (l[j])
			first_ugol = True
		if l[i][1] == l[j][1] and not second_ugol:
			rect['third'] = (l[j])
			second_ugol = True
		if first_ugol and second_ugol:
			if rect['second'][1] == l[j][1] and rect['third'][0] == l[j][0]:
				rect['forth'] = l[j]
				print(rect)
				current_max = (l[j][0] - rect['first'][0]) * (l[j][1] - rect['first'][1])
				print(current_max)
				if current_max > max_s:
					max_s = current_max
				rect = {'first': rect['first']}
				first_ugol = False
				second_ugol = False
	rect = {}
	first_ugol = False
	second_ugol = False

print(max_s)
