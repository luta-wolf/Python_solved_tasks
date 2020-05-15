'''
In a given text you need to sum the numbers. Only separated numbers should be counted.
If a number is part of a word it shouldn't be counted.

The text consists from numbers, spaces and english letters

Input: A string.
Output: An int.
'''

def sum_numbers(line):
    list = line.split(' ')
    summ = 0
    for i in list:
        if i.isdigit() == True:
            summ += int(i)
    return summ

# tests
sum_numbers("hi")
sum_numbers('who is 1st here')
sum_numbers('my numbers is 2')
sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')
sum_numbers('5 plus 6 is')
sum_numbers('')

