class Student:
  def __init__(self, first, last, code, credit):
      self.first = first
      self.last = last
      self.code = code
      self.credit = credit
      self.fullname = self.first + ' ' + self.last

  def comptuition(self, code, credit):
      if code.upper() == "I":
          tuition = 250.00 * credit
      elif code.upper() == "O": 
          tuition = 500.00 * credit
      else: 
          tuition = 0.00
          print("\nInvalid District code, please try again.\n(Tuition set to $0.00)\n")
      return tuition


first = input("Enter student's first name: ")
last = input("Enter student's last name: ")
code = input("Enter student's district code (I/O): ")
credit = int(input("Enter number of credit hours student has enrolled in: "))
  
student1 = Student(first, last, code, credit) 
  
tuition = student1.comptuition(code, credit)
print("===========\n")
print(student1.fullname, "owes a total tuition of ${:,.2f}".format(tuition))