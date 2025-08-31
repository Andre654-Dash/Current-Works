print("Student Grade Calculator")
print("========================")

number_subjects = int(input("Enter number of Subjects: "))
subject_score = 0
print(f"Number of Subjects: {number_subjects}")
for i in range(1, number_subjects + 1):

    subject = int(input(f"Enter Score for Subject {i}: "))
    subject_score += subject
    if i != number_subjects + 1:
        continue
average = subject_score / number_subjects
if average >= 97 and average <= 100:
    gpa = 4.0
    grade = "A+"
elif average >= 93 and average <= 96:
    gpa = 4.0
    grade = "A"
elif average >= 90 and average <= 92:
    gpa = 3.7
    grade = "A-"
elif average >= 87 and average <= 89:
    gpa = 3.3
    grade = "B+"
elif average >= 83 and average <= 86:
    gpa = 3.0
    grade = "B"
elif average >= 80 and average <= 82:
    gpa = 2.7
    grade = "B_"
elif average >= 77 and average <= 79:
    gpa = 2.3
    grade = "C+"
elif average >= 73 and average <= 76:
    gpa = 2.0
    grade = "C"
elif average >= 70 and average <= 72:
    gpa = 1.7
    grade = "C-"
elif average >= 67 and average <= 69:
    gpa = 1.3
    grade = "D+"
elif average >= 63 and average <= 66:
    gpa = 1.0
    grade = "D"
elif average >= 60 and average <= 62:
    gpa = 0.7
    grade = "D-"
else:
    gpa = 0.0
    grade = "F"

print("--- Student Report ---")
print(f"Average: {round(average)}")
print(f"GPA: {gpa}")
print(f"Grade: {grade}")
