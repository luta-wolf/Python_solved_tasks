'''
Check is the given number is even or not. Your function shoudl return True
if the number is even, andFalse if the number is odd.

Input: Int.

Output: Bool.
'''
def is_even2(num: int) -> bool:
    if num % 2 == 0: return True
    else: return False

# best
'''True = 1, False = 0. При вычислении четного числа остаток от деления всегда будет 0 или 1'''
def is_even(num: int) -> bool:
    return not bool(num % 2)
# 3th
'''Преобразуем десятичное число в двоичную строку и проверим последнюю цифру'''
def is_even3(num: int) -> bool:
    return bin(num)[-1] == '0'

# auto-testing
print(is_even(2)) == True
print(is_even(5)) == False
print(is_even(0)) == True