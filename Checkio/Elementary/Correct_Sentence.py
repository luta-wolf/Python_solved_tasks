'''
For the input of your function, you will be given one sentence.
You have to return a corrected version, that starts with a capital letter
and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary.
If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string.
Output: A string.

На вход Вашей функции будет передано одно предложение. Необходимо вернуть его
исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
Обратите внимание на то, что не все исправления необходимы. Если предложение уже
заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой

Входные аргументы: Строка (A string).
Выходные аргументы: Строка (A string).
'''


def correct_sentence(text: str) -> str:
    text = text.split()
    text[0] = text[0].capitalize()
    text = ' '.join(text)
    if text[-1] != '.': text = text + '.'
    return text




# auto-testing
print(correct_sentence("greetings, friends")) #== "Greetings, friends."
print(correct_sentence("Greetings, friends")) #== "Greetings, friends."
print(correct_sentence("Greetings, friends.")) #== "Greetings, friends."
print(correct_sentence("hi")) #== "Hi."
print(correct_sentence("welcome to New York")) #== "Welcome to New York."