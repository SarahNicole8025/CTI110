#CTI110
#Sarah Ayres
#9/26/2024
#https://www.geeksforgeeks.org/print-a-spirograph-using-turtle-in-python/
import turtle as tt
tt.bgcolor('black')
tt.pensize(2)
tt.speed(30)
for i in range(6):
     for color in ('red','pink','blue','cyan','green','gray','purple'):
         tt.color(color)
         tt.circle(100)
         tt.left(10)
         tt.hideturtle()
