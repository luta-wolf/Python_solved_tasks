# Тема урока: вывод элементов списка

# task 1
# 1
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
total = 0
for num in numbers:
    total += num**2
print(total)
# 2
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
print(sum([i**2 for i in numbers]))

# task 2 Значение функции
n, lst = int(input()), []
for _ in range(n):
    lst.append(int(input()))
print(*lst, sep='\n')
print()
for i in lst:
    print(i**2 + 2 * i + 1)

# task 3 Remove outliers
n, lst = int(input()), []
for _ in range(n):
    lst.append(int(input()))
lst.remove(max(lst))
lst.remove(min(lst))
print(*lst, sep='\n')

# task 4 Без дубликатов
n, lst = int(input()), []
for _ in range(n):
    word = input()
    if word not in lst:
        lst.append(word)
print(*lst, sep='\n')

# task 5 Google search - 1
n, lst = int(input()), []
for _ in range(n):
    lst.append(input())
key = input().lower()
for string in lst:
    if key in string.lower():
        print(string)

# task 6 Google search - 2 🌶️🌶️
# 1
n, lst = int(input()), []
for _ in range(n):
    lst.append(input())
k, lst2 = int(input()), []
for _ in range(k):
    lst2.append(input())
for s in lst:
    flag = 0
    for key in lst2:
        if key.lower() in s.lower():
            flag += 1
    if flag == len(lst2):
        print(s)
# 2
n = int(input())

strings = []
for _ in range(n):
    s = input()
    strings.append(s)

k = int(input())

search_queries = []
for _ in range(k):
    search_query = input()
    search_queries.append(search_query)

for s in strings:
    for search_query in search_queries:
        if search_query.lower() not in s.lower():
            break
    else:
        print(s)

# task 7 Negatives, Zeros and Positives
# 1
n, lst1, lst2, lst3 = int(input()), [], [], []
for _ in range(n):
    num = int(input())
    if num < 0:
        lst1.append(num)
    elif num == 0:
        lst2.append(num)
    else:
        lst3.append(num)
print(*lst1, *lst2, *lst3, sep='\n')
# 2
n = int(input())
lst = [int(input()) for _ in range(n)]
[print(i) for i in lst if i < 0]
[print(i) for i in lst if i == 0]
[print(i) for i in lst if i > 0]
