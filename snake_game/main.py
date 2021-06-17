from turtle import Screen, Turtle
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

turtle_list = []

for turtle_index in range(0, 3):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.goto(x=-20*turtle_index, y=0)
    turtle_list.append(new_turtle)

screen.update()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.5)

    # Moving a snake
    for turtle_num in range(len(turtle_list)-1, 0, -1):
        new_x = turtle_list[turtle_num - 1].xcor()
        new_y = turtle_list[turtle_num - 1].ycor()
        turtle_list[turtle_num].goto(new_x, new_y)
    turtle_list[0].fd(20)
    

screen.exitonclick()
