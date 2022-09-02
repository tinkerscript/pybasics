"""
1. Добавить в программу проверку ввода пользователя для всех функции с параметрами
(на уроке разбирали на примере одной функции).
2. Добавить возможность изменения текущей рабочей директории.
3. Добавить возможность развлечения в процессе работы с менеджером.
Для этого добавить в программу запуск одной из игр: “угадай число” или “угадай число (наоборот)”.
"""

import sys
import random
from file_manager import create_file, copy_file, delete_file, create_folder, get_list, save_info, change_dir


def game():
    lower_bound = 1
    upper_bound = 100

    while True:
        number = random.randint(lower_bound, upper_bound)
        print(number)
        answer = input('Угадал?')

        if answer == '=':
            print('Ура!')
            break
        elif answer == '>':
            lower_bound = number + 1
        elif answer == '<':
            upper_bound = number - 1


def print_help():
    print('list - список файлов и папок')
    print('create_file - создание файлов')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('game - запуск игры')


commands = {
    'get_list': (get_list, 0),
    'create_file': (create_file, 1),
    'create_folder': (create_folder, 1),
    'delete_file': (delete_file, 1),
    'copy': (copy_file, 2),
    'change_dir': (change_dir, 1),
    'game': (game, 0),
    'help': (print_help, 0)
}


def execute(command):
    if command not in commands:
        raise ValueError(command)

    handler = commands[command][0]
    args_count = commands[command][1]

    if len(sys.argv) != args_count + 2:
        raise AssertionError(args_count)

    handler(*sys.argv[2:args_count + 2])


save_info('Начало')

try:
    if len(sys.argv) > 1:
        execute(sys.argv[1])
    else:
        print('Введите команду help для вывода списка доступных команд')
except ValueError as e:
    print('Неизвестная команда:', str(e))
except AssertionError as e:
    print(f'Недопустимое число аргументов команды. Команда поддерживает {str.e}: аргументов')
except Exception as e:
    print('Неизвестная ошибка:', str(e))

save_info('Конец')
