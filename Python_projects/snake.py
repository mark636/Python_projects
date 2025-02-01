from turtle import Turtle

# Define constants
SETUP_POS = [(0, 0), (-20, 0), (-40, 0)]  
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  

    def create_snake(self):
        
        for position in SETUP_POS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake at the specified position."""
        seg = Turtle(shape="square")
        seg.color("light green")
        seg.penup()
        seg.goto(position)  
        self.segments.append(seg)

    def extend(self):
        """Extend the snake by adding a new segment at the position of the last segment."""
        last_position = self.segments[-1].position()  
        self.add_segment(last_position)  

    def move(self):
        """Move the snake by shifting each segment to the position of the one ahead."""
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        """Change the snake's direction to up, unless it's currently heading down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down, unless it's currently heading up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left, unless it's currently heading right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right, unless it's currently heading left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
