def cum(n):
    m=[]
    for i in range(len(n)+1):
        m.append(sum(n[0:i]))
    return m
            
