run = input("Would you like to run this program? (y/n): ")
DiscSum = 0
run = run.lower()
if run == "y":
  while True:
    Price = float(input("Enter item price: "))
    Quantity = int(input("Enter quantity you'd like to purchase: "))
    ExtPrice = Price * Quantity
    DiscRate = 0.25 if ExtPrice > 10000 else 0.1
    DiscAmnt = ExtPrice * DiscRate
    Total = ExtPrice - DiscAmnt
    DiscSum = DiscSum + DiscAmnt
    print("Your subtotal will be: ${:,.2f}".format(ExtPrice), "and your discount will be: ${:,.2f}".format(DiscAmnt))
    print("Totalling to: ${:,.2f}".format(Total))
    run = input("Would you like to run this program again? (y/n): ")
    run = run.lower()
    if run == "n":
      break
else: print("program stopped") + exit()
print("You saved a total of ${:,.2f}".format(DiscSum), "today! Have a nice day!")
  
    