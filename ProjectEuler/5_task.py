'''
Задача 4 - Smallest multiple
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''
#Factorial
n =10
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(factorial)
#Делители
list = []
for i in range(1,(factorial)):
        if factorial % i == 0:
            list.append(i)
print(list)
