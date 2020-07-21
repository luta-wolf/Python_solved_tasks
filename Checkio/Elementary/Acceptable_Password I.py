'''
You are the beginning of a password series. Every mission will be based on the previous one.
Going forward the missions will become slightly more complex.
In this mission you need to create a password verification function.
Those are the verification conditions:
the length should be bigger than 6.

Input: A string.
Output: A bool.

Вы - начало серии паролей. Каждая миссия будет основана на предыдущей.
В дальнейшем миссии станут немного сложнее.
В этой миссии вам нужно создать функцию проверки пароля.
Вот условия проверки:
длина должна быть больше 6.

Вход: строка.
Выход: A bool
'''


def is_acceptable_password2(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False


# best
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


# tests
print(is_acceptable_password('short'))  # == False
print(is_acceptable_password('muchlonger'))  # == True
print(is_acceptable_password('ashort'))  # == False
