# text: Маше 19 Васе 30 им49
a = input('Ведите текст: ')
l = []
sum = 0
k = 0
for i in a:
    k += 1
    if i != ' ':
        l.append(i)
        print(i, end='')
    else:
        print()
        l.append(' ')
print()

print(k)
print(l)


