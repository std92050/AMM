import turtle
t=turtle.Turtle()

a=0.1
b=0.0002

def sp(ds):
    d=0
    while d<3600:
        t.fd(ds)
        dd=ds/(a+b*d)
        t.lt(dd)
        d+=dd
