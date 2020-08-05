# Grades

print("Enter the marks scored in")
writtenTest = float(input("Written test: "))
labExams = float(input("Lab exams: "))
Assignments = float(input("Assignments: "))

grade = (writtenTest*70)/100 + (labExams*20)/100 + (Assignments*10)/100
print("Grade of the student is", grade)
