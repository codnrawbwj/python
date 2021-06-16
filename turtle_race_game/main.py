from turtle import Turtle, Screen

# Name of the turtle is john
john = Turtle()
screen = Screen()


def turtle_forward():
    john.forward(10)


def turtle_backward():
    john.bk(10)


def counter_clkwise():
    john.left(10)


def clkwise():
    john.right(10)


def clear_screen():
    john.reset()


screen.listen()
screen.onkey(key="w", fun=turtle_forward)
screen.onkey(key="s", fun=turtle_backward)
screen.onkey(key="a", fun=counter_clkwise)
screen.onkey(key="d", fun=clkwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
