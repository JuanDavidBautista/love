import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
t.speed(1)
t.hideturtle()
t.goto(0,-50)

t.pensize(5)
t.color("red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-100,100)
t.pendown
t.color("white")
t.write("Te amooo cansona", font=("Verdana",15,"bold"))

t.penup()
t.goto(-20,50)
t.pendown()
t.color("white")
t.write("pikos <3", font=("Verdana",10,"bold"))

turtle.done()


