def WallSquarFootage(Length, Width, Height):
  SquareFootage = (2 * (Length * Height)) + (2 * (Width * Height)) 
  return SquareFootage

def GallonsOfPaint(SquareFootage):
  WallGallonsNeeded = SquareFootage / 50
  return WallGallonsNeeded

def CeilingArea(Length, Width):
  CeilingsArea = Length * Width
  return CeilingsArea

def GallonsOfVarnish(CeilingsArea):
  GallOfVarnish = CeilingsArea / 50
  return GallOfVarnish

def Main():
  run = input("Would you like to run this program? (y/n): \n")
  while run.upper() == "Y":
    Length = float(input("Enter the length of the room(ft.): "))
    Width = float(input("Enter the width of the room(ft.): "))
    Height = float(input("Enter the height of the room(ft.): "))
    SquareFootage = float(WallSquarFootage(Length, Width, Height))
    WallGallonsNeeded = float(GallonsOfPaint(SquareFootage)) 
    CeilingsArea = float(CeilingArea(Length, Width))
    GallOfVarnish = float(GallonsOfVarnish(CeilingsArea))
    print("The wall square footage of the room is: " + str(SquareFootage), "ft.\n")
    print("The number of gallons of paint needed is: " + str(WallGallonsNeeded), "\n")
    print("The ceiling/floor area is: " + str(CeilingsArea), "ft.^2 \n")
    print("The number of gallons of varnish/ceiling paint needed is: " + str(GallOfVarnish), "\n")
    print("=====================")
    run = input("Would you like to run this program again? (y/n): \n")
  else:
    print("\nThank you for using this program.")

Main()
