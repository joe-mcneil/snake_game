from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

game_run = True
snake = Snake()
food = Food()
score_board = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def snake_game():
    screen.update()
    while score_board.game_cont:
        # screen.onkey(None, "Return")
        screen.update()
        score_board.keep_score()
        time.sleep(0.15)
        snake.move()
        # Detect collision with food:
        if snake.head.distance(food) < 15:
            print("nom nom nom")
            food.refresh()
            score_board.score += 1
            snake.extend()
            score_board.keep_score()
        # Detect collision with wall:
        if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
            score_board.game_over()
        # Detect collision with tail:
        for segment in snake.segments[1:]:  # This slice excludes the snake head, which is obviously close to itself.
            if snake.head.distance(segment) < 10:
                score_board.game_over()

# We need a wrapper function so that we can reset the snake and set the game to continue again when the player hits "Enter".
def snake_game_reset():
    score_board.game_continue()
    snake.reset()

while game_run:
    snake_game()
    screen.onkey(snake_game_reset, "Return")

screen.exitonclick()
