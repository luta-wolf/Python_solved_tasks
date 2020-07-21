'''
You should return a given string in reverse order.

Input: A string.
Output: A string.

Вы должны вернуть данную строку в обратном порядке.

Вход: строка.
Выход: строка.
'''


# best
def backward_string(val: str) -> str:
    """
    returns the string in reverse order
    :param val:
    :return:
    """
    return val[::-1]


def backward_string2(val: str) -> str:
    return val.replace(val, val[::-1])


def backward_string3(val: str) -> str:
    return ''.join(reversed(val))


# auto-testing
print(backward_string('val'))  # == 'lav'
print(backward_string(''))  # == ''
print(backward_string('ohho'))  # == 'ohho'
print(backward_string('123456789'))  # == '987654321'
