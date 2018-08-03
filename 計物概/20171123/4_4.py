#x從頭 y從尾來對 
def is_anagram(x,y):
    if not len(x)==len(y):
        return False
    for i in range(len(x)):
        print(x[i],y[len(y)-i-1])
        if x[i]==y[len(y)-i-1]:
            pass
        else:
            return False
    return True
    
