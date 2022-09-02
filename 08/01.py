"""
Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
"""

list1 = ['apple', 'orange', 'banana', 'kiwi']
list2 = ['pineapple', 'lemon', 'kiwi', 'orange']

result = [fruit for fruit in list1 if fruit in list2]
print(result)
