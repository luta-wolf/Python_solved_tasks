num: int = int(input())
lst: list[int] = list(map(int, input().split()))

max_num = max(lst)
min_num = min(lst)
min_i = lst.index(min_num)
max_i = len(lst) - list(reversed(lst)).index(max_num) - 1
print(max_i + 1, min_i + 1)
