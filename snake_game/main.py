from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
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
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detect collision w/ food.
    if snake.head.distance(food) < 5:
        food.refresh()
        scoreboard.get_score()
        snake.extend()

    # Detect collision w/ wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision w/ its own tail.
    # for tail_index in range(len(snake.turtle_list), 2, -1):
    #     if snake.head.position() == snake.turtle_list[tail_index-1].position():
    #         is_game_on = False
    #         scoreboard.game_over()

    for tail in snake.turtle_list[1:]:
        if snake.head.position() == tail.position():
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
