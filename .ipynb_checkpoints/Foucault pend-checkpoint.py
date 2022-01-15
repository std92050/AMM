
import turtle
import numpy as np



pend=turtle.Turtle()
w_0=1.656
w_z=2.9*10**(-5)
dt=0.001
t=0

for i in range(4320000):
    dx=dt*100*(-1*w_0*np.sin(w_0*t)*np.cos(w_z*t)-w_z*np.cos(w_0*t)*np.sin(w_z*t))
    dy=dt*100*(w_0*np.sin(w_0*t)*np.cos(w_z*t)-w_z*np.cos(w_0*t)*np.cos(w_z*t))
    pend.fd(dx)
    pend.lt(np.sign(dx)*90)
    pend.fd(dy)
    pend.rt(np.sign(dy)*90)
    t=t+dt
