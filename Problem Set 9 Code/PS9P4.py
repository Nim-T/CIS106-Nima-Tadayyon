def PayRate(Code,Hours):
  if Code.upper() == "L":
    Rate = 25.00
    print("Job code entered as: 'L'. \t Rate of pay: $25.00/hr.")
  elif Code.upper() == "A":
    Rate = 30.00
    print("Job code entered as: 'A'. \t Rate of pay: $30.00/hr.")
  elif Code.upper() == "J":
    Rate = 50.00
    print("Job code entered as: 'J'. \t Rate of pay: $50.00/hr.")
  else:
    print("Job code not found, please run the program again.")
    Rate = 0.00
  if Hours > 40:
     PayRate = (40 * Rate) + (Hours - 40) * Rate * 1.5
  else:
     PayRate = Hours * Rate
  return PayRate

def Main():
  count = 0
  SumGross = 0
  run = input("Do you wish to run the Payroll calculator? (Y/N): ")
  while run.upper() == "Y":
    print("Payroll Calculator")
    print("===================")
    Surname = input("Enter employee's last name: ")
    Code = input("Enter job code (L, A, or J): ")
    Hours = float(input("Enter hours worked: "))
    GrossPay = PayRate(Code,Hours)
    count = count + 1
    SumGross = SumGross + GrossPay
    print(Surname, ", earned $", format(GrossPay, ',.2f'), "this week.")
    run = input("Do you wish to run the Payroll calculator again? (Y/N): ")
  else: print("Total number of employees entered: ", count, "\nTotal gross pay: $", format(SumGross, ',.2f'))
Main()