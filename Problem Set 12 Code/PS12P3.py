f = open("PS12P3txt.txt", "r")
Surnames = []
Exam_Scores = []
for line in f:
  line = line.strip()
  if line:
    Surnames.append(line)
    Exam_Scores.append(int(f.readline()))
f.close()

def list_surnames(Surnames,Exam_Scores):
  for index in range(len(Surnames)):
    print("==============")
    print("\tLast Name: ",Surnames[index], "\n\tExam Score: ", Exam_Scores[index],"%")
    print("==============\n")

def reverse_surnames(Surnames,Exam_Scores):
  for index in reversed(range(len(Surnames))):
    print("==============")
    print("\tLast Name: ",Surnames[index], "\n\tExam Score: ",Exam_Scores[index],"%")
    print("==============\n")

def high_low_scores(Surnames,Exam_Scores):
  highest_score = max(Exam_Scores)
  highest_score_index = Exam_Scores.index(highest_score)
  highest_surname = Surnames[highest_score_index]
  lowest_score = min(Exam_Scores)
  lowest_score_index = Exam_Scores.index(lowest_score)
  lowest_surname = Surnames[lowest_score_index]
  return highest_score, highest_surname, lowest_score, lowest_surname
    


def Main():
  list_surnames(Surnames,Exam_Scores)
  print("\tLast names and scores in reverse order: \n")
  reverse_surnames(Surnames,Exam_Scores)
  highest_score, highest_surname, lowest_score, lowest_surname = high_low_scores(Surnames,Exam_Scores)
  print("==============")
  print(highest_surname, "recieved the highest score of", highest_score,"%")
  print(lowest_surname, "recieved the lowest score of", lowest_score,"%")
  print("==============")

  
  

    
  
  


Main()
    
  