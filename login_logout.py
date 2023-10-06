import calc
import cows_bulls
import guess_number
import robot
import wish_list
import mortal_combat
from colorama import Fore
from progress.bar import PixelBar
import time
def progress_bar():
    bar = PixelBar('Загрузка:', max= 40)
    for i in range(40):
        time.sleep(0.01)
        bar.next()
    bar.finish()



def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
      return file.read().split('\n')
  
def sign_in():
    login_list = read_file('logins.txt')
    password_list = read_file('passwords.txt')
    login = input('Введите ваш логин: ')
    password = input('Введите ваш пароль: ')
    flag = False
    if login in login_list and password in password_list:
        flag = True
    return flag, login

def sign_up():
    print('Давайте мы вас зарегистрируем: ')
    login = input('Придумайте логин: ')
    password1 = input('Создайте пароль: ')
    password2 = input('Повторите пароль: ')
    if password1 == password2:
        with open('logins.txt', 'a', encoding='utf-8') as file:
            file.write(f'{login}\n')
        with open('passwords.txt', 'a', encoding='utf-8') as file:
            file.write(f'{password1}\n')
        print('вы успешно зарегистрированы')
        
def sign_out():
    print('Вы вышли из системы')
    flag, login = False, False
    return flag, login

flag = False
while True:
    progress_bar()
    if not flag:
        do = input("""
               Что вы хотите сделать?
               1 - войти в аккаунт
               2 - зарегистрироваться
               3 - выйти из программы
               """)
        if do == '1':
            flag, login = sign_in()
        elif do == '2':
            sign_up()
        elif do == '3':
            print('Спасибо за использование программы')
            break
        else:
            print('Такого варианта не существует')
    else:     
        print(Fore.RED + '1 - выйти из аккаунта')
        print(Fore.BLACK + '2 - выйти из программы')
        print(Fore.GREEN + '3 - запустить калькулятор')
        print(Fore.YELLOW + '4 - запустить РоботКрафт')
        print(Fore.BLUE + '5 - открыть список желаний')
        print(Fore.MAGENTA + '6 - поиграть в "Угадай число"')
        print(Fore.CYAN + '7 - поиграть в "Быки и коровы"')
        do = input(Fore.RESET + "Что вы хотите сделать?")
        if do == '1':
            flag, login = sign_out()
        elif do == '2':
            print('Спасибо за использование программы')
            break
        elif do == '3':
            calc.calc()
        elif do == '4':
            robot.main()
        elif do == '5':
            wish_list.wish_app()
        elif do == '6':
            guess_number.game()
        elif do == '7':
            cows_bulls.cb_game(login)
        elif do == '8':
            mortal_combat.fighting()
        
