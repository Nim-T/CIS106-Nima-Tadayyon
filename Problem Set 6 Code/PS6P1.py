Widgets = int(input("Please enter quantity of widgets"))
if Widgets >= 10000: Price = 10
elif Widgets >= 5000: Price = 20
else: Price = 30
ExtendedPrice = Widgets * Price
Tax = 0.07 * ExtendedPrice
Total = ExtendedPrice + Tax
print("Subtotal: ${:,.2f}".format(ExtendedPrice)+"\t Tax: ${:,.2f}".format(Tax)+"\t Total: ${:,.2f}".format(Total))