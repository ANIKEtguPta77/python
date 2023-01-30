from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.goto(0,0)
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1
        
    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx,newy)
        
    def bounce_with_wall(self):
        self.ymove*=-1       
      
    def bounce_with_paddle(self):
        self.xmove*=-1 
        self.move_speed*=0.9
        
    def reset(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_with_paddle()   