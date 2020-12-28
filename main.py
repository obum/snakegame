from turtle import Screen
import time
from scoreboard import ScoreBoard
from food import Food
from snake import Snake

# Screen setup --------------------------------------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

# Create Screen objects -----------------------------------------

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")
# screen.onkeypress(snake.stop, "space")

# Play game ------------------------------------------------
game_is_on = True
game_speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        game_speed -= 0.005
        time.sleep(game_speed)

    # Detect collision with wall

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 \
            or snake.head.ycor() < -285:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with tail
    for section in snake.snake_body:
        if section == snake.head:
            pass
        elif snake.head.distance(section) < 10:
            game_is_on = False
            scoreboard.game_over()
            pass

screen.exitonclick()
