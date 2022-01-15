import turtle
import math
a=turtle.Turtle()
def c(n,l):
    for i in range(n):
        a.fd(l)
        a.lt(180-(360/n))
        a.fd(l)
        a.rt(180)

    a.lt((180-(360/n))/2)
    
    for i in range(n):
        a.fd(2*l*math.cos((math.pi-(2*math.pi/n))/2))
        
        
        a.rt((360/n))

   
