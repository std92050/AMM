import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(compass('N')=='E')
    test(compass('E')=='S')
    test(compass('idiot')==None)
   
    pass
def compass(u):
    compass1=['N','E','S','W']
    if u not in compass1:
        return None
    i=compass1.index(u)
    if i==3:
        return compass1[0]
    
    return compass1[i+1]

test_suite()

    
    
