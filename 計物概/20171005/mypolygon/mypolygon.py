import turtle;
import math;
nthu=turtle.Turtle()
def mm(r,n,d):
    """半徑   弧角/// 可畫圓,多邊或弧長 d=360,n很大時化圓 """
    for i in range(n):
        nthu.fd(2*math.pi*r/n);
        nthu.lt(d/n);
        
def f(n,m,r):
    '''m=花瓣片數'''
    for i in range(2*m):
        d=360/m
        mm(r,n,d)
        nthu.lt(180-d);
        
    
