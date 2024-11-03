import datetime
time = datetime.datetime.now()

def compCommission(sales):
    Comm = sales * 0.1 if sales > 100000 else sales * 0.05
    Target = sales + (sales * 0.05)
    return Comm, Target

def Main():
  run = input("Do you want to run the program? (y/n): ").strip().upper()
  while run[0] == "Y":
    surname = input("Enter employee's last name: ")
    sales = float(input("Enter sales made this year: "))
    Comm, Target = compCommission(sales)
    print("==============")
    print(surname,"made ${:,.2f}".format(sales),"in sales this year, and will receive a commission of ${:,.2f}".format(Comm))
    print("\nNext year's target will be ${:,.2f}".format(Target))
    print("==============")
    run = input("\nDo you want to run the program again? (y/n): ").strip().upper()
  else:
    print("\nEnd at:", time.strftime("%c"))
    print("\tThank you for using the program!")

Main()
    


