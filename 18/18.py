import turtle as t
import random

colors=["blue","tomato","spring green","blue violet","bisque"]
# jim=Turtle()
# jim.shape('turtle')
# jim.color('blue')
# jim.forward(100)
# jim.left(90)
# jim.forward(100)
# jim.left(90)
# jim.forward(100)
# jim.left(90)
# jim.forward(100)
tim=t.Turtle()
# tim.penup()
# tim.goto(-200,30)
# for i in range(0,16):
    
#     tim.fd(20)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()

hi=t.Turtle()
# for i in range(3,11):
#     for j in range(0,i):
#         hi.colormode(255)
#         hi.fd(100)
#         hi.right(360/i)


r=t.Turtle()
# t.colormode(255)

# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     t=(r,g,b)
#     return t
    
# direction=[0,90,180,270]
# r.pensize(10)
# r.speed('fastest')
# for i in range(200):
#     color=random_color()
#     r.pencolor(color)
#     r.forward(30)
#     r.setheading(random.choice(direction))



s=t.Turtle()
s.speed('fastest')

t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t=(r,g,b)
    return t

for i in range(100):
    s.color(random_color())
    s.circle(100)
    current_heading=s.heading()
    s.setheading(current_heading+5)

























screen=t.Screen()
screen.exitonclick()