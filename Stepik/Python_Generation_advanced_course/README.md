[Сравнить текст](https://text-compare.com/)

## Типы данных в Python
<img width="1084" alt="image" src="https://github.com/luta-wolf/luta-wolf/assets/58044383/ea82afef-af05-4fd2-b18e-21169d691065">
    print(17 > 7)  --> True
    print(17 == 7) --> False
    print(17 < 7)  --> False

Запомните: приоритет оператора not выше, чем у оператора and, приоритет которого, в свою очередь, выше, чем у оператора or.

Логические значения в Python можно трактовать как числа. Значению True соответствует число 1, в то время как значению False соответствует 0 . Таким образом мы можем сравнить логические значения с числами:
    print(True + True + True - False)	--> 3
    print(True + (False / True))		--> 1.0
<img width="885" alt="image" src="https://github.com/luta-wolf/luta-wolf/assets/58044383/496c378c-b37c-4ef6-932b-7bfbb738793b">

### Функция bool()
Для приведения других типов данных к булеву существует функция bool(), работающая по следующим соглашениям:

- строки: пустая строка — ложь (`False`), непустая строка — истина (`True`);
- числа: нулевое число — ложь (`False`), ненулевое число (в том числе и меньшее нуля) — истина (`True`);
- списки: пустой список — ложь (`False`), непустой — истина (`True`).
    print(bool('Beegeek'))				--> `True`
    print(bool(17))						--> `True`
    print(bool(['apple', 'cherry']))	--> `True`
    print(bool())						--> `False`
    print(bool(''))						--> `False`
    print(bool(0))						--> `False`
    print(bool([]))						--> `False`

В программировании функция, которая возвращает значение `True` или `False` называется **предикатом**.

### Функция isinstance()
- `isinstance()` проверяет соответствиу типа объекта какому-либо типу данных.
print(isinstance(3, int))			--> `True`
print(isinstance(3.5, float))		--> `True`
print(isinstance('Beegeek', str))	--> `True`
print(isinstance([1, 2, 3], list))	--> `True`
print(isinstance(True, bool))		--> `True`
print(isinstance(3.5, int))			--> `False`
print(isinstance('Beegeek', float))	--> `False`

### Функция type()
- type() позволяет получить тип указанного в качестве аргумента объекта.
    print(type(3))			--> `<class 'int'>`
    print(type(3.5))		--> `<class 'float'>`
    print(type('Beegeek'))	--> `<class 'str'>`
    print(type([1, 2, 3]))	--> `<class 'list'>`
    print(type(True))		--> `<class 'bool'>`
Функция type() часто бывает полезна при отладке программного кода, а также в реальном коде, особенно в объектно-ориентированном программировании с наследованием и пользовательскими строковыми представлениями, но об этом позже.

Обратите внимание, что при проверке типов обычно вместо функции `type()` используется функция `isinstance()` так как, она принимает во внимание **иерархию типов (ООП)**.

### тип данных NoneType
- `None` в Python позволяет представить `null` переменную, то есть переменную, которая не содержит какого-либо значения. По сути None – это специальная константа, означающая пустоту. Если более точно, то `None` – это объект специального типа данных `NoneType`.
<img width="729" alt="image" src="https://github.com/luta-wolf/Python_solved_tasks/assets/58044383/ff4aa226-1fd1-4f1a-96d7-6498d846c554">

```
var = None
print(type(var)) --> <class 'NoneType'>
```

### Проверка на None

```var = None
if var is None:   # используем оператор is
  print('None') --> None
else:
  print('Not None')
```

Следующий программный код:

```
var = None
if var == None:   # используем оператор ==
  print('None')
else:
  print('Not None')
```

Следующий программный код:

```print(None == 17)        ---> False
print(None == 3.14)         ---> False
print(None == True)         ---> False
print(None == [1, 2, 3])    ---> False
print(None == 'Beegeek')    ---> False

print(None == 0)            ---> False
print(None == False)        ---> False
print(None == '')           ---> False
```

**Значение `None` не отождествляется с значениями `0, False, ''`**.

### Создание вложенных списков
**Способ 1**. Создадим пустой список, потом n раз добавим в него новый элемент – список длины m, составленный из нулей:

```n, m = int(input()), int(input())    # считываем значения n и m
my_list = []

for _ in range(n):
    my_list.append([0] * m)

print(my_list)
```

Если ввести значения n = 3, m = 5, то результатом работы такого кода будет:

```[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```

Если передать значения n = 5, m = 3, то результатом работы такого кода будет:

```[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

**Способ 3**. Можно использовать генератор списка: создадим список из n элементов, каждый из которых будет списком, состоящих из m нулей:

```n, m = int(input()), int(input())    # считываем значения n и m

my_list = [[0] * m for _ in range(n)]

print(my_list)
```

### Считывание вложенных списков

```n = 4                                          # количество строк (элементов)
my_list = []

for _ in range(n):
    elem = [int(i) for i in input().split()]   # создаем список из элементов строки
    my_list.append(elem)
```

### Перебор и вывод элементов вложенного списка

```my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')   # используем необязательный параметр end
    print()
```

 Результатом работы такого кода будет:

```1 2 3
4 5 6
7 8 9
```

Перебор элементов вложенного списка по индексам дает нам больше гибкости для вывода данных. Например, поменяв порядок переменных i и j мы получаем иной тип вывода:

```my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
    print()
```

Результатом работы такого кода будет:

```1 4 7
2 5 8
3 6 9
```

### Обработка вложенных списков

Используем вложенный цикл для подсчета суммы всех чисел в списке:

```my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total += my_list[i][j]
print(total)
````

Или то же самое с циклом не по индексу, а по значениям:

````my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:
    for elem in row:
        total += elem
print(total)
````

Названия переменных `row` (строка) и `elem` (элемент) удобно использовать при переборе вложенного списка по значениям. Названия переменных `i` и `j` используются при переборе вложенного списка по индексам.
