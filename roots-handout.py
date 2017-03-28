##to find roots

def withinEpsilon(x, y, epsilon):
    """x,y,epsilon floats. epsilon > 0.0
    returns True if x is within epsilon of y"""
    return abs(x - y) <= epsilon


def isEven(i):
    """assumes i is a positive int
       returns true is i is even, otherwise False"""
    return i%2 == 0

def findRoot(pwr, val, epsilon):
    """assumes pwr as an int; val, epsilon floats
    pwr and epsilon > 0
    if it exists,
    returns a value within epsilon of val**pwr
    otherwise returns none"""
    assert type(pwr) == int and type(val) == float\
           and type(epsilon) == float
    assert pwr > 0 and epsilon > 0
    if isEven(pwr) and val < 0:
        return None
    low = -abs(val)
    high = max(abs(val), 1.0)
    ans = (high + low)/2.0
    while not withinEpsilon(ans**pwr, val, epsilon):
        #print 'ans=', ans...
        if ans**pwr < val:
            low = ans
        else:
            high = ans
            ans = (high + low)/2.0
    return ans

def testRindRoot():
    """x is float, epsilon float, pwr positive int"""
    for x in (-1.0, 1.0, 3456.0):
        for pwr in (1,2,3):
            ans = findRoot(pwr, x, 0.001)
            if ans ==None:
                print'The answer is imaginary'
            else: print ans, 'to the power', pwr,'is close to', x
        
    
