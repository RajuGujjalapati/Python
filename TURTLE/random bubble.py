import random
from turtle import *
t=Turtle()
t.speed(0)
t.up()
colors=["blue","green","yellow","purple","skyblue","orange"]
while True:
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    circle_size=random.randint(1,100)
    circle_color=random.choice(colors)
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(circle_color)
    t.color(circle_color)
    
    t.circle(circle_size)
    t.end_fill()
    t.up()
