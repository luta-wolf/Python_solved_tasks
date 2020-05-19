'''
Your mission here is to create a function that gets a tuple and returns a tuple
with 3 elements - the first, third and second element from the last for the given array.

Input: A tuple, at least 3 elements long.
Output: A tuple.

Ваше задание здесь создать функцию, которая получает массив(tuple)
и возвращает набор с 3 элементами - первым, третьим, вторым с конца.

Входные данные: Набор длинной не менее 3 элементов.
Выходные данные: Набор элементов.
'''

def easy_unpack(elements: tuple) -> tuple:
    return (elements[0],elements[2],elements[-2])

#tests
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))) #== (1, 3, 7)
print(easy_unpack((1, 1, 1, 1))) #== (1, 1, 1)
print(easy_unpack((6, 3, 7))) #== (6, 7, 3)