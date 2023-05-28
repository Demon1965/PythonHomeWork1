""" Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной
 """
 
 
def insert():
    record = []
    record.append(input("\n" + "Введите Фамилию: "))
    record.append(input("\n" + "Введите Имя: "))
    record.append(input("\n" + "Введите Отчество: "))
    record.append(input("\n" + "Введите Год рождения: "))
    record.append(input("\n" + "Введите телефон: "))
    with open('people.txt', 'a', encoding='utf-8') as data:
        data.write(str(record).upper() + '\n')
            
def output():
    with open('people.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)
            
def search():
    with open('people.txt', 'r', encoding='utf-8') as data:
        pers = input('Ведите любой параметр ФИО, год, телефон: ')
        for line in data:
            if pers.upper() in line:
                print('Найден:' + line)
            else:
                print('Совпадение нет!')
    

while True:
    print('1 - Ввести пользователя, 2 - Просмотр файла, 3 - Найти пользователя')
    mode = int(input())
    if mode == 1:
        insert()    
    elif mode == 2:
        output()
    elif mode == 3:
        search()
    else:
        break
