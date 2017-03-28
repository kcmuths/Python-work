## Cube root of perfect cube refined solution

x = int(raw_input('Enter an integer:'))
for ans in range(0, abs(x)+1):
## consider absolute value since negative vals are accepted
    if ans**3 == abs(x):
        break
if ans**3 != abs(x):
    print x, 'is not a perfect cube'
else:
    if x < 0:
        ans = -ans
    print 'Cube root of '+ str(x) + ' is ' + str(ans)
            
