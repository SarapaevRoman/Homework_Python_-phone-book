from data_create import *

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f'1 Вариант: \n'
    f'{name}\n{surname}\n{phone}\n{address}\n\n'
    f'2 Вариант: \n'
    f'{name};{surname};{phone};{address}\n'
    f'Выбирете вариант: '))

    while var != 1 and var != 2:
        print('Неверный ввод')
        var = int(input('Введите число: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')

    if var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address}\n\n')
def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j : i + 1]))
                j = i
        print(''.join(data_first_list))

    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()
        print(*data_second)

def change_contact():# Функция удаления контакта
    # Вводим контакт для поиска, выбираем файл
    search_name = input("Введите имя для поиска: ")
    found = False
    file_choice = int(input("В каком файле искать контакт?\n1. Первый файл\n2. Второй файл\nВыберите: "))
    while file_choice != 1 and file_choice !=2:
        print("Неверный выбор файла.")
        file_choice = int(input('Выберите номер файла: \n1. Первый файл\n2. Второй файл\nВыберите: '))

    if file_choice == 1:
        filename = 'data_first_variant.csv'
        delimiter = '\n'
    elif file_choice == 2:
        filename = 'data_second_variant.csv'
        delimiter = ';'
    # Считываем всю информацию из файла и сохраняем ее. Получаеться список в списке                  
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        contacts = []

    for line in lines:
        contact_data = line.strip().split(delimiter)
        contacts.append(contact_data)
    # Ищем запрашиваемый контакт и меняем его на новый
    for i in range(len(contacts)):    
        if search_name in contacts[i]: #and search_surname == contact_data[1]:
            name = input('Введите новое имя: ')
            surname = input("Введите новую фамилию: ")
            phone = input("Введите новый номер телефона: ")
            address = input("Введите новый адрес: ")
            if file_choice == 1:
                del contacts[i+1:i+4]               
            contacts[i:i+1] = [[name, surname, phone, address]]
            found = True
            break

    if found:
        with open(filename, 'w', encoding='utf-8') as f:
            for contact_data in contacts:
                    f.write(delimiter.join(contact_data)+'\n')
        print('Контакт успешно изменен')
    else:
        print('Контакт не найден')
def delet_contact(): # Функция удаления контакта
    #Вводим контакт для поиска и выбираем файл для удаления контакта
    search_name = input("Введите имя контакта: ")
    found = False
    file_choice = int(input("В каком файле искать контакт?\n1. Первый файл\n2. Второй файл\nВыберите: "))
    while file_choice != 1 and file_choice !=2:
        print("Неверный выбор файла.")
        file_choice = int(input('Выберите номер файла: \n1. Первый файл\n2. Второй файл\nВыберите: '))

    if file_choice == 1:
        filename = 'data_first_variant.csv'
        delimiter = '\n'
    elif file_choice == 2:
        filename = 'data_second_variant.csv'
        delimiter = ';'
    # Считываем всю информацию из файла и сохраняем ее. Получаеться список в списке           
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        contacts = []

    for line in lines:
        contact_data = line.strip().split(delimiter)
        contacts.append(contact_data)
    # Ищем запрашиваемый контакт и удаляем его
    for i in range(len(contacts)):    
        if search_name in contacts[i]:
            if file_choice == 1:
                del contacts[i:i+4]
            if file_choice == 2:
                del contacts[i]             
            found = True
            break
    # Перезаписываем файл
    if found:
        with open(filename, 'w', encoding='utf-8') as f:
            for contact_data in contacts:
                    f.write(delimiter.join(contact_data)+'\n')
        print('Контакт удален')
    else:
        print('Контакт не найден')