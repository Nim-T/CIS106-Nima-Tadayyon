Item = input("Would you like to purchase item A or B?")
Quantity = int(input("How many would you like to purchase?"))
if(Item == "A"): UnitPrice = 10
else:UnitPrice = 20
ExtendedPrice = Quantity * UnitPrice
print("You are purchasing", Quantity, "of item", Item, "at a unit price of $", UnitPrice)
print("Your total will be: $", ExtendedPrice)