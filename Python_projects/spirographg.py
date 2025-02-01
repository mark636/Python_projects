from turtle import Turtle, Screen
import random as rand

tim = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = rand.randint(0,255)
    g = rand.randint(0,255)
    b = rand.randint(0,255)
    color = (r,g,b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)


draw_spirograph(10)









screen.exitonclick()


