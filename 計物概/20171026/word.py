import os
fin=open('tt.txt')
def no(word,no):
    for letter in word:
        if letter in no:
            return False
        if letter not in no:
            return True
        
        
