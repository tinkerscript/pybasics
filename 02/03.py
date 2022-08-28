"""
Создайте программу “Медицинская анкета”,
где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес
"""

firstName = input('Enter first name: ')
lastName = input('Enter last name: ')
age = int(input('Enter age: '))
weight = float(input('Enter weight: '))

if (weight > 50) and (weight < 120):
    recommendation = 'good'
elif weight >= 120:
    recommendation = 'need doctor'
else:
    recommendation = 'need gym'

print(f'{firstName} {lastName}, age {age}, weight {weight} - {recommendation}')
