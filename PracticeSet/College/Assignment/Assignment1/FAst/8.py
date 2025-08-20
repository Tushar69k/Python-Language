# Write a python program to check whether a person is eligible for loan or not if he is
# having salary more than 50k and 3 years of experience.

# Python program to check loan eligibility

# Taking inputs
salary = float(input("Enter your monthly salary: "))
experience = int(input("Enter your work experience (in years): "))

# Checking loan eligibility
if salary > 50000 and experience >= 3:
    print("✅ You are eligible for the loan.")
else:
    print("❌ You are not eligible for the loan.")
