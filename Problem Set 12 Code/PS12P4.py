f = open("PS12P4txt.txt", "r")
Surnames = []
BattingAvg = []
for line in f:
  line = line.strip()
  if line:
    Surnames.append(line)
    BattingAvg.append(float(f.readline()))
f.close()

def list_surnames(Surnames,BattingAvg):
  for index in range(len(Surnames)):
    print("==============")
    print("\tLast Name: ",Surnames[index], "\n\tBatting Average: ", BattingAvg[index],)
    print("==============\n")

def name_search(Surnames,Search):
  with open("PS12P4txt.txt", "r") as f:
    line = f.readline()
    while line:
      if Search.strip().upper() in line.strip().upper():
        batting_avg = float(f.readline().strip())
        return batting_avg
      line = f.readline()
  return None


def Main():
  list_surnames(Surnames,BattingAvg)
  print("\n=====================\n")
  Search = input("Search for a player by last name: ")
  while Search.strip().upper() != "QUIT":
    batting_avg = name_search(Surnames,Search)
    print("\n\t",Search, "has a batting average of:",batting_avg)
    print("\n=====================\n")
    Search = input('Enter another player or type "QUIT" to quit: ')
  else:
    print("\nThank you for using the program!")
  
    
      
 


Main()
    
  