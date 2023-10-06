# функция сложения
def plus(a, b):  # \ div - делить, sub - вычесть
    return a + b


# функция умножения
def mul(a, b):
    return a*b


# функция деления
def div(a, b):
    return a/b


#функция вычитания
def minus(a, b):
    return a - b


def calc():
    while True:
        num1 = input('1 число: ')
        num1 = int(num1)
        operator = input('Введите знак: ')
        num2 = input('2 число: ')
        num2 = int(num2)
   
        if operator == '+':
            answer = plus(num1, num2)
        elif operator == '-':
            answer = minus(num1, num2)
        elif operator == '*':
            answer = mul(num1, num2)
        elif operator == '/':
            answer = div(num1, num2)
        print(f'Ответ: {answer}')
   
        stop = input('Закончить?')
        if stop == 'да':
            break
