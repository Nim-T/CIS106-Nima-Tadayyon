def BattingAvg(Hits, AtBats):
  BattingAvg = Hits / AtBats
  return BattingAvg

def Main():
  count = 0
  run = input("Do you want to run the program? (y/n): ")
  while run.upper() == "Y":
    Surname = input("Enter the player's last name: ")
    AtBats = int(input("Enter the number times player was at bat: "))
    Hits = int(input("Enter the number of hits: "))
    Batting_Avg = BattingAvg(Hits, AtBats)
    print(Surname,"has a batting Average: {:.3f}".format(Batting_Avg))
    count = count + 1
    run = input("Do you want to enter another player? (Y/N): ")
  else: 
    print("Totally players entered: ", count) 
Main()  