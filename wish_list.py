import os
def read_file(filename:str):
    if not os.path.exists(filename):
        open(filename, "w")
        return []
    with open(filename, encoding="utf-8") as file: 
        return file.read().split('\n')

def write_file(filename:str, data_list:list):
   with open(filename, "w", encoding="utf-8") as file:  
       for line in data_list:
           file.write(f"{line}\n")

def wish_app():
    flag = True
    wish_list = read_file("желания.txt")
    while flag:
        print('Добро пожаловать в мой чудесный список желаний!')
        print('Выбери действие:')
        print('1 - добавить в список желаемого')
        print('2 - удалить из списка желаемого')
        print('3 - вывести вишлист')
        print('4 - выйти из программы')
        action = input('->')
        if action == '1':
            wish = input('Новая запись: ')
            if wish == '':
                print('Вы ничего не ввели')
            else:
                if wish not in wish_list:
                    wish_list.append(wish)
                    print(f'{wish} добавлена')
                else:
                    print(f'{wish} уже есть')
        elif action == '2':
            if len(wish_list) < 2:
                print("Тут пока ничего нет!")
            else:
                print('Список желаний: ')
                for i, item in enumerate(wish_list):
                    print(f'{i+1}. {item}')
                wish_num = input('Какое желание сбылось?')
                if wish_num in range(len(wish_list)):
                    wish_list.pop(wish_num-1)
                    print(f'Желание  удалено')
                else:
                    print('такого желания нет')
        elif action == '3':
            if len(wish_list) ==0:
                print("Тут пока ничего нет!")
            else:
                print('Список желаний: ')
                for i, item in enumerate(wish_list):
                    print(f'{i+1}. {item}')

        elif action == '4':
            flag = False
            print('Спасибо за использование программы')
            break
        enter = input('Нажмите Enter, чтобы продолжить')


if __name__ == "__main__":
    wish_app()