from turtle import Turtle, Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        # Create a Snake Body
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        square = Turtle(shape="circle")
        square.penup()
        square.color("white")
        square.shapesize(stretch_wid=1, stretch_len=1)
        square.goto(position)
        self.snake_body.append(square)

    # Extend snake --------------------------------------------------------------
    def extend(self):
        # Add new squares to the snake body
        self.add_square(self.snake_body[-1].position())

    # Move Snake ----------------------------------------------------------------
    def move(self):
        for square_no in range(len(self.snake_body) - 1, 0, -1):
            new_x_position = self.snake_body[square_no - 1].xcor()
            new_y_position = self.snake_body[square_no - 1].ycor()
            self.snake_body[square_no].goto(new_x_position, new_y_position)
        self.head.fd(20)

    # Control Snake --------------------------------------------------------------

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    # def stop(self):
    #     screen = Screen()
    #     screen.exitonclick()
