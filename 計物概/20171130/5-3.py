lists=['sfe',87,77,'add','fe']
def has_duplicates(m):
    dic={}
    for x in m:
        dic[x]=dic.get(x,0)+1
        if dic[x]>1:
            return True
has_duplicates(lists)
            
    
