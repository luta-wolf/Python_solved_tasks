num = int(input())
lst = []
for i in range(num):
    lst.append(list(map(int, input().split())))

# num = 10
# lst = [(0, 0), (1, 1), (0, 2), (5, 0), (5, 2), (0, 4), (3, 0), (3, 4), (5, 0), (5, 4)]

max_s = 0
for i in range(num):
    rect = {'first': (lst[i])}
    first_corner = False
    second_corner = False
    for j in range(i + 1, num):
        if lst[i][0] == lst[j][0] and not first_corner:
            rect['second'] = (lst[j])
            first_corner = True
        if lst[i][1] == lst[j][1] and not second_corner:
            rect['third'] = (lst[j])
            second_corner = True
        if first_corner and second_corner:
            if rect['second'][1] == lst[j][1] and rect['third'][0] == lst[j][0]:
                rect['forth'] = lst[j]
                print(rect)
                current_max = (lst[j][0] - rect['first'][0]) * (lst[j][1] - rect['first'][1])
                print(current_max)
                if current_max > max_s:
                    max_s = current_max
                rect = {'first': rect['first']}
                first_corner = False
                second_corner = False
    rect = {}
    first_corner = False
    second_corner = False

print(max_s)
