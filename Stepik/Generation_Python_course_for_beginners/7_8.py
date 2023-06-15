# Тема урока: вложенные циклы
import time

for hours in range(24):
	for minutes in range(60):
		for seconds in range(60):
			time.sleep(1)
			print(hours, ':', minutes, ':', seconds)

# task 1 Таблица-1
n = int(input())
for i in range(n):
    print(f'{n} {n} {n}')

# task 2 Таблица-2
n = int(input())
for i in range(1, n + 1):
    print(i, i, i, i ,i)

n = int(input())
for i in range(1, n +1):
    for j in range(5):
        print(i, end=' ')
    print()

# task 3 Таблица-2
n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(f'{i} + {j} = {i + j}')
    print()

# task 4 Звездный треугольник 🌶️🌶️
n = int(input())
j = 0
for i in range(n):
    if i < n // 2 + 1:
        j += 1
    else:
        j -= 1
    print('*' * j)

n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))

# task 5 Численный треугольник 1
n = int(input())
for i in range(1, n + 1):
    print(str(i) * i)

# task 7 12 месяцев
print()
for n in range(1, 14):
	for k in range(1, 13):
		for m in range(1, 12):
			if n * 28 + k * 30 + m * 31 == 365:
				print(n, k, m)

# task 8 Старинная задача
# быки 10р
# корова 5 руб
# теленок 0,5 руб
for b in range(1, 11):
	for k in range(1, 21):
		for t in range(1, 201):
			if b * 10 + k * 5 + t * 0.5 == 100 and b + k + t == 100:
				print(n, k, m)

# task 9 Гипотеза Эйлера о сумме степеней 🌶️🌶️
from datetime import datetime
start_time = datetime.now()
flag = 0
for a in range(1, 150):
	for b in range(a, 150):
		for c in range(b, 150):
			for d in range(c, 150):
				e = (a**5 + b**5 + c**5 + d**5)**(1/5)
				if int(e) == round(e, 10):
						print(a,b,c,d,int(e))
						print(a+b+c+d+int(e))
						flag = 1
						break
			if flag:
				break
		if flag:
			break
	if flag:
		break

end_time = datetime.now()
print(f'Duration: {end_time - start_time}')
