Quantity = int(input("Enter quantity of item you'd like to purchase:"))
UnitPrice = 3.0 if Quantity >= 1000 else 5.0
ExtendedPrice = Quantity * UnitPrice
Tax = ExtendedPrice * 0.07
ActualPrice = ExtendedPrice + Tax
print("With a quantity of: " + str(Quantity) + " The price per unit is: $" + str(UnitPrice))
print(". Total before Tax: $" + str(ExtendedPrice) + ", Tax: $" + str(Tax))
print("Acutal Price: $" + str(ActualPrice))