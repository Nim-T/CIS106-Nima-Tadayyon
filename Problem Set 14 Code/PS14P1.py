
class Employee:
  def __init__(self, first, last, pay, rate):
    self.first = first
    self.last = last
    self.pay = pay
    self.rate = rate
    self.email = first + '.' + last + '@company.com'

  def get_bonus(self, rate):
    bonus = float(self.rate) * float(self.pay)
    return bonus

emp11 = Employee('Frank', 'Alvino',60000.00, 0.20)
bonus = emp11.get_bonus(0)

print("=========\n", emp11.email, "\n=========\n")
print("First name: ",emp11.first, "\n=========\n")
print("Surname: ",emp11.last, "\n=========\n")
print("Salary: ${:,.2f}".format(emp11.pay), "\n=========\n")
print("Bonus: ${:,.2f}".format(bonus), "\n=========\n")

