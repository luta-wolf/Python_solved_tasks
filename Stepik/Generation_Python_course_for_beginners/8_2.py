# Экзамен

# task 1 Ревью кода - 7 🌶️
n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)

# task 2 Ревью кода - 8 🌶️
n = 8 						# n = 7, по условию чисел 8
count = 0
maximum = -10**12 			# maximum = 1000, все случаи, когда все числа меньше 1000, обрабатываются неверно
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:			# x // 4 == 0, по условию нужно найти числа, дел. на 4 без остатка
        count += 1
        if x > maximum:		# if x < maximum, если число больше максимума, оно его заменяет, не если меньше максимума
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# task 3 Ревью кода - 9
n = 4
count = 0
maximum = -10**8 - 1 #
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x #
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# task 4 Звездная рамка
n = int(input())
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * 19)
    else:
        print('*' + ' ' * 17 + '*')

# task 5 Третья цифра
n = int(input())
print((n // 10**(len(str(n)) - 3)) % 10)

n = int(input())
while n > 999:
    n //= 10
print(n % 10)

# task 6 Все вместе 2
n = int(input())
last_digit = n % 10

count_three = 0
count_last = 0
count_even = 0
sum_digit_more_five = 0
res_digit_more_seven = 1
count_zero_five = 0

while n > 0:
    digit = n % 10
    if digit == 3:
        count_three += 1
    if digit == last_digit:
        count_last += 1
    if digit % 2 == 0:
        count_even += 1
    if digit > 5:
        sum_digit_more_five += digit
    if digit > 7:
        res_digit_more_seven *= digit
    if digit == 0 or digit == 5:
        count_zero_five += 1
    n //= 10

print(count_three)
print(count_last)
print(count_even)
print(sum_digit_more_five)
print(res_digit_more_seven)
print(count_zero_five)

# task 7 Числа Рамануджана 🌶️

max_digit = 0
for a in range(1, 50):
	for b in range(1, 50):
		for c in range(1, 50):
			for d in range(1, 50):
				if a**3 + b**3 == c**3 + d**3 and a != b and a != c and a != d and b != c and b != d and c != d:
					print(a, b, c, d)
					print(a**3 + b**3)
'''
1729
4104
13832
20683
32832
'''
