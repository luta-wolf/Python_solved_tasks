# Тема урока: строки - Поиск и замена

# task 1 Количество слов
s = input()
print(s.count(' ') + 1)

# task 2 Минутка генетики
s = input()
print('Аденин:', s.upper().count('А'))
print('Гуанин:', s.upper().count('Г'))
print('Цитозин:', s.upper().count('Ц'))
print('Тимин:', s.upper().count('Т'))

s = input().lower()
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))

# task 3 Очень странные дела
n, cnt = int(input()), 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        cnt +=1
print(cnt)

# task 4 Количество цифр
s, cnt = input(), 0
for i in s:
    if i in '0123456789':
        cnt += 1
print(cnt)

s = input()
print(s.count('0') +
      s.count('1') +
      s.count('2') +
      s.count('3') +
      s.count('4') +
      s.count('5') +
      s.count('6') +
      s.count('7') +
      s.count('8') +
      s.count('9'))

s, cnt = input(), 0
for i in range(10):
    cnt += s.count(str(i))
print(cnt)

# task 5 .com or .ru
s = input()
print('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')

s = input()
print('YES' if s.endswith(('.com','.ru')) else 'NO')

# task 6 Самый частотный символ
# 1
s, max_c, c = input(), 0, ''
template = 'aeioubcdfghjklmnpqrstvwxyzAEIOUBCDFGHJKLMNPQRSTVWXYZ0123456789абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
for i in template:
    cnt = s.count(i)
    if cnt >= max_c:
        max_c = cnt
        c = i
print(c)
# 2
s, cnt, liter = input(), 0, 0
for i in s:
    if s.count(i) >= cnt:
        cnt = s.count(i)
        liter = i
print(liter)
# 3
a = input()[::-1]
z = max(a, key = a.count)
print(z)
# 4
from collections import Counter

s = input()[::-1]
print(Counter(s).most_common(1)[0][0])

# task 7 Первое и последнее вхождение
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')

# task 8 Удаление фрагмента
s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])
