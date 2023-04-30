""" Задача 30. Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
прогрессии: an = a1 + (n - 1) * d. Каждое число вводится с новой строки. """

""" n = int(input("Please, insert the quantity of list's elements: "))
a = int(input("Please, insert the first element of list: "))
d = int(input("Please, insert the difference of elements: "))
new_list = list()
for i in range(1, n+1):
    new_list.append(a + (i-1)*d)
    print(new_list)
print(new_list) """


""" 
Задача 32. Определить индексы элементов массива (списка), значения которых принадлежат заданному
диапазону (не меньше заданного минимума и не больше заданного максимума). """


import random
n = int(input("Please, insert the quantity of array's elements: "))
list1 = [random.randint(10, 100) for i in range(n)]
list1.sort()
print(list1)
n1 = int(input("Please, min: "))
n2 = int(input("Please, max: "))
list2 = list()
for i in range(n):
    if n1 < list1[i] < n2:
        list2.append(list1[i])
print(list2)
print(set(list2))
