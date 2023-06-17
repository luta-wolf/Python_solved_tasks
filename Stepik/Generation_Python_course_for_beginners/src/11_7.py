# Тема урока: списочные выражения (list comprehension)

# task 1
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i[1:] for i in keywords]
print(new_keywords)

# task 2
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(el) for el in keywords]
print(lengths)

# task 3
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [el for el in keywords if len(el) >= 5]

print(new_keywords)

# task 4
# 1
palindromes = [el for el in range(100, 1000) if str(el) == str(el)[::-1]]
print(palindromes)
# 2
palindromes = [i for i in range(100, 1001) if i // 100 == i % 10]
print(palindromes)
# 3
palindromes = [int(a+b+a) for a in '123456789' for b in '0123456789']
print(palindromes)

# task 5 Списочное выражение 1
# 1
print(*[i * i for i in range(1, int(input()) + 1)], sep='\n')
# 2
lines = [a**2 for a in range(1, int(input())+1)]
for i in lines:
    print(i)

# task 6 Списочное выражение 3
lst = [int(el)**3 for el in input().split()]
print(*lst)

# task 7 В одну строку 1
# 1
print(*input().split(), sep='\n')
# 2
print(input().replace(" ","\n"))

# task 8 В одну строку 2
# 1
print(*[el for el in input() if el in '0123456789'], sep='')
# 2
print(*[el for el in input() if el.isdigit()], sep='')

# task 8 В одну строку 3
# 1
s = input().split()
lst = [int(i)**2 for i in s if int(i) % 2 == 0 and int(i)**2 % 10 != 4]
print(lst)

# 2
print(*[int(i)**2 for i in input().split() if int(i) % 2 == 0 and int(i)**2 % 10 != 4])
