class Phone:
    number = "111-11-11"
    def print_number(self):
        print( "Phone number is: ", self.number )

my_phone = Phone()
my_phone.print_number()

input( "Press Enter to exit" )

print('-' * 20)

class A:
    def _private(self):
        print("Это приватный метод!")

a = A()
a._private()
