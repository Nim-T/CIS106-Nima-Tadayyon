def compDiscount(Quantity,Price,DiscRate):
  Discount = DiscRate * 100
  DiscAmm = Quantity * Price * DiscRate
  DiscountedPrice = (Price - (Price * DiscRate)) * Quantity
  return Discount, DiscAmm, DiscountedPrice

def Main():
  run = input("Do you wanna run the program? (y/n): ").strip().upper()
  while run[0] == "Y":
    Quantity = int(input("Enter the item quantity: "))
    Price = float(input("Enter the individual item price: "))
    DiscRate = float(input("Enter the decimal discount rate (i.e. 20% -> 0.20): "))
    Discount, DiscAmm, DiscountedPrice = compDiscount(Quantity,Price,DiscRate)
    PreDisc = Quantity * Price
    print("================")
    print("You are purchasing:", Quantity,"items at ${:.2f}".format(Price)," per item with a discount of: {:.1f}%".format(Discount))
    print("\nTotal before discount: ${:.2f}".format(PreDisc))
    print("- Discounted ammount of: ${:.2f}".format(DiscAmm))
    print("Total after discount: ${:,.2f}".format(DiscountedPrice))
    print("================")
    run = input("\nDo you wanna run the program again? (y/n): ").strip().upper()
  else:
    print("\nThank you for using the program!")

Main()

