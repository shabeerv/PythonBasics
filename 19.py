# Income tax

tax = 0

income = int(input("Enter the annual income: "))

if income <= 200000:
    print("No tax for annual income up to 2.5 Lakhs.")
elif income <= 500000:
    tax = income*5/100
    print("Income tax amount = {0:.2f}(tax @ 5%)".format(tax))
elif income < 1000000:
    tax = income*20/100
    print("Income tax amount = {0:.2f}(tax @ 20%)".format(tax))
elif income <= 5000000:
    tax = income*30/100
    print("Income tax amount = {0:.2f}(tax @ 30%)".format(tax))
else:
    print("Please enter between a range from 2.5 Lakhs to 50 Lakhs!")
