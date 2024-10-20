def Tuition(Hours,Code):
  if Code.upper() == "I":
    CPC = 250
  elif Code.upper() == "O":
    CPC = 550
  else:
    print("Error, please enter a valid student code.")
    CPC = 0
  Total = Hours * CPC
  return Total

def Main():
  count = 0
  sum = 0
  run = input("do you wish to run this program? (Y/N): ")
  while run.upper() == "Y":
    count = count + 1
    Surname = input("Enter the student's last name: ")
    Hours = float(input("Enter the number of credit hours: "))
    Code = input("Enter the student's code (I or O): ")
    Total = Tuition(Hours,Code)
    print(Surname, "owes ${:,.2f}".format(Total), "in tuition fees.")
    sum = sum + Total
    run = input("do you wish to run this program again? (Y/N): ")
  else: print("Total number of students: ", count, "Total tuition fees: ${:,.2f}".format(sum))
Main()