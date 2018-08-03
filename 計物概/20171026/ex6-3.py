def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
def is_palindrome(word):
    i = 0
    j = len(word)-1

    while j >= 0:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1

    return True
