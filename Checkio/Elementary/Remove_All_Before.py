'''
Not all of the elements are important. What you need to do here is to remove
from the list all of the elements before the given one.
We have two edge cases here: (1) if a cutting element cannot be found, then the list shoudn't
be changed. (2) if the list is empty, then it should remain empty.

Input: List and the border element.
Output: Iterable (tuple, list, iterator ...).

Не все элементы важны. Здесь вам нужно удалить из списка все элементы до указанного.
У нас есть два крайних случая:
(1) если режущий элемент не может быть найден, то список не следует изменять.
(2) если список пуст, то он должен оставаться пустым.

Вход: список и элемент границы.
Выход: Iterable (кортеж, список, итератор ...).
'''

def remove_all_before(items: list, border: int) -> Iterable:
    if items == []:
        return items
    else:
        if border in items:
            for i in range(len(items)):
                if items[0] != border:
                    items.pop(0)
    return items

# auto-testing
print((remove_all_before([1, 2, 3, 4, 5], 3))) #== [3, 4, 5]
print((remove_all_before([1, 1, 2, 2, 3, 3], 2))) #== [2, 2, 3, 3]
print((remove_all_before([1, 1, 2, 4, 2, 3, 4], 2))) #== [2, 4, 2, 3, 4]
print((remove_all_before([1, 1, 5, 6, 7], 2))) #== [1, 1, 5, 6, 7]
print((remove_all_before([], 0))) #== []
print((remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))) #== [7, 7, 7, 7, 7, 7, 7, 7, 7]

from typing import Iterable
def f(ints: Iterable[int]):
    return [str(x) for x in ints]
print(f(range(1, 3)))
