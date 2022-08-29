import random

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
