import datetime
import os
dict_user = {}
my_list_text = []
dict_menu = {
    '1':'Написать объявление.',
    '2':'Прочитать объявление.',
    '3':'Удалить строку в объявлении.',
    '4':'Удалить объявление.',
    '5':'Удалить файл.',
    '6':'Удалить пользователя.',
    '7':'Выйти'
}
def add_text():
    count = 0
    my_list_text.append(str(datetime.date.today()))
    print('Введите объявление ,доступко 10 строк')
    while (count < 10):
        my_list_text.append(input())
        count += 1
    print(dict_user)
def add_file():
    with open("File_name/ads.txt", "w") as file:
        for line in my_list_text:
            file.write(line + '\n')
def read_file():
    with open("File_name/ads.txt","r") as file:
        for line in file:
            print(line)
def remove_file():
    if os.path.isfile('/Python Project/Bulletin Board/File_name/ads.txt'):
        os.remove('/Python Project/Bulletin Board/File_name/ads.txt')
        print("Файл успешно удален")
    else: print("Файл не найден")
def remove_line_text_file():
    with open("File_name/ads.txt", "r") as file:
        lines = file.readlines()
    del lines[int(input('Какую строку хотите удалить?'))]
    with open("File_name/ads.txt", "w") as file:
        file.writelines(lines)

#Надо дорабоать
def remove_text_file():
    line_text = 0
    n = 0
    with open("File_name/ads.txt", "r") as file:
        lines = file.readlines()
    while line_text < 10:
        del lines[n]
        n+=1
        line_text+=1
    with open("File_name/ads.txt", "w") as file:
        file.writelines(lines)
#Дорабоать
def user_regist():
    print('Для работы с объявлениями вам требуется зарегестрироваться.')
    dict_user[input('Введите имя пользователя\n')] = input('Введиет пароль\n')
    with open("users.txt", "w") as file:
        for line in dict_user:
            file.write(line + '\n')
#Авторизация не дорабоатна
def user_authorization():
    print('Теперь авторизируйтесь и можете приступать к работе.')
    while True:
        answer_name = input('Введите логин:\n')
        answer_password = input('Введите пароль:\n')
        for key in dict_user.keys():
            for value in dict_user.values():
                if key == answer_name and value == answer_password:
                    print('Вход выполнен успешно.')
                    break
                else:
                    print('Вы ввели неверный логин или пароль.')

def menu():
    for key in dict_menu.keys():
        for value in dict_menu.values():
            if value == dict_menu[key]:
                print(key + '-' + dict_menu[key])
while True:
    menu()
    answer = input('Выберите варинат меню:\n')
    if answer == '1' :
        add_text()
        add_file()
    elif answer == '2' :
        read_file()
    elif answer == '3' :
        remove_line_text_file()
    #elif answer == '4' :
    #    remove_text_file()
    elif answer == '5' :
        remove_file()
    # elif answer == '6':
    elif answer == '7':
        break
    else:
        print('Вы ввели некоректроный ответ.')
