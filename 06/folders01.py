"""
Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код.
Затем создайте вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.
"""

import os


def create():
    for i in range(1, 10):
        folder_name = os.path.join(os.getcwd(), f'dir_{i}')
        os.mkdir(folder_name)


def delete():
    for i in range(1, 10):
        folder_name = os.path.join(os.getcwd(), f'dir_{i}')
        os.rmdir(folder_name)
