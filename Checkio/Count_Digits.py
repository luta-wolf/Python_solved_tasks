'''
You need to count the number of digits in a given string.

Input: A Str.
Output: An Int.

Вам нужно посчитать количество цифр в данной строке.

Вход: строка.
Выход: Int.
'''

import re
def count_digits(text):
    pattern = r'[1234567890]'
    return len(re.findall(pattern,text))

#best
def count_digits2(text):
    return len(re.findall(r'\d',text))

#test
print(count_digits('hi')) #== 0
print(count_digits('who is 1st here')) #== 1
print(count_digits('my numbers is 2')) #== 1
print(count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')) #== 8
print(count_digits('5 plus 6 is')) #== 2
print(count_digits('')) #== 0