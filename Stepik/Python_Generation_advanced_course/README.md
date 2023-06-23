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
