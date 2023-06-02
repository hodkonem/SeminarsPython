"""
Создать телефонный справочник с возможностью импорта и
экспорта данных в формате .txt. Фамилия, имя, отчество,
номер телефона - данные, которые должны находиться в файле.

Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска 
определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной

Дополнить телефонный справочник возможностью изменения и
удаления данных. Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных


r - только чтение файла
a - дозапись в файл
w - перезапись файла
"""


def show_data():
    #  Метод показывает содержимое справочника
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book


def new_data():
    # Метод добавляет строку в справочник
    with open('data.txt', 'a', encoding='utf-8') as file:
        new_line = input('Введите новую строку: ')
        file.write(new_line + '\n')


def find_data():
    # Метод ищет информацию в справочнике
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Что ищем?: ')
        for i in book:
            if temp in i:
                print(i)


def delete_person(name):
    # Метод удаляет данные
    persons = read_data()
    with open("data.txt", "w", encoding="utf8") as file:
        for person in persons:
            if name != person:
                file.write(person + '\n')


def change_person(new_name, old_name):
    # Изменяет данные
    persons = read_data()
    with open("data.txt", "w", encoding="utf8") as file:
        for person in persons:
            if old_name != person:
                file.write(person + '\n')
            else:
                file.write(new_name + "\n")


def read_data():
    # Метод читает данные из файла
    with open('data.txt', 'r', encoding='utf-8') as file:
        persons = file.read().split('\n')
    return persons


while True:
    mode = input('Выберите режим работы справочника' + '\n'
                 + '0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')

    if mode == '1':
        print(show_data())

    elif mode == '0':
        find_data()

    elif mode == '2':
        new_data()

    elif mode == '3':
        name = input('Кого удаляем?: ')
        persons = read_data()
        if name not in persons:
            print("Такой записи не существует!")
        else:
            delete_person(name)

    elif mode == '4':
        old_name = input('Кого хотим переименовать?: ')
        new_name = input('Как хотим его назвать?: ')
        persons = read_data()
        if old_name not in persons:
            print("Такой записи не существует!")
        else:
            change_person(new_name, old_name)

    elif mode == '5':
        break

    else:
        print('Неверный режим работы!')
