import datetime
time = datetime.datetime.now()
tax = 0.07
total = 0

def compTotal(qty, price):
  stotal = qty * price
  global total
  total = stotal + (stotal * tax)
  return stotal, total

def Main():
  run = input("Do you want to run the program? (y/n): ").strip().upper()
  while run[0] == "Y":
    price = float(input("Enter the price of the item: "))
    qty = int(input("Enter the quantity of the item: "))
    stotal, total = compTotal(qty, price)
    print("==============\n")
    print(f"\tSubtotal: ${stotal:.2f}")
    print("\tTax: ${:,.2f}".format(stotal * tax))
    print(f"\tTotal: ${total:.2f} \n")
    print("==============\n")
    run = input("Do you want to run the program again? (y/n): ").strip().upper()
  else:
    print("\nEnd at:",time.strftime("%c"))
    print("\tThank you for using this program!")
    


Main()




