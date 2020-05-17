import turtle
t=turtle.Turtle()
"""t.speed(0)
list1=['purple','green','blue','orange','red']
for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10)
    #t.forward(i)
    #t.left(59)
    #below code is mine
    if i<=100:
        
        t.circle(50,steps=8)
    else:
        t.forward(i)
        t.left(59)"""
t.bk(300)

t.left(270)
t.pensize(20)
t.forward(100)
#t.home()
t.backward(200)

t.left(360)
t.up()
t.circle(75,70)
t.down()
t.circle(75,290)
t.up()
t.forward(45)
t.down()

t.goto(-180,-90)
t.color('yellow')
t.up()
t.backward(90)
t.right(-90)
t.forward(50)


