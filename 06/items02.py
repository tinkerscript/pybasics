"""
Создайте модуль. В нем создайте функцию, которая принимает список
и возвращает из него случайный элемент. Если список пустой функция должна вернуть None.
Проверьте работу функций в этом же модуле.
"""

from random import choice


def random_item(items):
    item = None

    if len(items) != 0:
        item = choice(items)

    return item
