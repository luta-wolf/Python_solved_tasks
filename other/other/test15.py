class Toy:
    def move(self):
        pass

class Ball(Toy):
    def move(self):
        print("The ball is bouncing!")

class Car(Toy):
    def move(self):
        print("The car is driving!")

class Cube(Toy):
    def move(self):
        print("The cube is rotating!")

# Создаем список игрушек
toys = [Ball(), Car(), Cube()]

# Вызываем метод move() для каждой игрушки в списке
for toy in toys:
    toy.move()


s = 'hello world!'
styyy = 's'
a = eval(styyy)
print(a)


class ball:
    _size = 10

    def __private(self):
        print('private')




boo = ball()
boo.__private()
boo._size = 5
print(boo._size)
