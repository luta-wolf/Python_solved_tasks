# Тема урока: функции с параметрами

# task 1
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        if i <= base // 2 + 1:
            print(fill * i)
        else:
            print(fill * (base - i + 1))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

# task 2 ФИО
# 1
def print_fio(name, surname, patronymic):
    print(surname.upper()[:1] + name.upper()[:1] + patronymic.upper()[:1])


name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)


# 2
def print_fio(name, surname, patronymic):
     print((surname[0] + name[0] + patronymic[0]).upper())


name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)

# task 3 Сумма цифр
# объявление функции
def print_digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    print(total)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
