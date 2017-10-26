import math
def mysqrt(a):
    x=10
    while True:
        
        y = (x + a/x) / 2
        if y == x:
            print('mysqrt=',x)
            print('math.sqrt=',math.sqrt(a))
            diff=math.sqrt(a)-x

            print('diff is',diff)
            
            break
            
        x = y
        
print('mysqrt='+mysqrt(a))
print('math.sqrt='+math.sqrt(a))
diff=math.sqrt(a)-mysqrt(a)

print('diff is'+diff)
