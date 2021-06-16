from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Welcome to the turtle race!", prompt="Which turtle will you choose?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
# turtle_name = ["tim", "john", "justin", "Chris", "Dillon", "Nancy"]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.fillcolor(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + 40*turtle_index)
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.fillcolor()
            if winner == user_choice:
                print(f"You won! The {winner} turtle got this game!")
            else:
                print(f"You lost! The {winner} turtle got this game!")

        rand_speed = randint(0, 30)
        turtle.forward(rand_speed)

screen.exitonclick()
