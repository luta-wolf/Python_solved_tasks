'''
In a given text you need to sum the numbers. Only separated numbers should be counted.
If a number is part of a word it shouldn't be counted.
The text consists from numbers, spaces and english letters

Input: A string.
Output: An int.

В данном тексте вам нужно сложить цифры. Только отдельные числа должны быть подсчитаны.
Если число является частью слова, оно не должно учитываться.
Текст состоит из цифр, пробелов и английских букв

Вход: строка.
Выход: Int.
'''

def sum_numbers(line):
    list = line.split(' ')
    summ = 0
    for i in list:
        if i.isdigit() == True:
            summ += int(i)
    return summ

# tests
print(sum_numbers("hi"),)
print(sum_numbers('who is 1st here'))
print(sum_numbers('my numbers is 2'))
print(sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year'))
print(sum_numbers('5 plus 6 is'))
print(sum_numbers(''))

