from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('green')
        self.shapesize(0.5,0.5)
        self.speed('fastest')
        self.penup()
        self.refresh()
        
    def refresh(self):
         self.goto(random.randint(-280,280),random.randint(-280,280))   