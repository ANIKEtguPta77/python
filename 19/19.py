from turtle import Turtle,Screen
tim=Turtle()


screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)
    
def clear():
    tim.clear()           



screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(clockwise,"Right")
screen.onkey(counter_clockwise,"Left")
screen.onkey(clear,'space')
screen.exitonclick()