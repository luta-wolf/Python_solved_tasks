# name = input("Как тебя зовут? ")
# print('Привет,', name, ',мне очень приятно:)')
from typing import Optional, Union, NamedTuple, TypeAlias, NewType

ResType: TypeAlias = Optional[Union[int, float]]
rub = NewType("rub", float)
dol = NewType("dol", float)

class Person(NamedTuple):
	name: str
	age: int



reponse: ResType = 5.0
col1: rub = rub(76.5)
col2: rub = dol(70.5)

age = 'dfsadf'
print(col1)
print(col2)

