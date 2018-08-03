# Final Exam
# Problem-2

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

# Note: in this problem you only need to worry about the lowercase characters and strings

# Build-in function ord and chr
# ord convert a character into an integer
# ord(c, /)
#    Return the Unicode code point for a one-character string.
# chr convert an integer back to a character
# chr(i, /)
#    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
# For example

test( ord('a') == 97 )
test( ord('b') == 98 )
test( ord('y') == 121 )
test( ord('z') == 122 )

test( 'a' == chr(97) )
test( 'b' == chr(98) )
test( 'y' == chr(121) )
test( 'z' == chr(122) )


# pb2-1
# Implement a function called inverse that gives you the mapping.

def inverse(c):
    return chr(219-ord(c))

test( inverse('a') == 'z' )
test( inverse('b') == 'y' )
test( inverse('y') == 'b' )
test( inverse('z') == 'a' )

# pb2-2
# Use inverse function above to create an inverse mapping dictionary called dic so that dic['a']=='z', dic['b']=='y', etc
dic=dict()
for i in range(97,122):
    dic[chr(i)]=inverse(chr(i))
test( dic['a'] == 'z' )
test( dic['k'] == 'p' )
test( dic['p'] == 'k' )

# pb2-3
# Implement a function called str_inversion that take a string as an argument and return a string with inverse characters.
# Hint: it might help to use str.join method.

def str_inversion(s):
    a=[]
    a.append('')
    for i in range(1,len(s)+1):
        
        a.append(a[i-1]+inverse(s[i-1]))
        
    return a[len(s)]
    
test( str_inversion('abcd') == 'zyxw')
test( str_inversion('zyxw') == 'abcd')
test( str_inversion('hello') == 'svool')
test( str_inversion('svool') == 'hello')
