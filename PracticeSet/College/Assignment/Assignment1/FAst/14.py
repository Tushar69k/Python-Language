# Write a python program to check whether a number is Armstrong or not.

# Python program to check Armstrong number

# Taking input
num = int(input("Enter a number: "))

# Converting number to string to count digits
num_str = str(num)
n = len(num_str)

# Calculating sum of powers of digits
sum_of_powers = sum(int(i) ** n for i in num_str)

# Checking Armstrong condition
if num == sum_of_powers:
    print(num, "is an Armstrong number ✅")
else:
    print(num, "is not an Armstrong number ❌")



# or 




# Simple Python program to check Armstrong number

num = int(input("Enter a number: "))

# Count digits
n = len(str(num))

# Copy original number
temp = num
sum_of_powers = 0

# For loop using digits
for digit in str(num):
    sum_of_powers = sum_of_powers + int(digit) ** n

# Check Armstrong condition
if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
