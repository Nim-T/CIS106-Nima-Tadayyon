Principle = float(input("Please enter principle amount: "))
YtM = int(input("Please enter years to maturity: "))
if Principle > 100000 and YtM == 5: InterestRate = 0.06
elif Principle >= 50000 and YtM == 10: InterestRate = 0.05
elif Principle >= 50000 and YtM == 5: InterestRate = 0.04
else: InterestRate = 0.02
FirstYear = Principle * InterestRate
print("With a principle investment of: ${:,.2f}".format(Principle))
print("and", YtM, "years to maturity, your interest rate will be: ", InterestRate * 100,"%")
print("Making your interest amount for the first year: ${:,.2f}".format(FirstYear))