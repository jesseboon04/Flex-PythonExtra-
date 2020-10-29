# Python program to draw 
# Spiral  Helix Pattern
# using Turtle Programming
 
import turtle
loadWindow = turtle.Screen()
turtle.speed(1)
turtle.bgcolor("black")
turtle.pencolor("#01FFF0")
turtle.fillcolor("white")
turtle.begin_fill()

 
for i in range(50):
    turtle.circle(3*i)
    turtle.circle(-3*i)
    turtle.left(i)
    turtle.right(i)
    turtle.circle(6*i)
    turtle.circle(-6*i)
    turtle.left(i)
    turtle.right(i)
    


turtle.exitonclick()
