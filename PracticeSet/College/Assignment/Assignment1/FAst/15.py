# Write a python program to calculate the sum of n natural numbers.


# Python program to calculate sum of n natural numbers using for loop

n = int(input("Enter a positive integer n: "))

sum_n = 0
for i in range(1, n + 1):
    sum_n = sum_n + i

print("Sum of first", n, "natural numbers is:", sum_n)
