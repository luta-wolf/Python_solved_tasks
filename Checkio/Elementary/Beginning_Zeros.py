'''
You have a string that consist only of digits. You need to find how many zero digits ("0")
are at the beginning of the given string.

Input: A string, that consist of digits.
Output: An Int.

У вас есть строка, состоящая только из цифр. Вам нужно найти, сколько нулевых цифр ("0")
находится в начале данной строки.

Ввод: строка, состоящая из цифр.
Выход: Int.
'''
import re
def beginning_zeros2(number: str) -> int:
    return len(''.join(re.findall(r'^0+', number)))

def beginning_zeros3(number: str) -> int:
    return len(re.sub(r'[^0].*$', '', number))

def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))

# auto-testing
print(beginning_zeros('100')) #== 0
print(beginning_zeros('001')) #== 2
print(beginning_zeros('100100')) #== 0
print(beginning_zeros('001001')) #== 2
print(beginning_zeros('012345679')) #== 1
print(beginning_zeros('0000')) #== 4
