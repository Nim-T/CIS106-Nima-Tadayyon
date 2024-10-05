run = input("Would you like to run this program? (y/n): ")
NumLoops = 0
run = run.lower()
if run == "y":
  while True:
    Surname = input("Enter student's last name ")
    Exam1 = float(input("Enter student's first exam score:  "))
    Exam2 = float(input("Enter student's second exam score: "))
    Avg = (Exam1 + Exam2) / 2
    print(Surname, "has an average of {:.2%}".format(Avg), "for the semester")
    NumLoops = NumLoops + 1
    run = input("Would you like to run this program again? (y/n): ")
    if run.lower() == "n":
      break
else: print("program stopped") + exit()
print("Program stopped," , NumLoops, "students processed")