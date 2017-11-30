import string
dic={}
def read():
    
    wordd=open('word.txt')
    for line in wordd:
        for word in line.split():
            word=word.strip(string.punctuation)
            
            dic[word]=dic.get(word,0)
        
                
    
