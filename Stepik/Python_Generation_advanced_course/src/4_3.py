# task 1 Список по образцу 1
# 1
n = int(input())
lst = []
for i in range(n):
    lst.append([int(i) for i in range(1, n + 1)])
for el in lst:
    print(el)

# 2
n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')

# task 2 Список по образцу 2
# 1
n = int(input())
for i in range(1, n + 1):
    print([el for el in range(1 , i + 1)])

# 2
n = int(input())
result = []

for i in range(1, n + 1):
    result.append(list(range(1, i + 1)))

print(*result, sep='\n')

# task 3 Треугольник Паскаля 1 🌶️
def pascal(n):
    lst = [[1]]
    s = ''
#    for el in range(n):
#        if el == 0:
#            lst2 = [1]
#            lst.append(lst2)
 #       for i in range(el - 1):
  #          s += '1' + lst[el][i] + lst[el][i + 1] + '1'
#    print(lst)
#    print(s)





n = int(input())
pascal(n)
