""" Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
второго множества. Затем пользователь вводит сами элементы множеств. """

""" import random
    
n = int(input("Please, insert the quantity of first array's elements: "))
list_first = [random.randint(1, 10) for i in range (n)]
list_first.sort()
print(list_first)
m = int(input("Please, insert the quantity of second array's elements: "))
list_second = [random.randint(1, 10) for i in range (m)]
list_second.sort()
print(list_second)
set_first = set(list_first)
set_second = set(list_second)
set_new = set_first.union(set_second) 
print(set_new) """


""" Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
на них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве 
внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и 
нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед 
некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для 
нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки."""


import random
n = int(input("Please, insert the quantity of blueberry bushes: "))
bush = [random.randint(80, 100) for i in range(n)]
print(bush)
sum = list()
for i in range(len(bush)-1):
    sum.append(bush[i-1] + bush[i] + bush[i + 1])
sum.append(bush[-2] + bush[-1] + bush[0])    
print(max(sum))


""" Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1 """

""" import random 

number_list = int(input("Введите количтсво оценок: "))
some_list = [random.randint(1, 5) for i in range (number_list)]

min = max = some_list[0]

for i in some_list:
    if min > i:
          min = i
    elif max < i:
          max = i

print(*some_list)

for i in range (len(some_list)):
    if some_list[i] == max:
        some_list[i] = min

print(*some_list)
 """

""" Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество
в строку, сворачивая соседние по числовому ряду числа в диапазоны.
Примеры:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4" """


""" some_list = [1, 4, 3, 9, 8, 11, 0, 13, 5, 12]
some_list.sort()
result_list = []
temp_list = []
print(some_list)
for i in range(0, len(some_list)-1):
    if some_list[i + 1] - some_list[i] == 1:
        temp_list.append(some_list[i])
    else:
        temp_list.append(some_list[i])
        result_list.append(temp_list)
        temp_list = []
if temp_list:
    result_list.append(temp_list)

if some_list[-1] - some_list[-2] == 1:
    result_list[-1].append(some_list[-1])
else:
    result_list.append([some_list[-1]])

print(result_list) """
