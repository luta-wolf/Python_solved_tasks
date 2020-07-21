'''
You have a table with all available goods in the store. The data is represented as a list of dicts
Your mission here is to find the TOP most expensive goods. The amount we are looking for will
be given as a first argument and the whole data as the second one

Input: int and list of dicts. Each dicts has two keys "name" and "price"
Output: the same as the second Input argument.

Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей
(a list of dicts).Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров,
которые мы ищем, будет передано в первом аргументе, а сами данные по товарам будут переданы
вторым аргументом.

Вх. данные: Число и список словарей (int and list of dicts). Каждый словарь имеет 2 ключа
"name" и "price".
Вых. данные: Такой же как и второй аргумент.
'''
def bigger_price(limit: int, data: list) -> list:
    pass


#tests
assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"