'''
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.

В данной строке вы должны поменять местами каждое слово, но слова должны оставаться на своих местах.

Вход: строка.
Выход: строка.
'''
import re
def backward_string_by_word(text: str) -> str:
    result, list = re.split(r'[ ]', text), []
    for i in result:
        list.append(i[::-1])
    return ' '.join(list)


#tests
print(backward_string_by_word('')) #== ''
print(backward_string_by_word('world')) #== 'dlrow'
print(backward_string_by_word('hello world')) #== 'olleh dlrow'
print(backward_string_by_word('hello   world')) #== 'olleh   dlrow'
print(backward_string_by_word('welcome to a game')) #== 'emoclew ot a emag'

