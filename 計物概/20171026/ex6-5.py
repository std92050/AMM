def gdc(a,b):
    while b!=0:
        x=a%b
        a=b
        b=x
    return a
