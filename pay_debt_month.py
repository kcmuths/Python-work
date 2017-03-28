##Write a program that calculates the minimum fixed monthly payment needed in
##order pay off a credit card balance within 12 months. We will not be dealing
##with a minimum monthly payment rate.

##retrieve the input from user

initialBalance = float(raw_input('Enter the outstanding balance on your credit card:'))
interestRate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))

##Intialize state variables
monthlyPayment = 0
monthlyInterestRate = interestRate/12.0
balance = initialBalance

##Test increasing amount of monthlyPayment in increments of $100
##until it can be paid off in a year

while balance > 0:
    monthlyPayment += 10
    balance = initialBalance
    numMonths = 0

    ##Time until balance can be paid off

    while numMonths < 12 and balance > 0:
        numMonths += 1

        ##interest for the month
        interest = monthlyInterestRate * balance

        balance -= monthlyPayment

        balance += interest


#Round final balance to 2 decimal places
balance = round(balance,2)
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', monthlyPayment
print 'Number of months needed:', numMonths
print 'Balance:', balance
