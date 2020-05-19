'''
You have a positive integer. Try to find out how many digits it has?

Input: A positive Int
Output: An Int.

У вас есть положительное целое число. Попробуйте узнать, сколько у него цифр?

Вход: положительный Int
Выход: Int.
'''

def number_length(a: int) -> int:
    # your code here
    return len(str(a))




# auto-testing
print(number_length(10)) #== 2
print(number_length(0)) #== 1
print(number_length(4)) #== 1
print(number_length(443)) #== 2