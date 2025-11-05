import turtle


screen = turtle.Screen()
screen.bgcolor("pink")

t = turtle.Turtle()
t.speed(10)
t.pensize(5)
t.fillcolor('red')
t.pencolor('black')

t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()

t.hideturtle()
turtle.done



