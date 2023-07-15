from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score = Scoreboard()

oberyn = Snake()
food = Food()
screen.listen()
screen.onkey(oberyn.up, "Up")
screen.onkey(oberyn.down, "Down")
screen.onkey(oberyn.left, "Left")
screen.onkey(oberyn.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    oberyn.move()

    if oberyn.head.distance(food) < 15:
        food.refresh()
        oberyn.extend()
        score.increase_score()

    if oberyn.head.xcor() > 290 or oberyn.head.xcor() < -290 or oberyn.head.ycor() > 290 or oberyn.head.ycor() < -290:
        game_on = False
        score.game_over()

    for segment in oberyn.segments:
        if segment == oberyn.head:
            pass
        elif oberyn.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
