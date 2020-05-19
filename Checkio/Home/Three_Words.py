'''
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.

Давайте научим наших роботов отличать слова от чисел.
Дана строка со словами и числами, разделенными пробелами
(один пробел между словами и/или числами). Слова состоят только из букв.
Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера,
в строке "start 5 one two three 7 end" есть три слова подряд.

Входные данные: Строка со словами (str).
Выходные данные: Ответ как логическое выражение (bool), True или False.
'''
def checkio(line):
    list = line.split()
    k = 0
    for i in list:
        if i.isalpha() == True:
            k += 1
        else:
            k = 0
        if k >= 3: return True
    else:
        return False

#tests
print(checkio("Hello World hello"))
print(checkio("He is 123 man"))
print(checkio("1 2 3 4"))
print(checkio("bla bla bla bla"))
print(checkio("Hi"))
print(checkio('one two 3 four five six 7 eight 9 ten eleven 12'))