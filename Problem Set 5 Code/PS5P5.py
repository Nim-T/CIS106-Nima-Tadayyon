Surname = input("What is your last name? ")
NumOfDependents = int(input("How many dependents do you have? "))
GrossIncome = float(input("What is your gross income? "))
AGI = GrossIncome - (NumOfDependents * 12000)
if(AGI > 50000): TaxRate = 0.20
else: TaxRate = 0.10
IncomeTax = AGI * TaxRate
if(IncomeTax < 0): IncomeTax = 100
print("The", Surname, "family has a gross income of $", GrossIncome, "and", NumOfDependents, "dependents.")
print("This makes their AGI: $", AGI, "and their income tax: $", IncomeTax)