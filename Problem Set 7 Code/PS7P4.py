run = input("Would you like to run this program? (y/n): ")
NumEmpl = 0
SumGross = 0
run = run.lower()
if run == "y":
  while True:
   Surname = input("Please enter employee's last name: ")
   NumEmpl = NumEmpl + 1
   Hours = int(input("Please enter hours worked: "))
   Rate = float(input("Please enter hourly rate: "))
   if Hours > 40:
     Gross = (40 * Rate) + (Hours - 40) * Rate * 1.5
   else:
     Gross = Hours * Rate
     SumGross = SumGross + Gross
   print(Surname, "has worked", Hours, "hours, and has earned ${:.2f}".format(Gross))
   run = input("Would you like to run this program again? (y/n): ")
   if run.lower() == "n":
    break
else: print("program stopped") + exit()
AvgPay = SumGross / NumEmpl
print("Program stopped, Data for", NumEmpl, "has been entered.")
print("The sum gross pay of the employees is ${:.2f}".format(SumGross))
print("The average gross pay of the employees is ${:.2f}".format(AvgPay))