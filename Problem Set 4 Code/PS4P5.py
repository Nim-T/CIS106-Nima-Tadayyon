Fixed_Cost = float(input("Enter the fixed cost: "))
PPU = float(input("Enter the price per unit: "))
CPU = float(input("Enter the cost per unit: "))
Break_Even = Fixed_Cost / (PPU - CPU)
print("With a fixed cost of", Fixed_Cost,", The break even point is;", Break_Even)