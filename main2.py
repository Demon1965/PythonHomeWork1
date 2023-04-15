""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
 """
 
""" q = int(input("Please, insert the quantity of coins:  "))
count0 = 0
count1 = 0
while count0 + count1 < q:
    z = int(input("Please, input avers(0) or revers(1): "))
    if z == 0:
        count0 += 1
    else:
        count1 += 1
if count0 < count1:
    print(count0)
else:
    print(count1)
 """






""" Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа. """



""" sum = int(input("Please, mind two integer positive numbers and insert their SUM number:  "))
mult = int(input("Please, now input their MULTIPLY number:  "))

for x in range(1, 1001, 1):
    for y in range (1, 1001, 1):
        if sum == x + y and mult == x * y:
            print(x, y)
        break
 """

""" Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N. """



""" n = int(input("Please, input any integer positive number, except NULL:  "))
i = 1
while 2**i <= n:
    res = 2**i
    print(i)
    i+=1 """




""" Дан список чисел. Определите, сколько в нем встречается различных чисел.



list_test = list()
while True:
    a = input("Заполните массив")
    if a == 'q':
        break
    else:
        list_test.append(int(a))
set_test = set(list_test)
print(len(set_test))


Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
(сдвиг - циклический) на K элементов вправо, K – положительное число.



list_test = [1, 2, 3, 4, 5, 7, 8, 9]
k = int(input("Введите число сдвига"))
value = list_test[k:]
for i in list_test[:k]:
    value.append(i)
print(value)


Напишите программу для печати всех уникальных значений в словаре.
# {2: 3, 4: 3, 4: 5} -> 3, 5 """



dict_test = {2: 3, 4: 3, 5: 5}
set_test = set()
for i in dict_test:
    set_test.add(dict_test[i])
print(set_test)


""" Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает 
количество элементов массива, больших предыдущего (элемента с предыдущим номером)



list_test = [0, -1, 5, 2, 3]
list_temp = []
count = 0
for i in range(len(list_test)-1):
    if list_test[i] < list_test[i+1]:
        count += 1
        list_temp.append(f"{list_test[i]} < {list_test[i+1]}")
print(f"{count}{list_temp}") """


# https://www.dropbox.com/s/7n18ccc3dgxf8u9/workbook.pdf?dl=0