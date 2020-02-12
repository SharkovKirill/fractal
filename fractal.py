from turtle import *
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

ice1(3,250)