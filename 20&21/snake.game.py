from turtle import Turtle,Screen
import time
from snakeclass import Snake
from food import Food
from score_board import Score

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
score=Score()





screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
    #detect collision with food
    if snake.head.distance(food)<25:
        food.refresh()    
        score.refresh()
        snake.refresh()
        
        
    #detect collison with wall    
    if snake.head.xcor()>290 or  snake.head.xcor()<-290  or snake.head.ycor()>290 or snake.head.ycor()<-290:
        
        score.reset() 
        snake.reset()


    #detect collision with snake
    for segment in snake.segments[1::]:
        # if segment==snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            
            score.reset()   
            snake.reset()     

















screen.exitonclick()