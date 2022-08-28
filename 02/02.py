"""
Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
После того как пользователь введет корректное число, возведите его в степень 2 и выведите на экран
"""

while True:
    number = float(input('Enter a number greater than 0 and lesser than 10: '))
    if (number > 0) and (number < 10):
        break
number = number ** 2
print('Square is ', number)
