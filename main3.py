""" Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Пример:
5
    1 2 3 4 5
    3
    -> 1 """
    
    
""" import random
    
n = int(input("Please, insert any positive number: "))
new_list = list()
for i in range(n):
    new_list.append(random.randint(1, 10))
print(new_list)
x = int(input("What number do you want to check?:  "))
count = j = 0
while j < n:
    if x == new_list[j]:
        count += 1
        j += 1
    else:
        j += 1
print(f"The number {x} we have founded {count} times!") """
    
       
    
""" Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в списке. В последующих  
строках записаны N целых чисел Ai. Последняя строка содержит число X
Пример:
5
    1 2 3 4 5
    6
    -> 5 """
    
    
    
""" import random
    
n = int(input("Please, insert any positive number until 10: "))
new_list = list()
for i in range(n):
    new_list.append(random.randint(1, 10))
print(new_list)
x = int(input("What number do you want to check?:  "))
j = 0
while j < n:
    if x - new_list[j] == 1 or x - new_list[j] == -1:
        print(f"The number {new_list[j]} is closest to {x}!")
        j += 1
    else: 
        j += 1
 """
    

    
""" Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 
А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет 
стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо 
только английские, либо только русские буквы.
Пример:
ноутбук
    12 """
    


lang = str(input("Please, you should choice languadge you will use (en OR rus): "))
sum = 0
if lang == 'en':
    str_en = str(input("Please, write here any word: "))
    dict_en = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
    for i in str_en:
        if dict_en.get(i):
            sum += dict_en[i]
    print(f"You have {sum} points!")
else:
    str_rus = str(input("Напишите любое слово: "))
    dict_rus = {'а':'1','б':'3','в':'1','г':'3','д':'2','е':'1','ё':'3','ж':'5','з':'5','и':'1','й':'4','к':'2','л':'2','м':'2','н':'1','о':'1','п':'2','р':'1','с':'1','т':'1','у':'2','ф':'10','х':'5','ц':'5','ч':'5','ш':'8',
'щ':'10','ъ':'10','ы':'4','ь':'3','э':'8','ю':'8','я':'3'}
    for i in str_rus:
        if dict_rus.get(i):
            sum += int(dict_rus[i])
    print(f"Вы набрали {sum} очков!")
