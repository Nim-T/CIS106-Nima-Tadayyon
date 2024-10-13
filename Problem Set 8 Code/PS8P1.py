principle = float(input("Enter principle amount: "))
IntRate = float(input("Enter rate of interest (As a decimal): "))
term = int(input("Enter number of years: "))
StartingPrinciple = principle
print("Year\t Beginning Bal.\t Ending Bal.")
for years in range(1,term+1,1):
  Interest = principle * IntRate
  Balance = Interest + principle
  print(years, "\t\t", "${:,.2f}".format(principle), "\t", "${:,.2f}".format(Balance))
  principle = Balance
Earned = Balance - StartingPrinciple
print("Total Earned Interest: ", "${:,.2f}".format(Earned))