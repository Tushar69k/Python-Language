# Write a python program to find the sum of digits of a given number.

num = int(input("Enter Num : "))

nums = str(num)

count = 0 

for digit in nums :
    count += int(digit)

print("Sum : " ,count)    


# Python program to find sum of digits of a number

nums = int(input("Enter a number: "))

temp = abs(nums)  # handle negative numbers
sum_digits = 0

while temp > 0:
    digit = temp % 10      # get the last digit
    sum_digits += digit    # add it to sum
    temp = temp // 10      # remove the last digit

print("Sum of digits of", nums, "is", sum_digits)
