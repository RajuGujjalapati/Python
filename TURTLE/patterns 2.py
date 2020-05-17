"""import turtle
t=turtle.Turtle()
list1=['yellow','green','blue','orange']
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.begin_fill()
    t.fillcolor(list1[i])
    t.circle(150)
    t.end_fill()
    t.up()
    t.bk(100)"""
    
#2.
import turtle
t=turtle.Turtle()
list1=['yellow','green','blue','orange']
t.up()
t.goto(200,0)
for i in range(4):
    t.down()
    t.pensize(30)
    t.color(list1[i])
    t.circle(150)
   
    t.up()
    t.bk(100)
