from turtle import Turtle


class Snake:
    def __init__(self):
        turtle_list = []

    def set_up(self):
        for turtle_index in range(0, 3):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(x=-20 * turtle_index, y=0)
            self.turtle_list.append(new_turtle)

    def move(self, turtle_list):
        for turtle_num in range(len(turtle_list) - 1, 0, -1):
            new_x = turtle_list[turtle_num - 1].xcor()
            new_y = turtle_list[turtle_num - 1].ycor()
            turtle_list[turtle_num].goto(new_x, new_y)
        turtle_list[0].fd(20)
