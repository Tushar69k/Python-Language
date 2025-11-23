# TUSHAR 

# Write a Python program using recursive function to display the Fibonacci series up to given number n.
print("Normal Function")

n = int(input("Enter how many terms: "))

a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


print("Recursive Function")

# Recursive function to find nth Fibonacci number
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Function to print Fibonacci series up to n terms
def print_fibonacci_series(n):
    print("Fibonacci Series:")
    for i in range(n):
        print(fibonacci(i), end=" ")

# Driver code
n = int(input("Enter the number of terms: "))
print_fibonacci_series(n)
