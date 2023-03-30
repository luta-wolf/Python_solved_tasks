d = {'ZENIT': 65, 'SOCHI': 56, 'DINAMO': 53, 'CSKA': 50, 'KRASNODAR': 49, 'LOKOMOTIV': 48, 'AKHMAT': 41}
lst = [65, 56, 53, 50, 49, 48, 41]
match = 'KRASNODAR-AKHMAT'

def print_index(const_lst: list, num: int) -> None:
    lst = const_lst[:]
    lst.append(num)
    lst.sort()
    print(len(lst) - lst.index(num), end=' ')


# num = int(input())
# if  num < 2 or num > 20:
#     quit()
# d = {}
# lst = []
# for i in range(num):
#     a, b = input().split()
#     if len(a) < 3 or len(a) > 12:
#         quit()
#     d[a.upper()] = int(b)
#     lst.append(int(b))
# match = input().upper()
team1 = match[:match.find("-")]
team2 = match[match.find("-") + 1 :]
print(team1, team2)
lst2 = lst[:]
lst2.remove(d[team1])
print_index(lst2, d[team1] + 3)
print_index(lst2, d[team1] + 1)
print(lst.index(d[team1]) + 1)
