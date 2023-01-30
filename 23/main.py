import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1=Player()
car=CarManager()
score=Scoreboard()


screen.listen()
screen.onkey(player1.move_up,"Up")
screen.onkey(player1.move_left,"Left")
screen.onkey(player1.move_right,"Right")
screen.onkey(player1.move_back,"Down")





game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    
    #detect collision with cars
    for cars in car.all_cars:
        if abs(cars.xcor()-player1.xcor())<20 and abs(cars.ycor()-player1.ycor())<20 :
            score.game_over()
            game_is_on=False
        
        
    #for levelup
    if player1.is_at_finish_line():
        score.refresh()
        player1.reset()
        car.level_up()
            
            
            









screen.exitonclick()