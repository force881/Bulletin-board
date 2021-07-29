import datetime
import os
dict_user = {}
my_list_text = []
def add_text():
    file = open('File_name/ads.txt', 'w')
    date_today = datetime.date.today()
    file.write(str(date_today)+'\n')
    file.write(input() + '\n' + 'Автор: ' + str(dict_user))
    file.close()
    print(file.closed)
    return file
def open_text():
    file = open('File_name/ads.txt')
    print(file.read())
    file.close()
def remove_file_text():
    if os.path.isfile('/Python Project/Bulletin Board/File_name/ads.txt'):
        os.remove('/Python Project/Bulletin Board/File_name/ads.txt')
        print("Файл успешно удален")
    else: print("Файл не найден")
def user_regist():
    dict_user[input('Введите имя пользователя\n')] = input('Введиет пароль\n')
    file_user = open('users.txt','r+')
    file_user.write(str(dict_user))
    file_user.close()
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

while True:
    print('Вам требуется зарегестрироваться:')
    user_regist()
    user_authorization()
    while True:
        answer = input('Вы можете написать объявление(а), прочитать его(r), удалить его(d), длч выхода нажмите(e)\n')
        if answer == 'a':
            add_text()
        elif answer == 'd':
            remove_text()
        elif answer == 'r':
            open_text()
        elif answer == 'e':
            break
        else:
            print('Вы ввели некоректроный ответ.')
    break





