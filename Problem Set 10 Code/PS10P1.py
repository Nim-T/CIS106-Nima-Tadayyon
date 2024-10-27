def ForecastPercent(Month, Sales):
  if Month.upper() in ["JAN", "FEB", "MAR"]:
    Percent = 0.10
  elif Month.upper() in ["APR", "MAY", "JUN"]:
    Percent = 0.15
  elif Month.upper() in ["JUL", "AUG", "SEP"]:
    Percent = 0.20
  elif Month.upper() in ["OCT", "NOV", "DEC"]:
    Percent = 0.25
  else:
    print("Error, invalid month. forecast will be set to 0. \n")
    Sales = 0
    Percent = 0
  Forecast = Sales * (1 + Percent)
  return Forecast

def Main():
  run = input("would you like to run the program? (y/n): ")
  while run.upper() == "Y":
    Surname = input("Please enter your last name: ")
    Month = input("Please enter the month: ")
    Sales = float(input("Please enter sales made this month: "))
    Forecast = ForecastPercent(Month, Sales)
    print("Since you made: ${:,.2f} in sales this month. Your forecast for next month is: ${:,.2f}".format(Sales, Forecast))
    run = input("would you like to run the program again? (y/n): ")
  else:
    print("Thank you for using the program.")
    
Main()