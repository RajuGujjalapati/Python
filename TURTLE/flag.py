import turtle

def rect(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)#or use setheading (270)
        t.forward(100)
        t.right(90)
    t.end_fill()
t=turtle.Turtle()
#t.speed(0)
t.pensize(3)
t.up()
t.goto(0,-600)
t.down()
t.goto(0,300)#orange range
rect('#FF9933')#FF9933
t.goto(0,200)#blue circle range
t.forward(200)
t.color("blue")#000088
t.circle(-50)
t.setheading(270)
t.forward(50)
t.setheading(0)
for i in range(24):
    t.forward(45)
    t.backward(45)
    t.left(15)
t.setheading(90)
t.forward(50)
#t.setheading(180)
#t.forward(200)
t.setheading(0)
t.color("black")
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.goto(0,100)#green range
rect('green')#128807

def cord(coo):
        t.begin_fill()
        t.fillcolor(coo)
        t.circle(10,steps=9)
        t.end_fill()
t.up()        
t.goto(200,150)
t.down()
cord("yellow")
t.up()
t.goto(100,140)
t.down()
cord("green")
t.up()        
t.goto(190,130)
t.down()
cord("skyblue")
t.up()        
t.goto(180,190)
t.down()
cord("blue")
t.up()        
t.goto(150,150)
t.down()
cord("yellow")
t.up()        
t.goto(280,175)
t.down()
cord("green")
t.hideturtle()



