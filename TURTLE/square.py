import turtle
a=turtle.Turtle()#turtle object
a.color('red')#turtle (line) color
b=turtle.Screen()
b.bgcolor('green')#background color

"""a.forward(100)
a.left(90)
a.forward(100)
a.left(90)

a.forward(100)
a.left(90)
a.forward(100)"""
a.speed(1)#0-fastest,1-slowest,3-slow,6-noraml,10-fast
a.begin_fill() 
a.fillcolor('yellow')
for i in range(4):
    a.forward(200)
    a.left(90)
a.hideturtle()#hide the turtle
a.end_fill()

