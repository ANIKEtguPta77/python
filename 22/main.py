from turtle import Turtle,Screen
from paddle import Paddle
import time
from ball import Ball
from score import Score

screen=Screen()
screen.screensize(800,600)
screen.bgcolor('black')
screen.tracer(0)


left_p=Paddle((-350,0))
right_p=Paddle((350,0))
ball=Ball()
left_score=Score((-50,240))
right_score=Score((50,240))

screen.listen()
screen.onkey(right_p.move_up,"Up")
screen.onkey(right_p.move_down,"Down")
screen.onkey(left_p.move_up,"w")
screen.onkey(left_p.move_down,"s")



is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_with_wall()
        
    #detect collision with right paddle
    if ball.distance(right_p)<50 and ball.xcor()>320:
        ball.bounce_with_paddle()
        
        
    #detecct collision with left paddle
    if ball.distance(left_p)<50 and ball.xcor()<-320:
        ball.bounce_with_paddle()
        
        
    #right paddle miss
    if ball.xcor()>380:
        left_score.refresh()
        ball.reset()
        
    #left paddle miss
    if ball.xcor()<-380:
        right_score.refresh()
        ball.reset()
        
        
        
        
        
          
        
        
        
        
          
            
            
            




















screen.exitonclick()