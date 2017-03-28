##Fibonacci numbers

def fib(x):
    """assumes x an int >= 0 return Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x ==0 or x == 1: ##base cases
        return 1
    else:
        return fib(x-1) + fib(x-2) ## recursive statements

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))


##NOTES: if n gets close to infinity, ratio of fib(n)/fib(n-1) = 1+ sqrt(5/2)

##all flower petals are fibonacci numbers why??
        
        
    
