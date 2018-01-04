# Final Exam
# Problem-1

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# pb1-1
# Implement a function call rev that takes a list and return the reversed list.
# Assume that the list is NOT nested.

def rev(list):
    k=[]
    for i in range(len(list)):
        k.append(list[len(list)-i-1])
    return k
        

test( rev([1,2,3,4,5]) == [5,4,3,2,1] )
test( rev(['a',2,'z',4,5]) == [5,4,'z',2,'a'] )

# pb1-2
# Implement a function call deep_rev that take a nested list and return the reversed list.
# The elements of the sub-list should also be reversed, as shown in the test.
# Hint: use recursion.

def deep_rev(x):
    k=[]
    for i in range(len(x)):
        if type(x[len(x)-i-1])==list:
            k.append(rev(x[len(x)-i-1]))

        else:
            k.append(x[len(x)-i-1])

    return k
    
        
    
test( deep_rev([1,2,3,4,5]) == [5,4,3,2,1] )
test( deep_rev([1, [2, 3], 4 ,5]) == [5,4,[3,2],1] )
test( deep_rev([1, [2, 3], [4 ,5]]) == [[5,4],[3,2],1] )
test( deep_rev([1, [2, [3, 4]]]) == [[[4,3],2],1])
