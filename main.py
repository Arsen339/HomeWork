# импорт встроенных функций
from random import randint
from termcolor import cprint

# импорт модуля проверки ошибок
from DumbGamerProtection import *

# массив для случайно сгенерированного числа
number = []

#Компьютер генерирует число
number.append(str(randint(1, 9)))
for i in range(3):
    number.append(str(randint(0, 9)))

# интерфейс
cprint("Компьютер загадал четырехзначное число.", color='yellow')
cprint("Бык-число на своем месте, корова - число есть , но оно не на своем месте", color='yellow')
cprint("код out!-узнать ответ ", color='yellow')
# cprint("test for answer {}".format(number), color='yellow')

while True:
    # инициализируем переменные подсчета быков, коров и массив для введенного числа
    bull_count = 0
    cow_count = 0
    user_try_array = []
    user_try = input("Введите число")
    # проверка ответа
    if user_try == 'out!':
        cprint("Ответ: {} ".format(number), color="green")
    if (catch_mistake(user_try)) == 0:
        continue
    # сформируем массив из цифр введенного числа и выведем его
    for integer in user_try:
        user_try_array.append(integer)
    cprint("Вы ввели {}".format(user_try_array), color='yellow')
    # подсчет быков и коров
    for i in range(4):
        if str(user_try_array[i]) == str(number[i]):
            bull_count = bull_count + 1
        if str(user_try_array[i]) != str(number[i]) and user_try_array[i] in number:
            cow_count = cow_count+1
    # вывод числа быков и коров
    cprint("Коров: {} ".format(cow_count), color='yellow')
    cprint("Быков: {}".format(bull_count), color='yellow')

    if user_try_array == number:
        break

cprint("Вы отгадали!", color='blue')
cprint("Число: {}".format(number), color='blue')




