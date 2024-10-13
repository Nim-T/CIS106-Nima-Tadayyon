f = open("PS8P5txt.txt", "r")
lastname = f.readline().strip()
TotalTuition = 0
Count = 0
while lastname != "":
  code = f.readline().strip()
#"CPC" = Cost per Credit
  CPC = 500 if code == "O" else 250
  credits = f.readline().strip()
  Tuition = int(credits) * int(CPC)
  print(lastname, "has taken", credits, "credit hours and owes ${:,.2f}.".format(Tuition), "\n")
  TotalTuition = TotalTuition + Tuition
  Count = Count + 1
  lastname = f.readline().strip()
f.close()
print(Count, "students paid a total of ${:,.2f}".format(TotalTuition), "in tuition fees.")
  