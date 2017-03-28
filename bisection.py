## perfect cube using bisection search
x = 0.5
epsilon = 0.01
##numguesses = 0
low = 0.0
high = max(x, 1.0)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    print 'ans =', ans, 'low =', low, 'high =', high
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
#print 'numguesses', numguesses
print ans, 'is close to square root of', x


## program didn't run well. Needed debugging
##DEBUG: Use print statements to do so (specifically below while loop
            
