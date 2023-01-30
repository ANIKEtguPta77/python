from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,cor):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5,1,None)
        self.penup()
        self.goto(cor)
        
        
    def move_up(self):
        newy=self.ycor()+20
        self.goto(self.xcor(),newy)
        
    def move_down(self):
        newy=self.ycor()-20
        self.goto(self.xcor(),newy)  
           
                