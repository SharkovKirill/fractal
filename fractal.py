"""Case-study
Developers:
Sharkov (%), Ermolenko (%).
"""

from turtle import *
import time


def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)  # 1
        left(60)
        koch(order - 1, size / 3)
        right(120)
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)


def ice1(order, size):
    if order == 0:
        forward(size)  # 3
    else:
        ice1(order - 1, size / 2)
        left(120)
        ice1(order - 1, size / 4)
        right(180)
        ice1(order - 1, size / 4)
        left(120)
        ice1(order - 1, size / 4)
        right(180)
        ice1(order - 1, size / 4)
        left(120)
        ice1(order - 1, size / 2)


def snegice1(order, size):
    ice1(order, size)  # 5
    right(120)
    ice1(order, size)
    right(120)
    ice1(order, size)
    right(180)
    ice1(order, size)
    left(120)
    ice1(order, size)
    left(120)
    ice1(order, size)


def mink(order, size):
    if order == 0:
        forward(size)  # 7
    else:
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        left(90)
        mink(order - 1, size / 4)
        right(90)
        mink(order - 1, size / 4)


def tree(order, size):
    if order == 0:
        forward(size)  # 9test
    else:
        tree(order - 1, size)
        right(30)
        tree(order - 1, size * 2 / 3)
        left(180)
        tree(order - 1, size * 2 / 3)
        right(120)
        tree(order - 1, size * 2 / 3)
        left(180)
        tree(order - 1, size * 2 / 3)
        right(30)
        tree(order - 1, size)
        left(180)


# speed('fastest')
koch(1, 150)
time.sleep(5)


def main():
    up()
    goto(-100, 0)
    down()
    order = int(input('Глубина рекурсии:'))
    size = int(input('Длина стороны:'))
    fractal = int(input('1 - Кривая Коха, 2 - Снежинка Коха, 3 - Ледяной фрактал(1), 4 - Ледяной фрактал(2),'
                        '5 - Снежинка к л.ф.(1), 6 -Снежинка к л.ф.(2), 7 - Кривая Минковского,'
                        '8 - Кривая Леви, 9 - Двоичное дерево '))
    if fractal == 1:
        koch(order, size)
    elif fractal == 2:
        snegkoch(order, size)
    elif fractal == 3:
        ice1(order, size)
    elif fractal == 4:
        ice2(order, size)
    elif fractal == 5:
        snegice1(order, size)
    elif fractal == 6:
        snegice2(order, size)
    elif fractal == 7:
        mink(order, size)
    elif fractal == 8:
        levi(order, size)
    elif fractal == 9:
        tree(order, size)


#main()
