from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.updated_score()
        self.l_score = 0
        self.r_score = 0 
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=("Courier", 80 , "normal"))
        
    def updated_score(self):
         self.write(f"Score: {self.score}",align="center",font=("Arial", 24 , "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial", 24 , "normal"))
   
    def increase_score(self):
        self.score +=1
        self.clear()
        self.updated_score()