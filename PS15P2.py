class Car:
  def __init__(self, make, model, sticker):
    self.make = make
    self.model = model
    self.sticker = sticker
    self.discount = self.sticker * 0.90

class SportsCar(Car):
  def __init__(self, make, model, sticker):
    super().__init__(make, model, sticker)
    self.wheels = 0
    self.engine = 0
    self.interior = 0

  def set_wheels(self, get_wheels):
    if get_wheels == "Y":
      self.wheels = 1000.00

  def set_engine(self, get_engine):
    if get_engine == "Y":
      self.engine = 3000.00

  def set_interior(self, get_interior):
    if get_interior == "Y":
      self.interior = 2000.00

  def get_UpTotal(self):
    UpTotal = self.discount + self.wheels + self.engine + self.interior
    return UpTotal


vehicle1 = Car('Honda', 'Accord', 35000.00)
print("\n=======\nCar 1 Details:\n")
print(f"Make: {vehicle1.make}\nModel: {vehicle1.model}\nSticker Price: ${vehicle1.sticker}\nDiscount Price: ${vehicle1.discount}\n")


vehicle2 = Car('Toyota', 'Tundra', 65000.00)
print("\n=======\nCar 2 Details:\n")
print(f"Make: {vehicle2.make}\nModel: {vehicle2.model}\nSticker Price: ${vehicle2.sticker}\nDiscount Price: ${vehicle2.discount}\n")


vehicle3 = SportsCar('Toyota', 'Supra', 51000.00)

vehicle3.set_wheels("Y")

vehicle3.set_engine("Y")

vehicle3.set_interior("N")

print("\n=======\nSportsCar 1 Details:\n")
print(f"Make: {vehicle3.make}\nModel: {vehicle3.model}\nSticker Price: ${vehicle3.sticker}\nUpgraded and discounted Price: ${vehicle3.get_UpTotal()}\n")


vehicle4 = SportsCar('Nissan', 'Skyline', 75000.00)

vehicle4.set_wheels("N")

vehicle4.set_engine("Y")

vehicle4.set_interior("N")

print("\n=======\nSportsCar 2 Details:\n")
print(f"Make: {vehicle4.make}\nModel: {vehicle4.model}\nSticker Price: ${vehicle4.sticker}\nUpgraded and discounted Price: ${vehicle4.get_UpTotal()}\n")
