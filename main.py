from turtle import Turtle, Screen
import random

WIDTH = 500
HEIGHT = 400
COLORS = ["red", "blue", "yellow", "black", "green", "orange", "purple"]
num_colors = len(COLORS)
GAP = 50
length_of_line = GAP*(num_colors-1)
CORD_START = WIDTH/(-2)+10
MAX_RANDOM = 10

screen = Screen()
screen.setup(WIDTH, HEIGHT)

user_bet = ""
while user_bet.lower() not in COLORS:
    user_bet = screen.textinput("Choose your bet", "What color is going to win? (Red, Blue, Yellow, Black, Green, "
                                                   "Orange, Purple)")
turtles = []
for i in range(0, num_colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(COLORS[i])
    new_turtle.penup()
    new_turtle.goto(x=CORD_START, y=length_of_line-length_of_line/2-GAP*i)
    turtles.append(new_turtle)

race_on = True
while race_on:
    for trt in turtles:
        next_move = random.randint(0, MAX_RANDOM)
        trt.forward(next_move)
    for trt in turtles:
        if trt.xcor() >= (WIDTH/2-10):
            race_on = False
            break

win_color = ""
max_dist = 0
for i in range(0, num_colors):
    if turtles[i].xcor() > max_dist:
        max_dist = turtles[i].xcor()
        win_color = COLORS[i]

if win_color == user_bet.lower():
    print("YOU WON")
else:
    print(f"YOU LOST. COLOR {win_color.upper()} WON")

screen.exitonclick()
