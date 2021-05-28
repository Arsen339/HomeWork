from random import randint
from DumbGamerProtection import *
from termcolor import cprint

number = []

number.append(str(randint(1, 9)))
for i in range(3):
    number.append(str(randint(0, 9)))
cprint("Компьютер загадал четырехзначное число.", color='yellow')
cprint("Бык-число на своем месте, корова - число есть , но оно не на своем месте", color='yellow')
cprint("код out-узнать ответ ", color='yellow')
# cprint("test for answer {}".format(number), color='yellow')
while True:
    bull_count = 0
    cow_count = 0
    user_try_array = []
    user_try = input("Введите число")
    if (catch_mistake(user_try)) == 0:
        continue

    for integer in user_try:
        user_try_array.append(integer)
    cprint("Вы ввели {}".format(user_try_array), color='yellow')
    for i in range(4):
        if str(user_try_array[i]) == str(number[i]):
            bull_count = bull_count + 1
        if str(user_try_array[i]) != str(number[i]) and user_try_array[i] in number:
            cow_count = cow_count+1
    cprint("Коров: {} ".format(cow_count), color='yellow')
    cprint("Быков: {}".format(bull_count), color='yellow')
    if user_try_array == number:
        break
cprint("Вы отгадали!", color='blue')
cprint("Число: {}".format(number), color='blue')




