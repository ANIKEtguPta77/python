colors=["blue","tomato","spring green","blue violet","bisque"]
import random
import turtle
tim=turtle.Turtle()
tim.speed('fastest')
tim.penup()
tim.setx(-250)
tim.sety(-240)

for j in range(10):
    for i in range(10):
        tim.pendown()  
        tim.dot(20,random.choice(colors))
        tim.penup()
        tim.forward(50)
    tim.setheading(90)  
    tim.forward(50)
    tim.left(90)
    tim.forward(500)  
    tim.left(180)
    












screen=turtle.Screen()
screen.exitonclick()