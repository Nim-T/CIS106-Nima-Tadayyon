f = open("PS8P3txt.txt", "r")
lastname = f.readline()
sumbonus = 0
while lastname != "":
  salary = float(f.readline())
  if salary >= 100000:
    bonusrate = 0.20
  elif salary >= 50000:
    bonusrate = 0.15
  else: bonusrate = 0.10
  bonus = float(salary) * float(bonusrate)
  sumbonus = sumbonus + bonus
  print(lastname, "has a salary of: ${:,.2f}".format(salary)) 
  print("They'll recieve a bonus of ${:,.2f}".format(bonus), "this year!\n\t")
  lastname = f.readline()
f.close()
print("Sum of all bonuses is ${:,.2f}".format(sumbonus))