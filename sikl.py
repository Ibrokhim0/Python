# 1) Составить таблицу умножения, как на картинке ниже:—-

for horizontal in range(1, 9 + 1):
    print(horizontal, end="\t")
    print(horizontal * 2, end="\t")
    print(horizontal * 3, end="\t")
    print(horizontal * 4, end="\t")
    print(horizontal * 5, end="\t")
    print(horizontal * 6, end="\t")
    print(horizontal * 7, end="\t")
    print(horizontal * 8, end="\t")
    print(horizontal * 9, end="\n")
# 2) Создать программу, которая спрашивает человека от 18 лет и старше и говорит "Замечательно. Вы можете водить автомобиль», а в противоположном случае – «К соялению, водить автомобиль Вам рановато». (так вы можете сами подумать и добавить вывод сообщений в зависимости от возраста)
while True:
    age = int(input('enter your age: '))
    if age >= 18:
        print('you can drive')
    else:
        print('you cannot drive a car')

    text = input('do you wanna continue? Y/N\n').lower()

    if text == 'y':
        print('do you wanna continue')
    elif text == 'n':
        print('stopped')
        break
# 3) Создайте игру «Угадай число», программа генирирует рандомное число в заданном интервале, и предлагает пользователю угадать, игра продолжается до тех пор пока пользователь угадает число, пример игры на картинке ниже:
from random import randrange
import time

name = input('what is your name: ')
print(f"hello {name} lets play a game if you find you will win")
while True:
    user = int(input('enter the random number '))
    num = randrange(1, 5 + 1)
    if user == num:
        print('wow it is true')
        break
    else:
        print('your number is not found')



# 6) Нарисуйте ёлку (вид ёлки произвольный, на картинке только пример) , высоту ёлки должен задавать пользователь
a = int(input('enter the number '))
for size in range(3, a + 1):
    x = ' ' * (a - size)
    m = '*' * (2 * size - 1)
    print(x + m)
# 8) Задача «Лесенка» По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
stair = int(input('enter the number: '))
if 1 <= stair <= 9:
    for i in range(1, stair, +1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
