# Экзамен

# task 1 Список четных
n = int(input())
print([i for i in range(1, n + 1) if i % 2 == 0])

# task 2 Сумма двух списков
lst1, lst2 = input().split(), input().split()
for i in range(len(lst1)):
    print(int(lst1[i]) + int(lst2[i]), end=' ')

# task 3 Сумма чисел
lst = [int(i) for i in input().split()]
print(*lst,  sep='+', end='=')
print(sum(lst))

# task 4 Валидный номер 🌶️🌶️
# 1
lst = input().split('-')
lst2 =[]
flag = 'YES'
if len(lst) == 4 and len(lst[0]) == 1 and int(lst[0]) == 7 and len(lst[1]) == len(lst[2]) == 3 and len(lst[3]) == 4:
    lst2.extend(lst[1])
    lst2.extend(lst[2])
    lst2.extend(lst[3])
    for el in lst2:
        if not el.isdigit():
            flag = 'NO'
            break
        else:
            flag = 'YES'
elif len(lst) == 3 and len(lst[0]) == len(lst[1]) == 3 and len(lst[2]) == 4:
    lst2.extend(lst[0])
    lst2.extend(lst[1])
    lst2.extend(lst[2])
    for el in lst2:
        if not el.isdigit():
            flag = 'NO'
            break
        else:
            flag = 'YES'
else:
    flag = 'NO'

print(flag)

# 2
s = input()
s1 = s.replace('-','')
if s1.isdigit():
    lst = s.split('-')
    if len(lst) == 4 and int(lst[0]) == 7 and len(lst[1]) == len(lst[2]) == 3 and len(lst[3]) == 4:
        print('YES')
    elif len(lst) == 3 and len(lst[0]) == len(lst[1]) == 3 and len(lst[2]) == 4:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

# 3
seq = input().split("-")
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and "".join(seq).isdigit() and seq[0] == "7":
    print("YES")
elif lens == [3, 3, 4] and "".join(seq).isdigit():
    print("YES")
else:
    print("NO")

# 4
n = input().split('-')
if n[0] == '7':
    del n[0]
if [len(i) for i in n] == [3, 3, 4] and ''.join(n).isdigit():
    print('YES')
else:
    print('NO')


# task 5 Самый длинный
print(max([len(el) for el in input().split()]))

# task 6 Молодежный жаргон
print(*[el[1:] + el[:1] + 'ки' for el in input().split()])
