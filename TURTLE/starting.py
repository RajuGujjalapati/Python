import turtle
turtle.colormode(255)#by default it will be '1' now.
#turtle.colormode()#gets the present color mode.
#we can set the code from '0' to '255'
raj = turtle.Turtle()#object for turtle
raj.shape("turtle")
raj.shape("circle")
raj.shape("square")
raj.shape("triangle")
raj.forward(100)
raj.color("red")
raj.forward(200)
raj.color("blue","green")
raj.shape("turtle")
raj.backward(300)
raj.color(200,200,100)
bujji=turtle.Screen()#creating screen object
bujji.bgcolor('red')
bujji.bgcolor(140,50,40)#RGB
bujji.title("NANI GRAPHICS")
bujji.bgpic("nani.gif")


