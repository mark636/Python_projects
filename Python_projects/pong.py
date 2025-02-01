from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
import time 
from scoreboard_pong import Scoreboard

score = Scoreboard()
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.ball_reverse_r()
        
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.ball_reverse_r()

    if ball.xcor() > 350:
        ball.reset_position()
        score.increase_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r()
        

screen.exitonclick()