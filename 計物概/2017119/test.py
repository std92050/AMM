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
    test(abs(-99)==99)
    test(abs(0)==0)
    test(abs(-0.633)==0.633)
    test(abs(-0.633)==663)
   
    pass


def abs(n):
    if n>0:
        return n
    elif n<0:
        return -1*n
    else:
        return 0
        
        
    
