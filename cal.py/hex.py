import turtle

turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0)


for i in range(100):
    for colours in ["red","magenta","blue","cyan","green","yellow"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()