import turtle

turnaround = 180
#Big X
for i in range(4):
    turtle.right(90)
    turtle.forward(250)
    turtle.circle(20)
    turtle.left(turnaround)
    turtle.circle(20)
    turtle.left(90)
    turtle.circle(20)
    turtle.right(90)
    turtle.forward(250)    
#Small X
for i in range(12):
    turtle.right(50)
    turtle.forward(170)
    turtle.circle(5) #FIrst circle at end(change color to red and fill)
    turtle.right(turnaround)
    turtle.forward(170)
    turtle.circle(5) # Little circle in middle(Change color to red and fill)
    turtle.forward(170)
    turtle.circle(5) # Second circle at end (Change color to red and fill)
    turtle.right(turnaround)
    turtle.forward(170)
    turtle.right(90)
    turtle.right(25)
    turtle.circle(10) # Big circle in middle (change color to green and fill)
    
    
    
  
    
    
