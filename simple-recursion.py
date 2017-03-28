##Simple rrecursion to find b^n.
##b^n = B*B^n-1

def simpleExp(b,n):
    if n == 0:
        return 1
    else:
        return b * simpleExp(b, n-1)
    
##Tower Of hanoi problem

def Hanoi(n, f, t, s):
    ## n is size of stack(64), f is from-stack, t is to-stack, s is the spare stack 
    if n==1:
        print'move from ' + f + ' to ' + t
    else:
        Hanoi(n-1, f, s, t) ## move n-1 
        Hanoi(1, f, t, s)
        Hanoi(n-1, s, t, f)
        
