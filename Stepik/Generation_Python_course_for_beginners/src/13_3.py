# Глобальные переменные

# 1
birds = 5000    # глобальная переменная

def print_texas():
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')

print_texas()
print_california()
# 2
def print_texas():
    global birds
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')

def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')

print_texas()
print_california()

# 3
