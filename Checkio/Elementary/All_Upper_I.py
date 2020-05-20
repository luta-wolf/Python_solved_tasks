'''
Check if a given string has all symbols in upper case.
If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.
Output: a boolean.

Проверьте, содержит ли данная строка все символы в верхнем регистре.
Если строка пуста или в ней нет буквы - функция должна вернуть True.

Вход: строка.
Вывод: логическое значение.
'''
import re

def is_all_upper2(text: str) -> bool:
    if text == None:
        return True
    if ' '.join(re.findall(r'[A-Z\d]+', text)) == text or text.isspace():
        return True
    return False

#best
def is_all_upper(text: str) -> bool:
    return text == text.upper()

#auto-testing
print(is_all_upper('ALL UPPER')) #== True
print(is_all_upper('all lower')) #== False
print(is_all_upper('mixed UPPER and lower')) #== False
print(is_all_upper('')) #== True
print(is_all_upper("     ")) #== True
print(is_all_upper("123"))  #== True

