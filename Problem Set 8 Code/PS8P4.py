f = open("PS8P4txt.txt", "r")
item = f.readline()
SumExt = 0
Orders = 0
while item != "":
  Quantity = int(f.readline())
  Price = float(f.readline())
  ExtPrice = Quantity * Price
  SumExt = SumExt + ExtPrice
  Orders = Orders + 1
  print("Item: ", item)
  print("Quantity: ", Quantity)
  print("Price per Item: ${:,.2f}".format(Price))
  print("Extended Price: ${:,.2f}".format(ExtPrice), "\n\t")
  item = f.readline()
f.close()
Avg = SumExt / Orders
print("A total of" , Orders , "items were purchased. Totaling at: ${:,.2f}.".format(SumExt))
print("The average price per item was: ${:,.2f}.".format(Avg))