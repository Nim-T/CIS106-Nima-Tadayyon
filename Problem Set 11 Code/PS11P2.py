def compAvgTotal(score1,score2,score3):
  Avg = (score1 + score2 + score3)/3
  Total = score1 + score2 + score3
  return Avg, Total

def Main():
  run = input("Do you want to run the program? (y/n): ").strip().upper()
  while run[0] == "Y":
    Surname = input("Enter student's last name: ")
    score1 = float(input("Enter score on exam 1: "))
    score2 = float(input("Enter score on exam 2: "))
    score3 = float(input("Enter score on exam 3: "))
    Avg, Total = compAvgTotal(score1,score2,score3)
    print("=============")
    print(Surname, "recieved a combined exam score of:", Total,"points.")
    print("Their average exam score is: {:.1f}%.".format(Avg))
    print("=============\n")
    run = input("Do you want to run the program? (y/n): ").strip().upper()
  else:
    print("\nThank you for using the program.")
    
  

Main()

