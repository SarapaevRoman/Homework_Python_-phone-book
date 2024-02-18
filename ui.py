from logger import *

def interface():
    print('Добрый день! Вы попали на специальный бот справочник от GeegBrains! \n 1 - Запись данных \n 2 - Вывод данных \n 3 - Изменение данных \n 4 - Удаление контакта')
    command = int(input('Введите число: '))
    #while command != 1 and command != 2:
    while command < 1 or command > 4:
        print('Неправильный ввод')
        command = int(input('Введите число: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        change_contact()
    elif command == 4:
        delet_contact()    
     