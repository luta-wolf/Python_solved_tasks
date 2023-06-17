# Тема урока: строковый тип данных

# task 1
print('"Python is a great language!", said Fred.' + ' "I don' + "'" + 't ever remember having this much fun before."')

# task 2 What's Your Name?
name, surname = input(), input()
print('Hello', name, surname + '! You just delved into Python')

# task 3 Футбольная команда
team = input()
print(f'Футбольная команда {team} имеет длину {len(team)} символов')

# task 4 Три города
t1, t2, t3 = [input() for _ in range(3)]
l1, l2, l3 = len(t1), len(t2), len(t3)
if l1 == min(len(t1), len(t2), len(t3)):
    print(t1)
elif l2 == min(len(t1), len(t2), len(t3)):
    print(t2)
elif l3 == min(len(t1), len(t2), len(t3)):
    print(t3)
if l1 == max(len(t1), len(t2), len(t3)):
    print(t1)
elif l2 == max(len(t1), len(t2), len(t3)):
    print(t2)
elif l3 == max(len(t1), len(t2), len(t3)):
    print(t3)


t1, t2, t3 = [input() for _ in range(3)]
print(min(t1, t2, t3, key=len))
print(max(t1, t2, t3, key=len))

# task 5 Арифметические строки
l1, l2, l3 = [len(input()) for _ in range(3)]
if max(abs(l1 - l2), abs(l2 - l3), abs(l3 - l1)) == 2 * min(abs(l1 - l2), abs(l2 - l3), abs(l3 - l1)):
    print('YES')
else:
    print('NO')

# task 6 Цвет настроения синий
line = input()
print('YES' if 'синий' in line else 'NO')

# task 7 Отдыхаем ли?
line = input()
print('YES' if 'суббота' in line or 'воскресенье' in line else 'NO')

# task 8 Корректный email
line = input()
print('YES' if '@' in line and '.' in line else 'NO')
