from turtle import Turtle
import random

tim = Turtle()

color = ["tomato","lime green","medium violet red","medium blue","yellow","deep pink"]
def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range (num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(color))
    draw_shape(shape_side_n)

