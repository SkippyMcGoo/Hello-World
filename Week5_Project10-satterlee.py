import math

purchasePrice = float(input("Please enter the price of the purchase: "))

balance = 0.9 * purchasePrice
monthlyPayment = 0.05 * balance
annualRate = 0.12
monthlyRate = annualRate / 12

monthlyPayment = purchasePrice * .05
print("Starting balance (purchase price minus down payment)", balance)
print("{: <10}{: <10}{: <10}{: <10}{: <10}{: <10}".format("Month","Balance","Interest","Principal","Payment","Remaining"))
monthCounter = 1
while balance > 0:
    if (monthlyPayment > balance):
        monthlyPayment = balance
        monthlyInterest = 0
    else:
        monthlyInterest = balance * monthlyRate

    principal = monthlyPayment - monthlyInterest
    remaining = balance - principal
    
    print("{: <10}{: <10.2f}{: <10.2f}{: <10.2f}{: <10.2f}{: <10.2f}".format(monthCounter, balance, monthlyInterest, principal, monthlyPayment, remaining))
    
    monthCounter += 1
    balance = remaining

    
print("End")

    
