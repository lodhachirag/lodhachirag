import turtle as t
import time
import snake as snake
import food as food
from scoreboard import Scoreboard


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
screen.listen()
snake = snake.snake()
food = food.Food()
scoreboard = Scoreboard()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.Score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.Gameover()

    for segment in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.Gameover()


screen.exitonclick()