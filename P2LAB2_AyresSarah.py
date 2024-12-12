# Sarah Ayres
#10-20-2024
#P2LAB@
#The assignment involves developing a program that gathers
#user inputs into a list and displays the followed by using that list to
#create visuals with the Turtle graphics library.



user_inputs = []

while True:
    user_input = input("Enter something (or type 'exit' to finish): ")
    if user_input.lower() == 'exit':
        break
    user_inputs.append(user_input)

print("You entered:")
for item in user_inputs:
    print(item)

import turtle
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(3)
t.pensize(5)

colors = ["BlueViolet", "coral2", "DarkSalmon", "DarkGray", "IndianRed4", "lavender", "firebrick3", "LightPink3"]


def draw_square():
    for color in colors[:4]:  
        t.pencolor(color)
        t.forward(100)
        t.right(90)


def draw_octagon():
    for i in range(8): 
        t.pencolor(colors[i % len(colors)])  
        t.forward(50)
        t.right(45)


def draw_circle():
    t.pencolor(colors[0])  
    t.circle(50)


def draw_rectangle():
    for color in colors[1:3]: 
        t.pencolor(color)
        t.forward(150)
        t.right(90)
        t.forward(75)
        t.right(90)


def draw_spiral():
    for i in range(50):
        t.pencolor(colors[i % len(colors)])  
        t.forward(i * 5)
        t.right(144)  





draw_square()
t.penup()
t.goto(-200, 0)  
t.pendown()
draw_octagon()
t.penup()
t.goto(200, 0)  
t.pendown()
draw_circle()
t.penup()
t.goto(-200, -200)  
t.pendown()
draw_rectangle()
t.penup()
t.goto(-230, 230)  # Adjust the position to the top left corner
t.pendown()
draw_spiral()


turtle.done()
