# Python program to calculate grades of a student

# Taking marks as input
marks = float(input("Enter the student's marks (out of 100): "))

# Grade calculation
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Displaying result
print(f"Marks: {marks}")
print(f"Grade: {grade}")
