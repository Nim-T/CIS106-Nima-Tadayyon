
class Employee:
  def IsManager(self):
    return False
    
  def __init__(self, first, last, pay, rate):
    self.first = first
    self.last = last
    self.pay = pay
    self.rate = rate
    self.email = first + '.' + last + '@company.com'

  def get_bonus(self, pay):
    bonus = float(self.rate) * float(self.pay)
    return bonus

class Manager(Employee):
  def IsManager(self):
    return True

  def get_bonus(self, pay):
    bonus = float(self.pay) * 0.4 
    return bonus

emp11 = Employee('Frank', 'Alvino',60000.00, 0.20)
emp12 = Manager('Jim', 'Jones', 100000.00, 0.00)
emp13 = Employee('Joseph', 'Sesto',75000.00, 0.15)
emp14 = Manager('Carmen', 'Alfonso', 130000.00, 0.00)
bonus11 = emp11.get_bonus(0)
bonus12 = emp12.get_bonus(0)
bonus13 = emp13.get_bonus(0)
bonus14 = emp14.get_bonus(0)

print("\n=============\n")

print("=========\n", emp11.email, "\n=========\n")
print("First name: ",emp11.first, "\n=========\n")
print("Surname: ",emp11.last, "\n=========\n")
print("Employee is a manager: ",emp11.IsManager(), "\n=========\n")
print("Salary: ${:,.2f}".format(emp11.pay), "\n=========\n")
print("Bonus: ${:,.2f}".format(bonus11), "\n=========\n")

print("\n=============\n")

print("=========\n", emp12.email, "\n=========\n")
print("First name: ",emp12.first, "\n=========\n")
print("Surname: ",emp12.last, "\n=========\n")
print("Employee is a manager: ",emp12.IsManager(), "\n=========\n")
print("Salary: ${:,.2f}".format(emp12.pay), "\n=========\n")
print("Bonus: ${:,.2f}".format(bonus12), "\n=========\n")

print("\n=============\n")

print("=========\n", emp13.email, "\n=========\n")
print("First name: ",emp13.first, "\n=========\n")
print("Surname: ",emp13.last, "\n=========\n")
print("Employee is a manager: ",emp13.IsManager(), "\n=========\n")
print("Salary: ${:,.2f}".format(emp13.pay), "\n=========\n")
print("Bonus: ${:,.2f}".format(bonus13), "\n=========\n")

print("\n=============\n")

print("=========\n", emp14.email, "\n=========\n")
print("First name: ",emp14.first, "\n=========\n")
print("Surname: ",emp14.last, "\n=========\n")
print("Employee is a manager: ",emp14.IsManager(), "\n=========\n")
print("Salary: ${:,.2f}".format(emp14.pay), "\n=========\n")
print("Bonus: ${:,.2f}".format(bonus14), "\n=========\n")