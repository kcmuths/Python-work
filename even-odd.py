x = int(raw_input('Enter a number:'))
if x%2 == 0:
    print 'Even'
else:
    print 'Odd'
    if x%3 != 0:
        print 'And not divisble by 3'
            
