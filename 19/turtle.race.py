from turtle import Turtle,Screen
import random
is_race_on=False
colors=["blue","tomato","spring green","blue violet","bisque","tomato"]
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color")
y_p=[-70,-40,-10,20,50,80]
all_turtle=[]

for turtle_index in range(0,6):
    tim=Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_p[turtle_index])
    all_turtle.append(tim)


if user_bet:
    is_race_on=True
    
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            is_race_on=False
            if winning_color==user_bet:
                print("You have won !!")
            else:
                print("You lose")    
        rand_dis=random.randint(0,11)
        turtle.forward(rand_dis)
    















screen.exitonclick()