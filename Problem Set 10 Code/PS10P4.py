def TrainTicket(Miles):
  if Miles >= 30:
    Price = 12
  elif Miles >= 20:
    Price = 10
  elif Miles >= 10:
    Price = 8
  else:
    Price = 5
  return Price

def Main():
  sum = 0
  run = input("Do you want to run the program? (y/n) ")
  while run.upper() == "Y":
    Surname = input("Enter your surname: ")
    Miles = float(input("Distance from downtown Chicago in miles: "))
    Price = TrainTicket(Miles)
    sum = sum + Price
    print("Your ticket price will be ${:,.2f}".format(Price))
    run = input("\nDo you want to run the program again? (y/n) ")
  else:
    print("\n======================")
    print("The total price for all tickets is ${:,.2f}".format(sum))
    print("\n Thank you for using the program!")

Main()
    