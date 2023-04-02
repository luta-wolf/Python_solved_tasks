num: int = int(input())
lst: list[str] = input().split()
lst: list[int] = list(map(lambda x: int(x), lst))
max_num: int = lst[0]
max_i: int = 0
min_num: int = lst[0]
min_i: int = 0
for i in range(num):
    if lst[i] >= max_num:
        max_i = i
    if lst[i] < min_num:
        min_i = i
print(max_i + 1, min_i + 1)
