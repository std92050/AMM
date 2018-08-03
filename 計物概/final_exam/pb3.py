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

# Pb4-1
# Implement Newton's method for finding roots.

# The method starts with a function f defined over the real numbers x,
# the function's derivative dfdx, and an initial guess x0 for a root of the function f.
# The process is repeated as
# x_{n+1} = x_n - f(x_n)/dfdx(x_n)
# You want to loop until a sufficiently accurate value is reached.
# Hint: control the accuracy by the variable tol

# Test your implementation with
# f1(x) = sin(x), x0 = 4.0
# f2(x) = x*x+3*x-10, x0 = 2.0

from math import *

def f1(x):
    return sin(x)

def dfdx1(x):
    return cos(x)

def f2(x):
    return x*x+3*x-10

def dfdx2(x):
    return 2*x+3

def Newton(f, dfdx, x):
    pass

tol = 1e-10
test( abs(Newton(f1,dfdx1,4)-pi) < tol )
test( abs(Newton(f2,dfdx2,3)-2.0) < tol )
