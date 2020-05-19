'''
Try to find out how many zeros a given number has at the end.

Input: A positive Int
Output: An Int.

Попытайтесь выяснить, сколько нулей у данного числа в конце.

Вход: положительный Int
Выход: Int.
'''
import re
def end_zeros(num: int) -> int:
    zerro = re.findall(r'[0]+\b', str(num))
    return len(''.join(zerro))


# auto-testing
print(end_zeros(0)) #== 1
print(end_zeros(1)) #== 0
print(end_zeros(10)) #== 1
print(end_zeros(101)) #== 0
print(end_zeros(245)) #== 0
print(end_zeros(100100)) #== 2