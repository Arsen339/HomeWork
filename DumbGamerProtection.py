from termcolor import cprint

def catch_mistake(input_args):
    """Проверка входных данных"""

    input_args_mas = []
    if len(input_args) != 4:
        "проверка четырехзначности"
        cprint("Ошибка! Число должно быть четырехзначным!", color='red')
        return 0
    elif input_args.isdigit() != 1:
        "проверка на число"
        cprint("Введите число, а не буквы!", color='red')
        return 0
    for num in input_args:
        "распарсим входные данные в массив для определение первого элемента"
        input_args_mas.append(num)
    if input_args_mas[0] == '0':
        "проверка, не начинается ли число с 0"
        cprint("Четырехзначное число не может начинаться с 0!", color='red')
        return 0