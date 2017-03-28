##program to find the sum of digits that are in the year i.e 1+9+5+2

x = raw_input('Enter any number to calculate sum:')

sumDigits = 0
for c in str(x):
    sumDigits += int(c)
print sumDigits





##This is tuple in python. Have a look at the recitation class after
##machine interpretation



##x = 100
##divisors = ()
##for i in range (1,x):
##    if x%i == 0:
##        divisors = divisors+(i,)
##print divisors[0] + divisors[1]
##print divisors[2:4]
