from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.title("You are now a snake!")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

# Better make a tuple of the starting pos like this:
# start_pos = [(0, 0), (-20, 0), (-40, 0)]
# for pos in start_pos:
#     new_seg = Turtle("square")
#     new_seg.color("white")
#     new_seg.goto(pos)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.05)

    snake.move()

screen.exitonclick()
