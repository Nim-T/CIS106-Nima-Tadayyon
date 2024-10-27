def AssessedValue(County,MarketValue):
  if County.upper() == "COOK":
    ValPercent = 0.90
  elif County.upper() == "DUPAGE":
    ValPercent = 0.80
  elif County.upper() == "MCHENRY":
    ValPercent = 0.75
  elif County.upper() == "KANE":
    ValPercent = 0.60
  else:
    ValPercent = 0.70
  ActualValue = MarketValue * ValPercent
  return ActualValue

def Main():
  sum = 0
  run = input("Do you want to run the program? (Y/N) ")
  while run.upper() == "Y":
    County = input("Enter the county: ")
    MarketValue = float(input("Enter the market value: "))
    ActualValue = AssessedValue(County,MarketValue)
    print("The assessed value is: ${:,.2f}".format(ActualValue))
    sum = sum + ActualValue
    run = input("Do you want to run the program again? (Y/N) ")
  else:
    print("================\n")
    print("The sum of all assessed values is: ${:,.2f}".format(sum))
    print("\nThank you for using the program!")

Main()
