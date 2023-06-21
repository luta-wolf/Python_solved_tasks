# Тема урока: функции с возвратом значения

def quick_merge(list1, list2):
	p1, p2, total = 0, 0, []

	while p1 < len(list1) and p2 < len(list2):
		if list1[p1] <= list2[p2]:
			total.append(list1[p1])
			p1 += 1
		else:
			total.append(list2[p2])
			p2 += 1

	if p1 < len(list1):
		total += list1[p1:]
	else:
		total += list2[p2:]

	return total

l1 = [1, 10, 15, 18, 21, 56, 89, 100, 678]
l2 = [2, 3, 5, 8, 10, 23, 67, 89]
print(quick_merge(l1, l2), len(quick_merge(l1, l2)))


# task 1 Is Valid Triangle?
# 1
# объявление функции
def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return False

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
# 2
# объявление функции
def is_valid_triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])  # создаём отсортированный список из сторон

    return sides[0] + sides[1] > sides[2]  # проверяем, минимальная и средняя стороны больше максимальной


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))

# task 2 Is a Number Prime? 🌶️
# 1
# объявление функции
def is_prime(num):
    cnt = 0
    for i in range(1, n + 1):
        if num % i == 0:
            cnt += 1
    return True if cnt == 2 else False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

# 2
# объявление функции
def is_prime(num):
    return len([el for el in range(1, n + 1) if n % el == 0]) == 2

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

# task 3 Next Prime 🌶️🌶️
# 1
# объявление функции
def get_next_prime(num):
    for i in range(num + 1, 200):
        if len([el for el in range(1, i + 1) if i % el == 0]) == 2:
            return i

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

# 2
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# объявление функции
def get_next_prime(num):
    cnt = num + 1
    while not is_prime(cnt):
        cnt +=1
    return cnt

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

# task 4 Good password 🌶️
# 1
def is_password_good(password):
    cnt = 0
    if len(password) >= 8:
        cnt += 1
    for i in password:
        if i in '0123456789':
            cnt += 1
            break
    for i in password:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            cnt += 1
            break
    for i in password:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            cnt += 1
            break
    return True if cnt == 4 else False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

# 2
def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

# 3
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])


txt = input()
print(is_password_good(txt))

# task 5 Ровно в одном
# 1
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        return True if cnt == 1 else False
    return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

# 2
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        return cnt == 1
    return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))

# task 6 Палиндром 🌶️
# 1
def is_palindrome(text):
    text = text.lower().replace(' ','').replace(',','').replace('.','').replace('!','').replace('?','').replace('-','')
    return True if text == text[::-1] else False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# 2
def is_palindrome(text):
    sep = [' ',',','.','!','?','-']
    for i in sep:
        text = text.replace(i, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# 3
def is_palindrome(text):
    text = [el.lower() for el in text if el not in ' .,!?-']
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# 4
def is_palindrome(text):
    l = [i.lower() for i in text if i.isalpha()]
    return l == l[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

# task 7 BEEGEEK
# объявление функции
def is_valid_password(password):
    cnt = 0
    lst = password.split(':')
    if len(lst) == 3:
        if lst[0] == lst[0][::-1]:
            cnt += 1
        if len([el for el in range(2, int(lst[1])) if int(lst[1]) % el == 0]) == 0:
            cnt += 1
        if int(lst[2]) % 2 == 0:
            cnt += 1
    return cnt == 3


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

# task 8 Правильная скобочная последовательность 🌶️
# 1
def is_correct_bracket(text):
    lst = []
    for el in text:
        if el == '(':
            lst.append(el)
        elif el == ')' and len(lst) != 0:
            del lst[-1]
        else:
            return False
    return lst == []

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

# 2
def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")

    return text == ""


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))

# task 9 Змеиный регистр
# 1
def convert_to_python_case(text):
    lst = []
    a, b = 0, 0
    for i in range(len(text)):
        if text[i].isupper():
            b = i
            lst.append(text[a:b])
            a = b
    lst.append(text[b:len(text)])
    return '_'.join(lst)[1:].lower()


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

# 2
def convert_to_python_case(text):
    new_text = ''
    for el in text:
        if not el == el.lower():
            new_text += '_' + el.lower()
        else:
            new_text += el
    return new_text[1:]

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

# 3
def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]


print(convert_to_python_case(input()))
