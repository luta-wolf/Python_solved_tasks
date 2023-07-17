n = 100000
for i in range(120):
	n += n * 0.01
print(n)


n = 100000
print(n * (1 + 0.12/12)**(120))


pv = 50000
r = 10
t = 5
fv = pv * (1 + 0.1/12)**(t * 12)
print(fv)

pv = 50000
r = 10
t = 5
fv = pv * (1 + r/100*t)
print(fv)

n = 5
a = 100
r = 0.12
m = 12
p = 4
fv = a * ((1 + r/m)**(m*n) - 1) / ((1 + r/m)**(m/p) - 1)
print(fv)

print('-' * 20)

s = 0
n = 365 * 2
for i in range(1, n + 1):
	s += i
	if i % 10 == 0:
		print(f'День {i} - кладем {i} руб, в копилке {s} руб')
print(s)

print(10000/365)



# n = 10
# a = 5000
# r = 0.1
# m = 12
# p = 12
# fv = a * ((1 + r/m)**(m*n) - 1) / ((1 + r/m)**(m/p) - 1)
# print(fv)

time = 12 * 10
money = 150000
per = (15 / 12) / 100
for i in range(time):
	money += money * per
print(money)

lst = [1, 2, 3, 4]
print(sum(lst, start=10))
#
