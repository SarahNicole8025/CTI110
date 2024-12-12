# P3LAB1_Ayres
#11-10-24
# Drawing a triangle and square using for loops

import turtle

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)  

# Set up the turtle
turtle.speed(1)  

# Draw a triangle
turtle.penup()
turtle.goto(-100, 0
turtle.pendown()
draw_triangle(100)

# Move to a new position for the square
turtle.penup()
turtle.goto(50, 0)  
turtle.pendown()
draw_square(100)  

# Finish up
turtle.done()
