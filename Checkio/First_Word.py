'''
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:
There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.

Input: A string.
Output: A string.

Дана строка и нужно найти ее первое слово.
При решении задачи обратите внимание на следующие моменты:
- В строке могут встречатся точки и запятые
- Строка может начинаться с буквы или, к примеру, с пробела или точки
- В слове может быть апостроф и он является частью слова
- Весь текст может быть представлен только одним словом и все

Входные параметры: Строка.
Выходные параметры: Строка.
'''
def first_word(line):
    line = line.split()
    for i in line:
        if i.isalpha() == True:
            return i
            break


#tests
print(first_word("Hello world")) # == "Hello"
print(first_word(" a word ")) # == "a"
print(first_word("don't touch it")) # == "don't"
print(first_word("greetings, friends")) # == "greetings"
print(first_word("hi")) # == "hi"
print(first_word("Hello.World")) # == "Hello"