PartNum = int(input("Enter part number: "))
Quantity = int(input("Enter quantity: "))
if PartNum == 10 or PartNum == 55: UnitCost = 1.00
elif PartNum == 99: UnitCost = 2.00
elif PartNum == 80 or PartNum == 70: UnitCost = 3.00
else: UnitCost = 5.00
Total = Quantity * UnitCost
print("Part Number: ", PartNum, "\nQuantity: ", Quantity,)
print("Cost Per Unit: ${:,.2f}".format(UnitCost))
print("Total: ${:,.2f}".format(Total))