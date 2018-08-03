def check_fermat():
    a=int(input('a?'))
    b=int(input('b?'))
    c=int(input('c?'))
    n=int(input('n?'))





    
    if n>2 and pow(a,n)+pow(b,n)==pow(c,n):
        print('定理錯了');
    elif n==2:
        print('n要大於2,重來');
            
    else:
        print('定理沒錯');

  
            
