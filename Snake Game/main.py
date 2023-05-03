from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snakes")
screen.tracer(0)

snake = Snake()    
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    
    #Food collision detection
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increment_score()
        food.refresh()
        
    #Wall collision detection
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
         game_is_on = False
         scoreboard.game_over()
    
    0#Tail colossion detection
    for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    
        
screen.exitonclick()