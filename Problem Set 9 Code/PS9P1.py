def Ext_Price(Price, Quantity):
  Ext_Price = Price * Quantity
  if Ext_Price > 10000:
      Discount = Ext_Price * 0.1
  else: Discount = 0
  Actual_Price = Ext_Price - Discount
  return Actual_Price
def main():
  totalactprice = 0
  response = input("Do you want to calculate the total order price? (Y/N): ")
  while response.upper() == "Y":
    Price = float(input("Enter the price of the item: "))
    Quantity = int(input("Enter the quantity of the item: "))
    Actual_Price = Ext_Price(Price, Quantity)
    print("You are purchasing", Quantity, "unit(s) at a price of             ${:,.2f}".format(Price), "per unit.")
    print("The total price of this purchace will be: ${:,.2f}".format(Actual_Price))
    totalactprice = totalactprice + Actual_Price
    response = input("Do you want to calculate another item? (Y/N): ")
  else:
    print("Your total order cost will be: ${:,.2f}".format(totalactprice))
main()