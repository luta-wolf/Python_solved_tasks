'''
In a given list the first element should become the last one.
An empty list or list with only one element should stay the same.

Input: List.
Output: Iterable.

В данном списке первый элемент должен стать последним.
Пустой список или список только с одним элементом должен остаться прежним.

Вход: список.
Выход: итерируемый.
'''

from typing import Iterable


def replace_first(items: list) -> Iterable:
    if len(items) == 1 or items == []:
        return items
    items.append(items[0])
    items.pop(0)
    return items

#best
def replace_first2(items: list) -> list:
    return items[1:] + items[:1]

#  auto-testing
print(list(replace_first([1, 2, 3, 4]))) #== [2, 3, 4, 1]
print(list(replace_first([1]))) #== [1]
print(list(replace_first([]))) #== []