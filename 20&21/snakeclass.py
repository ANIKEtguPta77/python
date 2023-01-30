starting_positions=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
from turtle import Turtle,Screen
class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
        
    def createsnake(self):
        for i in range(3):
            segment=Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(starting_positions[i])
            self.segments.append(segment)
            
    def refresh(self):
        seg=Turtle("square")
        seg.color('white')
        seg.penup()
        self.segments.append(seg)
                
            
    def move(self):
      for segment_no in range(len(self.segments)-1,0,-1):
        xc=self.segments[segment_no-1].xcor()
        yc=self.segments[segment_no-1].ycor()
        self.segments[segment_no].goto(xc,yc)
      self.head.forward(MOVE_DISTANCE)    
               
               
    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
        
    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
        
    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
        
    def move_right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
            
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.createsnake()        
        self.head=self.segments[0]
            
            
        
        
                   
                   
        