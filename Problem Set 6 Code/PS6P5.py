Surname = input("Please enter employee's last name: ")
JobLvl = int(input("Enter the employee's job level: "))
Salary = float(input("Enter the employee's salary: "))
if JobLvl >= 10: BonusRate = 0.25
elif JobLvl >= 5: BonusRate = 0.2
else: BonusRate = 0.1
Bonus = Salary * BonusRate
print(" The employee:",Surname,"will recieve a bonus of ${:,.2f}".format(Bonus), "this year!")