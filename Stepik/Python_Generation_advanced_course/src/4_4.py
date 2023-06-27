def chunked(s, n):
    s = ''.join(s)
    lst, tmp, cnt = [], [], 0
    for i in range(len(s)):
        cnt += 1
        tmp.append(s[i])
        if cnt % n == 0:
            lst.append(tmp)
            tmp = []
    cnt = 0
    for el in lst:
        cnt += len(el)
    if cnt != len(s):
        lst.append(tmp)
    return lst

s, n = input().split(), int(input())
print(chunked(s, n))
