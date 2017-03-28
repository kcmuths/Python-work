##Write a program to calculate the credit card balance after one year if a person
##only pays the minimum monthly payment required by the credit card company
##each month
##Use raw_input() to ask for the following three floating numbers:
##1. the outstanding balance on the credit card
##2. annual interest rate
##3. minimum monthly payment rate
##For each month print the minimum monthly payment, remaining balance,
##principle paid in the format shown in test cases. All numbers should be
##rounded to the nearest penny.
##Finally, print the result, which should include the total amount paid that year
##and the remaining balance.





outstanding_bal = float(raw_input('Enter your outstanding balance on credit card:'))
annual_interest_rate = float(raw_input('Enter annual interest rate as a decimal:'))
min_monthly_payment_rate = float(raw_input('Enter minimum monthly payment rateas a decimal:'))
total_amt_paid = 0
for i in range(1,13):

    minimum_monthly_payment = min_monthly_payment_rate * outstanding_bal
    interest_paid = annual_interest_rate / 12 * outstanding_bal
    principal_paid = minimum_monthly_payment - interest_paid
    remaining_balance = outstanding_bal - principal_paid
    print 'Month:', i
    print 'Minimum monthly payment:$',round(minimum_monthly_payment, 2)
    print 'Principle paid:$',round(principal_paid, 2)
    print 'Remaining balance:$',round(remaining_balance, 2)
    outstanding_bal = remaining_balance
    total_amt_paid += minimum_monthly_payment
print 'RESULT'
print 'Total amount paid: $',round(total_amt_paid, 2)
print 'remaining balance: $',round(outstanding_bal, 2)

    
    
