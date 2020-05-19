'''
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.

В данной строке вы должны поменять местами каждое слово, но слова должны оставаться на своих местах.

Вход: строка.
Выход: строка.
'''
# Без модуля re
def backward_string_by_word2(text: str) -> str:
    result, list = text.split(' '), []
    for i in result:
        list.append(i[::-1])
    return ' '.join(list)

#best
def backward_string_by_word(text: str) -> str:
    for i in text.split():
        text = text.replace(i,i[::-1])
    return text

#tests
print(backward_string_by_word('')) #== ''
print(backward_string_by_word('world')) #== 'dlrow'
print(backward_string_by_word('hello world')) #== 'olleh dlrow'
print(backward_string_by_word('hello   world')) #== 'olleh   dlrow'
print(backward_string_by_word('welcome to a game')) #== 'emoclew ot a emag'

print('-' * 20)
# Метод reversed()
string = 'welcome to a game'
string = ''.join(reversed(string))
print(string)