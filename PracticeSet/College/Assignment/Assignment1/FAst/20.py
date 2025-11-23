# Python program to count digits using string

num = int(input("Enter a number: "))

num_digits = len(str(abs(num)))  # use abs to handle negative numbers

print("Number of digits in", num, "is", num_digits)



# Python program to count digits in a number

num = int(input("Enter a number: "))

count = 0
temp = abs(num)  # use abs to handle negative numbers

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp = temp // 10
        count += 1

print("Number of digits in", num, "is", count)
