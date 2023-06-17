# Тема урока: строковые методы

# task 1
s = input().split()
print(*s, sep='\n')

# task 2 Инициалы
# 1
s, lst = input().split(), []
for i in s:
    lst.append(i[0])
print('.'.join(lst) + '.')
# 2
s = input().split()
print(f'{s[0][0]}.{s[1][0]}.{s[2][0]}.')

# task 3 Windows OS
s = input().split('\\')
print(*s, sep='\n')

# task 4 Windows OS
s = input().split()
for i in s:
    print(int(i) * '+')

# task 5 Корректный ip-адрес
# 1
s = input().split('.')
flag = 0
for el in s:
    if  int(el) < 0 or int(el) > 255:
        flag = 1
        break
print('НЕТ' if flag else 'ДА')
# 2
s = input().split('.')
for el in s:
    if int(el) >= 255:
        print('НЕТ')
        break
else:
    print('ДА')

# task 6 Добавь разделитель
# 1
s, spr, lst, string = input().split(), input(), [], ''
for el in s:
    lst.extend(el)
    lst.append(' ')
del lst[-1]
for i in range(len(lst)):
    if lst[i] != ' ':
        string += lst[i] + spr
    else:
        string += ' ' + spr
print(string[:-len(spr)])
# 2
s, spr, string = input().split(), input(), ''
for i in s:
    string += spr + spr.join(i) + spr + ' '
print(string[len(spr):-len(spr) -1])
# 3
s, spr = input(), input()
print(spr.join(s))

# task 7 Количество совпадающих пар
s, cnt = input().split(), 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            cnt += 1
print(cnt)
