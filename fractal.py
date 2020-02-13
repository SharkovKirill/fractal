from turtle import *
import time
def koch(order, size):
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)                   #1
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)

def ice1(order, size):
    if order == 0:
        forward(size)                                #3
    else:
        ice1(order-1,size/2)
        left(120)
        ice1(order-1,size/4)
        right(180)
        ice1(order - 1, size / 4)
        left(120)
        ice1(order - 1, size / 4)
        right(180)
        ice1(order - 1, size / 4)
        left(120)
        ice1(order - 1, size / 2)

def cnegice1(order,size):
    ice1(order,size)                        #5
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
        forward(size)                                   #7
    else:
        mink(order-1, size/4)
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
        forward(size)                   #9test
    else:
        tree(order-1, size)
        right(30)
        tree(order-1, size*2/3)
        left(180)
        tree(order - 1, size * 2 / 3)
        right(120)
        tree(order - 1, size * 2 / 3)
        left(180)
        tree(order - 1, size * 2 / 3)
        right(30)
        tree(order - 1, size)
        left(180)


left(90)
#speed('fastest')
tree(2,150)
time.sleep(5)
