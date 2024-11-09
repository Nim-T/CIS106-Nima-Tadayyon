Surnames = ["Smith", "Adams", "Goodman", "Jones", "Brown", "Williams", "Miller", "Davis", "Thomas", "Taylor"]

def list_surnames(Surnames):
  for name in Surnames:
    print("Last Name: \n","\t",name)
    print("==============")

def reverse_surnames(Surnames):
  for name in reversed(Surnames):
    print("Last Name: \n","\t",name)
    print("==============")


def Main():
  list_surnames(Surnames)
  print("\n\tLast names in reverse order: \n")
  reverse_surnames(Surnames)

Main()
