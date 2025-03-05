#Control flow for grading students marks

#Asks user to input name and marks
studName = str(input("Enter student name:"))
regno = str(input("Enter Registration number:"))
eng = int(input("Enter marks in English:"))
kis = int(input("Enter marks in Kiswahili:"))
math = int(input("Enter marks in Maths:"))
physics = int(input("Enter marks in Physics:"))

#Computation
sum = eng + kis + math + physics
avg = sum/4

#Outputs name for the student name entered and registration number
print("REPORT FORM")
print("Student name:", studName)
print("Reg NO:", regno)
print("Total Marks -", sum)
print("Average -", avg)

#Grading system  based on marks
if avg >= 70:
    print("Grade: A (Excellent)")
elif avg >= 60:
    print("Grade: B (Good)")
elif avg >= 50:
    print("Grade: C (Satisfactory)")
elif avg >= 40:
    print("Grade: D (Pass)")
else:
    print("Grade: E (Fail)")