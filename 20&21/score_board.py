from turtle import Turtle
with open("D:\\python\\udemy\\20&21\\data.txt") as f:
    content=f.read()
    



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=int(content)
        self.penup()
        self.goto(0,280)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}",False,align='center',font=("Arial",14,"normal"))
            
    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        
        
        if self.high_score>int(content):
            with open("D:\\python\\udemy\\20&21\\data.txt",mode="w") as g:
                g.write(str(self.high_score))
                
        self.update_scoreboard()    
        
    def refresh(self):
        self.score+=1

        self.update_scoreboard()   