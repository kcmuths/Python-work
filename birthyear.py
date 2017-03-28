from datetime import date
name = raw_input('Enter your name:')
age = int(raw_input('Enter your age:'))
x = int(raw_input('Enter print message times:'))
soln = 100 - age
final_year = date.today().year + soln
for i in range(0, x):
    print 'You will be 100 years old in ' + str(final_year)
