##perfect cube generalizing the solution (with the use of epilson) for sq. roots
## using exhaustive enumeration(brute force) algo. Later switch to binary
## to reduce the search space
x = 25
epilson = 0.01
numguesses = 0
ans = 0.0
while abs(ans**2 - x) >= epilson and ans <= x:
    ans +=0.001
    numguesses += 1
    print 'numguesses =', numguesses
if abs(ans**2 - x) >= epilson:
    print 'Failed on square root of', x
else:
    print ans, 'is close to square root of' + str(x)



    ##enumerator keeps running Needs to be stopped. and the prog
    ##ishighly ineffecient.
