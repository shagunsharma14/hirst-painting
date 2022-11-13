import turtle
from turtle import Turtle, Screen
import random

# todo: To extract the color from the .jpg file
# import colorgram
# rgb_colors = []
# colors = colorgram.extract("R.jpg", 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_ls = [(214, 157, 85), (33, 105, 151),
            (238, 215, 94), (153, 75, 52), (125, 168, 199), (209, 134, 163)]
# todo: Hirt-Painting (Main)
# 1 PAINTING WITH 10X10 SPOTS
# 2 EACH DOT 20 IN SIZE AND SPACE AROUND 50


tim = Turtle()
# tim.penup()
# tim.hideturtle()
turtle.colormode(255)
tim.setheading(200)
tim.forward(500)
tim.setheading(0)
tim.speed(0)
number_of_dots = 100  # 10X10 box i.e 100 dots

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_ls))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.right(180)

screen = Screen()
screen.exitonclick()
