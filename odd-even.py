num = int(raw_input('Enter a number:'))
if num%2 ==0:
    print 'The number entered is even'
else:
    print 'The number is odd'
    if num%4 ==0:
        print 'Divisible by 4'
