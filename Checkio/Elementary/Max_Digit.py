'''
You have a number and you need to determine which digit in this number is the biggest.

Input: A positive int.
Output: An Int (0-9).

У вас есть номер, и вам нужно определить, какая цифра в этом номере самая большая.

Вход: положительный Int.
Выход: Int (0-9).
'''
import re

def max_digit2(number: int) -> int:
    max_n = 0
    for i in re.findall(r'\d', str(number)):
        if int(i) > max_n:
            max_n = int(i)
    return max_n

#best
def max_digit(number: int) -> int:
    return int(max(str(number)))

# #auto-testing
print(max_digit(0)) #== 0
print(max_digit(52)) #== 5
print(max_digit(634)) #== 6
print(max_digit(1)) #== 1
print(max_digit(10000)) #== 1
