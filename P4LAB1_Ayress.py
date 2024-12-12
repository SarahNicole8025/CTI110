# CTI 110
# P4LAB1 - Turtle
#Ayress
#11-12-24

#Draw shapes and snowflakes using for loops

#Set up the turtle
import turtle
t = turtle.Turtle()

#add some diplay options
t.pensize(4)
t.pencolor("orange")
t.shape("turtle")

#Triangle
for side in range (20):
    t. forward (100)
    t.right (105)
    
t.pencolor("darkgray")
# Trippy Triangle
for side in range (30):
    t.backward(200)
    t.left(140)

#square
t.right(50)
t.pencolor("cadetblue4")
for side in range(4):
    t.forward(100)
    t.left(90)
    
#Snowflake
t.pencolor("lightblue")
for flake in range(40):
    t.backward(90)
    t.left(30)
    t.forward(90)
    t.right(30)
