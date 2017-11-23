#複製一個a的list叫a0 每一個a0的元素都做一個計數器 計數器>1就TRUE
def has_duplicates(a):
    a0=[]
    
    for i in a:
        a0.append(i)
    for i in a0:
        count=0
        for j in a:
            if i==j:
                count=count+1
            else:
                pass
        if count>1:
            return True
        
