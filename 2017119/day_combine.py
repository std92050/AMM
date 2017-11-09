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
    test(day(0)=='sunday')
    test(day(2)=='sunday')
    test(day(0)=='87')
    test(day_inver("friday") == 5)
    test(day_inver("sunday") == 0)
    test(day_inver(day(3)) == 3)
    
    """ Run the suite of tests for code in this module (this file).
    """
    pass
def day(i):
    day1=['sunday','monday','tuesday','wednesday','thirsday','friday','saturday']
    if day1[1] not in day1:
        return None
    return day1[i]
  
def day_inver(u):
    day1=['sunday','monday','tuesday','wednesday','thirsday','friday','saturday']
    if u not in day1:
        return None
    return day1.index(u)

test_suite()
