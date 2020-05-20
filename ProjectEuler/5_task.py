'''
Задача 4 - Smallest multiple
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''

#Делители
def smallest_divisor(n):
    list = []
    for i in range(2, n):
        if n % i == 0:
            list.append(i)
    return list

#tests
print(smallest_divisor(10))
print(smallest_divisor(9))
print(smallest_divisor(8))
print(smallest_divisor(7))
print(smallest_divisor(6))
print(smallest_divisor(5))
print(smallest_divisor(4))
print(smallest_divisor(3))
print(smallest_divisor(2))
print(smallest_divisor(1))
