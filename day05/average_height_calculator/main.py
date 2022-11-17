# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
no_of_students = 0
total_student_heights = 0
for height in student_heights:
    no_of_students += 1
    total_student_heights += height

average_student_height = total_student_heights / no_of_students
print(round(average_student_height))




