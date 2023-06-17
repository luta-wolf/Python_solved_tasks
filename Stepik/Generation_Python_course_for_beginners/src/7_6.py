# Тема урока: break, continue, else

# task 1 Наименьший делитель
n = int(input())
i = 2
while i >= n:
    if n % i == 0:
        break
    i += 1
print(i)


n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break

n, div = int(input()), 2
while n % div:
    div += 1
print(div)

# task 2 Следуй правилам
n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
