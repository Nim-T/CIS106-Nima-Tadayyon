import datetime
time = datetime.datetime.now()

def compScore(score1,score2,score3,Handicap):
  Avg = (score1 + score2 + score3) / 3
  HandicapAvg = Avg + Handicap
  return Avg, HandicapAvg

def Main():
  run = input("Would you like to run the program? (y/n): ").strip().upper()
  while run[0] == "Y":
    surname = input("Enter player's last name: ")
    score1 = int(input("\tEnter score 1: "))
    score2 = int(input("\tEnter score 2: "))
    score3 = int(input("\tEnter score 3: "))
    Handicap = int(input("Enter handicap pts.(If N/A enter 0): "))
    Avg, HandicapAvg = compScore(score1,score2,score3,Handicap)
    if HandicapAvg == Avg:
      print("======================\n")
      print(surname,"didn't receive a handicap, they bowled an average score of: {:.0f}".format(Avg),"pts.\n")
      print("======================\n")
    else:
      print("======================\n")
      print(surname,"bowled an average score of: {:.0f}".format(Avg),"pts.")
      print("\tTheir handicap average is: {:.0f}".format(HandicapAvg),"pts.\n")
      print("======================\n")     
    run = input("Would you like to run the program again? (y/n):").strip().upper()
  else:
    print("\nEnd at:",time.strftime("%c"))
    print("\tThank you for using the program.")


Main()




