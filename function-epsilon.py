def withinEpsilon(x, y, epsilon):
    """x,y,epsilon floats. epsilon > 0.0
    returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon

##print withinEpsilon(2,3,1)
##val = withinEpsilon(2,3,0.5)
##print val

##def f(x):
##    x = x + 1
##    print 'x=', x
##    return x
##x = 3
##z = f(x)
##print 'z =', z
##print 'x =', x


##NOTE: now in the withinEpsilon function, if there is no return statement
##(or is return is commented out) none would be printed.

def f1(x):
    def g():
        x = 'abc'
        ##assert False ## assert is a command where assert is followed by
        ##either true or false. If it evaluates to true, it continues
        ## if it evaluates to False, it stops the program dead.
    x = x + 1
    print 'x=', x
    g()
    assert false
    return x
x = 3
z = f1(x)

##NOTE: debug by looking at stack frames
