# Тема урока: цикл while

# task 1 Обратный порядок 1
n = int(input())
while n != 0:
    print(n % 10)
    n = n // 10

# task 2 Обратный порядок 2
n = int(input())
while n != 0:
    print(n % 10, end='')
    n = n // 10

# task 3 max и min
n, maxn, minn = int(input()), 0, 10
while n != 0:
    if n % 10 > maxn:
        maxn = n % 10
    if n % 10 < minn:
        minn = n % 10
    n = n // 10
print('Максимальная цифра равна', maxn)
print('Минимальная цифра равна', minn)

# task 4 Все вместе
n, total, count, res = int(input()), 0, 0, 1
first_digit = (n // 10**(len(str(n)) -1)) % 10
summ_last_first_digit = first_digit + n % 10
while n != 0:
    last_digit = n % 10
    total += last_digit
    count += 1
    res *= last_digit
    n = n // 10
print(total, count, res, total / count, first_digit, summ_last_first_digit, sep='\n')

# task 5 Вторая цифра
n = int(input())
print((n // 10**(len(str(n)) -2)) % 10)

# task 6 Одинаковые цифры
n, flag = int(input()), True
ld = n % 10
while n != 0:
    last = n % 10
    if ld != last:
        flag = False
    n = n // 10
print('YES' if flag else 'NO')

# task 7 Упорядоченные цифры 🌶️
n, flag, ld = int(input()), True, 0
while n != 0:
    last = n % 10
    if last >= ld:
        ld = last
    else:
        flag = False
    n = n // 10
print('YES' if flag else 'NO')
