Aplliance = input("Please enter name of appliance you are purchasing ")
CostOfAppl = float(input("Please enter appliance price: "))
if CostOfAppl > 1000.01: Warantee = 0.1
else: Warantee = 0.05
WarrCost = CostOfAppl * Warantee
Total = CostOfAppl + WarrCost
print("The product;", Aplliance, "costs $", CostOfAppl, "with a warantee of $", WarrCost)
print("The total cost is $", Total)