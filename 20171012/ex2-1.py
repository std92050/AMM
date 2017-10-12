def check_fermat(a,b,c,n):
    if type(a)==int and type(b)==int and type(c)==int and type(n)==int:
        if n>2 and pow(a,n)+pow(b,n)==pow(c,n):
            print('定理錯了');
        elif n==2:
            print('n要大於2,重來');
            
        else:
            print('定理沒錯');
    else:
        print('給整數!');
