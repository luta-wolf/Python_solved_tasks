# num = int(input())
# d = {}
# lst = []
# for i in range(num):
#     a, b = input().split()
#     d[a] = int(b)
#     lst.append(int(b))
# match = input()
# print(d)
# print(lst)
d = {'ZENIT': 65, 'SOCHI': 56, 'DINAMO': 53, 'CSKA': 50, 'KRASNODAR': 49, 'LOKOMOTIV': 48, 'AKHMAT': 41}
lst = [65, 56, 53, 50, 49, 48, 41]
match = 'KRASNODAR-AKHMAT'
match = match[:match.find("-")]
print(match, d[match])
new_num = d[match] + 3
lst.append(new_num)
lst.sort()
lst.reverse()
print(lst)
