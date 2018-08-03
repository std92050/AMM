def nested(m):
    
    for i in m:
        if type(i)==list:
            nested(i)
            v=sum(i)
            m.remove(i)
            m.append(v)
    return sum(m)
        

