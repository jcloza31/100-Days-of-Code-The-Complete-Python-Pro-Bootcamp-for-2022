student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    # print(student_scores[student])
    student_score = student_scores[student]
    scoring_bracket = ""
    if student_score >= 91:
        scoring_bracket = "Outstanding"
    elif student_score >= 81:
        scoring_bracket = "Exceeds Expectations"
    elif student_score >= 71:
        scoring_bracket = "Acceptable"
    else:
        scoring_bracket = "Fail"
    student_grades[student] = scoring_bracket

# 🚨 Don't change the code below 👇
print(student_grades)
