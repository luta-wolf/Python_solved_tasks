'''
"For centuries, left-handers have suffered unfair discrimination in a world designed for right-handers."
Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
"Most humans (say 70 percent to 95 percent) are right-handed, a minority (say 5 percent to 30 percent)
are left-handed, and an indeterminate number of people are probably best described as ambidextrous."
Scientific American. www.scientificamerican.com

One of the robots is charged with a simple task: to join a sequence of strings into one sentence to
produce instructions on how to get around the ship. But this robot is left-handed and has a tendency
to joke around and confuse its right-handed friends.
You are given a sequence of strings. You should join these strings into a chunk of text where the
initial strings are separated by commas. As a joke on the right handed robots, you should replace
all cases of the words "right" with the word "left", even if it's a part of another word. All strings
are given in lowercase.

Input: A sequence of strings.
Output: The text as a comma-separated string.

"На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей."
Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
"Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и неопределеное число людей
вероятно лучше всего охарактеризовать, как "симметричные"."
Scientific American. www.scientificamerican.com

Один робот был занят простой задачей: объединить последовательность строк в одно выражение
для создания инструкции по обходу корабля. Но робот был левша и зачастую шутил и запутывал
своих друзей правшей.
Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив
изначальные строки запятыми. В качестве шутки над праворукими роботами, вы должны заменить
все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки
даны в нижнем регистре.

Входные данные: Последовательность строк.
Выходные данные: Текст, как строка.
'''
def left_join(words):
    left = ','.join(words)
    left = left.replace("right", "left")
    return left

#tests
print(left_join(('left', 'right', 'left', 'stop')))
print(left_join(("bright aright", "ok")))
print(left_join(("brightness wright",)))
print(left_join(("enough", "jokes")))