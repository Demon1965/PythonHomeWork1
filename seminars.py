 with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     for letter in text:
#         print(letter)


# with open('example.txt', 'r', encoding='utf-8') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line[:-1])

# with open('example.txt', 'r', encoding='utf-8') as file:
#     line = file.readline()
#     while line:
#         print(line[:-1])
#         line = file.readline()


# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.splitlines())

# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.readlines()
#     print(text)
""" 
with open('example.txt', 'w', encoding='utf-8') as file:
    some_list = ['hello', 'world', 'how', 'are', 'you']
    for el in some_list:
        file.write(el + '\n') """
        
        
""" Пользователь вводит кол-во строк, затем сами строки. Нужно записать в новый текстовый файл все эти строки
Далее пользователь вводит символ, нужно найти кол-во этого символа в новом файле. """

with open('test.txt', 'w') as test:    
    n = int(input()) 
    for i in range(n):        
        test.write(input() + '\n')
    simbol = input()
    with open('test.txt', 'r') as test1:    
        data = test1.readline()    

# print(data)    
# sum = 0    
# while data:        
# # print(data)        
# sum += data.count(simbol)        
# data = test1.readline()print(sum)

""" Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и
выводить на печать построчно последние строки в количестве lines
(на всякий случай проверим, что задано положительное целое число).
Протестируем функцию на файле «article.txt» со следующим содержимым:

Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
 """
 
 # def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as f:
#         l = f.read().splitlines()
#         for i in range(len(l) - lines, len(l)):
#             print(l[i])
#
#
# read_last(3, 'article.txt')



# Документ «article.txt» содержит следующий текст:
# 
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела 
# 
# Требуется реализовать функцию longest_words(file), которая выводит слово, 
# имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read().lower().split()
        print(text)
        max = 0

        for i in range(len(text)):
            if len(text[i]) > max:
                max = i
        newlist = []

        for y in range(len(text)):
            if len(text[y]) == len(text[max]):
                newlist.append(text[y])
        print(newlist)


longest_words('article.txt')