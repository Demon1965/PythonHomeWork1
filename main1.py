""" Задача 2: Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)  """

""" a= int(input("Please, input any three digit number: "))
if a < 100 or a > 999:
    print("Sorry, you are wrong! Try again")
else:
    sum = 0
    while a > 0:
        sum = sum + a % 10
        a = a // 10
    print("The Sum of all digits is:", sum ) """



""" Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10 """
    
""" s = int(input("Please, input the quantity of origami: "))  # Петя сделал одну долю и Сережа сделал одну долю, вместе две доли. Катя сделала четыре доли (Какая молодец!!!) итого на четверых 6 долей!
kate = s * 4 / 6
serg = peter = s / 6
print("Kate made", kate,"origami Serg anp Peter made per", serg,"origami") """



""" Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no """

""" a = str(input("Please, input your ticket's number: "))
str1 = a[:3]
str2 = a[len(a)-3:]
sum1 = sum2 = 0
for i in str1:
    sum1 = sum1 + int(i)
for j in str2:
    sum2 = sum2 + int(j)
if sum1 == sum2: 
    print("Congradulations! It's happy ticket! You should eat it i!")
else:
    print("You have usual ticket!") """



""" Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку 
на два прямоугольника).
Пример
3 2 4 -> yes
3 2 1 -> no """

n = int(input("Please, input number of chocolate's row N: "))       # n1 - это полоска в один ряд и m колонок, разломов будет n-1. n1 += 1  Это полоска в два ряда и m колонок
m = int(input("Please, input number of chocolate's column M: "))    # m1 - это полоска в одну колонку и n рядов, разломов будет m-1. m1 += 1  Это полоска в две колонки и n рядов
k = int(input("Please, input the quantity of segments K: "))
i = j = z = 1
while i < n:
    if (n - i) * m == k:
        print("Yes, you can break off such segments of chocolate!")
        i += 1
        z += 1
    else:
        i += 1
while j < m:
    if (m - j) * n == k:
        if z == 1:
            print("Yes, you can break off such segments of chocolate!")
        else:
            print("Yes, and in this case you will get such segments of chocolate!")
        j += 1
        z += 1
    else:
        j += 1
if z == 1:   
    print("Sorry, you were left without chocolate! ")