# Тема урока: строки - Срезы строк

# task 1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

# task 2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

# task 3
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# task 4
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# task 5 Палиндром
s = input()
print('YES' if s == s[::-1] else 'NO')

# task 6 Делаем срезы 1
s = input()
print(len(s))
print(s * 3)
print(s[:1])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])

# task 7 Делаем срезы 2
s = input()
print(s[2:3])
print(s[-2:-1])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])

# task 8 Две половинки
s = input()
half = int(len(s)/2)
if len(s) % 2 == 0:
    print(s[half:] + s[:half])
else:
    print(s[half + 1:] + s[:half +1])
