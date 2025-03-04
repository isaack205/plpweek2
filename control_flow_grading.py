#Control flow for grading students marks

#Asks user to input name and marks
studname = str(input("Enter student name:"))
marks = float(input("Enter student marks(0-100):"))

#Outputs name for the student name entered
print("Student name:", studname)

#Grading system  based on marks
if marks >= 70:
    print("Grade: Excellent")
elif marks >= 60:
    print("Grade: Good")
elif marks >= 50:
    print("Grade: Satisfactory")
elif marks >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")