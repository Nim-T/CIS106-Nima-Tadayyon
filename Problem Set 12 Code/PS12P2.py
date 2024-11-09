Surnames = ["Smith", "Adams", "Goodman", "Jones", "Brown", "Williams", "Miller", "Davis", "Thomas", "Taylor"]
Exam_Scores = [98, 56, 79, 45, 65, 82, 90, 100, 67, 43]


def list_surnames(Surnames,Exam_Scores):
  for index in range(len(Surnames)):
    print("==============")
    print("\tLast Name: ",Surnames[index], "\n\tExam Score: {:.1f}%".format(Exam_Scores[index]))
    print("==============\n")

def reverse_surnames(Surnames,Exam_Scores):
  for index in reversed(range(len(Surnames))):
    print("==============")
    print("\tLast Name: ",Surnames[index], "\n\tExam Score: {:.1f}%".format(Exam_Scores[index]))
    print("==============\n")



def Main():
  list_surnames(Surnames,Exam_Scores)
  print("\tLast names and scores in reverse order: \n")
  reverse_surnames(Surnames,Exam_Scores)


Main()
