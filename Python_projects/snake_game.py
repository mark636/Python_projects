from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_on = True
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        #Detect collison with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_on = False
            score.game_over()

        #Detect collison with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score.game_over()
   

screen.exitonclick()

