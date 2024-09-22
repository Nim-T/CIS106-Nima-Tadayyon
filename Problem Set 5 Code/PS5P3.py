CostPerBook = float(input("Enter the book's price:"))
NumOfBooks = int(input("Enter the number of books you'd like to purchase:"))
OrderCost = CostPerBook * NumOfBooks
if(OrderCost > 50.01): Shipping = 0 
else: Shipping = 25
OrderTotal = OrderCost + Shipping
print("Your order will cost;", OrderCost, "With a shipping cost of;", Shipping)
print("Your total will be;", OrderTotal)