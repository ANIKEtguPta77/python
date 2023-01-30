from turtle import Turtle

class Score(Turtle):
    def __init__(self,cor):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(cor)
        self.update_board()
        
    def update_board(self):
        self.write(f"{self.score}",False,align='center',font=("Arial",68,"normal"))    
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",False,align='center',font=("Arial",14,"normal"))    
        
        
    def refresh(self):
        self.score+=1
        self.clear()
        self.update_board()
        
            
    
