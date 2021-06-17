from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.set_up()
        self.head = self.turtle_list[0]

    def set_up(self):
        for turtle_index in range(0, 3):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(x=-20 * turtle_index, y=0)
            self.turtle_list.append(new_turtle)

    def move(self):
        for turtle_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[turtle_num - 1].xcor()
            new_y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
