import random
backpack =[]
def robot_forward():
    print('Робот идет вперед')
def robot_left():
    print('Робот идет влево')
def robot_right():
    print('Робот идет вправо')
def robot_backward():
    print('Робот идет назад')
def robot_take(thing):
    global backpack
    print(f'Робот взял {thing}')
    backpack.append(thing)
def robot_scan():
    things_to_find = ['алмаз', "рубин", "кварц", "дерево", "золото"]
    thing = random.choice(things_to_find)
    if random.randint(1,2) == 1:
        return thing
    else:
        return ''
def robot_search():
    global backpack
    view = robot_scan()
    if view:
        print(f'Робот видит перед собой {view}')
        backpack.append(view)
    else:
        print('Робот ничего здесь не видит')
def view_backpack():
    for i, item in enumerate(backpack):
        print(f'{i+1}. {item}')
def craft():
    recept1 = ['золото']*3#золотой слиток
    recept2 = ['золотой слиток'] * 2 + ['дерево']#золотой меч
    recept3 = ['алмаз'] *2 + ['дерево']#алмазный меч
    recepts = [recept1, recept2, recept3]  
    recepts_name = ['золотой слиток', 'золотой меч', "алмазный меч"]
    for i, item in enumerate(recepts):
        print(f'{i+1}. {recepts_name[i]}: {item}')
    choice = input('Выбери что крафтить: ')
    if not choice.isdigit():
        print('нужно вводить число: ')
    elif int(choice) < len(recepts):
        thing = recepts[int(choice) - 1]
        while thing:
            view_backpack()
            print(f'Осталось: {thing}')
            choice = input('Что используем: ')
            if choice == 'стоп':
                break
            elif not choice.isdigit():
                print('нужно вводить число: ')
            elif int(choice) <= len(backpack):
                used = backpack.pop(int(choice)-1)
                print(f'Использовано {used}')
                if used in thing:
                    thing.remove(used)
                else:
                    print("Ингредиент сломался")
    if not thing:
        item = recepts_name[recepts.index(thing)]
        backpack.append(item)
        print(f"СОБЫТИЕ! {item} ДОБАВЛЕН В РЮКЗАК!")



def main():
    while True:
        key = input('Нажмите на клавишу: ')
        if key == 'a':
            robot_left()
            robot_search()
        elif key == 'd':
            robot_right()
            robot_search()
        elif key == 'w':
            robot_forward()
            robot_search()
        elif key == 's':
            robot_backward()
            robot_search()
        elif key == 'i':
            view_backpack()
        elif key == 'c':
            craft()
        elif key == 'x':
            print("Робот прощается с тобой")
            break

