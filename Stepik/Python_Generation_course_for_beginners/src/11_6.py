# Тема урока: методы списков

# task 1 Все сразу 2 🌶️
# 1
numbers = [8, 9, 10, 11]
numbers.pop(1)
numbers.insert(1, 17)
numbers.pop(0)
numbers = numbers * 2
print(numbers)
# 2
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)

# task 2 Переставить min и max
# 1
lst = list(map(int, input().split()))
a, b = max(lst), lst.index(max(lst))
c, d = min(lst), lst.index(min(lst))
lst[b] = c
lst[d] = a
print(*lst)
# 2
a = list(map(int, input().split()))
x = a.index(max(a))
y = a.index(min(a))
a[x], a[y] = a[y], a[x]
print(*a)

# task 3 Количество артиклей
s = input().lower().split()
print('Общее количество артиклей:', s.count('a') + s.count('an') + s.count('the'))

# task 4 Взлом Братства Стали 🌶️
# 1
s, lst, lst2 = input(), [], []
n = int(s[1:])
for _ in range(int(s[1:])):
    lst.append(input())
for el in lst:
    if '#'in el:
        lst2.append(el[:el.index('#')].rstrip())
    else:
        lst2.append(el)
print(*lst2, sep="\n")
# 2
s = input()
for _ in range(int(s[1:])):
    st = input()
    if '#'in st:
        st = st[:st.find("#")].rstrip()
    print(st)

# task 5 Сортировка чисел
lst = list(map(int, input().split()))
lst.sort()
print(*lst)
lst.sort(reverse = True)
print(*lst)
