# a = int(input())
# b = int(input())
# speed = int(input())
# time = (b - a) / speed
# print(f'{time:.2f}')

# a = int(input())
# b = int(input())
# bb = int(str(b), 2)
# print(a + bb)

# price = int(input())
# money = int(input())
# price2 = int(str(price), 2)
# print(money - price2)


goods = input()
price = int(input())
weight = int(input())
money = int(input())
total = int(price * weight)
change = money - total
pr_we = str(weight) + 'кг' + ' * ' + str(price) + 'руб/кг'
print('=' * 16 + 'Чек' + '=' * 16)
print(f'{"Товар:" :<10}{goods :>25}')
print(f'{"Цена:" :<10}{pr_we :>25}')
print(f'{"Итого:" :<10}{total :>22}{"руб" :>3}')
print(f'{"Внесено" :<10}{money :>22}{"руб" :>3}')
print(f'{"Сдача:" :<10}{change :>22}{"руб" :>3}')
print('=' * 35)

# n, m, k1, k2 = int(input()), int(input()), int(input()), int(input())
# for i in range(1, n):
# 	x = (n * m - i * k2) / k1
# 	if x * 10 % 10 == 0 and int(x) + i == n:
# 		break
# print(int(x), i)

# n, m, k1, k2 = int(input()), int(input()), int(input()), int(input())
# dif = k1 - k2
# dif1 = m - k2
# x = int(n * dif1 / dif)
# y = n - x
# print(x, y)
