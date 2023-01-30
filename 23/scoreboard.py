FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-240,260)
        self.update_board()
        
    def update_board(self):
        self.write(f"LEVEL :{self.level}",False,align='center',font=("Arial",14,"normal"))    
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",False,align='center',font=("Arial",14,"normal"))    
        
        
    def refresh(self):
        self.level+=1
        self.clear()
        self.update_board()
    
