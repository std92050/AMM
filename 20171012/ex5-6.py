import math
import turtle
A=turtle.Turtle()
def koch(turtle,x):
    turtle.fd(x/3)
    turtle.lt(60)
    turtle.fd(x/3)
    turtle.rt(120)
    turtle.fd(x/3)
    turtle.lt(60)
    turtle.fd(x/3)
def snowflake(turtle,x):
    for i in range(3):
        
    
        koch(turtle,x)

        turtle.lt(60)

        koch(turtle,x)
        
        turtle.rt(120)
        
        koch(turtle,x)

        turtle.lt(60)
        
        koch(turtle,x)

        turtle.rt(120)
        
