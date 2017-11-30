string=('Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies')
def most_frequent(y):
    dic={}
    t=[]
    for letter in y:
        dic[letter]=dic.get(letter,0)+1
    for key,value in dic.items():
        t.append((value,key))
        t.sort(reverse=True)
    return t
