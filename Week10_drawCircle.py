import turtle
import math

def drawCircle(t, x, y, r):
    distance = 2.0 * 3.14 * r /120
    t.up()
    t.goto(x, y)
    t.down()
    for count in range(120):
        t.right(3)
        t.forward(distance)
new = turtle.Turtle()
drawCircle(new, 0, 0, 50)
        
    
