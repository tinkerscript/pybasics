"""
Даны два произвольных списка. Удалите из первого списка элементы
присутствующие во втором списке
"""

my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

# i = len(my_list_1) - 1
#
# while i >= 0:
#     if my_list_1[i] in my_list_2:
#         del my_list_1[i]
#     i -= 1

for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)

print(my_list_1)
