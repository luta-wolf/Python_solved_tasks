# task 1 На easy
a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a**10 + b**10)**0.5)

# task 2 Индекс массы тела
mass, rost = float(input()), float(input())
imt = mass / rost**2
if imt > 25:
    print('Избыточная масса')
elif imt < 18.5:
    print('Недостаточная масса')
else:
    print('Оптимальная масса')

# task 3 Стоимость строки
s = input()
summ = len(s) * 0.6
print(f'{int(summ)} р. {int(round(summ % 1 * 100, 0))} коп.')


# task 4 Количество слов
s = input().split()
print(len(s))

# task 5 Зодиак
year = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
n = int(input())

print(year[(n - 2000) % 12])

# task 6 Переворот числа
# 1
n = int(input())
bb = str(n)
s = ''
if len(str(n)) == 6:
    s += str(n // 10**5)
    n %= 10**5
while n > 0:
    if s == '' and n % 10 == 0:
        n //= 10
        continue
    else:
        s += str(n % 10)
    n //= 10
if bb[1] == '0' and len(bb) == 6:
    print(s + str(0))
else:
    print(s)

# 2
n = input()
new_n = int(n[:-5] + n[-5:][::-1])

print(new_n)

# task 7 Standard American Convention
#1
n, s, count  = input()[::-1], '', -1
for el in str(n):
    count += 1
    if count % 3 == 0:
        s += ','
    s += el
print(s[::-1][:-1])
#2
num = int(input())
print(f'{num:,}')

# task 8 Задача Иосифа Флавия 🌶️🌶️
# 1
def one_lst(lst, k):
	while len(lst) > 1:
		lst2 = lst * k                  # создаем запас длины списка
		el = lst2[k - 1]                # находим элемент для удаления
		first_index = lst2.index(el)    # находим 1-й индекс
		second_index = lst2[first_index + 1:].index(el) + first_index   # находим 2-й индекс
		lst = lst2[first_index + 1:second_index + 1]                    # записываем в lst все что между 1 и 2 индексом
	return lst

n, k = int(input()), int(input())
lst = [i for i in range(1, n + 1)]
while len(lst) > k - 1:
    del lst[k - 1]
    lst = lst[k - 1:] + lst[:k - 1]
    if len(lst) <= k - 1:
        lst = one_lst(lst, k)
        break
if k == 1:
    print(n)
else:
    print(*lst)

# 2
n = int(input())
k = int(input())

res = 0
for i in range(1, n+1):
    res = (res + k) % i
print(res + 1)
# 3
n = int(input())
k = int(input())

#Создание массива номеров, из которого потом будем выкидывать элементы.
line = [i for i in range(1, n+1)]

# Нам нужно отсчитать k элементов по массиву из n первых натуральных чисел. Затем выкинуть
# элемент, на котором будет остановлен счет и сдвинуть весь массив так, чтобы первым стал
# следующий после выкинутого, а те элементы, что были до него, перешли в конец. А дальше
# все просто повторяется, пока в массиве не останется один элемент - это и будет искомый номер
# Для этого сначала берем остаток от деления k на длину массива (не просто k - потому что k
# может быть больше длины массива). Если он больше 0, то выкидываем элемент массива с номером,
# равным этому остатку, уменьшенному на единицу (нумерация от нуля), если же он равен нулю,
# то это означает, что надо просто выкинуть последний элемент, а массив никуда не сдвигать.
# Оставшийся в результате массив из одного элемента и дает нужный номер.

while(len(line) > 1):
    num = k % len(line)
    if num > 0:
        pos = num - 1
        line.pop(pos)
        line = line[pos:] + line[:pos]
    else:
        line.pop(-1)

print(line[0])
