from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=500)

User_bet = screen.textinput(title="Make your Bet", prompt="which turtle will win the race? Enter a color: ")

colors = ["red","orange","yellow","green","blue","purple" ]

y_positions = [-70,-40,-10,20,50,80]

all_turtles= []

for turtle_index in range(0,6):     
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[turtle_index])
    all_turtles.append(new_turtle)

if User_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.pencolor()
            if winning == User_bet:
                print("You win")
            else:
                print("YOU LOSE :(")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()