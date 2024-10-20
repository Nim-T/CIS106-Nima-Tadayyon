def MPG(miles, gallons):
  MPG = miles / gallons
  return MPG

def Main():
  count = 0
  run = input("Do you wish to run this program? (Y/N): ")
  while run.upper() == "Y":
    Destination = input("Enter your destination: ")
    miles = float(input("Enter the miles driven: "))
    gallons = float(input("Enter the gallons used: "))
    MilesPerGallon = MPG(miles, gallons)
    print("Traveling to", Destination,", you traveled", miles, "miles, at {:.2f}".format(MilesPerGallon), "MPG")
    count = count + 1
    run = input("Do you wish to run the program again? (Y/N): ")
  else: print("You've traveled to", count, "cities!")
Main()