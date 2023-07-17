# # a = 1
# # a_id = id(a)
# # a += 1
# # print(id(a) == a_id)


# x = 13
# num = 0 if x > 5 else x == 5
# print(num)


# for i in 'hello world':
# 	if i == 'o':
# 		break
# 	print(i * 2 , end='')
# print()

# for i in range(len('str')):
# 	if i != 2:
# 		print('str'[i], end='-')
# 	else:
# 		print('str'[1])

# print()

# f = lambda a,b : a+b
# print(f(2,3))
# print()

# a = 5
# b = a
# c = [6,7]
# d = c
# a = 6
# c.append(8)
# print(b,d)
# print()

# def print_arr(arr = []):
# 	arr.append(1)
# 	print(arr, end='')
# print_arr()
# print_arr()

def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()  # Сортируем стороны треугольника по возрастанию

    # Проверяем условие Пифагора для прямоугольного треугольника: a^2 + b^2 = c^2
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

a = 3
b = 4
c = 5
is_right_triangle(a, b, c)

# test 1: Треугольник со сторонами 3, 4, 5 является прямоугольным
if is_right_triangle(3, 4, 5):
	print('test Ok')
else:
	print('test Fail')


# test 2: Треугольник со сторонами 5, 12, 13 является прямоугольным
if is_right_triangle(5, 12, 13):
	print('test Ok')
else:
	print('test Fail')

# test 3: Треугольник со сторонами 8, 15, 17 является прямоугольным
if is_right_triangle(8, 15, 17):
	print('test Ok')
else:
	print('test Fail')

# test 4: Треугольник со сторонами 7, 24, 25 является прямоугольным
if is_right_triangle(7, 24, 25):
	print('test Ok')
else:
	print('test Fail')

# test 5: Треугольник со сторонами 6, 8, 10 не является прямоугольным
if is_right_triangle(6, 8, 10):
	print('test Ok')
else:
	print('test Fail')

# test 6: Треугольник со сторонами 1, 2, 3 не является прямоугольным
if is_right_triangle(1, 2, 3):
	print('test Ok')
else:
	print('test Fail')
