'''
Split the string into pairs of two characters. If the string contains an odd number of characters,
then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.
Output: An iterable of strings.

Разделите строку на пары из двух символов. Если строка содержит нечетное количество символов,
пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').

Входные данные: Строка.
Входные данные: An iterable of strings.
'''
import re

def split_pairs(a):
    b, c = [], re.findall(r'\w{2}', a)
    if a == b: return a
    for i in c:
        b.append(i)
    if a != ''.join(c):
        b.append(a[-1] + '_')
    return b


#  auto-testing
print(split_pairs('abcd')) #== ['ab', 'cd']
print(split_pairs('abc')) #== ['ab', 'c_']
print(split_pairs('abcdf')) #== ['ab', 'cd', 'f_']
print(split_pairs('a')) #== ['a_']
print(split_pairs('')) #== []
