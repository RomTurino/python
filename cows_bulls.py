import random
import time
import cowsay

def cb_game(login):
    login = login.capitalize()
    cowsay.cow('''Добро пожаловать в игру "Быки и коровы!"
          Компьютер загадает 4-значное число.
          Ты говоришь число из такого же количества символов.
          Если символы из твоего есть в загаданном - это корова.
          Если есть совпадение и по позиции символа - это бык''')
    while True:
        number_chars = input(f'{login}, сколькизначное число будет? ')
        if number_chars.isdigit():
            number_chars = int(number_chars)
            break
        cowsay.cow(f'{login}, ты ввел что-то не то')
    start_diapazon = 10**(number_chars-1)
    end_diapazon = 10**(number_chars)-1
    secret_number = str(random.randint(start_diapazon,end_diapazon))
    tries = 10
    for turn in range(tries):
        cowsay.cow(f'{login}, это попытка №{turn+1}')
        while True:
            user_number = input(f'{login}, введите ваше число: ')
            if not user_number.isdigit():
                cowsay.cow('Должно быть число')
                continue
            elif int(user_number) > end_diapazon or int(user_number) < start_diapazon:
                cowsay.cow(f'Должно быть в диапазоне от {start_diapazon} до {end_diapazon}')
                continue
            break
        cows = 0
        bulls = 0
        for i, char in enumerate(user_number):
            if user_number[i] == secret_number[i]:
                bulls+=1
            elif char in secret_number:
                cows+=1    
        cowsay.cow(f'В твоем числе {bulls} быков и {cows} коров, {login}')
        time.sleep(2)
        if bulls ==number_chars:
            cowsay.cow(f'Ты победил, {login}')
            return True
    cowsay.cow(f'Попытки кончились, ты проиграл, {login}')
    return False

if __name__ == "__main__":
    cb_game("Роман")
