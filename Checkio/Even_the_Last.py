'''

You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the array together.
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero).

Input: A list of integers.
Output: The number as an integer.

Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
затем перемножить эту сумму и последний элемент исходного массива.
Не забудьте, что первый элемент массива имеет индекс 0.
Для пустого массива результат всегда 0 (ноль).

Входные данные: Список (list) целых чисел (int).
Выходные данные: Число как целочисленное (int).
'''
def checkio(list):
    summ = 0
    if list != []:
        for i in range(0, len(list), 2):
            summ += list[i]
        return summ * list[-1]
    else:
        return 0

#test
print(checkio([0, 1, 2, 3, 4, 5]))
print(checkio([1, 3, 5]))
print(checkio([6]))
print(checkio([]))
