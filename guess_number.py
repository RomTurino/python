import random
import math

def input_number(input_num):
    number = input(input_num)
    if not number.isdigit():
        print("Вводить можно только числа")
        return input_number(input_num)
    return int(number)

def attempt_end(count):
    if count == 1:
        return "попытка"
    elif count in [2, 3, 4]:
        return "попытки"
    else:
        return "попыток"

def game():
    print("Приветствую! Я - компьютер. Я хочу сыграть с тобой в игру. Я загадаю число, а ты попробуешь его отгадать")
    min_num = input_number("Какое самое меньшее число я могу загадать? ")
    max_num = input_number("Какое самое большее число я могу загадать? ")
    attempts = int(math.log(max_num - min_num)) + 3

    print(f"Я загадал число от {min_num} до {max_num}. У тебя {attempts} {attempt_end(attempts)}, чтобы отгадать")
    secret_number = random.randint(min_num, max_num)
    
    while attempts > 0:
        my_number = input_number("Введите число:")
        print(secret_number)
        if my_number > secret_number:
            print("Твое число больше моего")
        elif my_number < secret_number:
            print("Твое число меньше моего")
        else:
            print("Ты угадал, чемпион!")
            break
        attempts -= 1
        print(f"Осталось {attempts} {attempt_end(attempts)}")
    
    answer = input("Если желаешь сыграть еще, нажми Enter, если нет - введи что-нибудь: ")
    if not answer:
        return game()
    print("Ну что ж, это была восхитительная игра. Всего хорошего тебе, человек!")


if __name__ == "__main__":
    game()