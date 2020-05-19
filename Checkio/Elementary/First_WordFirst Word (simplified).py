'''
You are given a string where you have to find its first word.
Input string consists of only english letters and spaces.
There aren’t any spaces at the beginning and the end of the string.

Input: A string.
Output: A string.

Дана строка и нужно найти ее первое слово.
- Строка состоит только из английских символов и пробелов.
- В начале и в конце строки пробелов нет.

Входные параметры: Строка.
Выходные параметры: Строка.
'''


def first_word(text: str) -> str:
    return text.split(' ')[0]

#tests
print(first_word("Hello world")) #== "Hello"
print(first_word("a word")) #== "a"
print(first_word("hi")) #== "hi"
