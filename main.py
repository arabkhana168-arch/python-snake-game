from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake = Snake()
snake_food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")





game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(snake_food) < 15:
        snake_food.refresh()
        snake.extend()
        score.increase()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.colide()

    for seg in snake.segment[1:]:

        if snake.head.distance(seg) < 10:
           score.colide()
           game_on = False




























screen.exitonclick()