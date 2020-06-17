'''
You are given a string and two markers (the initial one and final).
You have to find a substring enclosed between these two markers.
But there are a few important conditions.
This is a simplified version of the Between Markers mission.

The initial and final markers are always different.
The initial and final markers are always 1 char size.
The initial and final markers always exist in a string and go one after another.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.

Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст,
заключенный между двумя этими маркерами. Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers.

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.

Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.
'''

def between_markers(text: str, begin: str, end: str) -> str:
    t = text.index(begin)
    t2 = text.index(end)
    return  text[t+1:t2]



# auto-testing
print(between_markers('What is >apple<', '>', '<')) #== "apple"
print(between_markers('What is [apple]', '[', ']')) #== "apple"
print(between_markers('What is ><', '>', '<')) #== ""
print(between_markers('>apple<', '>', '<')) #== "apple"