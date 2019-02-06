from turtle import *
from random import randint
speed(0)
penup()
goto(-140,140)

player1=input("enter your color:")
player2=input("enter your color:")

for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color(player1)
ada.shape('turtle')

ada.penup()
ada.goto(-160,120)
ada.pendown()

bob = Turtle()
bob.color(player2)
bob.shape('turtle')

bob.penup()
bob.goto(-160,100)
bob.pendown()

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
