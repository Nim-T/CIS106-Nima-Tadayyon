# Problem 1
list1 = []
listamm = int(input("enter number of items in list: "))
for i in range(listamm):
  list1.append(int(input("enter item: ")))
print("======P1======\n")
print(list1)
print("======P2======\n")
# Problem 2
list1[0] = 99
print(list1)
print("======P3======\n")
# Problem 3
index = list1.index(99)
list1[index] = 100
print(list1)
print("======P4======\n")
# Problem 4
list2 = []
for i in range(500, 901, 100):
  list2.append(i)
print(list2)
list1.extend(list1 + list2)
print(list1)
print("======P5======\n")
# Problem 5
list1.remove(800)
print(list1)
print("======P6======\n")
# Problem 6
list1.remove(list1[2])
print(list1)
print("======P8======\n")
# Problem 7
grades = ["A", "B", "C", "A", "A", "C"]
# Problem 8
print("Number of 'A' grades: ", grades.count("A"))
print("======P9======\n")
# Problem 9
print("Position of 'B' in list: ", grades.index("B"))
print("======P10======\n")
# Problem 10
if "F" in grades:
  print("Position of 'F' in list: ", grades.index("F"))
else: 
  print("F is not in the list")
print("======P11======\n")
# Problem 11
list2.clear()
print("list2: ",list2)
print("======P12======\n")
# Problem 12
del list2
try:
  print(list2)
except NameError:
  print("list2 does not exist")
print("======P14======\n")
# Problem 13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
# Problem 14
players.sort()
print("players in alphabetical order: ",players)
print("======P15======\n")
# Problem 15
players2 = players.copy()
print(players2)
print("======P16======\n")
#Problem 16
players2.reverse()
print("Players: ",players)
print("\nPlayers reversed: ",players2)