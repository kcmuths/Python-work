##Program to find the cuberoot of a perfect cube

x = int(raw_input('Enter a number:'))
ans = 0
while ans*ans*ans < abs(x): ## absolute value is to eliminate negative values
    ans = ans + 1
    ##print 'current guess =', ans   ## to debug the code, print statement

if ans*ans*ans !=abs(x):
    print x, 'is not a perfect cube'
elif x < 0:
    print 'You entered a negative number'
    ans = -ans
print 'Cube root of ' + str(x) + ' is ' + str(ans)
 
