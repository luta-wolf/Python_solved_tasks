# task 1 Координатные четверти
n = int(input())
ch1, ch2, ch3, ch4 = 0, 0, 0, 0
for i in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    if x > 0 and y > 0:
        ch1 += 1
    elif x < 0 and y > 0:
        ch2 += 1
    elif x < 0 and y < 0:
        ch3 += 1
    elif x > 0 and y < 0:
        ch4 += 1
print(f'Первая четверть: {ch1}')
print(f'Вторая четверть: {ch2}')
print(f'Третья четверть: {ch3}')
print(f'Четвертая четверть: {ch4}')

# task 2 Больше предыдущего
lst, cnt = [int(el) for el in input().split()], 0
for i in range(1, len(lst)):
    if lst[i - 1] < lst[i]:
        cnt += 1
print(cnt)

# task 3 Назад, вперёд и наоборот
# 1
lst = [int(el) for el in input().split()]
if len(lst) % 2 != 0:
    lst2 = lst[:-1]
else:
    lst2 = lst
for i in range(0, len(lst2), 2):
    lst2[i], lst2[i+1] = lst2[i+1], lst2[i]
if len(lst) % 2 != 0:
    lst2.append(lst[-1])
print(*lst2)

# 2
numbers = input().split()
for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(*numbers)
# 2
s = list(map(int, input().split()))
s[:-1:2], s[1::2] = s[1::2], s[:-1:2]
print(*s)

# task 4 Сдвиг в развитии
# 1
n = input().split()
lst = []
lst.append(n[-1])
lst.extend(n[:-1])
print(*lst)
# 2
seq = input().split()
new_seq = [seq[-1]] + seq[:-1]
print(*new_seq)
# 3
n=input().split()
print(n.pop(), *n)

# task 5 Различные элементы
lst = [int(el) for el in input().split()]
print(len(set(lst)))

# task 6 Произведение чисел
# 1
lst = [int(input()) for el in range(int(input()))]
n = int(input())
flag = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] * lst[j] == n:
            flag = 1
            break

print('ДА' if flag else 'НЕТ')
# 2
size = int(input())
seq = [int(input()) for _ in range(size)]
number = int(input())
flag = False

for i in range(size):
    for j in range(size):
        if i != j and seq[i] * seq[j] == number:
            flag = True
print('ДА' if flag else 'НЕТ')

# task 7  Камень, ножницы, бумага
s1, s2 = input(), input()
if s1 == s2:
    print('ничья')
elif s1 == 'камень' and s2 == 'ножницы' or s1 == 'ножницы' and s2 == 'бумага' or s1 == 'бумага' and s2 == 'камень':
    print('Тимур')
else:
    print('Руслан')

# task 8  Камень, ножницы, бумага, ящерица, Спок 🌶️
# 1
lst = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']
s1, s2 = input(), input()
index1, index2 = lst.index(s1), lst.index(s2)
if abs(index1 - index2) == 0:
    print('ничья')
elif abs(index1 - index2) % 2 == 0:
    if max(index1, index2) == index1:
        print('Тимур')
    else:
        print('Руслан')
elif abs(index1 - index2) % 2 != 0:
        if min(index1, index2) == index1:
            print('Тимур')
        else:
            print('Руслан')
# 2
g = ('ножницы', 'бумага', 'камень', 'ящерица', 'Спок')
dist = (g.index(input()) - g.index(input())) % len(g)
print(('ничья', 'Тимур', 'Руслан')[dist and dist % 2 + 1])
# 3
a = 'ножницыбумагакаменьящерицаСпокножницыящерицабумагаСпоккаменьножницы'
t, r = input(), input()
if t == r:
  print('ничья')
elif t + r in a:
  print('Тимур')
else:
  print('Руслан')

# task 9  Орел и решка
# 1
s = input()
cnt_max_p, cnt = 1, 1
for i in range(len(s) - 1):
    if s[i] == 'Р' and  s[i + 1] == 'Р':
        cnt += 1
    else:
        cnt = 1
    if cnt > cnt_max_p:
        cnt_max_p = cnt
print(cnt_max_p if 'Р' in s else 0)
# 2
s = input().split('О')
print(len(max(s)))
# 3
s = input()
count, m = 0, 0
for i in s:
    if i == 'Р':
        count += 1
        if count > m:
            m = count
    elif i != 'Р':
        count = 0
print(m)

# task 10  Кремниевая долина 🌶️🌶️
# 1
n = int(input())
lst = [input() for el in range(n)]
tamplate = 'anton'
lst2 = []
lst_finish = []
for el in lst:
    for el2 in el:
        if el2 in tamplate:
            if el2 == 'a' and len(lst2) == 0 or el2 == 'n' and (len(lst2) == 1 or len(lst2) == 4) or el2 == 't' and len(lst2) == 2 or el2 == 'o' and len(lst2) == 3:
                lst2.append(el2)
    if ''.join(lst2) == tamplate:
        lst_finish.append(lst.index(el) + 1)
    lst2 = []
print(*lst_finish)
# 2
for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break

# task 11  Роскомнадзор запретил букву а 🌶️🌶️
# 1
word = input() + ' запретил букву  '
template = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(template)):
    word = word[:-1] + template[i]
    if template[i] in word[:-1]:
        word = ' '.join(word.split())
        print(word.lstrip())
        word = word.replace(template[i], '') + template[i]
# 2
word = input() + ' запретил букву  '
template = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for i in range(len(template)):
    word = word[:-1] + template[i]
    if template[i] in word[:-1]:
        print(word.strip())
        word = word.replace(template[i], '').replace('  ', ' ') + template[i]
