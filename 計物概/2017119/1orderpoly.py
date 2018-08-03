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
    test(m(5, 3, 4, 2) == 1.0)
    test(m(1, 2, 3, 2) == 0.0)
    test(m(1, 2, 3, 3) == 0.5)
    test(m(2, 4, 2, 2) == 'explode')
    test(b(1, 6, 3, 12) == 3.0)
    test(b(1, 6, 1, 12) == 1)
    test(b(1, 2, 3, 6) == 0)
   
    pass
def m(x1,y1,x2,y2):
    if (x1-x2)==0:
        return "explode"
    return (y1-y2)/(x1-x2)

def b(x1,y1,x2,y2):
    if (x1-x2)==0:
        return x1
    return y1-((y1-y2)/(x1-x2))*x1
test_suite()
    
