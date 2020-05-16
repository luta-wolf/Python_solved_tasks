'''
How old are you in a number of days? It's easy to calculate - just subtract your birthday
from today. We could make this a real challenge though and count the difference between any dates.
You are given two dates as an array with three numbers - a year, month and day.
For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days
between the given dates. For example between today and tomorrow = 1 day. The difference
will always be either a positive number or zero, so don't forget about the absolute value.

Input: Two dates as tuples of integers.
Output: The difference between the dates in days as an integer.

Сколько вам лет в днях? Это легко вычислить - достаточно вычесть свой день рождения от
сегодняшнего дня. Мы имеем реальную задачу - посчитать разницу между любыми датами.
У вас есть две даты в кортежах с тремя числами - год, месяц и день. Например,
19 апреля 1982 будет (1982, 4, 19). Вы должны найти разницу в днях между имеющимися датами.
Например, между сегодня и вчера = 1 день. Разница между днями всегда будет положительной
или нулем, не забывайте про абсолютное значение.

Входные данные: Две даты, как кортежи целых чисел.
Выходные данные: Разница между датами в днях, как целое число.
'''
import datetime
a, b = (2014, 8, 27), (2014, 1, 1)
diff = (a[0] - b[0]) * 365 + (a[1] - b[1]) * 30 + (a[2] - b[2])
print(diff)

# def days_diff(a, b):
#     pass

print(dir(datetime))

#tests
# days_diff((1982, 4, 19), (1982, 4, 22)) == 3
# days_diff((2014, 1, 1), (2014, 8, 27)) == 238
# days_diff((2014, 8, 27), (2014, 1, 1)) == 238