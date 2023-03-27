number = input()
list_1 = []
for i in number:
    if int(i) == 0:
        quit()
    list_1.append(i)
list_1.sort()
list_2 = list_1[::-1]
number_min = ''.join(list_1)
number_max = ''.join(list_2)
print(int(number_max) - int(number_min))
