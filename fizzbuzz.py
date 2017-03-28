##Write a program that prints the numbers from 1 to 100.
##But for multiples of three print 'Fizz'instead of the number and
##for the multiples of five print 'Buzz'. For multiples of both the numbers,
##print 'fizzBuzz'

for i in range(1,101):
    s = str(i)  ## get string value of number. i.e s = '1'
    if i % 3 == 0 or i % 5 == 0:
        s = ''
        if i % 3 == 0:
            s = s + 'Fizz'
        if i % 5 == 0:
            s = s + 'Buzz'
    print s
