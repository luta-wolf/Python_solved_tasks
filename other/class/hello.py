a = '123'


def add():
    pass


# print(globals())

# print('Imported from: ', __name__)

def squaring(i: int) -> int:
    return i * i #if i % 2 == 0 else i * -4


def main():
    lst: list = [i for i in range(10)]
    lst2: list = list(map(squaring, lst))
    print(lst, '\n', lst2)


if __name__ == "__main__":
    main()
