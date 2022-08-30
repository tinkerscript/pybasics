"""
Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
name - строка полученная от пользователя,
health = 100,
damage = 50
"""

player = {
    'name': input('Введите имя игрока: '),
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy = {
    'name': input('Введите имя противника: '),
    'health': 100,
    'damage': 50,
    'armor': 1.2
}


def attack(person1, person2):
    if person1 == player['name']:
        source = player
    elif person1 == enemy['name']:
        source = enemy
    else:
        print('Неверное имя атакующего')
        return

    if person2 == player['name']:
        target = player
    elif person2 == enemy['name']:
        target = enemy
    else:
        print('Неверное имя атакуемого')
        return

    damage = reduce_by_armor(source['damage'], target['armor'])
    hp = target['health'] - damage

    if hp < 0:
        target['health'] = 0
        print(f"{target['name']} всё")
    else:
        target['health'] = hp
        print(f"У {target['name']} осталось {target['health']} хп")


def reduce_by_armor(damage, armor):
    return damage / armor


attack(input('Кто бьёт: '), input('Кого бьют: '))
