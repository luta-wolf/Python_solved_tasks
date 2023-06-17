# Экзамен

# task 1
s = 'Python rocks!'
print(len(s))

# task 2
s = 'Python rocks!'
print(s[3:4])

# task 3
s = 'Python rocks!'
print(s[1:5])

# task 4
s = '    Python rocks!     '
print(s.strip())

# task 5
s = 'Python rocks!'
print(s.upper())

# task 6
s = 'Python rocks!'
print(s.replace('o','@'))

# task 7 Каждый третий
s, s2  = input(), ''
for i in range(len(s)):
    if i % 3 == 0:
        s2 = s2 + s[i + 1:i + 3]
print(s2)

# task 8 Замени меня полностью
s = input()
print(s.replace('1', 'one'))

# task 9 Удали меня полностью
s = input()
for i in s:
    if i == '@':
        index = s.find('@')
        s = s[:index] + s[index + 1:]
print(s)

s = input()
res = s.replace("@", "")
print(res)

# task 10 Второе вхождение
# 1
s = input()
if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    f = s.find('f')
    s = s[:f] + '0' + s[f + 1:]
    print(s.find('f'))
# 2
s = input()
if s.count("f") == 0:
    print(-2)
elif s.count("f") == 1:
    print(-1)
else:
    res = s.replace("f", ".", 1).find("f")
    print(res)
# 3
s = input()
if s.count('f') == 0:
	print(-2)
elif s.count('f') == 1:
	print(-1)
else:
    print(s.find('f',s.find('f') + 1))

# task 11 Переворот
# 1
s = input()
a, b = s.find('h'), s.rfind('h')
s2 = s[a + 1:b]
s2 = s[:a + 1] + s2[::-1] + s[b:]
print(s2)
# 2
s=input()
a = s.find('h')
b = s.rfind('h')
print(s[:a] + s[b:a: -1] + s[b:])
